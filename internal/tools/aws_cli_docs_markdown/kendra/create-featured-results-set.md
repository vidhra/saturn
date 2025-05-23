# create-featured-results-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-featured-results-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-featured-results-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# create-featured-results-set

## Description

Creates a set of featured results to display at the top of the search results page. Featured results are placed above all other results for certain queries. You map specific queries to specific documents for featuring in the results. If a query contains an exact match, then one or more specific documents are featured in the search results.

You can create up to 50 sets of featured results per index. You can request to increase this limit by contacting [Support](http://aws.amazon.com/contact-us/) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/CreateFeaturedResultsSet)

## Synopsis

```
create-featured-results-set
--index-id <value>
--featured-results-set-name <value>
[--description <value>]
[--client-token <value>]
[--status <value>]
[--query-texts <value>]
[--featured-documents <value>]
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

`--index-id` (string)

The identifier of the index that you want to use for featuring results.

`--featured-results-set-name` (string)

A name for the set of featured results.

`--description` (string)

A description for the set of featured results.

`--client-token` (string)

A token that you provide to identify the request to create a set of featured results. Multiple calls to the `CreateFeaturedResultsSet` API with the same client token will create only one featured results set.

`--status` (string)

The current status of the set of featured results. When the value is `ACTIVE` , featured results are ready for use. You can still configure your settings before setting the status to `ACTIVE` . You can set the status to `ACTIVE` or `INACTIVE` using the [UpdateFeaturedResultsSet](https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateFeaturedResultsSet.html) API. The queries you specify for featured results must be unique per featured results set for each index, whether the status is `ACTIVE` or `INACTIVE` .

Possible values:

- `ACTIVE`
- `INACTIVE`

`--query-texts` (list)

A list of queries for featuring results. For more information on the list of queries, see [FeaturedResultsSet](https://docs.aws.amazon.com/kendra/latest/dg/API_FeaturedResultsSet.html) .

(string)

Syntax:

```
"string" "string" ...
```

`--featured-documents` (list)

A list of document IDs for the documents you want to feature at the top of the search results page. For more information on the list of documents, see [FeaturedResultsSet](https://docs.aws.amazon.com/kendra/latest/dg/API_FeaturedResultsSet.html) .

(structure)

A featured document. This document is displayed at the top of the search results page, placed above all other results for certain queries. If thereâs an exact match of a query, then the document is featured in the search results.

Id -> (string)

The identifier of the document to feature in the search results. You can use the [Query](https://docs.aws.amazon.com/kendra/latest/dg/API_Query.html) API to search for specific documents with their document IDs included in the result items, or you can use the console.

Shorthand Syntax:

```
Id=string ...
```

JSON Syntax:

```
[
  {
    "Id": "string"
  }
  ...
]
```

`--tags` (list)

A list of key-value pairs that identify or categorize the featured results set. You can also use tags to help control access to the featured results set. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols:_ . : / = + - @.

(structure)

A key-value pair that identifies or categorizes an index, FAQ, data source, or other resource. TA tag key and value can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

Key -> (string)

The key for the tag. Keys are not case sensitive and must be unique for the index, FAQ, data source, or other resource.

Value -> (string)

The value associated with the tag. The value may be an empty string but it canât be null.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
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

FeaturedResultsSet -> (structure)

Information on the set of featured results. This includes the identifier of the featured results set, whether the featured results set is active or inactive, when the featured results set was created, and more.

FeaturedResultsSetId -> (string)

The identifier of the set of featured results.

FeaturedResultsSetName -> (string)

The name for the set of featured results.

Description -> (string)

The description for the set of featured results.

Status -> (string)

The current status of the set of featured results. When the value is `ACTIVE` , featured results are ready for use. You can still configure your settings before setting the status to `ACTIVE` . You can set the status to `ACTIVE` or `INACTIVE` using the [UpdateFeaturedResultsSet](https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateFeaturedResultsSet.html) API. The queries you specify for featured results must be unique per featured results set for each index, whether the status is `ACTIVE` or `INACTIVE` .

QueryTexts -> (list)

The list of queries for featuring results.

Specific queries are mapped to specific documents for featuring in the results. If a query contains an exact match, then one or more specific documents are featured in the results. The exact match applies to the full query. For example, if you only specify âKendraâ, queries such as âHow does kendra semantically rank results?â will not render the featured results. Featured results are designed for specific queries, rather than queries that are too broad in scope.

(string)

FeaturedDocuments -> (list)

The list of document IDs for the documents you want to feature at the top of the search results page. You can use the [Query](https://docs.aws.amazon.com/kendra/latest/dg/API_Query.html) API to search for specific documents with their document IDs included in the result items, or you can use the console.

You can add up to four featured documents. You can request to increase this limit by contacting [Support](http://aws.amazon.com/contact-us/) .

Specific queries are mapped to specific documents for featuring in the results. If a query contains an exact match, then one or more specific documents are featured in the results. The exact match applies to the full query. For example, if you only specify âKendraâ, queries such as âHow does kendra semantically rank results?â will not render the featured results. Featured results are designed for specific queries, rather than queries that are too broad in scope.

(structure)

A featured document. This document is displayed at the top of the search results page, placed above all other results for certain queries. If thereâs an exact match of a query, then the document is featured in the search results.

Id -> (string)

The identifier of the document to feature in the search results. You can use the [Query](https://docs.aws.amazon.com/kendra/latest/dg/API_Query.html) API to search for specific documents with their document IDs included in the result items, or you can use the console.

LastUpdatedTimestamp -> (long)

The Unix timestamp when the set of featured results was last updated.

CreationTimestamp -> (long)

The Unix timestamp when the set of featured results was created.