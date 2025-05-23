# initiate-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/initiate-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/initiate-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glacier](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/index.html#cli-aws-glacier) ]

# initiate-job

## Description

This operation initiates a job of the specified type, which can be a select, an archival retrieval, or a vault retrieval. For more information about using this operation, see the documentation for the underlying REST API [Initiate a Job](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/InitiateJob)

## Synopsis

```
initiate-job
--account-id <value>
--vault-name <value>
[--job-parameters <value>]
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

`--account-id` (string)

The `AccountId` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single â`-` â (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (â-â) in the ID.

`--vault-name` (string)

The name of the vault.

`--job-parameters` (structure)

Provides options for specifying job information.

Format -> (string)

When initiating a job to retrieve a vault inventory, you can optionally add this parameter to your request to specify the output format. If you are initiating an inventory job and do not specify a Format field, JSON is the default format. Valid values are âCSVâ and âJSONâ.

Type -> (string)

The job type. You can initiate a job to perform a select query on an archive, retrieve an archive, or get an inventory of a vault. Valid values are âselectâ, âarchive-retrievalâ and âinventory-retrievalâ.

ArchiveId -> (string)

The ID of the archive that you want to retrieve. This field is required only if `Type` is set to `select` or `archive-retrieval` code>. An error occurs if you specify this request parameter for an inventory retrieval job request.

Description -> (string)

The optional description for the job. The description must be less than or equal to 1,024 bytes. The allowable characters are 7-bit ASCII without control codes-specifically, ASCII values 32-126 decimal or 0x20-0x7E hexadecimal.

SNSTopic -> (string)

The Amazon SNS topic ARN to which Amazon S3 Glacier sends a notification when the job is completed and the output is ready for you to download. The specified topic publishes the notification to its subscribers. The SNS topic must exist.

RetrievalByteRange -> (string)

The byte range to retrieve for an archive retrieval. in the form â*StartByteValue* -*EndByteValue* â If not specified, the whole archive is retrieved. If specified, the byte range must be megabyte (1024*1024) aligned which means that *StartByteValue* must be divisible by 1 MB and *EndByteValue* plus 1 must be divisible by 1 MB or be the end of the archive specified as the archive byte size value minus 1. If RetrievalByteRange is not megabyte aligned, this operation returns a 400 response.

An error occurs if you specify this field for an inventory retrieval job request.

Tier -> (string)

The tier to use for a select or an archive retrieval job. Valid values are `Expedited` , `Standard` , or `Bulk` . `Standard` is the default.

InventoryRetrievalParameters -> (structure)

Input parameters used for range inventory retrieval.

StartDate -> (string)

The start of the date range in UTC for vault inventory retrieval that includes archives created on or after this date. This value should be a string in the ISO 8601 date format, for example `2013-03-20T17:03:43Z` .

EndDate -> (string)

The end of the date range in UTC for vault inventory retrieval that includes archives created before this date. This value should be a string in the ISO 8601 date format, for example `2013-03-20T17:03:43Z` .

Limit -> (string)

Specifies the maximum number of inventory items returned per vault inventory retrieval request. Valid values are greater than or equal to 1.

Marker -> (string)

An opaque string that represents where to continue pagination of the vault inventory retrieval results. You use the marker in a new **InitiateJob** request to obtain additional inventory items. If there are no more inventory items, this value is `null` .

SelectParameters -> (structure)

Contains the parameters that define a job.

InputSerialization -> (structure)

Describes the serialization format of the object.

csv -> (structure)

Describes the serialization of a CSV-encoded object.

FileHeaderInfo -> (string)

Describes the first line of input. Valid values are `None` , `Ignore` , and `Use` .

Comments -> (string)

A single character used to indicate that a row should be ignored when the character is present at the start of that row.

QuoteEscapeCharacter -> (string)

A single character used for escaping the quotation-mark character inside an already escaped value.

RecordDelimiter -> (string)

A value used to separate individual records from each other.

FieldDelimiter -> (string)

A value used to separate individual fields from each other within a record.

QuoteCharacter -> (string)

A value used as an escape character where the field delimiter is part of the value.

ExpressionType -> (string)

The type of the provided expression, for example `SQL` .

Expression -> (string)

The expression that is used to select the object.

OutputSerialization -> (structure)

Describes how the results of the select job are serialized.

csv -> (structure)

Describes the serialization of CSV-encoded query results.

QuoteFields -> (string)

A value that indicates whether all output fields should be contained within quotation marks.

QuoteEscapeCharacter -> (string)

A single character used for escaping the quotation-mark character inside an already escaped value.

RecordDelimiter -> (string)

A value used to separate individual records from each other.

FieldDelimiter -> (string)

A value used to separate individual fields from each other within a record.

QuoteCharacter -> (string)

A value used as an escape character where the field delimiter is part of the value.

OutputLocation -> (structure)

Contains information about the location where the select job results are stored.

S3 -> (structure)

Describes an S3 location that will receive the results of the job request.

BucketName -> (string)

The name of the Amazon S3 bucket where the job results are stored.

Prefix -> (string)

The prefix that is prepended to the results for this request.

Encryption -> (structure)

Contains information about the encryption used to store the job results in Amazon S3.

EncryptionType -> (string)

The server-side encryption algorithm used when storing job results in Amazon S3, for example `AES256` or `aws:kms` .

KMSKeyId -> (string)

The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature Version 4.

KMSContext -> (string)

Optional. If the encryption type is `aws:kms` , you can use this value to specify the encryption context for the job results.

CannedACL -> (string)

The canned access control list (ACL) to apply to the job results.

AccessControlList -> (list)

A list of grants that control access to the staged results.

(structure)

Contains information about a grant.

Grantee -> (structure)

The grantee.

Type -> (string)

Type of grantee

DisplayName -> (string)

Screen name of the grantee.

URI -> (string)

URI of the grantee group.

ID -> (string)

The canonical user ID of the grantee.

EmailAddress -> (string)

Email address of the grantee.

Permission -> (string)

Specifies the permission given to the grantee.

Tagging -> (map)

The tag-set that is applied to the job results.

key -> (string)

value -> (string)

UserMetadata -> (map)

A map of metadata to store with the job results in Amazon S3.

key -> (string)

value -> (string)

StorageClass -> (string)

The storage class used to store the job results.

JSON Syntax:

```
{
  "Format": "string",
  "Type": "string",
  "ArchiveId": "string",
  "Description": "string",
  "SNSTopic": "string",
  "RetrievalByteRange": "string",
  "Tier": "string",
  "InventoryRetrievalParameters": {
    "StartDate": "string",
    "EndDate": "string",
    "Limit": "string",
    "Marker": "string"
  },
  "SelectParameters": {
    "InputSerialization": {
      "csv": {
        "FileHeaderInfo": "USE"|"IGNORE"|"NONE",
        "Comments": "string",
        "QuoteEscapeCharacter": "string",
        "RecordDelimiter": "string",
        "FieldDelimiter": "string",
        "QuoteCharacter": "string"
      }
    },
    "ExpressionType": "SQL",
    "Expression": "string",
    "OutputSerialization": {
      "csv": {
        "QuoteFields": "ALWAYS"|"ASNEEDED",
        "QuoteEscapeCharacter": "string",
        "RecordDelimiter": "string",
        "FieldDelimiter": "string",
        "QuoteCharacter": "string"
      }
    }
  },
  "OutputLocation": {
    "S3": {
      "BucketName": "string",
      "Prefix": "string",
      "Encryption": {
        "EncryptionType": "aws:kms"|"AES256",
        "KMSKeyId": "string",
        "KMSContext": "string"
      },
      "CannedACL": "private"|"public-read"|"public-read-write"|"aws-exec-read"|"authenticated-read"|"bucket-owner-read"|"bucket-owner-full-control",
      "AccessControlList": [
        {
          "Grantee": {
            "Type": "AmazonCustomerByEmail"|"CanonicalUser"|"Group",
            "DisplayName": "string",
            "URI": "string",
            "ID": "string",
            "EmailAddress": "string"
          },
          "Permission": "FULL_CONTROL"|"WRITE"|"WRITE_ACP"|"READ"|"READ_ACP"
        }
        ...
      ],
      "Tagging": {"string": "string"
        ...},
      "UserMetadata": {"string": "string"
        ...},
      "StorageClass": "STANDARD"|"REDUCED_REDUNDANCY"|"STANDARD_IA"
    }
  }
}
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

