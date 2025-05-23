# list-data-source-sync-jobsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/list-data-source-sync-jobs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/list-data-source-sync-jobs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# list-data-source-sync-jobs

## Description

Gets statistics about synchronizing a data source connector.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/ListDataSourceSyncJobs)

## Synopsis

```
list-data-source-sync-jobs
--id <value>
--index-id <value>
[--next-token <value>]
[--max-results <value>]
[--start-time-filter <value>]
[--status-filter <value>]
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

`--id` (string)

The identifier of the data source connector.

`--index-id` (string)

The identifier of the index used with the data source connector.

`--next-token` (string)

If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of jobs.

`--max-results` (integer)

The maximum number of synchronization jobs to return in the response. If there are fewer results in the list, this response contains only the actual results.

`--start-time-filter` (structure)

When specified, the synchronization jobs returned in the list are limited to jobs between the specified dates.

StartTime -> (timestamp)

The Unix timestamp for the beginning of the time range.

EndTime -> (timestamp)

The Unix timestamp for the end of the time range.

Shorthand Syntax:

```
StartTime=timestamp,EndTime=timestamp
```

JSON Syntax:

```
{
  "StartTime": timestamp,
  "EndTime": timestamp
}
```

`--status-filter` (string)

Only returns synchronization jobs with the `Status` field equal to the specified status.

Possible values:

- `FAILED`
- `SUCCEEDED`
- `SYNCING`
- `INCOMPLETE`
- `STOPPING`
- `ABORTED`
- `SYNCING_INDEXING`

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

History -> (list)

A history of synchronization jobs for the data source connector.

(structure)

Provides information about a data source synchronization job.

ExecutionId -> (string)

A identifier for the synchronization job.

StartTime -> (timestamp)

The Unix timestamp when the synchronization job started.

EndTime -> (timestamp)

The Unix timestamp when the synchronization job completed.

Status -> (string)

The execution status of the synchronization job. When the `Status` field is set to `SUCCEEDED` , the synchronization job is done. If the status code is set to `FAILED` , the `ErrorCode` and `ErrorMessage` fields give you the reason for the failure.

ErrorMessage -> (string)

If the `Status` field is set to `ERROR` , the `ErrorMessage` field contains a description of the error that caused the synchronization to fail.

ErrorCode -> (string)

If the `Status` field is set to `FAILED` , the `ErrorCode` field indicates the reason the synchronization failed.

DataSourceErrorCode -> (string)

If the reason that the synchronization failed is due to an error with the underlying data source, this field contains a code that identifies the error.

Metrics -> (structure)

Maps a batch delete document request to a specific data source sync job. This is optional and should only be supplied when documents are deleted by a data source connector.

DocumentsAdded -> (string)

The number of documents added from the data source up to now in the data source sync.

DocumentsModified -> (string)

The number of documents modified in the data source up to now in the data source sync run.

DocumentsDeleted -> (string)

The number of documents deleted from the data source up to now in the data source sync run.

DocumentsFailed -> (string)

The number of documents that failed to sync from the data source up to now in the data source sync run.

DocumentsScanned -> (string)

The current number of documents crawled by the current sync job in the data source.

NextToken -> (string)

If the response is truncated, Amazon Kendra returns this token that you can use in the subsequent request to retrieve the next set of jobs.