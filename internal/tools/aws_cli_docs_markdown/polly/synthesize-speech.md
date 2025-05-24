# synthesize-speechÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/synthesize-speech.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/synthesize-speech.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [polly](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/index.html#cli-aws-polly) ]

# synthesize-speech

## Description

Synthesizes UTF-8 input, plain text or SSML, to a stream of bytes. SSML input must be valid, well-formed SSML. Some alphabets might not be available with all the voices (for example, Cyrillic might not be read at all by English voices) unless phoneme mapping is used. For more information, see [How it Works](https://docs.aws.amazon.com/polly/latest/dg/how-text-to-speech-works.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/SynthesizeSpeech)

## Synopsis

```
synthesize-speech
[--engine <value>]
[--language-code <value>]
[--lexicon-names <value>]
--output-format <value>
[--sample-rate <value>]
[--speech-mark-types <value>]
--text <value>
[--text-type <value>]
--voice-id <value>
<outfile>
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

Specifies the engine (`standard` , `neural` , `long-form` , or `generative` ) for Amazon Polly to use when processing input text for speech synthesis. Provide an engine that is supported by the voice you select. If you donât provide an engine, the standard engine is selected by default. If a chosen voice isnât supported by the standard engine, this will result in an error. For information on Amazon Polly voices and which voices are available for each engine, see [Available Voices](https://docs.aws.amazon.com/polly/latest/dg/voicelist.html) .

Type: String

Valid Values: `standard` | `neural` | `long-form` | `generative`

Required: Yes

Possible values:

- `standard`
- `neural`
- `long-form`
- `generative`

`--language-code` (string)

Optional language code for the Synthesize Speech request. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN).

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

List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. For information about storing lexicons, see [PutLexicon](https://docs.aws.amazon.com/polly/latest/dg/API_PutLexicon.html) .

(string)

Syntax:

```
"string" "string" ...
```

`--output-format` (string)

The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

When pcm is used, the content returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format.

Possible values:

- `json`
- `mp3`
- `ogg_vorbis`
- `pcm`

`--sample-rate` (string)

The audio frequency specified in Hz.

The valid values for mp3 and ogg_vorbis are â8000â, â16000â, â22050â, and â24000â. The default value for standard voices is â22050â. The default value for neural voices is â24000â. The default value for long-form voices is â24000â. The default value for generative voices is â24000â.

Valid values for pcm are â8000â and â16000â The default value is â16000â.

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

Input text to synthesize. If you specify `ssml` as the `TextType` , follow the SSML format for the input text.

`--text-type` (string)

Specifies whether the input text is plain text or SSML. The default value is plain text. For more information, see [Using SSML](https://docs.aws.amazon.com/polly/latest/dg/ssml.html) .

Possible values:

- `ssml`
- `text`

`--voice-id` (string)

Voice ID to use for the synthesis. You can get a list of available voice IDs by calling the [DescribeVoices](https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html) operation.

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

`outfile` (string)
Filename where the content will be saved

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

AudioStream -> (streaming blob)

Stream containing the synthesized speech.

ContentType -> (string)

Specifies the type audio stream. This should reflect the `OutputFormat` parameter in your request.

- If you request `mp3` as the `OutputFormat` , the `ContentType` returned is audio/mpeg.
- If you request `ogg_vorbis` as the `OutputFormat` , the `ContentType` returned is audio/ogg.
- If you request `pcm` as the `OutputFormat` , the `ContentType` returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format.
- If you request `json` as the `OutputFormat` , the `ContentType` returned is application/x-json-stream.

RequestCharacters -> (integer)

Number of characters synthesized.