# batch-put-documentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/batch-put-document.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/batch-put-document.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qbusiness](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/index.html#cli-aws-qbusiness) ]

# batch-put-document

## Description

Adds one or more documents to an Amazon Q Business index.

You use this API to:

- ingest your structured and unstructured documents and documents stored in an Amazon S3 bucket into an Amazon Q Business index.
- add custom attributes to documents in an Amazon Q Business index.
- attach an access control list to the documents added to an Amazon Q Business index.

You can see the progress of the deletion, and any error messages related to the process, by using CloudWatch.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qbusiness-2023-11-27/BatchPutDocument)

## Synopsis

```
batch-put-document
--application-id <value>
--index-id <value>
--documents <value>
[--role-arn <value>]
[--data-source-sync-id <value>]
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

`--application-id` (string)

The identifier of the Amazon Q Business application.

`--index-id` (string)

The identifier of the Amazon Q Business index to add the documents to.

`--documents` (list)

One or more documents to add to the index.

(structure)

A document in an Amazon Q Business application.

id -> (string)

The identifier of the document.

attributes -> (list)

Custom attributes to apply to the document for refining Amazon Q Business web experience responses.

(structure)

A document attribute or metadata field.

name -> (string)

The identifier for the attribute.

value -> (tagged union structure)

The value of the attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

content -> (tagged union structure)

The contents of the document.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `blob`, `s3`.

blob -> (blob)

The contents of the document. Documents passed to the `blob` parameter must be base64 encoded. Your code might not need to encode the document file bytes if youâre using an Amazon Web Services SDK to call Amazon Q Business APIs. If you are calling the Amazon Q Business endpoint directly using REST, you must base64 encode the contents before sending.

s3 -> (structure)

The path to the document in an Amazon S3 bucket.

bucket -> (string)

The name of the S3 bucket that contains the file.

key -> (string)

The name of the file.

contentType -> (string)

The file type of the document in the Blob field.

If you want to index snippets or subsets of HTML documents instead of the entirety of the HTML documents, you add the `HTML` start and closing tags (`<HTML>content</HTML>` ) around the content.

title -> (string)

The title of the document.

accessConfiguration -> (structure)

Configuration information for access permission to a document.

accessControls -> (list)

A list of `AccessControlList` objects.

(structure)

A list of principals. Each principal can be either a `USER` or a `GROUP` and can be designated document access permissions of either `ALLOW` or `DENY` .

principals -> (list)

Contains a list of principals, where a principal can be either a `USER` or a `GROUP` . Each principal can be have the following type of document access: `ALLOW` or `DENY` .

(tagged union structure)

Provides user and group information used for filtering documents to use for generating Amazon Q Business conversation responses.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `user`, `group`.

user -> (structure)

The user associated with the principal.

id -> (string)

The identifier of the user.

access -> (string)

Provides information about whether to allow or deny access to the principal.

membershipType -> (string)

The type of group.

group -> (structure)

The group associated with the principal.

name -> (string)

The name of the group.

access -> (string)

Provides information about whether to allow or deny access to the principal.

membershipType -> (string)

The type of group.

memberRelation -> (string)

Describes the member relation within a principal list.

memberRelation -> (string)

Describes the member relation within the `AccessControlList` object.

documentEnrichmentConfiguration -> (structure)

The configuration information for altering document metadata and content during the document ingestion process.

inlineConfigurations -> (list)

Configuration information to alter document attributes or metadata fields and content when ingesting documents into Amazon Q Business.

(structure)

Provides the configuration information for applying basic logic to alter document metadata and content when ingesting documents into Amazon Q Business.

To apply advanced logic, to go beyond what you can do with basic logic, see ` `HookConfiguration` [https://docs.aws.amazon.com/amazonq/latest/api-reference/API_HookConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_HookConfiguration).html`__ .

For more information, see [Custom document enrichment](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html) .

condition -> (structure)

The condition used for the target document attribute or metadata field when ingesting documents into Amazon Q Business. You use this with ` `DocumentAttributeTarget` [https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeTarget](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeTarget).html`__ to apply the condition.

For example, you can create the âDepartmentâ target field and have it prefill department names associated with the documents based on information in the âSource_URIâ field. Set the condition that if the âSource_URIâ field contains âfinancialâ in its URI value, then prefill the target field âDepartmentâ with the target value âFinanceâ for the document.

Amazon Q Business canât create a target field if it has not already been created as an index field. After you create your index field, you can create a document metadata field using `DocumentAttributeTarget` . Amazon Q Business then will map your newly created metadata field to your index field.

key -> (string)

The identifier of the document attribute used for the condition.

For example, âSource_URIâ could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.

Amazon Q Business currently doesnât support `_document_body` as an attribute key used for the condition.

operator -> (string)

The identifier of the document attribute used for the condition.

For example, âSource_URIâ could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.

Amazon Q Business currently does not support `_document_body` as an attribute key used for the condition.

value -> (tagged union structure)

The value of a document attribute. You can only provide one value for a document attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

target -> (structure)

The target document attribute or metadata field you want to alter when ingesting documents into Amazon Q Business.

For example, you can delete all customer identification numbers associated with the documents, stored in the document metadata field called âCustomer_IDâ by setting the target key as âCustomer_IDâ and the deletion flag to `TRUE` . This removes all customer ID values in the field âCustomer_IDâ. This would scrub personally identifiable information from each documentâs metadata.

Amazon Q Business canât create a target field if it has not already been created as an index field. After you create your index field, you can create a document metadata field using ` `DocumentAttributeTarget` [https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeTarget](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeTarget).html`__ . Amazon Q Business will then map your newly created document attribute to your index field.

You can also use this with ` `DocumentAttributeCondition` [https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeCondition](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeCondition).html`__ .

key -> (string)

The identifier of the target document attribute or metadata field. For example, âDepartmentâ could be an identifier for the target attribute or metadata field that includes the department names associated with the documents.

value -> (tagged union structure)

The value of a document attribute. You can only provide one value for a document attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

attributeValueOperator -> (string)

`TRUE` to delete the existing target value for your specified target attribute key. You cannot create a target value and set this to `TRUE` .

documentContentOperator -> (string)

`TRUE` to delete content if the condition used for the target attribute is met.

preExtractionHookConfiguration -> (structure)

Provides the configuration information for invoking a Lambda function in Lambda to alter document metadata and content when ingesting documents into Amazon Q Business.

You can configure your Lambda function using the `PreExtractionHookConfiguration` parameter if you want to apply advanced alterations on the original or raw documents.

If you want to apply advanced alterations on the Amazon Q Business structured documents, you must configure your Lambda function using `PostExtractionHookConfiguration` .

You can only invoke one Lambda function. However, this function can invoke other functions it requires.

For more information, see [Custom document enrichment](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html) .

invocationCondition -> (structure)

The condition used for when a Lambda function should be invoked.

For example, you can specify a condition that if there are empty date-time values, then Amazon Q Business should invoke a function that inserts the current date-time.

key -> (string)

The identifier of the document attribute used for the condition.

For example, âSource_URIâ could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.

Amazon Q Business currently doesnât support `_document_body` as an attribute key used for the condition.

operator -> (string)

The identifier of the document attribute used for the condition.

For example, âSource_URIâ could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.

Amazon Q Business currently does not support `_document_body` as an attribute key used for the condition.

value -> (tagged union structure)

The value of a document attribute. You can only provide one value for a document attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

lambdaArn -> (string)

The Amazon Resource Name (ARN) of the Lambda function sduring ingestion. For more information, see [Using Lambda functions for Amazon Q Business document enrichment](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cde-lambda-operations.html) .

s3BucketName -> (string)

Stores the original, raw documents or the structured, parsed documents before and after altering them. For more information, see [Data contracts for Lambda functions](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/cde-lambda-operations.html#cde-lambda-operations-data-contracts) .

roleArn -> (string)

The Amazon Resource Name (ARN) of a role with permission to run `PreExtractionHookConfiguration` and `PostExtractionHookConfiguration` for altering document metadata and content during the document ingestion process.

postExtractionHookConfiguration -> (structure)

Provides the configuration information for invoking a Lambda function in Lambda to alter document metadata and content when ingesting documents into Amazon Q Business.

You can configure your Lambda function using the `PreExtractionHookConfiguration` parameter if you want to apply advanced alterations on the original or raw documents.

If you want to apply advanced alterations on the Amazon Q Business structured documents, you must configure your Lambda function using `PostExtractionHookConfiguration` .

You can only invoke one Lambda function. However, this function can invoke other functions it requires.

For more information, see [Custom document enrichment](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html) .

invocationCondition -> (structure)

The condition used for when a Lambda function should be invoked.

For example, you can specify a condition that if there are empty date-time values, then Amazon Q Business should invoke a function that inserts the current date-time.

key -> (string)

The identifier of the document attribute used for the condition.

For example, âSource_URIâ could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.

Amazon Q Business currently doesnât support `_document_body` as an attribute key used for the condition.

operator -> (string)

The identifier of the document attribute used for the condition.

For example, âSource_URIâ could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.

Amazon Q Business currently does not support `_document_body` as an attribute key used for the condition.

value -> (tagged union structure)

The value of a document attribute. You can only provide one value for a document attribute.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `longValue`, `dateValue`.

stringValue -> (string)

A string.

stringListValue -> (list)

A list of strings.

(string)

longValue -> (long)

A long integer value.

dateValue -> (timestamp)

A date expressed as an ISO 8601 string.

Itâs important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

lambdaArn -> (string)

The Amazon Resource Name (ARN) of the Lambda function sduring ingestion. For more information, see [Using Lambda functions for Amazon Q Business document enrichment](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cde-lambda-operations.html) .

s3BucketName -> (string)

Stores the original, raw documents or the structured, parsed documents before and after altering them. For more information, see [Data contracts for Lambda functions](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/cde-lambda-operations.html#cde-lambda-operations-data-contracts) .

roleArn -> (string)

The Amazon Resource Name (ARN) of a role with permission to run `PreExtractionHookConfiguration` and `PostExtractionHookConfiguration` for altering document metadata and content during the document ingestion process.

mediaExtractionConfiguration -> (structure)

The configuration for extracting information from media in the document.

imageExtractionConfiguration -> (structure)

The configuration for extracting semantic meaning from images in documents. For more information, see [Extracting semantic meaning from images and visuals](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/extracting-meaning-from-images.html) .

imageExtractionStatus -> (string)

Specify whether to extract semantic meaning from images and visuals from documents.

audioExtractionConfiguration -> (structure)

Configuration settings for extracting and processing audio content from media files.

audioExtractionStatus -> (string)

The status of audio extraction (ENABLED or DISABLED) for processing audio content from files.

videoExtractionConfiguration -> (structure)

Configuration settings for extracting and processing video content from media files.

videoExtractionStatus -> (string)

The status of video extraction (ENABLED or DISABLED) for processing video content from files.

JSON Syntax:

```
[
  {
    "id": "string",
    "attributes": [
      {
        "name": "string",
        "value": {
          "stringValue": "string",
          "stringListValue": ["string", ...],
          "longValue": long,
          "dateValue": timestamp
        }
      }
      ...
    ],
    "content": {
      "blob": blob,
      "s3": {
        "bucket": "string",
        "key": "string"
      }
    },
    "contentType": "PDF"|"HTML"|"MS_WORD"|"PLAIN_TEXT"|"PPT"|"RTF"|"XML"|"XSLT"|"MS_EXCEL"|"CSV"|"JSON"|"MD",
    "title": "string",
    "accessConfiguration": {
      "accessControls": [
        {
          "principals": [
            {
              "user": {
                "id": "string",
                "access": "ALLOW"|"DENY",
                "membershipType": "INDEX"|"DATASOURCE"
              },
              "group": {
                "name": "string",
                "access": "ALLOW"|"DENY",
                "membershipType": "INDEX"|"DATASOURCE"
              }
            }
            ...
          ],
          "memberRelation": "AND"|"OR"
        }
        ...
      ],
      "memberRelation": "AND"|"OR"
    },
    "documentEnrichmentConfiguration": {
      "inlineConfigurations": [
        {
          "condition": {
            "key": "string",
            "operator": "GREATER_THAN"|"GREATER_THAN_OR_EQUALS"|"LESS_THAN"|"LESS_THAN_OR_EQUALS"|"EQUALS"|"NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"|"EXISTS"|"NOT_EXISTS"|"BEGINS_WITH",
            "value": {
              "stringValue": "string",
              "stringListValue": ["string", ...],
              "longValue": long,
              "dateValue": timestamp
            }
          },
          "target": {
            "key": "string",
            "value": {
              "stringValue": "string",
              "stringListValue": ["string", ...],
              "longValue": long,
              "dateValue": timestamp
            },
            "attributeValueOperator": "DELETE"
          },
          "documentContentOperator": "DELETE"
        }
        ...
      ],
      "preExtractionHookConfiguration": {
        "invocationCondition": {
          "key": "string",
          "operator": "GREATER_THAN"|"GREATER_THAN_OR_EQUALS"|"LESS_THAN"|"LESS_THAN_OR_EQUALS"|"EQUALS"|"NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"|"EXISTS"|"NOT_EXISTS"|"BEGINS_WITH",
          "value": {
            "stringValue": "string",
            "stringListValue": ["string", ...],
            "longValue": long,
            "dateValue": timestamp
          }
        },
        "lambdaArn": "string",
        "s3BucketName": "string",
        "roleArn": "string"
      },
      "postExtractionHookConfiguration": {
        "invocationCondition": {
          "key": "string",
          "operator": "GREATER_THAN"|"GREATER_THAN_OR_EQUALS"|"LESS_THAN"|"LESS_THAN_OR_EQUALS"|"EQUALS"|"NOT_EQUALS"|"CONTAINS"|"NOT_CONTAINS"|"EXISTS"|"NOT_EXISTS"|"BEGINS_WITH",
          "value": {
            "stringValue": "string",
            "stringListValue": ["string", ...],
            "longValue": long,
            "dateValue": timestamp
          }
        },
        "lambdaArn": "string",
        "s3BucketName": "string",
        "roleArn": "string"
      }
    },
    "mediaExtractionConfiguration": {
      "imageExtractionConfiguration": {
        "imageExtractionStatus": "ENABLED"|"DISABLED"
      },
      "audioExtractionConfiguration": {
        "audioExtractionStatus": "ENABLED"|"DISABLED"
      },
      "videoExtractionConfiguration": {
        "videoExtractionStatus": "ENABLED"|"DISABLED"
      }
    }
  }
  ...
]
```

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role with permission to access your S3 bucket.

`--data-source-sync-id` (string)

The identifier of the data source sync during which the documents were added.

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

failedDocuments -> (list)

A list of documents that were not added to the Amazon Q Business index because the document failed a validation check. Each document contains an error message that indicates why the document couldnât be added to the index.

(structure)

A list of documents that could not be removed from an Amazon Q Business index. Each entry contains an error message that indicates why the document couldnât be removed from the index.

id -> (string)

The identifier of the document that couldnât be removed from the Amazon Q Business index.

error -> (structure)

An explanation for why the document couldnât be removed from the index.

errorMessage -> (string)

The message explaining the Amazon Q Business request error.

errorCode -> (string)

The code associated with the Amazon Q Business request error.

dataSourceId -> (string)

The identifier of the Amazon Q Business data source connector that contains the failed document.