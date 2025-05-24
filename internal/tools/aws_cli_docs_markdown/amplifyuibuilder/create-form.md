# create-formÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifyuibuilder/create-form.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifyuibuilder/create-form.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [amplifyuibuilder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifyuibuilder/index.html#cli-aws-amplifyuibuilder) ]

# create-form

## Description

Creates a new form for an Amplify app.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/amplifyuibuilder-2021-08-11/CreateForm)

## Synopsis

```
create-form
--app-id <value>
--environment-name <value>
[--client-token <value>]
--form-to-create <value>
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

The unique ID of the Amplify app to associate with the form.

`--environment-name` (string)

The name of the backend environment that is a part of the Amplify app.

`--client-token` (string)

The unique client token.

`--form-to-create` (structure)

Represents the configuration of the form to create.

name -> (string)

The name of the form.

dataType -> (structure)

The type of data source to use to create the form.

dataSourceType -> (string)

The data source type, either an Amplify DataStore model or a custom data type.

dataTypeName -> (string)

The unique name of the data type you are using as the data source for the form.

formActionType -> (string)

Specifies whether to perform a create or update action on the form.

fields -> (map)

The configuration information for the formâs fields.

key -> (string)

value -> (structure)

Describes the configuration information for a field in a table.

label -> (string)

The label for the field.

position -> (tagged union structure)

Specifies the field position.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fixed`, `rightOf`, `below`.

fixed -> (string)

The field position is fixed and doesnât change in relation to other fields.

rightOf -> (string)

The field position is to the right of the field specified by the string.

below -> (string)

The field position is below the field specified by the string.

excluded -> (boolean)

Specifies whether to hide a field.

inputType -> (structure)

Describes the configuration for the default input value to display for a field.

type -> (string)

The input type for the field.

required -> (boolean)

Specifies a field that requires input.

readOnly -> (boolean)

Specifies a read only field.

placeholder -> (string)

The text to display as a placeholder for the field.

defaultValue -> (string)

The default value for the field.

descriptiveText -> (string)

The text to display to describe the field.

defaultChecked -> (boolean)

Specifies whether a field has a default value.

defaultCountryCode -> (string)

The default country code for a phone number.

valueMappings -> (structure)

The information to use to customize the input fields with data at runtime.

values -> (list)

The value and display value pairs.

(structure)

Associates a complex object with a display value. Use `ValueMapping` to store how to represent complex objects when they are displayed.

displayValue -> (structure)

The value to display for the complex object.

value -> (string)

The value to assign to the input field.

bindingProperties -> (structure)

The information to bind fields to data at runtime.

property -> (string)

The form property to bind to the data field.

field -> (string)

The data field to bind the property to.

concat -> (list)

A list of form properties to concatenate to create the value to assign to this field property.

(structure)

Describes the configuration for an input field on a form. Use `FormInputValueProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the input field.

bindingProperties -> (structure)

The information to bind fields to data at runtime.

property -> (string)

The form property to bind to the data field.

field -> (string)

The data field to bind the property to.

concat -> (list)

A list of form properties to concatenate to create the value to assign to this field property.

( â¦ recursive â¦ )

value -> (structure)

The complex object.

value -> (string)

The value to assign to the input field.

bindingProperties -> (structure)

The information to bind fields to data at runtime.

property -> (string)

The form property to bind to the data field.

field -> (string)

The data field to bind the property to.

concat -> (list)

A list of form properties to concatenate to create the value to assign to this field property.

(structure)

Describes the configuration for an input field on a form. Use `FormInputValueProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the input field.

bindingProperties -> (structure)

The information to bind fields to data at runtime.

property -> (string)

The form property to bind to the data field.

field -> (string)

The data field to bind the property to.

concat -> (list)

A list of form properties to concatenate to create the value to assign to this field property.

( â¦ recursive â¦ )

bindingProperties -> (map)

The information to bind fields to data at runtime.

key -> (string)

value -> (structure)

Represents the data binding configuration for a formâs input fields at runtime.You can use `FormInputBindingPropertiesValue` to add exposed properties to a form to allow different values to be entered when a form is reused in different places in an app.

type -> (string)

The property type.

bindingProperties -> (structure)

Describes the properties to customize with data at runtime.

model -> (string)

An Amplify DataStore model.

name -> (string)

The name of the field.

minValue -> (float)

The minimum value to display for the field.

maxValue -> (float)

The maximum value to display for the field.

step -> (float)

The stepping increment for a numeric value in a field.

value -> (string)

