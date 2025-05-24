# start-speech-synthesis-taskÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/start-speech-synthesis-task.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/start-speech-synthesis-task.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [polly](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/index.html#cli-aws-polly) ]

# start-speech-synthesis-task

## Description

Allows the creation of an asynchronous synthesis task, by starting a new `SpeechSynthesisTask` . This operation requires all the standard information needed for speech synthesis, plus the name of an Amazon S3 bucket for the service to store the output of the synthesis task and two optional parameters (`OutputS3KeyPrefix` and `SnsTopicArn` ). Once the synthesis task is created, this operation will return a `SpeechSynthesisTask` object, which will include an identifier of this task as well as the current status. The `SpeechSynthesisTask` object is available for 72 hours after starting the asynchronous synthesis task.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/StartSpeechSynthesisTask)

## Synopsis

```
start-speech-synthesis-task
[--engine <value>]
[--language-code <value>]
[--lexicon-names <value>]
--output-format <value>
--output-s3-bucket-name <value>
[--output-s3-key-prefix <value>]
[--sample-rate <value>]
[--sns-topic-arn <value>]
[--speech-mark-types <value>]
--text <value>
[--text-type <value>]
--voice-id <value>
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

`--engine` (string)

Specifies the engine (`standard` , `neural` , `long-form` or `generative` ) for Amazon Polly to use when processing input text for speech synthesis. Using a voice that is not supported for the engine selected will result in an error.

Possible values:

- `standard`
- `neural`
- `long-form`
- `generative`

`--language-code` (string)

Optional language code for the Speech Synthesis request. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN).

If a bilingual voice is used and no language code is specified, Amazon Polly uses the default language of the bilingual voice. The default language for any voice is the one returned by the [DescribeVoices](https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html) operation for the `LanguageCode` parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.

Possible values:

- `arb`
- `cmn-CN`
- `cy-GB`
- `da-DK`
- `de-DE`
- `en-AU`
- `en-GB`
- `en-GB-WLS`
- `en-IN`
- `en-US`
- `es-ES`
- `es-MX`
- `es-US`
- `fr-CA`
- `fr-FR`
- `is-IS`
- `it-IT`
- `ja-JP`
- `hi-IN`
- `ko-KR`
- `nb-NO`
- `nl-NL`
- `pl-PL`
- `pt-BR`
- `pt-PT`
- `ro-RO`
- `ru-RU`
- `sv-SE`
- `tr-TR`
- `en-NZ`
- `en-ZA`
- `ca-ES`
- `de-AT`
- `yue-CN`
- `ar-AE`
- `fi-FI`
- `en-IE`
- `nl-BE`
- `fr-BE`
- `cs-CZ`
- `de-CH`
- `en-SG`

`--lexicon-names` (list)

List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice.

(string)

Syntax:

```
"string" "string" ...
```

`--output-format` (string)

The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

Possible values:

- `json`
- `mp3`
- `ogg_vorbis`
- `pcm`

`--output-s3-bucket-name` (string)

Amazon S3 bucket name to which the output file will be saved.

`--output-s3-key-prefix` (string)

The Amazon S3 key prefix for the output speech file.

`--sample-rate` (string)

The audio frequency specified in Hz.

The valid values for mp3 and ogg_vorbis are â8000â, â16000â, â22050â, and â24000â. The default value for standard voices is â22050â. The default value for neural voices is â24000â. The default value for long-form voices is â24000â. The default value for generative voices is â24000â.

Valid values for pcm are â8000â and â16000â The default value is â16000â.

`--sns-topic-arn` (string)

ARN for the SNS topic optionally used for providing status notification for a speech synthesis task.

`--speech-mark-types` (list)

The type of speech marks returned for the input text.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  sentence
  ssml
  viseme
  word
```

`--text` (string)

The input text to synthesize. If you specify ssml as the TextType, follow the SSML format for the input text.

`--text-type` (string)

Specifies whether the input text is plain text or SSML. The default value is plain text.

Possible values:

- `ssml`
- `text`

`--voice-id` (string)

Voice ID to use for the synthesis.

Possible values:

