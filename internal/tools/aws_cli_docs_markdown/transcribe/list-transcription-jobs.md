# list-transcription-jobsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-transcription-jobs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-transcription-jobs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transcribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/index.html#cli-aws-transcribe) ]

# list-transcription-jobs

## Description

Provides a list of transcription jobs that match the specified criteria. If no criteria are specified, all transcription jobs are returned.

To get detailed information about a specific transcription job, use the operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/ListTranscriptionJobs)

## Synopsis

```
list-transcription-jobs
[--status <value>]
[--job-name-contains <value>]
[--next-token <value>]
[--max-results <value>]
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

`--status` (string)

Returns only transcription jobs with the specified status. Jobs are ordered by creation date, with the newest job first. If you do not include `Status` , all transcription jobs are returned.

Possible values:

- `QUEUED`
- `IN_PROGRESS`
- `FAILED`
- `COMPLETED`

`--job-name-contains` (string)

Returns only the transcription jobs that contain the specified string. The search is not case sensitive.

`--next-token` (string)

If your `ListTranscriptionJobs` request returns more results than can be displayed, `NextToken` is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including `NextToken` with the value of the copied string. Repeat as needed to view all your results.

`--max-results` (integer)

The maximum number of transcription jobs to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.

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

**To list your transcription jobs**

The following `list-transcription-jobs` example lists the transcription jobs associated with your AWS account and Region.

```
aws transcribe list-transcription-jobs
```

Output:

```
{
    "NextToken": "NextToken",
    "TranscriptionJobSummaries": [
        {
            "TranscriptionJobName": "speak-id-job-1",
            "CreationTime": "2020-08-17T21:06:15.391000+00:00",
            "StartTime": "2020-08-17T21:06:15.416000+00:00",
            "CompletionTime": "2020-08-17T21:07:05.098000+00:00",
            "LanguageCode": "language-code",
            "TranscriptionJobStatus": "COMPLETED",
            "OutputLocationType": "SERVICE_BUCKET"
        },
        {
            "TranscriptionJobName": "job-1",
            "CreationTime": "2020-08-17T20:50:24.207000+00:00",
            "StartTime": "2020-08-17T20:50:24.230000+00:00",
            "CompletionTime": "2020-08-17T20:52:18.737000+00:00",
            "LanguageCode": "language-code",
            "TranscriptionJobStatus": "COMPLETED",
            "OutputLocationType": "SERVICE_BUCKET"
        },
        {
            "TranscriptionJobName": "sdk-test-job-4",
            "CreationTime": "2020-08-17T20:32:27.917000+00:00",
            "StartTime": "2020-08-17T20:32:27.956000+00:00",
            "CompletionTime": "2020-08-17T20:33:15.126000+00:00",
            "LanguageCode": "language-code",
            "TranscriptionJobStatus": "COMPLETED",
            "OutputLocationType": "SERVICE_BUCKET"
        },
        {
            "TranscriptionJobName": "Diarization-speak-id",
            "CreationTime": "2020-08-10T22:10:09.066000+00:00",
            "StartTime": "2020-08-10T22:10:09.116000+00:00",
            "CompletionTime": "2020-08-10T22:26:48.172000+00:00",
            "LanguageCode": "language-code",
            "TranscriptionJobStatus": "COMPLETED",
            "OutputLocationType": "SERVICE_BUCKET"
        },
        {
            "TranscriptionJobName": "your-transcription-job-name",
            "CreationTime": "2020-07-29T17:45:09.791000+00:00",
            "StartTime": "2020-07-29T17:45:09.826000+00:00",
            "CompletionTime": "2020-07-29T17:46:20.831000+00:00",
            "LanguageCode": "language-code",
            "TranscriptionJobStatus": "COMPLETED",
            "OutputLocationType": "SERVICE_BUCKET"
        }
    ]
}
```

For more information, see [Getting Started (AWS Command Line Interface)](https://docs.aws.amazon.com/transcribe/latest/dg/getting-started-cli.html) in the *Amazon Transcribe Developer Guide*.

## Output

Status -> (string)

Lists all transcription jobs that have the status specified in your request. Jobs are ordered by creation date, with the newest job first.

NextToken -> (string)

If `NextToken` is present in your response, it indicates that not all results are displayed. To view the next set of results, copy the string associated with the `NextToken` parameter in your results output, then run your request again including `NextToken` with the value of the copied string. Repeat as needed to view all your results.

TranscriptionJobSummaries -> (list)

Provides a summary of information about each result.

(structure)

Provides detailed information about a specific transcription job.

TranscriptionJobName -> (string)

The name of the transcription job. Job names are case sensitive and must be unique within an Amazon Web Services account.

CreationTime -> (timestamp)

The date and time the specified transcription job request was made.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:32:58.761000-07:00` represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.

