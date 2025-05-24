# retrieveÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent-runtime/retrieve.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent-runtime/retrieve.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock-agent-runtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent-runtime/index.html#cli-aws-bedrock-agent-runtime) ]

# retrieve

## Description

Queries a knowledge base and retrieves information from it.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agent-runtime-2023-07-26/Retrieve)

`retrieve` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

`retrieve` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `retrievalResults`

## Synopsis

```
retrieve
[--guardrail-configuration <value>]
--knowledge-base-id <value>
[--retrieval-configuration <value>]
--retrieval-query <value>
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--max-items <value>]
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

`--guardrail-configuration` (structure)

Guardrail settings.

guardrailId -> (string)

The unique identifier for the guardrail.

guardrailVersion -> (string)

The version of the guardrail.

Shorthand Syntax:

```
guardrailId=string,guardrailVersion=string
```

JSON Syntax:

```
{
  "guardrailId": "string",
  "guardrailVersion": "string"
}
```

`--knowledge-base-id` (string)

The unique identifier of the knowledge base to query.

`--retrieval-configuration` (structure)

Contains configurations for the knowledge base query and retrieval process. For more information, see [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html) .

vectorSearchConfiguration -> (structure)

Contains details about how the results from the vector search should be returned. For more information, see [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html) .

filter -> (tagged union structure)

Specifies the filters to use on the metadata in the knowledge base data sources before returning results. For more information, see [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html) .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `andAll`, `equals`, `greaterThan`, `greaterThanOrEquals`, `in`, `lessThan`, `lessThanOrEquals`, `listContains`, `notEquals`, `notIn`, `orAll`, `startsWith`, `stringContains`.

andAll -> (list)

Knowledge base data sources are returned if their metadata attributes fulfill all the filter conditions inside this list.

(tagged union structure)

Specifies the filters to use on the metadata attributes in the knowledge base data sources before returning results. For more information, see [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html) . See the examples below to see how to use these filters.

This data type is used in the following API operations:

- [Retrieve request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html#API_agent-runtime_Retrieve_RequestSyntax) â in the `filter` field
- [RetrieveAndGenerate request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html#API_agent-runtime_RetrieveAndGenerate_RequestSyntax) â in the `filter` field

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `andAll`, `equals`, `greaterThan`, `greaterThanOrEquals`, `in`, `lessThan`, `lessThanOrEquals`, `listContains`, `notEquals`, `notIn`, `orAll`, `startsWith`, `stringContains`.

andAll -> (list)

Knowledge base data sources are returned if their metadata attributes fulfill all the filter conditions inside this list.

( â¦ recursive â¦ )

equals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value matches the `value` in this object.

The following example would return data sources with an `animal` attribute whose value is `cat` :

`"equals": { "key": "animal", "value": "cat" }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

greaterThan -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is greater than the `value` in this object.

The following example would return data sources with an `year` attribute whose value is greater than `1989` :

`"greaterThan": { "key": "year", "value": 1989 }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

greaterThanOrEquals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is greater than or equal to the `value` in this object.

The following example would return data sources with an `year` attribute whose value is greater than or equal to `1989` :

`"greaterThanOrEquals": { "key": "year", "value": 1989 }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

in -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is in the list specified in the `value` in this object.

The following example would return data sources with an `animal` attribute that is either `cat` or `dog` :

`"in": { "key": "animal", "value": ["cat", "dog"] }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

lessThan -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is less than the `value` in this object.

The following example would return data sources with an `year` attribute whose value is less than to `1989` .

`"lessThan": { "key": "year", "value": 1989 }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

lessThanOrEquals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is less than or equal to the `value` in this object.

The following example would return data sources with an `year` attribute whose value is less than or equal to `1989` .

`"lessThanOrEquals": { "key": "year", "value": 1989 }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

listContains -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is a list that contains the `value` as one of its members.

The following example would return data sources with an `animals` attribute that is a list containing a `cat` member (for example `["dog", "cat"]` ).

`"listContains": { "key": "animals", "value": "cat" }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

notEquals -> (structure)

Knowledge base data sources are returned when:

- It contains a metadata attribute whose name matches the `key` and whose value doesnât match the `value` in this object.
- The key is not present in the document.