The value for the field.

isArray -> (boolean)

Specifies whether to render the field as an array. This property is ignored if the `dataSourceType` for the form is a Data Store.

fileUploaderConfig -> (structure)

The configuration for the file uploader field.

accessLevel -> (string)

The access level to assign to the uploaded files in the Amazon S3 bucket where they are stored. The valid values for this property are `private` , `protected` , or `public` . For detailed information about the permissions associated with each access level, see [File access levels](https://docs.amplify.aws/lib/storage/configureaccess/q/platform/js/) in the *Amplify documentation* .

acceptedFileTypes -> (list)

The file types that are allowed to be uploaded by the file uploader. Provide this information in an array of strings specifying the valid file extensions.

(string)

showThumbnails -> (boolean)

Specifies whether to display or hide the image preview after selecting a file for upload. The default value is `true` to display the image preview.

isResumable -> (boolean)

Allows the file upload operation to be paused and resumed. The default value is `false` .

When `isResumable` is set to `true` , the file uploader uses a multipart upload to break the files into chunks before upload. The progress of the upload isnât continuous, because the file uploader uploads a chunk at a time.

maxFileCount -> (integer)

Specifies the maximum number of files that can be selected to upload. The default value is an unlimited number of files.

maxSize -> (integer)

The maximum file size in bytes that the file uploader will accept. The default value is an unlimited file size.

validations -> (list)

The validations to perform on the value in the field.

(structure)

Describes the validation configuration for a field.

type -> (string)

The validation to perform on an object type.

strValues -> (list)

The validation to perform on a string value.

(string)

numValues -> (list)

The validation to perform on a number value.

(integer)

validationMessage -> (string)

The validation message to display.

style -> (structure)

The configuration for the formâs style.

horizontalGap -> (tagged union structure)

The spacing for the horizontal gap.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `tokenReference`, `value`.

tokenReference -> (string)

A reference to a design token to use to bind the formâs style properties to an existing theme.

value -> (string)

The value of the style setting.

verticalGap -> (tagged union structure)

The spacing for the vertical gap.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `tokenReference`, `value`.

tokenReference -> (string)

A reference to a design token to use to bind the formâs style properties to an existing theme.

value -> (string)

The value of the style setting.

outerPadding -> (tagged union structure)

The size of the outer padding for the form.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `tokenReference`, `value`.

tokenReference -> (string)

A reference to a design token to use to bind the formâs style properties to an existing theme.

value -> (string)

The value of the style setting.

sectionalElements -> (map)

The configuration information for the visual helper elements for the form. These elements are not associated with any data.

key -> (string)

value -> (structure)

Stores the configuration information for a visual helper element for a form. A sectional element can be a header, a text block, or a divider. These elements are static and not associated with any data.

type -> (string)

The type of sectional element. Valid values are `Heading` , `Text` , and `Divider` .

position -> (tagged union structure)

Specifies the position of the text in a field for a `Text` sectional element.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fixed`, `rightOf`, `below`.

fixed -> (string)

The field position is fixed and doesnât change in relation to other fields.

rightOf -> (string)

The field position is to the right of the field specified by the string.

below -> (string)

The field position is below the field specified by the string.

text -> (string)

The text for a `Text` sectional element.

level -> (integer)

Specifies the size of the font for a `Heading` sectional element. Valid values are `1 | 2 | 3 | 4 | 5 | 6` .

orientation -> (string)

Specifies the orientation for a `Divider` sectional element. Valid values are `horizontal` or `vertical` .

excluded -> (boolean)

Excludes a sectional element that was generated by default for a specified data model.

schemaVersion -> (string)

The schema version of the form.

cta -> (structure)

The `FormCTA` object that stores the call to action configuration for the form.

position -> (string)

The position of the button.

clear -> (structure)

Displays a clear button.

excluded -> (boolean)

Specifies whether the button is visible on the form.

children -> (string)

Describes the buttonâs properties.

position -> (tagged union structure)

The position of the button.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fixed`, `rightOf`, `below`.

fixed -> (string)

The field position is fixed and doesnât change in relation to other fields.

rightOf -> (string)

The field position is to the right of the field specified by the string.

below -> (string)

The field position is below the field specified by the string.

cancel -> (structure)

Displays a cancel button.

excluded -> (boolean)

Specifies whether the button is visible on the form.

children -> (string)

Describes the buttonâs properties.

position -> (tagged union structure)

The position of the button.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fixed`, `rightOf`, `below`.

fixed -> (string)

The field position is fixed and doesnât change in relation to other fields.

rightOf -> (string)

The field position is to the right of the field specified by the string.

below -> (string)

The field position is below the field specified by the string.

submit -> (structure)

Displays a submit button.

excluded -> (boolean)

Specifies whether the button is visible on the form.

children -> (string)

Describes the buttonâs properties.

position -> (tagged union structure)

The position of the button.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fixed`, `rightOf`, `below`.

fixed -> (string)

The field position is fixed and doesnât change in relation to other fields.

rightOf -> (string)

The field position is to the right of the field specified by the string.

below -> (string)

The field position is below the field specified by the string.

tags -> (map)

One or more key-value pairs to use when tagging the form data.

key -> (string)

value -> (string)

labelDecorator -> (string)

Specifies an icon or decoration to display on the form.

JSON Syntax:

```
{
  "name": "string",
  "dataType": {
    "dataSourceType": "DataStore"|"Custom",
    "dataTypeName": "string"
  },
  "formActionType": "create"|"update",
  "fields": {"string": {
        "label": "string",
        "position": {
          "fixed": "first",
          "rightOf": "string",
          "below": "string"
        },
        "excluded": true|false,
        "inputType": {
          "type": "string",
          "required": true|false,
          "readOnly": true|false,
          "placeholder": "string",
          "defaultValue": "string",
          "descriptiveText": "string",
          "defaultChecked": true|false,
          "defaultCountryCode": "string",
          "valueMappings": {
            "values": [
              {
                "displayValue": {
                  "value": "string",
                  "bindingProperties": {
                    "property": "string",
                    "field": "string"
                  },
                  "concat": [
                    {
                      "value": "string",
                      "bindingProperties": {
                        "property": "string",
                        "field": "string"
                      },
                      "concat": [
                        { ... recursive ... }
                        ...
                      ]
                    }
                    ...
                  ]
                },
                "value": {
                  "value": "string",
                  "bindingProperties": {
                    "property": "string",
                    "field": "string"
                  },
                  "concat": [
                    {
                      "value": "string",
                      "bindingProperties": {
                        "property": "string",
                        "field": "string"
                      },
                      "concat": [
                        { ... recursive ... }
                        ...
                      ]
                    }
                    ...
                  ]
                }
              }
              ...
            ],
            "bindingProperties": {"string": {
                  "type": "string",
                  "bindingProperties": {
                    "model": "string"
                  }
                }
              ...}
          },
          "name": "string",
          "minValue": float,
          "maxValue": float,
          "step": float,
          "value": "string",
          "isArray": true|false,
          "fileUploaderConfig": {
            "accessLevel": "public"|"protected"|"private",
            "acceptedFileTypes": ["string", ...],
            "showThumbnails": true|false,
            "isResumable": true|false,
            "maxFileCount": integer,
            "maxSize": integer
          }
        },
        "validations": [
          {
            "type": "string",
            "strValues": ["string", ...],
            "numValues": [integer, ...],
            "validationMessage": "string"
          }
          ...
        ]
      }
    ...},
  "style": {
    "horizontalGap": {
      "tokenReference": "string",
      "value": "string"
    },
    "verticalGap": {
      "tokenReference": "string",
      "value": "string"
    },
    "outerPadding": {
      "tokenReference": "string",
      "value": "string"
    }
  },
  "sectionalElements": {"string": {
        "type": "string",
        "position": {
          "fixed": "first",
          "rightOf": "string",
          "below": "string"
        },
        "text": "string",
        "level": integer,
        "orientation": "string",
        "excluded": true|false
      }
    ...},
  "schemaVersion": "string",
  "cta": {
    "position": "top"|"bottom"|"top_and_bottom",
    "clear": {
      "excluded": true|false,
      "children": "string",
      "position": {
        "fixed": "first",
        "rightOf": "string",
        "below": "string"
      }
    },
    "cancel": {
      "excluded": true|false,
      "children": "string",
      "position": {
        "fixed": "first",
        "rightOf": "string",
        "below": "string"
      }
    },
    "submit": {
      "excluded": true|false,
      "children": "string",
      "position": {
        "fixed": "first",
        "rightOf": "string",
        "below": "string"
      }
    }
  },
  "tags": {"string": "string"
    ...},
  "labelDecorator": "required"|"optional"|"none"
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

entity -> (structure)

Describes the configuration of the new form.

appId -> (string)

The unique ID of the Amplify app associated with the form.

environmentName -> (string)

The name of the backend environment that is a part of the Amplify app.

id -> (string)

The unique ID of the form.

name -> (string)

The name of the form.

formActionType -> (string)

The operation to perform on the specified form.

style -> (structure)

Stores the configuration for the formâs style.

horizontalGap -> (tagged union structure)

The spacing for the horizontal gap.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `tokenReference`, `value`.

tokenReference -> (string)

A reference to a design token to use to bind the formâs style properties to an existing theme.

value -> (string)

The value of the style setting.

verticalGap -> (tagged union structure)

The spacing for the vertical gap.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `tokenReference`, `value`.

tokenReference -> (string)

A reference to a design token to use to bind the formâs style properties to an existing theme.

value -> (string)

The value of the style setting.

outerPadding -> (tagged union structure)

The size of the outer padding for the form.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `tokenReference`, `value`.

tokenReference -> (string)

A reference to a design token to use to bind the formâs style properties to an existing theme.

value -> (string)

The value of the style setting.

dataType -> (structure)

The type of data source to use to create the form.

dataSourceType -> (string)

The data source type, either an Amplify DataStore model or a custom data type.

dataTypeName -> (string)

The unique name of the data type you are using as the data source for the form.

fields -> (map)

Stores the information about the formâs fields.

key -> (string)

value -> (structure)

Describes the configuration information for a field in a table.

label -> (string)

The label for the field.

position -> (tagged union structure)

Specifies the field position.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fixed`, `rightOf`, `below`.

fixed -> (string)

The field position is fixed and doesnât change in relation to other fields.

rightOf -> (string)

The field position is to the right of the field specified by the string.

below -> (string)

The field position is below the field specified by the string.

excluded -> (boolean)

Specifies whether to hide a field.

inputType -> (structure)

Describes the configuration for the default input value to display for a field.

type -> (string)

The input type for the field.

required -> (boolean)

Specifies a field that requires input.

readOnly -> (boolean)

Specifies a read only field.

placeholder -> (string)

The text to display as a placeholder for the field.

defaultValue -> (string)

The default value for the field.

descriptiveText -> (string)

The text to display to describe the field.

defaultChecked -> (boolean)

Specifies whether a field has a default value.

defaultCountryCode -> (string)

The default country code for a phone number.

valueMappings -> (structure)

The information to use to customize the input fields with data at runtime.

values -> (list)

The value and display value pairs.

(structure)

Associates a complex object with a display value. Use `ValueMapping` to store how to represent complex objects when they are displayed.

displayValue -> (structure)

The value to display for the complex object.

value -> (string)

The value to assign to the input field.

bindingProperties -> (structure)

The information to bind fields to data at runtime.

property -> (string)

The form property to bind to the data field.

field -> (string)

The data field to bind the property to.

concat -> (list)

A list of form properties to concatenate to create the value to assign to this field property.

(structure)

Describes the configuration for an input field on a form. Use `FormInputValueProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the input field.

bindingProperties -> (structure)

The information to bind fields to data at runtime.

property -> (string)

The form property to bind to the data field.

field -> (string)

The data field to bind the property to.

concat -> (list)

A list of form properties to concatenate to create the value to assign to this field property.

( â¦ recursive â¦ )

value -> (structure)

The complex object.

value -> (string)

The value to assign to the input field.

bindingProperties -> (structure)

The information to bind fields to data at runtime.

property -> (string)

The form property to bind to the data field.

field -> (string)

The data field to bind the property to.

concat -> (list)

A list of form properties to concatenate to create the value to assign to this field property.

(structure)

Describes the configuration for an input field on a form. Use `FormInputValueProperty` to specify the values to render or bind by default.

value -> (string)

The value to assign to the input field.

bindingProperties -> (structure)

The information to bind fields to data at runtime.

property -> (string)

The form property to bind to the data field.

field -> (string)

The data field to bind the property to.

concat -> (list)

A list of form properties to concatenate to create the value to assign to this field property.

( â¦ recursive â¦ )

bindingProperties -> (map)

The information to bind fields to data at runtime.

key -> (string)

value -> (structure)

Represents the data binding configuration for a formâs input fields at runtime.You can use `FormInputBindingPropertiesValue` to add exposed properties to a form to allow different values to be entered when a form is reused in different places in an app.

type -> (string)

The property type.

bindingProperties -> (structure)

Describes the properties to customize with data at runtime.

model -> (string)

An Amplify DataStore model.

name -> (string)

The name of the field.

minValue -> (float)

The minimum value to display for the field.

maxValue -> (float)

The maximum value to display for the field.

step -> (float)

The stepping increment for a numeric value in a field.

value -> (string)

The value for the field.

isArray -> (boolean)

Specifies whether to render the field as an array. This property is ignored if the `dataSourceType` for the form is a Data Store.

fileUploaderConfig -> (structure)

The configuration for the file uploader field.

accessLevel -> (string)

The access level to assign to the uploaded files in the Amazon S3 bucket where they are stored. The valid values for this property are `private` , `protected` , or `public` . For detailed information about the permissions associated with each access level, see [File access levels](https://docs.amplify.aws/lib/storage/configureaccess/q/platform/js/) in the *Amplify documentation* .

acceptedFileTypes -> (list)

The file types that are allowed to be uploaded by the file uploader. Provide this information in an array of strings specifying the valid file extensions.

(string)

showThumbnails -> (boolean)

Specifies whether to display or hide the image preview after selecting a file for upload. The default value is `true` to display the image preview.

isResumable -> (boolean)

Allows the file upload operation to be paused and resumed. The default value is `false` .

When `isResumable` is set to `true` , the file uploader uses a multipart upload to break the files into chunks before upload. The progress of the upload isnât continuous, because the file uploader uploads a chunk at a time.

maxFileCount -> (integer)

Specifies the maximum number of files that can be selected to upload. The default value is an unlimited number of files.

maxSize -> (integer)

The maximum file size in bytes that the file uploader will accept. The default value is an unlimited file size.

validations -> (list)

The validations to perform on the value in the field.

(structure)

Describes the validation configuration for a field.

type -> (string)

The validation to perform on an object type.

strValues -> (list)

The validation to perform on a string value.

(string)

numValues -> (list)

The validation to perform on a number value.

(integer)

validationMessage -> (string)

The validation message to display.

sectionalElements -> (map)

Stores the visual helper elements for the form that are not associated with any data.

key -> (string)

value -> (structure)

Stores the configuration information for a visual helper element for a form. A sectional element can be a header, a text block, or a divider. These elements are static and not associated with any data.

type -> (string)

The type of sectional element. Valid values are `Heading` , `Text` , and `Divider` .

position -> (tagged union structure)

Specifies the position of the text in a field for a `Text` sectional element.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fixed`, `rightOf`, `below`.

fixed -> (string)

The field position is fixed and doesnât change in relation to other fields.

rightOf -> (string)

The field position is to the right of the field specified by the string.

below -> (string)

The field position is below the field specified by the string.

text -> (string)

The text for a `Text` sectional element.

level -> (integer)

Specifies the size of the font for a `Heading` sectional element. Valid values are `1 | 2 | 3 | 4 | 5 | 6` .

orientation -> (string)

Specifies the orientation for a `Divider` sectional element. Valid values are `horizontal` or `vertical` .

excluded -> (boolean)

Excludes a sectional element that was generated by default for a specified data model.

schemaVersion -> (string)

The schema version of the form when it was imported.

tags -> (map)

One or more key-value pairs to use when tagging the form.

key -> (string)

value -> (string)

cta -> (structure)

Stores the call to action configuration for the form.

position -> (string)

The position of the button.

clear -> (structure)

Displays a clear button.

excluded -> (boolean)

Specifies whether the button is visible on the form.

children -> (string)

Describes the buttonâs properties.

position -> (tagged union structure)

The position of the button.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fixed`, `rightOf`, `below`.

fixed -> (string)

The field position is fixed and doesnât change in relation to other fields.

rightOf -> (string)

The field position is to the right of the field specified by the string.

below -> (string)

The field position is below the field specified by the string.

cancel -> (structure)

Displays a cancel button.

excluded -> (boolean)

Specifies whether the button is visible on the form.

children -> (string)

Describes the buttonâs properties.

position -> (tagged union structure)

The position of the button.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fixed`, `rightOf`, `below`.

fixed -> (string)

The field position is fixed and doesnât change in relation to other fields.

rightOf -> (string)

The field position is to the right of the field specified by the string.

below -> (string)

The field position is below the field specified by the string.

submit -> (structure)

Displays a submit button.

excluded -> (boolean)

Specifies whether the button is visible on the form.

children -> (string)

Describes the buttonâs properties.

position -> (tagged union structure)

The position of the button.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fixed`, `rightOf`, `below`.

fixed -> (string)

The field position is fixed and doesnât change in relation to other fields.

rightOf -> (string)

The field position is to the right of the field specified by the string.

below -> (string)

The field position is below the field specified by the string.

labelDecorator -> (string)

Specifies an icon or decoration to display on the form.