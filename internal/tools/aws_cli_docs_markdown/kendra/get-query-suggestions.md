# get-query-suggestionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/get-query-suggestions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/get-query-suggestions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# get-query-suggestions

## Description

Fetches the queries that are suggested to your users.

`GetQuerySuggestions` is currently not supported in the Amazon Web Services GovCloud (US-West) region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/GetQuerySuggestions)

## Synopsis

```
get-query-suggestions
--index-id <value>
--query-text <value>
[--max-suggestions-count <value>]
[--suggestion-types <value>]
[--attribute-suggestions-config <value>]
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

`--index-id` (string)

The identifier of the index you want to get query suggestions from.

`--query-text` (string)

The text of a userâs query to generate query suggestions.

A query is suggested if the query prefix matches what a user starts to type as their query.

Amazon Kendra does not show any suggestions if a user types fewer than two characters or more than 60 characters. A query must also have at least one search result and contain at least one word of more than four characters.

`--max-suggestions-count` (integer)

The maximum number of query suggestions you want to show to your users.

`--suggestion-types` (list)

The suggestions type to base query suggestions on. The suggestion types are query history or document fields/attributes. You can set one type or the other.

If you set query history as your suggestions type, Amazon Kendra suggests queries relevant to your users based on popular queries in the query history.

If you set document fields/attributes as your suggestions type, Amazon Kendra suggests queries relevant to your users based on the contents of document fields.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  QUERY
  DOCUMENT_ATTRIBUTES
```

`--attribute-suggestions-config` (structure)

Configuration information for the document fields/attributes that you want to base query suggestions on.

SuggestionAttributes -> (list)

The list of document field/attribute keys or field names to use for query suggestions. If the content within any of the fields match what your user starts typing as their query, then the field content is returned as a query suggestion.

(string)

AdditionalResponseAttributes -> (list)

The list of additional document field/attribute keys or field names to include in the response. You can use additional fields to provide extra information in the response. Additional fields are not used to based suggestions on.

(string)

AttributeFilter -> (structure)

Filters the search results based on document fields/attributes.

AndAllFilters -> (list)

Performs a logical `AND` operation on all filters that you specify.

(structure)

Filters the search results based on document attributes or fields.

You can filter results using attributes for your particular documents. The attributes must exist in your index. For example, if your documents include the custom attribute âDepartmentâ, you can filter documents that belong to the âHRâ department. You would use the `EqualsTo` operation to filter results or documents with âDepartmentâ equals to âHRâ.

You can use `AndAllFilters` and `OrAllFilters` in combination with each other or with other operations such as `EqualsTo` . For example:

`AndAllFilters`

- `EqualsTo` : âDepartmentâ, âHRâ
- `OrAllFilters`
- `ContainsAny` : âProject Nameâ, [ânew hiresâ, ânew hiringâ]

This example filters results or documents that belong to the HR department `AND` belong to projects that contain ânew hiresâ `OR` ânew hiringâ in the project name (must use `ContainAny` with `StringListValue` ). This example is filtering with a depth of 2.

You cannot filter more than a depth of 2, otherwise you receive a `ValidationException` exception with the message âAttributeFilter cannot have a depth of more than 2.â Also, if you use more than 10 attribute filters in a given list for `AndAllFilters` or `OrAllFilters` , you receive a `ValidationException` with the message âAttributeFilter cannot have a length of more than 10â.