StartTime -> (timestamp)

The date and time your transcription job began processing.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:32:58.789000-07:00` represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.

CompletionTime -> (timestamp)

The date and time the specified transcription job finished processing.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:33:13.922000-07:00` represents a transcription job that started processing at 12:33 PM UTC-7 on May 4, 2022.

LanguageCode -> (string)

The language code used to create your transcription.

TranscriptionJobStatus -> (string)

Provides the status of your transcription job.

If the status is `COMPLETED` , the job is finished and you can find the results at the location specified in `TranscriptFileUri` (or `RedactedTranscriptFileUri` , if you requested transcript redaction). If the status is `FAILED` , `FailureReason` provides details on why your transcription job failed.

FailureReason -> (string)

If `TranscriptionJobStatus` is `FAILED` , `FailureReason` contains information about why the transcription job failed. See also: [Common Errors](https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html) .

OutputLocationType -> (string)

Indicates where the specified transcription output is stored.

If the value is `CUSTOMER_BUCKET` , the location is the Amazon S3 bucket you specified using the `OutputBucketName` parameter in your request. If you also included `OutputKey` in your request, your output is located in the path you specified in your request.

If the value is `SERVICE_BUCKET` , the location is a service-managed Amazon S3 bucket. To access a transcript stored in a service-managed bucket, use the URI shown in the `TranscriptFileUri` or `RedactedTranscriptFileUri` field.

ContentRedaction -> (structure)

The content redaction settings of the transcription job.

RedactionType -> (string)

Specify the category of information you want to redact; `PII` (personally identifiable information) is the only valid value. You can use `PiiEntityTypes` to choose which types of PII you want to redact. If you do not include `PiiEntityTypes` in your request, all PII is redacted.

RedactionOutput -> (string)

Specify if you want only a redacted transcript, or if you want a redacted and an unredacted transcript.

When you choose `redacted` Amazon Transcribe creates only a redacted transcript.

When you choose `redacted_and_unredacted` Amazon Transcribe creates a redacted and an unredacted transcript (as two separate files).

PiiEntityTypes -> (list)

Specify which types of personally identifiable information (PII) you want to redact in your transcript. You can include as many types as youâd like, or you can select `ALL` . If you do not include `PiiEntityTypes` in your request, all PII is redacted.

(string)

ModelSettings -> (structure)

Provides the name of the custom language model that was included in the specified transcription job.

Only use `ModelSettings` with the `LanguageModelName` sub-parameter if youâre **not** using automatic language identification (). If using `LanguageIdSettings` in your request, this parameter contains a `LanguageModelName` sub-parameter.

LanguageModelName -> (string)

The name of the custom language model you want to use when processing your transcription job. Note that custom language model names are case sensitive.

The language of the specified custom language model must match the language code that you specify in your transcription request. If the languages do not match, the custom language model isnât applied. There are no errors or warnings associated with a language mismatch.

IdentifyLanguage -> (boolean)

Indicates whether automatic language identification was enabled (`TRUE` ) for the specified transcription job.

IdentifyMultipleLanguages -> (boolean)

Indicates whether automatic multi-language identification was enabled (`TRUE` ) for the specified transcription job.

IdentifiedLanguageScore -> (float)

The confidence score associated with the language identified in your media file.

Confidence scores are values between 0 and 1; a larger value indicates a higher probability that the identified language correctly matches the language spoken in your media.

LanguageCodes -> (list)

The language codes used to create your transcription job. This parameter is used with multi-language identification. For single-language identification, the singular version of this parameter, `LanguageCode` , is present.

(structure)

Provides information on the speech contained in a discreet utterance when multi-language identification is enabled in your request. This utterance represents a block of speech consisting of one language, preceded or followed by a block of speech in a different language.

LanguageCode -> (string)

Provides the language code for each language identified in your media.

DurationInSeconds -> (float)

Provides the total time, in seconds, each identified language is spoken in your media.

ToxicityDetection -> (list)

Indicates whether toxicity detection was enabled for the specified transcription job.

(structure)

Contains `ToxicityCategories` , which is a required parameter if you want to enable toxicity detection (`ToxicityDetection` ) in your transcription request.

ToxicityCategories -> (list)

If you include `ToxicityDetection` in your transcription request, you must also include `ToxicityCategories` . The only accepted value for this parameter is `ALL` .

(string)