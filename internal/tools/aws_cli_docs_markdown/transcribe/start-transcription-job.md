# start-transcription-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/start-transcription-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/start-transcription-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transcribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/index.html#cli-aws-transcribe) ]

# start-transcription-job

## Description

Transcribes the audio from a media file and applies any additional Request Parameters you choose to include in your request.

To make a `StartTranscriptionJob` request, you must first upload your media file into an Amazon S3 bucket; you can then specify the Amazon S3 location of the file using the `Media` parameter.

You must include the following parameters in your `StartTranscriptionJob` request:

- `region` : The Amazon Web Services Region where you are making your request. For a list of Amazon Web Services Regions supported with Amazon Transcribe, refer to [Amazon Transcribe endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/transcribe.html) .
- `TranscriptionJobName` : A custom name you create for your transcription job that is unique within your Amazon Web Services account.
- `Media` (`MediaFileUri` ): The Amazon S3 location of your media file.
- One of `LanguageCode` , `IdentifyLanguage` , or `IdentifyMultipleLanguages` : If you know the language of your media file, specify it using the `LanguageCode` parameter; you can find all valid language codes in the [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) table. If you do not know the languages spoken in your media, use either `IdentifyLanguage` or `IdentifyMultipleLanguages` and let Amazon Transcribe identify the languages for you.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/StartTranscriptionJob)

## Synopsis

```
start-transcription-job
--transcription-job-name <value>
[--language-code <value>]
[--media-sample-rate-hertz <value>]
[--media-format <value>]
--media <value>
[--output-bucket-name <value>]
[--output-key <value>]
[--output-encryption-kms-key-id <value>]
[--kms-encryption-context <value>]
[--settings <value>]
[--model-settings <value>]
[--job-execution-settings <value>]
[--content-redaction <value>]
[--identify-language | --no-identify-language]
[--identify-multiple-languages | --no-identify-multiple-languages]
[--language-options <value>]
[--subtitles <value>]
[--tags <value>]
[--language-id-settings <value>]
[--toxicity-detection <value>]
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

A unique name, chosen by you, for your transcription job. The name that you specify is also used as the default name of your transcription output file. If you want to specify a different name for your transcription output, use the `OutputKey` parameter.

This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account. If you try to create a new job with the same name as an existing job, you get a `ConflictException` error.

`--language-code` (string)

The language code that represents the language spoken in the input media file.

If youâre unsure of the language spoken in your media file, consider using `IdentifyLanguage` or `IdentifyMultipleLanguages` to enable automatic language identification.

Note that you must include one of `LanguageCode` , `IdentifyLanguage` , or `IdentifyMultipleLanguages` in your request. If you include more than one of these parameters, your transcription job fails.

For a list of supported languages and their associated language codes, refer to the [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) table.

### Note

To transcribe speech in Modern Standard Arabic (`ar-SA` ) in Amazon Web Services GovCloud (US) (US-West, us-gov-west-1), Amazon Web Services GovCloud (US) (US-East, us-gov-east-1), Canada (Calgary, ca-west-1) and Africa (Cape Town, af-south-1), your media file must be encoded at a sample rate of 16,000 Hz or higher.

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

If you do not specify the media sample rate, Amazon Transcribe determines it for you. If you specify the sample rate, it must match the rate detected by Amazon Transcribe. If thereâs a mismatch between the value that you specify and the value detected, your job fails. In most cases, you can omit `MediaSampleRateHertz` and let Amazon Transcribe determine the sample rate.

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

The name of the Amazon S3 bucket where you want your transcription output stored. Do not include the `S3://` prefix of the specified bucket.

If you want your output to go to a sub-folder of this bucket, specify it using the `OutputKey` parameter; `OutputBucketName` only accepts the name of a bucket.

For example, if you want your output stored in `S3://DOC-EXAMPLE-BUCKET` , set `OutputBucketName` to `DOC-EXAMPLE-BUCKET` . However, if you want your output stored in `S3://DOC-EXAMPLE-BUCKET/test-files/` , set `OutputBucketName` to `DOC-EXAMPLE-BUCKET` and `OutputKey` to `test-files/` .