- `Aditi`
- `Amy`
- `Astrid`
- `Bianca`
- `Brian`
- `Camila`
- `Carla`
- `Carmen`
- `Celine`
- `Chantal`
- `Conchita`
- `Cristiano`
- `Dora`
- `Emma`
- `Enrique`
- `Ewa`
- `Filiz`
- `Gabrielle`
- `Geraint`
- `Giorgio`
- `Gwyneth`
- `Hans`
- `Ines`
- `Ivy`
- `Jacek`
- `Jan`
- `Joanna`
- `Joey`
- `Justin`
- `Karl`
- `Kendra`
- `Kevin`
- `Kimberly`
- `Lea`
- `Liv`
- `Lotte`
- `Lucia`
- `Lupe`
- `Mads`
- `Maja`
- `Marlene`
- `Mathieu`
- `Matthew`
- `Maxim`
- `Mia`
- `Miguel`
- `Mizuki`
- `Naja`
- `Nicole`
- `Olivia`
- `Penelope`
- `Raveena`
- `Ricardo`
- `Ruben`
- `Russell`
- `Salli`
- `Seoyeon`
- `Takumi`
- `Tatyana`
- `Vicki`
- `Vitoria`
- `Zeina`
- `Zhiyu`
- `Aria`
- `Ayanda`
- `Arlet`
- `Hannah`
- `Arthur`
- `Daniel`
- `Liam`
- `Pedro`
- `Kajal`
- `Hiujin`
- `Laura`
- `Elin`
- `Ida`
- `Suvi`
- `Ola`
- `Hala`
- `Andres`
- `Sergio`
- `Remi`
- `Adriano`
- `Thiago`
- `Ruth`
- `Stephen`
- `Kazuha`
- `Tomoko`
- `Niamh`
- `Sofie`
- `Lisa`
- `Isabelle`
- `Zayd`
- `Danielle`
- `Gregory`
- `Burcu`
- `Jitka`
- `Sabrina`
- `Jasmine`
- `Jihye`

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

**To synthesize text**

The following `start-speech-synthesis-task` example synthesizes the text in `text_file.txt` and stores the resulting MP3 file in the specified bucket.

```
aws polly start-speech-synthesis-task \
    --output-format mp3 \
    --output-s3-bucket-name amzn-s3-demo-bucket \
    --text  file://text_file.txt \
    --voice-id Joanna
```

Output:

```
{
    "SynthesisTask": {
        "TaskId": "70b61c0f-57ce-4715-a247-cae8729dcce9",
        "TaskStatus": "scheduled",
        "OutputUri": "https://s3.us-east-2.amazonaws.com/amzn-s3-demo-bucket/70b61c0f-57ce-4715-a247-cae8729dcce9.mp3",
        "CreationTime": 1603911042.689,
        "RequestCharacters": 1311,
        "OutputFormat": "mp3",
        "TextType": "text",
        "VoiceId": "Joanna"
    }
}
```

For more information, see [Creating long audio files](https://docs.aws.amazon.com/polly/latest/dg/longer-cli.html) in the *Amazon Polly Developer Guide*.

## Output

SynthesisTask -> (structure)

SynthesisTask object that provides information and attributes about a newly submitted speech synthesis task.

Engine -> (string)

Specifies the engine (`standard` , `neural` , `long-form` or `generative` ) for Amazon Polly to use when processing input text for speech synthesis. Using a voice that is not supported for the engine selected will result in an error.

TaskId -> (string)

The Amazon Polly generated identifier for a speech synthesis task.

TaskStatus -> (string)

Current status of the individual speech synthesis task.

TaskStatusReason -> (string)

Reason for the current status of a specific speech synthesis task, including errors if the task has failed.

OutputUri -> (string)

Pathway for the output speech file.

CreationTime -> (timestamp)

Timestamp for the time the synthesis task was started.

RequestCharacters -> (integer)

Number of billable characters synthesized.

SnsTopicArn -> (string)

ARN for the SNS topic optionally used for providing status notification for a speech synthesis task.

LexiconNames -> (list)

List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice.

(string)

OutputFormat -> (string)

The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

SampleRate -> (string)

The audio frequency specified in Hz.

The valid values for mp3 and ogg_vorbis are â8000â, â16000â, â22050â, and â24000â. The default value for standard voices is â22050â. The default value for neural voices is â24000â. The default value for long-form voices is â24000â. The default value for generative voices is â24000â.

Valid values for pcm are â8000â and â16000â The default value is â16000â.

SpeechMarkTypes -> (list)

The type of speech marks returned for the input text.

(string)

TextType -> (string)

Specifies whether the input text is plain text or SSML. The default value is plain text.

VoiceId -> (string)

Voice ID to use for the synthesis.

LanguageCode -> (string)

Optional language code for a synthesis task. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN).

If a bilingual voice is used and no language code is specified, Amazon Polly uses the default language of the bilingual voice. The default language for any voice is the one returned by the [DescribeVoices](https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html) operation for the `LanguageCode` parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.