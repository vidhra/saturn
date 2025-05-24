# update-media-insights-pipeline-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-media-pipelines/update-media-insights-pipeline-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-media-pipelines/update-media-insights-pipeline-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [chime-sdk-media-pipelines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-media-pipelines/index.html#cli-aws-chime-sdk-media-pipelines) ]

# update-media-insights-pipeline-configuration

## Description

Updates the media insights pipelineâs configuration settings.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/chime-sdk-media-pipelines-2021-07-15/UpdateMediaInsightsPipelineConfiguration)

## Synopsis

```
update-media-insights-pipeline-configuration
--identifier <value>
--resource-access-role-arn <value>
[--real-time-alert-configuration <value>]
--elements <value>
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

`--identifier` (string)

The unique identifier for the resource to be updated. Valid values include the name and ARN of the media insights pipeline configuration.

`--resource-access-role-arn` (string)

The ARN of the role used by the service to access Amazon Web Services resources.

`--real-time-alert-configuration` (structure)

The configuration settings for real-time alerts for the media insights pipeline.

Disabled -> (boolean)

Turns off real-time alerts.

Rules -> (list)

The rules in the alert. Rules specify the words or phrases that you want to be notified about.

(structure)

Specifies the words or phrases that trigger an alert.

Type -> (string)

The type of alert rule.

KeywordMatchConfiguration -> (structure)

Specifies the settings for matching the keywords in a real-time alert rule.

RuleName -> (string)

The name of the keyword match rule.

Keywords -> (list)

The keywords or phrases that you want to match.

(string)

Negate -> (boolean)

Matches keywords or phrases on their presence or absence. If set to `TRUE` , the rule matches when all the specified keywords or phrases are absent. Default: `FALSE` .

SentimentConfiguration -> (structure)

Specifies the settings for predicting sentiment in a real-time alert rule.

RuleName -> (string)

The name of the rule in the sentiment configuration.

SentimentType -> (string)

The type of sentiment, `POSITIVE` , `NEGATIVE` , or `NEUTRAL` .

TimePeriod -> (integer)

Specifies the analysis interval.

IssueDetectionConfiguration -> (structure)

Specifies the issue detection settings for a real-time alert rule.

RuleName -> (string)

The name of the issue detection rule.

JSON Syntax:

```
{
  "Disabled": true|false,
  "Rules": [
    {
      "Type": "KeywordMatch"|"Sentiment"|"IssueDetection",
      "KeywordMatchConfiguration": {
        "RuleName": "string",
        "Keywords": ["string", ...],
        "Negate": true|false
      },
      "SentimentConfiguration": {
        "RuleName": "string",
        "SentimentType": "NEGATIVE",
        "TimePeriod": integer
      },
      "IssueDetectionConfiguration": {
        "RuleName": "string"
      }
    }
    ...
  ]
}
```

`--elements` (list)

The elements in the request, such as a processor for Amazon Transcribe or a sink for a Kinesis Data Stream..

(structure)

An element in a media insights pipeline configuration.

Type -> (string)

The element type.

AmazonTranscribeCallAnalyticsProcessorConfiguration -> (structure)

The analytics configuration settings for transcribing audio in a media insights pipeline configuration element.

LanguageCode -> (string)

The language code in the configuration.

VocabularyName -> (string)

Specifies the name of the custom vocabulary to use when processing a transcription. Note that vocabulary names are case sensitive.

If the language of the specified custom vocabulary doesnât match the language identified in your media, the custom vocabulary is not applied to your transcription.

For more information, see [Custom vocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html) in the *Amazon Transcribe Developer Guide* .

Length Constraints: Minimum length of 1. Maximum length of 200.

VocabularyFilterName -> (string)

Specifies the name of the custom vocabulary filter to use when processing a transcription. Note that vocabulary filter names are case sensitive.

If the language of the specified custom vocabulary filter doesnât match the language identified in your media, the vocabulary filter is not applied to your transcription.

For more information, see [Using vocabulary filtering with unwanted words](https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html) in the *Amazon Transcribe Developer Guide* .

Length Constraints: Minimum length of 1. Maximum length of 200.

VocabularyFilterMethod -> (string)

Specifies how to apply a vocabulary filter to a transcript.

To replace words with ******* , choose `mask` .

To delete words, choose `remove` .

To flag words without changing them, choose `tag` .

LanguageModelName -> (string)

Specifies the name of the custom language model to use when processing a transcription. Note that language model names are case sensitive.

The language of the specified language model must match the language code specified in the transcription request. If the languages donât match, the custom language model isnât applied. Language mismatches donât generate errors or warnings.

For more information, see [Custom language models](https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html) in the *Amazon Transcribe Developer Guide* .

EnablePartialResultsStabilization -> (boolean)

Enables partial result stabilization for your transcription. Partial result stabilization can reduce latency in your output, but may impact accuracy. For more information, see [Partial-result stabilization](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization) in the *Amazon Transcribe Developer Guide* .

PartialResultsStability -> (string)

Specifies the level of stability to use when you enable partial results stabilization (`EnablePartialResultsStabilization` ).

Low stability provides the highest accuracy. High stability transcribes faster, but with slightly lower accuracy.

For more information, see [Partial-result stabilization](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization) in the *Amazon Transcribe Developer Guide* .

ContentIdentificationType -> (string)

Labels all personally identifiable information (PII) identified in your transcript.

Content identification is performed at the segment level; PII specified in `PiiEntityTypes` is flagged upon complete transcription of an audio segment.

You canât set `ContentIdentificationType` and `ContentRedactionType` in the same request. If you do, your request returns a `BadRequestException` .

For more information, see [Redacting or identifying personally identifiable information](https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html) in the *Amazon Transcribe Developer Guide* .

ContentRedactionType -> (string)

Redacts all personally identifiable information (PII) identified in your transcript.

Content redaction is performed at the segment level; PII specified in `PiiEntityTypes` is redacted upon complete transcription of an audio segment.

You canât set `ContentRedactionType` and `ContentIdentificationType` in the same request. If you do, your request returns a `BadRequestException` .

For more information, see [Redacting or identifying personally identifiable information](https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html) in the *Amazon Transcribe Developer Guide* .

PiiEntityTypes -> (string)

Specifies the types of personally identifiable information (PII) to redact from a transcript. You can include as many types as youâd like, or you can select `ALL` .

To include `PiiEntityTypes` in your Call Analytics request, you must also include `ContentIdentificationType` or `ContentRedactionType` , but you canât include both.

Values must be comma-separated and can include: `ADDRESS` , `BANK_ACCOUNT_NUMBER` , `BANK_ROUTING` , `CREDIT_DEBIT_CVV` , `CREDIT_DEBIT_EXPIRY` , `CREDIT_DEBIT_NUMBER` , `EMAIL` , `NAME` , `PHONE` , `PIN` , `SSN` , or `ALL` .

Length Constraints: Minimum length of 1. Maximum length of 300.

FilterPartialResults -> (boolean)

If true, `UtteranceEvents` with `IsPartial: true` are filtered out of the insights target.

PostCallAnalyticsSettings -> (structure)

The settings for a post-call analysis task in an analytics configuration.

OutputLocation -> (string)

The URL of the Amazon S3 bucket that contains the post-call data.

DataAccessRoleArn -> (string)

The ARN of the role used by Amazon Web Services Transcribe to upload your post call analysis. For more information, see [Post-call analytics with real-time transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/tca-post-call.html) in the *Amazon Transcribe Developer Guide* .

ContentRedactionOutput -> (string)

The content redaction output settings for a post-call analysis task.

OutputEncryptionKMSKeyId -> (string)

The ID of the KMS (Key Management Service) key used to encrypt the output.

CallAnalyticsStreamCategories -> (list)

By default, all `CategoryEvents` are sent to the insights target. If this parameter is specified, only included categories are sent to the insights target.

(string)

AmazonTranscribeProcessorConfiguration -> (structure)

The transcription processor configuration settings in a media insights pipeline configuration element.

LanguageCode -> (string)

The language code that represents the language spoken in your audio.

If youâre unsure of the language spoken in your audio, consider using `IdentifyLanguage` to enable automatic language identification.

For a list of languages that real-time Call Analytics supports, see the [Supported languages table](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) in the *Amazon Transcribe Developer Guide* .

VocabularyName -> (string)

The name of the custom vocabulary that you specified in your Call Analytics request.

Length Constraints: Minimum length of 1. Maximum length of 200.

VocabularyFilterName -> (string)

The name of the custom vocabulary filter that you specified in your Call Analytics request.

Length Constraints: Minimum length of 1. Maximum length of 200.

VocabularyFilterMethod -> (string)

The vocabulary filtering method used in your Call Analytics transcription.

ShowSpeakerLabel -> (boolean)

Enables speaker partitioning (diarization) in your transcription output. Speaker partitioning labels the speech from individual speakers in your media file.

For more information, see [Partitioning speakers (diarization)](https://docs.aws.amazon.com/transcribe/latest/dg/diarization.html) in the *Amazon Transcribe Developer Guide* .

EnablePartialResultsStabilization -> (boolean)

Enables partial result stabilization for your transcription. Partial result stabilization can reduce latency in your output, but may impact accuracy.

For more information, see [Partial-result stabilization](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization) in the *Amazon Transcribe Developer Guide* .

PartialResultsStability -> (string)

The level of stability to use when you enable partial results stabilization (`EnablePartialResultsStabilization` ).

Low stability provides the highest accuracy. High stability transcribes faster, but with slightly lower accuracy.

For more information, see [Partial-result stabilization](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization) in the *Amazon Transcribe Developer Guide* .

ContentIdentificationType -> (string)

Labels all personally identifiable information (PII) identified in your transcript.

Content identification is performed at the segment level; PII specified in `PiiEntityTypes` is flagged upon complete transcription of an audio segment.

You canât set `ContentIdentificationType` and `ContentRedactionType` in the same request. If you set both, your request returns a `BadRequestException` .

For more information, see [Redacting or identifying personally identifiable information](https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html) in the *Amazon Transcribe Developer Guide* .

ContentRedactionType -> (string)

Redacts all personally identifiable information (PII) identified in your transcript.

Content redaction is performed at the segment level; PII specified in PiiEntityTypes is redacted upon complete transcription of an audio segment.

You canât set ContentRedactionType and ContentIdentificationType in the same request. If you set both, your request returns a `BadRequestException` .

For more information, see [Redacting or identifying personally identifiable information](https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html) in the *Amazon Transcribe Developer Guide* .

PiiEntityTypes -> (string)

The types of personally identifiable information (PII) to redact from a transcript. You can include as many types as youâd like, or you can select `ALL` .

To include `PiiEntityTypes` in your Call Analytics request, you must also include `ContentIdentificationType` or `ContentRedactionType` , but you canât include both.

Values must be comma-separated and can include: `ADDRESS` , `BANK_ACCOUNT_NUMBER` , `BANK_ROUTING` , `CREDIT_DEBIT_CVV` , `CREDIT_DEBIT_EXPIRY` , `CREDIT_DEBIT_NUMBER` , `EMAIL` , `NAME` , `PHONE` , `PIN` , `SSN` , or `ALL` .

If you leave this parameter empty, the default behavior is equivalent to `ALL` .

LanguageModelName -> (string)

The name of the custom language model that you want to use when processing your transcription. Note that language model names are case sensitive.

The language of the specified language model must match the language code you specify in your transcription request. If the languages donât match, the custom language model isnât applied. There are no errors or warnings associated with a language mismatch.

For more information, see [Custom language models](https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html) in the *Amazon Transcribe Developer Guide* .

FilterPartialResults -> (boolean)

If true, `TranscriptEvents` with `IsPartial: true` are filtered out of the insights target.

IdentifyLanguage -> (boolean)

Turns language identification on or off.

IdentifyMultipleLanguages -> (boolean)

Turns language identification on or off for multiple languages.

### Note

Calls to this API must include a `LanguageCode` , `IdentifyLanguage` , or `IdentifyMultipleLanguages` parameter. If you include more than one of those parameters, your transcription job fails.

LanguageOptions -> (string)

The language options for the transcription, such as automatic language detection.

PreferredLanguage -> (string)

The preferred language for the transcription.

VocabularyNames -> (string)

The names of the custom vocabulary or vocabularies used during transcription.

VocabularyFilterNames -> (string)

The names of the custom vocabulary filter or filters using during transcription.

KinesisDataStreamSinkConfiguration -> (structure)

The configuration settings for the Kinesis Data Stream Sink in a media insights pipeline configuration element.

InsightsTarget -> (string)

The ARN of the sink.

S3RecordingSinkConfiguration -> (structure)

The configuration settings for the Amazon S3 recording bucket in a media insights pipeline configuration element.

Destination -> (string)

The default URI of the Amazon S3 bucket used as the recording sink.

RecordingFileFormat -> (string)

The default file format for the media files sent to the Amazon S3 bucket.

VoiceAnalyticsProcessorConfiguration -> (structure)

The voice analytics configuration settings in a media insights pipeline configuration element.

SpeakerSearchStatus -> (string)

The status of the speaker search task.

VoiceToneAnalysisStatus -> (string)

The status of the voice tone analysis task.

LambdaFunctionSinkConfiguration -> (structure)

The configuration settings for the Amazon Web Services Lambda sink in a media insights pipeline configuration element.

InsightsTarget -> (string)

The ARN of the sink.

SqsQueueSinkConfiguration -> (structure)

The configuration settings for an SQS queue sink in a media insights pipeline configuration element.

InsightsTarget -> (string)

The ARN of the SQS sink.

SnsTopicSinkConfiguration -> (structure)

The configuration settings for an SNS topic sink in a media insights pipeline configuration element.

InsightsTarget -> (string)

The ARN of the SNS sink.

VoiceEnhancementSinkConfiguration -> (structure)

The configuration settings for voice enhancement sink in a media insights pipeline configuration element.

Disabled -> (boolean)

Disables the `VoiceEnhancementSinkConfiguration` element.

Shorthand Syntax:

```
Type=string,AmazonTranscribeCallAnalyticsProcessorConfiguration={LanguageCode=string,VocabularyName=string,VocabularyFilterName=string,VocabularyFilterMethod=string,LanguageModelName=string,EnablePartialResultsStabilization=boolean,PartialResultsStability=string,ContentIdentificationType=string,ContentRedactionType=string,PiiEntityTypes=string,FilterPartialResults=boolean,PostCallAnalyticsSettings={OutputLocation=string,DataAccessRoleArn=string,ContentRedactionOutput=string,OutputEncryptionKMSKeyId=string},CallAnalyticsStreamCategories=[string,string]},AmazonTranscribeProcessorConfiguration={LanguageCode=string,VocabularyName=string,VocabularyFilterName=string,VocabularyFilterMethod=string,ShowSpeakerLabel=boolean,EnablePartialResultsStabilization=boolean,PartialResultsStability=string,ContentIdentificationType=string,ContentRedactionType=string,PiiEntityTypes=string,LanguageModelName=string,FilterPartialResults=boolean,IdentifyLanguage=boolean,IdentifyMultipleLanguages=boolean,LanguageOptions=string,PreferredLanguage=string,VocabularyNames=string,VocabularyFilterNames=string},KinesisDataStreamSinkConfiguration={InsightsTarget=string},S3RecordingSinkConfiguration={Destination=string,RecordingFileFormat=string},VoiceAnalyticsProcessorConfiguration={SpeakerSearchStatus=string,VoiceToneAnalysisStatus=string},LambdaFunctionSinkConfiguration={InsightsTarget=string},SqsQueueSinkConfiguration={InsightsTarget=string},SnsTopicSinkConfiguration={InsightsTarget=string},VoiceEnhancementSinkConfiguration={Disabled=boolean} ...
```

JSON Syntax:

```
[
  {
    "Type": "AmazonTranscribeCallAnalyticsProcessor"|"VoiceAnalyticsProcessor"|"AmazonTranscribeProcessor"|"KinesisDataStreamSink"|"LambdaFunctionSink"|"SqsQueueSink"|"SnsTopicSink"|"S3RecordingSink"|"VoiceEnhancementSink",
    "AmazonTranscribeCallAnalyticsProcessorConfiguration": {
      "LanguageCode": "en-US"|"en-GB"|"es-US"|"fr-CA"|"fr-FR"|"en-AU"|"it-IT"|"de-DE"|"pt-BR",
      "VocabularyName": "string",
      "VocabularyFilterName": "string",
      "VocabularyFilterMethod": "remove"|"mask"|"tag",
      "LanguageModelName": "string",
      "EnablePartialResultsStabilization": true|false,
      "PartialResultsStability": "high"|"medium"|"low",
      "ContentIdentificationType": "PII",
      "ContentRedactionType": "PII",
      "PiiEntityTypes": "string",
      "FilterPartialResults": true|false,
      "PostCallAnalyticsSettings": {
        "OutputLocation": "string",
        "DataAccessRoleArn": "string",
        "ContentRedactionOutput": "redacted"|"redacted_and_unredacted",
        "OutputEncryptionKMSKeyId": "string"
      },
      "CallAnalyticsStreamCategories": ["string", ...]
    },
    "AmazonTranscribeProcessorConfiguration": {
      "LanguageCode": "en-US"|"en-GB"|"es-US"|"fr-CA"|"fr-FR"|"en-AU"|"it-IT"|"de-DE"|"pt-BR",
      "VocabularyName": "string",
      "VocabularyFilterName": "string",
      "VocabularyFilterMethod": "remove"|"mask"|"tag",
      "ShowSpeakerLabel": true|false,
      "EnablePartialResultsStabilization": true|false,
      "PartialResultsStability": "high"|"medium"|"low",
      "ContentIdentificationType": "PII",
      "ContentRedactionType": "PII",
      "PiiEntityTypes": "string",
      "LanguageModelName": "string",
      "FilterPartialResults": true|false,
      "IdentifyLanguage": true|false,
      "IdentifyMultipleLanguages": true|false,
      "LanguageOptions": "string",
      "PreferredLanguage": "en-US"|"en-GB"|"es-US"|"fr-CA"|"fr-FR"|"en-AU"|"it-IT"|"de-DE"|"pt-BR",
      "VocabularyNames": "string",
      "VocabularyFilterNames": "string"
    },
    "KinesisDataStreamSinkConfiguration": {
      "InsightsTarget": "string"
    },
    "S3RecordingSinkConfiguration": {
      "Destination": "string",
      "RecordingFileFormat": "Wav"|"Opus"
    },
    "VoiceAnalyticsProcessorConfiguration": {
      "SpeakerSearchStatus": "Enabled"|"Disabled",
      "VoiceToneAnalysisStatus": "Enabled"|"Disabled"
    },
    "LambdaFunctionSinkConfiguration": {
      "InsightsTarget": "string"
    },
    "SqsQueueSinkConfiguration": {
      "InsightsTarget": "string"
    },
    "SnsTopicSinkConfiguration": {
      "InsightsTarget": "string"
    },
    "VoiceEnhancementSinkConfiguration": {
      "Disabled": true|false
    }
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

## Output

MediaInsightsPipelineConfiguration -> (structure)

The updated configuration settings.

MediaInsightsPipelineConfigurationName -> (string)

The name of the configuration.

MediaInsightsPipelineConfigurationArn -> (string)

The ARN of the configuration.

ResourceAccessRoleArn -> (string)

The ARN of the role used by the service to access Amazon Web Services resources.

RealTimeAlertConfiguration -> (structure)

Lists the rules that trigger a real-time alert.

Disabled -> (boolean)

Turns off real-time alerts.

Rules -> (list)

The rules in the alert. Rules specify the words or phrases that you want to be notified about.

(structure)

Specifies the words or phrases that trigger an alert.

Type -> (string)

The type of alert rule.

KeywordMatchConfiguration -> (structure)

Specifies the settings for matching the keywords in a real-time alert rule.

RuleName -> (string)

The name of the keyword match rule.

Keywords -> (list)

The keywords or phrases that you want to match.

(string)

Negate -> (boolean)

Matches keywords or phrases on their presence or absence. If set to `TRUE` , the rule matches when all the specified keywords or phrases are absent. Default: `FALSE` .

SentimentConfiguration -> (structure)

Specifies the settings for predicting sentiment in a real-time alert rule.

RuleName -> (string)

The name of the rule in the sentiment configuration.

SentimentType -> (string)

The type of sentiment, `POSITIVE` , `NEGATIVE` , or `NEUTRAL` .

TimePeriod -> (integer)

Specifies the analysis interval.

IssueDetectionConfiguration -> (structure)

Specifies the issue detection settings for a real-time alert rule.

RuleName -> (string)

The name of the issue detection rule.

Elements -> (list)

The elements in the configuration.

(structure)

An element in a media insights pipeline configuration.

Type -> (string)

The element type.

AmazonTranscribeCallAnalyticsProcessorConfiguration -> (structure)

The analytics configuration settings for transcribing audio in a media insights pipeline configuration element.

LanguageCode -> (string)

The language code in the configuration.

VocabularyName -> (string)

Specifies the name of the custom vocabulary to use when processing a transcription. Note that vocabulary names are case sensitive.

If the language of the specified custom vocabulary doesnât match the language identified in your media, the custom vocabulary is not applied to your transcription.

For more information, see [Custom vocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html) in the *Amazon Transcribe Developer Guide* .

Length Constraints: Minimum length of 1. Maximum length of 200.

VocabularyFilterName -> (string)

Specifies the name of the custom vocabulary filter to use when processing a transcription. Note that vocabulary filter names are case sensitive.

If the language of the specified custom vocabulary filter doesnât match the language identified in your media, the vocabulary filter is not applied to your transcription.

For more information, see [Using vocabulary filtering with unwanted words](https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html) in the *Amazon Transcribe Developer Guide* .

Length Constraints: Minimum length of 1. Maximum length of 200.

VocabularyFilterMethod -> (string)

Specifies how to apply a vocabulary filter to a transcript.

To replace words with ******* , choose `mask` .

To delete words, choose `remove` .

To flag words without changing them, choose `tag` .

LanguageModelName -> (string)

Specifies the name of the custom language model to use when processing a transcription. Note that language model names are case sensitive.

The language of the specified language model must match the language code specified in the transcription request. If the languages donât match, the custom language model isnât applied. Language mismatches donât generate errors or warnings.

For more information, see [Custom language models](https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html) in the *Amazon Transcribe Developer Guide* .

EnablePartialResultsStabilization -> (boolean)

Enables partial result stabilization for your transcription. Partial result stabilization can reduce latency in your output, but may impact accuracy. For more information, see [Partial-result stabilization](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization) in the *Amazon Transcribe Developer Guide* .

PartialResultsStability -> (string)

Specifies the level of stability to use when you enable partial results stabilization (`EnablePartialResultsStabilization` ).

Low stability provides the highest accuracy. High stability transcribes faster, but with slightly lower accuracy.

For more information, see [Partial-result stabilization](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization) in the *Amazon Transcribe Developer Guide* .

ContentIdentificationType -> (string)

Labels all personally identifiable information (PII) identified in your transcript.

Content identification is performed at the segment level; PII specified in `PiiEntityTypes` is flagged upon complete transcription of an audio segment.

You canât set `ContentIdentificationType` and `ContentRedactionType` in the same request. If you do, your request returns a `BadRequestException` .

For more information, see [Redacting or identifying personally identifiable information](https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html) in the *Amazon Transcribe Developer Guide* .

ContentRedactionType -> (string)

Redacts all personally identifiable information (PII) identified in your transcript.

Content redaction is performed at the segment level; PII specified in `PiiEntityTypes` is redacted upon complete transcription of an audio segment.

You canât set `ContentRedactionType` and `ContentIdentificationType` in the same request. If you do, your request returns a `BadRequestException` .

For more information, see [Redacting or identifying personally identifiable information](https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html) in the *Amazon Transcribe Developer Guide* .

PiiEntityTypes -> (string)

Specifies the types of personally identifiable information (PII) to redact from a transcript. You can include as many types as youâd like, or you can select `ALL` .

To include `PiiEntityTypes` in your Call Analytics request, you must also include `ContentIdentificationType` or `ContentRedactionType` , but you canât include both.

Values must be comma-separated and can include: `ADDRESS` , `BANK_ACCOUNT_NUMBER` , `BANK_ROUTING` , `CREDIT_DEBIT_CVV` , `CREDIT_DEBIT_EXPIRY` , `CREDIT_DEBIT_NUMBER` , `EMAIL` , `NAME` , `PHONE` , `PIN` , `SSN` , or `ALL` .

Length Constraints: Minimum length of 1. Maximum length of 300.

FilterPartialResults -> (boolean)

If true, `UtteranceEvents` with `IsPartial: true` are filtered out of the insights target.

PostCallAnalyticsSettings -> (structure)

The settings for a post-call analysis task in an analytics configuration.

OutputLocation -> (string)

The URL of the Amazon S3 bucket that contains the post-call data.

DataAccessRoleArn -> (string)

The ARN of the role used by Amazon Web Services Transcribe to upload your post call analysis. For more information, see [Post-call analytics with real-time transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/tca-post-call.html) in the *Amazon Transcribe Developer Guide* .

ContentRedactionOutput -> (string)

The content redaction output settings for a post-call analysis task.

OutputEncryptionKMSKeyId -> (string)

The ID of the KMS (Key Management Service) key used to encrypt the output.

CallAnalyticsStreamCategories -> (list)

By default, all `CategoryEvents` are sent to the insights target. If this parameter is specified, only included categories are sent to the insights target.

(string)

AmazonTranscribeProcessorConfiguration -> (structure)

The transcription processor configuration settings in a media insights pipeline configuration element.

LanguageCode -> (string)

The language code that represents the language spoken in your audio.

If youâre unsure of the language spoken in your audio, consider using `IdentifyLanguage` to enable automatic language identification.

For a list of languages that real-time Call Analytics supports, see the [Supported languages table](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) in the *Amazon Transcribe Developer Guide* .

VocabularyName -> (string)

The name of the custom vocabulary that you specified in your Call Analytics request.

Length Constraints: Minimum length of 1. Maximum length of 200.

VocabularyFilterName -> (string)

The name of the custom vocabulary filter that you specified in your Call Analytics request.

Length Constraints: Minimum length of 1. Maximum length of 200.

VocabularyFilterMethod -> (string)

The vocabulary filtering method used in your Call Analytics transcription.

ShowSpeakerLabel -> (boolean)

Enables speaker partitioning (diarization) in your transcription output. Speaker partitioning labels the speech from individual speakers in your media file.

For more information, see [Partitioning speakers (diarization)](https://docs.aws.amazon.com/transcribe/latest/dg/diarization.html) in the *Amazon Transcribe Developer Guide* .

EnablePartialResultsStabilization -> (boolean)

Enables partial result stabilization for your transcription. Partial result stabilization can reduce latency in your output, but may impact accuracy.

For more information, see [Partial-result stabilization](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization) in the *Amazon Transcribe Developer Guide* .

PartialResultsStability -> (string)

The level of stability to use when you enable partial results stabilization (`EnablePartialResultsStabilization` ).

Low stability provides the highest accuracy. High stability transcribes faster, but with slightly lower accuracy.

For more information, see [Partial-result stabilization](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization) in the *Amazon Transcribe Developer Guide* .

ContentIdentificationType -> (string)

Labels all personally identifiable information (PII) identified in your transcript.

Content identification is performed at the segment level; PII specified in `PiiEntityTypes` is flagged upon complete transcription of an audio segment.

You canât set `ContentIdentificationType` and `ContentRedactionType` in the same request. If you set both, your request returns a `BadRequestException` .

For more information, see [Redacting or identifying personally identifiable information](https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html) in the *Amazon Transcribe Developer Guide* .

ContentRedactionType -> (string)

Redacts all personally identifiable information (PII) identified in your transcript.

Content redaction is performed at the segment level; PII specified in PiiEntityTypes is redacted upon complete transcription of an audio segment.

You canât set ContentRedactionType and ContentIdentificationType in the same request. If you set both, your request returns a `BadRequestException` .

For more information, see [Redacting or identifying personally identifiable information](https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html) in the *Amazon Transcribe Developer Guide* .

PiiEntityTypes -> (string)

The types of personally identifiable information (PII) to redact from a transcript. You can include as many types as youâd like, or you can select `ALL` .

To include `PiiEntityTypes` in your Call Analytics request, you must also include `ContentIdentificationType` or `ContentRedactionType` , but you canât include both.

Values must be comma-separated and can include: `ADDRESS` , `BANK_ACCOUNT_NUMBER` , `BANK_ROUTING` , `CREDIT_DEBIT_CVV` , `CREDIT_DEBIT_EXPIRY` , `CREDIT_DEBIT_NUMBER` , `EMAIL` , `NAME` , `PHONE` , `PIN` , `SSN` , or `ALL` .

If you leave this parameter empty, the default behavior is equivalent to `ALL` .

LanguageModelName -> (string)

The name of the custom language model that you want to use when processing your transcription. Note that language model names are case sensitive.

The language of the specified language model must match the language code you specify in your transcription request. If the languages donât match, the custom language model isnât applied. There are no errors or warnings associated with a language mismatch.

For more information, see [Custom language models](https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html) in the *Amazon Transcribe Developer Guide* .

FilterPartialResults -> (boolean)

If true, `TranscriptEvents` with `IsPartial: true` are filtered out of the insights target.

IdentifyLanguage -> (boolean)

Turns language identification on or off.

IdentifyMultipleLanguages -> (boolean)

Turns language identification on or off for multiple languages.

### Note

Calls to this API must include a `LanguageCode` , `IdentifyLanguage` , or `IdentifyMultipleLanguages` parameter. If you include more than one of those parameters, your transcription job fails.

LanguageOptions -> (string)

The language options for the transcription, such as automatic language detection.

PreferredLanguage -> (string)

The preferred language for the transcription.

VocabularyNames -> (string)

The names of the custom vocabulary or vocabularies used during transcription.

VocabularyFilterNames -> (string)

The names of the custom vocabulary filter or filters using during transcription.

KinesisDataStreamSinkConfiguration -> (structure)

The configuration settings for the Kinesis Data Stream Sink in a media insights pipeline configuration element.

InsightsTarget -> (string)

The ARN of the sink.

S3RecordingSinkConfiguration -> (structure)

The configuration settings for the Amazon S3 recording bucket in a media insights pipeline configuration element.

Destination -> (string)

The default URI of the Amazon S3 bucket used as the recording sink.

RecordingFileFormat -> (string)

The default file format for the media files sent to the Amazon S3 bucket.

VoiceAnalyticsProcessorConfiguration -> (structure)

The voice analytics configuration settings in a media insights pipeline configuration element.

SpeakerSearchStatus -> (string)

The status of the speaker search task.

VoiceToneAnalysisStatus -> (string)

The status of the voice tone analysis task.

LambdaFunctionSinkConfiguration -> (structure)

The configuration settings for the Amazon Web Services Lambda sink in a media insights pipeline configuration element.

InsightsTarget -> (string)

The ARN of the sink.

SqsQueueSinkConfiguration -> (structure)

The configuration settings for an SQS queue sink in a media insights pipeline configuration element.

InsightsTarget -> (string)

The ARN of the SQS sink.

SnsTopicSinkConfiguration -> (structure)

The configuration settings for an SNS topic sink in a media insights pipeline configuration element.

InsightsTarget -> (string)

The ARN of the SNS sink.

VoiceEnhancementSinkConfiguration -> (structure)

The configuration settings for voice enhancement sink in a media insights pipeline configuration element.

Disabled -> (boolean)

Disables the `VoiceEnhancementSinkConfiguration` element.

MediaInsightsPipelineConfigurationId -> (string)

The ID of the configuration.

CreatedTimestamp -> (timestamp)

The time at which the configuration was created.

UpdatedTimestamp -> (timestamp)

The time at which the configuration was last updated.