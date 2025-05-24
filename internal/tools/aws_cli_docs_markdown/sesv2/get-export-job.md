# get-export-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-export-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-export-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sesv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/index.html#cli-aws-sesv2) ]

# get-export-job

## Description

Provides information about an export job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sesv2-2019-09-27/GetExportJob)

## Synopsis

```
get-export-job
--job-id <value>
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

`--job-id` (string)

The export job ID.

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

JobId -> (string)

The export job ID.

ExportSourceType -> (string)

The type of source of the export job.

JobStatus -> (string)

The status of the export job.

ExportDestination -> (structure)

The destination of the export job.

DataFormat -> (string)

The data format of the final export job file, can be one of the following:

- `CSV` - A comma-separated values file.
- `JSON` - A Json file.

S3Url -> (string)

An Amazon S3 pre-signed URL that points to the generated export file.

ExportDataSource -> (structure)

The data source of the export job.

MetricsDataSource -> (structure)

An object that contains details about the data source for the metrics export.

Dimensions -> (map)

An object that contains a mapping between a `MetricDimensionName` and `MetricDimensionValue` to filter metrics by. Must contain a least 1 dimension but no more than 3 unique ones.

key -> (string)

The `BatchGetMetricDataQuery` dimension name. This can be one of the following:

- `EMAIL_IDENTITY` â The email identity used when sending messages.
- `CONFIGURATION_SET` â The configuration set used when sending messages (if one was used).
- `ISP` â The recipient ISP (e.g. `Gmail` , `Yahoo` , etc.).

value -> (list)

(string)

A list of values associated with the `MetricDimensionName` to filter metrics by. Can either be `*` as a wildcard for all values or a list of up to 10 specific values. If one `Dimension` has the `*` value, other dimensions can only contain one value.

Namespace -> (string)

The metrics namespace - e.g., `VDM` .

Metrics -> (list)

A list of `ExportMetric` objects to export.

(structure)

An object that contains a mapping between a `Metric` and `MetricAggregation` .

Name -> (string)

The metric to export, can be one of the following:

- `SEND` - Emails sent eligible for tracking in the VDM dashboard. This excludes emails sent to the mailbox simulator and emails addressed to more than one recipient.
- `COMPLAINT` - Complaints received for your account. This excludes complaints from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those for emails addressed to more than one recipient
- `PERMANENT_BOUNCE` - Permanent bounces - i.e., feedback received for emails sent to non-existent mailboxes. Excludes bounces from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those for emails addressed to more than one recipient.
- `TRANSIENT_BOUNCE` - Transient bounces - i.e., feedback received for delivery failures excluding issues with non-existent mailboxes. Excludes bounces from the mailbox simulator, and those for emails addressed to more than one recipient.
- `OPEN` - Unique open events for emails including open trackers. Excludes opens for emails addressed to more than one recipient.
- `CLICK` - Unique click events for emails including wrapped links. Excludes clicks for emails addressed to more than one recipient.
- `DELIVERY` - Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator and for emails addressed to more than one recipient.
- `DELIVERY_OPEN` - Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails without open trackers.
- `DELIVERY_CLICK` - Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails without click trackers.
- `DELIVERY_COMPLAINT` - Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails addressed to recipients hosted by ISPs with which Amazon SES does not have a feedback loop agreement.

Aggregation -> (string)

The aggregation to apply to a metric, can be one of the following:

- `VOLUME` - The volume of events for this metric.
- `RATE` - The rate for this metric relative to the `SEND` metric volume.

StartDate -> (timestamp)

Represents the start date for the export interval as a timestamp.

EndDate -> (timestamp)

Represents the end date for the export interval as a timestamp.

MessageInsightsDataSource -> (structure)

An object that contains filters applied when performing the Message Insights export.

StartDate -> (timestamp)

Represents the start date for the export interval as a timestamp. The start date is inclusive.

EndDate -> (timestamp)

Represents the end date for the export interval as a timestamp. The end date is inclusive.

Include -> (structure)

Filters for results to be included in the export file.

FromEmailAddress -> (list)

The from address used to send the message.

(string)

Destination -> (list)

The recipientâs email address.

(string)

Subject -> (list)

The subject line of the message.

(string)

Isp -> (list)

The recipientâs ISP (e.g., `Gmail` , `Yahoo` , etc.).

(string)

LastDeliveryEvent -> (list)

The last delivery-related event for the email, where the ordering is as follows: `SEND` < `BOUNCE` < `DELIVERY` < `COMPLAINT` .

(string)

The type of delivery events:

- `SEND` - The send request was successful and SES will attempt to deliver the message to the recipientâs mail server. (If account-level or global suppression is being used, SES will still count it as a send, but delivery is suppressed.)
- `DELIVERY` - SES successfully delivered the email to the recipientâs mail server. Excludes deliveries to the mailbox simulator and emails addressed to more than one recipient.
- `TRANSIENT_BOUNCE` - Feedback received for delivery failures excluding issues with non-existent mailboxes. Excludes bounces from the mailbox simulator, and those from emails addressed to more than one recipient.
- `PERMANENT_BOUNCE` - Feedback received for emails sent to non-existent mailboxes. Excludes bounces from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those from emails addressed to more than one recipient.
- `UNDETERMINED_BOUNCE` - SES was unable to determine the bounce reason.
- `COMPLAINT` - Complaint received for the email. This excludes complaints from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those from emails addressed to more than one recipient.

LastEngagementEvent -> (list)

The last engagement-related event for the email, where the ordering is as follows: `OPEN` < `CLICK` .

Engagement events are only available if [Engagement tracking](https://docs.aws.amazon.com/ses/latest/dg/vdm-settings.html) is enabled.

(string)

The type of delivery events:

- `OPEN` - Open event for emails including open trackers. Excludes opens for emails addressed to more than one recipient.
- `CLICK` - Click event for emails including wrapped links. Excludes clicks for emails addressed to more than one recipient.

Exclude -> (structure)

Filters for results to be excluded from the export file.

FromEmailAddress -> (list)

The from address used to send the message.

(string)

Destination -> (list)

The recipientâs email address.

(string)

Subject -> (list)

The subject line of the message.

(string)

Isp -> (list)

The recipientâs ISP (e.g., `Gmail` , `Yahoo` , etc.).

(string)

LastDeliveryEvent -> (list)

The last delivery-related event for the email, where the ordering is as follows: `SEND` < `BOUNCE` < `DELIVERY` < `COMPLAINT` .

(string)

The type of delivery events:

- `SEND` - The send request was successful and SES will attempt to deliver the message to the recipientâs mail server. (If account-level or global suppression is being used, SES will still count it as a send, but delivery is suppressed.)
- `DELIVERY` - SES successfully delivered the email to the recipientâs mail server. Excludes deliveries to the mailbox simulator and emails addressed to more than one recipient.
- `TRANSIENT_BOUNCE` - Feedback received for delivery failures excluding issues with non-existent mailboxes. Excludes bounces from the mailbox simulator, and those from emails addressed to more than one recipient.
- `PERMANENT_BOUNCE` - Feedback received for emails sent to non-existent mailboxes. Excludes bounces from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those from emails addressed to more than one recipient.
- `UNDETERMINED_BOUNCE` - SES was unable to determine the bounce reason.
- `COMPLAINT` - Complaint received for the email. This excludes complaints from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those from emails addressed to more than one recipient.

LastEngagementEvent -> (list)

The last engagement-related event for the email, where the ordering is as follows: `OPEN` < `CLICK` .

Engagement events are only available if [Engagement tracking](https://docs.aws.amazon.com/ses/latest/dg/vdm-settings.html) is enabled.

(string)

The type of delivery events:

- `OPEN` - Open event for emails including open trackers. Excludes opens for emails addressed to more than one recipient.
- `CLICK` - Click event for emails including wrapped links. Excludes clicks for emails addressed to more than one recipient.

MaxResults -> (integer)

The maximum number of results.

CreatedTimestamp -> (timestamp)

The timestamp of when the export job was created.

CompletedTimestamp -> (timestamp)

The timestamp of when the export job was completed.

FailureInfo -> (structure)

The failure details about an export job.

FailedRecordsS3Url -> (string)

An Amazon S3 pre-signed URL that contains all the failed records and related information.

ErrorMessage -> (string)

A message about why the job failed.

Statistics -> (structure)

The statistics about the export job.

ProcessedRecordsCount -> (integer)

The number of records that were processed to generate the final export file.

ExportedRecordsCount -> (integer)

The number of records that were exported to the final export file.

This value might not be available for all export source types