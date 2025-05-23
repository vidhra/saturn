# create-data-sourceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/create-data-source.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/create-data-source.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qbusiness](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/index.html#cli-aws-qbusiness) ]

# create-data-source

## Description

Creates a data source connector for an Amazon Q Business application.

`CreateDataSource` is a synchronous operation. The operation returns 200 if the data source was successfully created. Otherwise, an exception is raised.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qbusiness-2023-11-27/CreateDataSource)

`create-data-source` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
create-data-source
--application-id <value>
--index-id <value>
--display-name <value>
--configuration <value>
[--vpc-configuration <value>]
[--description <value>]
[--tags <value>]
[--sync-schedule <value>]
[--role-arn <value>]
[--client-token <value>]
[--document-enrichment-configuration <value>]
[--media-extraction-configuration <value>]
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

The identifier of the Amazon Q Business application the data source will be attached to.

`--index-id` (string)

The identifier of the index that you want to use with the data source connector.

`--display-name` (string)

A name for the data source connector.

`--configuration` (document)

Configuration information to connect your data source repository to Amazon Q Business. Use this parameter to provide a JSON schema with configuration information specific to your data source connector.

Each data source has a JSON schema provided by Amazon Q Business that you must use. For example, the Amazon S3 and Web Crawler connectors require the following JSON schemas:

- [Amazon S3 JSON schema](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-api.html)
- [Web Crawler JSON schema](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/web-crawler-api.html)

You can find configuration templates for your specific data source using the following steps:

- Navigate to the [Supported connectors](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connectors-list.html) page in the Amazon Q Business User Guide, and select the data source of your choice.
- Then, from your specific data source connector page, select **Using the API** . You will find the JSON schema for your data source, including parameter descriptions, in this section.

JSON Syntax:

```
{...}
```

`--vpc-configuration` (structure)

Configuration information for an Amazon VPC (Virtual Private Cloud) to connect to your data source. For more information, see [Using Amazon VPC with Amazon Q Business connectors](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connector-vpc.html) .

subnetIds -> (list)

A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.

(string)

securityGroupIds -> (list)

A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Q Business to connect to the data source.

(string)

Shorthand Syntax:

```
subnetIds=string,string,securityGroupIds=string,string
```

JSON Syntax:

```
{
  "subnetIds": ["string", ...],
  "securityGroupIds": ["string", ...]
}
```

`--description` (string)

A description for the data source connector.

`--tags` (list)

A list of key-value pairs that identify or categorize the data source connector. You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

(structure)

A list of key/value pairs that identify an index, FAQ, or data source. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

key -> (string)

The key for the tag. Keys are not case sensitive and must be unique for the Amazon Q Business application or data source.

value -> (string)

The value associated with the tag. The value may be an empty string but it canât be null.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
```

`--sync-schedule` (string)

Sets the frequency for Amazon Q Business to check the documents in your data source repository and update your index. If you donât set a schedule, Amazon Q Business wonât periodically update the index.

Specify a `cron-` format schedule string or an empty string to indicate that the index is updated on demand. You canât specify the `Schedule` parameter when the `Type` parameter is set to `CUSTOM` . If you do, you receive a `ValidationException` exception.

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources.

`--client-token` (string)

A token you provide to identify a request to create a data source connector. Multiple calls to the `CreateDataSource` API with the same client token will create only one data source connector.

`--document-enrichment-configuration` (structure)

Provides the configuration information for altering document metadata and content during the document ingestion process.

For more information, see [Custom document enrichment](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html) .

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

JSON Syntax:

```
{
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
}
```

`--media-extraction-configuration` (structure)

The configuration for extracting information from media in documents during ingestion.

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

Shorthand Syntax:

```
imageExtractionConfiguration={imageExtractionStatus=string},audioExtractionConfiguration={audioExtractionStatus=string},videoExtractionConfiguration={videoExtractionStatus=string}
```

JSON Syntax:

```
{
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

dataSourceId -> (string)

The identifier of the data source connector.

dataSourceArn -> (string)

The Amazon Resource Name (ARN) of a data source in an Amazon Q Business application.