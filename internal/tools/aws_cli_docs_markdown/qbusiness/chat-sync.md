# chat-syncÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/chat-sync.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/chat-sync.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qbusiness](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/index.html#cli-aws-qbusiness) ]

# chat-sync

## Description

Starts or continues a non-streaming Amazon Q Business conversation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qbusiness-2023-11-27/ChatSync)

`chat-sync` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
chat-sync
--application-id <value>
[--user-id <value>]
[--user-groups <value>]
[--user-message <value>]
[--attachments <value>]
[--action-execution <value>]
[--auth-challenge-response <value>]
[--conversation-id <value>]
[--parent-message-id <value>]
[--attribute-filter <value>]
[--chat-mode <value>]
[--chat-mode-configuration <value>]
[--client-token <value>]
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

The identifier of the Amazon Q Business application linked to the Amazon Q Business conversation.

`--user-id` (string)

The identifier of the user attached to the chat input.

`--user-groups` (list)

The group names that a user associated with the chat input belongs to.

(string)

Syntax:

```
"string" "string" ...
```

`--user-message` (string)

A end user message in a conversation.

`--attachments` (list)

A list of files uploaded directly during chat. You can upload a maximum of 5 files of upto 10 MB each.

(structure)

This is either a file directly uploaded into a web experience chat or a reference to an existing attachment that is part of a web experience chat.

data -> (blob)

The contents of the attachment.

name -> (string)

The filename of the attachment.

copyFrom -> (tagged union structure)

A reference to an existing attachment.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `conversation`.

conversation -> (structure)

A reference to an attachment in an existing conversation.

conversationId -> (string)

The unique identifier of the Amazon Q Business conversation.

attachmentId -> (string)

The unique identifier of the Amazon Q Business attachment.

Shorthand Syntax:

```
data=blob,name=string,copyFrom={conversation={conversationId=string,attachmentId=string}} ...
```

JSON Syntax:

```
[
  {
    "data": blob,
    "name": "string",
    "copyFrom": {
      "conversation": {
        "conversationId": "string",
        "attachmentId": "string"
      }
    }
  }
  ...
]
```

`--action-execution` (structure)

A request from an end user to perform an Amazon Q Business plugin action.

pluginId -> (string)

The identifier of the plugin the action is attached to.

payload -> (map)

A mapping of field names to the field values in input that an end user provides to Amazon Q Business requests to perform their plugin action.

key -> (string)

value -> (structure)

A user input field in an plugin action execution payload.

value -> (document)

The content of a user input field in an plugin action execution payload.

payloadFieldNameSeparator -> (string)

A string used to retain information about the hierarchical contexts within an action execution event payload.

Shorthand Syntax:

```
pluginId=string,payload={KeyName1={},KeyName2={}},payloadFieldNameSeparator=string
```

JSON Syntax:

```
{
  "pluginId": "string",
  "payload": {"string": {
        "value": {...}
      }
    ...},
  "payloadFieldNameSeparator": "string"
}
```

`--auth-challenge-response` (structure)

An authentication verification event response by a third party authentication server to Amazon Q Business.

responseMap -> (map)

The mapping of key-value pairs in an authentication challenge response.

key -> (string)

value -> (string)

Shorthand Syntax:

```
responseMap={KeyName1=string,KeyName2=string}
```

JSON Syntax:

```
{
  "responseMap": {"string": "string"
    ...}
}
```

`--conversation-id` (string)

The identifier of the Amazon Q Business conversation.

`--parent-message-id` (string)

The identifier of the previous system message in a conversation.

`--attribute-filter` (structure)

