# get-componentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifyuibuilder/get-component.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifyuibuilder/get-component.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [amplifyuibuilder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifyuibuilder/index.html#cli-aws-amplifyuibuilder) ]

# get-component

## Description

Returns an existing component for an Amplify app.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/amplifyuibuilder-2021-08-11/GetComponent)

## Synopsis

```
get-component
--app-id <value>
--environment-name <value>
--id <value>
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

`--app-id` (string)

The unique ID of the Amplify app.

`--environment-name` (string)

The name of the backend environment that is part of the Amplify app.

`--id` (string)

The unique ID of the component.

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

component -> (structure)

Represents the configuration settings for the component.

appId -> (string)

The unique ID of the Amplify app associated with the component.

environmentName -> (string)

The name of the backend environment that is a part of the Amplify app.

sourceId -> (string)

The unique ID of the component in its original source system, such as Figma.

id -> (string)

The unique ID of the component.

name -> (string)

The name of the component.

componentType -> (string)

The type of the component. This can be an Amplify custom UI component or another custom component.

properties -> (map)

Describes the componentâs properties. You canât specify `tags` as a valid property for `properties` .

key -> (string)

value -> (structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

children -> (list)

A list of the componentâs `ComponentChild` instances.

(structure)

A nested UI configuration within a parent `Component` .

componentType -> (string)

The type of the child component.

name -> (string)

The name of the child component.

properties -> (map)

Describes the properties of the child component. You canât specify `tags` as a valid property for `properties` .

key -> (string)

value -> (structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

children -> (list)

The list of `ComponentChild` instances for this component.

(structure)

A nested UI configuration within a parent `Component` .

componentType -> (string)

The type of the child component.

name -> (string)

The name of the child component.

properties -> (map)

Describes the properties of the child component. You canât specify `tags` as a valid property for `properties` .

key -> (string)

value -> (structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

events -> (map)

Describes the events that can be raised on the child component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.

key -> (string)

value -> (structure)

Describes the configuration of an event. You can bind an event and a corresponding action to a `Component` or a `ComponentChild` . A button click is an example of an event.

action -> (string)

The action to perform when a specific event is raised.

parameters -> (structure)

Describes information about the action.

type -> (structure)

The type of navigation action. Valid values are `url` and `anchor` . This value is required for a navigation action.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

url -> (structure)

The URL to the location to open. Specify this value for a navigation action.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

anchor -> (structure)

The HTML anchor link to the location to open. Specify this value for a navigation action.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

target -> (structure)

The element within the same component to modify when the action occurs.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

global -> (structure)

Specifies whether the user should be signed out globally. Specify this value for an auth sign out action.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

model -> (string)

The name of the data model. Use when the action performs an operation on an Amplify DataStore model.

id -> (structure)

The unique ID of the component that the `ActionParameters` apply to.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

fields -> (map)

A dictionary of key-value pairs mapping Amplify Studio properties to fields in a data model. Use when the action performs an operation on an Amplify DataStore model.

key -> (string)

value -> (structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

state -> (structure)

A key-value pair that specifies the state property name and its initial value.

componentName -> (string)

The name of the component that is being modified.

property -> (string)

The name of the component property to apply the state configuration to.

set -> (structure)

The state configuration to assign to the property.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

bindingEvent -> (string)

Binds an event to an action on a component. When you specify a `bindingEvent` , the event is called when the action is performed.

sourceId -> (string)

The unique ID of the child component in its original source system, such as Figma.

events -> (map)

Describes the events that can be raised on the child component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.

key -> (string)

value -> (structure)

Describes the configuration of an event. You can bind an event and a corresponding action to a `Component` or a `ComponentChild` . A button click is an example of an event.

action -> (string)

The action to perform when a specific event is raised.

parameters -> (structure)

Describes information about the action.

type -> (structure)

The type of navigation action. Valid values are `url` and `anchor` . This value is required for a navigation action.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

url -> (structure)

The URL to the location to open. Specify this value for a navigation action.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

anchor -> (structure)

The HTML anchor link to the location to open. Specify this value for a navigation action.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

target -> (structure)

The element within the same component to modify when the action occurs.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

global -> (structure)

Specifies whether the user should be signed out globally. Specify this value for an auth sign out action.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

model -> (string)

The name of the data model. Use when the action performs an operation on an Amplify DataStore model.

id -> (structure)

The unique ID of the component that the `ActionParameters` apply to.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

fields -> (map)

A dictionary of key-value pairs mapping Amplify Studio properties to fields in a data model. Use when the action performs an operation on an Amplify DataStore model.

key -> (string)

value -> (structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

state -> (structure)

A key-value pair that specifies the state property name and its initial value.

componentName -> (string)

The name of the component that is being modified.

property -> (string)

The name of the component property to apply the state configuration to.

set -> (structure)

The state configuration to assign to the property.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

bindingEvent -> (string)

Binds an event to an action on a component. When you specify a `bindingEvent` , the event is called when the action is performed.

sourceId -> (string)

The unique ID of the child component in its original source system, such as Figma.

variants -> (list)

A list of the componentâs variants. A variant is a unique style configuration of a main component.

(structure)

Describes the style configuration of a unique variation of a main component.

variantValues -> (map)

The combination of variants that comprise this variant. You canât specify `tags` as a valid property for `variantValues` .

key -> (string)

value -> (string)

overrides -> (map)

The properties of the component variant that can be overriden when customizing an instance of the component. You canât specify `tags` as a valid property for `overrides` .

key -> (string)

value -> (map)

key -> (string)

value -> (string)

overrides -> (map)

Describes the componentâs properties that can be overriden in a customized instance of the component. You canât specify `tags` as a valid property for `overrides` .

key -> (string)

value -> (map)

key -> (string)

value -> (string)

bindingProperties -> (map)

The information to connect a componentâs properties to data at runtime. You canât specify `tags` as a valid property for `bindingProperties` .

key -> (string)

value -> (structure)

Represents the data binding configuration for a component at runtime. You can use `ComponentBindingPropertiesValue` to add exposed properties to a component to allow different values to be entered when a component is reused in different places in an app.

type -> (string)

The property type.

bindingProperties -> (structure)

Describes the properties to customize with data at runtime.

model -> (string)

An Amplify DataStore model.

field -> (string)

The field to bind the data to.

predicates -> (list)

A list of predicates for binding a componentâs properties to data.

(structure)

Stores information for generating Amplify DataStore queries. Use a `Predicate` to retrieve a subset of the data in a collection.

or -> (list)

A list of predicates to combine logically.

(structure)

Stores information for generating Amplify DataStore queries. Use a `Predicate` to retrieve a subset of the data in a collection.

field -> (string)

The field to query.

operator -> (string)

The operator to use to perform the evaluation.

operand -> (string)

The value to use when performing the evaluation.

operandType -> (string)

The type of value to use when performing the evaluation.

and -> (list)

A list of predicates to combine logically.

(structure)

Stores information for generating Amplify DataStore queries. Use a `Predicate` to retrieve a subset of the data in a collection.

field -> (string)

The field to query.

operator -> (string)

The operator to use to perform the evaluation.

operand -> (string)

The value to use when performing the evaluation.

operandType -> (string)

The type of value to use when performing the evaluation.

field -> (string)

The field to query.

operator -> (string)

The operator to use to perform the evaluation.

operand -> (string)

The value to use when performing the evaluation.

operandType -> (string)

The type of value to use when performing the evaluation.

userAttribute -> (string)

An authenticated user attribute.

bucket -> (string)

An Amazon S3 bucket.

key -> (string)

The storage key for an Amazon S3 bucket.

defaultValue -> (string)

The default value to assign to the property.

slotName -> (string)

The name of a component slot.

defaultValue -> (string)

The default value of the property.

collectionProperties -> (map)

The data binding configuration for the componentâs properties. Use this for a collection component. You canât specify `tags` as a valid property for `collectionProperties` .

key -> (string)

value -> (structure)

Describes the configuration for binding a componentâs properties to data.

model -> (string)

The name of the data model to use to bind data to a component.

sort -> (list)

Describes how to sort the componentâs properties.

(structure)

Describes how to sort the data that you bind to a component.

field -> (string)

The field to perform the sort on.

direction -> (string)

The direction of the sort, either ascending or descending.

predicate -> (structure)

Represents the conditional logic to use when binding data to a component. Use this property to retrieve only a subset of the data in a collection.

or -> (list)

A list of predicates to combine logically.

(structure)

Stores information for generating Amplify DataStore queries. Use a `Predicate` to retrieve a subset of the data in a collection.

or -> (list)

A list of predicates to combine logically.

( â¦ recursive â¦ )

and -> (list)

A list of predicates to combine logically.

( â¦ recursive â¦ )

field -> (string)

The field to query.

operator -> (string)

The operator to use to perform the evaluation.

operand -> (string)

The value to use when performing the evaluation.

operandType -> (string)

The type of value to use when performing the evaluation.

and -> (list)

A list of predicates to combine logically.

(structure)

Stores information for generating Amplify DataStore queries. Use a `Predicate` to retrieve a subset of the data in a collection.

or -> (list)

A list of predicates to combine logically.

( â¦ recursive â¦ )

and -> (list)

A list of predicates to combine logically.

( â¦ recursive â¦ )

field -> (string)

The field to query.

operator -> (string)

The operator to use to perform the evaluation.

operand -> (string)

The value to use when performing the evaluation.

operandType -> (string)

The type of value to use when performing the evaluation.

field -> (string)

The field to query.

operator -> (string)

The operator to use to perform the evaluation.

operand -> (string)

The value to use when performing the evaluation.

operandType -> (string)

The type of value to use when performing the evaluation.

identifiers -> (list)

A list of IDs to use to bind data to a component. Use this property to bind specifically chosen data, rather than data retrieved from a query.

(string)

createdAt -> (timestamp)

The time that the component was created.

modifiedAt -> (timestamp)

The time that the component was modified.

tags -> (map)

One or more key-value pairs to use when tagging the component.

key -> (string)

value -> (string)

events -> (map)

Describes the events that can be raised on the component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.

key -> (string)

value -> (structure)

Describes the configuration of an event. You can bind an event and a corresponding action to a `Component` or a `ComponentChild` . A button click is an example of an event.

action -> (string)

The action to perform when a specific event is raised.

parameters -> (structure)

Describes information about the action.

type -> (structure)

The type of navigation action. Valid values are `url` and `anchor` . This value is required for a navigation action.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

url -> (structure)

The URL to the location to open. Specify this value for a navigation action.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

anchor -> (structure)

The HTML anchor link to the location to open. Specify this value for a navigation action.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

target -> (structure)

The element within the same component to modify when the action occurs.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

global -> (structure)

Specifies whether the user should be signed out globally. Specify this value for an auth sign out action.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

model -> (string)

The name of the data model. Use when the action performs an operation on an Amplify DataStore model.

id -> (structure)

The unique ID of the component that the `ActionParameters` apply to.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

fields -> (map)

A dictionary of key-value pairs mapping Amplify Studio properties to fields in a data model. Use when the action performs an operation on an Amplify DataStore model.

key -> (string)

value -> (structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

state -> (structure)

A key-value pair that specifies the state property name and its initial value.

componentName -> (string)

The name of the component that is being modified.

property -> (string)

The name of the component property to apply the state configuration to.

set -> (structure)

The state configuration to assign to the property.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

(structure)

Describes the configuration for all of a componentâs properties. Use `ComponentProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

