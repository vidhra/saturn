# queryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/query.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/query.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# query

## Description

Searches an index given an input query.

### Note

If you are working with large language models (LLMs) or implementing retrieval augmented generation (RAG) systems, you can use Amazon Kendraâs [Retrieve](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Retrieve.html) API, which can return longer semantically relevant passages. We recommend using the `Retrieve` API instead of filing a service limit increase to increase the `Query` API document excerpt length.

You can configure boosting or relevance tuning at the query level to override boosting at the index level, filter based on document fields/attributes and faceted search, and filter based on the user or their group access to documents. You can also include certain fields in the response that might provide useful additional information.

A query response contains three types of results.

- Relevant suggested answers. The answers can be either a text excerpt or table excerpt. The answer can be highlighted in the excerpt.
- Matching FAQs or questions-answer from your FAQ file.
- Relevant documents. This result type includes an excerpt of the document with the document title. The searched terms can be highlighted in the excerpt.

You can specify that the query return only one type of result using the `QueryResultTypeFilter` parameter. Each query returns the 100 most relevant results. If you filter result type to only question-answers, a maximum of four results are returned. If you filter result type to only answers, a maximum of three results are returned.

### Warning

If youâre using an Amazon Kendra Gen AI Enterprise Edition index, you can only use `ATTRIBUTE_FILTER` to filter search results by user context. If youâre using an Amazon Kendra Gen AI Enterprise Edition index and you try to use `USER_TOKEN` to configure user context policy, Amazon Kendra returns a `ValidationException` error.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/Query)

## Synopsis

