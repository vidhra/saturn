# start-medical-transcription-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/start-medical-transcription-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/start-medical-transcription-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transcribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/index.html#cli-aws-transcribe) ]

# start-medical-transcription-job

## Description

Transcribes the audio from a medical dictation or conversation and applies any additional Request Parameters you choose to include in your request.

In addition to many standard transcription features, Amazon Transcribe Medical provides you with a robust medical vocabulary and, optionally, content identification, which adds flags to personal health information (PHI). To learn more about these features, refer to [How Amazon Transcribe Medical works](https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works-med.html) .

To make a `StartMedicalTranscriptionJob` request, you must first upload your media file into an Amazon S3 bucket; you can then specify the Amazon S3 location of the file using the `Media` parameter.

You must include the following parameters in your `StartMedicalTranscriptionJob` request:

- `region` : The Amazon Web Services Region where you are making your request. For a list of Amazon Web Services Regions supported with Amazon Transcribe, refer to [Amazon Transcribe endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/transcribe.html) .
- `MedicalTranscriptionJobName` : A custom name you create for your transcription job that is unique within your Amazon Web Services account.
- `Media` (`MediaFileUri` ): The Amazon S3 location of your media file.
- `LanguageCode` : This must be `en-US` .
- `OutputBucketName` : The Amazon S3 bucket where you want your transcript stored. If you want your output stored in a sub-folder of this bucket, you must also include `OutputKey` .
- `Specialty` : This must be `PRIMARYCARE` .
- `Type` : Choose whether your audio is a conversation or a dictation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/StartMedicalTranscriptionJob)

## Synopsis

```
start-medical-transcription-job
--medical-transcription-job-name <value>
--language-code <value>
[--media-sample-rate-hertz <value>]
[--media-format <value>]
--media <value>
--output-bucket-name <value>
[--output-key <value>]
[--output-encryption-kms-key-id <value>]
[--kms-encryption-context <value>]
[--settings <value>]
[--content-identification-type <value>]
--specialty <value>
--type <value>
[--tags <value>]
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

A unique name, chosen by you, for your medical transcription job. The name that you specify is also used as the default name of your transcription output file. If you want to specify a different name for your transcription output, use the `OutputKey` parameter.

This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account. If you try to create a new job with the same name as an existing job, you get a `ConflictException` error.

`--language-code` (string)

The language code that represents the language spoken in the input media file. US English (`en-US` ) is the only valid value for medical transcription jobs. Any other value you enter for language code results in a `BadRequestException` error.

Possible values:

- `af-ZA`
- `ar-AE`
- `ar-SA`
- `da-DK`
- `de-CH`
- `de-DE`
- `en-AB`
- `en-AU`
- `en-GB`
- `en-IE`
- `en-IN`
- `en-US`
- `en-WL`
- `es-ES`
- `es-US`
- `fa-IR`
- `fr-CA`
- `fr-FR`
- `he-IL`
- `hi-IN`
- `id-ID`
- `it-IT`
- `ja-JP`
- `ko-KR`
- `ms-MY`
- `nl-NL`
- `pt-BR`
- `pt-PT`
- `ru-RU`
- `ta-IN`
- `te-IN`
- `tr-TR`
- `zh-CN`
- `zh-TW`
- `th-TH`
- `en-ZA`
- `en-NZ`
- `vi-VN`
- `sv-SE`
- `ab-GE`
- `ast-ES`
- `az-AZ`
- `ba-RU`
- `be-BY`
- `bg-BG`
- `bn-IN`
- `bs-BA`
- `ca-ES`
- `ckb-IQ`
- `ckb-IR`
- `cs-CZ`
- `cy-WL`
- `el-GR`
- `et-ET`
- `eu-ES`
- `fi-FI`
- `gl-ES`
- `gu-IN`
- `ha-NG`
- `hr-HR`
- `hu-HU`
- `hy-AM`
- `is-IS`
- `ka-GE`
- `kab-DZ`
- `kk-KZ`
- `kn-IN`
- `ky-KG`
- `lg-IN`
- `lt-LT`
- `lv-LV`
- `mhr-RU`
- `mi-NZ`
- `mk-MK`
- `ml-IN`
- `mn-MN`
- `mr-IN`
- `mt-MT`
- `no-NO`
- `or-IN`
- `pa-IN`
- `pl-PL`
- `ps-AF`
- `ro-RO`
- `rw-RW`
- `si-LK`
- `sk-SK`
- `sl-SI`
- `so-SO`
- `sr-RS`
- `su-ID`
- `sw-BI`
- `sw-KE`
- `sw-RW`
- `sw-TZ`
- `sw-UG`
- `tl-PH`
- `tt-RU`
- `ug-CN`
- `uk-UA`
- `uz-UZ`
- `wo-SN`
- `zh-HK`
- `zu-ZA`

`--media-sample-rate-hertz` (integer)

The sample rate, in hertz, of the audio track in your input media file.

If you do not specify the media sample rate, Amazon Transcribe Medical determines it for you. If you specify the sample rate, it must match the rate detected by Amazon Transcribe Medical; if thereâs a mismatch between the value that you specify and the value detected, your job fails. Therefore, in most cases, itâs advised to omit `MediaSampleRateHertz` and let Amazon Transcribe Medical determine the sample rate.

`--media-format` (string)

Specify the format of your input media file.

Possible values:

- `mp3`
- `mp4`
- `wav`
- `flac`
- `ogg`
- `amr`
- `webm`
- `m4a`

`--media` (structure)

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

Shorthand Syntax:

```
MediaFileUri=string,RedactedMediaFileUri=string
```

JSON Syntax:

```
{
  "MediaFileUri": "string",
  "RedactedMediaFileUri": "string"
}
```

`--output-bucket-name` (string)

The name of the Amazon S3 bucket where you want your medical transcription output stored. Do not include the `S3://` prefix of the specified bucket.

