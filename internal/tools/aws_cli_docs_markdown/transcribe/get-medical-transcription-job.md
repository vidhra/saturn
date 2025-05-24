# get-medical-transcription-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-medical-transcription-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-medical-transcription-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transcribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/index.html#cli-aws-transcribe) ]

# get-medical-transcription-job

## Description

Provides information about the specified medical transcription job.

To view the status of the specified medical transcription job, check the `TranscriptionJobStatus` field. If the status is `COMPLETED` , the job is finished. You can find the results at the location specified in `TranscriptFileUri` . If the status is `FAILED` , `FailureReason` provides details on why your transcription job failed.

To get a list of your medical transcription jobs, use the operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/GetMedicalTranscriptionJob)

## Synopsis

```
get-medical-transcription-job
--medical-transcription-job-name <value>
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

`--medical-transcription-job-name` (string)

The name of the medical transcription job you want information about. Job names are case sensitive.

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

**To get information about a specific medical transcription job**

The following `get-medical-transcription-job` example gets information about a specific medical transcription job. To access the transcription results, use the TranscriptFileUri parameter. If youâve enabled additional features for the transcription job, you can see them in the Settings object. The Specialty parameter shows the medical specialty of the provider. The Type parameter indicates whether the speech in the transcription job is of a medical conversation, or a medical dictation.

```
aws transcribe get-medical-transcription-job \
    --medical-transcription-job-name vocabulary-dictation-medical-transcription-job
```

Output:

```
{
    "MedicalTranscriptionJob": {
        "MedicalTranscriptionJobName": "vocabulary-dictation-medical-transcription-job",
        "TranscriptionJobStatus": "COMPLETED",
        "LanguageCode": "en-US",
        "MediaSampleRateHertz": 48000,
        "MediaFormat": "mp4",
        "Media": {
            "MediaFileUri": "s3://Amazon-S3-Prefix/your-audio-file.file-extension"
        },
        "Transcript": {
            "TranscriptFileUri": "https://s3.Region.amazonaws.com/Amazon-S3-Prefix/vocabulary-dictation-medical-transcription-job.json"
        },
        "StartTime": "2020-09-21T21:17:27.045000+00:00",
        "CreationTime": "2020-09-21T21:17:27.016000+00:00",
        "CompletionTime": "2020-09-21T21:17:59.561000+00:00",
        "Settings": {
            "ChannelIdentification": false,
            "ShowAlternatives": false,
            "VocabularyName": "cli-medical-vocab-example"
        },
        "Specialty": "PRIMARYCARE",
        "Type": "DICTATION"
    }
}
```

For more information, see [Batch Transcription](https://docs.aws.amazon.com/transcribe/latest/dg/batch-med-transcription.html) in the *Amazon Transcribe Developer Guide*.

## Output

MedicalTranscriptionJob -> (structure)

Provides detailed information about the specified medical transcription job, including job status and, if applicable, failure reason.

MedicalTranscriptionJobName -> (string)

The name of the medical transcription job. Job names are case sensitive and must be unique within an Amazon Web Services account.

TranscriptionJobStatus -> (string)

Provides the status of the specified medical transcription job.

If the status is `COMPLETED` , the job is finished and you can find the results at the location specified in `TranscriptFileUri` . If the status is `FAILED` , `FailureReason` provides details on why your transcription job failed.

LanguageCode -> (string)

The language code used to create your medical transcription job. US English (`en-US` ) is the only supported language for medical transcriptions.

MediaSampleRateHertz -> (integer)

The sample rate, in hertz, of the audio track in your input media file.

MediaFormat -> (string)

The format of the input media file.

Media -> (structure)

Describes the Amazon S3 location of the media file you want to use in your request.

For information on supported media formats, refer to the `MediaFormat` parameter or the [Media formats](https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio) section in the Amazon S3 Developer Guide.

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

Note that this is the Amazon S3 location you specified in your request using the `OutputBucketName` parameter.

StartTime -> (timestamp)

The date and time the specified medical transcription job began processing.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:32:58.789000-07:00` represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.

CreationTime -> (timestamp)

