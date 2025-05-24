# describe-dashboard-snapshot-job-resultÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-dashboard-snapshot-job-result.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-dashboard-snapshot-job-result.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# describe-dashboard-snapshot-job-result

## Description

Describes the result of an existing snapshot job that has finished running.

A finished snapshot job will return a `COMPLETED` or `FAILED` status when you poll the job with a `DescribeDashboardSnapshotJob` API call.

If the job has not finished running, this operation returns a message that says `Dashboard Snapshot Job with id <SnapshotjobId> has not reached a terminal state.` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/DescribeDashboardSnapshotJobResult)

## Synopsis

```
describe-dashboard-snapshot-job-result
--aws-account-id <value>
--dashboard-id <value>
--snapshot-job-id <value>
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

`--aws-account-id` (string)

The ID of the Amazon Web Services account that the dashboard snapshot job is executed in.

`--dashboard-id` (string)

The ID of the dashboard that you have started a snapshot job for.

`--snapshot-job-id` (string)

The ID of the job to be described. The job ID is set when you start a new job with a `StartDashboardSnapshotJob` API call.

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

Arn -> (string)

The Amazon Resource Name (ARN) for the snapshot job. The job ARN is generated when you start a new job with a `StartDashboardSnapshotJob` API call.

JobStatus -> (string)

Indicates the status of a job after it has reached a terminal state. A finished snapshot job will retuen a `COMPLETED` or `FAILED` status.

CreatedTime -> (timestamp)

The time that a snapshot job was created.

LastUpdatedTime -> (timestamp)

The time that a snapshot job status was last updated.

Result -> (structure)

The result of the snapshot job. Jobs that have successfully completed will return the S3Uri where they are located. Jobs that have failedwill return information on the error that caused the job to fail.

AnonymousUsers -> (list)

A list of `AnonymousUserSnapshotJobResult` objects that contain information on anonymous users and their user configurations. This data provided by you when you make a `StartDashboardSnapshotJob` API call.

(structure)

A structure that contains the file groups that are requested for the artifact generation in a `StartDashboardSnapshotJob` API call.

FileGroups -> (list)

A list of `SnapshotJobResultFileGroup` objects that contain information on the files that are requested during a `StartDashboardSnapshotJob` API call. If the job succeeds, these objects contain the location where the snapshot artifacts are stored. If the job fails, the objects contain information about the error that caused the job to fail.

(structure)

A structure that contains information on the generated snapshot file groups.

Files -> (list)

A list of `SnapshotFile` objects.

(structure)

A structure that contains the information for the snapshot that you want to generate. This information is provided by you when you start a new snapshot job.

SheetSelections -> (list)

A list of `SnapshotFileSheetSelection` objects that contain information on the dashboard sheet that is exported. These objects provide information about the snapshot artifacts that are generated during the job. This structure can hold a maximum of 5 CSV configurations, 5 Excel configurations, or 1 configuration for PDF.

(structure)

A structure that contains information that identifies the snapshot that needs to be generated.

SheetId -> (string)

The sheet ID of the dashboard to generate the snapshot artifact from. This value is required for CSV, Excel, and PDF format types.

SelectionScope -> (string)

The selection scope of the visuals on a sheet of a dashboard that you are generating a snapthot of. You can choose one of the following options.

- `ALL_VISUALS` - Selects all visuals that are on the sheet. This value is required if the snapshot is a PDF.
- `SELECTED_VISUALS` - Select the visual that you want to add to the snapshot. This value is required if the snapshot is a CSV or Excel workbook.

VisualIds -> (list)

A structure that lists the IDs of the visuals in the selected sheet. Supported visual types are table, pivot table visuals. This value is required if you are generating a CSV or Excel workbook. This value supports a maximum of 1 visual ID for CSV and 5 visual IDs across up to 5 sheet selections for Excel. If you are generating an Excel workbook, the order of the visual IDs provided in this structure determines the order of the worksheets in the Excel file.

(string)

FormatType -> (string)

The format of the snapshot file to be generated. You can choose between `CSV` , `Excel` , or `PDF` .

S3Results -> (list)

A list of `SnapshotJobS3Result` objects.

(structure)

The Amazon S3 result from the snapshot job. The result includes the `DestinationConfiguration` and the Amazon S3 Uri. If an error occured during the job, the result returns information on the error.

S3DestinationConfiguration -> (structure)

A list of Amazon S3 bucket configurations that are provided when you make a `StartDashboardSnapshotJob` API call.

BucketConfiguration -> (structure)

A structure that contains details about the Amazon S3 bucket that the generated dashboard snapshot is saved in.

BucketName -> (string)

The name of an existing Amazon S3 bucket where the generated snapshot artifacts are sent.

BucketPrefix -> (string)

The prefix of the Amazon S3 bucket that the generated snapshots are stored in.

BucketRegion -> (string)

The region that the Amazon S3 bucket is located in. The bucket must be located in the same region that the `StartDashboardSnapshotJob` API call is made.

S3Uri -> (string)

The Amazon S3 Uri.

ErrorInfo -> (list)

An array of error records that describe any failures that occur while the dashboard snapshot job runs.

(structure)

Information on the error that caused the snapshot job to fail.

ErrorMessage -> (string)

The error message.

ErrorType -> (string)

The error type.

ErrorInfo -> (structure)

Displays information for the error that caused a job to fail.

ErrorMessage -> (string)

The error message.

ErrorType -> (string)

The error type.

RequestId -> (string)

The Amazon Web Services request ID for this operation.

Status -> (integer)

The HTTP status of the request