For examples of using `AttributeFilter` , see [Using document attributes to filter search results](https://docs.aws.amazon.com/kendra/latest/dg/filtering.html#search-filtering) .

AndAllFilters -> (list)

Performs a logical `AND` operation on all filters that you specify.

( â¦ recursive â¦ )

OrAllFilters -> (list)

Performs a logical `OR` operation on all filters that you specify.

( â¦ recursive â¦ )

( â¦ recursive â¦ )EqualsTo -> (structure)

Performs an equals operation on document attributes/fields and their values.

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

ContainsAll -> (structure)

Returns true when a document contains all of the specified document attributes/fields. This filter is only applicable to [StringListValue](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

ContainsAny -> (structure)

Returns true when a document contains any of the specified document attributes/fields. This filter is only applicable to [StringListValue](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

GreaterThan -> (structure)

Performs a greater than operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long` .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

GreaterThanOrEquals -> (structure)

Performs a greater or equals than operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long` .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

LessThan -> (structure)

Performs a less than operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long` .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

LessThanOrEquals -> (structure)

Performs a less than or equals operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long` .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

OrAllFilters -> (list)

Performs a logical `OR` operation on all filters that you specify.

(structure)

Filters the search results based on document attributes or fields.

You can filter results using attributes for your particular documents. The attributes must exist in your index. For example, if your documents include the custom attribute âDepartmentâ, you can filter documents that belong to the âHRâ department. You would use the `EqualsTo` operation to filter results or documents with âDepartmentâ equals to âHRâ.

You can use `AndAllFilters` and `OrAllFilters` in combination with each other or with other operations such as `EqualsTo` . For example:

`AndAllFilters`

- `EqualsTo` : âDepartmentâ, âHRâ
- `OrAllFilters`
- `ContainsAny` : âProject Nameâ, [ânew hiresâ, ânew hiringâ]

This example filters results or documents that belong to the HR department `AND` belong to projects that contain ânew hiresâ `OR` ânew hiringâ in the project name (must use `ContainAny` with `StringListValue` ). This example is filtering with a depth of 2.

You cannot filter more than a depth of 2, otherwise you receive a `ValidationException` exception with the message âAttributeFilter cannot have a depth of more than 2.â Also, if you use more than 10 attribute filters in a given list for `AndAllFilters` or `OrAllFilters` , you receive a `ValidationException` with the message âAttributeFilter cannot have a length of more than 10â.

For examples of using `AttributeFilter` , see [Using document attributes to filter search results](https://docs.aws.amazon.com/kendra/latest/dg/filtering.html#search-filtering) .

AndAllFilters -> (list)

Performs a logical `AND` operation on all filters that you specify.

( â¦ recursive â¦ )

OrAllFilters -> (list)

Performs a logical `OR` operation on all filters that you specify.

( â¦ recursive â¦ )

( â¦ recursive â¦ )EqualsTo -> (structure)

Performs an equals operation on document attributes/fields and their values.

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

ContainsAll -> (structure)

Returns true when a document contains all of the specified document attributes/fields. This filter is only applicable to [StringListValue](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

ContainsAny -> (structure)

Returns true when a document contains any of the specified document attributes/fields. This filter is only applicable to [StringListValue](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

GreaterThan -> (structure)

Performs a greater than operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long` .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

GreaterThanOrEquals -> (structure)

Performs a greater or equals than operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long` .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

LessThan -> (structure)

Performs a less than operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long` .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

LessThanOrEquals -> (structure)

Performs a less than or equals operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long` .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

NotFilter -> (structure)

Performs a logical `NOT` operation on all filters that you specify.

AndAllFilters -> (list)

Performs a logical `AND` operation on all filters that you specify.

( â¦ recursive â¦ )

OrAllFilters -> (list)

Performs a logical `OR` operation on all filters that you specify.

( â¦ recursive â¦ )

( â¦ recursive â¦ )EqualsTo -> (structure)

Performs an equals operation on document attributes/fields and their values.

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

ContainsAll -> (structure)

Returns true when a document contains all of the specified document attributes/fields. This filter is only applicable to [StringListValue](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

ContainsAny -> (structure)

Returns true when a document contains any of the specified document attributes/fields. This filter is only applicable to [StringListValue](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

GreaterThan -> (structure)

Performs a greater than operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long` .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

GreaterThanOrEquals -> (structure)

Performs a greater or equals than operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long` .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

LessThan -> (structure)

Performs a less than operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long` .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

LessThanOrEquals -> (structure)

Performs a less than or equals operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long` .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

EqualsTo -> (structure)

Performs an equals operation on document attributes/fields and their values.

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

ContainsAll -> (structure)

Returns true when a document contains all of the specified document attributes/fields. This filter is only applicable to [StringListValue](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

ContainsAny -> (structure)

Returns true when a document contains any of the specified document attributes/fields. This filter is only applicable to [StringListValue](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

GreaterThan -> (structure)

Performs a greater than operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long` .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

GreaterThanOrEquals -> (structure)

Performs a greater or equals than operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long` .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

LessThan -> (structure)

Performs a less than operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long` .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

LessThanOrEquals -> (structure)

Performs a less than or equals operation on document attributes/fields and their values. Use with the [document attribute type](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DocumentAttributeValue.html) `Date` or `Long` .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

UserContext -> (structure)

Applies user context filtering so that only users who are given access to certain documents see these document in their search results.

Token -> (string)

The user context token for filtering search results for a user. It must be a JWT or a JSON token.

UserId -> (string)

The identifier of the user you want to filter search results based on their access to documents.

Groups -> (list)

The list of groups you want to filter search results based on the groupsâ access to documents.

(string)

DataSourceGroups -> (list)

The list of data source groups you want to filter search results based on groupsâ access to documents in that data source.

(structure)

Data source information for user context filtering.

GroupId -> (string)

The identifier of the group you want to add to your list of groups. This is for filtering search results based on the groupsâ access to documents.

DataSourceId -> (string)

The identifier of the data source group you want to add to your list of data source groups. This is for filtering search results based on the groupsâ access to documents in that data source.

JSON Syntax:

```
{
  "SuggestionAttributes": ["string", ...],
  "AdditionalResponseAttributes": ["string", ...],
  "AttributeFilter": {
    "AndAllFilters": [
      {
        "AndAllFilters": [
          { ... recursive ... }
          ...
        ],
        "OrAllFilters": [
          { ... recursive ... }
          ...
        ],
        "NotFilter": { ... recursive ... },
        "EqualsTo": {
          "Key": "string",
          "Value": {
            "StringValue": "string",
            "StringListValue": ["string", ...],
            "LongValue": long,
            "DateValue": timestamp
          }
        },
        "ContainsAll": {
          "Key": "string",
          "Value": {
            "StringValue": "string",
            "StringListValue": ["string", ...],
            "LongValue": long,
            "DateValue": timestamp
          }
        },
        "ContainsAny": {
          "Key": "string",
          "Value": {
            "StringValue": "string",
            "StringListValue": ["string", ...],
            "LongValue": long,
            "DateValue": timestamp
          }
        },
        "GreaterThan": {
          "Key": "string",
          "Value": {
            "StringValue": "string",
            "StringListValue": ["string", ...],
            "LongValue": long,
            "DateValue": timestamp
          }
        },
        "GreaterThanOrEquals": {
          "Key": "string",
          "Value": {
            "StringValue": "string",
            "StringListValue": ["string", ...],
            "LongValue": long,
            "DateValue": timestamp
          }
        },
        "LessThan": {
          "Key": "string",
          "Value": {
            "StringValue": "string",
            "StringListValue": ["string", ...],
            "LongValue": long,
            "DateValue": timestamp
          }
        },
        "LessThanOrEquals": {
          "Key": "string",
          "Value": {
            "StringValue": "string",
            "StringListValue": ["string", ...],
            "LongValue": long,
            "DateValue": timestamp
          }
        }
      }
      ...
    ],
    "OrAllFilters": [
      {
        "AndAllFilters": [
          { ... recursive ... }
          ...
        ],
        "OrAllFilters": [
          { ... recursive ... }
          ...
        ],
        "NotFilter": { ... recursive ... },
        "EqualsTo": {
          "Key": "string",
          "Value": {
            "StringValue": "string",
            "StringListValue": ["string", ...],
            "LongValue": long,
            "DateValue": timestamp
          }
        },
        "ContainsAll": {
          "Key": "string",
          "Value": {
            "StringValue": "string",
            "StringListValue": ["string", ...],
            "LongValue": long,
            "DateValue": timestamp
          }
        },
        "ContainsAny": {
          "Key": "string",
          "Value": {
            "StringValue": "string",
            "StringListValue": ["string", ...],
            "LongValue": long,
            "DateValue": timestamp
          }
        },
        "GreaterThan": {
          "Key": "string",
          "Value": {
            "StringValue": "string",
            "StringListValue": ["string", ...],
            "LongValue": long,
            "DateValue": timestamp
          }
        },
        "GreaterThanOrEquals": {
          "Key": "string",
          "Value": {
            "StringValue": "string",
            "StringListValue": ["string", ...],
            "LongValue": long,
            "DateValue": timestamp
          }
        },
        "LessThan": {
          "Key": "string",
          "Value": {
            "StringValue": "string",
            "StringListValue": ["string", ...],
            "LongValue": long,
            "DateValue": timestamp
          }
        },
        "LessThanOrEquals": {
          "Key": "string",
          "Value": {
            "StringValue": "string",
            "StringListValue": ["string", ...],
            "LongValue": long,
            "DateValue": timestamp
          }
        }
      }
      ...
    ],
    "NotFilter": {
      "AndAllFilters": [
        { ... recursive ... }
        ...
      ],
      "OrAllFilters": [
        { ... recursive ... }
        ...
      ],
      "NotFilter": { ... recursive ... },
      "EqualsTo": {
        "Key": "string",
        "Value": {
          "StringValue": "string",
          "StringListValue": ["string", ...],
          "LongValue": long,
          "DateValue": timestamp
        }
      },
      "ContainsAll": {
        "Key": "string",
        "Value": {
          "StringValue": "string",
          "StringListValue": ["string", ...],
          "LongValue": long,
          "DateValue": timestamp
        }
      },
      "ContainsAny": {
        "Key": "string",
        "Value": {
          "StringValue": "string",
          "StringListValue": ["string", ...],
          "LongValue": long,
          "DateValue": timestamp
        }
      },
      "GreaterThan": {
        "Key": "string",
        "Value": {
          "StringValue": "string",
          "StringListValue": ["string", ...],
          "LongValue": long,
          "DateValue": timestamp
        }
      },
      "GreaterThanOrEquals": {
        "Key": "string",
        "Value": {
          "StringValue": "string",
          "StringListValue": ["string", ...],
          "LongValue": long,
          "DateValue": timestamp
        }
      },
      "LessThan": {
        "Key": "string",
        "Value": {
          "StringValue": "string",
          "StringListValue": ["string", ...],
          "LongValue": long,
          "DateValue": timestamp
        }
      },
      "LessThanOrEquals": {
        "Key": "string",
        "Value": {
          "StringValue": "string",
          "StringListValue": ["string", ...],
          "LongValue": long,
          "DateValue": timestamp
        }
      }
    },
    "EqualsTo": {
      "Key": "string",
      "Value": {
        "StringValue": "string",
        "StringListValue": ["string", ...],
        "LongValue": long,
        "DateValue": timestamp
      }
    },
    "ContainsAll": {
      "Key": "string",
      "Value": {
        "StringValue": "string",
        "StringListValue": ["string", ...],
        "LongValue": long,
        "DateValue": timestamp
      }
    },
    "ContainsAny": {
      "Key": "string",
      "Value": {
        "StringValue": "string",
        "StringListValue": ["string", ...],
        "LongValue": long,
        "DateValue": timestamp
      }
    },
    "GreaterThan": {
      "Key": "string",
      "Value": {
        "StringValue": "string",
        "StringListValue": ["string", ...],
        "LongValue": long,
        "DateValue": timestamp
      }
    },
    "GreaterThanOrEquals": {
      "Key": "string",
      "Value": {
        "StringValue": "string",
        "StringListValue": ["string", ...],
        "LongValue": long,
        "DateValue": timestamp
      }
    },
    "LessThan": {
      "Key": "string",
      "Value": {
        "StringValue": "string",
        "StringListValue": ["string", ...],
        "LongValue": long,
        "DateValue": timestamp
      }
    },
    "LessThanOrEquals": {
      "Key": "string",
      "Value": {
        "StringValue": "string",
        "StringListValue": ["string", ...],
        "LongValue": long,
        "DateValue": timestamp
      }
    }
  },
  "UserContext": {
    "Token": "string",
    "UserId": "string",
    "Groups": ["string", ...],
    "DataSourceGroups": [
      {
        "GroupId": "string",
        "DataSourceId": "string"
      }
      ...
    ]
  }
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

QuerySuggestionsId -> (string)

The identifier for a list of query suggestions for an index.

Suggestions -> (list)

A list of query suggestions for an index.

(structure)

A single query suggestion.

Id -> (string)

The UUID (universally unique identifier) of a single query suggestion.

Value -> (structure)

The value for the UUID (universally unique identifier) of a single query suggestion.

The value is the text string of a suggestion.

Text -> (structure)

The `SuggestionTextWithHighlights` structure that contains the query suggestion text and highlights.

Text -> (string)

The query suggestion text to display to the user.

Highlights -> (list)

The beginning and end of the query suggestion text that should be highlighted.

(structure)

The text highlights for a single query suggestion.

BeginOffset -> (integer)

The zero-based location in the response string where the highlight starts.

EndOffset -> (integer)

The zero-based location in the response string where the highlight ends.

SourceDocuments -> (list)

The list of document IDs and their fields/attributes that are used for a single query suggestion, if document fields set to use for query suggestions.

(structure)

The document ID and its fields/attributes that are used for a query suggestion, if document fields set to use for query suggestions.

DocumentId -> (string)

The identifier of the document used for a query suggestion.

SuggestionAttributes -> (list)

The document fields/attributes used for a query suggestion.

(string)

AdditionalAttributes -> (list)

The additional fields/attributes to include in the response. You can use additional fields to provide extra information in the response. Additional fields are not used to based suggestions on.

(structure)

A document attribute or metadata field. To create custom document attributes, see [Custom attributes](https://docs.aws.amazon.com/kendra/latest/dg/custom-attributes.html) .

Key -> (string)

The identifier for the attribute.

Value -> (structure)

The value of the attribute.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.