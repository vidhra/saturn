# analyze-expenseÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/analyze-expense.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/analyze-expense.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [textract](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/index.html#cli-aws-textract) ]

# analyze-expense

## Description

`AnalyzeExpense` synchronously analyzes an input document for financially related relationships between text.

Information is returned as `ExpenseDocuments` and seperated as follows:

- `LineItemGroups` - A data set containing `LineItems` which store information about the lines of text, such as an item purchased and its price on a receipt.
- `SummaryFields` - Contains all other information a receipt, such as header information or the vendors name.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/textract-2018-06-27/AnalyzeExpense)

## Synopsis

```
analyze-expense
--document <value>
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

The input document, either as bytes or as an S3 object.

You pass image bytes to an Amazon Textract API operation by using the `Bytes` property. For example, you would use the `Bytes` property to pass a document loaded from a local file system. Image bytes passed by using the `Bytes` property must be base64 encoded. Your code might not need to encode document file bytes if youâre using an AWS SDK to call Amazon Textract API operations.

You pass images stored in an S3 bucket to an Amazon Textract API operation by using the `S3Object` property. Documents stored in an S3 bucket donât need to be base64 encoded.

The AWS Region for the S3 bucket that contains the S3 object must match the AWS Region that you use for Amazon Textract operations.

If you use the AWS CLI to call Amazon Textract operations, passing image bytes using the Bytes property isnât supported. You must first upload the document to an Amazon S3 bucket, and then call the operation using the S3Object property.

For Amazon Textract to process an S3 object, the user must have permission to access the S3 object.

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

DocumentMetadata -> (structure)

Information about the input document.

Pages -> (integer)

The number of pages that are detected in the document.

ExpenseDocuments -> (list)

The expenses detected by Amazon Textract.

(structure)

The structure holding all the information returned by AnalyzeExpense

ExpenseIndex -> (integer)

Denotes which invoice or receipt in the document the information is coming from. First document will be 1, the second 2, and so on.

SummaryFields -> (list)

Any information found outside of a table by Amazon Textract.

(structure)

Breakdown of detected information, seperated into the catagories Type, LabelDetection, and ValueDetection

Type -> (structure)

The implied label of a detected element. Present alongside LabelDetection for explicit elements.

Text -> (string)

The word or line of text detected by Amazon Textract.

Confidence -> (float)

The confidence of accuracy, as a percentage.

LabelDetection -> (structure)

The explicitly stated label of a detected element.

Text -> (string)

The word or line of text recognized by Amazon Textract

Geometry -> (structure)

Information about where the following items are located on a document page: detected page, text, key-value pairs, tables, table cells, and selection elements.

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

Confidence -> (float)

The confidence in detection, as a percentage

ValueDetection -> (structure)

The value of a detected element. Present in explicit and implicit elements.

Text -> (string)

The word or line of text recognized by Amazon Textract

Geometry -> (structure)

Information about where the following items are located on a document page: detected page, text, key-value pairs, tables, table cells, and selection elements.

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

Confidence -> (float)

The confidence in detection, as a percentage

PageNumber -> (integer)

The page number the value was detected on.

Currency -> (structure)

Shows the kind of currency, both the code and confidence associated with any monatary value detected.

Code -> (string)

Currency code for detected currency. the current supported codes are:

- USD
- EUR
- GBP
- CAD
- INR
- JPY
- CHF
- AUD
- CNY
- BZR
- SEK
- HKD

Confidence -> (float)

Percentage confideence in the detected currency.

GroupProperties -> (list)

Shows which group a response object belongs to, such as whether an address line belongs to the vendorâs address or the recipentâs address.

(structure)

Shows the group that a certain key belongs to. This helps differentiate between names and addresses for different organizations, that can be hard to determine via JSON response.

Types -> (list)

Informs you on whether the expense group is a name or an address.

(string)

Id -> (string)

Provides a group Id number, which will be the same for each in the group.

LineItemGroups -> (list)

Information detected on each table of a document, seperated into `LineItems` .

(structure)

A grouping of tables which contain LineItems, with each table identified by the tableâs `LineItemGroupIndex` .

LineItemGroupIndex -> (integer)

The number used to identify a specific table in a document. The first table encountered will have a LineItemGroupIndex of 1, the second 2, etc.

LineItems -> (list)

The breakdown of information on a particular line of a table.

(structure)

A structure that holds information about the different lines found in a documentâs tables.

LineItemExpenseFields -> (list)

ExpenseFields used to show information from detected lines on a table.

(structure)

Breakdown of detected information, seperated into the catagories Type, LabelDetection, and ValueDetection

Type -> (structure)

The implied label of a detected element. Present alongside LabelDetection for explicit elements.

Text -> (string)

The word or line of text detected by Amazon Textract.

Confidence -> (float)

The confidence of accuracy, as a percentage.

LabelDetection -> (structure)

The explicitly stated label of a detected element.

Text -> (string)

The word or line of text recognized by Amazon Textract

Geometry -> (structure)

Information about where the following items are located on a document page: detected page, text, key-value pairs, tables, table cells, and selection elements.

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

Confidence -> (float)

The confidence in detection, as a percentage

ValueDetection -> (structure)

The value of a detected element. Present in explicit and implicit elements.

Text -> (string)

The word or line of text recognized by Amazon Textract

Geometry -> (structure)

Information about where the following items are located on a document page: detected page, text, key-value pairs, tables, table cells, and selection elements.

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

Confidence -> (float)

The confidence in detection, as a percentage

PageNumber -> (integer)

The page number the value was detected on.

Currency -> (structure)

Shows the kind of currency, both the code and confidence associated with any monatary value detected.

Code -> (string)

Currency code for detected currency. the current supported codes are:

- USD
- EUR
- GBP
- CAD
- INR
- JPY
- CHF
- AUD
- CNY
- BZR
- SEK
- HKD

Confidence -> (float)

Percentage confideence in the detected currency.

GroupProperties -> (list)

Shows which group a response object belongs to, such as whether an address line belongs to the vendorâs address or the recipentâs address.

(structure)

Shows the group that a certain key belongs to. This helps differentiate between names and addresses for different organizations, that can be hard to determine via JSON response.

Types -> (list)

Informs you on whether the expense group is a name or an address.

(string)

Id -> (string)

Provides a group Id number, which will be the same for each in the group.

Blocks -> (list)

This is a block object, the same as reported when DetectDocumentText is run on a document. It provides word level recognition of text.

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