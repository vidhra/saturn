# list-managed-notification-eventsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/list-managed-notification-events.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/list-managed-notification-events.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [notifications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/index.html#cli-aws-notifications) ]

# list-managed-notification-events

## Description

Returns a list of Managed Notification Events according to specified filters, ordered by creation time in reverse chronological order (newest first).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/notifications-2018-05-10/ListManagedNotificationEvents)

`list-managed-notification-events` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `managedNotificationEvents`

## Synopsis

```
list-managed-notification-events
[--start-time <value>]
[--end-time <value>]
[--locale <value>]
[--source <value>]
[--organizational-unit-id <value>]
[--related-account <value>]
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

`--start-time` (timestamp)

The earliest time of events to return from this call.

`--end-time` (timestamp)

Latest time of events to return from this call.

`--locale` (string)

The locale code of the language used for the retrieved NotificationEvent. The default locale is English (en_US).

Possible values:

- `de_DE`
- `en_CA`
- `en_US`
- `en_UK`
- `es_ES`
- `fr_CA`
- `fr_FR`
- `id_ID`
- `it_IT`
- `ja_JP`
- `ko_KR`
- `pt_BR`
- `tr_TR`
- `zh_CN`
- `zh_TW`

`--source` (string)

The Amazon Web Services service the event originates from. For example aws.cloudwatch.

`--organizational-unit-id` (string)

The Organizational Unit Id that an Amazon Web Services account belongs to.

`--related-account` (string)

The Amazon Web Services account ID associated with the Managed Notification Events.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

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

## Output

nextToken -> (string)

A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.

managedNotificationEvents -> (list)

A list of Managed Notification Events matching the request criteria.

(structure)

Describes an overview and metadata for a ManagedNotificationEvent.

arn -> (string)

The Amazon Resource Name (ARN) of the ManagedNotificationEvent.

managedNotificationConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the `ManagedNotificationConfiguration` .

relatedAccount -> (string)

The account that related to the `ManagedNotificationEvent` .

creationTime -> (timestamp)

The creation time of the `ManagedNotificationEvent` .

notificationEvent -> (structure)

A short summary of a `ManagedNotificationEvent` . This is only used when listing managed notification events.

schemaVersion -> (string)

The schema version of the `ManagedNotificationEvent` .

sourceEventMetadata -> (structure)

Contains metadata about the event that caused the `ManagedNotificationEvent` .

eventOriginRegion -> (string)

The Region where the notification originated.

source -> (string)

The source service of the notification.

Must match one of the valid EventBridge sources. Only Amazon Web Services service sourced events are supported. For example, `aws.ec2` and `aws.cloudwatch` . For more information, see [Event delivery from Amazon Web Services services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level) in the *Amazon EventBridge User Guide* .

eventType -> (string)

The event Type of the notification.

messageComponents -> (structure)

Contains the headline message component.

headline -> (string)

A sentence long summary. For example, titles or an email subject line.

eventStatus -> (string)

The managed notification event status.

- Values:
- `HEALTHY`
- All `EventRules` are `ACTIVE` .
- `UNHEALTHY`
- Some `EventRules` are `ACTIVE` and some are `INACTIVE` .

notificationType -> (string)

The Type of event causing the notification.

- Values:
- `ALERT`
- A notification about an event where something was triggered, initiated, reopened, deployed, or a threshold was breached.
- `WARNING`
- A notification about an event where an issue is about to arise. For example, something is approaching a threshold.
- `ANNOUNCEMENT`
- A notification about an important event. For example, a step in a workflow or escalation path or that a workflow was updated.
- `INFORMATIONAL`
- A notification about informational messages. For example, recommendations, service announcements, or reminders.

aggregationEventType -> (string)

The notifications aggregation type.

- Values:
- `AGGREGATE`
- The notification event is an aggregate notification. Aggregate notifications summarize grouped events over a specified time period.
- `CHILD`
- Some `EventRules` are `ACTIVE` and some are `INACTIVE` . Any call can be run.
- `NONE`
- The notification isnât aggregated.

organizationalUnitId -> (string)

The Organizational Unit Id that an Amazon Web Services account belongs to.

aggregationSummary -> (structure)

Provides additional information about the aggregation key.

eventCount -> (integer)

Indicates the number of events associated with the aggregation key.

aggregatedBy -> (list)

Indicates the criteria or rules by which notifications have been grouped together.

(structure)

Key-value collection that indicate how notifications are grouped.

name -> (string)

Indicates the type of aggregation key.

value -> (string)

Indicates the value associated with the aggregation key name.

aggregatedAccounts -> (structure)

Indicates the Amazon Web Services accounts in the aggregation key.

name -> (string)

Name of the summarization dimension.

count -> (integer)

Total number of occurrences for this dimension.

sampleValues -> (list)

Indicates the sample values found within the dimension.

(string)

aggregatedRegions -> (structure)

Indicates the Amazon Web Services Regions in the aggregation key.

name -> (string)

Name of the summarization dimension.

count -> (integer)

Total number of occurrences for this dimension.

sampleValues -> (list)

Indicates the sample values found within the dimension.

(string)

aggregatedOrganizationalUnits -> (structure)

Indicates the collection of organizational units that are involved in the aggregation key.

name -> (string)

Name of the summarization dimension.

count -> (integer)

Total number of occurrences for this dimension.

sampleValues -> (list)

Indicates the sample values found within the dimension.

(string)

additionalSummarizationDimensions -> (list)

List of additional dimensions used to group and summarize data.

(structure)

Provides an overview of how data is summarized across different dimensions.

name -> (string)

Name of the summarization dimension.

count -> (integer)

Total number of occurrences for this dimension.

sampleValues -> (list)

Indicates the sample values found within the dimension.

(string)

aggregatedNotificationRegions -> (list)

The list of the regions where the aggregated notifications in this `NotificationEvent` originated.

(string)