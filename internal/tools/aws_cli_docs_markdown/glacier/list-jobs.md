# list-jobsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-jobs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-jobs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glacier](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/index.html#cli-aws-glacier) ]

# list-jobs

## Description

This operation lists jobs for a vault, including jobs that are in-progress and jobs that have recently finished. The List Job operation returns a list of these jobs sorted by job initiation time.

### Note

Amazon Glacier retains recently completed jobs for a period before deleting them; however, it eventually removes completed jobs. The output of completed jobs can be retrieved. Retaining completed jobs for a period of time after they have completed enables you to get a job output in the event you miss the job completion notification or your first attempt to download it fails. For example, suppose you start an archive retrieval job to download an archive. After the job completes, you start to download the archive but encounter a network error. In this scenario, you can retry and download the archive while the job exists.

The List Jobs operation supports pagination. You should always check the response `Marker` field. If there are no more jobs to list, the `Marker` field is set to `null` . If there are more jobs to list, the `Marker` field is set to a non-null value, which you can use to continue the pagination of the list. To return a list of jobs that begins at a specific job, set the marker request parameter to the `Marker` value for that job that you obtained from a previous List Jobs request.

You can set a maximum limit for the number of jobs returned in the response by specifying the `limit` parameter in the request. The default limit is 50. The number of jobs returned might be fewer than the limit, but the number of returned jobs never exceeds the limit.

Additionally, you can filter the jobs list returned by specifying the optional `statuscode` parameter or `completed` parameter, or both. Using the `statuscode` parameter, you can specify to return only jobs that match either the `InProgress` , `Succeeded` , or `Failed` status. Using the `completed` parameter, you can specify to return only jobs that were completed (`true` ) or jobs that were not completed (`false` ).

For more information about using this operation, see the documentation for the underlying REST API [List Jobs](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-jobs-get.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs)

`list-jobs` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `JobList`

## Synopsis

```
list-jobs
--account-id <value>
--vault-name <value>
[--statuscode <value>]
[--completed <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--statuscode` (string)

The type of job status to return. You can specify the following values: `InProgress` , `Succeeded` , or `Failed` .

`--completed` (string)

The state of the jobs to return. You can specify `true` or `false` .

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (string)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (string)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

The following command lists in-progress and recently completed jobs for a vault named `my-vault`:

```
aws glacier list-jobs --account-id - --vault-name my-vault
```

Output:

```
{
    "JobList": [
        {
            "VaultARN": "arn:aws:glacier:us-west-2:0123456789012:vaults/my-vault",
            "RetrievalByteRange": "0-3145727",
            "SNSTopic": "arn:aws:sns:us-west-2:0123456789012:my-vault",
            "Completed": false,
            "SHA256TreeHash": "9628195fcdbcbbe76cdde932d4646fa7de5f219fb39823836d81f0cc0e18aa67",
            "JobId": "l7IL5-EkXyEY9Ws95fClzIbk2O5uLYaFdAYOi-azsX_Z8V6NH4yERHzars8wTKYQMX6nBDI9cMNHzyZJO59-8N9aHWav",
            "ArchiveId": "kKB7ymWJVpPSwhGP6ycSOAekp9ZYe_--zM_mw6k76ZFGEIWQX-ybtRDvc2VkPSDtfKmQrj0IRQLSGsNuDp-AJVlu2ccmDSyDUmZwKbwbpAdGATGDiB3hHO0bjbGehXTcApVud_wyDw",
            "JobDescription": "Retrieve archive on 2015-07-17",
            "ArchiveSizeInBytes": 3145728,
            "Action": "ArchiveRetrieval",
            "ArchiveSHA256TreeHash": "9628195fcdbcbbe76cdde932d4646fa7de5f219fb39823836d81f0cc0e18aa67",
            "CreationDate": "2015-07-17T21:16:13.840Z",
            "StatusCode": "InProgress"
        },
        {
            "InventoryRetrievalParameters": {
                "Format": "JSON"
            },
            "VaultARN": "arn:aws:glacier:us-west-2:0123456789012:vaults/my-vault",
            "Completed": false,
            "JobId": "zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4CnMW",
            "Action": "InventoryRetrieval",
            "CreationDate": "2015-07-17T20:23:41.616Z",
            "StatusCode": ""InProgress""
        }
    ]
}
```

Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account.

## Output

JobList -> (list)