The following example would return data sources that donât contain an `animal` attribute whose value is `cat` .

`"notEquals": { "key": "animal", "value": "cat" }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

notIn -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value isnât in the list specified in the `value` in this object.

The following example would return data sources whose `animal` attribute is neither `cat` nor `dog` .

`"notIn": { "key": "animal", "value": ["cat", "dog"] }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

orAll -> (list)

Knowledge base data sources are returned if their metadata attributes fulfill at least one of the filter conditions inside this list.

( â¦ recursive â¦ )

startsWith -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value starts with the `value` in this object. This filter is currently only supported for Amazon OpenSearch Serverless vector stores.

The following example would return data sources with an `animal` attribute starts with `ca` (for example, `cat` or `camel` ).

`"startsWith": { "key": "animal", "value": "ca" }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

stringContains -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is one of the following:

- A string that contains the `value` as a substring. The following example would return data sources with an `animal` attribute that contains the substring `at` (for example `cat` ).  `"stringContains": { "key": "animal", "value": "at" }`
- A list with a member that contains the `value` as a substring. The following example would return data sources with an `animals` attribute that is a list containing a member that contains the substring `at` (for example `["dog", "cat"]` ).  `"stringContains": { "key": "animals", "value": "at" }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

equals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value matches the `value` in this object.

The following example would return data sources with an `animal` attribute whose value is `cat` :

`"equals": { "key": "animal", "value": "cat" }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

greaterThan -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is greater than the `value` in this object.

The following example would return data sources with an `year` attribute whose value is greater than `1989` :

`"greaterThan": { "key": "year", "value": 1989 }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

greaterThanOrEquals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is greater than or equal to the `value` in this object.

The following example would return data sources with an `year` attribute whose value is greater than or equal to `1989` :

`"greaterThanOrEquals": { "key": "year", "value": 1989 }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

in -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is in the list specified in the `value` in this object.

The following example would return data sources with an `animal` attribute that is either `cat` or `dog` :

`"in": { "key": "animal", "value": ["cat", "dog"] }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

lessThan -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is less than the `value` in this object.

The following example would return data sources with an `year` attribute whose value is less than to `1989` .

`"lessThan": { "key": "year", "value": 1989 }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

lessThanOrEquals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is less than or equal to the `value` in this object.

The following example would return data sources with an `year` attribute whose value is less than or equal to `1989` .

`"lessThanOrEquals": { "key": "year", "value": 1989 }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

listContains -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is a list that contains the `value` as one of its members.

The following example would return data sources with an `animals` attribute that is a list containing a `cat` member (for example `["dog", "cat"]` ).

`"listContains": { "key": "animals", "value": "cat" }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

notEquals -> (structure)

Knowledge base data sources are returned when:

- It contains a metadata attribute whose name matches the `key` and whose value doesnât match the `value` in this object.
- The key is not present in the document.

The following example would return data sources that donât contain an `animal` attribute whose value is `cat` .

`"notEquals": { "key": "animal", "value": "cat" }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

notIn -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value isnât in the list specified in the `value` in this object.

The following example would return data sources whose `animal` attribute is neither `cat` nor `dog` .

`"notIn": { "key": "animal", "value": ["cat", "dog"] }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

orAll -> (list)

Knowledge base data sources are returned if their metadata attributes fulfill at least one of the filter conditions inside this list.

(tagged union structure)

Specifies the filters to use on the metadata attributes in the knowledge base data sources before returning results. For more information, see [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html) . See the examples below to see how to use these filters.

This data type is used in the following API operations:

- [Retrieve request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html#API_agent-runtime_Retrieve_RequestSyntax) â in the `filter` field
- [RetrieveAndGenerate request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html#API_agent-runtime_RetrieveAndGenerate_RequestSyntax) â in the `filter` field

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `andAll`, `equals`, `greaterThan`, `greaterThanOrEquals`, `in`, `lessThan`, `lessThanOrEquals`, `listContains`, `notEquals`, `notIn`, `orAll`, `startsWith`, `stringContains`.

andAll -> (list)

Knowledge base data sources are returned if their metadata attributes fulfill all the filter conditions inside this list.

( â¦ recursive â¦ )

equals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value matches the `value` in this object.

The following example would return data sources with an `animal` attribute whose value is `cat` :

`"equals": { "key": "animal", "value": "cat" }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

