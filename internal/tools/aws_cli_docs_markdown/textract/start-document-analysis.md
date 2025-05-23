# start-document-analysisÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/start-document-analysis.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/start-document-analysis.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [textract](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/index.html#cli-aws-textract) ]

# start-document-analysis

## Description

Starts the asynchronous analysis of an input document for relationships between detected items such as key-value pairs, tables, and selection elements.

`StartDocumentAnalysis` can analyze text in documents that are in JPEG, PNG, TIFF, and PDF format. The documents are stored in an Amazon S3 bucket. Use  DocumentLocation to specify the bucket name and file name of the document.

`StartDocumentAnalysis` returns a job identifier (`JobId` ) that you use to get the results of the operation. When text analysis is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in `NotificationChannel` . To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is `SUCCEEDED` . If so, call  GetDocumentAnalysis , and pass the job identifier (`JobId` ) from the initial call to `StartDocumentAnalysis` .

For more information, see [Document Text Analysis](https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/textract-2018-06-27/StartDocumentAnalysis)

## Synopsis

```
start-document-analysis
--document-location <value>
--feature-types <value>
[--client-request-token <value>]
[--job-tag <value>]
[--notification-channel <value>]
[--output-config <value>]
[--kms-key-id <value>]
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

`--document-location` (structure)

The location of the document to be processed.

S3Object -> (structure)

The Amazon S3 bucket that contains the input document.

Bucket -> (string)

The name of the S3 bucket. Note that the # character is not valid in the file name.

Name -> (string)

The file name of the input document. Synchronous operations can use image files that are in JPEG or PNG format. Asynchronous operations also support PDF and TIFF format files.

Version -> (string)

If the bucket has versioning enabled, you can specify the object version.

Shorthand Syntax:

```
S3Object={Bucket=string,Name=string,Version=string}
```

JSON Syntax:

```
{
  "S3Object": {
    "Bucket": "string",
    "Name": "string",
    "Version": "string"
  }
}
```

`--feature-types` (list)

A list of the types of analysis to perform. Add TABLES to the list to return information about the tables that are detected in the input document. Add FORMS to return detected form data. To perform both types of analysis, add TABLES and FORMS to `FeatureTypes` . All lines and words detected in the document are included in the response (including text that isnât related to the value of `FeatureTypes` ).

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

`--client-request-token` (string)

The idempotent token that you use to identify the start request. If you use the same token with multiple `StartDocumentAnalysis` requests, the same `JobId` is returned. Use `ClientRequestToken` to prevent the same job from being accidentally started more than once. For more information, see [Calling Amazon Textract Asynchronous Operations](https://docs.aws.amazon.com/textract/latest/dg/api-async.html) .

`--job-tag` (string)

An identifier that you specify thatâs included in the completion notification published to the Amazon SNS topic. For example, you can use `JobTag` to identify the type of document that the completion notification corresponds to (such as a tax form or a receipt).

`--notification-channel` (structure)

The Amazon SNS topic ARN that you want Amazon Textract to publish the completion status of the operation to.

SNSTopicArn -> (string)

The Amazon SNS topic that Amazon Textract posts the completion status to.

RoleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role that gives Amazon Textract publishing permissions to the Amazon SNS topic.

Shorthand Syntax:

```
SNSTopicArn=string,RoleArn=string
```

JSON Syntax:

```
{
  "SNSTopicArn": "string",
  "RoleArn": "string"
}
```

`--output-config` (structure)

Sets if the output will go to a customer defined bucket. By default, Amazon Textract will save the results internally to be accessed by the GetDocumentAnalysis operation.

S3Bucket -> (string)

The name of the bucket your output will go to.

S3Prefix -> (string)

The prefix of the object key that the output will be saved to. When not enabled, the prefix will be âtextract_outputâ.

Shorthand Syntax:

```
S3Bucket=string,S3Prefix=string
```

JSON Syntax:

```
{
  "S3Bucket": "string",
  "S3Prefix": "string"
}
```

`--kms-key-id` (string)

The KMS key used to encrypt the inference results. This can be in either Key ID or Key Alias format. When a KMS key is provided, the KMS key will be used for server-side encryption of the objects in the customer bucket. When this parameter is not enabled, the result will be encrypted server side,using SSE-S3.

`--queries-config` (structure)

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

**To start analyzing text in a multi-page document**

The following `start-document-analysis` example shows how to start asynchronous analysis of text in a multi-page document.

Linux/macOS:

```
aws textract start-document-analysis \
    --document-location '{"S3Object":{"Bucket":"bucket","Name":"document"}}' \
    --feature-types '["TABLES","FORMS"]' \
    --notification-channel "SNSTopicArn=arn:snsTopic,RoleArn=roleArn"
```

Windows:

```
aws textract start-document-analysis \
    --document-location "{\"S3Object\":{\"Bucket\":\"bucket\",\"Name\":\"document\"}}" \
    --feature-types "[\"TABLES\", \"FORMS\"]" \
    --region region-name \
    --notification-channel "SNSTopicArn=arn:snsTopic,RoleArn=roleArn"
```

Output:

```
{
    "JobId": "df7cf32ebbd2a5de113535fcf4d921926a701b09b4e7d089f3aebadb41e0712b"
}
```

For more information, see [Detecting and Analyzing Text in Multi-Page Documents](https://docs.aws.amazon.com/textract/latest/dg/async.html) in the *Amazon Textract Developers Guide*

## Output

JobId -> (string)

The identifier for the document text detection job. Use `JobId` to identify the job in a subsequent call to `GetDocumentAnalysis` . A `JobId` value is only valid for 7 days.