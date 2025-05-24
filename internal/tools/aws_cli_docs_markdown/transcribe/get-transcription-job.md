# get-transcription-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-transcription-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-transcription-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transcribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/index.html#cli-aws-transcribe) ]

# get-transcription-job

## Description

Provides information about the specified transcription job.

To view the status of the specified transcription job, check the `TranscriptionJobStatus` field. If the status is `COMPLETED` , the job is finished. You can find the results at the location specified in `TranscriptFileUri` . If the status is `FAILED` , `FailureReason` provides details on why your transcription job failed.

If you enabled content redaction, the redacted transcript can be found at the location specified in `RedactedTranscriptFileUri` .

To get a list of your transcription jobs, use the operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/GetTranscriptionJob)

## Synopsis

```
get-transcription-job
--transcription-job-name <value>
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

`--transcription-job-name` (string)

The name of the transcription job you want information about. Job names are case sensitive.

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

**To get information about a specific transcription job**

The following `get-transcription-job` example gets information about a specific transcription job. To access the transcription results, use the TranscriptFileUri parameter. Use the MediaFileUri parameter to see which audio file you transcribed with this job. You can use the Settings object to see the optional features youâve enabled in the transcription job.

```
aws transcribe get-transcription-job \
    --transcription-job-name your-transcription-job
```

Output:

```
{
    "TranscriptionJob": {
        "TranscriptionJobName": "your-transcription-job",
        "TranscriptionJobStatus": "COMPLETED",
        "LanguageCode": "language-code",
        "MediaSampleRateHertz": 48000,
        "MediaFormat": "mp4",
        "Media": {
            "MediaFileUri": "s3://amzn-s3-demo-bucket/your-audio-file.file-extension"
        },
        "Transcript": {
            "TranscriptFileUri": "https://Amazon-S3-file-location-of-transcription-output"
        },
        "StartTime": "2020-09-18T22:27:23.970000+00:00",
        "CreationTime": "2020-09-18T22:27:23.948000+00:00",
        "CompletionTime": "2020-09-18T22:28:21.197000+00:00",
        "Settings": {
            "ChannelIdentification": false,
            "ShowAlternatives": false
        },
        "IdentifyLanguage": true,
        "IdentifiedLanguageScore": 0.8672199249267578
    }
}
```

For more information, see [Getting Started (AWS Command Line Interface)](https://docs.aws.amazon.com/transcribe/latest/dg/getting-started-cli.html) in the *Amazon Transcribe Developer Guide*.

## Output

TranscriptionJob -> (structure)

Provides detailed information about the specified transcription job, including job status and, if applicable, failure reason.

TranscriptionJobName -> (string)

The name of the transcription job. Job names are case sensitive and must be unique within an Amazon Web Services account.

TranscriptionJobStatus -> (string)

Provides the status of the specified transcription job.

If the status is `COMPLETED` , the job is finished and you can find the results at the location specified in `TranscriptFileUri` (or `RedactedTranscriptFileUri` , if you requested transcript redaction). If the status is `FAILED` , `FailureReason` provides details on why your transcription job failed.

LanguageCode -> (string)

The language code used to create your transcription job. This parameter is used with single-language identification. For multi-language identification requests, refer to the plural version of this parameter, `LanguageCodes` .

MediaSampleRateHertz -> (integer)

The sample rate, in hertz, of the audio track in your input media file.

MediaFormat -> (string)

The format of the input media file.

Media -> (structure)

Provides the Amazon S3 location of the media file you used in your request.

MediaFileUri -> (string)

The Amazon S3 location of the media file you want to transcribe. For example:

- `s3://DOC-EXAMPLE-BUCKET/my-media-file.flac`
- `s3://DOC-EXAMPLE-BUCKET/media-files/my-media-file.flac`

Note that the Amazon S3 bucket that contains your input media must be located in the same Amazon Web Services Region where youâre making your transcription request.

RedactedMediaFileUri -> (string)

The Amazon S3 location of the media file you want to redact. For example:

- `s3://DOC-EXAMPLE-BUCKET/my-media-file.flac`
- `s3://DOC-EXAMPLE-BUCKET/media-files/my-media-file.flac`

Note that the Amazon S3 bucket that contains your input media must be located in the same Amazon Web Services Region where youâre making your transcription request.

### Warning

`RedactedMediaFileUri` produces a redacted audio file in addition to a redacted transcript. It is only supported for Call Analytics (`StartCallAnalyticsJob` ) transcription requests.

Transcript -> (structure)

Provides you with the Amazon S3 URI you can use to access your transcript.

TranscriptFileUri -> (string)

The Amazon S3 location of your transcript. You can use this URI to access or download your transcript.