greaterThan -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is greater than the `value` in this object.

The following example would return data sources with an `year` attribute whose value is greater than `1989` :

`"greaterThan": { "key": "year", "value": 1989 }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

greaterThanOrEquals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is greater than or equal to the `value` in this object.

The following example would return data sources with an `year` attribute whose value is greater than or equal to `1989` :

`"greaterThanOrEquals": { "key": "year", "value": 1989 }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

in -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is in the list specified in the `value` in this object.

The following example would return data sources with an `animal` attribute that is either `cat` or `dog` :

`"in": { "key": "animal", "value": ["cat", "dog"] }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

lessThan -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is less than the `value` in this object.

The following example would return data sources with an `year` attribute whose value is less than to `1989` .

`"lessThan": { "key": "year", "value": 1989 }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

lessThanOrEquals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is less than or equal to the `value` in this object.

The following example would return data sources with an `year` attribute whose value is less than or equal to `1989` .

`"lessThanOrEquals": { "key": "year", "value": 1989 }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

listContains -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is a list that contains the `value` as one of its members.

The following example would return data sources with an `animals` attribute that is a list containing a `cat` member (for example `["dog", "cat"]` ).

`"listContains": { "key": "animals", "value": "cat" }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

notEquals -> (structure)

Knowledge base data sources are returned when:

- It contains a metadata attribute whose name matches the `key` and whose value doesnât match the `value` in this object.
- The key is not present in the document.

The following example would return data sources that donât contain an `animal` attribute whose value is `cat` .

`"notEquals": { "key": "animal", "value": "cat" }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

notIn -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value isnât in the list specified in the `value` in this object.

The following example would return data sources whose `animal` attribute is neither `cat` nor `dog` .

`"notIn": { "key": "animal", "value": ["cat", "dog"] }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

orAll -> (list)

Knowledge base data sources are returned if their metadata attributes fulfill at least one of the filter conditions inside this list.

( â¦ recursive â¦ )

startsWith -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value starts with the `value` in this object. This filter is currently only supported for Amazon OpenSearch Serverless vector stores.

The following example would return data sources with an `animal` attribute starts with `ca` (for example, `cat` or `camel` ).

`"startsWith": { "key": "animal", "value": "ca" }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

stringContains -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is one of the following:

- A string that contains the `value` as a substring. The following example would return data sources with an `animal` attribute that contains the substring `at` (for example `cat` ).  `"stringContains": { "key": "animal", "value": "at" }`
- A list with a member that contains the `value` as a substring. The following example would return data sources with an `animals` attribute that is a list containing a member that contains the substring `at` (for example `["dog", "cat"]` ).  `"stringContains": { "key": "animals", "value": "at" }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

startsWith -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value starts with the `value` in this object. This filter is currently only supported for Amazon OpenSearch Serverless vector stores.

The following example would return data sources with an `animal` attribute starts with `ca` (for example, `cat` or `camel` ).

`"startsWith": { "key": "animal", "value": "ca" }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

stringContains -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the `key` and whose value is one of the following:

- A string that contains the `value` as a substring. The following example would return data sources with an `animal` attribute that contains the substring `at` (for example `cat` ).  `"stringContains": { "key": "animal", "value": "at" }`
- A list with a member that contains the `value` as a substring. The following example would return data sources with an `animals` attribute that is a list containing a member that contains the substring `at` (for example `["dog", "cat"]` ).  `"stringContains": { "key": "animals", "value": "at" }`

key -> (string)

The name that the metadata attribute must match.

value -> (document)

The value to whcih to compare the value of the metadata attribute.

implicitFilterConfiguration -> (structure)

Settings for implicit filtering.

metadataAttributes -> (list)

Metadata that can be used in a filter.

(structure)

Details about a metadata attribute.

description -> (string)

The attributeâs description.

key -> (string)

The attributeâs key.

type -> (string)

The attributeâs type.

modelArn -> (string)

The model that generates the filter.

numberOfResults -> (integer)

The number of source chunks to retrieve.

overrideSearchType -> (string)

By default, Amazon Bedrock decides a search strategy for you. If youâre using an Amazon OpenSearch Serverless vector store that contains a filterable text field, you can specify whether to query the knowledge base with a `HYBRID` search using both vector embeddings and raw text, or `SEMANTIC` search using only vector embeddings. For other vector store configurations, only `SEMANTIC` search is available. For more information, see [Test a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-test.html) .

rerankingConfiguration -> (structure)

Contains configurations for reranking the retrieved results. For more information, see [Improve the relevance of query responses with a reranker model](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html) .

bedrockRerankingConfiguration -> (structure)

Contains configurations for an Amazon Bedrock reranker model.

metadataConfiguration -> (structure)

Contains configurations for the metadata to use in reranking.

selectionMode -> (string)

Specifies whether to consider all metadata when reranking, or only the metadata that you select. If you specify `SELECTIVE` , include the `selectiveModeConfiguration` field.

selectiveModeConfiguration -> (tagged union structure)

Contains configurations for the metadata fields to include or exclude when considering reranking.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fieldsToExclude`, `fieldsToInclude`.

