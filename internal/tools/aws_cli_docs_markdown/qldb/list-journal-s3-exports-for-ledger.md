# list-journal-s3-exports-for-ledgerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/list-journal-s3-exports-for-ledger.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/list-journal-s3-exports-for-ledger.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qldb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/index.html#cli-aws-qldb) ]

# list-journal-s3-exports-for-ledger

## Description

Returns all journal export jobs for a specified ledger.

This action returns a maximum of `MaxResults` items, and is paginated so that you can retrieve all the items by calling `ListJournalS3ExportsForLedger` multiple times.

This action does not return any expired export jobs. For more information, see [Export job expiration](https://docs.aws.amazon.com/qldb/latest/developerguide/export-journal.request.html#export-journal.request.expiration) in the *Amazon QLDB Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/ListJournalS3ExportsForLedger)

## Synopsis

```
list-journal-s3-exports-for-ledger
--name <value>
[--max-results <value>]
[--next-token <value>]
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

`--max-results` (integer)

The maximum number of results to return in a single `ListJournalS3ExportsForLedger` request. (The actual number of results returned might be fewer.)

`--next-token` (string)

A pagination token, indicating that you want to retrieve the next page of results. If you received a value for `NextToken` in the response from a previous `ListJournalS3ExportsForLedger` call, then you should use that value as input here.

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

**To list journal export jobs for a ledger**

The following `list-journal-s3-exports-for-ledger` example lists journal export jobs for the specified ledger.

```
aws qldb list-journal-s3-exports-for-ledger \
    --name myExampleLedger
```

Output:

```
{
    "JournalS3Exports": [
        {
            "LedgerName": "myExampleLedger",
            "ExclusiveEndTime": 1568847599.0,
            "ExportCreationTime": 1568847801.418,
            "S3ExportConfiguration": {
                "Bucket": "amzn-s3-demo-bucket",
                "Prefix": "ledgerexport1/",
                "EncryptionConfiguration": {
                    "ObjectEncryptionType": "SSE_S3"
                }
            },
            "ExportId": "ADR2ONPKN5LINYGb4dp7yZ",
            "RoleArn": "arn:aws:iam::123456789012:role/qldb-s3-export",
            "InclusiveStartTime": 1568764800.0,
            "Status": "IN_PROGRESS"
        }
    ]
}
```

For more information, see [Exporting Your Journal in Amazon QLDB](https://docs.aws.amazon.com/qldb/latest/developerguide/export-journal.html) in the *Amazon QLDB Developer Guide*.

## Output

JournalS3Exports -> (list)

The journal export jobs that are currently associated with the specified ledger.

(structure)

Information about a journal export job, including the ledger name, export ID, creation time, current status, and the parameters of the original export creation request.

LedgerName -> (string)

The name of the ledger.

ExportId -> (string)

The UUID (represented in Base62-encoded text) of the journal export job.

ExportCreationTime -> (timestamp)

The date and time, in epoch time format, when the export job was created. (Epoch time format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

Status -> (string)

The current state of the journal export job.

InclusiveStartTime -> (timestamp)

The inclusive start date and time for the range of journal contents that was specified in the original export request.

ExclusiveEndTime -> (timestamp)

The exclusive end date and time for the range of journal contents that was specified in the original export request.

S3ExportConfiguration -> (structure)

The Amazon Simple Storage Service (Amazon S3) bucket location in which a journal export job writes the journal contents.

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

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal export job to do the following:

- Write objects into your Amazon Simple Storage Service (Amazon S3) bucket.
- (Optional) Use your customer managed key in Key Management Service (KMS) for server-side encryption of your exported data.

OutputFormat -> (string)

The output format of the exported journal data.

NextToken -> (string)

- If `NextToken` is empty, then the last page of results has been processed and there are no more results to be retrieved.
- If `NextToken` is *not* empty, then there are more results available. To retrieve the next page of results, use the value of `NextToken` in a subsequent `ListJournalS3ExportsForLedger` call.