Note that Amazon Transcribe must have permission to use the specified location. You can change Amazon S3 permissions using the [Amazon Web Services Management Console](https://console.aws.amazon.com/s3) . See also [Permissions Required for IAM User Roles](https://docs.aws.amazon.com/transcribe/latest/dg/security_iam_id-based-policy-examples.html#auth-role-iam-user) .

If you do not specify `OutputBucketName` , your transcript is placed in a service-managed Amazon S3 bucket and you are provided with a URI to access your transcript.

`--output-key` (string)

Use in combination with `OutputBucketName` to specify the output location of your transcript and, optionally, a unique name for your output file. The default name for your transcription output is the same as the name you specified for your transcription job (`TranscriptionJobName` ).

Here are some examples of how you can use `OutputKey` :

- If you specify âDOC-EXAMPLE-BUCKETâ as the `OutputBucketName` and âmy-transcript.jsonâ as the `OutputKey` , your transcription output path is `s3://DOC-EXAMPLE-BUCKET/my-transcript.json` .
- If you specify âmy-first-transcriptionâ as the `TranscriptionJobName` , âDOC-EXAMPLE-BUCKETâ as the `OutputBucketName` , and âmy-transcriptâ as the `OutputKey` , your transcription output path is `s3://DOC-EXAMPLE-BUCKET/my-transcript/my-first-transcription.json` .
- If you specify âDOC-EXAMPLE-BUCKETâ as the `OutputBucketName` and âtest-files/my-transcript.jsonâ as the `OutputKey` , your transcription output path is `s3://DOC-EXAMPLE-BUCKET/test-files/my-transcript.json` .
- If you specify âmy-first-transcriptionâ as the `TranscriptionJobName` , âDOC-EXAMPLE-BUCKETâ as the `OutputBucketName` , and âtest-files/my-transcriptâ as the `OutputKey` , your transcription output path is `s3://DOC-EXAMPLE-BUCKET/test-files/my-transcript/my-first-transcription.json` .

If you specify the name of an Amazon S3 bucket sub-folder that doesnât exist, one is created for you.

`--output-encryption-kms-key-id` (string)

The KMS key you want to use to encrypt your transcription output.

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

Specify additional optional settings in your request, including channel identification, alternative transcriptions, speaker partitioning. You can use that to apply custom vocabularies and vocabulary filters.

If you want to include a custom vocabulary or a custom vocabulary filter (or both) with your request but **do not** want to use automatic language identification, use `Settings` with the `VocabularyName` or `VocabularyFilterName` (or both) sub-parameter.

If youâre using automatic language identification with your request and want to include a custom language model, a custom vocabulary, or a custom vocabulary filter, use instead the parameter with the `LanguageModelName` , `VocabularyName` or `VocabularyFilterName` sub-parameters.

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

Shorthand Syntax:

```
VocabularyName=string,ShowSpeakerLabels=boolean,MaxSpeakerLabels=integer,ChannelIdentification=boolean,ShowAlternatives=boolean,MaxAlternatives=integer,VocabularyFilterName=string,VocabularyFilterMethod=string
```

JSON Syntax:

```
{
  "VocabularyName": "string",
  "ShowSpeakerLabels": true|false,
  "MaxSpeakerLabels": integer,
  "ChannelIdentification": true|false,
  "ShowAlternatives": true|false,
  "MaxAlternatives": integer,
  "VocabularyFilterName": "string",
  "VocabularyFilterMethod": "remove"|"mask"|"tag"
}
```

`--model-settings` (structure)

Specify the custom language model you want to include with your transcription job. If you include `ModelSettings` in your request, you must include the `LanguageModelName` sub-parameter.

For more information, see [Custom language models](https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html) .

LanguageModelName -> (string)

The name of the custom language model you want to use when processing your transcription job. Note that custom language model names are case sensitive.

The language of the specified custom language model must match the language code that you specify in your transcription request. If the languages do not match, the custom language model isnât applied. There are no errors or warnings associated with a language mismatch.

Shorthand Syntax:

```
LanguageModelName=string
```

JSON Syntax:

```
{
  "LanguageModelName": "string"
}
```

`--job-execution-settings` (structure)

Makes it possible to control how your transcription job is processed. Currently, the only `JobExecutionSettings` modification you can choose is enabling job queueing using the `AllowDeferredExecution` sub-parameter.

If you include `JobExecutionSettings` in your request, you must also include the sub-parameters: `AllowDeferredExecution` and `DataAccessRoleArn` .

AllowDeferredExecution -> (boolean)

Makes it possible to enable job queuing when your concurrent request limit is exceeded. When `AllowDeferredExecution` is set to `true` , transcription job requests are placed in a queue until the number of jobs falls below the concurrent request limit. If `AllowDeferredExecution` is set to `false` and the number of transcription job requests exceed the concurrent request limit, you get a `LimitExceededException` error.

If you include `AllowDeferredExecution` in your request, you must also include `DataAccessRoleArn` .

DataAccessRoleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files. If the role that you specify doesnât have the appropriate permissions to access the specified Amazon S3 location, your request fails.

IAM role ARNs have the format `arn:partition:iam::account:role/role-name-with-path` . For example: `arn:aws:iam::111122223333:role/Admin` . For more information, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns) .

