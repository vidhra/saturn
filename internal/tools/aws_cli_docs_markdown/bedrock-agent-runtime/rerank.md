# rerankÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent-runtime/rerank.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent-runtime/rerank.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock-agent-runtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent-runtime/index.html#cli-aws-bedrock-agent-runtime) ]

# rerank

## Description

Reranks the relevance of sources based on queries. For more information, see [Improve the relevance of query responses with a reranker model](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agent-runtime-2023-07-26/Rerank)

`rerank` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

`rerank` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `results`

## Synopsis

```
rerank
--queries <value>
--reranking-configuration <value>
--sources <value>
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

`--queries` (list)

An array of objects, each of which contains information about a query to submit to the reranker model.

(structure)

Contains information about a query to submit to the reranker model.

textQuery -> (structure)

Contains information about a text query.

text -> (string)

The text of the document.

type -> (string)

The type of the query.

Shorthand Syntax:

```
textQuery={text=string},type=string ...
```

JSON Syntax:

```
[
  {
    "textQuery": {
      "text": "string"
    },
    "type": "TEXT"
  }
  ...
]
```

`--reranking-configuration` (structure)

Contains configurations for reranking.

bedrockRerankingConfiguration -> (structure)

Contains configurations for an Amazon Bedrock reranker.

modelConfiguration -> (structure)

Contains configurations for a reranker model.

additionalModelRequestFields -> (map)

A JSON object whose keys are request fields for the model and whose values are values for those fields.

key -> (string)

value -> (document)

modelArn -> (string)

The ARN of the reranker model.

numberOfResults -> (integer)

The number of results to return after reranking.

type -> (string)

The type of reranker that the configurations apply to.

Shorthand Syntax:

```
bedrockRerankingConfiguration={modelConfiguration={modelArn=string},numberOfResults=integer},type=string
```

JSON Syntax:

```
{
  "bedrockRerankingConfiguration": {
    "modelConfiguration": {
      "additionalModelRequestFields": {"string": {...}
        ...},
      "modelArn": "string"
    },
    "numberOfResults": integer
  },
  "type": "BEDROCK_RERANKING_MODEL"
}
```

`--sources` (list)

An array of objects, each of which contains information about the sources to rerank.

(structure)

Contains information about a source for reranking.

inlineDocumentSource -> (structure)

Contains an inline definition of a source for reranking.

jsonDocument -> (document)

Contains a JSON document to rerank.

textDocument -> (structure)

Contains information about a text document to rerank.

text -> (string)

The text of the document.

type -> (string)

The type of document to rerank.

type -> (string)

The type of the source.

Shorthand Syntax:

```
inlineDocumentSource={textDocument={text=string},type=string},type=string ...
```

JSON Syntax:

```
[
  {
    "inlineDocumentSource": {
      "jsonDocument": {...},
      "textDocument": {
        "text": "string"
      },
      "type": "TEXT"|"JSON"
    },
    "type": "INLINE"
  }
  ...
]
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

nextToken -> (string)

If the total number of results is greater than can fit in the response, use this token in the `nextToken` field when making another request to return the next batch of results.

results -> (list)

An array of objects, each of which contains information about the results of reranking.

(structure)

Contains information about a document that was reranked.

document -> (structure)

Contains information about the document.

jsonDocument -> (document)

Contains a JSON document to rerank.

textDocument -> (structure)

Contains information about a text document to rerank.

text -> (string)

The text of the document.

type -> (string)

The type of document to rerank.

index -> (integer)

The ranking of the document. The lower a number, the higher the document is ranked.

relevanceScore -> (float)

The relevance score of the document.