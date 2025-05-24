# select-object-contentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/select-object-content.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/select-object-content.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3api](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html#cli-aws-s3api) ]

# select-object-content

## Description

### Note

This operation is not supported for directory buckets.

This action filters the contents of an Amazon S3 object based on a simple structured query language (SQL) statement. In the request, along with the SQL expression, you must also specify a data serialization format (JSON, CSV, or Apache Parquet) of the object. Amazon S3 uses this format to parse object data into records, and returns only records that match the specified SQL expression. You must also specify the data serialization format for the response.

This functionality is not supported for Amazon S3 on Outposts.

For more information about Amazon S3 Select, see [Selecting Content from Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/selecting-content-from-objects.html) and [SELECT Command](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-glacier-select-sql-reference-select.html) in the *Amazon S3 User Guide* .

Permissions

You must have the `s3:GetObject` permission for this operation. Amazon S3 Select does not support anonymous access. For more information about permissions, see [Specifying Permissions in a Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html) in the *Amazon S3 User Guide* .

Object Data Formats

You can use Amazon S3 Select to query objects that have the following format properties:

- *CSV, JSON, and Parquet* - Objects must be in CSV, JSON, or Parquet format.
- *UTF-8* - UTF-8 is the only encoding type Amazon S3 Select supports.
- *GZIP or BZIP2* - CSV and JSON files can be compressed using GZIP or BZIP2. GZIP and BZIP2 are the only compression formats that Amazon S3 Select supports for CSV and JSON files. Amazon S3 Select supports columnar compression for Parquet using GZIP or Snappy. Amazon S3 Select does not support whole-object compression for Parquet objects.
- *Server-side encryption* - Amazon S3 Select supports querying objects that are protected with server-side encryption. For objects that are encrypted with customer-provided encryption keys (SSE-C), you must use HTTPS, and you must use the headers that are documented in the [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) . For more information about SSE-C, see [Server-Side Encryption (Using Customer-Provided Encryption Keys)](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the *Amazon S3 User Guide* . For objects that are encrypted with Amazon S3 managed keys (SSE-S3) and Amazon Web Services KMS keys (SSE-KMS), server-side encryption is handled transparently, so you donât need to specify anything. For more information about server-side encryption, including SSE-S3 and SSE-KMS, see [Protecting Data Using Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html) in the *Amazon S3 User Guide* .

Working with the Response Body

Given the response size is unknown, Amazon S3 Select streams the response as a series of messages and includes a `Transfer-Encoding` header with `chunked` as its value in the response. For more information, see [Appendix: SelectObjectContent Response](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTSelectObjectAppendix.html) .

GetObject Support

The `SelectObjectContent` action does not support the following `GetObject` functionality. For more information, see [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) .

- `Range` : Although you can specify a scan range for an Amazon S3 Select request (see [SelectObjectContentRequest - ScanRange](https://docs.aws.amazon.com/AmazonS3/latest/API/API_SelectObjectContent.html#AmazonS3-SelectObjectContent-request-ScanRange) in the request parameters), you cannot specify the range of bytes of an object to return.
- The `GLACIER` , `DEEP_ARCHIVE` , and `REDUCED_REDUNDANCY` storage classes, or the `ARCHIVE_ACCESS` and `DEEP_ARCHIVE_ACCESS` access tiers of the `INTELLIGENT_TIERING` storage class: You cannot query objects in the `GLACIER` , `DEEP_ARCHIVE` , or `REDUCED_REDUNDANCY` storage classes, nor objects in the `ARCHIVE_ACCESS` or `DEEP_ARCHIVE_ACCESS` access tiers of the `INTELLIGENT_TIERING` storage class. For more information about storage classes, see [Using Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html) in the *Amazon S3 User Guide* .

Special Errors

For a list of special errors for this operation, see [List of SELECT Object Content Error Codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#SelectObjectContentErrorCodeList)

The following operations are related to `SelectObjectContent` :

- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)
- [GetBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html)
- [PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/SelectObjectContent)

## Synopsis

```
select-object-content
--bucket <value>
--key <value>
[--sse-customer-algorithm <value>]
[--sse-customer-key <value>]
[--sse-customer-key-md5 <value>]
--expression <value>
--expression-type <value>
[--request-progress <value>]
--input-serialization <value>
--output-serialization <value>
[--scan-range <value>]
[--expected-bucket-owner <value>]
<outfile>
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

`--bucket` (string)

The S3 bucket.

`--key` (string)

The object key.

`--sse-customer-algorithm` (string)

The server-side encryption (SSE) algorithm used to encrypt the object. This parameter is needed only when the object was created using a checksum algorithm. For more information, see [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the *Amazon S3 User Guide* .

`--sse-customer-key` (string)

The server-side encryption (SSE) customer managed key. This parameter is needed only when the object was created using a checksum algorithm. For more information, see [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the *Amazon S3 User Guide* .

`--sse-customer-key-md5` (string)

The MD5 server-side encryption (SSE) customer managed key. This parameter is needed only when the object was created using a checksum algorithm. For more information, see [Protecting data using SSE-C keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) in the *Amazon S3 User Guide* .

`--expression` (string)

The expression that is used to query the object.

`--expression-type` (string)

The type of the provided expression (for example, SQL).

Possible values:

- `SQL`

`--request-progress` (structure)

Specifies if periodic request progress information should be enabled.

Enabled -> (boolean)

Specifies whether periodic QueryProgress frames should be sent. Valid values: TRUE, FALSE. Default value: FALSE.

Shorthand Syntax:

```
Enabled=boolean
```

JSON Syntax:

```
{
  "Enabled": true|false
}
```

`--input-serialization` (structure)

Describes the format of the data in the object that is being queried.

CSV -> (structure)

Describes the serialization of a CSV-encoded object.

FileHeaderInfo -> (string)

Describes the first line of input. Valid values are:

- `NONE` : First line is not a header.
- `IGNORE` : First line is a header, but you canât use the header values to indicate the column in an expression. You can use column position (such as _1, _2, â¦) to indicate the column (`SELECT s._1 FROM OBJECT s` ).
- `Use` : First line is a header, and you can use the header value to identify a column in an expression (`SELECT "name" FROM OBJECT` ).

Comments -> (string)

A single character used to indicate that a row should be ignored when the character is present at the start of that row. You can specify any character to indicate a comment line. The default character is `#` .

Default: `#`

QuoteEscapeCharacter -> (string)

A single character used for escaping the quotation mark character inside an already escaped value. For example, the value `""" a , b """` is parsed as `" a , b "` .

RecordDelimiter -> (string)

A single character used to separate individual records in the input. Instead of the default value, you can specify an arbitrary delimiter.

FieldDelimiter -> (string)

A single character used to separate individual fields in a record. You can specify an arbitrary delimiter.

QuoteCharacter -> (string)

A single character used for escaping when the field delimiter is part of the value. For example, if the value is `a, b` , Amazon S3 wraps this field value in quotation marks, as follows: `" a , b "` .

Type: String

Default: `"`

Ancestors: `CSV`

AllowQuotedRecordDelimiter -> (boolean)

Specifies that CSV field values may contain quoted record delimiters and such records should be allowed. Default value is FALSE. Setting this value to TRUE may lower performance.

CompressionType -> (string)

Specifies objectâs compression format. Valid values: NONE, GZIP, BZIP2. Default Value: NONE.

JSON -> (structure)

Specifies JSON as objectâs input serialization format.

Type -> (string)

The type of JSON. Valid values: Document, Lines.

Parquet -> (structure)

Specifies Parquet as objectâs input serialization format.

Shorthand Syntax:

```
CSV={FileHeaderInfo=string,Comments=string,QuoteEscapeCharacter=string,RecordDelimiter=string,FieldDelimiter=string,QuoteCharacter=string,AllowQuotedRecordDelimiter=boolean},CompressionType=string,JSON={Type=string},Parquet={}
```

JSON Syntax:

```
{
  "CSV": {
    "FileHeaderInfo": "USE"|"IGNORE"|"NONE",
    "Comments": "string",
    "QuoteEscapeCharacter": "string",
    "RecordDelimiter": "string",
    "FieldDelimiter": "string",
    "QuoteCharacter": "string",
    "AllowQuotedRecordDelimiter": true|false
  },
  "CompressionType": "NONE"|"GZIP"|"BZIP2",
  "JSON": {
    "Type": "DOCUMENT"|"LINES"
  },
  "Parquet": {

  }
}
```

`--output-serialization` (structure)

Describes the format of the data that you want Amazon S3 to return in response.

CSV -> (structure)

Describes the serialization of CSV-encoded Select results.

QuoteFields -> (string)

Indicates whether to use quotation marks around output fields.

- `ALWAYS` : Always use quotation marks for output fields.
- `ASNEEDED` : Use quotation marks for output fields when needed.

QuoteEscapeCharacter -> (string)

The single character used for escaping the quote character inside an already escaped value.

RecordDelimiter -> (string)

A single character used to separate individual records in the output. Instead of the default value, you can specify an arbitrary delimiter.

FieldDelimiter -> (string)

The value used to separate individual fields in a record. You can specify an arbitrary delimiter.

QuoteCharacter -> (string)

A single character used for escaping when the field delimiter is part of the value. For example, if the value is `a, b` , Amazon S3 wraps this field value in quotation marks, as follows: `" a , b "` .

JSON -> (structure)

Specifies JSON as requestâs output serialization format.

RecordDelimiter -> (string)

The value used to separate individual records in the output. If no value is specified, Amazon S3 uses a newline character (ânâ).

Shorthand Syntax:

```
CSV={QuoteFields=string,QuoteEscapeCharacter=string,RecordDelimiter=string,FieldDelimiter=string,QuoteCharacter=string},JSON={RecordDelimiter=string}
```

JSON Syntax:

```
{
  "CSV": {
    "QuoteFields": "ALWAYS"|"ASNEEDED",
    "QuoteEscapeCharacter": "string",
    "RecordDelimiter": "string",
    "FieldDelimiter": "string",
    "QuoteCharacter": "string"
  },
  "JSON": {
    "RecordDelimiter": "string"
  }
}
```

`--scan-range` (structure)

Specifies the byte range of the object to get the records from. A record is processed when its first byte is contained by the range. This parameter is optional, but when specified, it must not be empty. See RFC 2616, Section 14.35.1 about how to specify the start and end of the range.

`ScanRange` may be used in the following ways:

- `<scanrange><start>50</start><end>100</end></scanrange>` - process only the records starting between the bytes 50 and 100 (inclusive, counting from zero)
- `<scanrange><start>50</start></scanrange>` - process only the records starting after the byte 50
- `<scanrange><end>50</end></scanrange>` - process only the records within the last 50 bytes of the file.

Start -> (long)

Specifies the start of the byte range. This parameter is optional. Valid values: non-negative integers. The default value is 0. If only `start` is supplied, it means scan from that point to the end of the file. For example, `<scanrange><start>50</start></scanrange>` means scan from byte 50 until the end of the file.

End -> (long)

Specifies the end of the byte range. This parameter is optional. Valid values: non-negative integers. The default value is one less than the size of the object being queried. If only the End parameter is supplied, it is interpreted to mean scan the last N bytes of the file. For example, `<scanrange><end>50</end></scanrange>` means scan the last 50 bytes.

Shorthand Syntax:

```
Start=long,End=long
```

JSON Syntax:

```
{
  "Start": long,
  "End": long
}
```

`--expected-bucket-owner` (string)

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

`outfile` (string)
Filename where the records will be saved

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

**To filter the contents of an Amazon S3 object based on an SQL statement**

The following `select-object-content` example filters the object `my-data-file.csv` with the specified SQL statement and sends output to a file.

```
aws s3api select-object-content \
    --bucket amzn-s3-demo-bucket \
    --key my-data-file.csv \
    --expression "select * from s3object limit 100" \
    --expression-type 'SQL' \
    --input-serialization '{"CSV": {}, "CompressionType": "NONE"}' \
    --output-serialization '{"CSV": {}}' "output.csv"
```

This command produces no output.

## Output

This command generates no output.  The selected object content is written to the specified outfile.