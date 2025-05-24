# translate-documentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/translate-document.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/translate-document.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [translate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/index.html#cli-aws-translate) ]

# translate-document

## Description

Translates the input document from the source language to the target language. This synchronous operation supports text, HTML, or Word documents as the input document. `TranslateDocument` supports translations from English to any supported language, and from any supported language to English. Therefore, specify either the source language code or the target language code as âenâ (English).

If you set the `Formality` parameter, the request will fail if the target language does not support formality. For a list of target languages that support formality, see [Setting formality](https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-formality.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/translate-2017-07-01/TranslateDocument)

## Synopsis

```
translate-document
--document <value>
[--terminology-names <value>]
--source-language-code <value>
--target-language-code <value>
[--settings <value>]
--document-content <value>
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

`--document` (structure)

The content and content type for the document to be translated. The document size must not exceed 100 KB.

ContentType -> (string)

Describes the format of the document. You can specify one of the following:

- `text/html` - The input data consists of HTML content. Amazon Translate translates only the text in the HTML element.
- `text/plain` - The input data consists of unformatted text. Amazon Translate translates every character in the content.
- `application/vnd.openxmlformats-officedocument.wordprocessingml.document` - The input data consists of a Word document (.docx).

Shorthand Syntax:

```
ContentType=string
```

JSON Syntax:

```
{
  "ContentType": "string"
}
```

`--terminology-names` (list)

The name of a terminology list file to add to the translation job. This file provides source terms and the desired translation for each term. A terminology list can contain a maximum of 256 terms. You can use one custom terminology resource in your translation request.

Use the  ListTerminologies operation to get the available terminology lists.

For more information about custom terminology lists, see [Custom terminology](https://docs.aws.amazon.com/translate/latest/dg/how-custom-terminology.html) .

(string)

Syntax:

```
"string" "string" ...
```

`--source-language-code` (string)

The language code for the language of the source text. For a list of supported language codes, see [Supported languages](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html) .

To have Amazon Translate determine the source language of your text, you can specify `auto` in the `SourceLanguageCode` field. If you specify `auto` , Amazon Translate will call [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-general.html) to determine the source language.

### Note

If you specify `auto` , you must send the `TranslateDocument` request in a region that supports Amazon Comprehend. Otherwise, the request returns an error indicating that autodetect is not supported.

`--target-language-code` (string)

The language code requested for the translated document. For a list of supported language codes, see [Supported languages](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html) .

`--settings` (structure)

Settings to configure your translation output. You can configure the following options:

- Brevity: not supported.
- Formality: sets the formality level of the output text.
- Profanity: masks profane words and phrases in your translation output.

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

Shorthand Syntax:

```
Formality=string,Profanity=string,Brevity=string
```

JSON Syntax:

```
{
  "Formality": "FORMAL"|"INFORMAL",
  "Profanity": "MASK",
  "Brevity": "ON"
}
```

`--document-content` (blob)

The path to a file of the content you are uploading Example: fileb://data.txt

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

TranslatedDocument -> (structure)

The document containing the translated content. The document format matches the source document format.

Content -> (blob)

The document containing the translated content.

SourceLanguageCode -> (string)

The language code of the source document.

TargetLanguageCode -> (string)

The language code of the translated document.

AppliedTerminologies -> (list)

The names of the custom terminologies applied to the input text by Amazon Translate to produce the translated text document.

(structure)

The custom terminology applied to the input text by Amazon Translate for the translated text response. This is optional in the response and will only be present if you specified terminology input in the request. Currently, only one terminology can be applied per TranslateText request.

Name -> (string)

The name of the custom terminology applied to the input text by Amazon Translate for the translated text response.

Terms -> (list)

The specific terms of the custom terminology applied to the input text by Amazon Translate for the translated text response. A maximum of 250 terms will be returned, and the specific terms applied will be the first 250 terms in the source text.

(structure)

The term being translated by the custom terminology.

SourceText -> (string)

The source text of the term being translated by the custom terminology.

TargetText -> (string)

The target text of the term being translated by the custom terminology.

AppliedSettings -> (structure)

Settings to configure your translation output. You can configure the following options:

- Brevity: reduces the length of the translation output for most translations. Available for `TranslateText` only.
- Formality: sets the formality level of the translation output.
- Profanity: masks profane words and phrases in the translation output.

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