# describe-text-translation-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/describe-text-translation-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/describe-text-translation-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [translate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/index.html#cli-aws-translate) ]

# describe-text-translation-job

## Description

Gets the properties associated with an asynchronous batch translation job including name, ID, status, source and target languages, input/output S3 buckets, and so on.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/translate-2017-07-01/DescribeTextTranslationJob)

## Synopsis

```
describe-text-translation-job
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

The identifier that Amazon Translate generated for the job. The  StartTextTranslationJob operation returns this identifier in its response.

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

TextTranslationJobProperties -> (structure)

An object that contains the properties associated with an asynchronous batch translation job.

JobId -> (string)

The ID of the translation job.

JobName -> (string)

The user-defined name of the translation job.

JobStatus -> (string)

The status of the translation job.

JobDetails -> (structure)

The number of documents successfully and unsuccessfully processed during the translation job.

TranslatedDocumentsCount -> (integer)

The number of documents successfully processed during a translation job.

DocumentsWithErrorsCount -> (integer)

The number of documents that could not be processed during a translation job.

InputDocumentsCount -> (integer)

The number of documents used as input in a translation job.

SourceLanguageCode -> (string)

The language code of the language of the source text. The language must be a language supported by Amazon Translate.

TargetLanguageCodes -> (list)

The language code of the language of the target text. The language must be a language supported by Amazon Translate.

(string)

TerminologyNames -> (list)

A list containing the names of the terminologies applied to a translation job. Only one terminology can be applied per  StartTextTranslationJob request at this time.

(string)

ParallelDataNames -> (list)

A list containing the names of the parallel data resources applied to the translation job.

(string)

Message -> (string)

An explanation of any errors that may have occurred during the translation job.

SubmittedTime -> (timestamp)

The time at which the translation job was submitted.

EndTime -> (timestamp)

The time at which the translation job ended.

InputDataConfig -> (structure)

The input configuration properties that were specified when the job was requested.

S3Uri -> (string)

The URI of the AWS S3 folder that contains the input files. Amazon Translate translates all the files in the folder and all its sub-folders. The folder must be in the same Region as the API endpoint you are calling.

ContentType -> (string)

Describes the format of the data that you submit to Amazon Translate as input. You can specify one of the following multipurpose internet mail extension (MIME) types:

- `text/html` : The input data consists of one or more HTML files. Amazon Translate translates only the text that resides in the `html` element in each file.
- `text/plain` : The input data consists of one or more unformatted text files. Amazon Translate translates every character in this type of input.
- `application/vnd.openxmlformats-officedocument.wordprocessingml.document` : The input data consists of one or more Word documents (.docx).
- `application/vnd.openxmlformats-officedocument.presentationml.presentation` : The input data consists of one or more PowerPoint Presentation files (.pptx).
- `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` : The input data consists of one or more Excel Workbook files (.xlsx).
- `application/x-xliff+xml` : The input data consists of one or more XML Localization Interchange File Format (XLIFF) files (.xlf). Amazon Translate supports only XLIFF version 1.2.

### Warning

If you structure your input data as HTML, ensure that you set this parameter to `text/html` . By doing so, you cut costs by limiting the translation to the contents of the `html` element in each file. Otherwise, if you set this parameter to `text/plain` , your costs will cover the translation of every character.

OutputDataConfig -> (structure)

The output configuration properties that were specified when the job was requested.

S3Uri -> (string)

The URI of the S3 folder that contains a translation jobâs output file. The folder must be in the same Region as the API endpoint that you are calling.

EncryptionKey -> (structure)

The encryption key used to encrypt this object.

Type -> (string)

The type of encryption key used by Amazon Translate to encrypt this object.

Id -> (string)

The Amazon Resource Name (ARN) of the encryption key being used to encrypt this object.

DataAccessRoleArn -> (string)

The Amazon Resource Name (ARN) of an AWS Identity Access and Management (IAM) role that granted Amazon Translate read access to the jobâs input data.

Settings -> (structure)

Settings that modify the translation output.

Formality -> (string)

You can specify the desired level of formality for translations to supported target languages. The formality setting controls the level of formal language usage (also known as [register](https://en.wikipedia.org/wiki/Register_(sociolinguistics)) ) in the translation output. You can set the value to informal or formal. If you donât specify a value for formality, or if the target language doesnât support formality, the translation will ignore the formality setting.

If you specify multiple target languages for the job, translate ignores the formality setting for any unsupported target language.

For a list of target languages that support formality, see [Supported languages](https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-formality.html#customizing-translations-formality-languages) in the Amazon Translate Developer Guide.

Profanity -> (string)

You can enable the profanity setting if you want to mask profane words and phrases in your translation output.

To mask profane words and phrases, Amazon Translate replaces them with the grawlix string â?$#@$â. This 5-character sequence is used for each profane word or phrase, regardless of the length or number of words.

Amazon Translate doesnât detect profanity in all of its supported languages. For languages that donât support profanity detection, see [Unsupported languages](https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-profanity.html#customizing-translations-profanity-languages) in the Amazon Translate Developer Guide.

If you specify multiple target languages for the job, all the target languages must support profanity masking. If any of the target languages donât support profanity masking, the translation job wonât mask profanity for any target language.

Brevity -> (string)

When you turn on brevity, Amazon Translate reduces the length of the translation output for most translations (when compared with the same translation with brevity turned off). By default, brevity is turned off.

If you turn on brevity for a translation request with an unsupported language pair, the translation proceeds with the brevity setting turned off.

For the language pairs that brevity supports, see [Using brevity](https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-brevity) in the Amazon Translate Developer Guide.