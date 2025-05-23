# update-q-appÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qapps/update-q-app.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qapps/update-q-app.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qapps](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qapps/index.html#cli-aws-qapps) ]

# update-q-app

## Description

Updates an existing Amazon Q App, allowing modifications to its title, description, and definition.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qapps-2023-11-27/UpdateQApp)

`update-q-app` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
update-q-app
--instance-id <value>
--app-id <value>
[--title <value>]
[--description <value>]
[--app-definition <value>]
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

`--instance-id` (string)

The unique identifier of the Amazon Q Business application environment instance.

`--app-id` (string)

The unique identifier of the Q App to update.

`--title` (string)

The new title for the Q App.

`--description` (string)

The new description for the Q App.

`--app-definition` (structure)

The new definition specifying the cards and flow for the Q App.

cards -> (list)

The cards that make up the Q App definition.

(tagged union structure)

The properties defining an input card in an Amazon Q App.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `textInput`, `qQuery`, `qPlugin`, `fileUpload`, `formInput`.

textInput -> (structure)

A container for the properties of the text input card.

title -> (string)

The title or label of the text input card.

id -> (string)

The unique identifier of the text input card.

type -> (string)

The type of the card.

placeholder -> (string)

The placeholder text to display in the text input field.

defaultValue -> (string)

The default value to pre-populate in the text input field.

qQuery -> (structure)

A container for the properties of the query input card.

title -> (string)

The title or label of the query card.

id -> (string)

The unique identifier of the query card.

type -> (string)

The type of the card.

prompt -> (string)

The prompt or instructions displayed for the query card.

outputSource -> (string)

The source or type of output to generate for the query card.

attributeFilter -> (structure)

Turns on filtering of responses based on document attributes or metadata fields.

andAllFilters -> (list)

Performs a logical `AND` operation on all supplied filters.

(structure)

The filter criteria used on responses based on document attributes or metadata fields.

andAllFilters -> (list)

Performs a logical `AND` operation on all supplied filters.

( â¦ recursive â¦ )

orAllFilters -> (list)

Performs a logical `OR` operation on all supplied filters.

( â¦ recursive â¦ )

( â¦ recursive â¦ )equalsTo -> (structure)

Performs an *equals* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` , `longValue` , `stringListValue` and `stringValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

containsAll -> (structure)

Returns `true` when a document contains all the specified document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `stringListValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

containsAny -> (structure)

Returns `true` when a document contains any of the specified document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `stringListValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

greaterThan -> (structure)

Performs a *greater than* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

greaterThanOrEquals -> (structure)

Performs a *greater than or equals* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

lessThan -> (structure)

Performs a *less than* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

lessThanOrEquals -> (structure)