Note that if you include `DataAccessRoleArn` in your request, you must also include `AllowDeferredExecution` .

Shorthand Syntax:

```
AllowDeferredExecution=boolean,DataAccessRoleArn=string
```

JSON Syntax:

```
{
  "AllowDeferredExecution": true|false,
  "DataAccessRoleArn": "string"
}
```

`--content-redaction` (structure)

Makes it possible to redact or flag specified personally identifiable information (PII) in your transcript. If you use `ContentRedaction` , you must also include the sub-parameters: `RedactionOutput` and `RedactionType` . You can optionally include `PiiEntityTypes` to choose which types of PII you want to redact. If you do not include `PiiEntityTypes` in your request, all PII is redacted.

RedactionType -> (string)

Specify the category of information you want to redact; `PII` (personally identifiable information) is the only valid value. You can use `PiiEntityTypes` to choose which types of PII you want to redact. If you do not include `PiiEntityTypes` in your request, all PII is redacted.

RedactionOutput -> (string)

Specify if you want only a redacted transcript, or if you want a redacted and an unredacted transcript.

When you choose `redacted` Amazon Transcribe creates only a redacted transcript.

When you choose `redacted_and_unredacted` Amazon Transcribe creates a redacted and an unredacted transcript (as two separate files).

PiiEntityTypes -> (list)

Specify which types of personally identifiable information (PII) you want to redact in your transcript. You can include as many types as youâd like, or you can select `ALL` . If you do not include `PiiEntityTypes` in your request, all PII is redacted.

(string)

Shorthand Syntax:

```
RedactionType=string,RedactionOutput=string,PiiEntityTypes=string,string
```

JSON Syntax:

```
{
  "RedactionType": "PII",
  "RedactionOutput": "redacted"|"redacted_and_unredacted",
  "PiiEntityTypes": ["BANK_ACCOUNT_NUMBER"|"BANK_ROUTING"|"CREDIT_DEBIT_NUMBER"|"CREDIT_DEBIT_CVV"|"CREDIT_DEBIT_EXPIRY"|"PIN"|"EMAIL"|"ADDRESS"|"NAME"|"PHONE"|"SSN"|"ALL", ...]
}
```

`--identify-language` | `--no-identify-language` (boolean)

Enables automatic language identification in your transcription job request. Use this parameter if your media file contains only one language. If your media contains multiple languages, use `IdentifyMultipleLanguages` instead.

If you include `IdentifyLanguage` , you can optionally include a list of language codes, using `LanguageOptions` , that you think may be present in your media file. Including `LanguageOptions` restricts `IdentifyLanguage` to only the language options that you specify, which can improve transcription accuracy.

If you want to apply a custom language model, a custom vocabulary, or a custom vocabulary filter to your automatic language identification request, include `LanguageIdSettings` with the relevant sub-parameters (`VocabularyName` , `LanguageModelName` , and `VocabularyFilterName` ). If you include `LanguageIdSettings` , also include `LanguageOptions` .

Note that you must include one of `LanguageCode` , `IdentifyLanguage` , or `IdentifyMultipleLanguages` in your request. If you include more than one of these parameters, your transcription job fails.

`--identify-multiple-languages` | `--no-identify-multiple-languages` (boolean)

Enables automatic multi-language identification in your transcription job request. Use this parameter if your media file contains more than one language. If your media contains only one language, use `IdentifyLanguage` instead.

If you include `IdentifyMultipleLanguages` , you can optionally include a list of language codes, using `LanguageOptions` , that you think may be present in your media file. Including `LanguageOptions` restricts `IdentifyLanguage` to only the language options that you specify, which can improve transcription accuracy.

If you want to apply a custom vocabulary or a custom vocabulary filter to your automatic language identification request, include `LanguageIdSettings` with the relevant sub-parameters (`VocabularyName` and `VocabularyFilterName` ). If you include `LanguageIdSettings` , also include `LanguageOptions` .

Note that you must include one of `LanguageCode` , `IdentifyLanguage` , or `IdentifyMultipleLanguages` in your request. If you include more than one of these parameters, your transcription job fails.

`--language-options` (list)

You can specify two or more language codes that represent the languages you think may be present in your media. Including more than five is not recommended. If youâre unsure what languages are present, do not include this parameter.

If you include `LanguageOptions` in your request, you must also include `IdentifyLanguage` .

For more information, refer to [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) .

