# analyze-documentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/analyze-document.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/analyze-document.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [textract](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/index.html#cli-aws-textract) ]

# analyze-document

## Description

Analyzes an input document for relationships between detected items.

The types of information returned are as follows:

- Form data (key-value pairs). The related information is returned in two  Block objects, each of type `KEY_VALUE_SET` : a KEY `Block` object and a VALUE `Block` object. For example, *Name: Ana Silva Carolina* contains a key and value. *Name:* is the key. *Ana Silva Carolina* is the value.
- Table and table cell data. A TABLE `Block` object contains information about a detected table. A CELL `Block` object is returned for each cell in a table.
- Lines and words of text. A LINE `Block` object contains one or more WORD `Block` objects. All lines and words that are detected in the document are returned (including text that doesnât have a relationship with the value of `FeatureTypes` ).
- Signatures. A SIGNATURE `Block` object contains the location information of a signature in a document. If used in conjunction with forms or tables, a signature can be given a Key-Value pairing or be detected in the cell of a table.
- Query. A QUERY Block object contains the query text, alias and link to the associated Query results block object.
- Query Result. A QUERY_RESULT Block object contains the answer to the query and an ID that connects it to the query asked. This Block also contains a confidence score.

Selection elements such as check boxes and option buttons (radio buttons) can be detected in form data and in tables. A SELECTION_ELEMENT `Block` object contains information about a selection element, including the selection status.

You can choose which type of analysis to perform by specifying the `FeatureTypes` list.

The output is returned in a list of `Block` objects.

`AnalyzeDocument` is a synchronous operation. To analyze documents asynchronously, use  StartDocumentAnalysis .

For more information, see [Document Text Analysis](https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/textract-2018-06-27/AnalyzeDocument)

## Synopsis

```
analyze-document
--document <value>
--feature-types <value>
[--human-loop-config <value>]
[--queries-config <value>]
[--adapters-config <value>]
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

`--document` (structure)

The input document as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call Amazon Textract operations, you canât pass image bytes. The document must be an image in JPEG, PNG, PDF, or TIFF format.

If youâre using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes that are passed using the `Bytes` field.

Bytes -> (blob)

A blob of base64-encoded document bytes. The maximum size of a document thatâs provided in a blob of bytes is 5 MB. The document bytes must be in PNG or JPEG format.

If youâre using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes passed using the `Bytes` field.

S3Object -> (structure)

Identifies an S3 object as the document source. The maximum size of a document thatâs stored in an S3 bucket is 5 MB.

Bucket -> (string)

The name of the S3 bucket. Note that the # character is not valid in the file name.

Name -> (string)

The file name of the input document. Synchronous operations can use image files that are in JPEG or PNG format. Asynchronous operations also support PDF and TIFF format files.

Version -> (string)

If the bucket has versioning enabled, you can specify the object version.

Shorthand Syntax:

```
Bytes=blob,S3Object={Bucket=string,Name=string,Version=string}
```

JSON Syntax:

```
{
  "Bytes": blob,
  "S3Object": {
    "Bucket": "string",
    "Name": "string",
    "Version": "string"
  }
}
```

`--feature-types` (list)

A list of the types of analysis to perform. Add TABLES to the list to return information about the tables that are detected in the input document. Add FORMS to return detected form data. Add SIGNATURES to return the locations of detected signatures. Add LAYOUT to the list to return information about the layout of the document. All lines and words detected in the document are included in the response (including text that isnât related to the value of `FeatureTypes` ).

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  TABLES
  FORMS
  QUERIES
  SIGNATURES
  LAYOUT
```

`--human-loop-config` (structure)

Sets the configuration for the human in the loop workflow for analyzing documents.

HumanLoopName -> (string)

The name of the human workflow used for this image. This should be kept unique within a region.

FlowDefinitionArn -> (string)

The Amazon Resource Name (ARN) of the flow definition.

DataAttributes -> (structure)

Sets attributes of the input data.

ContentClassifiers -> (list)

Sets whether the input image is free of personally identifiable information or adult content.

(string)

Shorthand Syntax:

```
HumanLoopName=string,FlowDefinitionArn=string,DataAttributes={ContentClassifiers=[string,string]}
```

JSON Syntax:

```
{
  "HumanLoopName": "string",
  "FlowDefinitionArn": "string",
  "DataAttributes": {
    "ContentClassifiers": ["FreeOfPersonallyIdentifiableInformation"|"FreeOfAdultContent", ...]
  }
}
```

`--queries-config` (structure)

Contains Queries and the alias for those Queries, as determined by the input.

Queries -> (list)

(structure)

Each query contains the question you want to ask in the Text and the alias you want to associate.

Text -> (string)

