# get-lending-analysis-summaryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/get-lending-analysis-summary.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/get-lending-analysis-summary.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [textract](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/index.html#cli-aws-textract) ]

# get-lending-analysis-summary

## Description

Gets summarized results for the `StartLendingAnalysis` operation, which analyzes text in a lending document. The returned summary consists of information about documents grouped together by a common document type. Information like detected signatures, page numbers, and split documents is returned with respect to the type of grouped document.

You start asynchronous text analysis by calling `StartLendingAnalysis` , which returns a job identifier (`JobId` ). When the text analysis operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic thatâs registered in the initial call to `StartLendingAnalysis` .

To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If so, call `GetLendingAnalysisSummary` , and pass the job identifier (`JobId` ) from the initial call to `StartLendingAnalysis` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/textract-2018-06-27/GetLendingAnalysisSummary)

## Synopsis

```
get-lending-analysis-summary
--job-id <value>
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

`--job-id` (string)

A unique identifier for the lending or text-detection job. The `JobId` is returned from StartLendingAnalysis. A `JobId` value is only valid for 7 days.

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

JobStatus -> (string)

The current status of the lending analysis job.

Summary -> (structure)

Contains summary information for documents grouped by type.

DocumentGroups -> (list)

Contains an array of all DocumentGroup objects.

(structure)

Summary information about documents grouped by the same document type.

Type -> (string)

The type of document that Amazon Textract has detected. See [Analyze Lending Response Objects](https://docs.aws.amazon.com/textract/latest/dg/lending-response-objects.html) for a list of all types returned by Textract.

SplitDocuments -> (list)

An array that contains information about the pages of a document, defined by logical boundary.

(structure)

Contains information about the pages of a document, defined by logical boundary.

Index -> (integer)

The index for a given document in a DocumentGroup of a specific Type.

Pages -> (list)

An array of page numbers for a for a given document, ordered by logical boundary.

(integer)

DetectedSignatures -> (list)

A list of the detected signatures found in a document group.

(structure)

A structure that holds information regarding a detected signature on a page.

Page -> (integer)

The page a detected signature was found on.

UndetectedSignatures -> (list)

A list of any expected signatures not found in a document group.

(structure)

A structure containing information about an undetected signature on a page where it was expected but not found.

Page -> (integer)

The page where a signature was expected but not found.

UndetectedDocumentTypes -> (list)

UndetectedDocumentTypes.

(string)

Warnings -> (list)

A list of warnings that occurred during the lending analysis operation.

(structure)

A warning about an issue that occurred during asynchronous text analysis ( StartDocumentAnalysis ) or asynchronous document text detection ( StartDocumentTextDetection ).

ErrorCode -> (string)

The error code for the warning.

Pages -> (list)

A list of the pages that the warning applies to.

(integer)

StatusMessage -> (string)

Returns if the lending analysis could not be completed. Contains explanation for what error occurred.

AnalyzeLendingModelVersion -> (string)

The current model version of the Analyze Lending API.