To transcribe speech in Modern Standard Arabic (`ar-SA` )in Amazon Web Services GovCloud (US) (US-West, us-gov-west-1), Amazon Web Services GovCloud (US) (US-East, us-gov-east-1), in Canada (Calgary) ca-west-1 and Africa (Cape Town) af-south-1, your media file must be encoded at a sample rate of 16,000 Hz or higher.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  af-ZA
  ar-AE
  ar-SA
  da-DK
  de-CH
  de-DE
  en-AB
  en-AU
  en-GB
  en-IE
  en-IN
  en-US
  en-WL
  es-ES
  es-US
  fa-IR
  fr-CA
  fr-FR
  he-IL
  hi-IN
  id-ID
  it-IT
  ja-JP
  ko-KR
  ms-MY
  nl-NL
  pt-BR
  pt-PT
  ru-RU
  ta-IN
  te-IN
  tr-TR
  zh-CN
  zh-TW
  th-TH
  en-ZA
  en-NZ
  vi-VN
  sv-SE
  ab-GE
  ast-ES
  az-AZ
  ba-RU
  be-BY
  bg-BG
  bn-IN
  bs-BA
  ca-ES
  ckb-IQ
  ckb-IR
  cs-CZ
  cy-WL
  el-GR
  et-ET
  eu-ES
  fi-FI
  gl-ES
  gu-IN
  ha-NG
  hr-HR
  hu-HU
  hy-AM
  is-IS
  ka-GE
  kab-DZ
  kk-KZ
  kn-IN
  ky-KG
  lg-IN
  lt-LT
  lv-LV
  mhr-RU
  mi-NZ
  mk-MK
  ml-IN
  mn-MN
  mr-IN
  mt-MT
  no-NO
  or-IN
  pa-IN
  pl-PL
  ps-AF
  ro-RO
  rw-RW
  si-LK
  sk-SK
  sl-SI
  so-SO
  sr-RS
  su-ID
  sw-BI
  sw-KE
  sw-RW
  sw-TZ
  sw-UG
  tl-PH
  tt-RU
  ug-CN
  uk-UA
  uz-UZ
  wo-SN
  zh-HK
  zu-ZA
```

`--subtitles` (structure)

Produces subtitle files for your input media. You can specify WebVTT (*.vtt) and SubRip (*.srt) formats.

Formats -> (list)

Specify the output format for your subtitle file; if you select both WebVTT (`vtt` ) and SubRip (`srt` ) formats, two output files are generated.

(string)

OutputStartIndex -> (integer)

Specify the starting value that is assigned to the first subtitle segment.

The default start index for Amazon Transcribe is `0` , which differs from the more widely used standard of `1` . If youâre uncertain which value to use, we recommend choosing `1` , as this may improve compatibility with other services.

Shorthand Syntax:

```
Formats=string,string,OutputStartIndex=integer
```

JSON Syntax:

```
{
  "Formats": ["vtt"|"srt", ...],
  "OutputStartIndex": integer
}
```

`--tags` (list)

Adds one or more custom tags, each in the form of a key:value pair, to a new transcription job at the time you start this new job.

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

`--language-id-settings` (map)

If using automatic language identification in your request and you want to apply a custom language model, a custom vocabulary, or a custom vocabulary filter, include `LanguageIdSettings` with the relevant sub-parameters (`VocabularyName` , `LanguageModelName` , and `VocabularyFilterName` ). Note that multi-language identification (`IdentifyMultipleLanguages` ) doesnât support custom language models.

`LanguageIdSettings` supports two to five language codes. Each language code you include can have an associated custom language model, custom vocabulary, and custom vocabulary filter. The language codes that you specify must match the languages of the associated custom language models, custom vocabularies, and custom vocabulary filters.

Itâs recommended that you include `LanguageOptions` when using `LanguageIdSettings` to ensure that the correct language dialect is identified. For example, if you specify a custom vocabulary that is in `en-US` but Amazon Transcribe determines that the language spoken in your media is `en-AU` , your custom vocabulary *is not* applied to your transcription. If you include `LanguageOptions` and include `en-US` as the only English language dialect, your custom vocabulary *is* applied to your transcription.

If you want to include a custom language model with your request but **do not** want to use automatic language identification, use instead the parameter with the `LanguageModelName` sub-parameter. If you want to include a custom vocabulary or a custom vocabulary filter (or both) with your request but **do not** want to use automatic language identification, use instead the parameter with the `VocabularyName` or `VocabularyFilterName` (or both) sub-parameter.

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

Shorthand Syntax:

```
KeyName1=VocabularyName=string,VocabularyFilterName=string,LanguageModelName=string,KeyName2=VocabularyName=string,VocabularyFilterName=string,LanguageModelName=string