If you included `OutputBucketName` in your transcription job request, this is the URI of that bucket. If you also included `OutputKey` in your request, your output is located in the path you specified in your request.

If you didnât include `OutputBucketName` in your transcription job request, your transcript is stored in a service-managed bucket, and `TranscriptFileUri` provides you with a temporary URI you can use for secure access to your transcript.

### Note

Temporary URIs for service-managed Amazon S3 buckets are only valid for 15 minutes. If you get an `AccesDenied` error, you can get a new temporary URI by running a `GetTranscriptionJob` or `ListTranscriptionJob` request.

RedactedTranscriptFileUri -> (string)

The Amazon S3 location of your redacted transcript. You can use this URI to access or download your transcript.

If you included `OutputBucketName` in your transcription job request, this is the URI of that bucket. If you also included `OutputKey` in your request, your output is located in the path you specified in your request.

If you didnât include `OutputBucketName` in your transcription job request, your transcript is stored in a service-managed bucket, and `RedactedTranscriptFileUri` provides you with a temporary URI you can use for secure access to your transcript.

### Note

Temporary URIs for service-managed Amazon S3 buckets are only valid for 15 minutes. If you get an `AccesDenied` error, you can get a new temporary URI by running a `GetTranscriptionJob` or `ListTranscriptionJob` request.

StartTime -> (timestamp)

The date and time the specified transcription job began processing.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:32:58.789000-07:00` represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.

CreationTime -> (timestamp)

The date and time the specified transcription job request was made.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:32:58.761000-07:00` represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.

CompletionTime -> (timestamp)

