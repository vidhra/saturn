# classify-documentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/classify-document.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/classify-document.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [comprehend](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/index.html#cli-aws-comprehend) ]

# classify-document

## Description

Creates a classification request to analyze a single document in real-time. `ClassifyDocument` supports the following model types:

- Custom classifier - a custom model that you have created and trained. For input, you can provide plain text, a single-page document (PDF, Word, or image), or Amazon Textract API output. For more information, see [Custom classification](https://docs.aws.amazon.com/comprehend/latest/dg/how-document-classification.html) in the *Amazon Comprehend Developer Guide* .
- Prompt safety classifier - Amazon Comprehend provides a pre-trained model for classifying input prompts for generative AI applications. For input, you provide English plain text input. For prompt safety classification, the response includes only the `Classes` field. For more information about prompt safety classifiers, see [Prompt safety classification](https://docs.aws.amazon.com/comprehend/latest/dg/trust-safety.html#prompt-classification) in the *Amazon Comprehend Developer Guide* .

If the system detects errors while processing a page in the input document, the API response includes an `Errors` field that describes the errors.

If the system detects a document-level error in your input document, the API returns an `InvalidRequestException` error response. For details about this exception, see [Errors in semi-structured documents](https://docs.aws.amazon.com/comprehend/latest/dg/idp-inputs-sync-err.html) in the Comprehend Developer Guide.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ClassifyDocument)

## Synopsis

```
classify-document
[--text <value>]
--endpoint-arn <value>
[--bytes <value>]
[--document-reader-config <value>]
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

`--text` (string)

The document text to be analyzed. If you enter text using this parameter, do not use the `Bytes` parameter.

`--endpoint-arn` (string)

The Amazon Resource Number (ARN) of the endpoint.

For prompt safety classification, Amazon Comprehend provides the endpoint ARN. For more information about prompt safety classifiers, see [Prompt safety classification](https://docs.aws.amazon.com/comprehend/latest/dg/trust-safety.html#prompt-classification) in the *Amazon Comprehend Developer Guide*

For custom classification, you create an endpoint for your custom model. For more information, see [Using Amazon Comprehend endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/using-endpoints.html) .

`--bytes` (blob)

Use the `Bytes` parameter to input a text, PDF, Word or image file.

When you classify a document using a custom model, you can also use the `Bytes` parameter to input an Amazon Textract `DetectDocumentText` or `AnalyzeDocument` output file.

To classify a document using the prompt safety classifier, use the `Text` parameter for input.

Provide the input document as a sequence of base64-encoded bytes. If your code uses an Amazon Web Services SDK to classify documents, the SDK may encode the document file bytes for you.

The maximum length of this field depends on the input document type. For details, see [Inputs for real-time custom analysis](https://docs.aws.amazon.com/comprehend/latest/dg/idp-inputs-sync.html) in the Comprehend Developer Guide.

If you use the `Bytes` parameter, do not use the `Text` parameter.

`--document-reader-config` (structure)

Provides configuration parameters to override the default actions for extracting text from PDF documents and image files.

DocumentReadAction -> (string)

This field defines the Amazon Textract API operation that Amazon Comprehend uses to extract text from PDF files and image files. Enter one of the following values:

- `TEXTRACT_DETECT_DOCUMENT_TEXT` - The Amazon Comprehend service uses the `DetectDocumentText` API operation.
- `TEXTRACT_ANALYZE_DOCUMENT` - The Amazon Comprehend service uses the `AnalyzeDocument` API operation.

DocumentReadMode -> (string)

Determines the text extraction actions for PDF files. Enter one of the following values:

- `SERVICE_DEFAULT` - use the Amazon Comprehend service defaults for PDF files.
- `FORCE_DOCUMENT_READ_ACTION` - Amazon Comprehend uses the Textract API specified by DocumentReadAction for all PDF files, including digital PDF files.

FeatureTypes -> (list)

Specifies the type of Amazon Textract features to apply. If you chose `TEXTRACT_ANALYZE_DOCUMENT` as the read action, you must specify one or both of the following values:

- `TABLES` - Returns additional information about any tables that are detected in the input document.
- `FORMS` - Returns additional information about any forms that are detected in the input document.

(string)

TABLES or FORMS

Shorthand Syntax:

```
DocumentReadAction=string,DocumentReadMode=string,FeatureTypes=string,string
```

JSON Syntax:

```
{
  "DocumentReadAction": "TEXTRACT_DETECT_DOCUMENT_TEXT"|"TEXTRACT_ANALYZE_DOCUMENT",
  "DocumentReadMode": "SERVICE_DEFAULT"|"FORCE_DOCUMENT_READ_ACTION",
  "FeatureTypes": ["TABLES"|"FORMS", ...]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To classify document with model-specific endpoint**

The following `classify-document` example classifies a document with an endpoint of a custom model. The model in this example was trained on
a dataset containing sms messages labeled as spam or non-spam, or, âhamâ.

```
aws comprehend classify-document \
    --endpoint-arn arn:aws:comprehend:us-west-2:111122223333:document-classifier-endpoint/example-classifier-endpoint \
    --text "CONGRATULATIONS! TXT 1235550100 to win $5000"
```

Output:

```
{
    "Classes": [
        {
            "Name": "spam",
            "Score": 0.9998599290847778
        },
        {
            "Name": "ham",
            "Score": 0.00014001205272506922
        }
    ]
}
```

For more information, see [Custom Classification](https://docs.aws.amazon.com/comprehend/latest/dg/how-document-classification.html) in the *Amazon Comprehend Developer Guide*.

## Output

Classes -> (list)

The classes used by the document being analyzed. These are used for models trained in multi-class mode. Individual classes are mutually exclusive and each document is expected to have only a single class assigned to it. For example, an animal can be a dog or a cat, but not both at the same time.

For prompt safety classification, the response includes only two classes (SAFE_PROMPT and UNSAFE_PROMPT), along with a confidence score for each class. The value range of the score is zero to one, where one is the highest confidence.

(structure)

Specifies the class that categorizes the document being analyzed

Name -> (string)

The name of the class.

Score -> (float)

The confidence score that Amazon Comprehend has this class correctly attributed.

Page -> (integer)

Page number in the input document. This field is present in the response only if your request includes the `Byte` parameter.

Labels -> (list)

The labels used in the document being analyzed. These are used for multi-label trained models. Individual labels represent different categories that are related in some manner and are not mutually exclusive. For example, a movie can be just an action movie, or it can be an action movie, a science fiction movie, and a comedy, all at the same time.

(structure)

Specifies one of the label or labels that categorize the document being analyzed.

Name -> (string)

The name of the label.

Score -> (float)

The confidence score that Amazon Comprehend has this label correctly attributed.

Page -> (integer)

Page number where the label occurs. This field is present in the response only if your request includes the `Byte` parameter.

DocumentMetadata -> (structure)

Extraction information about the document. This field is present in the response only if your request includes the `Byte` parameter.

Pages -> (integer)

Number of pages in the document.

ExtractedCharacters -> (list)

List of pages in the document, with the number of characters extracted from each page.

(structure)

Array of the number of characters extracted from each page.

Page -> (integer)

Page number.

Count -> (integer)

Number of characters extracted from each page.

DocumentType -> (list)

The document type for each page in the input document. This field is present in the response only if your request includes the `Byte` parameter.

(structure)

Document type for each page in the document.

Page -> (integer)

Page number.

Type -> (string)

Document type.

Errors -> (list)

Page-level errors that the system detected while processing the input document. The field is empty if the system encountered no errors.

(structure)

Text extraction encountered one or more page-level errors in the input document.

The `ErrorCode` contains one of the following values:

- TEXTRACT_BAD_PAGE - Amazon Textract cannot read the page. For more information about page limits in Amazon Textract, see [Page Quotas in Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/limits-document.html) .
- TEXTRACT_PROVISIONED_THROUGHPUT_EXCEEDED - The number of requests exceeded your throughput limit. For more information about throughput quotas in Amazon Textract, see [Default quotas in Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/limits-quotas-explained.html) .
- PAGE_CHARACTERS_EXCEEDED - Too many text characters on the page (10,000 characters maximum).
- PAGE_SIZE_EXCEEDED - The maximum page size is 10 MB.
- INTERNAL_SERVER_ERROR - The request encountered a service issue. Try the API request again.

Page -> (integer)

Page number where the error occurred.

ErrorCode -> (string)

Error code for the cause of the error.

ErrorMessage -> (string)

Text message explaining the reason for the error.

Warnings -> (list)

Warnings detected while processing the input document. The response includes a warning if there is a mismatch between the input document type and the model type associated with the endpoint that you specified. The response can also include warnings for individual pages that have a mismatch.

The field is empty if the system generated no warnings.

(structure)

The system identified one of the following warnings while processing the input document:

- The document to classify is plain text, but the classifier is a native document model.
- The document to classify is semi-structured, but the classifier is a plain-text model.

Page -> (integer)

Page number in the input document.

WarnCode -> (string)

The type of warning.

WarnMessage -> (string)

Text message associated with the warning.