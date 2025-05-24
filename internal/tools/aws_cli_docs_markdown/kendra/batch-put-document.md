# batch-put-documentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/batch-put-document.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/batch-put-document.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# batch-put-document

## Description

Adds one or more documents to an index.

The `BatchPutDocument` API enables you to ingest inline documents or a set of documents stored in an Amazon S3 bucket. Use this API to ingest your text and unstructured text into an index, add custom attributes to the documents, and to attach an access control list to the documents added to the index.

The documents are indexed asynchronously. You can see the progress of the batch using Amazon Web Services CloudWatch. Any error messages related to processing the batch are sent to your Amazon Web Services CloudWatch log. You can also use the `BatchGetDocumentStatus` API to monitor the progress of indexing your documents.

For an example of ingesting inline documents using Python and Java SDKs, see [Adding files directly to an index](https://docs.aws.amazon.com/kendra/latest/dg/in-adding-binary-doc.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/BatchPutDocument)

## Synopsis

```
batch-put-document
--index-id <value>
[--role-arn <value>]
--documents <value>
[--custom-document-enrichment-configuration <value>]
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

The identifier of the index to add the documents to. You need to create the index first using the `CreateIndex` API.

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role with permission to access your S3 bucket. For more information, see [IAM access roles for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html) .

`--documents` (list)

One or more documents to add to the index.

Documents have the following file size limits.

- 50 MB total size for any file
- 5 MB extracted text for any file

For more information, see [Quotas](https://docs.aws.amazon.com/kendra/latest/dg/quotas.html) .

(structure)

A document in an index.

Id -> (string)

A identifier of the document in the index.

Note, each document ID must be unique per index. You cannot create a data source to index your documents with their unique IDs and then use the `BatchPutDocument` API to index the same documents, or vice versa. You can delete a data source and then use the `BatchPutDocument` API to index the same documents, or vice versa.

Title -> (string)

The title of the document.

Blob -> (blob)

The contents of the document.

Documents passed to the `Blob` parameter must be base64 encoded. Your code might not need to encode the document file bytes if youâre using an Amazon Web Services SDK to call Amazon Kendra APIs. If you are calling the Amazon Kendra endpoint directly using REST, you must base64 encode the contents before sending.

S3Path -> (structure)

Information required to find a specific file in an Amazon S3 bucket.

Bucket -> (string)

The name of the S3 bucket that contains the file.

Key -> (string)

The name of the file.

Attributes -> (list)

Custom attributes to apply to the document. Use the custom attributes to provide additional information for searching, to provide facets for refining searches, and to provide additional information in the query response.

For example, âDataSourceIdâ and âDataSourceSyncJobIdâ are custom attributes that provide information on the synchronization of documents running on a data source. Note, âDataSourceSyncJobIdâ could be an optional custom attribute as Amazon Kendra will use the ID of a running sync job.

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

AccessControlList -> (list)

Information on principals (users and/or groups) and which documents they should have access to. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.

(structure)

Provides user and group information for [user context filtering](https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html) .

Name -> (string)

The name of the user or group.

Type -> (string)

The type of principal.

Access -> (string)

Whether to allow or deny document access to the principal.

DataSourceId -> (string)

The identifier of the data source the principal should access documents from.

HierarchicalAccessControlList -> (list)

The list of [principal](https://docs.aws.amazon.com/kendra/latest/dg/API_Principal.html) lists that define the hierarchy for which documents users should have access to.

(structure)

Information to define the hierarchy for which documents users should have access to.

PrincipalList -> (list)

A list of [principal](https://docs.aws.amazon.com/kendra/latest/dg/API_Principal.html) lists that define the hierarchy for which documents users should have access to. Each hierarchical list specifies which user or group has allow or deny access for each document.

(structure)

Provides user and group information for [user context filtering](https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html) .

Name -> (string)

The name of the user or group.

Type -> (string)

The type of principal.

Access -> (string)

Whether to allow or deny document access to the principal.

DataSourceId -> (string)

The identifier of the data source the principal should access documents from.

ContentType -> (string)

The file type of the document in the `Blob` field.

If you want to index snippets or subsets of HTML documents instead of the entirety of the HTML documents, you must add the `HTML` start and closing tags (`<HTML>content</HTML>` ) around the content.

AccessControlConfigurationId -> (string)

The identifier of the access control configuration that you want to apply to the document.

JSON Syntax:

```
[
  {
    "Id": "string",
    "Title": "string",
    "Blob": blob,
    "S3Path": {
      "Bucket": "string",
      "Key": "string"
    },
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
    ],
    "AccessControlList": [
      {
        "Name": "string",
        "Type": "USER"|"GROUP",
        "Access": "ALLOW"|"DENY",
        "DataSourceId": "string"
      }
      ...
    ],
    "HierarchicalAccessControlList": [
      {
        "PrincipalList": [
          {
            "Name": "string",
            "Type": "USER"|"GROUP",
            "Access": "ALLOW"|"DENY",
            "DataSourceId": "string"
          }
          ...
        ]
      }
      ...
    ],
    "ContentType": "PDF"|"HTML"|"MS_WORD"|"PLAIN_TEXT"|"PPT"|"RTF"|"XML"|"XSLT"|"MS_EXCEL"|"CSV"|"JSON"|"MD",
    "AccessControlConfigurationId": "string"
  }
  ...
]
```

`--custom-document-enrichment-configuration` (structure)

Configuration information for altering your document metadata and content during the document ingestion process when you use the `BatchPutDocument` API.

For more information on how to create, modify and delete document metadata, or make other content alterations when you ingest documents into Amazon Kendra, see [Customizing document metadata during the ingestion process](https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html) .

InlineConfigurations -> (list)

Configuration information to alter document attributes or metadata fields and content when ingesting documents into Amazon Kendra.

(structure)

Provides the configuration information for applying basic logic to alter document metadata and content when ingesting documents into Amazon Kendra. To apply advanced logic, to go beyond what you can do with basic logic, see [HookConfiguration](https://docs.aws.amazon.com/kendra/latest/dg/API_HookConfiguration.html) .

For more information, see [Customizing document metadata during the ingestion process](https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html) .

Condition -> (structure)

Configuration of the condition used for the target document attribute or metadata field when ingesting documents into Amazon Kendra.

ConditionDocumentAttributeKey -> (string)

The identifier of the document attribute used for the condition.

For example, âSource_URIâ could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.

Amazon Kendra currently does not support `_document_body` as an attribute key used for the condition.

Operator -> (string)

The condition operator.

For example, you can use âContainsâ to partially match a string.

ConditionOnValue -> (structure)

The value used by the operator.

For example, you can specify the value âfinancialâ for strings in the âSource_URIâ field that partially match or contain this value.

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

Target -> (structure)

Configuration of the target document attribute or metadata field when ingesting documents into Amazon Kendra. You can also include a value.

TargetDocumentAttributeKey -> (string)

The identifier of the target document attribute or metadata field.

For example, âDepartmentâ could be an identifier for the target attribute or metadata field that includes the department names associated with the documents.

TargetDocumentAttributeValueDeletion -> (boolean)

`TRUE` to delete the existing target value for your specified target attribute key. You cannot create a target value and set this to `TRUE` . To create a target value (`TargetDocumentAttributeValue` ), set this to `FALSE` .

TargetDocumentAttributeValue -> (structure)

The target value you want to create for the target attribute.

For example, âFinanceâ could be the target value for the target attribute key âDepartmentâ.

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

DocumentContentDeletion -> (boolean)

`TRUE` to delete content if the condition used for the target attribute is met.

PreExtractionHookConfiguration -> (structure)

Configuration information for invoking a Lambda function in Lambda on the original or raw documents before extracting their metadata and text. You can use a Lambda function to apply advanced logic for creating, modifying, or deleting document metadata and content. For more information, see [Advanced data manipulation](https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#advanced-data-manipulation) .

InvocationCondition -> (structure)

The condition used for when a Lambda function should be invoked.

For example, you can specify a condition that if there are empty date-time values, then Amazon Kendra should invoke a function that inserts the current date-time.

ConditionDocumentAttributeKey -> (string)

The identifier of the document attribute used for the condition.

For example, âSource_URIâ could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.

Amazon Kendra currently does not support `_document_body` as an attribute key used for the condition.

Operator -> (string)

The condition operator.

For example, you can use âContainsâ to partially match a string.

ConditionOnValue -> (structure)

The value used by the operator.

For example, you can specify the value âfinancialâ for strings in the âSource_URIâ field that partially match or contain this value.

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

LambdaArn -> (string)

The Amazon Resource Name (ARN) of an IAM role with permission to run a Lambda function during ingestion. For more information, see [an IAM roles for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html) .

S3Bucket -> (string)

Stores the original, raw documents or the structured, parsed documents before and after altering them. For more information, see [Data contracts for Lambda functions](https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#cde-data-contracts-lambda) .

PostExtractionHookConfiguration -> (structure)

Configuration information for invoking a Lambda function in Lambda on the structured documents with their metadata and text extracted. You can use a Lambda function to apply advanced logic for creating, modifying, or deleting document metadata and content. For more information, see [Advanced data manipulation](https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#advanced-data-manipulation) .

InvocationCondition -> (structure)

The condition used for when a Lambda function should be invoked.

For example, you can specify a condition that if there are empty date-time values, then Amazon Kendra should invoke a function that inserts the current date-time.

ConditionDocumentAttributeKey -> (string)

The identifier of the document attribute used for the condition.

For example, âSource_URIâ could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.

Amazon Kendra currently does not support `_document_body` as an attribute key used for the condition.

Operator -> (string)

The condition operator.

For example, you can use âContainsâ to partially match a string.

ConditionOnValue -> (structure)

The value used by the operator.

For example, you can specify the value âfinancialâ for strings in the âSource_URIâ field that partially match or contain this value.

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

LambdaArn -> (string)

The Amazon Resource Name (ARN) of an IAM role with permission to run a Lambda function during ingestion. For more information, see [an IAM roles for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html) .

S3Bucket -> (string)

Stores the original, raw documents or the structured, parsed documents before and after altering them. For more information, see [Data contracts for Lambda functions](https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#cde-data-contracts-lambda) .

RoleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role with permission to run `PreExtractionHookConfiguration` and `PostExtractionHookConfiguration` for altering document metadata and content during the document ingestion process. For more information, see [an IAM roles for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html) .

JSON Syntax:

```
{
  "InlineConfigurations": [
    {
      "Condition": {
        "ConditionDocumentAttributeKey": "string",
        "Operator": "GreaterThan"|"GreaterThanOrEquals"|"LessThan"|"LessThanOrEquals"|"Equals"|"NotEquals"|"Contains"|"NotContains"|"Exists"|"NotExists"|"BeginsWith",
        "ConditionOnValue": {
          "StringValue": "string",
          "StringListValue": ["string", ...],
          "LongValue": long,
          "DateValue": timestamp
        }
      },
      "Target": {
        "TargetDocumentAttributeKey": "string",
        "TargetDocumentAttributeValueDeletion": true|false,
        "TargetDocumentAttributeValue": {
          "StringValue": "string",
          "StringListValue": ["string", ...],
          "LongValue": long,
          "DateValue": timestamp
        }
      },
      "DocumentContentDeletion": true|false
    }
    ...
  ],
  "PreExtractionHookConfiguration": {
    "InvocationCondition": {
      "ConditionDocumentAttributeKey": "string",
      "Operator": "GreaterThan"|"GreaterThanOrEquals"|"LessThan"|"LessThanOrEquals"|"Equals"|"NotEquals"|"Contains"|"NotContains"|"Exists"|"NotExists"|"BeginsWith",
      "ConditionOnValue": {
        "StringValue": "string",
        "StringListValue": ["string", ...],
        "LongValue": long,
        "DateValue": timestamp
      }
    },
    "LambdaArn": "string",
    "S3Bucket": "string"
  },
  "PostExtractionHookConfiguration": {
    "InvocationCondition": {
      "ConditionDocumentAttributeKey": "string",
      "Operator": "GreaterThan"|"GreaterThanOrEquals"|"LessThan"|"LessThanOrEquals"|"Equals"|"NotEquals"|"Contains"|"NotContains"|"Exists"|"NotExists"|"BeginsWith",
      "ConditionOnValue": {
        "StringValue": "string",
        "StringListValue": ["string", ...],
        "LongValue": long,
        "DateValue": timestamp
      }
    },
    "LambdaArn": "string",
    "S3Bucket": "string"
  },
  "RoleArn": "string"
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

FailedDocuments -> (list)

A list of documents that were not added to the index because the document failed a validation check. Each document contains an error message that indicates why the document couldnât be added to the index.

If there was an error adding a document to an index the error is reported in your Amazon Web Services CloudWatch log. For more information, see [Monitoring Amazon Kendra with Amazon CloudWatch logs](https://docs.aws.amazon.com/kendra/latest/dg/cloudwatch-logs.html) .

(structure)

Provides information about a document that could not be indexed.

Id -> (string)

The identifier of the document.

DataSourceId -> (string)

The identifier of the data source connector that the failed document belongs to.

ErrorCode -> (string)

The type of error that caused the document to fail to be indexed.

ErrorMessage -> (string)

A description of the reason why the document could not be indexed.