The date and time the specified transcription job finished processing.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:33:13.922000-07:00` represents a transcription job that started processing at 12:33 PM UTC-7 on May 4, 2022.

FailureReason -> (string)

If `TranscriptionJobStatus` is `FAILED` , `FailureReason` contains information about why the transcription job request failed.

The `FailureReason` field contains one of the following values:

- `Unsupported media format` . The media format specified in `MediaFormat` isnât valid. Refer to refer to the `MediaFormat` parameter for a list of supported formats.
- `The media format provided does not match the detected media format` . The media format specified in `MediaFormat` doesnât match the format of the input file. Check the media format of your media file and correct the specified value.
- `Invalid sample rate for audio file` . The sample rate specified in `MediaSampleRateHertz` isnât valid. The sample rate must be between 8,000 and 48,000 hertz.
- `The sample rate provided does not match the detected sample rate` . The sample rate specified in `MediaSampleRateHertz` doesnât match the sample rate detected in your input media file. Check the sample rate of your media file and correct the specified value.
- `Invalid file size: file size too large` . The size of your media file is larger than what Amazon Transcribe can process. For more information, refer to [Service quotas](https://docs.aws.amazon.com/general/latest/gr/transcribe.html#limits-amazon-transcribe) .
- `Invalid number of channels: number of channels too large` . Your audio contains more channels than Amazon Transcribe is able to process. For more information, refer to [Service quotas](https://docs.aws.amazon.com/general/latest/gr/transcribe.html#limits-amazon-transcribe) .

Settings -> (structure)

Provides information on any additional settings that were included in your request. Additional settings include channel identification, alternative transcriptions, speaker partitioning, custom vocabularies, and custom vocabulary filters.

VocabularyName -> (string)

The name of the custom vocabulary you want to use in your transcription job request. This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account.

ShowSpeakerLabels -> (boolean)

Enables speaker partitioning (diarization) in your transcription output. Speaker partitioning labels the speech from individual speakers in your media file.

If you enable `ShowSpeakerLabels` in your request, you must also include `MaxSpeakerLabels` .

For more information, see [Partitioning speakers (diarization)](https://docs.aws.amazon.com/transcribe/latest/dg/diarization.html) .

MaxSpeakerLabels -> (integer)

Specify the maximum number of speakers you want to partition in your media.

Note that if your media contains more speakers than the specified number, multiple speakers are treated as a single speaker.

If you specify the `MaxSpeakerLabels` field, you must set the `ShowSpeakerLabels` field to true.

ChannelIdentification -> (boolean)

Enables channel identification in multi-channel audio.

Channel identification transcribes the audio on each channel independently, then appends the output for each channel into one transcript.

For more information, see [Transcribing multi-channel audio](https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html) .

ShowAlternatives -> (boolean)

To include alternative transcriptions within your transcription output, include `ShowAlternatives` in your transcription request.

If you have multi-channel audio and do not enable channel identification, your audio is transcribed in a continuous manner and your transcript does not separate the speech by channel.

If you include `ShowAlternatives` , you must also include `MaxAlternatives` , which is the maximum number of alternative transcriptions you want Amazon Transcribe to generate.

For more information, see [Alternative transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/how-alternatives.html) .

MaxAlternatives -> (integer)

Indicate the maximum number of alternative transcriptions you want Amazon Transcribe to include in your transcript.

If you select a number greater than the number of alternative transcriptions generated by Amazon Transcribe, only the actual number of alternative transcriptions are included.

If you include `MaxAlternatives` in your request, you must also include `ShowAlternatives` with a value of `true` .

For more information, see [Alternative transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/how-alternatives.html) .

VocabularyFilterName -> (string)

The name of the custom vocabulary filter you want to use in your transcription job request. This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account.

Note that if you include `VocabularyFilterName` in your request, you must also include `VocabularyFilterMethod` .

VocabularyFilterMethod -> (string)

Specify how you want your custom vocabulary filter applied to your transcript.

To replace words with `***` , choose `mask` .

To delete words, choose `remove` .

To flag words without changing them, choose `tag` .

ModelSettings -> (structure)

Provides information on the custom language model you included in your request.

LanguageModelName -> (string)

The name of the custom language model you want to use when processing your transcription job. Note that custom language model names are case sensitive.

The language of the specified custom language model must match the language code that you specify in your transcription request. If the languages do not match, the custom language model isnât applied. There are no errors or warnings associated with a language mismatch.

JobExecutionSettings -> (structure)

Provides information about how your transcription job was processed. This parameter shows if your request was queued and what data access role was used.

AllowDeferredExecution -> (boolean)

Makes it possible to enable job queuing when your concurrent request limit is exceeded. When `AllowDeferredExecution` is set to `true` , transcription job requests are placed in a queue until the number of jobs falls below the concurrent request limit. If `AllowDeferredExecution` is set to `false` and the number of transcription job requests exceed the concurrent request limit, you get a `LimitExceededException` error.

If you include `AllowDeferredExecution` in your request, you must also include `DataAccessRoleArn` .

DataAccessRoleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files. If the role that you specify doesnât have the appropriate permissions to access the specified Amazon S3 location, your request fails.

IAM role ARNs have the format `arn:partition:iam::account:role/role-name-with-path` . For example: `arn:aws:iam::111122223333:role/Admin` . For more information, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns) .

Note that if you include `DataAccessRoleArn` in your request, you must also include `AllowDeferredExecution` .

ContentRedaction -> (structure)

Indicates whether redaction was enabled in your transcript.

RedactionType -> (string)

Specify the category of information you want to redact; `PII` (personally identifiable information) is the only valid value. You can use `PiiEntityTypes` to choose which types of PII you want to redact. If you do not include `PiiEntityTypes` in your request, all PII is redacted.

RedactionOutput -> (string)

Specify if you want only a redacted transcript, or if you want a redacted and an unredacted transcript.

When you choose `redacted` Amazon Transcribe creates only a redacted transcript.

When you choose `redacted_and_unredacted` Amazon Transcribe creates a redacted and an unredacted transcript (as two separate files).

PiiEntityTypes -> (list)

Specify which types of personally identifiable information (PII) you want to redact in your transcript. You can include as many types as youâd like, or you can select `ALL` . If you do not include `PiiEntityTypes` in your request, all PII is redacted.

(string)

IdentifyLanguage -> (boolean)

Indicates whether automatic language identification was enabled (`TRUE` ) for the specified transcription job.

IdentifyMultipleLanguages -> (boolean)

Indicates whether automatic multi-language identification was enabled (`TRUE` ) for the specified transcription job.

LanguageOptions -> (list)

Provides the language codes you specified in your request.

(string)

IdentifiedLanguageScore -> (float)

The confidence score associated with the language identified in your media file.

Confidence scores are values between 0 and 1; a larger value indicates a higher probability that the identified language correctly matches the language spoken in your media.

LanguageCodes -> (list)

The language codes used to create your transcription job. This parameter is used with multi-language identification. For single-language identification requests, refer to the singular version of this parameter, `LanguageCode` .

(structure)

Provides information on the speech contained in a discreet utterance when multi-language identification is enabled in your request. This utterance represents a block of speech consisting of one language, preceded or followed by a block of speech in a different language.

LanguageCode -> (string)

Provides the language code for each language identified in your media.

DurationInSeconds -> (float)

Provides the total time, in seconds, each identified language is spoken in your media.

Tags -> (list)

The tags, each in the form of a key:value pair, assigned to the specified transcription job.

(structure)

Adds metadata, in the form of a key:value pair, to the specified resource.

For example, you could add the tag `Department:Sales` to a resource to indicate that it pertains to your organizationâs sales department. You can also use tags for tag-based access control.

To learn more about tagging, see [Tagging resources](https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html) .

Key -> (string)

The first part of a key:value pair that forms a tag associated with a given resource. For example, in the tag `Department:Sales` , the key is âDepartmentâ.

Value -> (string)

The second part of a key:value pair that forms a tag associated with a given resource. For example, in the tag `Department:Sales` , the value is âSalesâ.

Note that you can set the value of a tag to an empty string, but you canât set the value of a tag to null. Omitting the tag value is the same as using an empty string.

Subtitles -> (structure)

Indicates whether subtitles were generated with your transcription.

Formats -> (list)

Provides the format of your subtitle files. If your request included both WebVTT (`vtt` ) and SubRip (`srt` ) formats, both formats are shown.

(string)

SubtitleFileUris -> (list)

The Amazon S3 location of your transcript. You can use this URI to access or download your subtitle file. Your subtitle file is stored in the same location as your transcript. If you specified both WebVTT and SubRip subtitle formats, two URIs are provided.

If you included `OutputBucketName` in your transcription job request, this is the URI of that bucket. If you also included `OutputKey` in your request, your output is located in the path you specified in your request.

If you didnât include `OutputBucketName` in your transcription job request, your subtitle file is stored in a service-managed bucket, and `TranscriptFileUri` provides you with a temporary URI you can use for secure access to your subtitle file.

### Note

Temporary URIs for service-managed Amazon S3 buckets are only valid for 15 minutes. If you get an `AccesDenied` error, you can get a new temporary URI by running a `GetTranscriptionJob` or `ListTranscriptionJob` request.

(string)

OutputStartIndex -> (integer)

Provides the start index value for your subtitle files. If you did not specify a value in your request, the default value of `0` is used.

LanguageIdSettings -> (map)

Provides the name and language of all custom language models, custom vocabularies, and custom vocabulary filters that you included in your request.

key -> (string)

value -> (structure)

If using automatic language identification in your request and you want to apply a custom language model, a custom vocabulary, or a custom vocabulary filter, include `LanguageIdSettings` with the relevant sub-parameters (`VocabularyName` , `LanguageModelName` , and `VocabularyFilterName` ). Note that multi-language identification (`IdentifyMultipleLanguages` ) doesnât support custom language models.

`LanguageIdSettings` supports two to five language codes. Each language code you include can have an associated custom language model, custom vocabulary, and custom vocabulary filter. The language codes that you specify must match the languages of the associated custom language models, custom vocabularies, and custom vocabulary filters.

Itâs recommended that you include `LanguageOptions` when using `LanguageIdSettings` to ensure that the correct language dialect is identified. For example, if you specify a custom vocabulary that is in `en-US` but Amazon Transcribe determines that the language spoken in your media is `en-AU` , your custom vocabulary *is not* applied to your transcription. If you include `LanguageOptions` and include `en-US` as the only English language dialect, your custom vocabulary *is* applied to your transcription.

If you want to include a custom language model with your request but **do not** want to use automatic language identification, use instead the parameter with the `LanguageModelName` sub-parameter. If you want to include a custom vocabulary or a custom vocabulary filter (or both) with your request but **do not** want to use automatic language identification, use instead the parameter with the `VocabularyName` or `VocabularyFilterName` (or both) sub-parameter.

VocabularyName -> (string)

The name of the custom vocabulary you want to use when processing your transcription job. Custom vocabulary names are case sensitive.

The language of the specified custom vocabulary must match the language code that you specify in your transcription request. If the languages do not match, the custom vocabulary isnât applied. There are no errors or warnings associated with a language mismatch.

VocabularyFilterName -> (string)

The name of the custom vocabulary filter you want to use when processing your transcription job. Custom vocabulary filter names are case sensitive.

The language of the specified custom vocabulary filter must match the language code that you specify in your transcription request. If the languages do not match, the custom vocabulary filter isnât applied. There are no errors or warnings associated with a language mismatch.

Note that if you include `VocabularyFilterName` in your request, you must also include `VocabularyFilterMethod` .

LanguageModelName -> (string)

The name of the custom language model you want to use when processing your transcription job. Note that custom language model names are case sensitive.

The language of the specified custom language model must match the language code that you specify in your transcription request. If the languages do not match, the custom language model isnât applied. There are no errors or warnings associated with a language mismatch.

ToxicityDetection -> (list)

Provides information about the toxicity detection settings applied to your transcription.

(structure)

Contains `ToxicityCategories` , which is a required parameter if you want to enable toxicity detection (`ToxicityDetection` ) in your transcription request.

ToxicityCategories -> (list)

If you include `ToxicityDetection` in your transcription request, you must also include `ToxicityCategories` . The only accepted value for this parameter is `ALL` .

(string)