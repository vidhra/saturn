# start-dashboard-snapshot-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/start-dashboard-snapshot-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/start-dashboard-snapshot-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# start-dashboard-snapshot-job

## Description

Starts an asynchronous job that generates a snapshot of a dashboardâs output. You can request one or several of the following format configurations in each API call.

- 1 Paginated PDF
- 1 Excel workbook that includes up to 5 table or pivot table visuals
- 5 CSVs from table or pivot table visuals

The status of a submitted job can be polled with the `DescribeDashboardSnapshotJob` API. When you call the `DescribeDashboardSnapshotJob` API, check the `JobStatus` field in the response. Once the job reaches a `COMPLETED` or `FAILED` status, use the `DescribeDashboardSnapshotJobResult` API to obtain the URLs for the generated files. If the job fails, the `DescribeDashboardSnapshotJobResult` API returns detailed information about the error that occurred.

**StartDashboardSnapshotJob API throttling**

Amazon QuickSight utilizes API throttling to create a more consistent user experience within a time span for customers when they call the `StartDashboardSnapshotJob` . By default, 12 jobs can run simlutaneously in one Amazon Web Services account and users can submit up 10 API requests per second before an account is throttled. If an overwhelming number of API requests are made by the same user in a short period of time, Amazon QuickSight throttles the API calls to maintin an optimal experience and reliability for all Amazon QuickSight users.

**Common throttling scenarios**

The following list provides information about the most commin throttling scenarios that can occur.

- **A large number of ``SnapshotExport`` API jobs are running simultaneously on an Amazon Web Services account.** When a new `StartDashboardSnapshotJob` is created and there are already 12 jobs with the `RUNNING` status, the new job request fails and returns a `LimitExceededException` error. Wait for a current job to comlpete before you resubmit the new job.
- **A large number of API requests are submitted on an Amazon Web Services account.** When a user makes more than 10 API calls to the Amazon QuickSight API in one second, a `ThrottlingException` is returned.

If your use case requires a higher throttling limit, contact your account admin or [Amazon Web ServicesSupport](http://aws.amazon.com/contact-us/) to explore options to tailor a more optimal expereince for your account.

**Best practices to handle throttling**

If your use case projects high levels of API traffic, try to reduce the degree of frequency and parallelism of API calls as much as you can to avoid throttling. You can also perform a timing test to calculate an estimate for the total processing time of your projected load that stays within the throttling limits of the Amazon QuickSight APIs. For example, if your projected traffic is 100 snapshot jobs before 12:00 PM per day, start 12 jobs in parallel and measure the amount of time it takes to proccess all 12 jobs. Once you obtain the result, multiply the duration by 9, for example `(12 minutes * 9 = 108 minutes)` . Use the new result to determine the latest time at which the jobs need to be started to meet your target deadline.

The time that it takes to process a job can be impacted by the following factors:

- The dataset type (Direct Query or SPICE).
- The size of the dataset.
- The complexity of the calculated fields that are used in the dashboard.
- The number of visuals that are on a sheet.
- The types of visuals that are on the sheet.
- The number of formats and snapshots that are requested in the job configuration.
- The size of the generated snapshots.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/StartDashboardSnapshotJob)

## Synopsis

