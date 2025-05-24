# create-vocabulary-filterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/create-vocabulary-filter.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/create-vocabulary-filter.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transcribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/index.html#cli-aws-transcribe) ]

# create-vocabulary-filter

## Description

Creates a new custom vocabulary filter.

You can use custom vocabulary filters to mask, delete, or flag specific words from your transcript. Custom vocabulary filters are commonly used to mask profanity in transcripts.

Each language has a character set that contains all allowed characters for that specific language. If you use unsupported characters, your custom vocabulary filter request fails. Refer to [Character Sets for Custom Vocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html) to get the character set for your language.

For more information, see [Vocabulary filtering](https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/CreateVocabularyFilter)

## Synopsis

```
create-vocabulary-filter
--vocabulary-filter-name <value>
--language-code <value>
[--words <value>]
[--vocabulary-filter-file-uri <value>]
[--tags <value>]
[--data-access-role-arn <value>]
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

`--vocabulary-filter-name` (string)

A unique name, chosen by you, for your new custom vocabulary filter.

This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account. If you try to create a new custom vocabulary filter with the same name as an existing custom vocabulary filter, you get a `ConflictException` error.

`--language-code` (string)

The language code that represents the language of the entries in your vocabulary filter. Each custom vocabulary filter must contain terms in only one language.

A custom vocabulary filter can only be used to transcribe files in the same language as the filter. For example, if you create a custom vocabulary filter using US English (`en-US` ), you can only apply this filter to files that contain English audio.

For a list of supported languages and their associated language codes, refer to the [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) table.

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

`--words` (list)

Use this parameter if you want to create your custom vocabulary filter by including all desired terms, as comma-separated values, within your request. The other option for creating your vocabulary filter is to save your entries in a text file and upload them to an Amazon S3 bucket, then specify the location of your file using the `VocabularyFilterFileUri` parameter.

Note that if you include `Words` in your request, you cannot use `VocabularyFilterFileUri` ; you must choose one or the other.

Each language has a character set that contains all allowed characters for that specific language. If you use unsupported characters, your custom vocabulary filter request fails. Refer to [Character Sets for Custom Vocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html) to get the character set for your language.

(string)

Syntax:

```
"string" "string" ...
```

`--vocabulary-filter-file-uri` (string)

The Amazon S3 location of the text file that contains your custom vocabulary filter terms. The URI must be located in the same Amazon Web Services Region as the resource youâre calling.

Hereâs an example URI path: `s3://DOC-EXAMPLE-BUCKET/my-vocab-filter-file.txt`

Note that if you include `VocabularyFilterFileUri` in your request, you cannot use `Words` ; you must choose one or the other.

`--tags` (list)

Adds one or more custom tags, each in the form of a key:value pair, to a new custom vocabulary filter at the time you create this new vocabulary filter.

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

`--data-access-role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files (in this case, your custom vocabulary filter). If the role that you specify doesnât have the appropriate permissions to access the specified Amazon S3 location, your request fails.

IAM role ARNs have the format `arn:partition:iam::account:role/role-name-with-path` . For example: `arn:aws:iam::111122223333:role/Admin` .

For more information, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns) .

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

**To create a vocabulary filter**

The following `create-vocabulary-filter` example creates a vocabulary filter that uses a text file that contains a list of words that you wouldnât want to appear in a transcription. For language-code, specify the language code corresponding to the language of your vocabulary filter. For vocabulary-filter-file-uri, specify the Amazon Simple Storage Service (Amazon S3) URI of the text file. For vocabulary-filter-name, specify the name of your vocabulary filter.

```
aws transcribe create-vocabulary-filter \
    --language-code language-code \
    --vocabulary-filter-file-uri s3://amzn-s3-demo-bucket/vocabulary-filter.txt \
    --vocabulary-filter-name cli-vocabulary-filter-example
```

Output:

```
{
    "VocabularyFilterName": "cli-vocabulary-filter-example",
    "LanguageCode": "language-code"
}
```

For more information, see [Filtering Unwanted Words](https://docs.aws.amazon.com/transcribe/latest/dg/filter-unwanted-words.html) in the *Amazon Transcribe Developer Guide*.

## Output

VocabularyFilterName -> (string)

The name you chose for your custom vocabulary filter.

LanguageCode -> (string)

The language code you selected for your custom vocabulary filter.

LastModifiedTime -> (timestamp)

The date and time you created your custom vocabulary filter.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:32:58.761000-07:00` represents 12:32 PM UTC-7 on May 4, 2022.