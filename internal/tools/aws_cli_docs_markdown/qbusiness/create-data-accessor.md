# create-data-accessorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/create-data-accessor.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/create-data-accessor.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qbusiness](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/index.html#cli-aws-qbusiness) ]

# create-data-accessor

## Description

Creates a new data accessor for an ISV to access data from a Amazon Q Business application. The data accessor is an entity that represents the ISVâs access to the Amazon Q Business applicationâs data. It includes the IAM role ARN for the ISV, a friendly name, and a set of action configurations that define the specific actions the ISV is allowed to perform and any associated data filters. When the data accessor is created, an IAM Identity Center application is also created to manage the ISVâs identity and authentication for accessing the Amazon Q Business application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qbusiness-2023-11-27/CreateDataAccessor)

## Synopsis

```
create-data-accessor
--application-id <value>
--principal <value>
--action-configurations <value>
[--client-token <value>]
--display-name <value>
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

`--application-id` (string)

The unique identifier of the Amazon Q Business application.

`--principal` (string)

The Amazon Resource Name (ARN) of the IAM role for the ISV that will be accessing the data.

`--action-configurations` (list)

A list of action configurations specifying the allowed actions and any associated filters.

(structure)

Specifies an allowed action and its associated filter configuration.

action -> (string)

The Amazon Q Business action that is allowed.

filterConfiguration -> (structure)

The filter configuration for the action, if any.

documentAttributeFilter -> (structure)

Enables filtering of responses based on document attributes or metadata fields.

andAllFilters -> (list)

Performs a logical `AND` operation on all supplied filters.

(structure)

Enables filtering of responses based on document attributes or metadata fields.

andAllFilters -> (list)

Performs a logical `AND` operation on all supplied filters.

( â¦ recursive â¦ )

orAllFilters -> (list)

Performs a logical `OR` operation on all supplied filters.

( â¦ recursive â¦ )

( â¦ recursive â¦ )equalsTo -> (structure)

Performs an equals operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` , `longValue` , `stringListValue` and `stringValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

greaterThan -> (structure)

Performs a greater than operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

greaterThanOrEquals -> (structure)

Performs a greater or equals than operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

lessThan -> (structure)

Performs a less than operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

lessThanOrEquals -> (structure)

Performs a less than or equals operation on two document attributes or metadata fields.Supported for the following [document attribute value type](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

orAllFilters -> (list)

Performs a logical `OR` operation on all supplied filters.

(structure)

Enables filtering of responses based on document attributes or metadata fields.

andAllFilters -> (list)

Performs a logical `AND` operation on all supplied filters.

( â¦ recursive â¦ )

orAllFilters -> (list)

Performs a logical `OR` operation on all supplied filters.

( â¦ recursive â¦ )

( â¦ recursive â¦ )equalsTo -> (structure)

Performs an equals operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` , `longValue` , `stringListValue` and `stringValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

greaterThan -> (structure)

Performs a greater than operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

greaterThanOrEquals -> (structure)

Performs a greater or equals than operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

lessThan -> (structure)

Performs a less than operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

lessThanOrEquals -> (structure)

Performs a less than or equals operation on two document attributes or metadata fields.Supported for the following [document attribute value type](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

notFilter -> (structure)

Performs a logical `NOT` operation on all supplied filters.

andAllFilters -> (list)

Performs a logical `AND` operation on all supplied filters.

( â¦ recursive â¦ )

orAllFilters -> (list)

Performs a logical `OR` operation on all supplied filters.

( â¦ recursive â¦ )

( â¦ recursive â¦ )equalsTo -> (structure)

Performs an equals operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` , `longValue` , `stringListValue` and `stringValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

greaterThan -> (structure)

Performs a greater than operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

greaterThanOrEquals -> (structure)

Performs a greater or equals than operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

lessThan -> (structure)

Performs a less than operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

lessThanOrEquals -> (structure)

Performs a less than or equals operation on two document attributes or metadata fields.Supported for the following [document attribute value type](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

equalsTo -> (structure)

Performs an equals operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` , `longValue` , `stringListValue` and `stringValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

greaterThan -> (structure)

Performs a greater than operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

greaterThanOrEquals -> (structure)

Performs a greater or equals than operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

lessThan -> (structure)

Performs a less than operation on two document attributes or metadata fields. Supported for the following [document attribute value types](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

lessThanOrEquals -> (structure)

Performs a less than or equals operation on two document attributes or metadata fields.Supported for the following [document attribute value type](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html) : `dateValue` and `longValue` .

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

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

JSON Syntax:

```
[
  {
    "action": "string",
    "filterConfiguration": {
      "documentAttributeFilter": {
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
    }
  }
  ...
]
```

`--client-token` (string)

A unique, case-sensitive identifier you provide to ensure idempotency of the request.

`--display-name` (string)

A friendly name for the data accessor.

`--tags` (list)

The tags to associate with the data accessor.

(structure)

A list of key/value pairs that identify an index, FAQ, or data source. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

key -> (string)

The key for the tag. Keys are not case sensitive and must be unique for the Amazon Q Business application or data source.

value -> (string)

The value associated with the tag. The value may be an empty string but it canât be null.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
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

dataAccessorId -> (string)

The unique identifier of the created data accessor.

idcApplicationArn -> (string)

The Amazon Resource Name (ARN) of the IAM Identity Center application created for this data accessor.

dataAccessorArn -> (string)

The Amazon Resource Name (ARN) of the created data accessor.