fieldsToExclude -> (list)

An array of objects, each of which specifies a metadata field to exclude from consideration when reranking.

(structure)

Contains information for a metadata field to include in or exclude from consideration when reranking.

fieldName -> (string)

The name of a metadata field to include in or exclude from consideration when reranking.

fieldsToInclude -> (list)

An array of objects, each of which specifies a metadata field to include in consideration when reranking. The remaining metadata fields are ignored.

(structure)

Contains information for a metadata field to include in or exclude from consideration when reranking.

fieldName -> (string)

The name of a metadata field to include in or exclude from consideration when reranking.

modelConfiguration -> (structure)

Contains configurations for the reranker model.

additionalModelRequestFields -> (map)

A JSON object whose keys are request fields for the model and whose values are values for those fields.

key -> (string)

value -> (document)

modelArn -> (string)

The ARN of the reranker model to use.

numberOfRerankedResults -> (integer)

The number of results to return after reranking.

type -> (string)

The type of reranker model.

JSON Syntax:

```
{
  "vectorSearchConfiguration": {
    "filter": {
      "andAll": [
        {
          "andAll": [
            { ... recursive ... }
            ...
          ],
          "equals": {
            "key": "string",
            "value": {...}
          },
          "greaterThan": {
            "key": "string",
            "value": {...}
          },
          "greaterThanOrEquals": {
            "key": "string",
            "value": {...}
          },
          "in": {
            "key": "string",
            "value": {...}
          },
          "lessThan": {
            "key": "string",
            "value": {...}
          },
          "lessThanOrEquals": {
            "key": "string",
            "value": {...}
          },
          "listContains": {
            "key": "string",
            "value": {...}
          },
          "notEquals": {
            "key": "string",
            "value": {...}
          },
          "notIn": {
            "key": "string",
            "value": {...}
          },
          "orAll": [
            { ... recursive ... }
            ...
          ],
          "startsWith": {
            "key": "string",
            "value": {...}
          },
          "stringContains": {
            "key": "string",
            "value": {...}
          }
        }
        ...
      ],
      "equals": {
        "key": "string",
        "value": {...}
      },
      "greaterThan": {
        "key": "string",
        "value": {...}
      },
      "greaterThanOrEquals": {
        "key": "string",
        "value": {...}
      },
      "in": {
        "key": "string",
        "value": {...}
      },
      "lessThan": {
        "key": "string",
        "value": {...}
      },
      "lessThanOrEquals": {
        "key": "string",
        "value": {...}
      },
      "listContains": {
        "key": "string",
        "value": {...}
      },
      "notEquals": {
        "key": "string",
        "value": {...}
      },
      "notIn": {
        "key": "string",
        "value": {...}
      },
      "orAll": [
        {
          "andAll": [
            { ... recursive ... }
            ...
          ],
          "equals": {
            "key": "string",
            "value": {...}
          },
          "greaterThan": {
            "key": "string",
            "value": {...}
          },
          "greaterThanOrEquals": {
            "key": "string",
            "value": {...}
          },
          "in": {
            "key": "string",
            "value": {...}
          },
          "lessThan": {
            "key": "string",
            "value": {...}
          },
          "lessThanOrEquals": {
            "key": "string",
            "value": {...}
          },
          "listContains": {
            "key": "string",
            "value": {...}
          },
          "notEquals": {
            "key": "string",
            "value": {...}
          },
          "notIn": {
            "key": "string",
            "value": {...}
          },
          "orAll": [
            { ... recursive ... }
            ...
          ],
          "startsWith": {
            "key": "string",
            "value": {...}
          },
          "stringContains": {
            "key": "string",
            "value": {...}
          }
        }
        ...
      ],
      "startsWith": {
        "key": "string",
        "value": {...}
      },
      "stringContains": {
        "key": "string",
        "value": {...}
      }
    },
    "implicitFilterConfiguration": {
      "metadataAttributes": [
        {
          "description": "string",
          "key": "string",
          "type": "STRING"|"NUMBER"|"BOOLEAN"|"STRING_LIST"
        }
        ...
      ],
      "modelArn": "string"
    },
    "numberOfResults": integer,
    "overrideSearchType": "HYBRID"|"SEMANTIC",
    "rerankingConfiguration": {
      "bedrockRerankingConfiguration": {
        "metadataConfiguration": {
          "selectionMode": "SELECTIVE"|"ALL",
          "selectiveModeConfiguration": {
            "fieldsToExclude": [
              {
                "fieldName": "string"
              }
              ...
            ],
            "fieldsToInclude": [
              {
                "fieldName": "string"
              }
              ...
            ]
          }
        },
        "modelConfiguration": {
          "additionalModelRequestFields": {"string": {...}
            ...},
          "modelArn": "string"
        },
        "numberOfRerankedResults": integer
      },
      "type": "BEDROCK_RERANKING_MODEL"
    }
  }
}
```