```
query
--index-id <value>
[--query-text <value>]
[--attribute-filter <value>]
[--facets <value>]
[--requested-document-attributes <value>]
[--query-result-type-filter <value>]
[--document-relevance-override-configurations <value>]
[--page-number <value>]
[--page-size <value>]
[--sorting-configuration <value>]
[--sorting-configurations <value>]
[--user-context <value>]
[--visitor-id <value>]
[--spell-correction-configuration <value>]
[--collapse-configuration <value>]
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

The identifier of the index for the search.

`--query-text` (string)

The input query text for the search. Amazon Kendra truncates queries at 30 token words, which excludes punctuation and stop words. Truncation still applies if you use Boolean or more advanced, complex queries. For example, `Timeoff AND October AND Category:HR` is counted as 3 tokens: `timeoff` , `october` , `hr` . For more information, see [Searching with advanced query syntax](https://docs.aws.amazon.com/kendra/latest/dg/searching-example.html#searching-index-query-syntax) in the Amazon Kendra Developer Guide.

`--attribute-filter` (structure)

Filters search results by document fields/attributes. You can only provide one attribute filter; however, the `AndAllFilters` , `NotFilter` , and `OrAllFilters` parameters contain a list of other filters.

The `AttributeFilter` parameter means you can create a set of filtering rules that a document must satisfy to be included in the query results.

### Note

For Amazon Kendra Gen AI Enterprise Edition indices use `AttributeFilter` to enable document filtering for end users using `_email_id` or include public documents (`_email_id=null` ).

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

JSON Syntax:

```
{
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
}
```

`--facets` (list)

An array of documents fields/attributes for faceted search. Amazon Kendra returns a count for each field key specified. This helps your users narrow their search.

(structure)

Information about a document attribute or field. You can use document attributes as facets.

For example, the document attribute or facet âDepartmentâ includes the values âHRâ, âEngineeringâ, and âAccountingâ. You can display these values in the search results so that documents can be searched by department.

You can display up to 10 facet values per facet for a query. If you want to increase this limit, contact [Support](http://aws.amazon.com/contact-us/) .

DocumentAttributeKey -> (string)

The unique key for the document attribute.

Facets -> (list)

An array of document attributes that are nested facets within a facet.

For example, the document attribute or facet âDepartmentâ includes a value called âEngineeringâ. In addition, the document attribute or facet âSubDepartmentâ includes the values âFrontendâ and âBackendâ for documents assigned to âEngineeringâ. You can display nested facets in the search results so that documents can be searched not only by department but also by a sub department within a department. This helps your users further narrow their search.

You can only have one nested facet within a facet. If you want to increase this limit, contact [Support](http://aws.amazon.com/contact-us/) .

(structure)

Information about a document attribute or field. You can use document attributes as facets.

For example, the document attribute or facet âDepartmentâ includes the values âHRâ, âEngineeringâ, and âAccountingâ. You can display these values in the search results so that documents can be searched by department.

You can display up to 10 facet values per facet for a query. If you want to increase this limit, contact [Support](http://aws.amazon.com/contact-us/) .

DocumentAttributeKey -> (string)

The unique key for the document attribute.

MaxResults -> (integer)

Maximum number of facet values per facet. The default is 10. You can use this to limit the number of facet values to less than 10. If you want to increase the default, contact [Support](http://aws.amazon.com/contact-us/) .

MaxResults -> (integer)

Maximum number of facet values per facet. The default is 10. You can use this to limit the number of facet values to less than 10. If you want to increase the default, contact [Support](http://aws.amazon.com/contact-us/) .

Shorthand Syntax:

```
DocumentAttributeKey=string,Facets=[{DocumentAttributeKey=string,( ... recursive ... ),MaxResults=integer},{DocumentAttributeKey=string,( ... recursive ... ),MaxResults=integer}],MaxResults=integer ...
```

JSON Syntax:

```
[
  {
    "DocumentAttributeKey": "string",
    "Facets": [
      {
        "DocumentAttributeKey": "string",
        "Facets": ,
        "MaxResults": integer
      }
      ...
    ],
    "MaxResults": integer
  }
  ...
]
```

`--requested-document-attributes` (list)

An array of document fields/attributes to include in the response. You can limit the response to include certain document fields. By default, all document attributes are included in the response.

(string)

Syntax:

```
"string" "string" ...
```

`--query-result-type-filter` (string)

Sets the type of query result or response. Only results for the specified type are returned.

Possible values:

- `DOCUMENT`
- `QUESTION_ANSWER`
- `ANSWER`

`--document-relevance-override-configurations` (list)

Overrides relevance tuning configurations of fields/attributes set at the index level.

If you use this API to override the relevance tuning configured at the index level, but there is no relevance tuning configured at the index level, then Amazon Kendra does not apply any relevance tuning.

If there is relevance tuning configured for fields at the index level, and you use this API to override only some of these fields, then for the fields you did not override, the importance is set to 1.

(structure)

Overrides the document relevance properties of a custom index field.

Name -> (string)

The name of the index field.

Relevance -> (structure)

Provides information for tuning the relevance of a field in a search. When a query includes terms that match the field, the results are given a boost in the response based on these tuning parameters.

Freshness -> (boolean)

Indicates that this field determines how âfreshâ a document is. For example, if document 1 was created on November 5, and document 2 was created on October 31, document 1 is âfresherâ than document 2. Only applies to `DATE` fields.

Importance -> (integer)

The relative importance of the field in the search. Larger numbers provide more of a boost than smaller numbers.

Duration -> (string)

Specifies the time period that the boost applies to. For example, to make the boost apply to documents with the field value within the last month, you would use â2628000sâ. Once the field value is beyond the specified range, the effect of the boost drops off. The higher the importance, the faster the effect drops off. If you donât specify a value, the default is 3 months. The value of the field is a numeric string followed by the character âsâ, for example â86400sâ for one day, or â604800sâ for one week.

Only applies to `DATE` fields.

RankOrder -> (string)

Determines how values should be interpreted.

When the `RankOrder` field is `ASCENDING` , higher numbers are better. For example, a document with a rating score of 10 is higher ranking than a document with a rating score of 1.

When the `RankOrder` field is `DESCENDING` , lower numbers are better. For example, in a task tracking application, a priority 1 task is more important than a priority 5 task.

Only applies to `LONG` fields.

ValueImportanceMap -> (map)

A list of values that should be given a different boost when they appear in the result list. For example, if you are boosting a field called âdepartmentâ, query terms that match the department field are boosted in the result. However, you can add entries from the department field to boost documents with those values higher.

For example, you can add entries to the map with names of departments. If you add âHRâ,5 and âLegalâ,3 those departments are given special attention when they appear in the metadata of a document. When those terms appear they are given the specified importance instead of the regular importance for the boost.

key -> (string)

value -> (integer)

Shorthand Syntax:

```
Name=string,Relevance={Freshness=boolean,Importance=integer,Duration=string,RankOrder=string,ValueImportanceMap={KeyName1=integer,KeyName2=integer}} ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Relevance": {
      "Freshness": true|false,
      "Importance": integer,
      "Duration": "string",
      "RankOrder": "ASCENDING"|"DESCENDING",
      "ValueImportanceMap": {"string": integer
        ...}
    }
  }
  ...
]
```

`--page-number` (integer)

Query results are returned in pages the size of the `PageSize` parameter. By default, Amazon Kendra returns the first page of results. Use this parameter to get result pages after the first one.

`--page-size` (integer)

Sets the number of results that are returned in each page of results. The default page size is 10. The maximum number of results returned is 100. If you ask for more than 100 results, only 100 are returned.

`--sorting-configuration` (structure)

Provides information that determines how the results of the query are sorted. You can set the field that Amazon Kendra should sort the results on, and specify whether the results should be sorted in ascending or descending order. In the case of ties in sorting the results, the results are sorted by relevance.

If you donât provide sorting configuration, the results are sorted by the relevance that Amazon Kendra determines for the result.

DocumentAttributeKey -> (string)

The name of the document attribute used to sort the response. You can use any field that has the `Sortable` flag set to true.

You can also sort by any of the following built-in attributes:

- _category
- _created_at
- _last_updated_at
- _version
- _view_count

SortOrder -> (string)

The order that the results should be returned in. In case of ties, the relevance assigned to the result by Amazon Kendra is used as the tie-breaker.

Shorthand Syntax:

```
DocumentAttributeKey=string,SortOrder=string
```

JSON Syntax:

```
{
  "DocumentAttributeKey": "string",
  "SortOrder": "DESC"|"ASC"
}
```

`--sorting-configurations` (list)

Provides configuration information to determine how the results of a query are sorted.

You can set upto 3 fields that Amazon Kendra should sort the results on, and specify whether the results should be sorted in ascending or descending order. The sort field quota can be increased.

If you donât provide a sorting configuration, the results are sorted by the relevance that Amazon Kendra determines for the result. In the case of ties in sorting the results, the results are sorted by relevance.

(structure)

Specifies the document attribute to use to sort the response to a Amazon Kendra query. You can specify a single attribute for sorting. The attribute must have the `Sortable` flag set to `true` , otherwise Amazon Kendra returns an exception.

You can sort attributes of the following types.

- Date value
- Long value
- String value

You canât sort attributes of the following type.

- String list value

DocumentAttributeKey -> (string)

The name of the document attribute used to sort the response. You can use any field that has the `Sortable` flag set to true.

You can also sort by any of the following built-in attributes:

- _category
- _created_at
- _last_updated_at
- _version
- _view_count

SortOrder -> (string)

The order that the results should be returned in. In case of ties, the relevance assigned to the result by Amazon Kendra is used as the tie-breaker.

Shorthand Syntax:

```
DocumentAttributeKey=string,SortOrder=string ...
```

JSON Syntax:

```
[
  {
    "DocumentAttributeKey": "string",
    "SortOrder": "DESC"|"ASC"
  }
  ...
]
```

`--user-context` (structure)

The user context token or user and group information.

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

Shorthand Syntax:

```
Token=string,UserId=string,Groups=string,string,DataSourceGroups=[{GroupId=string,DataSourceId=string},{GroupId=string,DataSourceId=string}]
```

JSON Syntax:

```
{
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
```

`--visitor-id` (string)

Provides an identifier for a specific user. The `VisitorId` should be a unique identifier, such as a GUID. Donât use personally identifiable information, such as the userâs email address, as the `VisitorId` .

`--spell-correction-configuration` (structure)

Enables suggested spell corrections for queries.

IncludeQuerySpellCheckSuggestions -> (boolean)

`TRUE` to suggest spell corrections for queries.

Shorthand Syntax:

```
IncludeQuerySpellCheckSuggestions=boolean
```

JSON Syntax:

```
{
  "IncludeQuerySpellCheckSuggestions": true|false
}
```

`--collapse-configuration` (structure)

Provides configuration to determine how to group results by document attribute value, and how to display them (collapsed or expanded) under a designated primary document for each group.

DocumentAttributeKey -> (string)

The document attribute used to group search results. You can use any attribute that has the `Sortable` flag set to true. You can also sort by any of the following built-in attributes:â_categoryâ,â_created_atâ, â_last_updated_atâ, â_versionâ, â_view_countâ.

SortingConfigurations -> (list)

A prioritized list of document attributes/fields that determine the primary document among those in a collapsed group.

(structure)

Specifies the document attribute to use to sort the response to a Amazon Kendra query. You can specify a single attribute for sorting. The attribute must have the `Sortable` flag set to `true` , otherwise Amazon Kendra returns an exception.

You can sort attributes of the following types.

- Date value
- Long value
- String value

You canât sort attributes of the following type.

- String list value

DocumentAttributeKey -> (string)

The name of the document attribute used to sort the response. You can use any field that has the `Sortable` flag set to true.

You can also sort by any of the following built-in attributes:

- _category
- _created_at
- _last_updated_at
- _version
- _view_count

SortOrder -> (string)

The order that the results should be returned in. In case of ties, the relevance assigned to the result by Amazon Kendra is used as the tie-breaker.

MissingAttributeKeyStrategy -> (string)

Specifies the behavior for documents without a value for the collapse attribute.

Amazon Kendra offers three customization options:

- Choose to `COLLAPSE` all documents with null or missing values in one group. This is the default configuration.
- Choose to `IGNORE` documents with null or missing values. Ignored documents will not appear in query results.
- Choose to `EXPAND` each document with a null or missing value into a group of its own.

Expand -> (boolean)

Specifies whether to expand the collapsed results.

ExpandConfiguration -> (structure)

Provides configuration information to customize expansion options for a collapsed group.

MaxResultItemsToExpand -> (integer)

The number of collapsed search result groups to expand. If you set this value to 10, for example, only the first 10 out of 100 result groups will have expand functionality.

MaxExpandedResultsPerItem -> (integer)

The number of expanded results to show per collapsed primary document. For instance, if you set this value to 3, then at most 3 results per collapsed group will be displayed.

Shorthand Syntax:

```
DocumentAttributeKey=string,SortingConfigurations=[{DocumentAttributeKey=string,SortOrder=string},{DocumentAttributeKey=string,SortOrder=string}],MissingAttributeKeyStrategy=string,Expand=boolean,ExpandConfiguration={MaxResultItemsToExpand=integer,MaxExpandedResultsPerItem=integer}
```

JSON Syntax:

```
{
  "DocumentAttributeKey": "string",
  "SortingConfigurations": [
    {
      "DocumentAttributeKey": "string",
      "SortOrder": "DESC"|"ASC"
    }
    ...
  ],
  "MissingAttributeKeyStrategy": "IGNORE"|"COLLAPSE"|"EXPAND",
  "Expand": true|false,
  "ExpandConfiguration": {
    "MaxResultItemsToExpand": integer,
    "MaxExpandedResultsPerItem": integer
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

QueryId -> (string)

The identifier for the search. You also use `QueryId` to identify the search when using the [SubmitFeedback](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SubmitFeedback.html) API.

ResultItems -> (list)

The results of the search.

(structure)

A single query result.

A query result contains information about a document returned by the query. This includes the original location of the document, a list of attributes assigned to the document, and relevant text from the document that satisfies the query.

Id -> (string)

The unique identifier for the query result item id (`Id` ) and the query result item document id (`DocumentId` ) combined. The value of this field changes with every request, even when you have the same documents.

Type -> (string)

The type of document within the response. For example, a response could include a question-answer thatâs relevant to the query.

Format -> (string)

If the `Type` of document within the response is `ANSWER` , then it is either a `TABLE` answer or `TEXT` answer. If itâs a table answer, a table excerpt is returned in `TableExcerpt` . If itâs a text answer, a text excerpt is returned in `DocumentExcerpt` .

AdditionalAttributes -> (list)

One or more additional fields/attributes associated with the query result.

(structure)

An attribute returned from an index query.

Key -> (string)

The key that identifies the attribute.

ValueType -> (string)

The data type of the `Value` property.

Value -> (structure)

An object that contains the attribute value.

TextWithHighlightsValue -> (structure)

The text associated with the attribute and information about the highlight to apply to the text.

Text -> (string)

The text to display to the user.

Highlights -> (list)

The beginning and end of the text that should be highlighted.

(structure)

Provides information that you can use to highlight a search result so that your users can quickly identify terms in the response.

BeginOffset -> (integer)

The zero-based location in the response string where the highlight starts.

EndOffset -> (integer)

The zero-based location in the response string where the highlight ends.

TopAnswer -> (boolean)

Indicates whether the response is the best response. True if this is the best response; otherwise, false.

Type -> (string)

The highlight type.

DocumentId -> (string)

The identifier for the document.

DocumentTitle -> (structure)

The title of the document. Contains the text of the title and information for highlighting the relevant terms in the title.

Text -> (string)

The text to display to the user.

Highlights -> (list)

The beginning and end of the text that should be highlighted.

(structure)

Provides information that you can use to highlight a search result so that your users can quickly identify terms in the response.

BeginOffset -> (integer)

The zero-based location in the response string where the highlight starts.

EndOffset -> (integer)

The zero-based location in the response string where the highlight ends.

TopAnswer -> (boolean)

Indicates whether the response is the best response. True if this is the best response; otherwise, false.

Type -> (string)

The highlight type.

DocumentExcerpt -> (structure)

An extract of the text in the document. Contains information about highlighting the relevant terms in the excerpt.

Text -> (string)

The text to display to the user.

Highlights -> (list)

The beginning and end of the text that should be highlighted.

(structure)

Provides information that you can use to highlight a search result so that your users can quickly identify terms in the response.

BeginOffset -> (integer)

The zero-based location in the response string where the highlight starts.

EndOffset -> (integer)

The zero-based location in the response string where the highlight ends.

TopAnswer -> (boolean)

Indicates whether the response is the best response. True if this is the best response; otherwise, false.

Type -> (string)

The highlight type.

DocumentURI -> (string)

The URI of the original location of the document.

DocumentAttributes -> (list)

An array of document fields/attributes assigned to a document in the search results. For example, the document author (`_author` ) or the source URI (`_source_uri` ) of the document.

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

ScoreAttributes -> (structure)

Indicates the confidence level of Amazon Kendra providing a relevant result for the query. Each result is placed into a bin that indicates the confidence, `VERY_HIGH` , `HIGH` , `MEDIUM` and `LOW` . You can use the score to determine if a response meets the confidence needed for your application.

The field is only set to `LOW` when the `Type` field is set to `DOCUMENT` and Amazon Kendra is not confident that the result is relevant to the query.

ScoreConfidence -> (string)

A relative ranking for how relevant the response is to the query.

FeedbackToken -> (string)

A token that identifies a particular result from a particular query. Use this token to provide click-through feedback for the result. For more information, see [Submitting feedback](https://docs.aws.amazon.com/kendra/latest/dg/submitting-feedback.html) .

TableExcerpt -> (structure)

An excerpt from a table within a document.

Rows -> (list)

A list of rows in the table excerpt.

(structure)

Information about a row in a table excerpt.

Cells -> (list)

A list of table cells in a row.

(structure)

Provides information about a table cell in a table excerpt.

Value -> (string)

The actual value or content within a table cell. A table cell could contain a date value of a year, or a string value of text, for example.

TopAnswer -> (boolean)

`TRUE` if the response of the table cell is the top answer. This is the cell value or content with the highest confidence score or is the most relevant to the query.

Highlighted -> (boolean)

`TRUE` means that the table cell has a high enough confidence and is relevant to the query, so the value or content should be highlighted.

Header -> (boolean)

`TRUE` means that the table cell should be treated as a header.

TotalNumberOfRows -> (integer)

A count of the number of rows in the original table within the document.

CollapsedResultDetail -> (structure)

Provides details about a collapsed group of search results.

DocumentAttribute -> (structure)

The value of the document attribute that results are collapsed on.

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

ExpandedResults -> (list)

A list of results in the collapsed group.

(structure)

A single expanded result in a collapsed group of search results.

An expanded result item contains information about an expanded result document within a collapsed group of search results. This includes the original location of the document, a list of attributes assigned to the document, and relevant text from the document that satisfies the query.

Id -> (string)

The identifier for the expanded result.

DocumentId -> (string)

The idenitifier of the document.

DocumentTitle -> (structure)

Provides text and information about where to highlight the text.

Text -> (string)

The text to display to the user.

Highlights -> (list)

The beginning and end of the text that should be highlighted.

(structure)

Provides information that you can use to highlight a search result so that your users can quickly identify terms in the response.

BeginOffset -> (integer)

The zero-based location in the response string where the highlight starts.

EndOffset -> (integer)

The zero-based location in the response string where the highlight ends.

TopAnswer -> (boolean)

Indicates whether the response is the best response. True if this is the best response; otherwise, false.

Type -> (string)

The highlight type.

DocumentExcerpt -> (structure)

Provides text and information about where to highlight the text.

Text -> (string)

The text to display to the user.

Highlights -> (list)

The beginning and end of the text that should be highlighted.

(structure)

Provides information that you can use to highlight a search result so that your users can quickly identify terms in the response.

BeginOffset -> (integer)

The zero-based location in the response string where the highlight starts.

EndOffset -> (integer)

The zero-based location in the response string where the highlight ends.

TopAnswer -> (boolean)

Indicates whether the response is the best response. True if this is the best response; otherwise, false.

Type -> (string)

The highlight type.

DocumentURI -> (string)

The URI of the original location of the document.

DocumentAttributes -> (list)

An array of document attributes assigned to a document in the search results. For example, the document author (â_authorâ) or the source URI (â_source_uriâ) of the document.

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

FacetResults -> (list)

Contains the facet results. A `FacetResult` contains the counts for each field/attribute key that was specified in the `Facets` input parameter.

(structure)

The facet values for the documents in the response.

DocumentAttributeKey -> (string)

The key for the facet values. This is the same as the `DocumentAttributeKey` provided in the query.

DocumentAttributeValueType -> (string)

The data type of the facet value. This is the same as the type defined for the index field when it was created.

DocumentAttributeValueCountPairs -> (list)

An array of key/value pairs, where the key is the value of the attribute and the count is the number of documents that share the key value.

(structure)

Provides the count of documents that match a particular document attribute or field when doing a faceted search.

DocumentAttributeValue -> (structure)

The value of the attribute/field. For example, âHRâ.

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

Count -> (integer)

The number of documents in the response that have the attribute/field value for the key.

FacetResults -> (list)

Contains the results of a document attribute/field that is a nested facet. A `FacetResult` contains the counts for each facet nested within a facet.

For example, the document attribute or facet âDepartmentâ includes a value called âEngineeringâ. In addition, the document attribute or facet âSubDepartmentâ includes the values âFrontendâ and âBackendâ for documents assigned to âEngineeringâ. You can display nested facets in the search results so that documents can be searched not only by department but also by a sub department within a department. The counts for documents that belong to âFrontendâ and âBackendâ within âEngineeringâ are returned for a query.

(structure)

The facet values for the documents in the response.

DocumentAttributeKey -> (string)

The key for the facet values. This is the same as the `DocumentAttributeKey` provided in the query.

DocumentAttributeValueType -> (string)

The data type of the facet value. This is the same as the type defined for the index field when it was created.

DocumentAttributeValueCountPairs -> (list)

An array of key/value pairs, where the key is the value of the attribute and the count is the number of documents that share the key value.

(structure)

Provides the count of documents that match a particular document attribute or field when doing a faceted search.

DocumentAttributeValue -> (structure)

The value of the attribute/field. For example, âHRâ.

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

Count -> (integer)

The number of documents in the response that have the attribute/field value for the key.

TotalNumberOfResults -> (integer)

The total number of items found by the search. However, you can only retrieve up to 100 items. For example, if the search found 192 items, you can only retrieve the first 100 of the items.

Warnings -> (list)

A list of warning codes and their messages on problems with your query.

Amazon Kendra currently only supports one type of warning, which is a warning on invalid syntax used in the query. For examples of invalid query syntax, see [Searching with advanced query syntax](https://docs.aws.amazon.com/kendra/latest/dg/searching-example.html#searching-index-query-syntax) .

(structure)

The warning code and message that explains a problem with a query.

Message -> (string)

The message that explains the problem with the query.

Code -> (string)

The code used to show the type of warning for the query.

SpellCorrectedQueries -> (list)

A list of information related to suggested spell corrections for a query.

(structure)

A query with suggested spell corrections.

SuggestedQueryText -> (string)

The query with the suggested spell corrections.

Corrections -> (list)

The corrected misspelled word or words in a query.

(structure)

A corrected misspelled word in a query.

BeginOffset -> (integer)

The zero-based location in the response string or text where the corrected word starts.

EndOffset -> (integer)

The zero-based location in the response string or text where the corrected word ends.

Term -> (string)

The string or text of a misspelled word in a query.

CorrectedTerm -> (string)

The string or text of a corrected misspelled word in a query.

FeaturedResultsItems -> (list)

The list of featured result items. Featured results are displayed at the top of the search results page, placed above all other results for certain queries. If thereâs an exact match of a query, then certain documents are featured in the search results.

(structure)

A single featured result item. A featured result is displayed at the top of the search results page, placed above all other results for certain queries. If thereâs an exact match of a query, then certain documents are featured in the search results.

Id -> (string)

The identifier of the featured result.

Type -> (string)

The type of document within the featured result response. For example, a response could include a question-answer type thatâs relevant to the query.

AdditionalAttributes -> (list)

One or more additional attributes associated with the featured result.

(structure)

An attribute returned from an index query.

Key -> (string)

The key that identifies the attribute.

ValueType -> (string)

The data type of the `Value` property.

Value -> (structure)

An object that contains the attribute value.

TextWithHighlightsValue -> (structure)

The text associated with the attribute and information about the highlight to apply to the text.

Text -> (string)

The text to display to the user.

Highlights -> (list)

The beginning and end of the text that should be highlighted.

(structure)

Provides information that you can use to highlight a search result so that your users can quickly identify terms in the response.

BeginOffset -> (integer)

The zero-based location in the response string where the highlight starts.

EndOffset -> (integer)

The zero-based location in the response string where the highlight ends.

TopAnswer -> (boolean)

Indicates whether the response is the best response. True if this is the best response; otherwise, false.

Type -> (string)

The highlight type.

DocumentId -> (string)

The identifier of the featured document.

DocumentTitle -> (structure)

Provides text and information about where to highlight the text.

Text -> (string)

The text to display to the user.

Highlights -> (list)

The beginning and end of the text that should be highlighted.

(structure)

Provides information that you can use to highlight a search result so that your users can quickly identify terms in the response.

BeginOffset -> (integer)

The zero-based location in the response string where the highlight starts.

EndOffset -> (integer)

The zero-based location in the response string where the highlight ends.

TopAnswer -> (boolean)

Indicates whether the response is the best response. True if this is the best response; otherwise, false.

Type -> (string)

The highlight type.

DocumentExcerpt -> (structure)

Provides text and information about where to highlight the text.

Text -> (string)

The text to display to the user.

Highlights -> (list)

The beginning and end of the text that should be highlighted.

(structure)

Provides information that you can use to highlight a search result so that your users can quickly identify terms in the response.

BeginOffset -> (integer)

The zero-based location in the response string where the highlight starts.

EndOffset -> (integer)

The zero-based location in the response string where the highlight ends.

TopAnswer -> (boolean)

Indicates whether the response is the best response. True if this is the best response; otherwise, false.

Type -> (string)

The highlight type.

DocumentURI -> (string)

The source URI location of the featured document.

DocumentAttributes -> (list)

An array of document attributes assigned to a featured document in the search results. For example, the document author (`_author` ) or the source URI (`_source_uri` ) of the document.

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

FeedbackToken -> (string)

A token that identifies a particular featured result from a particular query. Use this token to provide click-through feedback for the result. For more information, see [Submitting feedback](https://docs.aws.amazon.com/kendra/latest/dg/submitting-feedback.html) .