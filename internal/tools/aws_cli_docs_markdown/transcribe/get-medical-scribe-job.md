# get-medical-scribe-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-medical-scribe-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-medical-scribe-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transcribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/index.html#cli-aws-transcribe) ]

# get-medical-scribe-job

## Description

Provides information about the specified Medical Scribe job.

To view the status of the specified medical transcription job, check the `MedicalScribeJobStatus` field. If the status is `COMPLETED` , the job is finished. You can find the results at the location specified in `MedicalScribeOutput` . If the status is `FAILED` , `FailureReason` provides details on why your Medical Scribe job failed.

To get a list of your Medical Scribe jobs, use the operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/GetMedicalScribeJob)

## Synopsis

```
get-medical-scribe-job
--medical-scribe-job-name <value>
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

`--medical-scribe-job-name` (string)

The name of the Medical Scribe job you want information about. Job names are case sensitive.

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

MedicalScribeJob -> (structure)

Provides detailed information about the specified Medical Scribe job, including job status and, if applicable, failure reason

MedicalScribeJobName -> (string)

The name of the Medical Scribe job. Job names are case sensitive and must be unique within an Amazon Web Services account.

MedicalScribeJobStatus -> (string)

Provides the status of the specified Medical Scribe job.

If the status is `COMPLETED` , the job is finished and you can find the results at the location specified in `MedicalScribeOutput` If the status is `FAILED` , `FailureReason` provides details on why your Medical Scribe job failed.

LanguageCode -> (string)

The language code used to create your Medical Scribe job. US English (`en-US` ) is the only supported language for Medical Scribe jobs.

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

MedicalScribeOutput -> (structure)

The location of the output of your Medical Scribe job. `ClinicalDocumentUri` holds the Amazon S3 URI for the Clinical Document and `TranscriptFileUri` holds the Amazon S3 URI for the Transcript.

TranscriptFileUri -> (string)

Holds the Amazon S3 URI for the Transcript.

ClinicalDocumentUri -> (string)

Holds the Amazon S3 URI for the Clinical Document.

StartTime -> (timestamp)

The date and time your Medical Scribe job began processing.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:32:58.789000-07:00` represents a Medical Scribe job that started processing at 12:32 PM UTC-7 on May 4, 2022.

CreationTime -> (timestamp)

The date and time the specified Medical Scribe job request was made.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:32:58.761000-07:00` represents a Medical Scribe job that started processing at 12:32 PM UTC-7 on May 4, 2022.

CompletionTime -> (timestamp)

The date and time the specified Medical Scribe job finished processing.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:32:58.761000-07:00` represents a Medical Scribe job that finished processing at 12:32 PM UTC-7 on May 4, 2022.

FailureReason -> (string)

If `MedicalScribeJobStatus` is `FAILED` , `FailureReason` contains information about why the transcription job failed. See also: [Common Errors](https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html) .

Settings -> (structure)

Makes it possible to control how your Medical Scribe job is processed using a `MedicalScribeSettings` object. Specify `ChannelIdentification` if `ChannelDefinitions` are set. Enabled `ShowSpeakerLabels` if `ChannelIdentification` and `ChannelDefinitions` are not set. One and only one of `ChannelIdentification` and `ShowSpeakerLabels` must be set. If `ShowSpeakerLabels` is set, `MaxSpeakerLabels` must also be set. Use `Settings` to specify a vocabulary or vocabulary filter or both using `VocabularyName` , `VocabularyFilterName` . `VocabularyFilterMethod` must be specified if `VocabularyFilterName` is set.

ShowSpeakerLabels -> (boolean)

Enables speaker partitioning (diarization) in your Medical Scribe output. Speaker partitioning labels the speech from individual speakers in your media file.

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

VocabularyName -> (string)

The name of the custom vocabulary you want to include in your Medical Scribe request. Custom vocabulary names are case sensitive.

VocabularyFilterName -> (string)

The name of the custom vocabulary filter you want to include in your Medical Scribe request. Custom vocabulary filter names are case sensitive.

Note that if you include `VocabularyFilterName` in your request, you must also include `VocabularyFilterMethod` .

VocabularyFilterMethod -> (string)

Specify how you want your custom vocabulary filter applied to your transcript.

To replace words with `***` , choose `mask` .

To delete words, choose `remove` .

To flag words without changing them, choose `tag` .

ClinicalNoteGenerationSettings -> (structure)

Specify settings for the clinical note generation.

NoteTemplate -> (string)

Specify one of the following templates to use for the clinical note summary. The default is `HISTORY_AND_PHYSICAL` .

- HISTORY_AND_PHYSICAL: Provides summaries for key sections of the clinical documentation. Examples of sections include Chief Complaint, History of Present Illness, Review of Systems, Past Medical History, Assessment, and Plan.
- GIRPP: Provides summaries based on the patients progress toward goals. Examples of sections include Goal, Intervention, Response, Progress, and Plan.

DataAccessRoleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files, write to the output bucket, and use your KMS key if supplied. If the role that you specify doesnât have the appropriate permissions your request fails.

IAM role ARNs have the format `arn:partition:iam::account:role/role-name-with-path` . For example: `arn:aws:iam::111122223333:role/Admin` .

For more information, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns) .

ChannelDefinitions -> (list)

Makes it possible to specify which speaker is on which channel. For example, if the clinician is the first participant to speak, you would set `ChannelId` of the first `ChannelDefinition` in the list to `0` (to indicate the first channel) and `ParticipantRole` to `CLINICIAN` (to indicate that itâs the clinician speaking). Then you would set the `ChannelId` of the second `ChannelDefinition` in the list to `1` (to indicate the second channel) and `ParticipantRole` to `PATIENT` (to indicate that itâs the patient speaking).

(structure)

Indicates which speaker is on which channel. The options are `CLINICIAN` and `PATIENT`

ChannelId -> (integer)

Specify the audio channel you want to define.

ParticipantRole -> (string)

Specify the participant that you want to flag. The options are `CLINICIAN` and `PATIENT`

Tags -> (list)

Adds one or more custom tags, each in the form of a key:value pair, to the Medica Scribe job.

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