If you want your output to go to a sub-folder of this bucket, specify it using the `OutputKey` parameter; `OutputBucketName` only accepts the name of a bucket.

For example, if you want your output stored in `S3://DOC-EXAMPLE-BUCKET` , set `OutputBucketName` to `DOC-EXAMPLE-BUCKET` . However, if you want your output stored in `S3://DOC-EXAMPLE-BUCKET/test-files/` , set `OutputBucketName` to `DOC-EXAMPLE-BUCKET` and `OutputKey` to `test-files/` .

Note that Amazon Transcribe must have permission to use the specified location. You can change Amazon S3 permissions using the [Amazon Web Services Management Console](https://console.aws.amazon.com/s3) . See also [Permissions Required for IAM User Roles](https://docs.aws.amazon.com/transcribe/latest/dg/security_iam_id-based-policy-examples.html#auth-role-iam-user) .

`--output-key` (string)

Use in combination with `OutputBucketName` to specify the output location of your transcript and, optionally, a unique name for your output file. The default name for your transcription output is the same as the name you specified for your medical transcription job (`MedicalTranscriptionJobName` ).

Here are some examples of how you can use `OutputKey` :

- If you specify âDOC-EXAMPLE-BUCKETâ as the `OutputBucketName` and âmy-transcript.jsonâ as the `OutputKey` , your transcription output path is `s3://DOC-EXAMPLE-BUCKET/my-transcript.json` .
- If you specify âmy-first-transcriptionâ as the `MedicalTranscriptionJobName` , âDOC-EXAMPLE-BUCKETâ as the `OutputBucketName` , and âmy-transcriptâ as the `OutputKey` , your transcription output path is `s3://DOC-EXAMPLE-BUCKET/my-transcript/my-first-transcription.json` .
- If you specify âDOC-EXAMPLE-BUCKETâ as the `OutputBucketName` and âtest-files/my-transcript.jsonâ as the `OutputKey` , your transcription output path is `s3://DOC-EXAMPLE-BUCKET/test-files/my-transcript.json` .
- If you specify âmy-first-transcriptionâ as the `MedicalTranscriptionJobName` , âDOC-EXAMPLE-BUCKETâ as the `OutputBucketName` , and âtest-files/my-transcriptâ as the `OutputKey` , your transcription output path is `s3://DOC-EXAMPLE-BUCKET/test-files/my-transcript/my-first-transcription.json` .

If you specify the name of an Amazon S3 bucket sub-folder that doesnât exist, one is created for you.

`--output-encryption-kms-key-id` (string)

The KMS key you want to use to encrypt your medical transcription output.

If using a key located in the **current** Amazon Web Services account, you can specify your KMS key in one of four ways:

- Use the KMS key ID itself. For example, `1234abcd-12ab-34cd-56ef-1234567890ab` .
- Use an alias for the KMS key ID. For example, `alias/ExampleAlias` .
- Use the Amazon Resource Name (ARN) for the KMS key ID. For example, `arn:aws:kms:region:account-ID:key/1234abcd-12ab-34cd-56ef-1234567890ab` .
- Use the ARN for the KMS key alias. For example, `arn:aws:kms:region:account-ID:alias/ExampleAlias` .

If using a key located in a **different** Amazon Web Services account than the current Amazon Web Services account, you can specify your KMS key in one of two ways:

- Use the ARN for the KMS key ID. For example, `arn:aws:kms:region:account-ID:key/1234abcd-12ab-34cd-56ef-1234567890ab` .
- Use the ARN for the KMS key alias. For example, `arn:aws:kms:region:account-ID:alias/ExampleAlias` .

If you do not specify an encryption key, your output is encrypted with the default Amazon S3 key (SSE-S3).

If you specify a KMS key to encrypt your output, you must also specify an output location using the `OutputLocation` parameter.

Note that the role making the request must have permission to use the specified KMS key.

`--kms-encryption-context` (map)

A map of plain text, non-secret key:value pairs, known as encryption context pairs, that provide an added layer of security for your data. For more information, see [KMS encryption context](https://docs.aws.amazon.com/transcribe/latest/dg/key-management.html#kms-context) and [Asymmetric keys in KMS](https://docs.aws.amazon.com/transcribe/latest/dg/symmetric-asymmetric.html) .

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--settings` (structure)

Specify additional optional settings in your request, including channel identification, alternative transcriptions, and speaker partitioning. You can use that to apply custom vocabularies to your transcription job.

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

Shorthand Syntax:

```
ShowSpeakerLabels=boolean,MaxSpeakerLabels=integer,ChannelIdentification=boolean,ShowAlternatives=boolean,MaxAlternatives=integer,VocabularyName=string
```

JSON Syntax:

```
{
  "ShowSpeakerLabels": true|false,
  "MaxSpeakerLabels": integer,
  "ChannelIdentification": true|false,
  "ShowAlternatives": true|false,
  "MaxAlternatives": integer,
  "VocabularyName": "string"
}
```

`--content-identification-type` (string)

Labels all personal health information (PHI) identified in your transcript. For more information, see [Identifying personal health information (PHI) in a transcription](https://docs.aws.amazon.com/transcribe/latest/dg/phi-id.html) .

Possible values:

- `PHI`

`--specialty` (string)

Specify the predominant medical specialty represented in your media. For batch transcriptions, `PRIMARYCARE` is the only valid value. If you require additional specialties, refer to .

Possible values:

- `PRIMARYCARE`

`--type` (string)

Specify whether your input media contains only one person (`DICTATION` ) or contains a conversation between two people (`CONVERSATION` ).

For example, `DICTATION` could be used for a medical professional wanting to transcribe voice memos; `CONVERSATION` could be used for transcribing the doctor-patient dialogue during the patientâs office visit.

Possible values:

- `CONVERSATION`
- `DICTATION`

`--tags` (list)

Adds one or more custom tags, each in the form of a key:value pair, to a new medical transcription job at the time you start this new job.

To learn more about using tags with Amazon Transcribe, refer to [Tagging resources](https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html) .

(structure)

Adds metadata, in the form of a key:value pair, to the specified resource.

For example, you could add the tag `Department:Sales` to a resource to indicate that it pertains to your organizationâs sales department. You can also use tags for tag-based access control.

To learn more about tagging, see [Tagging resources](https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html) .

Key -> (string)

The first part of a key:value pair that forms a tag associated with a given resource. For example, in the tag `Department:Sales` , the key is âDepartmentâ.

Value -> (string)

The second part of a key:value pair that forms a tag associated with a given resource. For example, in the tag `Department:Sales` , the value is âSalesâ.

Note that you can set the value of a tag to an empty string, but you canât set the value of a tag to null. Omitting the tag value is the same as using an empty string.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
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

**Example 1: To transcribe a medical dictation stored as an audio file**

The following `start-medical-transcription-job` example transcribes an audio file. You specify the location of the transcription output in the `OutputBucketName` parameter.

```
aws transcribe start-medical-transcription-job \
    --cli-input-json file://myfile.json
```

Contents of `myfile.json`:

```
{
    "MedicalTranscriptionJobName": "simple-dictation-medical-transcription-job",
    "LanguageCode": "language-code",
    "Specialty": "PRIMARYCARE",
    "Type": "DICTATION",
    "OutputBucketName":"amzn-s3-demo-bucket",
    "Media": {
        "MediaFileUri": "s3://amzn-s3-demo-bucket/your-audio-file.extension"
    }
}
```

Output:

```
{
    "MedicalTranscriptionJob": {
        "MedicalTranscriptionJobName": "simple-dictation-medical-transcription-job",
        "TranscriptionJobStatus": "IN_PROGRESS",
        "LanguageCode": "language-code",
        "Media": {
            "MediaFileUri": "s3://amzn-s3-demo-bucket/your-audio-file.extension"
        },
        "StartTime": "2020-09-20T00:35:22.256000+00:00",
        "CreationTime": "2020-09-20T00:35:22.218000+00:00",
        "Specialty": "PRIMARYCARE",
        "Type": "DICTATION"
    }
}
```

For more information, see [Batch Transcription Overview](https://docs.aws.amazon.com/transcribe/latest/dg/batch-med-transcription.html) in the *Amazon Transcribe Developer Guide*.

**Example 2: To transcribe a clinician-patient dialogue stored as an audio file**

The following `start-medical-transcription-job` example transcribes an audio file containing a clinician-patient dialogue. You specify the location of the transcription output in the OutputBucketName parameter.

```
aws transcribe start-medical-transcription-job \
    --cli-input-json file://mysecondfile.json
```

Contents of `mysecondfile.json`:

```
{
    "MedicalTranscriptionJobName": "simple-dictation-medical-transcription-job",
    "LanguageCode": "language-code",
    "Specialty": "PRIMARYCARE",
    "Type": "CONVERSATION",
    "OutputBucketName":"amzn-s3-demo-bucket",
    "Media": {
        "MediaFileUri": "s3://amzn-s3-demo-bucket/your-audio-file.extension"
    }
}
```

Output:

```
{
    "MedicalTranscriptionJob": {
        "MedicalTranscriptionJobName": "simple-conversation-medical-transcription-job",
        "TranscriptionJobStatus": "IN_PROGRESS",
        "LanguageCode": "language-code",
        "Media": {
            "MediaFileUri": "s3://amzn-s3-demo-bucket/your-audio-file.extension"
        },
        "StartTime": "2020-09-20T23:19:49.965000+00:00",
        "CreationTime": "2020-09-20T23:19:49.941000+00:00",
        "Specialty": "PRIMARYCARE",
        "Type": "CONVERSATION"
    }
}
```

For more information, see [Batch Transcription Overview](https://docs.aws.amazon.com/transcribe/latest/dg/batch-med-transcription.html) in the *Amazon Transcribe Developer Guide*.

**Example 3: To transcribe a multichannel audio file of a clinician-patient dialogue**

The following `start-medical-transcription-job` example transcribes the audio from each channel in the audio file and merges the separate transcriptions from each channel into a single transcription output. You specify the location of the transcription output in the `OutputBucketName` parameter.

```
aws transcribe start-medical-transcription-job \
    --cli-input-json file://mythirdfile.json
```

Contents of `mythirdfile.json`:

```
{
    "MedicalTranscriptionJobName": "multichannel-conversation-medical-transcription-job",
    "LanguageCode": "language-code",
    "Specialty": "PRIMARYCARE",
    "Type": "CONVERSATION",
    "OutputBucketName":"amzn-s3-demo-bucket",
        "Media": {
          "MediaFileUri": "s3://amzn-s3-demo-bucket/your-audio-file.extension"
        },
        "Settings":{
          "ChannelIdentification": true
        }
}
```

Output:

```
{
    "MedicalTranscriptionJob": {
        "MedicalTranscriptionJobName": "multichannel-conversation-medical-transcription-job",
        "TranscriptionJobStatus": "IN_PROGRESS",
        "LanguageCode": "language-code",
        "Media": {
            "MediaFileUri": "s3://amzn-s3-demo-bucket/your-audio-file.extension"
        },
        "StartTime": "2020-09-20T23:46:44.081000+00:00",
        "CreationTime": "2020-09-20T23:46:44.053000+00:00",
        "Settings": {
            "ChannelIdentification": true
        },
        "Specialty": "PRIMARYCARE",
        "Type": "CONVERSATION"
    }
}
```

For more information, see [Channel Identification](https://docs.aws.amazon.com/transcribe/latest/dg/how-channel-id-med.html) in the *Amazon Transcribe Developer Guide*.

**Example 4: To transcribe an audio file of a clinician-patient dialogue and identify the speakers in the transcription output**

The following `start-medical-transcription-job` example transcribes an audio file and labels the speech of each speaker in the transcription output. You specify the location of the transcription output in the `OutputBucketName` parameter.

```
aws transcribe start-medical-transcription-job \
    --cli-input-json file://myfourthfile.json
```

Contents of `myfourthfile.json`:

```
{
    "MedicalTranscriptionJobName": "speaker-id-conversation-medical-transcription-job",
    "LanguageCode": "language-code",
    "Specialty": "PRIMARYCARE",
    "Type": "CONVERSATION",
    "OutputBucketName":"amzn-s3-demo-bucket",
    "Media": {
        "MediaFileUri": "s3://amzn-s3-demo-bucket/your-audio-file.extension"
        },
    "Settings":{
        "ShowSpeakerLabels": true,
        "MaxSpeakerLabels": 2
        }
}
```

Output:

```
{
    "MedicalTranscriptionJob": {
        "MedicalTranscriptionJobName": "speaker-id-conversation-medical-transcription-job",
        "TranscriptionJobStatus": "IN_PROGRESS",
        "LanguageCode": "language-code",
        "Media": {
            "MediaFileUri": "s3://amzn-s3-demo-bucket/your-audio-file.extension"
        },
        "StartTime": "2020-09-21T18:43:37.265000+00:00",
        "CreationTime": "2020-09-21T18:43:37.157000+00:00",
        "Settings": {
            "ShowSpeakerLabels": true,
            "MaxSpeakerLabels": 2
        },
        "Specialty": "PRIMARYCARE",
        "Type": "CONVERSATION"
    }
}
```

For more information, see [Identifying Speakers](https://docs.aws.amazon.com/transcribe/latest/dg/diarization-med.html) in the *Amazon Transcribe Developer Guide*.

**Example 5: To transcribe a medical conversation stored as an audio file with up to two transcription alternatives**

The following `start-medical-transcription-job` example creates up to two alternative transcriptions from a single audio file. Every transcriptions has a level of confidence associated with it. By default, Amazon Transcribe returns the transcription with the highest confidence level. You can specify that Amazon Transcribe return additional transcriptions with lower confidence levels. You specify the location of the transcription output in the `OutputBucketName` parameter.

```
aws transcribe start-medical-transcription-job \
    --cli-input-json file://myfifthfile.json
```

Contents of `myfifthfile.json`:

```
{
    "MedicalTranscriptionJobName": "alternatives-conversation-medical-transcription-job",
    "LanguageCode": "language-code",
    "Specialty": "PRIMARYCARE",
    "Type": "CONVERSATION",
    "OutputBucketName":"amzn-s3-demo-bucket",
    "Media": {
        "MediaFileUri": "s3://amzn-s3-demo-bucket/your-audio-file.extension"
    },
    "Settings":{
        "ShowAlternatives": true,
        "MaxAlternatives": 2
    }
}
```

Output:

```
{
    "MedicalTranscriptionJob": {
        "MedicalTranscriptionJobName": "alternatives-conversation-medical-transcription-job",
        "TranscriptionJobStatus": "IN_PROGRESS",
        "LanguageCode": "language-code",
        "Media": {
            "MediaFileUri": "s3://amzn-s3-demo-bucket/your-audio-file.extension"
        },
        "StartTime": "2020-09-21T19:09:18.199000+00:00",
        "CreationTime": "2020-09-21T19:09:18.171000+00:00",
        "Settings": {
            "ShowAlternatives": true,
            "MaxAlternatives": 2
        },
        "Specialty": "PRIMARYCARE",
        "Type": "CONVERSATION"
    }
}
```

For more information, see [Alternative Transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/how-alternatives-med.html) in the *Amazon Transcribe Developer Guide*.

**Example 6: To transcribe an audio file of a medical dictation with up to two alternative transcriptions**

The following `start-medical-transcription-job` example transcribes an audio file and uses a vocabulary filter to mask any unwanted words. You specify the location of the transcription output in the OutputBucketName parameter.

```
aws transcribe start-medical-transcription-job \
    --cli-input-json file://mysixthfile.json
```

Contents of `mysixthfile.json`:

```
{
    "MedicalTranscriptionJobName": "alternatives-conversation-medical-transcription-job",
    "LanguageCode": "language-code",
    "Specialty": "PRIMARYCARE",
    "Type": "DICTATION",
    "OutputBucketName":"amzn-s3-demo-bucket",
    "Media": {
        "MediaFileUri": "s3://amzn-s3-demo-bucket/your-audio-file.extension"
    },
    "Settings":{
          "ShowAlternatives": true,
          "MaxAlternatives": 2
    }
}
```

Output:

```
{
    "MedicalTranscriptionJob": {
        "MedicalTranscriptionJobName": "alternatives-dictation-medical-transcription-job",
        "TranscriptionJobStatus": "IN_PROGRESS",
        "LanguageCode": "language-code",
        "Media": {
            "MediaFileUri": "s3://amzn-s3-demo-bucket/your-audio-file.extension"
        },
        "StartTime": "2020-09-21T21:01:14.592000+00:00",
        "CreationTime": "2020-09-21T21:01:14.569000+00:00",
        "Settings": {
            "ShowAlternatives": true,
            "MaxAlternatives": 2
        },
        "Specialty": "PRIMARYCARE",
        "Type": "DICTATION"
    }
}
```

For more information, see [Alternative Transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/how-alternatives-med.html) in the *Amazon Transcribe Developer Guide*.

**Example 7: To transcribe an audio file of a medical dictation with increased accuracy by using a custom vocabulary**

The following `start-medical-transcription-job` example transcribes an audio file and uses a medical custom vocabulary youâve previously created to increase the transcription accuracy. You specify the location of the transcription output in the `OutputBucketName` parameter.

```
aws transcribe start-transcription-job \
    --cli-input-json file://myseventhfile.json
```

Contents of `mysixthfile.json`:

```
{
    "MedicalTranscriptionJobName": "vocabulary-dictation-medical-transcription-job",
    "LanguageCode": "language-code",
    "Specialty": "PRIMARYCARE",
    "Type": "DICTATION",
    "OutputBucketName":"amzn-s3-demo-bucket",
    "Media": {
        "MediaFileUri": "s3://amzn-s3-demo-bucket/your-audio-file.extension"
    },
    "Settings":{
        "VocabularyName": "cli-medical-vocab-1"
    }
}
```

Output:

```
{
    "MedicalTranscriptionJob": {
        "MedicalTranscriptionJobName": "vocabulary-dictation-medical-transcription-job",
        "TranscriptionJobStatus": "IN_PROGRESS",
        "LanguageCode": "language-code",
        "Media": {
            "MediaFileUri": "s3://amzn-s3-demo-bucket/your-audio-file.extension"
        },
        "StartTime": "2020-09-21T21:17:27.045000+00:00",
        "CreationTime": "2020-09-21T21:17:27.016000+00:00",
        "Settings": {
            "VocabularyName": "cli-medical-vocab-1"
        },
        "Specialty": "PRIMARYCARE",
        "Type": "DICTATION"
    }
}
```

For more information, see [Medical Custom Vocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/how-vocabulary-med.html) in the *Amazon Transcribe Developer Guide*.

## Output

MedicalTranscriptionJob -> (structure)

Provides detailed information about the current medical transcription job, including job status and, if applicable, failure reason.

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