then -> (structure)

The value to assign to the property if the condition is met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

else -> (structure)

The value to assign to the property if the condition is not met.

value -> (string)

The value to assign to the component property.

bindingProperties -> (structure)

The information to bind the component property to data at runtime.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

collectionBindingProperties -> (structure)

The information to bind the component property to data at runtime. Use this for collection components.

property -> (string)

The component property to bind to the data field.

field -> (string)

The data field to bind the property to.

defaultValue -> (string)

The default value to assign to the component property.

model -> (string)

The data model to use to assign a value to the component property.

bindings -> (map)

The information to bind the component property to form data.

key -> (string)

value -> (structure)

Describes how to bind a component property to form data.

element -> (string)

The name of the component to retrieve a value from.

property -> (string)

The property to retrieve a value from.

event -> (string)

An event that occurs in your app. Use this for workflow data binding.

userAttribute -> (string)

An authenticated user attribute to use to assign a value to the component property.

concat -> (list)

A list of component properties to concatenate to create the value to assign to this component property.

( â¦ recursive â¦ )

condition -> (structure)

The conditional expression to use to assign a value to the component property.

property -> (string)

The name of the conditional property.

field -> (string)

The name of a field. Specify this when the property is a data model.

operator -> (string)

The operator to use to perform the evaluation, such as `eq` to represent equals.

operand -> (string)

The value of the property to evaluate.

( â¦ recursive â¦ )( â¦ recursive â¦ )operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

operandType -> (string)

The type of the property to evaluate.

configured -> (boolean)

Specifies whether the user configured the property in Amplify Studio after importing it.

type -> (string)

The component type.

importedValue -> (string)

The default value assigned to the property when the component is imported into an app.

componentName -> (string)

The name of the component that is affected by an event.

property -> (string)

The name of the componentâs property that is affected by an event.

bindingEvent -> (string)

Binds an event to an action on a component. When you specify a `bindingEvent` , the event is called when the action is performed.

schemaVersion -> (string)

The schema version of the component when it was imported.