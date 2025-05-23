# get-parallel-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/get-parallel-data.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/get-parallel-data.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [translate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/index.html#cli-aws-translate) ]

# get-parallel-data

## Description

Provides information about a parallel data resource.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/translate-2017-07-01/GetParallelData)

## Synopsis

```
get-parallel-data
--name <value>
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

The name of the parallel data resource that is being retrieved.

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

ParallelDataProperties -> (structure)

The properties of the parallel data resource that is being retrieved.

Name -> (string)

The custom name assigned to the parallel data resource.

Arn -> (string)

The Amazon Resource Name (ARN) of the parallel data resource.

Description -> (string)

The description assigned to the parallel data resource.

Status -> (string)

The status of the parallel data resource. When the parallel data is ready for you to use, the status is `ACTIVE` .

SourceLanguageCode -> (string)

The source language of the translations in the parallel data file.

TargetLanguageCodes -> (list)

The language codes for the target languages available in the parallel data file. All possible target languages are returned as an array.

(string)

ParallelDataConfig -> (structure)

Specifies the format and S3 location of the parallel data input file.

S3Uri -> (string)

The URI of the Amazon S3 folder that contains the parallel data input file. The folder must be in the same Region as the API endpoint you are calling.

Format -> (string)

The format of the parallel data input file.

Message -> (string)

Additional information from Amazon Translate about the parallel data resource.

ImportedDataSize -> (long)

The number of UTF-8 characters that Amazon Translate imported from the parallel data input file. This number includes only the characters in your translation examples. It does not include characters that are used to format your file. For example, if you provided a Translation Memory Exchange (.tmx) file, this number does not include the tags.

ImportedRecordCount -> (long)

The number of records successfully imported from the parallel data input file.

FailedRecordCount -> (long)

The number of records unsuccessfully imported from the parallel data input file.

SkippedRecordCount -> (long)

The number of items in the input file that Amazon Translate skipped when you created or updated the parallel data resource. For example, Amazon Translate skips empty records, empty target texts, and empty lines.

EncryptionKey -> (structure)

The encryption key used to encrypt this object.

Type -> (string)

The type of encryption key used by Amazon Translate to encrypt this object.

Id -> (string)

The Amazon Resource Name (ARN) of the encryption key being used to encrypt this object.

CreatedAt -> (timestamp)

The time at which the parallel data resource was created.

LastUpdatedAt -> (timestamp)

The time at which the parallel data resource was last updated.

LatestUpdateAttemptStatus -> (string)

The status of the most recent update attempt for the parallel data resource.

LatestUpdateAttemptAt -> (timestamp)

The time that the most recent update was attempted.

DataLocation -> (structure)

The Amazon S3 location of the most recent parallel data input file that was successfully imported into Amazon Translate. The location is returned as a presigned URL that has a 30-minute expiration.

### Warning

Amazon Translate doesnât scan all input files for the risk of CSV injection attacks.

CSV injection occurs when a .csv or .tsv file is altered so that a record contains malicious code. The record begins with a special character, such as =, +, -, or @. When the file is opened in a spreadsheet program, the program might interpret the record as a formula and run the code within it.

Before you download an input file from Amazon S3, ensure that you recognize the file and trust its creator.

RepositoryType -> (string)

Describes the repository that contains the parallel data input file.

Location -> (string)

The Amazon S3 location of the parallel data input file. The location is returned as a presigned URL to that has a 30-minute expiration.

### Warning

Amazon Translate doesnât scan all input files for the risk of CSV injection attacks.

CSV injection occurs when a .csv or .tsv file is altered so that a record contains malicious code. The record begins with a special character, such as =, +, -, or @. When the file is opened in a spreadsheet program, the program might interpret the record as a formula and run the code within it.

Before you download an input file from Amazon S3, ensure that you recognize the file and trust its creator.

AuxiliaryDataLocation -> (structure)

The Amazon S3 location of a file that provides any errors or warnings that were produced by your input file. This file was created when Amazon Translate attempted to create a parallel data resource. The location is returned as a presigned URL to that has a 30-minute expiration.

RepositoryType -> (string)

Describes the repository that contains the parallel data input file.

Location -> (string)

The Amazon S3 location of the parallel data input file. The location is returned as a presigned URL to that has a 30-minute expiration.

### Warning

Amazon Translate doesnât scan all input files for the risk of CSV injection attacks.

CSV injection occurs when a .csv or .tsv file is altered so that a record contains malicious code. The record begins with a special character, such as =, +, -, or @. When the file is opened in a spreadsheet program, the program might interpret the record as a formula and run the code within it.

Before you download an input file from Amazon S3, ensure that you recognize the file and trust its creator.

LatestUpdateAttemptAuxiliaryDataLocation -> (structure)

The Amazon S3 location of a file that provides any errors or warnings that were produced by your input file. This file was created when Amazon Translate attempted to update a parallel data resource. The location is returned as a presigned URL to that has a 30-minute expiration.

RepositoryType -> (string)

Describes the repository that contains the parallel data input file.

Location -> (string)

The Amazon S3 location of the parallel data input file. The location is returned as a presigned URL to that has a 30-minute expiration.

### Warning

Amazon Translate doesnât scan all input files for the risk of CSV injection attacks.

CSV injection occurs when a .csv or .tsv file is altered so that a record contains malicious code. The record begins with a special character, such as =, +, -, or @. When the file is opened in a spreadsheet program, the program might interpret the record as a formula and run the code within it.

Before you download an input file from Amazon S3, ensure that you recognize the file and trust its creator.