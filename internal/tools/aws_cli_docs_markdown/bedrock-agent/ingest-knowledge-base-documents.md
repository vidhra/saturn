# ingest-knowledge-base-documentsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/ingest-knowledge-base-documents.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/ingest-knowledge-base-documents.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock-agent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/index.html#cli-aws-bedrock-agent) ]

# ingest-knowledge-base-documents

## Description

Ingests documents directly into the knowledge base that is connected to the data source. The `dataSourceType` specified in the content for each document must match the type of the data source that you specify in the header. For more information, see [Ingest changes directly into a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html) in the Amazon Bedrock User Guide.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agent-2023-06-05/IngestKnowledgeBaseDocuments)

## Synopsis

```
ingest-knowledge-base-documents
[--client-token <value>]
--data-source-id <value>
--documents <value>
--knowledge-base-id <value>
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

`--client-token` (string)

A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .

`--data-source-id` (string)

The unique identifier of the data source connected to the knowledge base that youâre adding documents to.

`--documents` (list)

A list of objects, each of which contains information about the documents to add.

(structure)

Contains information about a document to ingest into a knowledge base and metadata to associate with it.

content -> (structure)

Contains the content of the document.

custom -> (structure)

Contains information about the content to ingest into a knowledge base connected to a custom data source.

customDocumentIdentifier -> (structure)

A unique identifier for the document.

id -> (string)

The identifier of the document to ingest into a custom data source.

inlineContent -> (structure)

Contains information about content defined inline to ingest into a knowledge base.

byteContent -> (structure)

Contains information about content defined inline in bytes.

data -> (blob)

The base64-encoded string of the content.

mimeType -> (string)

The MIME type of the content. For a list of MIME types, see [Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml) . The following MIME types are supported:

- text/plain
- text/html
- text/csv
- text/vtt
- message/rfc822
- application/xhtml+xml
- application/pdf
- application/msword
- application/vnd.ms-word.document.macroenabled.12
- application/vnd.ms-word.template.macroenabled.12
- application/vnd.ms-excel
- application/vnd.ms-excel.addin.macroenabled.12
- application/vnd.ms-excel.sheet.macroenabled.12
- application/vnd.ms-excel.template.macroenabled.12
- application/vnd.ms-excel.sheet.binary.macroenabled.12
- application/vnd.ms-spreadsheetml
- application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
- application/vnd.openxmlformats-officedocument.spreadsheetml.template
- application/vnd.openxmlformats-officedocument.wordprocessingml.document
- application/vnd.openxmlformats-officedocument.wordprocessingml.template

textContent -> (structure)

Contains information about content defined inline in text.

data -> (string)

The text of the content.

type -> (string)

The type of inline content to define.

s3Location -> (structure)

Contains information about the Amazon S3 location of the file from which to ingest data.

bucketOwnerAccountId -> (string)

The identifier of the Amazon Web Services account that owns the S3 bucket containing the content to ingest.

uri -> (string)

The S3 URI of the file containing the content to ingest.

sourceType -> (string)

The source of the data to ingest.

dataSourceType -> (string)

The type of data source that is connected to the knowledge base to which to ingest this document.

s3 -> (structure)

Contains information about the content to ingest into a knowledge base connected to an Amazon S3 data source

s3Location -> (structure)

The S3 location of the file containing the content to ingest.

uri -> (string)

The locationâs URI. For example, `s3://my-bucket/chunk-processor/` .

metadata -> (structure)

Contains the metadata to associate with the document.

inlineAttributes -> (list)

An array of objects, each of which defines a metadata attribute to associate with the content to ingest. You define the attributes inline.

(structure)

Contains information about a metadata attribute.

key -> (string)

The key of the metadata attribute.

value -> (structure)

Contains the value of the metadata attribute.

booleanValue -> (boolean)

The value of the Boolean metadata attribute.

numberValue -> (double)

The value of the numeric metadata attribute.

stringListValue -> (list)

An array of strings that define the value of the metadata attribute.

(string)

stringValue -> (string)

The value of the string metadata attribute.

type -> (string)

The type of the metadata attribute.

s3Location -> (structure)

The Amazon S3 location of the file containing metadata to associate with the content to ingest.

bucketOwnerAccountId -> (string)

The identifier of the Amazon Web Services account that owns the S3 bucket containing the content to ingest.

uri -> (string)

The S3 URI of the file containing the content to ingest.

type -> (string)

The type of the source source from which to add metadata.

JSON Syntax:

```
[
  {
    "content": {
      "custom": {
        "customDocumentIdentifier": {
          "id": "string"
        },
        "inlineContent": {
          "byteContent": {
            "data": blob,
            "mimeType": "string"
          },
          "textContent": {
            "data": "string"
          },
          "type": "BYTE"|"TEXT"
        },
        "s3Location": {
          "bucketOwnerAccountId": "string",
          "uri": "string"
        },
        "sourceType": "IN_LINE"|"S3_LOCATION"
      },
      "dataSourceType": "CUSTOM"|"S3",
      "s3": {
        "s3Location": {
          "uri": "string"
        }
      }
    },
    "metadata": {
      "inlineAttributes": [
        {
          "key": "string",
          "value": {
            "booleanValue": true|false,
            "numberValue": double,
            "stringListValue": ["string", ...],
            "stringValue": "string",
            "type": "BOOLEAN"|"NUMBER"|"STRING"|"STRING_LIST"
          }
        }
        ...
      ],
      "s3Location": {
        "bucketOwnerAccountId": "string",
        "uri": "string"
      },
      "type": "IN_LINE_ATTRIBUTE"|"S3_LOCATION"
    }
  }
  ...
]
```

`--knowledge-base-id` (string)

The unique identifier of the knowledge base to ingest the documents into.

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

documentDetails -> (list)

A list of objects, each of which contains information about the documents that were ingested.

(structure)

Contains the details for a document that was ingested or deleted.

dataSourceId -> (string)

The identifier of the data source connected to the knowledge base that the document was ingested into or deleted from.

identifier -> (structure)

Contains information that identifies the document.

custom -> (structure)

Contains information that identifies the document in a custom data source.

id -> (string)

The identifier of the document to ingest into a custom data source.

dataSourceType -> (string)

The type of data source connected to the knowledge base that contains the document.

s3 -> (structure)

Contains information that identifies the document in an S3 data source.

uri -> (string)

The locationâs URI. For example, `s3://my-bucket/chunk-processor/` .

knowledgeBaseId -> (string)

The identifier of the knowledge base that the document was ingested into or deleted from.

status -> (string)

The ingestion status of the document. The following statuses are possible:

- STARTED â You submitted the ingestion job containing the document.
- PENDING â The document is waiting to be ingested.
- IN_PROGRESS â The document is being ingested.
- INDEXED â The document was successfully indexed.
- PARTIALLY_INDEXED â The document was partially indexed.
- METADATA_PARTIALLY_INDEXED â You submitted metadata for an existing document and it was partially indexed.
- METADATA_UPDATE_FAILED â You submitted a metadata update for an existing document but it failed.
- FAILED â The document failed to be ingested.
- NOT_FOUND â The document wasnât found.
- IGNORED â The document was ignored during ingestion.
- DELETING â You submitted the delete job containing the document.
- DELETE_IN_PROGRESS â The document is being deleted.

statusReason -> (string)

The reason for the status. Appears alongside the status `IGNORED` .

updatedAt -> (timestamp)

The date and time at which the document was last updated.