The following command initiates a job to get an inventory of the vault `my-vault`:

```
aws glacier initiate-job --account-id - --vault-name my-vault --job-parameters '{"Type": "inventory-retrieval"}'
```

Output:

```
{
    "location": "/0123456789012/vaults/my-vault/jobs/zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4CnMW",
    "jobId": "zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4CnMW"
}
```

Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account.

The following command initiates a job to retrieve an archive from the vault `my-vault`:

```
aws glacier initiate-job --account-id - --vault-name my-vault --job-parameters file://job-archive-retrieval.json
```

`job-archive-retrieval.json` is a JSON file in the local folder that specifies the type of job, archive ID, and some optional parameters:

```
{
  "Type": "archive-retrieval",
  "ArchiveId": "kKB7ymWJVpPSwhGP6ycSOAekp9ZYe_--zM_mw6k76ZFGEIWQX-ybtRDvc2VkPSDtfKmQrj0IRQLSGsNuDp-AJVlu2ccmDSyDUmZwKbwbpAdGATGDiB3hHO0bjbGehXTcApVud_wyDw",
  "Description": "Retrieve archive on 2015-07-17",
  "SNSTopic": "arn:aws:sns:us-west-2:0123456789012:my-topic"
}
```

Archive IDs are available in the output of `aws glacier upload-archive` and `aws glacier get-job-output`.

Output:

```
{
    "location": "/011685312445/vaults/mwunderl/jobs/l7IL5-EkXyEY9Ws95fClzIbk2O5uLYaFdAYOi-azsX_Z8V6NH4yERHzars8wTKYQMX6nBDI9cMNHzyZJO59-8N9aHWav",
    "jobId": "l7IL5-EkXy2O5uLYaFdAYOiEY9Ws95fClzIbk-azsX_Z8V6NH4yERHzars8wTKYQMX6nBDI9cMNHzyZJO59-8N9aHWav"
}
```

See [Initiate Job](http://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html) in the *Amazon Glacier API Reference* for details on the job parameters format.

## Output

location -> (string)

The relative URI path of the job.

jobId -> (string)

The ID of the job.

jobOutputPath -> (string)

The path to the location of where the select results are stored.