Where valid key names are:
  af-ZA
  ar-AE
  ar-SA
  da-DK
  de-CH
  de-DE
  en-AB
  en-AU
  en-GB
  en-IE
  en-IN
  en-US
  en-WL
  es-ES
  es-US
  fa-IR
  fr-CA
  fr-FR
  he-IL
  hi-IN
  id-ID
  it-IT
  ja-JP
  ko-KR
  ms-MY
  nl-NL
  pt-BR
  pt-PT
  ru-RU
  ta-IN
  te-IN
  tr-TR
  zh-CN
  zh-TW
  th-TH
  en-ZA
  en-NZ
  vi-VN
  sv-SE
  ab-GE
  ast-ES
  az-AZ
  ba-RU
  be-BY
  bg-BG
  bn-IN
  bs-BA
  ca-ES
  ckb-IQ
  ckb-IR
  cs-CZ
  cy-WL
  el-GR
  et-ET
  eu-ES
  fi-FI
  gl-ES
  gu-IN
  ha-NG
  hr-HR
  hu-HU
  hy-AM
  is-IS
  ka-GE
  kab-DZ
  kk-KZ
  kn-IN
  ky-KG
  lg-IN
  lt-LT
  lv-LV
  mhr-RU
  mi-NZ
  mk-MK
  ml-IN
  mn-MN
  mr-IN
  mt-MT
  no-NO
  or-IN
  pa-IN
  pl-PL
  ps-AF
  ro-RO
  rw-RW
  si-LK
  sk-SK
  sl-SI
  so-SO
  sr-RS
  su-ID
  sw-BI
  sw-KE
  sw-RW
  sw-TZ
  sw-UG
  tl-PH
  tt-RU
  ug-CN
  uk-UA
  uz-UZ
  wo-SN
  zh-HK
  zu-ZA
```

JSON Syntax:

```
{"af-ZA"|"ar-AE"|"ar-SA"|"da-DK"|"de-CH"|"de-DE"|"en-AB"|"en-AU"|"en-GB"|"en-IE"|"en-IN"|"en-US"|"en-WL"|"es-ES"|"es-US"|"fa-IR"|"fr-CA"|"fr-FR"|"he-IL"|"hi-IN"|"id-ID"|"it-IT"|"ja-JP"|"ko-KR"|"ms-MY"|"nl-NL"|"pt-BR"|"pt-PT"|"ru-RU"|"ta-IN"|"te-IN"|"tr-TR"|"zh-CN"|"zh-TW"|"th-TH"|"en-ZA"|"en-NZ"|"vi-VN"|"sv-SE"|"ab-GE"|"ast-ES"|"az-AZ"|"ba-RU"|"be-BY"|"bg-BG"|"bn-IN"|"bs-BA"|"ca-ES"|"ckb-IQ"|"ckb-IR"|"cs-CZ"|"cy-WL"|"el-GR"|"et-ET"|"eu-ES"|"fi-FI"|"gl-ES"|"gu-IN"|"ha-NG"|"hr-HR"|"hu-HU"|"hy-AM"|"is-IS"|"ka-GE"|"kab-DZ"|"kk-KZ"|"kn-IN"|"ky-KG"|"lg-IN"|"lt-LT"|"lv-LV"|"mhr-RU"|"mi-NZ"|"mk-MK"|"ml-IN"|"mn-MN"|"mr-IN"|"mt-MT"|"no-NO"|"or-IN"|"pa-IN"|"pl-PL"|"ps-AF"|"ro-RO"|"rw-RW"|"si-LK"|"sk-SK"|"sl-SI"|"so-SO"|"sr-RS"|"su-ID"|"sw-BI"|"sw-KE"|"sw-RW"|"sw-TZ"|"sw-UG"|"tl-PH"|"tt-RU"|"ug-CN"|"uk-UA"|"uz-UZ"|"wo-SN"|"zh-HK"|"zu-ZA": {
      "VocabularyName": "string",
      "VocabularyFilterName": "string",
      "LanguageModelName": "string"
    }
  ...}
