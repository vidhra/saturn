# detect-entitiesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/detect-entities.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/detect-entities.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [comprehend](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/index.html#cli-aws-comprehend) ]

# detect-entities

## Description

Detects named entities in input text when you use the pre-trained model. Detects custom entities if you have a custom entity recognition model.

When detecting named entities using the pre-trained model, use plain text as the input. For more information about named entities, see [Entities](https://docs.aws.amazon.com/comprehend/latest/dg/how-entities.html) in the Comprehend Developer Guide.

When you use a custom entity recognition model, you can input plain text or you can upload a single-page input document (text, PDF, Word, or image).

If the system detects errors while processing a page in the input document, the API response includes an entry in `Errors` for each error.

If the system detects a document-level error in your input document, the API returns an `InvalidRequestException` error response. For details about this exception, see [Errors in semi-structured documents](https://docs.aws.amazon.com/comprehend/latest/dg/idp-inputs-sync-err.html) in the Comprehend Developer Guide.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DetectEntities)

## Synopsis

```
detect-entities
[--text <value>]
[--language-code <value>]
[--endpoint-arn <value>]
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

A UTF-8 text string. The maximum string size is 100 KB. If you enter text using this parameter, do not use the `Bytes` parameter.

`--language-code` (string)

The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. If your request includes the endpoint for a custom entity recognition model, Amazon Comprehend uses the language of your custom model, and it ignores any language code that you specify here.

All input documents must be in the same language.

Possible values:

- `en`
- `es`
- `fr`
- `de`
- `it`
- `pt`
- `ar`
- `hi`
- `ja`
- `ko`
- `zh`
- `zh-TW`

`--endpoint-arn` (string)

The Amazon Resource Name of an endpoint that is associated with a custom entity recognition model. Provide an endpoint if you want to detect entities by using your own custom model instead of the default model that is used by Amazon Comprehend.

If you specify an endpoint, Amazon Comprehend uses the language of your custom model, and it ignores any language code that you provide in your request.

For information about endpoints, see [Managing endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html) .

`--bytes` (blob)

This field applies only when you use a custom entity recognition model that was trained with PDF annotations. For other cases, enter your text input in the `Text` field.

Use the `Bytes` parameter to input a text, PDF, Word or image file. Using a plain-text file in the `Bytes` parameter is equivelent to using the `Text` parameter (the `Entities` field in the response is identical).

You can also use the `Bytes` parameter to input an Amazon Textract `DetectDocumentText` or `AnalyzeDocument` output file.

Provide the input document as a sequence of base64-encoded bytes. If your code uses an Amazon Web Services SDK to detect entities, the SDK may encode the document file bytes for you.

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

**To detect named entities in input text**

The following `detect-entities` example analyzes the input text and returns the named entities. The pre-trained modelâs confidence score
is also output for each prediction.

```
aws comprehend detect-entities \
    --language-code en \
    --text "Hello Zhang Wei, I am John. Your AnyCompany Financial Services, LLC credit card \
    account 1111-XXXX-1111-XXXX has a minimum payment of $24.53 that is due by July 31st. Based on your autopay settings, \
    we will withdraw your payment on the due date from your bank account number XXXXXX1111 with the routing number XXXXX0000. \
    Customer feedback for Sunshine Spa, 123 Main St, Anywhere. Send comments to Alice at AnySpa@example.com."
```

Output:

```
{
    "Entities": [
        {
            "Score": 0.9994556307792664,
            "Type": "PERSON",
            "Text": "Zhang Wei",
            "BeginOffset": 6,
            "EndOffset": 15
        },
        {
            "Score": 0.9981022477149963,
            "Type": "PERSON",
            "Text": "John",
            "BeginOffset": 22,
            "EndOffset": 26
        },
        {
            "Score": 0.9986887574195862,
            "Type": "ORGANIZATION",
            "Text": "AnyCompany Financial Services, LLC",
            "BeginOffset": 33,
            "EndOffset": 67
        },
        {
            "Score": 0.9959119558334351,
            "Type": "OTHER",
            "Text": "1111-XXXX-1111-XXXX",
            "BeginOffset": 88,
            "EndOffset": 107
        },
        {
            "Score": 0.9708039164543152,
            "Type": "QUANTITY",
            "Text": ".53",
            "BeginOffset": 133,
            "EndOffset": 136
        },
        {
            "Score": 0.9987268447875977,
            "Type": "DATE",
            "Text": "July 31st",
            "BeginOffset": 152,
            "EndOffset": 161
        },
        {
            "Score": 0.9858865737915039,
            "Type": "OTHER",
            "Text": "XXXXXX1111",
            "BeginOffset": 271,
            "EndOffset": 281
        },
        {
            "Score": 0.9700471758842468,
            "Type": "OTHER",
            "Text": "XXXXX0000",
            "BeginOffset": 306,
            "EndOffset": 315
        },
        {
            "Score": 0.9591118693351746,
            "Type": "ORGANIZATION",
            "Text": "Sunshine Spa",
            "BeginOffset": 340,
            "EndOffset": 352
        },
        {
            "Score": 0.9797496795654297,
            "Type": "LOCATION",
            "Text": "123 Main St",
            "BeginOffset": 354,
            "EndOffset": 365
        },
        {
            "Score": 0.994929313659668,
            "Type": "PERSON",
            "Text": "Alice",
            "BeginOffset": 394,
            "EndOffset": 399
        },
        {
            "Score": 0.9949769377708435,
            "Type": "OTHER",
            "Text": "AnySpa@example.com",
            "BeginOffset": 403,
            "EndOffset": 418
        }
    ]
}
```

For more information, see [Entities](https://docs.aws.amazon.com/comprehend/latest/dg/how-entities.html) in the *Amazon Comprehend Developer Guide*.

## Output

Entities -> (list)

A collection of entities identified in the input text. For each entity, the response provides the entity text, entity type, where the entity text begins and ends, and the level of confidence that Amazon Comprehend has in the detection.

If your request uses a custom entity recognition model, Amazon Comprehend detects the entities that the model is trained to recognize. Otherwise, it detects the default entity types. For a list of default entity types, see [Entities](https://docs.aws.amazon.com/comprehend/latest/dg/how-entities.html) in the Comprehend Developer Guide.

(structure)

Provides information about an entity.

Score -> (float)

The level of confidence that Amazon Comprehend has in the accuracy of the detection.

Type -> (string)

The entity type. For entity detection using the built-in model, this field contains one of the standard entity types listed below.

For custom entity detection, this field contains one of the entity types that you specified when you trained your custom model.

Text -> (string)

The text of the entity.

BeginOffset -> (integer)

The zero-based offset from the beginning of the source text to the first character in the entity.

This field is empty for non-text input.

EndOffset -> (integer)

The zero-based offset from the beginning of the source text to the last character in the entity.

This field is empty for non-text input.

BlockReferences -> (list)

A reference to each block for this entity. This field is empty for plain-text input.

(structure)

A reference to a block.

BlockId -> (string)

Unique identifier for the block.

BeginOffset -> (integer)

Offset of the start of the block within its parent block.

EndOffset -> (integer)

Offset of the end of the block within its parent block.

ChildBlocks -> (list)

List of child blocks within this block.

(structure)

Nested block contained within a block.

ChildBlockId -> (string)

Unique identifier for the child block.

BeginOffset -> (integer)

Offset of the start of the child block within its parent block.

EndOffset -> (integer)

Offset of the end of the child block within its parent block.

DocumentMetadata -> (structure)

Information about the document, discovered during text extraction. This field is present in the response only if your request used the `Byte` parameter.

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

The document type for each page in the input document. This field is present in the response only if your request used the `Byte` parameter.

(structure)

Document type for each page in the document.

Page -> (integer)

Page number.

Type -> (string)

Document type.

Blocks -> (list)

Information about each block of text in the input document. Blocks are nested. A page block contains a block for each line of text, which contains a block for each word.

The `Block` content for a Word input document does not include a `Geometry` field.

The `Block` field is not present in the response for plain-text inputs.

(structure)

Information about each word or line of text in the input document.

For additional information, see [Block](https://docs.aws.amazon.com/textract/latest/dg/API_Block.html) in the Amazon Textract API reference.

Id -> (string)

Unique identifier for the block.

BlockType -> (string)

The block represents a line of text or one word of text.

- WORD - A word thatâs detected on a document page. A word is one or more ISO basic Latin script characters that arenât separated by spaces.
- LINE - A string of tab-delimited, contiguous words that are detected on a document page

Text -> (string)

The word or line of text extracted from the block.

Page -> (integer)

Page number where the block appears.

Geometry -> (structure)

Co-ordinates of the rectangle or polygon that contains the text.

BoundingBox -> (structure)

An axis-aligned coarse representation of the location of the recognized item on the document page.

Height -> (float)

The height of the bounding box as a ratio of the overall document page height.

Left -> (float)

The left coordinate of the bounding box as a ratio of overall document page width.

Top -> (float)

The top coordinate of the bounding box as a ratio of overall document page height.

Width -> (float)

The width of the bounding box as a ratio of the overall document page width.

Polygon -> (list)

Within the bounding box, a fine-grained polygon around the recognized item.

(structure)

The X and Y coordinates of a point on a document page.

For additional information, see [Point](https://docs.aws.amazon.com/textract/latest/dg/API_Point.html) in the Amazon Textract API reference.

X -> (float)

The value of the X coordinate for a point on a polygon

Y -> (float)

The value of the Y coordinate for a point on a polygon

Relationships -> (list)

A list of child blocks of the current block. For example, a LINE object has child blocks for each WORD block thatâs part of the line of text.

(structure)

List of child blocks for the current block.

Ids -> (list)

Identifers of the child blocks.

(string)

Type -> (string)

Only supported relationship is a child relationship.

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