The date and time the specified medical transcription job request was made.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:32:58.761000-07:00` represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.

CompletionTime -> (timestamp)

The date and time the specified medical transcription job finished processing.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:33:13.922000-07:00` represents a transcription job that started processing at 12:33 PM UTC-7 on May 4, 2022.

FailureReason -> (string)

If `TranscriptionJobStatus` is `FAILED` , `FailureReason` contains information about why the transcription job request failed.

The `FailureReason` field contains one of the following values:

- `Unsupported media format` . The media format specified in `MediaFormat` isnât valid. Refer to refer to the `MediaFormat` parameter for a list of supported formats.
- `The media format provided does not match the detected media format` . The media format specified in `MediaFormat` doesnât match the format of the input file. Check the media format of your media file and correct the specified value.
- `Invalid sample rate for audio file` . The sample rate specified in `MediaSampleRateHertz` isnât valid. The sample rate must be between 16,000 and 48,000 hertz.
- `The sample rate provided does not match the detected sample rate` . The sample rate specified in `MediaSampleRateHertz` doesnât match the sample rate detected in your input media file. Check the sample rate of your media file and correct the specified value.
- `Invalid file size: file size too large` . The size of your media file is larger than what Amazon Transcribe can process. For more information, refer to [Service quotas](https://docs.aws.amazon.com/general/latest/gr/transcribe.html#limits-amazon-transcribe) .
- `Invalid number of channels: number of channels too large` . Your audio contains more channels than Amazon Transcribe is able to process. For more information, refer to [Service quotas](https://docs.aws.amazon.com/general/latest/gr/transcribe.html#limits-amazon-transcribe) .

Settings -> (structure)

Provides information on any additional settings that were included in your request. Additional settings include channel identification, alternative transcriptions, speaker partitioning, custom vocabularies, and custom vocabulary filters.

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

If you have multi-channel audio and do not enable channel identification, your audio is transcribed in a continuous manner and your transcript does not separate the speech by channel.

For more information, see [Transcribing multi-channel audio](https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html) .

ShowAlternatives -> (boolean)

To include alternative transcriptions within your transcription output, include `ShowAlternatives` in your transcription request.

If you include `ShowAlternatives` , you must also include `MaxAlternatives` , which is the maximum number of alternative transcriptions you want Amazon Transcribe Medical to generate.

For more information, see [Alternative transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/how-alternatives.html) .

MaxAlternatives -> (integer)

Indicate the maximum number of alternative transcriptions you want Amazon Transcribe Medical to include in your transcript.

If you select a number greater than the number of alternative transcriptions generated by Amazon Transcribe Medical, only the actual number of alternative transcriptions are included.

If you include `MaxAlternatives` in your request, you must also include `ShowAlternatives` with a value of `true` .

For more information, see [Alternative transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/how-alternatives.html) .

VocabularyName -> (string)

The name of the custom vocabulary you want to use when processing your medical transcription job. Custom vocabulary names are case sensitive.

The language of the specified custom vocabulary must match the language code that you specify in your transcription request. If the languages do not match, the custom vocabulary isnât applied. There are no errors or warnings associated with a language mismatch. US English (`en-US` ) is the only valid language for Amazon Transcribe Medical.

ContentIdentificationType -> (string)

Indicates whether content identification was enabled for your transcription request.

Specialty -> (string)

Describes the medical specialty represented in your media.

Type -> (string)

Indicates whether the input media is a dictation or a conversation, as specified in the `StartMedicalTranscriptionJob` request.

Tags -> (list)

The tags, each in the form of a key:value pair, assigned to the specified medical transcription job.

(structure)

Adds metadata, in the form of a key:value pair, to the specified resource.

For example, you could add the tag `Department:Sales` to a resource to indicate that it pertains to your organizationâs sales department. You can also use tags for tag-based access control.

To learn more about tagging, see [Tagging resources](https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html) .

Key -> (string)

The first part of a key:value pair that forms a tag associated with a given resource. For example, in the tag `Department:Sales` , the key is âDepartmentâ.

Value -> (string)

The second part of a key:value pair that forms a tag associated with a given resource. For example, in the tag `Department:Sales` , the value is âSalesâ.

Note that you can set the value of a tag to an empty string, but you canât set the value of a tag to null. Omitting the tag value is the same as using an empty string.