`--retrieval-query` (structure)

Contains the query to send the knowledge base.

text -> (string)

The text of the query made to the knowledge base.

Shorthand Syntax:

```
text=string
```

JSON Syntax:

```
{
  "text": "string"
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

guardrailAction -> (string)

Specifies if there is a guardrail intervention in the response.

nextToken -> (string)

If there are more results than can fit in the response, the response returns a `nextToken` . Use this token in the `nextToken` field of another request to retrieve the next batch of results.

retrievalResults -> (list)

A list of results from querying the knowledge base.

(structure)

Details about a result from querying the knowledge base.

This data type is used in the following API operations:

- [Retrieve response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html#API_agent-runtime_Retrieve_ResponseSyntax) â in the `retrievalResults` field

content -> (structure)

Contains information about the content of the chunk.

byteContent -> (string)

A data URI with base64-encoded content from the data source. The URI is in the following format: returned in the following format: `data:image/jpeg;base64,${base64-encoded string}` .

row -> (list)

Specifies information about the rows with the cells to return in retrieval.

(structure)

Contains information about a column with a cell to return in retrieval.

columnName -> (string)

The name of the column.

columnValue -> (string)

The value in the column.

type -> (string)

The data type of the value.

text -> (string)

The cited text from the data source.

type -> (string)

The type of content in the retrieval result.

location -> (structure)

Contains information about the location of the data source.

confluenceLocation -> (structure)

The Confluence data source location.

url -> (string)

The Confluence host URL for the data source location.

customDocumentLocation -> (structure)

Specifies the location of a document in a custom data source.

id -> (string)

The ID of the document.

kendraDocumentLocation -> (structure)

The location of a document in Amazon Kendra.

uri -> (string)

The documentâs uri.

s3Location -> (structure)

The S3 data source location.

uri -> (string)

The S3 URI for the data source location.

salesforceLocation -> (structure)

The Salesforce data source location.

url -> (string)

The Salesforce host URL for the data source location.

sharePointLocation -> (structure)

The SharePoint data source location.

url -> (string)

The SharePoint site URL for the data source location.

sqlLocation -> (structure)

Specifies information about the SQL query used to retrieve the result.

query -> (string)

The SQL query used to retrieve the result.

type -> (string)

The type of data source location.

webLocation -> (structure)

The web URL/URLs data source location.

url -> (string)

The web URL/URLs for the data source location.

metadata -> (map)

Contains metadata attributes and their values for the file in the data source. For more information, see [Metadata and filtering](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-ds.html#kb-ds-metadata) .

key -> (string)

value -> (document)

score -> (double)

The level of relevance of the result to the query.