# get-call-analytics-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-call-analytics-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-call-analytics-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transcribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/index.html#cli-aws-transcribe) ]

# get-call-analytics-job

## Description

Provides information about the specified Call Analytics job.

To view the jobâs status, refer to `CallAnalyticsJobStatus` . If the status is `COMPLETED` , the job is finished. You can find your completed transcript at the URI specified in `TranscriptFileUri` . If the status is `FAILED` , `FailureReason` provides details on why your transcription job failed.

If you enabled personally identifiable information (PII) redaction, the redacted transcript appears at the location specified in `RedactedTranscriptFileUri` .

If you chose to redact the audio in your media file, you can find your redacted media file at the location specified in `RedactedMediaFileUri` .

To get a list of your Call Analytics jobs, use the operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/GetCallAnalyticsJob)

## Synopsis

```
get-call-analytics-job
--call-analytics-job-name <value>
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

`--call-analytics-job-name` (string)

The name of the Call Analytics job you want information about. Job names are case sensitive.

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

CallAnalyticsJob -> (structure)

Provides detailed information about the specified Call Analytics job, including job status and, if applicable, failure reason.

CallAnalyticsJobName -> (string)

The name of the Call Analytics job. Job names are case sensitive and must be unique within an Amazon Web Services account.

CallAnalyticsJobStatus -> (string)

Provides the status of the specified Call Analytics job.

If the status is `COMPLETED` , the job is finished and you can find the results at the location specified in `TranscriptFileUri` (or `RedactedTranscriptFileUri` , if you requested transcript redaction). If the status is `FAILED` , `FailureReason` provides details on why your transcription job failed.

CallAnalyticsJobDetails -> (structure)

Provides detailed information about a call analytics job, including information about skipped analytics features.

Skipped -> (list)

Contains information about any skipped analytics features during the analysis of a call analytics job.

This array lists all the analytics features that were skipped, along with their corresponding reason code and message.

(structure)

Represents a skipped analytics feature during the analysis of a call analytics job.

The `Feature` field indicates the type of analytics feature that was skipped.

The `Message` field contains additional information or a message explaining why the analytics feature was skipped.

The `ReasonCode` field provides a code indicating the reason why the analytics feature was skipped.

Feature -> (string)

Indicates the type of analytics feature that was skipped during the analysis of a call analytics job.

ReasonCode -> (string)

Provides a code indicating the reason why a specific analytics feature was skipped during the analysis of a call analytics job.

Message -> (string)

Contains additional information or a message explaining why a specific analytics feature was skipped during the analysis of a call analytics job.

LanguageCode -> (string)

The language code used to create your Call Analytics job. For a list of supported languages and their associated language codes, refer to the [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) table.

If you do not know the language spoken in your media file, you can omit this field and let Amazon Transcribe automatically identify the language of your media. To improve the accuracy of language identification, you can include several language codes and Amazon Transcribe chooses the closest match for your transcription.

MediaSampleRateHertz -> (integer)

The sample rate, in hertz, of the audio track in your input media file.

MediaFormat -> (string)

The format of the input media file.

Media -> (structure)

Provides the Amazon S3 location of the media file you used in your Call Analytics request.

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

The date and time the specified Call Analytics job began processing.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:32:58.789000-07:00` represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.

CreationTime -> (timestamp)

The date and time the specified Call Analytics job request was made.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:32:58.761000-07:00` represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.

CompletionTime -> (timestamp)

The date and time the specified Call Analytics job finished processing.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:33:13.922000-07:00` represents a transcription job that started processing at 12:33 PM UTC-7 on May 4, 2022.

FailureReason -> (string)

If `CallAnalyticsJobStatus` is `FAILED` , `FailureReason` contains information about why the Call Analytics job request failed.

The `FailureReason` field contains one of the following values:

- `Unsupported media format` . The media format specified in `MediaFormat` isnât valid. Refer to refer to the `MediaFormat` parameter for a list of supported formats.
- `The media format provided does not match the detected media format` . The media format specified in `MediaFormat` doesnât match the format of the input file. Check the media format of your media file and correct the specified value.
- `Invalid sample rate for audio file` . The sample rate specified in `MediaSampleRateHertz` isnât valid. The sample rate must be between 8,000 and 48,000 hertz.
- `The sample rate provided does not match the detected sample rate` . The sample rate specified in `MediaSampleRateHertz` doesnât match the sample rate detected in your input media file. Check the sample rate of your media file and correct the specified value.
- `Invalid file size: file size too large` . The size of your media file is larger than what Amazon Transcribe can process. For more information, refer to [Service quotas](https://docs.aws.amazon.com/general/latest/gr/transcribe.html#limits-amazon-transcribe) .
- `Invalid number of channels: number of channels too large` . Your audio contains more channels than Amazon Transcribe is able to process. For more information, refer to [Service quotas](https://docs.aws.amazon.com/general/latest/gr/transcribe.html#limits-amazon-transcribe) .

DataAccessRoleArn -> (string)

The Amazon Resource Name (ARN) you included in your request.

IdentifiedLanguageScore -> (float)

The confidence score associated with the language identified in your media file.

Confidence scores are values between 0 and 1; a larger value indicates a higher probability that the identified language correctly matches the language spoken in your media.

Settings -> (structure)

Provides information on any additional settings that were included in your request. Additional settings include content redaction and language identification settings.

VocabularyName -> (string)

The name of the custom vocabulary you want to include in your Call Analytics transcription request. Custom vocabulary names are case sensitive.

VocabularyFilterName -> (string)

The name of the custom vocabulary filter you want to include in your Call Analytics transcription request. Custom vocabulary filter names are case sensitive.

Note that if you include `VocabularyFilterName` in your request, you must also include `VocabularyFilterMethod` .

VocabularyFilterMethod -> (string)

Specify how you want your custom vocabulary filter applied to your transcript.

To replace words with `***` , choose `mask` .

To delete words, choose `remove` .

To flag words without changing them, choose `tag` .

LanguageModelName -> (string)

The name of the custom language model you want to use when processing your Call Analytics job. Note that custom language model names are case sensitive.

The language of the specified custom language model must match the language code that you specify in your transcription request. If the languages do not match, the custom language model isnât applied. There are no errors or warnings associated with a language mismatch.

ContentRedaction -> (structure)

Makes it possible to redact or flag specified personally identifiable information (PII) in your transcript. If you use `ContentRedaction` , you must also include the sub-parameters: `RedactionOutput` and `RedactionType` . You can optionally include `PiiEntityTypes` to choose which types of PII you want to redact.

RedactionType -> (string)

Specify the category of information you want to redact; `PII` (personally identifiable information) is the only valid value. You can use `PiiEntityTypes` to choose which types of PII you want to redact. If you do not include `PiiEntityTypes` in your request, all PII is redacted.

RedactionOutput -> (string)

Specify if you want only a redacted transcript, or if you want a redacted and an unredacted transcript.

When you choose `redacted` Amazon Transcribe creates only a redacted transcript.

When you choose `redacted_and_unredacted` Amazon Transcribe creates a redacted and an unredacted transcript (as two separate files).

PiiEntityTypes -> (list)

Specify which types of personally identifiable information (PII) you want to redact in your transcript. You can include as many types as youâd like, or you can select `ALL` . If you do not include `PiiEntityTypes` in your request, all PII is redacted.

(string)

LanguageOptions -> (list)

You can specify two or more language codes that represent the languages you think may be present in your media. Including more than five is not recommended. If youâre unsure what languages are present, do not include this parameter.

Including language options can improve the accuracy of language identification.

For a list of languages supported with Call Analytics, refer to the [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) table.

To transcribe speech in Modern Standard Arabic (`ar-SA` ) in Amazon Web Services GovCloud (US) (US-West, us-gov-west-1), Amazon Web Services GovCloud (US) (US-East, us-gov-east-1), Canada (Calgary) ca-west-1 and Africa (Cape Town) af-south-1, your media file must be encoded at a sample rate of 16,000 Hz or higher.

(string)

LanguageIdSettings -> (map)

If using automatic language identification in your request and you want to apply a custom language model, a custom vocabulary, or a custom vocabulary filter, include `LanguageIdSettings` with the relevant sub-parameters (`VocabularyName` , `LanguageModelName` , and `VocabularyFilterName` ).

`LanguageIdSettings` supports two to five language codes. Each language code you include can have an associated custom language model, custom vocabulary, and custom vocabulary filter. The language codes that you specify must match the languages of the associated custom language models, custom vocabularies, and custom vocabulary filters.

Itâs recommended that you include `LanguageOptions` when using `LanguageIdSettings` to ensure that the correct language dialect is identified. For example, if you specify a custom vocabulary that is in `en-US` but Amazon Transcribe determines that the language spoken in your media is `en-AU` , your custom vocabulary *is not* applied to your transcription. If you include `LanguageOptions` and include `en-US` as the only English language dialect, your custom vocabulary *is* applied to your transcription.

If you want to include a custom language model, custom vocabulary, or custom vocabulary filter with your request but **do not** want to use automatic language identification, use instead the parameter with the `LanguageModelName` , `VocabularyName` , or `VocabularyFilterName` sub-parameters.

For a list of languages supported with Call Analytics, refer to [Supported languages and language-specific features](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) .

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

Summarization -> (structure)

Contains `GenerateAbstractiveSummary` , which is a required parameter if you want to enable Generative call summarization in your Call Analytics request.

GenerateAbstractiveSummary -> (boolean)

Enables Generative call summarization in your Call Analytics request

Generative call summarization provides a summary of the transcript including important components discussed in the conversation.

For more information, see [Enabling generative call summarization](https://docs.aws.amazon.com/transcribe/latest/dg/tca-enable-summarization.html) .

ChannelDefinitions -> (list)

Indicates which speaker is on which channel.

(structure)

Makes it possible to specify which speaker is on which channel. For example, if your agent is the first participant to speak, you would set `ChannelId` to `0` (to indicate the first channel) and `ParticipantRole` to `AGENT` (to indicate that itâs the agent speaking).

ChannelId -> (integer)

Specify the audio channel you want to define.

ParticipantRole -> (string)

Specify the speaker you want to define. Omitting this parameter is equivalent to specifying both participants.

Tags -> (list)

The tags, each in the form of a key:value pair, assigned to the specified call analytics job.

(structure)

Adds metadata, in the form of a key:value pair, to the specified resource.

For example, you could add the tag `Department:Sales` to a resource to indicate that it pertains to your organizationâs sales department. You can also use tags for tag-based access control.

To learn more about tagging, see [Tagging resources](https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html) .

Key -> (string)

The first part of a key:value pair that forms a tag associated with a given resource. For example, in the tag `Department:Sales` , the key is âDepartmentâ.

Value -> (string)

The second part of a key:value pair that forms a tag associated with a given resource. For example, in the tag `Department:Sales` , the value is âSalesâ.

Note that you can set the value of a tag to an empty string, but you canât set the value of a tag to null. Omitting the tag value is the same as using an empty string.