Question that Amazon Textract will apply to the document. An example would be âWhat is the customerâs SSN?â

Alias -> (string)

Alias attached to the query, for ease of location.

Pages -> (list)

Pages is a parameter that the user inputs to specify which pages to apply a query to. The following is a list of rules for using this parameter.

- If a page is not specified, it is set to `["1"]` by default.
- The following characters are allowed in the parameterâs string: `0 1 2 3 4 5 6 7 8 9 - *` . No whitespace is allowed.
- When using * to indicate all pages, it must be the only element in the list.
- You can use page intervals, such as `[â1-3â, â1-1â, â4-*â]` . Where `*` indicates last page of document.
- Specified pages must be greater than 0 and less than or equal to the number of pages in the document.

(string)

JSON Syntax:

```
{
  "Queries": [
    {
      "Text": "string",
      "Alias": "string",
      "Pages": ["string", ...]
    }
    ...
  ]
}
```

`--adapters-config` (structure)

Specifies the adapter to be used when analyzing a document.

Adapters -> (list)

A list of adapters to be used when analyzing the specified document.

(structure)

An adapter selected for use when analyzing documents. Contains an adapter ID and a version number. Contains information on pages selected for analysis when analyzing documents asychronously.

AdapterId -> (string)

A unique identifier for the adapter resource.

Pages -> (list)

Pages is a parameter that the user inputs to specify which pages to apply an adapter to. The following is a list of rules for using this parameter.

- If a page is not specified, it is set to `["1"]` by default.
- The following characters are allowed in the parameterâs string: `0 1 2 3 4 5 6 7 8 9 - *` . No whitespace is allowed.
- When using * to indicate all pages, it must be the only element in the list.
- You can use page intervals, such as `["1-3", "1-1", "4-*"]` . Where `*` indicates last page of document.
- Specified pages must be greater than 0 and less than or equal to the number of pages in the document.

(string)

Version -> (string)

A string that identifies the version of the adapter.

JSON Syntax:

```
{
  "Adapters": [
    {
      "AdapterId": "string",
      "Pages": ["string", ...],
      "Version": "string"
    }
    ...
  ]
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

**To analyze text in a document**

The following `analyze-document` example shows how to analyze text in a document.

Linux/macOS:

```
aws textract analyze-document \
    --document '{"S3Object":{"Bucket":"bucket","Name":"document"}}' \
    --feature-types '["TABLES","FORMS"]'
```

Windows:

```
aws textract analyze-document \
    --document "{\"S3Object\":{\"Bucket\":\"bucket\",\"Name\":\"document\"}}" \
    --feature-types "[\"TABLES\",\"FORMS\"]" \
    --region region-name