```

`--toxicity-detection` (list)

Enables toxic speech detection in your transcript. If you include `ToxicityDetection` in your request, you must also include `ToxicityCategories` .

For information on the types of toxic speech Amazon Transcribe can detect, see [Detecting toxic speech](https://docs.aws.amazon.com/transcribe/latest/dg/toxic-language.html) .

(structure)

Contains `ToxicityCategories` , which is a required parameter if you want to enable toxicity detection (`ToxicityDetection` ) in your transcription request.

ToxicityCategories -> (list)

If you include `ToxicityDetection` in your transcription request, you must also include `ToxicityCategories` . The only accepted value for this parameter is `ALL` .

(string)

Shorthand Syntax:

```
ToxicityCategories=string,string ...
```

JSON Syntax:

```
[
  {
    "ToxicityCategories": ["ALL", ...]
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

**Example 1: To transcribe an audio file**

The following `start-transcription-job` example transcribes your audio file.

```
aws transcribe start-transcription-job \
    --cli-input-json file://myfile.json
```

Contents of `myfile.json`:

```
{
    "TranscriptionJobName": "cli-simple-transcription-job",
    "LanguageCode": "the-language-of-your-transcription-job",
    "Media": {
        "MediaFileUri": "s3://amzn-s3-demo-bucket/Amazon-S3-prefix/your-media-file-name.file-extension"
    }
}
```

For more information, see [Getting Started (AWS Command Line Interface)](https://docs.aws.amazon.com/transcribe/latest/dg/getting-started-cli.html) in the *Amazon Transcribe Developer Guide*.

**Example 2: To transcribe a multi-channel audio file**

The following `start-transcription-job` example transcribes your multi-channel audio file.

```
aws transcribe start-transcription-job \
    --cli-input-json file://mysecondfile.json
```

Contents of `mysecondfile.json`:

```
{
    "TranscriptionJobName": "cli-channelid-job",
    "LanguageCode": "the-language-of-your-transcription-job",
    "Media": {
        "MediaFileUri": "s3://amzn-s3-demo-bucket/Amazon-S3-prefix/your-media-file-name.file-extension"
    },
    "Settings":{
        "ChannelIdentification":true
    }
}
```

Output:

```
{
    "TranscriptionJob": {
        "TranscriptionJobName": "cli-channelid-job",
        "TranscriptionJobStatus": "IN_PROGRESS",
        "LanguageCode": "the-language-of-your-transcription-job",
        "Media": {
            "MediaFileUri": "s3://amzn-s3-demo-bucket/Amazon-S3-prefix/your-media-file-name.file-extension"
        },
        "StartTime": "2020-09-17T16:07:56.817000+00:00",
        "CreationTime": "2020-09-17T16:07:56.784000+00:00",
        "Settings": {
            "ChannelIdentification": true
        }
    }
}
```

For more information, see [Transcribing Multi-Channel Audio](https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html) in the *Amazon Transcribe Developer Guide*.

**Example 3: To transcribe an audio file and identify the different speakers**

The following `start-transcription-job` example transcribes your audio file and identifies the speakers in the transcription output.

```
aws transcribe start-transcription-job \
    --cli-input-json file://mythirdfile.json
```

Contents of `mythirdfile.json`:

```
{
    "TranscriptionJobName": "cli-speakerid-job",
    "LanguageCode": "the-language-of-your-transcription-job",
    "Media": {
        "MediaFileUri": "s3://amzn-s3-demo-bucket/Amazon-S3-prefix/your-media-file-name.file-extension"
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
    "TranscriptionJob": {
        "TranscriptionJobName": "cli-speakerid-job",
        "TranscriptionJobStatus": "IN_PROGRESS",
        "LanguageCode": "the-language-of-your-transcription-job",
        "Media": {
            "MediaFileUri": "s3://amzn-s3-demo-bucket/Amazon-S3-prefix/your-media-file-name.file-extension"
        },
        "StartTime": "2020-09-17T16:22:59.696000+00:00",
        "CreationTime": "2020-09-17T16:22:59.676000+00:00",
        "Settings": {
            "ShowSpeakerLabels": true,
            "MaxSpeakerLabels": 2
        }
    }
}
```

For more information, see [Identifying Speakers](https://docs.aws.amazon.com/transcribe/latest/dg/diarization.html) in the *Amazon Transcribe Developer Guide*.

**Example 4: To transcribe an audio file and mask any unwanted words in the transcription output**

The following `start-transcription-job` example transcribes your audio file and uses a vocabulary filter youâve previously created to mask any unwanted words.

```
aws transcribe start-transcription-job \
    --cli-input-json file://myfourthfile.json
```

Contents of `myfourthfile.json`:

```
{
    "TranscriptionJobName": "cli-filter-mask-job",
    "LanguageCode": "the-language-of-your-transcription-job",
    "Media": {
          "MediaFileUri": "s3://amzn-s3-demo-bucket/Amazon-S3-prefix/your-media-file-name.file-extension"
    },
    "Settings":{
        "VocabularyFilterName": "your-vocabulary-filter",
        "VocabularyFilterMethod": "mask"
    }
}
```

Output:

```
{
    "TranscriptionJob": {
        "TranscriptionJobName": "cli-filter-mask-job",
        "TranscriptionJobStatus": "IN_PROGRESS",
        "LanguageCode": "the-language-of-your-transcription-job",
        "Media": {
            "MediaFileUri": "s3://Amazon-S3-Prefix/your-media-file.file-extension"
        },
        "StartTime": "2020-09-18T16:36:18.568000+00:00",
        "CreationTime": "2020-09-18T16:36:18.547000+00:00",
        "Settings": {
            "VocabularyFilterName": "your-vocabulary-filter",
            "VocabularyFilterMethod": "mask"
        }
    }
}
```

For more information, see [Filtering Transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/filter-transcriptions.html) in the *Amazon Transcribe Developer Guide*.

**Example 5: To transcribe an audio file and remove any unwanted words in the transcription output**

The following `start-transcription-job` example transcribes your audio file and uses a vocabulary filter youâve previously created to mask any unwanted words.

```
aws transcribe start-transcription-job \
    --cli-input-json file://myfifthfile.json
```

Contents of `myfifthfile.json`:

```
{
    "TranscriptionJobName": "cli-filter-remove-job",
    "LanguageCode": "the-language-of-your-transcription-job",
    "Media": {
        "MediaFileUri": "s3://amzn-s3-demo-bucket/Amazon-S3-prefix/your-media-file-name.file-extension"
    },
    "Settings":{
        "VocabularyFilterName": "your-vocabulary-filter",
        "VocabularyFilterMethod": "remove"
    }
}
```

Output:

```
{
    "TranscriptionJob": {
        "TranscriptionJobName": "cli-filter-remove-job",
        "TranscriptionJobStatus": "IN_PROGRESS",
        "LanguageCode": "the-language-of-your-transcription-job",
        "Media": {
            "MediaFileUri": "s3://amzn-s3-demo-bucket/Amazon-S3-prefix/your-media-file-name.file-extension"
        },
        "StartTime": "2020-09-18T16:36:18.568000+00:00",
        "CreationTime": "2020-09-18T16:36:18.547000+00:00",
        "Settings": {
            "VocabularyFilterName": "your-vocabulary-filter",
            "VocabularyFilterMethod": "remove"
        }
    }
}
```

For more information, see [Filtering Transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/filter-transcriptions.html) in the *Amazon Transcribe Developer Guide*.

**Example 6: To transcribe an audio file with increased accuracy using a custom vocabulary**

The following `start-transcription-job` example transcribes your audio file and uses a vocabulary filter youâve previously created to mask any unwanted words.

```
aws transcribe start-transcription-job \
    --cli-input-json file://mysixthfile.json
```

Contents of `mysixthfile.json`:

```
{
    "TranscriptionJobName": "cli-vocab-job",
    "LanguageCode": "the-language-of-your-transcription-job",
    "Media": {
        "MediaFileUri": "s3://amzn-s3-demo-bucket/Amazon-S3-prefix/your-media-file-name.file-extension"
    },
    "Settings":{
        "VocabularyName": "your-vocabulary"
    }
}
```

Output:

```
{
    "TranscriptionJob": {
        "TranscriptionJobName": "cli-vocab-job",
        "TranscriptionJobStatus": "IN_PROGRESS",
        "LanguageCode": "the-language-of-your-transcription-job",
        "Media": {
            "MediaFileUri": "s3://amzn-s3-demo-bucket/Amazon-S3-prefix/your-media-file-name.file-extension"
        },
        "StartTime": "2020-09-18T16:36:18.568000+00:00",
        "CreationTime": "2020-09-18T16:36:18.547000+00:00",
        "Settings": {
            "VocabularyName": "your-vocabulary"
        }
    }
}
```

For more information, see [Filtering Transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/filter-transcriptions.html) in the *Amazon Transcribe Developer Guide*.

**Example 7: To identify the language of an audio file and transcribe it**

The following `start-transcription-job` example transcribes your audio file and uses a vocabulary filter youâve previously created to mask any unwanted words.

```
aws transcribe start-transcription-job \
    --cli-input-json file://myseventhfile.json
```

Contents of `myseventhfile.json`:

```
{
    "TranscriptionJobName": "cli-identify-language-transcription-job",
    "IdentifyLanguage": true,
    "Media": {
        "MediaFileUri": "s3://amzn-s3-demo-bucket/Amazon-S3-prefix/your-media-file-name.file-extension"
    }
}
```

Output:

```
{
    "TranscriptionJob": {
        "TranscriptionJobName": "cli-identify-language-transcription-job",
        "TranscriptionJobStatus": "IN_PROGRESS",
        "Media": {
            "MediaFileUri": "s3://amzn-s3-demo-bucket/Amazon-S3-prefix/your-media-file-name.file-extension"
        },
        "StartTime": "2020-09-18T22:27:23.970000+00:00",
        "CreationTime": "2020-09-18T22:27:23.948000+00:00",
        "IdentifyLanguage": true
    }
}
```

For more information, see [Identifying the Language](https://docs.aws.amazon.com/transcribe/latest/dg/auto-lang-id.html) in the *Amazon Transcribe Developer Guide*.

**Example 8: To transcribe an audio file with personally identifiable information redacted**

The following `start-transcription-job` example transcribes your audio file and redacts any personally identifiable information in the transcription output.

```
aws transcribe start-transcription-job \
    --cli-input-json file://myeighthfile.json
```

Contents of `myeigthfile.json`:

```
{
    "TranscriptionJobName": "cli-redaction-job",
    "LanguageCode": "language-code",
    "Media": {
        "MediaFileUri": "s3://Amazon-S3-Prefix/your-media-file.file-extension"
    },
    "ContentRedaction": {
        "RedactionOutput":"redacted",
        "RedactionType":"PII"
    }
}
```

Output:

```
{
    "TranscriptionJob": {
        "TranscriptionJobName": "cli-redaction-job",
        "TranscriptionJobStatus": "IN_PROGRESS",
        "LanguageCode": "language-code",
        "Media": {
            "MediaFileUri": "s3://Amazon-S3-Prefix/your-media-file.file-extension"
        },
        "StartTime": "2020-09-25T23:49:13.195000+00:00",
        "CreationTime": "2020-09-25T23:49:13.176000+00:00",
        "ContentRedaction": {
            "RedactionType": "PII",
            "RedactionOutput": "redacted"
        }
    }
}
```

For more information, see [Automatic Content Redaction](https://docs.aws.amazon.com/transcribe/latest/dg/content-redaction.html) in the *Amazon Transcribe Developer Guide*.

**Example 9: To generate a transcript with personally identifiable information (PII) redacted and an unredacted transcript**

The following `start-transcription-job` example generates two transcrptions of your audio file, one with the personally identifiable information redacted, and the other without any redactions.

```
aws transcribe start-transcription-job \
    --cli-input-json file://myninthfile.json
```

Contents of `myninthfile.json`:

```
{
    "TranscriptionJobName": "cli-redaction-job-with-unredacted-transcript",
    "LanguageCode": "language-code",
    "Media": {
          "MediaFileUri": "s3://Amazon-S3-Prefix/your-media-file.file-extension"
        },
    "ContentRedaction": {
        "RedactionOutput":"redacted_and_unredacted",
        "RedactionType":"PII"
    }
}
```

Output:

```
{
    "TranscriptionJob": {
        "TranscriptionJobName": "cli-redaction-job-with-unredacted-transcript",
        "TranscriptionJobStatus": "IN_PROGRESS",
        "LanguageCode": "language-code",
        "Media": {
            "MediaFileUri": "s3://Amazon-S3-Prefix/your-media-file.file-extension"
        },
        "StartTime": "2020-09-25T23:59:47.677000+00:00",
        "CreationTime": "2020-09-25T23:59:47.653000+00:00",
        "ContentRedaction": {
            "RedactionType": "PII",
            "RedactionOutput": "redacted_and_unredacted"
        }
    }
}
```

For more information, see [Automatic Content Redaction](https://docs.aws.amazon.com/transcribe/latest/dg/content-redaction.html) in the *Amazon Transcribe Developer Guide*.

**Example 10: To use a custom language model youâve previously created to transcribe an audio file.**

The following `start-transcription-job` example transcribes your audio file with a custom language model youâve previously created.

```
aws transcribe start-transcription-job \
    --cli-input-json file://mytenthfile.json
```

Contents of `mytenthfile.json`:

```
{
    "TranscriptionJobName": "cli-clm-2-job-1",
    "LanguageCode": "language-code",
    "Media": {
        "MediaFileUri": "s3://amzn-s3-demo-bucket/your-audio-file.file-extension"
    },
    "ModelSettings": {
        "LanguageModelName":"cli-clm-2"
    }
}
```

Output:

```
{
    "TranscriptionJob": {
        "TranscriptionJobName": "cli-clm-2-job-1",
        "TranscriptionJobStatus": "IN_PROGRESS",
        "LanguageCode": "language-code",
        "Media": {
            "MediaFileUri": "s3://amzn-s3-demo-bucket/your-audio-file.file-extension"
        },
        "StartTime": "2020-09-28T17:56:01.835000+00:00",
        "CreationTime": "2020-09-28T17:56:01.801000+00:00",
        "ModelSettings": {
            "LanguageModelName": "cli-clm-2"
        }
    }
}
```

For more information, see [Improving Domain-Specific Transcription Accuracy with Custom Language Models](https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html) in the *Amazon Transcribe Developer Guide*.

## Output

TranscriptionJob -> (structure)

Provides detailed information about the current transcription job, including job status and, if applicable, failure reason.

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