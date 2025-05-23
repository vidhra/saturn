# batch-get-document-statusÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/batch-get-document-status.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/batch-get-document-status.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# batch-get-document-status

## Description

Returns the indexing status for one or more documents submitted with the [BatchPutDocument](https://docs.aws.amazon.com/kendra/latest/dg/API_BatchPutDocument.html) API.

When you use the `BatchPutDocument` API, documents are indexed asynchronously. You can use the `BatchGetDocumentStatus` API to get the current status of a list of documents so that you can determine if they have been successfully indexed.

You can also use the `BatchGetDocumentStatus` API to check the status of the [BatchDeleteDocument](https://docs.aws.amazon.com/kendra/latest/dg/API_BatchDeleteDocument.html) API. When a document is deleted from the index, Amazon Kendra returns `NOT_FOUND` as the status.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/BatchGetDocumentStatus)

## Synopsis

```
batch-get-document-status
--index-id <value>
--document-info-list <value>
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

The identifier of the index to add documents to. The index ID is returned by the [CreateIndex](https://docs.aws.amazon.com/kendra/latest/dg/API_CreateIndex.html) API.

`--document-info-list` (list)

A list of `DocumentInfo` objects that identify the documents for which to get the status. You identify the documents by their document ID and optional attributes.

(structure)

Identifies a document for which to retrieve status information

DocumentId -> (string)

The identifier of the document.

Attributes -> (list)

Attributes that identify a specific version of a document to check.

The only valid attributes are:

- version
- datasourceId
- jobExecutionId

The attributes follow these rules:

- `dataSourceId` and `jobExecutionId` must be used together.
- `version` is ignored if `dataSourceId` and `jobExecutionId` are not provided.
- If `dataSourceId` and `jobExecutionId` are provided, but `version` is not, the version defaults to â0â.

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

JSON Syntax:

```
[
  {
    "DocumentId": "string",
    "Attributes": [
      {
        "Key": "string",
        "Value": {
          "StringValue": "string",
          "StringListValue": ["string", ...],
          "LongValue": long,
          "DateValue": timestamp
        }
      }
      ...
    ]
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

Errors -> (list)

A list of documents that Amazon Kendra couldnât get the status for. The list includes the ID of the document and the reason that the status couldnât be found.

(structure)

Provides a response when the status of a document could not be retrieved.

DocumentId -> (string)

The identifier of the document whose status could not be retrieved.

DataSourceId -> (string)

The identifier of the data source connector that the failed document belongs to.

ErrorCode -> (string)

Indicates the source of the error.

ErrorMessage -> (string)

States that the API could not get the status of a document. This could be because the request is not valid or there is a system error.

DocumentStatusList -> (list)

The status of documents. The status indicates if the document is waiting to be indexed, is in the process of indexing, has completed indexing, or failed indexing. If a document failed indexing, the status provides the reason why.

(structure)

Provides information about the status of documents submitted for indexing.

DocumentId -> (string)

The identifier of the document.

DocumentStatus -> (string)

The current status of a document.

If the document was submitted for deletion, the status is `NOT_FOUND` after the document is deleted.

FailureCode -> (string)

Indicates the source of the error.

FailureReason -> (string)

Provides detailed information about why the document couldnât be indexed. Use this information to correct the error before you resubmit the document for indexing.