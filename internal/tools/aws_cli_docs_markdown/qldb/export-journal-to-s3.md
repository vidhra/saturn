# export-journal-to-s3Â¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/export-journal-to-s3.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/export-journal-to-s3.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qldb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/index.html#cli-aws-qldb) ]

# export-journal-to-s3

## Description

Exports journal contents within a date and time range from a ledger into a specified Amazon Simple Storage Service (Amazon S3) bucket. A journal export job can write the data objects in either the text or binary representation of Amazon Ion format, or in *JSON Lines* text format.

If the ledger with the given `Name` doesnât exist, then throws `ResourceNotFoundException` .

If the ledger with the given `Name` is in `CREATING` status, then throws `ResourcePreconditionNotMetException` .

You can initiate up to two concurrent journal export requests for each ledger. Beyond this limit, journal export requests throw `LimitExceededException` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/ExportJournalToS3)

## Synopsis

```
export-journal-to-s3
--name <value>
--inclusive-start-time <value>
--exclusive-end-time <value>
--s3-export-configuration <value>
--role-arn <value>
[--output-format <value>]
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

The name of the ledger.

`--inclusive-start-time` (timestamp)

The inclusive start date and time for the range of journal contents to export.

The `InclusiveStartTime` must be in `ISO 8601` date and time format and in Universal Coordinated Time (UTC). For example: `2019-06-13T21:36:34Z` .

The `InclusiveStartTime` must be before `ExclusiveEndTime` .

If you provide an `InclusiveStartTime` that is before the ledgerâs `CreationDateTime` , Amazon QLDB defaults it to the ledgerâs `CreationDateTime` .

`--exclusive-end-time` (timestamp)

The exclusive end date and time for the range of journal contents to export.

The `ExclusiveEndTime` must be in `ISO 8601` date and time format and in Universal Coordinated Time (UTC). For example: `2019-06-13T21:36:34Z` .

The `ExclusiveEndTime` must be less than or equal to the current UTC date and time.

`--s3-export-configuration` (structure)

The configuration settings of the Amazon S3 bucket destination for your export request.

Bucket -> (string)

The Amazon S3 bucket name in which a journal export job writes the journal contents.

The bucket name must comply with the Amazon S3 bucket naming conventions. For more information, see [Bucket Restrictions and Limitations](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html) in the *Amazon S3 Developer Guide* .

Prefix -> (string)

The prefix for the Amazon S3 bucket in which a journal export job writes the journal contents.

The prefix must comply with Amazon S3 key naming rules and restrictions. For more information, see [Object Key and Metadata](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html) in the *Amazon S3 Developer Guide* .

The following are examples of valid `Prefix` values:

- `JournalExports-ForMyLedger/Testing/`
- `JournalExports`
- `My:Tests/`

EncryptionConfiguration -> (structure)

The encryption settings that are used by a journal export job to write data in an Amazon S3 bucket.

ObjectEncryptionType -> (string)

The Amazon S3 object encryption type.

To learn more about server-side encryption options in Amazon S3, see [Protecting Data Using Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html) in the *Amazon S3 Developer Guide* .

KmsKeyArn -> (string)

The Amazon Resource Name (ARN) of a symmetric encryption key in Key Management Service (KMS). Amazon S3 does not support asymmetric KMS keys.

You must provide a `KmsKeyArn` if you specify `SSE_KMS` as the `ObjectEncryptionType` .

`KmsKeyArn` is not required if you specify `SSE_S3` as the `ObjectEncryptionType` .

Shorthand Syntax:

```
Bucket=string,Prefix=string,EncryptionConfiguration={ObjectEncryptionType=string,KmsKeyArn=string}
```

JSON Syntax:

```
{
  "Bucket": "string",
  "Prefix": "string",
  "EncryptionConfiguration": {
    "ObjectEncryptionType": "SSE_KMS"|"SSE_S3"|"NO_ENCRYPTION",
    "KmsKeyArn": "string"
  }
}
```

`--role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal export job to do the following:

- Write objects into your Amazon S3 bucket.
- (Optional) Use your customer managed key in Key Management Service (KMS) for server-side encryption of your exported data.

To pass a role to QLDB when requesting a journal export, you must have permissions to perform the `iam:PassRole` action on the IAM role resource. This is required for all journal export requests.

`--output-format` (string)

The output format of your exported journal data. A journal export job can write the data objects in either the text or binary representation of [Amazon Ion](https://docs.aws.amazon.com/qldb/latest/developerguide/ion.html) format, or in [JSON Lines](https://jsonlines.org/) text format.

Default: `ION_TEXT`

In JSON Lines format, each journal block in an exported data object is a valid JSON object that is delimited by a newline. You can use this format to directly integrate JSON exports with analytics tools such as Amazon Athena and Glue because these services can parse newline-delimited JSON automatically.

Possible values:

- `ION_BINARY`
- `ION_TEXT`
- `JSON`

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

**To export journal blocks to S3**

The following `export-journal-to-s3` example creates an export job for journal blocks within a specified date and time range from a ledger with the name `myExampleLedger`. The export job writes the blocks into a specified Amazon S3 bucket.

```
aws qldb export-journal-to-s3 \
    --name myExampleLedger \
    --inclusive-start-time 2019-09-18T00:00:00Z \
    --exclusive-end-time 2019-09-18T22:59:59Z \
    --role-arn arn:aws:iam::123456789012:role/my-s3-export-role \
    --s3-export-configuration file://my-s3-export-config.json
```

Contents of `my-s3-export-config.json`:

```
{
    "Bucket": "amzn-s3-demo-bucket",
    "Prefix": "ledgerexport1/",
    "EncryptionConfiguration": {
        "ObjectEncryptionType": "SSE_S3"
    }
}
```

Output:

```
{
    "ExportId": "ADR2ONPKN5LINYGb4dp7yZ"
}
```

For more information, see [Exporting Your Journal in Amazon QLDB](https://docs.aws.amazon.com/qldb/latest/developerguide/export-journal.html) in the *Amazon QLDB Developer Guide*.

## Output

ExportId -> (string)

The UUID (represented in Base62-encoded text) that QLDB assigns to each journal export job.

To describe your export request and check the status of the job, you can use `ExportId` to call `DescribeJournalS3Export` .