```
start-dashboard-snapshot-job
--aws-account-id <value>
--dashboard-id <value>
--snapshot-job-id <value>
--user-configuration <value>
--snapshot-configuration <value>
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

The ID of the dashboard that you want to start a snapshot job for.

`--snapshot-job-id` (string)

An ID for the dashboard snapshot job. This ID is unique to the dashboard while the job is running. This ID can be used to poll the status of a job with a `DescribeDashboardSnapshotJob` while the job runs. You can reuse this ID for another job 24 hours after the current job is completed.

`--user-configuration` (structure)

A structure that contains information about the anonymous users that the generated snapshot is for. This API will not return information about registered Amazon QuickSight.

AnonymousUsers -> (list)

An array of records that describe the anonymous users that the dashboard snapshot is generated for.

(structure)

A structure that contains information on the anonymous user configuration.

RowLevelPermissionTags -> (list)

The tags to be used for row-level security (RLS). Make sure that the relevant datasets have RLS tags configured before you start a snapshot export job. You can configure the RLS tags of a dataset with a `DataSet$RowLevelPermissionTagConfiguration` API call.

These are not the tags that are used for Amazon Web Services resource tagging. For more information on row level security in Amazon QuickSight, see [Using Row-Level Security (RLS) with Tags](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-dev-rls-tags.html) in the *Amazon QuickSight User Guide* .

(structure)

The key-value pair used for the row-level security tags feature.

Key -> (string)

The key for the tag.

Value -> (string)

The value that you want to assign the tag.

JSON Syntax:

```
{
  "AnonymousUsers": [
    {
      "RowLevelPermissionTags": [
        {
          "Key": "string",
          "Value": "string"
        }
        ...
      ]
    }
    ...
  ]
}
```

`--snapshot-configuration` (structure)

A structure that describes the configuration of the dashboard snapshot.

FileGroups -> (list)

A list of `SnapshotJobResultFileGroup` objects that contain information about the snapshot that is generated. This list can hold a maximum of 6 `FileGroup` configurations.

(structure)

A structure that contains the information on the snapshot files.

Files -> (list)

A list of `SnapshotFile` objects that contain the information on the snapshot files that need to be generated. This structure can hold 1 configuration at a time.

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

DestinationConfiguration -> (structure)

A structure that contains information on the Amazon S3 bucket that the generated snapshot is stored in.

S3Destinations -> (list)

A list of `SnapshotS3DestinationConfiguration` objects that contain Amazon S3 destination configurations. This structure can hold a maximum of 1 `S3DestinationConfiguration` .

(structure)

A structure that describes the Amazon S3 settings to use to save the generated dashboard snapshot.

BucketConfiguration -> (structure)

A structure that contains details about the Amazon S3 bucket that the generated dashboard snapshot is saved in.

BucketName -> (string)

The name of an existing Amazon S3 bucket where the generated snapshot artifacts are sent.

BucketPrefix -> (string)

The prefix of the Amazon S3 bucket that the generated snapshots are stored in.

BucketRegion -> (string)

The region that the Amazon S3 bucket is located in. The bucket must be located in the same region that the `StartDashboardSnapshotJob` API call is made.

Parameters -> (structure)

A list of Amazon QuickSight parameters and the listâs override values.

StringParameters -> (list)

The parameters that have a data type of string.

(structure)

A string parameter.

Name -> (string)

A display name for a string parameter.

Values -> (list)

The values of a string parameter.

(string)

IntegerParameters -> (list)

The parameters that have a data type of integer.

(structure)

An integer parameter.

Name -> (string)

The name of the integer parameter.

Values -> (list)

The values for the integer parameter.

(long)

DecimalParameters -> (list)

The parameters that have a data type of decimal.

(structure)

A decimal parameter.

Name -> (string)

A display name for the decimal parameter.

Values -> (list)

The values for the decimal parameter.

(double)

DateTimeParameters -> (list)

The parameters that have a data type of date-time.

(structure)

A date-time parameter.

Name -> (string)

A display name for the date-time parameter.

Values -> (list)

The values for the date-time parameter.

(timestamp)

JSON Syntax:

```
{
  "FileGroups": [
    {
      "Files": [
        {
          "SheetSelections": [
            {
              "SheetId": "string",
              "SelectionScope": "ALL_VISUALS"|"SELECTED_VISUALS",
              "VisualIds": ["string", ...]
            }
            ...
          ],
          "FormatType": "CSV"|"PDF"|"EXCEL"
        }
        ...
      ]
    }
    ...
  ],
  "DestinationConfiguration": {
    "S3Destinations": [
      {
        "BucketConfiguration": {
          "BucketName": "string",
          "BucketPrefix": "string",
          "BucketRegion": "string"
        }
      }
      ...
    ]
  },
  "Parameters": {
    "StringParameters": [
      {
        "Name": "string",
        "Values": ["string", ...]
      }
      ...
    ],
    "IntegerParameters": [
      {
        "Name": "string",
        "Values": [long, ...]
      }
      ...
    ],
    "DecimalParameters": [
      {
        "Name": "string",
        "Values": [double, ...]
      }
      ...
    ],
    "DateTimeParameters": [
      {
        "Name": "string",
        "Values": [timestamp, ...]
      }
      ...
    ]
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

## Output

Arn -> (string)

The Amazon Resource Name (ARN) for the dashboard snapshot job.

SnapshotJobId -> (string)

The ID of the job. The job ID is set when you start a new job with a `StartDashboardSnapshotJob` API call.

RequestId -> (string)

The Amazon Web Services request ID for this operation.

Status -> (integer)

The HTTP status of the request