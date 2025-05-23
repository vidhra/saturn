# rescoreÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra-ranking/rescore.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra-ranking/rescore.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra-ranking](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra-ranking/index.html#cli-aws-kendra-ranking) ]

# rescore

## Description

Rescores or re-ranks search results from a search service such as OpenSearch (self managed). You use the semantic search capabilities of Amazon Kendra Intelligent Ranking to improve the search serviceâs results.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-ranking-2022-10-19/Rescore)

## Synopsis

```
rescore
--rescore-execution-plan-id <value>
--search-query <value>
--documents <value>
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

`--rescore-execution-plan-id` (string)

The identifier of the rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the `Rescore` API.

`--search-query` (string)

The input query from the search service.

`--documents` (list)

The list of documents for Amazon Kendra Intelligent Ranking to rescore or rank on.

(structure)

Information about a document from a search service such as OpenSearch (self managed). Amazon Kendra Intelligent Ranking uses this information to rank and score on.

Id -> (string)

The identifier of the document from the search service.

GroupId -> (string)

The optional group identifier of the document from the search service. Documents with the same group identifier are grouped together and processed as one document within the service.

Title -> (string)

The title of the search serviceâs document.

Body -> (string)

The body text of the search serviceâs document.

TokenizedTitle -> (list)

The title of the search serviceâs document represented as a list of tokens or words. You must choose to provide `Title` or `TokenizedTitle` . You cannot provide both.

(string)

TokenizedBody -> (list)

The body text of the search serviceâs document represented as a list of tokens or words. You must choose to provide `Body` or `TokenizedBody` . You cannot provide both.

(string)

OriginalScore -> (float)

The original document score or rank from the search service. Amazon Kendra Intelligent Ranking gives the document a new score or rank based on its intelligent search algorithms.

Shorthand Syntax:

```
Id=string,GroupId=string,Title=string,Body=string,TokenizedTitle=string,string,TokenizedBody=string,string,OriginalScore=float ...
```

JSON Syntax:

```
[
  {
    "Id": "string",
    "GroupId": "string",
    "Title": "string",
    "Body": "string",
    "TokenizedTitle": ["string", ...],
    "TokenizedBody": ["string", ...],
    "OriginalScore": float
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

RescoreId -> (string)

The identifier associated with the scores that Amazon Kendra Intelligent Ranking gives to the results. Amazon Kendra Intelligent Ranking rescores or re-ranks the results for the search service.

ResultItems -> (list)

A list of result items for documents with new relevancy scores. The results are in descending order.

(structure)

A result item for a document with a new relevancy score.

DocumentId -> (string)

The identifier of the document from the search service.

Score -> (float)

The relevancy score or rank that Amazon Kendra Intelligent Ranking gives to the result.