A list of job objects. Each job object contains metadata describing the job.

(structure)

Contains the description of an Amazon S3 Glacier job.

JobId -> (string)

An opaque string that identifies an Amazon S3 Glacier job.

JobDescription -> (string)

The job description provided when initiating the job.

Action -> (string)

The job type. This value is either `ArchiveRetrieval` , `InventoryRetrieval` , or `Select` .

ArchiveId -> (string)

The archive ID requested for a select job or archive retrieval. Otherwise, this field is null.

VaultARN -> (string)

The Amazon Resource Name (ARN) of the vault from which an archive retrieval was requested.

CreationDate -> (string)

The UTC date when the job was created. This value is a string representation of ISO 8601 date format, for example `"2012-03-20T17:03:43.221Z"` .

Completed -> (boolean)

The job status. When a job is completed, you get the jobâs output using Get Job Output (GET output).

StatusCode -> (string)

The status code can be `InProgress` , `Succeeded` , or `Failed` , and indicates the status of the job.

StatusMessage -> (string)

A friendly message that describes the job status.

ArchiveSizeInBytes -> (long)

For an archive retrieval job, this value is the size in bytes of the archive being requested for download. For an inventory retrieval or select job, this value is null.

InventorySizeInBytes -> (long)

For an inventory retrieval job, this value is the size in bytes of the inventory requested for download. For an archive retrieval or select job, this value is null.

SNSTopic -> (string)

An Amazon SNS topic that receives notification.

CompletionDate -> (string)

The UTC time that the job request completed. While the job is in progress, the value is null.

SHA256TreeHash -> (string)

For an archive retrieval job, this value is the checksum of the archive. Otherwise, this value is null.

The SHA256 tree hash value for the requested range of an archive. If the **InitiateJob** request for an archive specified a tree-hash aligned range, then this field returns a value.

If the whole archive is retrieved, this value is the same as the ArchiveSHA256TreeHash value.

This field is null for the following:

- Archive retrieval jobs that specify a range that is not tree-hash aligned
- Archival jobs that specify a range that is equal to the whole archive, when the job status is `InProgress`
- Inventory jobs
- Select jobs

ArchiveSHA256TreeHash -> (string)

The SHA256 tree hash of the entire archive for an archive retrieval. For inventory retrieval or select jobs, this field is null.

RetrievalByteRange -> (string)

The retrieved byte range for archive retrieval jobs in the form *StartByteValue* -*EndByteValue* . If no range was specified in the archive retrieval, then the whole archive is retrieved. In this case, *StartByteValue* equals 0 and *EndByteValue* equals the size of the archive minus 1. For inventory retrieval or select jobs, this field is null.

Tier -> (string)

The tier to use for a select or an archive retrieval. Valid values are `Expedited` , `Standard` , or `Bulk` . `Standard` is the default.

InventoryRetrievalParameters -> (structure)

Parameters used for range inventory retrieval.

Format -> (string)

The output format for the vault inventory list, which is set by the **InitiateJob** request when initiating a job to retrieve a vault inventory. Valid values are `CSV` and `JSON` .

StartDate -> (string)

The start of the date range in Universal Coordinated Time (UTC) for vault inventory retrieval that includes archives created on or after this date. This value should be a string in the ISO 8601 date format, for example `2013-03-20T17:03:43Z` .

EndDate -> (string)

The end of the date range in UTC for vault inventory retrieval that includes archives created before this date. This value should be a string in the ISO 8601 date format, for example `2013-03-20T17:03:43Z` .

Limit -> (string)

The maximum number of inventory items returned per vault inventory retrieval request. This limit is set when initiating the job with the a **InitiateJob** request.

Marker -> (string)

An opaque string that represents where to continue pagination of the vault inventory retrieval results. You use the marker in a new **InitiateJob** request to obtain additional inventory items. If there are no more inventory items, this value is `null` . For more information, see [Range Inventory Retrieval](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html#api-initiate-job-post-vault-inventory-list-filtering) .

JobOutputPath -> (string)

Contains the job output location.

SelectParameters -> (structure)

Contains the parameters used for a select.

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

Contains the location where the data from the select job is stored.

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

Marker -> (string)

An opaque string used for pagination that specifies the job at which the listing of jobs should begin. You get the `marker` value from a previous List Jobs response. You only need to include the marker if you are continuing the pagination of the results started in a previous List Jobs request.