# retrieveÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/retrieve.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/retrieve.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# retrieve

## Description

Retrieves relevant passages or text excerpts given an input query.

This API is similar to the [Query](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Query.html) API. However, by default, the `Query` API only returns excerpt passages of up to 100 token words. With the `Retrieve` API, you can retrieve longer passages of up to 200 token words and up to 100 semantically relevant passages. This doesnât include question-answer or FAQ type responses from your index. The passages are text excerpts that can be semantically extracted from multiple documents and multiple parts of the same document. If in extreme cases your documents produce zero passages using the `Retrieve` API, you can alternatively use the `Query` API and its types of responses.

You can also do the following:

- Override boosting at the index level
- Filter based on document fields or attributes
- Filter based on the user or their group access to documents
- View the confidence score bucket for a retrieved passage result. The confidence bucket provides a relative ranking that indicates how confident Amazon Kendra is that the response is relevant to the query.

### Note

Confidence score buckets are currently available only for English.

You can also include certain fields in the response that might provide useful additional information.

The `Retrieve` API shares the number of [query capacity units](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CapacityUnitsConfiguration.html) that you set for your index. For more information on whatâs included in a single capacity unit and the default base capacity for an index, see [Adjusting capacity](https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html) .

### Warning

If youâre using an Amazon Kendra Gen AI Enterprise Edition index, you can only use `ATTRIBUTE_FILTER` to filter search results by user context. If youâre using an Amazon Kendra Gen AI Enterprise Edition index and you try to use `USER_TOKEN` to configure user context policy, Amazon Kendra returns a `ValidationException` error.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/Retrieve)

## Synopsis

```
retrieve
--index-id <value>
--query-text <value>
[--attribute-filter <value>]
[--requested-document-attributes <value>]
[--document-relevance-override-configurations <value>]
[--page-number <value>]
[--page-size <value>]
[--user-context <value>]
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

The identifier of the index to retrieve relevant passages for the search.

`--query-text` (string)

The input query text to retrieve relevant passages for the search. Amazon Kendra truncates queries at 30 token words, which excludes punctuation and stop words. Truncation still applies if you use Boolean or more advanced, complex queries. For example, `Timeoff AND October AND Category:HR` is counted as 3 tokens: `timeoff` , `october` , `hr` . For more information, see [Searching with advanced query syntax](https://docs.aws.amazon.com/kendra/latest/dg/searching-example.html#searching-index-query-syntax) in the Amazon Kendra Developer Guide.

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

`--requested-document-attributes` (list)

A list of document fields/attributes to include in the response. You can limit the response to include certain document fields. By default, all document fields are included in the response.

(string)

Syntax:

```
"string" "string" ...
```

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

Retrieved relevant passages are returned in pages the size of the `PageSize` parameter. By default, Amazon Kendra returns the first page of results. Use this parameter to get result pages after the first one.

`--page-size` (integer)

Sets the number of retrieved relevant passages that are returned in each page of results. The default page size is 10. The maximum number of results returned is 100. If you ask for more than 100 results, only 100 are returned.

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

The identifier of query used for the search. You also use `QueryId` to identify the search when using the [Submitfeedback](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SubmitFeedback.html) API.

ResultItems -> (list)

The results of the retrieved relevant passages for the search.

(structure)

A single retrieved relevant passage result.

Id -> (string)

The identifier of the relevant passage result.

DocumentId -> (string)

The identifier of the document.

DocumentTitle -> (string)

The title of the document.

Content -> (string)

The contents of the relevant passage.

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

The confidence score bucket for a retrieved passage result. The confidence bucket provides a relative ranking that indicates how confident Amazon Kendra is that the response is relevant to the query.

ScoreConfidence -> (string)

A relative ranking for how relevant the response is to the query.