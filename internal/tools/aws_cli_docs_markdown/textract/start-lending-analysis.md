# start-lending-analysisÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/start-lending-analysis.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/start-lending-analysis.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [textract](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/index.html#cli-aws-textract) ]

# start-lending-analysis

## Description

Starts the classification and analysis of an input document. `StartLendingAnalysis` initiates the classification and analysis of a packet of lending documents. `StartLendingAnalysis` operates on a document file located in an Amazon S3 bucket.

`StartLendingAnalysis` can analyze text in documents that are in one of the following formats: JPEG, PNG, TIFF, PDF. Use `DocumentLocation` to specify the bucket name and the file name of the document.

`StartLendingAnalysis` returns a job identifier (`JobId` ) that you use to get the results of the operation. When the text analysis is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in `NotificationChannel` . To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If the status is SUCCEEDED you can call either `GetLendingAnalysis` or `GetLendingAnalysisSummary` and provide the `JobId` to obtain the results of the analysis.

If using `OutputConfig` to specify an Amazon S3 bucket, the output will be contained within the specified prefix in a directory labeled with the job-id. In the directory there are 3 sub-directories:

- detailedResponse (contains the GetLendingAnalysis response)
- summaryResponse (for the GetLendingAnalysisSummary response)
- splitDocuments (documents split across logical boundaries)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/textract-2018-06-27/StartLendingAnalysis)

## Synopsis

```
start-lending-analysis
--document-location <value>
[--client-request-token <value>]
[--job-tag <value>]
[--notification-channel <value>]
[--output-config <value>]
[--kms-key-id <value>]
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

The Amazon S3 bucket that contains the document to be processed. Itâs used by asynchronous operations.

The input document can be an image file in JPEG or PNG format. It can also be a file in PDF format.

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

`--client-request-token` (string)

The idempotent token that you use to identify the start request. If you use the same token with multiple `StartLendingAnalysis` requests, the same `JobId` is returned. Use `ClientRequestToken` to prevent the same job from being accidentally started more than once. For more information, see [Calling Amazon Textract Asynchronous Operations](https://docs.aws.amazon.com/textract/latest/dg/api-sync.html) .

`--job-tag` (string)

An identifier that you specify to be included in the completion notification published to the Amazon SNS topic. For example, you can use `JobTag` to identify the type of document that the completion notification corresponds to (such as a tax form or a receipt).

`--notification-channel` (structure)

The Amazon Simple Notification Service (Amazon SNS) topic to which Amazon Textract publishes the completion status of an asynchronous document operation.

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

Sets whether or not your output will go to a user created bucket. Used to set the name of the bucket, and the prefix on the output file.

`OutputConfig` is an optional parameter which lets you adjust where your output will be placed. By default, Amazon Textract will store the results internally and can only be accessed by the Get API operations. With `OutputConfig` enabled, you can set the name of the bucket the output will be sent to the file prefix of the results where you can download your results. Additionally, you can set the `KMSKeyID` parameter to a customer master key (CMK) to encrypt your output. Without this parameter set Amazon Textract will encrypt server-side using the AWS managed CMK for Amazon S3.

Decryption of Customer Content is necessary for processing of the documents by Amazon Textract. If your account is opted out under an AI services opt out policy then all unencrypted Customer Content is immediately and permanently deleted after the Customer Content has been processed by the service. No copy of of the output is retained by Amazon Textract. For information about how to opt out, see [Managing AI services opt-out policy.](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html)

For more information on data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/) .

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

The KMS key used to encrypt the inference results. This can be in either Key ID or Key Alias format. When a KMS key is provided, the KMS key will be used for server-side encryption of the objects in the customer bucket. When this parameter is not enabled, the result will be encrypted server side, using SSE-S3.

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

JobId -> (string)

A unique identifier for the lending or text-detection job. The `JobId` is returned from `StartLendingAnalysis` . A `JobId` value is only valid for 7 days.