```

Output:

```
{
    "Blocks": [
        {
            "Geometry": {
                "BoundingBox": {
                    "Width": 1.0,
                    "Top": 0.0,
                    "Left": 0.0,
                    "Height": 1.0
                },
                "Polygon": [
                    {
                        "Y": 0.0,
                        "X": 0.0
                    },
                    {
                        "Y": 0.0,
                        "X": 1.0
                    },
                    {
                        "Y": 1.0,
                        "X": 1.0
                    },
                    {
                        "Y": 1.0,
                        "X": 0.0
                    }
                ]
            },
            "Relationships": [
                {
                    "Type": "CHILD",
                    "Ids": [
                        "87586964-d50d-43e2-ace5-8a890657b9a0",
                        "a1e72126-21d9-44f4-a8d6-5c385f9002ba",
                        "e889d012-8a6b-4d2e-b7cd-7a8b327d876a"
                    ]
                }
            ],
            "BlockType": "PAGE",
            "Id": "c2227f12-b25d-4e1f-baea-1ee180d926b2"
        }
    ],
    "DocumentMetadata": {
        "Pages": 1
    }
}
```

For more information, see [Analyzing Document Text with Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/analyzing-document-text.html) in the *Amazon Textract Developers Guide*

## Output

DocumentMetadata -> (structure)

Metadata about the analyzed document. An example is the number of pages.

Pages -> (integer)

The number of pages that are detected in the document.

Blocks -> (list)

The items that are detected and analyzed by `AnalyzeDocument` .

(structure)

A `Block` represents items that are recognized in a document within a group of pixels close to each other. The information returned in a `Block` object depends on the type of operation. In text detection for documents (for example  DetectDocumentText ), you get information about the detected words and lines of text. In text analysis (for example  AnalyzeDocument ), you can also get information about the fields, tables, and selection elements that are detected in the document.

An array of `Block` objects is returned by both synchronous and asynchronous operations. In synchronous operations, such as  DetectDocumentText , the array of `Block` objects is the entire set of results. In asynchronous operations, such as  GetDocumentAnalysis , the array is returned over one or more responses.

For more information, see [How Amazon Textract Works](https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html) .

BlockType -> (string)

The type of text item thatâs recognized. In operations for text detection, the following types are returned:

- *PAGE* - Contains a list of the LINE `Block` objects that are detected on a document page.
- *WORD* - A word detected on a document page. A word is one or more ISO basic Latin script characters that arenât separated by spaces.
- *LINE* - A string of tab-delimited, contiguous words that are detected on a document page.

In text analysis operations, the following types are returned:

- *PAGE* - Contains a list of child `Block` objects that are detected on a document page.
- *KEY_VALUE_SET* - Stores the KEY and VALUE `Block` objects for linked text thatâs detected on a document page. Use the `EntityType` field to determine if a KEY_VALUE_SET object is a KEY `Block` object or a VALUE `Block` object.
- *WORD* - A word thatâs detected on a document page. A word is one or more ISO basic Latin script characters that arenât separated by spaces.
- *LINE* - A string of tab-delimited, contiguous words that are detected on a document page.
- *TABLE* - A table thatâs detected on a document page. A table is grid-based information with two or more rows or columns, with a cell span of one row and one column each.
- *TABLE_TITLE* - The title of a table. A title is typically a line of text above or below a table, or embedded as the first row of a table.
- *TABLE_FOOTER* - The footer associated with a table. A footer is typically a line or lines of text below a table or embedded as the last row of a table.
- *CELL* - A cell within a detected table. The cell is the parent of the block that contains the text in the cell.
- *MERGED_CELL* - A cell in a table whose content spans more than one row or column. The `Relationships` array for this cell contain data from individual cells.
- *SELECTION_ELEMENT* - A selection element such as an option button (radio button) or a check box thatâs detected on a document page. Use the value of `SelectionStatus` to determine the status of the selection element.
- *SIGNATURE* - The location and confidence score of a signature detected on a document page. Can be returned as part of a Key-Value pair or a detected cell.
- *QUERY* - A question asked during the call of AnalyzeDocument. Contains an alias and an ID that attaches it to its answer.
- *QUERY_RESULT* - A response to a question asked during the call of analyze document. Comes with an alias and ID for ease of locating in a response. Also contains location and confidence score.

The following BlockTypes are only returned for Amazon Textract Layout.

- `LAYOUT_TITLE` - The main title of the document.
- `LAYOUT_HEADER` - Text located in the top margin of the document.
- `LAYOUT_FOOTER` - Text located in the bottom margin of the document.
- `LAYOUT_SECTION_HEADER` - The titles of sections within a document.
- `LAYOUT_PAGE_NUMBER` - The page number of the documents.
- `LAYOUT_LIST` - Any information grouped together in list form.
- `LAYOUT_FIGURE` - Indicates the location of an image in a document.
- `LAYOUT_TABLE` - Indicates the location of a table in the document.
- `LAYOUT_KEY_VALUE` - Indicates the location of form key-values in a document.
- `LAYOUT_TEXT` - Text that is present typically as a part of paragraphs in documents.

Confidence -> (float)

The confidence score that Amazon Textract has in the accuracy of the recognized text and the accuracy of the geometry points around the recognized text.

Text -> (string)

The word or line of text thatâs recognized by Amazon Textract.

TextType -> (string)

The kind of text that Amazon Textract has detected. Can check for handwritten text and printed text.

RowIndex -> (integer)

The row in which a table cell is located. The first row position is 1. `RowIndex` isnât returned by `DetectDocumentText` and `GetDocumentTextDetection` .

ColumnIndex -> (integer)

The column in which a table cell appears. The first column position is 1. `ColumnIndex` isnât returned by `DetectDocumentText` and `GetDocumentTextDetection` .

RowSpan -> (integer)

The number of rows that a table cell spans. `RowSpan` isnât returned by `DetectDocumentText` and `GetDocumentTextDetection` .

ColumnSpan -> (integer)

The number of columns that a table cell spans. `ColumnSpan` isnât returned by `DetectDocumentText` and `GetDocumentTextDetection` .

Geometry -> (structure)

The location of the recognized text on the image. It includes an axis-aligned, coarse bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial information.

BoundingBox -> (structure)

An axis-aligned coarse representation of the location of the recognized item on the document page.

Width -> (float)

The width of the bounding box as a ratio of the overall document page width.

Height -> (float)

The height of the bounding box as a ratio of the overall document page height.

Left -> (float)

The left coordinate of the bounding box as a ratio of overall document page width.

Top -> (float)

The top coordinate of the bounding box as a ratio of overall document page height.

Polygon -> (list)

Within the bounding box, a fine-grained polygon around the recognized item.

(structure)

The X and Y coordinates of a point on a document page. The X and Y values that are returned are ratios of the overall document page size. For example, if the input document is 700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the document page.

An array of `Point` objects, `Polygon` , is returned by  DetectDocumentText . `Polygon` represents a fine-grained polygon around detected text. For more information, see Geometry in the Amazon Textract Developer Guide.

X -> (float)

The value of the X coordinate for a point on a `Polygon` .

Y -> (float)

The value of the Y coordinate for a point on a `Polygon` .

Id -> (string)

The identifier for the recognized text. The identifier is only unique for a single operation.

Relationships -> (list)

A list of relationship objects that describe how blocks are related to each other. For example, a LINE block object contains a CHILD relationship type with the WORD blocks that make up the line of text. There arenât Relationship objects in the list for relationships that donât exist, such as when the current block has no child blocks.

(structure)

Information about how blocks are related to each other. A `Block` object contains 0 or more `Relation` objects in a list, `Relationships` . For more information, see  Block .

The `Type` element provides the type of the relationship for all blocks in the `IDs` array.

Type -> (string)

The type of relationship between the blocks in the IDs array and the current block. The following list describes the relationship types that can be returned.

- *VALUE* - A list that contains the ID of the VALUE block thatâs associated with the KEY of a key-value pair.
- *CHILD* - A list of IDs that identify blocks found within the current block object. For example, WORD blocks have a CHILD relationship to the LINE block type.
- *MERGED_CELL* - A list of IDs that identify each of the MERGED_CELL block types in a table.
- *ANSWER* - A list that contains the ID of the QUERY_RESULT block thatâs associated with the corresponding QUERY block.
- *TABLE* - A list of IDs that identify associated TABLE block types.
- *TABLE_TITLE* - A list that contains the ID for the TABLE_TITLE block type in a table.
- *TABLE_FOOTER* - A list of IDs that identify the TABLE_FOOTER block types in a table.

Ids -> (list)

An array of IDs for related blocks. You can get the type of the relationship from the `Type` element.

(string)

EntityTypes -> (list)

The type of entity.

The following entity types can be returned by FORMS analysis:

- *KEY* - An identifier for a field on the document.
- *VALUE* - The field text.

The following entity types can be returned by TABLES analysis:

- *COLUMN_HEADER* - Identifies a cell that is a header of a column.
- *TABLE_TITLE* - Identifies a cell that is a title within the table.
- *TABLE_SECTION_TITLE* - Identifies a cell that is a title of a section within a table. A section title is a cell that typically spans an entire row above a section.
- *TABLE_FOOTER* - Identifies a cell that is a footer of a table.
- *TABLE_SUMMARY* - Identifies a summary cell of a table. A summary cell can be a row of a table or an additional, smaller table that contains summary information for another table.
- *STRUCTURED_TABLE* - Identifies a table with column headers where the content of each row corresponds to the headers.
- *SEMI_STRUCTURED_TABLE* - Identifies a non-structured table.

`EntityTypes` isnât returned by `DetectDocumentText` and `GetDocumentTextDetection` .

(string)

SelectionStatus -> (string)

The selection status of a selection element, such as an option button or check box.

Page -> (integer)

The page on which a block was detected. `Page` is returned by synchronous and asynchronous operations. Page values greater than 1 are only returned for multipage documents that are in PDF or TIFF format. A scanned image (JPEG/PNG) provided to an asynchronous operation, even if it contains multiple document pages, is considered a single-page document. This means that for scanned images the value of `Page` is always 1.

Query -> (structure)

Text -> (string)

Question that Amazon Textract will apply to the document. An example would be âWhat is the customerâs SSN?â

Alias -> (string)

Alias attached to the query, for ease of location.

Pages -> (list)

Pages is a parameter that the user inputs to specify which pages to apply a query to. The following is a list of rules for using this parameter.

- If a page is not specified, it is set to `["1"]` by default.
- The following characters are allowed in the parameterâs string: `0 1 2 3 4 5 6 7 8 9 - *` . No whitespace is allowed.
- When using * to indicate all pages, it must be the only element in the list.
- You can use page intervals, such as `[â1-3â, â1-1â, â4-*â]` . Where `*` indicates last page of document.
- Specified pages must be greater than 0 and less than or equal to the number of pages in the document.

(string)

HumanLoopActivationOutput -> (structure)

Shows the results of the human in the loop evaluation.

HumanLoopArn -> (string)

The Amazon Resource Name (ARN) of the HumanLoop created.

HumanLoopActivationReasons -> (list)

Shows if and why human review was needed.

(string)

HumanLoopActivationConditionsEvaluationResults -> (string)

Shows the result of condition evaluations, including those conditions which activated a human review.

AnalyzeDocumentModelVersion -> (string)

The version of the model used to analyze the document.