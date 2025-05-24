# get-managed-notification-eventÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/get-managed-notification-event.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/get-managed-notification-event.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [notifications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/index.html#cli-aws-notifications) ]

# get-managed-notification-event

## Description

Returns a specified `ManagedNotificationEvent` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/notifications-2018-05-10/GetManagedNotificationEvent)

## Synopsis

```
get-managed-notification-event
--arn <value>
[--locale <value>]
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

`--arn` (string)

The Amazon Resource Name (ARN) of the `ManagedNotificationEvent` to return.

`--locale` (string)

The locale code of the language used for the retrieved `ManagedNotificationEvent` . The default locale is English `(en_US)` .

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

arn -> (string)

The ARN of the resource.

managedNotificationConfigurationArn -> (string)

The ARN of the `ManagedNotificationConfiguration` .

creationTime -> (timestamp)

The creation time of the `ManagedNotificationEvent` .

content -> (structure)

The content of the `ManagedNotificationEvent` .

schemaVersion -> (string)

Version of the `ManagedNotificationEvent` schema.

id -> (string)

Unique identifier for a `ManagedNotificationEvent` .

messageComponents -> (structure)

Describes the components of a notification message.

headline -> (string)

A sentence long summary. For example, titles or an email subject line.

paragraphSummary -> (string)

A paragraph long or multiple sentence summary. For example, Chatbot notifications.

completeDescription -> (string)

A complete summary with all possible relevant information.

dimensions -> (list)

A list of properties in key-value pairs. Pairs are shown in order of importance from most important to least important. Channels may limit the number of dimensions shown to the notification viewer.

### Note

Included dimensions, keys, and values are subject to change.

(structure)

The key-value pair of properties for an event.

name -> (string)

The name of the dimension

value -> (string)

The value of the dimension.

sourceEventDetailUrl -> (string)

URL defined by Source Service to be used by notification consumers to get additional information about event.

sourceEventDetailUrlDisplayText -> (string)

Text that needs to be hyperlinked with the sourceEventDetailUrl. For example, the description of the sourceEventDetailUrl.

notificationType -> (string)

The nature of the event causing this notification.

- Values:
- `ALERT`
- A notification about an event where something was triggered, initiated, reopened, deployed, or a threshold was breached.
- `WARNING`
- A notification about an event where an issue is about to arise. For example, something is approaching a threshold.
- `ANNOUNCEMENT`
- A notification about an important event. For example, a step in a workflow or escalation path or that a workflow was updated.
- `INFORMATIONAL`
- A notification about informational messages. For example, recommendations, service announcements, or reminders.

eventStatus -> (string)

The status of an event.

- Values:
- `HEALTHY`
- All EventRules are `ACTIVE` and any call can be run.
- `UNHEALTHY`
- Some EventRules are `ACTIVE` and some are `INACTIVE` . Any call can be run.

aggregationEventType -> (string)

The notifications aggregation type.

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

startTime -> (timestamp)

The earliest time of events to return from this call.

endTime -> (timestamp)

The end time of the notification event.

textParts -> (map)

A list of text values.

key -> (string)

value -> (structure)

Describes text information objects containing fields that determine how text part objects are composed.

type -> (string)

The type of text part. Determines the usage of all other fields and whether or not theyâre required.

displayText -> (string)

A short single line description of the link. Must be hyper-linked with the URL itself.

Used for text parts with the type `URL` .

textByLocale -> (map)

A map of locales to the text in that locale.

key -> (string)

value -> (string)

url -> (string)

The URL itself.

organizationalUnitId -> (string)

The Organizational Unit Id that an Amazon Web Services account belongs to.