Enables filtering of Amazon Q Business web experience responses based on document attributes or metadata fields.

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
{
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
```

`--chat-mode` (string)

The `chatMode` parameter determines the chat modes available to Amazon Q Business users:

- `RETRIEVAL_MODE` - If you choose this mode, Amazon Q generates responses solely from the data sources connected and indexed by the application. If an answer is not found in the data sources or there are no data sources available, Amazon Q will respond with a â*No Answer Found* â message, unless LLM knowledge has been enabled. In that case, Amazon Q will generate a response from the LLM knowledge
- `CREATOR_MODE` - By selecting this mode, you can choose to generate responses only from the LLM knowledge. You can also attach files and have Amazon Q generate a response based on the data in those files. If the attached files do not contain an answer for the query, Amazon Q will automatically fall back to generating a response from the LLM knowledge.
- `PLUGIN_MODE` - By selecting this mode, users can choose to use plugins in chat to get their responses.

### Note

If none of the modes are selected, Amazon Q will only respond using the information from the attached files.

For more information, see [Admin controls and guardrails](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails.html) , [Plugins](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/plugins.html) , and [Response sources](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/using-web-experience.html#chat-source-scope) .

Possible values:

- `RETRIEVAL_MODE`
- `CREATOR_MODE`
- `PLUGIN_MODE`

`--chat-mode-configuration` (tagged union structure)

The chat mode configuration for an Amazon Q Business application.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `pluginConfiguration`.

pluginConfiguration -> (structure)

Configuration information required to invoke chat in `PLUGIN_MODE` .

pluginId -> (string)

The identifier of the plugin you want to use.

Shorthand Syntax:

```
pluginConfiguration={pluginId=string}
```

JSON Syntax:

```
{
  "pluginConfiguration": {
    "pluginId": "string"
  }
}
```

`--client-token` (string)

A token that you provide to identify a chat request.

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

conversationId -> (string)

The identifier of the Amazon Q Business conversation.

systemMessage -> (string)

An AI-generated message in a conversation.

systemMessageId -> (string)

The identifier of an Amazon Q Business AI generated message within the conversation.

userMessageId -> (string)

The identifier of an Amazon Q Business end user text input message within the conversation.

actionReview -> (structure)

A request from Amazon Q Business to the end user for information Amazon Q Business needs to successfully complete a requested plugin action.

pluginId -> (string)

The identifier of the plugin associated with the action review.

pluginType -> (string)

The type of plugin.

payload -> (map)

Field values that an end user needs to provide to Amazon Q Business for Amazon Q Business to perform the requested plugin action.

key -> (string)

value -> (structure)

A user input field in an plugin action review payload.

displayName -> (string)

The name of the field.

displayOrder -> (integer)

The display order of fields in a payload.

displayDescription -> (string)

The field level description of each action review input field. This could be an explanation of the field. In the Amazon Q Business web experience, these descriptions could be used to display as tool tips to help users understand the field.

type -> (string)

The type of field.

value -> (document)

The field value.

allowedValues -> (list)

Information about the field values that an end user can use to provide to Amazon Q Business for Amazon Q Business to perform the requested plugin action.

(structure)

Information about the field values that an end user can use to provide to Amazon Q Business for Amazon Q Business to perform the requested plugin action.

value -> (document)

The field value.

displayValue -> (document)

The name of the field.

allowedFormat -> (string)

The expected data format for the action review input field value. For example, in PTO request, `from` and `to` would be of `datetime` allowed format.

arrayItemJsonSchema -> (document)

Use to create a custom form with array fields (fields with nested objects inside an array).

required -> (boolean)

Information about whether the field is required.

payloadFieldNameSeparator -> (string)

A string used to retain information about the hierarchical contexts within an action review payload.

authChallengeRequest -> (structure)

An authentication verification event activated by an end user request to use a custom plugin.

authorizationUrl -> (string)

The URL sent by Amazon Q Business to the third party authentication server to authenticate a custom plugin user through an OAuth protocol.

sourceAttributions -> (list)

The source documents used to generate the conversation response.

(structure)

The documents used to generate an Amazon Q Business web experience response.

title -> (string)

The title of the document which is the source for the Amazon Q Business generated response.

snippet -> (string)

The content extract from the document on which the generated response is based.

url -> (string)

The URL of the document which is the source for the Amazon Q Business generated response.

citationNumber -> (integer)

The number attached to a citation in an Amazon Q Business generated response.

updatedAt -> (timestamp)

The Unix timestamp when the Amazon Q Business application was last updated.

textMessageSegments -> (list)

A text extract from a source document that is used for source attribution.

(structure)

Provides information about a text extract in a chat response that can be attributed to a source document.

beginOffset -> (integer)

The zero-based location in the response string where the source attribution starts.

endOffset -> (integer)

The zero-based location in the response string where the source attribution ends.

snippetExcerpt -> (structure)

The relevant text excerpt from a source that was used to generate a citation text segment in an Amazon Q Business chat response.

text -> (string)

The relevant text excerpt from a source that was used to generate a citation text segment in an Amazon Q chat response.

mediaId -> (string)

The identifier of the media object associated with the text segment in the source attribution.

mediaMimeType -> (string)

The MIME type (image/png) of the media object associated with the text segment in the source attribution.

sourceDetails -> (tagged union structure)

Source information for a segment of extracted text, including its media type.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `imageSourceDetails`, `audioSourceDetails`, `videoSourceDetails`.

imageSourceDetails -> (structure)

Details specific to image content within the source.

mediaId -> (string)

Unique identifier for the image file.

mediaMimeType -> (string)

The MIME type of the image file.

audioSourceDetails -> (structure)

Details specific to audio content within the source.

mediaId -> (string)

Unique identifier for the audio media file.

mediaMimeType -> (string)

The MIME type of the audio file (e.g., audio/mp3, audio/wav).

startTimeMilliseconds -> (long)

The starting timestamp in milliseconds for the relevant audio segment.

endTimeMilliseconds -> (long)

The ending timestamp in milliseconds for the relevant audio segment.

audioExtractionType -> (string)

The type of audio extraction performed on the content.

videoSourceDetails -> (structure)

Details specific to video content within the source.

mediaId -> (string)

Unique identifier for the video media file.

mediaMimeType -> (string)

The MIME type of the video file (e.g., video/mp4, video/avi).

startTimeMilliseconds -> (long)

The starting timestamp in milliseconds for the relevant video segment.

endTimeMilliseconds -> (long)

The ending timestamp in milliseconds for the relevant video segment.

videoExtractionType -> (string)

The type of video extraction performed on the content.

failedAttachments -> (list)

A list of files which failed to upload during chat.

(structure)

The details of a file uploaded during chat.

name -> (string)

The name of a file uploaded during chat.

status -> (string)

The status of a file uploaded during chat.

error -> (structure)

An error associated with a file uploaded during chat.

errorMessage -> (string)

The message explaining the Amazon Q Business request error.

errorCode -> (string)

The code associated with the Amazon Q Business request error.

attachmentId -> (string)

The unique identifier of the Amazon Q Business attachment.

conversationId -> (string)

The unique identifier of the Amazon Q Business conversation.