Performs a *less than or equals* operation on two document attributes or metadata fields.Supported for the following [document attribute value type](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

orAllFilters -> (list)

Performs a logical `OR` operation on all supplied filters.

(structure)

The filter criteria used on responses based on document attributes or metadata fields.

andAllFilters -> (list)

Performs a logical `AND` operation on all supplied filters.

( â¦ recursive â¦ )

orAllFilters -> (list)

Performs a logical `OR` operation on all supplied filters.

( â¦ recursive â¦ )

( â¦ recursive â¦ )equalsTo -> (structure)

Performs an *equals* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` , `longValue` , `stringListValue` and `stringValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

containsAll -> (structure)

Returns `true` when a document contains all the specified document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `stringListValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

containsAny -> (structure)

Returns `true` when a document contains any of the specified document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `stringListValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

greaterThan -> (structure)

Performs a *greater than* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

greaterThanOrEquals -> (structure)

Performs a *greater than or equals* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

lessThan -> (structure)

Performs a *less than* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

lessThanOrEquals -> (structure)

Performs a *less than or equals* operation on two document attributes or metadata fields.Supported for the following [document attribute value type](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

notFilter -> (structure)

Performs a logical `NOT` operation on all supplied filters.

andAllFilters -> (list)

Performs a logical `AND` operation on all supplied filters.

( â¦ recursive â¦ )

orAllFilters -> (list)

Performs a logical `OR` operation on all supplied filters.

( â¦ recursive â¦ )

( â¦ recursive â¦ )equalsTo -> (structure)

Performs an *equals* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` , `longValue` , `stringListValue` and `stringValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

containsAll -> (structure)

Returns `true` when a document contains all the specified document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `stringListValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

containsAny -> (structure)

Returns `true` when a document contains any of the specified document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `stringListValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

greaterThan -> (structure)

Performs a *greater than* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

greaterThanOrEquals -> (structure)

Performs a *greater than or equals* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

lessThan -> (structure)

Performs a *less than* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

lessThanOrEquals -> (structure)

Performs a *less than or equals* operation on two document attributes or metadata fields.Supported for the following [document attribute value type](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

equalsTo -> (structure)

Performs an *equals* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` , `longValue` , `stringListValue` and `stringValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

containsAll -> (structure)

Returns `true` when a document contains all the specified document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `stringListValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

containsAny -> (structure)

Returns `true` when a document contains any of the specified document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `stringListValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

greaterThan -> (structure)

Performs a *greater than* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

greaterThanOrEquals -> (structure)

Performs a *greater than or equals* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

lessThan -> (structure)

Performs a *less than* operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

lessThanOrEquals -> (structure)

Performs a *less than or equals* operation on two document attributes or metadata fields.Supported for the following [document attribute value type](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the *ISO 8601 date-time* format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

qPlugin -> (structure)

A container for the properties of the plugin input card.

title -> (string)

The title or label of the plugin card.

id -> (string)

The unique identifier of the plugin card.

type -> (string)

The type of the card.

prompt -> (string)

The prompt or instructions displayed for the plugin card.

pluginId -> (string)

The unique identifier of the plugin used by the card.

actionIdentifier -> (string)

The action identifier of the action to be performed by the plugin card.

fileUpload -> (structure)

A container for the properties of the file upload input card.

title -> (string)

The title or label of the file upload card.

id -> (string)

The unique identifier of the file upload card.

type -> (string)

The type of the card.

filename -> (string)

The default filename to use for the file upload card.

fileId -> (string)

The identifier of a pre-uploaded file associated with the card.

allowOverride -> (boolean)

A flag indicating if the user can override the default file for the upload card.

formInput -> (structure)

A container for the properties of the form input card.

title -> (string)

The title or label of the form input card.

id -> (string)

The unique identifier of the form input card.

type -> (string)

The type of the card.

metadata -> (structure)

The metadata that defines the form input card data.

schema -> (document)

The JSON schema that defines the shape of the response data.

computeMode -> (string)

The compute mode of the form input card. This property determines whether individual participants of a data collection session can submit multiple response or one response. A compute mode of `append` shall allow participants to submit the same form multiple times with different values. A compute mode of `replace` code> shall overwrite the current value for each participant.

initialPrompt -> (string)

The initial prompt displayed when the Q App is started.

JSON Syntax:

```
{
  "cards": [
    {
      "textInput": {
        "title": "string",
        "id": "string",
        "type": "text-input"|"q-query"|"file-upload"|"q-plugin"|"form-input",
        "placeholder": "string",
        "defaultValue": "string"
      },
      "qQuery": {
        "title": "string",
        "id": "string",
        "type": "text-input"|"q-query"|"file-upload"|"q-plugin"|"form-input",
        "prompt": "string",
        "outputSource": "approved-sources"|"llm",
        "attributeFilter": {
          "andAllFilters": [
            {
              "andAllFilters": [
                { ... recursive ... }
                ...
              ],
              "orAllFilters": [
                { ... recursive ... }
                ...
              ],
              "notFilter": { ... recursive ... },
              "equalsTo": {
                "name": "string",
                "value": {
                  "stringValue": "string",
                  "stringListValue": ["string", ...],
                  "longValue": long,
                  "dateValue": timestamp
                }
              },
              "containsAll": {
                "name": "string",
                "value": {
                  "stringValue": "string",
                  "stringListValue": ["string", ...],
                  "longValue": long,
                  "dateValue": timestamp
                }
              },
              "containsAny": {
                "name": "string",
                "value": {
                  "stringValue": "string",
                  "stringListValue": ["string", ...],
                  "longValue": long,
                  "dateValue": timestamp
                }
              },
              "greaterThan": {
                "name": "string",
                "value": {
                  "stringValue": "string",
                  "stringListValue": ["string", ...],
                  "longValue": long,
                  "dateValue": timestamp
                }
              },
              "greaterThanOrEquals": {
                "name": "string",
                "value": {
                  "stringValue": "string",
                  "stringListValue": ["string", ...],
                  "longValue": long,
                  "dateValue": timestamp
                }
              },
              "lessThan": {
                "name": "string",
                "value": {
                  "stringValue": "string",
                  "stringListValue": ["string", ...],
                  "longValue": long,
                  "dateValue": timestamp
                }
              },
              "lessThanOrEquals": {
                "name": "string",
                "value": {
                  "stringValue": "string",
                  "stringListValue": ["string", ...],
                  "longValue": long,
                  "dateValue": timestamp
                }
              }
            }
            ...
          ],
          "orAllFilters": [
            {
              "andAllFilters": [
                { ... recursive ... }
                ...
              ],
              "orAllFilters": [
                { ... recursive ... }
                ...
              ],
              "notFilter": { ... recursive ... },
              "equalsTo": {
                "name": "string",
                "value": {
                  "stringValue": "string",
                  "stringListValue": ["string", ...],
                  "longValue": long,
                  "dateValue": timestamp
                }
              },
              "containsAll": {
                "name": "string",
                "value": {
                  "stringValue": "string",
                  "stringListValue": ["string", ...],
                  "longValue": long,
                  "dateValue": timestamp
                }
              },
              "containsAny": {
                "name": "string",
                "value": {
                  "stringValue": "string",
                  "stringListValue": ["string", ...],
                  "longValue": long,
                  "dateValue": timestamp
                }
              },
              "greaterThan": {
                "name": "string",
                "value": {
                  "stringValue": "string",
                  "stringListValue": ["string", ...],
                  "longValue": long,
                  "dateValue": timestamp
                }
              },
              "greaterThanOrEquals": {
                "name": "string",
                "value": {
                  "stringValue": "string",
                  "stringListValue": ["string", ...],
                  "longValue": long,
                  "dateValue": timestamp
                }
              },
              "lessThan": {
                "name": "string",
                "value": {
                  "stringValue": "string",
                  "stringListValue": ["string", ...],
                  "longValue": long,
                  "dateValue": timestamp
                }
              },
              "lessThanOrEquals": {
                "name": "string",
                "value": {
                  "stringValue": "string",
                  "stringListValue": ["string", ...],
                  "longValue": long,
                  "dateValue": timestamp
                }
              }
            }
            ...
          ],
          "notFilter": {
            "andAllFilters": [
              { ... recursive ... }
              ...
            ],
            "orAllFilters": [
              { ... recursive ... }
              ...
            ],
            "notFilter": { ... recursive ... },
            "equalsTo": {
              "name": "string",
              "value": {
                "stringValue": "string",
                "stringListValue": ["string", ...],
                "longValue": long,
                "dateValue": timestamp
              }
            },
            "containsAll": {
              "name": "string",
              "value": {
                "stringValue": "string",
                "stringListValue": ["string", ...],
                "longValue": long,
                "dateValue": timestamp
              }
            },
            "containsAny": {
              "name": "string",
              "value": {
                "stringValue": "string",
                "stringListValue": ["string", ...],
                "longValue": long,
                "dateValue": timestamp
              }
            },
            "greaterThan": {
              "name": "string",
              "value": {
                "stringValue": "string",
                "stringListValue": ["string", ...],
                "longValue": long,
                "dateValue": timestamp
              }
            },
            "greaterThanOrEquals": {
              "name": "string",
              "value": {
                "stringValue": "string",
                "stringListValue": ["string", ...],
                "longValue": long,
                "dateValue": timestamp
              }
            },
            "lessThan": {
              "name": "string",
              "value": {
                "stringValue": "string",
                "stringListValue": ["string", ...],
                "longValue": long,
                "dateValue": timestamp
              }
            },
            "lessThanOrEquals": {
              "name": "string",
              "value": {
                "stringValue": "string",
                "stringListValue": ["string", ...],
                "longValue": long,
                "dateValue": timestamp
              }
            }
          },
          "equalsTo": {
            "name": "string",
            "value": {
              "stringValue": "string",
              "stringListValue": ["string", ...],
              "longValue": long,
              "dateValue": timestamp
            }
          },
          "containsAll": {
            "name": "string",
            "value": {
              "stringValue": "string",
              "stringListValue": ["string", ...],
              "longValue": long,
              "dateValue": timestamp
            }
          },
          "containsAny": {
            "name": "string",
            "value": {
              "stringValue": "string",
              "stringListValue": ["string", ...],
              "longValue": long,
              "dateValue": timestamp
            }
          },
          "greaterThan": {
            "name": "string",
            "value": {
              "stringValue": "string",
              "stringListValue": ["string", ...],
              "longValue": long,
              "dateValue": timestamp
            }
          },
          "greaterThanOrEquals": {
            "name": "string",
            "value": {
              "stringValue": "string",
              "stringListValue": ["string", ...],
              "longValue": long,
              "dateValue": timestamp
            }
          },
          "lessThan": {
            "name": "string",
            "value": {
              "stringValue": "string",
              "stringListValue": ["string", ...],
              "longValue": long,
              "dateValue": timestamp
            }
          },
          "lessThanOrEquals": {
            "name": "string",
            "value": {
              "stringValue": "string",
              "stringListValue": ["string", ...],
              "longValue": long,
              "dateValue": timestamp
            }
          }
        }
      },
      "qPlugin": {
        "title": "string",
        "id": "string",
        "type": "text-input"|"q-query"|"file-upload"|"q-plugin"|"form-input",
        "prompt": "string",
        "pluginId": "string",
        "actionIdentifier": "string"
      },
      "fileUpload": {
        "title": "string",
        "id": "string",
        "type": "text-input"|"q-query"|"file-upload"|"q-plugin"|"form-input",
        "filename": "string",
        "fileId": "string",
        "allowOverride": true|false
      },
      "formInput": {
        "title": "string",
        "id": "string",
        "type": "text-input"|"q-query"|"file-upload"|"q-plugin"|"form-input",
        "metadata": {
          "schema": {...}
        },
        "computeMode": "append"|"replace"
      }
    }
    ...
  ],
  "initialPrompt": "string"
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

appId -> (string)

The unique identifier of the updated Q App.

appArn -> (string)

The Amazon Resource Name (ARN) of the updated Q App.

title -> (string)

The new title of the updated Q App.

description -> (string)

The new description of the updated Q App.

initialPrompt -> (string)

The initial prompt for the updated Q App.

appVersion -> (integer)

The new version of the updated Q App.

status -> (string)

The status of the updated Q App.

createdAt -> (timestamp)

The date and time the Q App was originally created.

createdBy -> (string)

The user who originally created the Q App.

updatedAt -> (timestamp)

The date and time the Q App was last updated.

updatedBy -> (string)

The user who last updated the Q App.

requiredCapabilities -> (list)

The capabilities required for the updated Q App.

(string)