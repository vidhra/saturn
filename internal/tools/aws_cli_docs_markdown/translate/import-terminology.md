# import-terminologyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/import-terminology.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/import-terminology.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [translate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/index.html#cli-aws-translate) ]

# import-terminology

## Description

Creates or updates a custom terminology, depending on whether one already exists for the given terminology name. Importing a terminology with the same name as an existing one will merge the terminologies based on the chosen merge strategy. The only supported merge strategy is OVERWRITE, where the imported terminology overwrites the existing terminology of the same name.

If you import a terminology that overwrites an existing one, the new terminology takes up to 10 minutes to fully propagate. After that, translations have access to the new terminology.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/translate-2017-07-01/ImportTerminology)

## Synopsis

```
import-terminology
--name <value>
--merge-strategy <value>
[--description <value>]
[--terminology-data <value>]
[--encryption-key <value>]
[--tags <value>]
--data-file <value>
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

`--name` (string)

The name of the custom terminology being imported.

`--merge-strategy` (string)

The merge strategy of the custom terminology being imported. Currently, only the OVERWRITE merge strategy is supported. In this case, the imported terminology will overwrite an existing terminology of the same name.

Possible values:

- `OVERWRITE`

`--description` (string)

The description of the custom terminology being imported.

`--terminology-data` (structure)

The terminology data for the custom terminology being imported.

Format -> (string)

The data format of the custom terminology.

Directionality -> (string)

The directionality of your terminology resource indicates whether it has one source language (uni-directional) or multiple (multi-directional).

UNI

The terminology resource has one source language (for example, the first column in a CSV file), and all of its other languages are target languages.

MULTI

Any language in the terminology resource can be the source language or a target language. A single multi-directional terminology resource can be used for jobs that translate different language pairs. For example, if the terminology contains English and Spanish terms, it can be used for jobs that translate English to Spanish and Spanish to English.

When you create a custom terminology resource without specifying the directionality, it behaves as uni-directional terminology, although this parameter will have a null value.

Shorthand Syntax:

```
Format=string,Directionality=string
```

JSON Syntax:

```
{
  "Format": "CSV"|"TMX"|"TSV",
  "Directionality": "UNI"|"MULTI"
}
```

`--encryption-key` (structure)

The encryption key for the custom terminology being imported.

Type -> (string)

The type of encryption key used by Amazon Translate to encrypt this object.

Id -> (string)

The Amazon Resource Name (ARN) of the encryption key being used to encrypt this object.

Shorthand Syntax:

```
Type=string,Id=string
```

JSON Syntax:

```
{
  "Type": "KMS",
  "Id": "string"
}
```

`--tags` (list)

Tags to be associated with this resource. A tag is a key-value pair that adds metadata to a resource. Each tag key for the resource must be unique. For more information, see [Tagging your resources](https://docs.aws.amazon.com/translate/latest/dg/tagging.html) .

(structure)

A key-value pair that adds as a metadata to a resource used by Amazon Translate.

Key -> (string)

The initial part of a key-value pair that forms a tag associated with a given resource.

Value -> (string)

The second part of a key-value pair that forms a tag associated with a given resource.

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

`--data-file` (blob)

The path to the file of the code you are uploading. Example: fileb://data.csv

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

**To import a custom terminology from a file**

The following `import-terminology` example  creates a terminology called `MyTestTerminology` from the `test-terminology.csv` file:

```
aws translate import-terminology \
    --name MyTestTerminology \
    --description "Creating a test terminology in AWS Translate" \
    --merge-strategy OVERWRITE \
    --data-file fileb://test-terminology.csv \
    --terminology-data Format=CSV
```

Contents of `test-terminology.csv`:

en,fr,es,zh
Hello world!,Bonjour tout le monde!,Hola Mundo!,????
Amazon,Amazon,Amazon,Amazon

Output:

```
{
    "TerminologyProperties": {
        "SourceLanguageCode": "en",
        "Name": "MyTestTerminology",
        "TargetLanguageCodes": [
            "fr",
            "es",
            "zh"
        ],
        "SizeBytes": 97,
        "LastUpdatedAt": 1571089500.851,
        "CreatedAt": 1571089500.851,
        "TermCount": 6,
        "Arn": "arn:aws:translate:us-west-2:123456789012:terminology/MyTestTerminology/LATEST",
        "Description": "Creating a test terminology in AWS Translate"
    }
}
```

## Output

TerminologyProperties -> (structure)

The properties of the custom terminology being imported.

Name -> (string)

The name of the custom terminology.

Description -> (string)

The description of the custom terminology properties.

Arn -> (string)

The Amazon Resource Name (ARN) of the custom terminology.

SourceLanguageCode -> (string)

The language code for the source text of the translation request for which the custom terminology is being used.

TargetLanguageCodes -> (list)

The language codes for the target languages available with the custom terminology resource. All possible target languages are returned in array.

(string)

EncryptionKey -> (structure)

The encryption key for the custom terminology.

Type -> (string)

The type of encryption key used by Amazon Translate to encrypt this object.

Id -> (string)

The Amazon Resource Name (ARN) of the encryption key being used to encrypt this object.

SizeBytes -> (integer)

The size of the file used when importing a custom terminology.

TermCount -> (integer)

The number of terms included in the custom terminology.

CreatedAt -> (timestamp)

The time at which the custom terminology was created, based on the timestamp.

LastUpdatedAt -> (timestamp)

The time at which the custom terminology was last update, based on the timestamp.

Directionality -> (string)

The directionality of your terminology resource indicates whether it has one source language (uni-directional) or multiple (multi-directional).

UNI

The terminology resource has one source language (the first column in a CSV file), and all of its other languages are target languages.

MULTI

Any language in the terminology resource can be the source language.

Message -> (string)

Additional information from Amazon Translate about the terminology resource.

SkippedTermCount -> (integer)

The number of terms in the input file that Amazon Translate skipped when you created or updated the terminology resource.

Format -> (string)

The format of the custom terminology input file.

AuxiliaryDataLocation -> (structure)

The Amazon S3 location of a file that provides any errors or warnings that were produced by your input file. This file was created when Amazon Translate attempted to create a terminology resource. The location is returned as a presigned URL to that has a 30 minute expiration.

RepositoryType -> (string)

The repository type for the custom terminology data.

Location -> (string)

The Amazon S3 location of the most recent custom terminology input file that was successfully imported into Amazon Translate. The location is returned as a presigned URL that has a 30-minute expiration .

### Warning

Amazon Translate doesnât scan all input files for the risk of CSV injection attacks.

CSV injection occurs when a .csv or .tsv file is altered so that a record contains malicious code. The record begins with a special character, such as =, +, -, or @. When the file is opened in a spreadsheet program, the program might interpret the record as a formula and run the code within it.

Before you download an input file from Amazon S3, ensure that you recognize the file and trust its creator.