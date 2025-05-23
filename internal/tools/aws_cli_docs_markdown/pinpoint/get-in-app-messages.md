# get-in-app-messagesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-in-app-messages.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-in-app-messages.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/index.html#cli-aws-pinpoint) ]

# get-in-app-messages

## Description

Retrieves the in-app messages targeted for the provided endpoint ID.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/GetInAppMessages)

## Synopsis

```
get-in-app-messages
--application-id <value>
--endpoint-id <value>
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

`--application-id` (string)

The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console.

`--endpoint-id` (string)

The unique identifier for the endpoint.

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

InAppMessagesResponse -> (structure)

Get in-app messages response object.

InAppMessageCampaigns -> (list)

List of targeted in-app message campaigns.

(structure)

Targeted in-app message campaign.

CampaignId -> (string)

Campaign id of the corresponding campaign.

DailyCap -> (integer)

Daily cap which controls the number of times any in-app messages can be shown to the endpoint during a day.

InAppMessage -> (structure)

In-app message content with all fields required for rendering an in-app message.

Content -> (list)

In-app message content.

(structure)

The configuration for the message content.

BackgroundColor -> (string)

The background color for the message.

BodyConfig -> (structure)

The configuration for the message body.

Alignment -> (string)

The alignment of the text. Valid values: LEFT, CENTER, RIGHT.

Body -> (string)

Message Body.

TextColor -> (string)

The text color.

HeaderConfig -> (structure)

The configuration for the message header.

Alignment -> (string)

The alignment of the text. Valid values: LEFT, CENTER, RIGHT.

Header -> (string)

Message Header.

TextColor -> (string)

The text color.

ImageUrl -> (string)

The image url for the background of message.

PrimaryBtn -> (structure)

The first button inside the message.

Android -> (structure)

Default button content.

ButtonAction -> (string)

Action triggered by the button.

Link -> (string)

Button destination.

DefaultConfig -> (structure)

Default button content.

BackgroundColor -> (string)

The background color of the button.

BorderRadius -> (integer)

The border radius of the button.

ButtonAction -> (string)

Action triggered by the button.

Link -> (string)

Button destination.

Text -> (string)

Button text.

TextColor -> (string)

The text color of the button.

IOS -> (structure)

Default button content.

ButtonAction -> (string)

Action triggered by the button.

Link -> (string)

Button destination.

Web -> (structure)

Default button content.

ButtonAction -> (string)

Action triggered by the button.

Link -> (string)

Button destination.

SecondaryBtn -> (structure)

The second button inside message.

Android -> (structure)

Default button content.

ButtonAction -> (string)

Action triggered by the button.

Link -> (string)

Button destination.

DefaultConfig -> (structure)

Default button content.

BackgroundColor -> (string)

The background color of the button.

BorderRadius -> (integer)

The border radius of the button.

ButtonAction -> (string)

Action triggered by the button.

Link -> (string)

Button destination.

Text -> (string)

Button text.

TextColor -> (string)

The text color of the button.

IOS -> (structure)

Default button content.

ButtonAction -> (string)

Action triggered by the button.

Link -> (string)

Button destination.

Web -> (structure)

Default button content.

ButtonAction -> (string)

Action triggered by the button.

Link -> (string)

Button destination.

CustomConfig -> (map)

Custom config to be sent to SDK.

key -> (string)

value -> (string)

Layout -> (string)

The layout of the message.

Priority -> (integer)

Priority of the in-app message.

Schedule -> (structure)

Schedule of the campaign.

EndDate -> (string)

The scheduled time after which the in-app message should not be shown. Timestamp is in ISO 8601 format.

EventFilter -> (structure)

The event filter the SDK has to use to show the in-app message in the application.

Dimensions -> (structure)

The dimension settings of the event filter for the campaign.

Attributes -> (map)

One or more custom attributes that your application reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.

key -> (string)

value -> (structure)

Specifies attribute-based criteria for including or excluding endpoints from a segment.

AttributeType -> (string)

The type of segment dimension to use. Valid values are:

- INCLUSIVE - endpoints that have attributes matching the values are included in the segment.
- EXCLUSIVE - endpoints that have attributes matching the values are excluded in the segment.
- CONTAINS - endpoints that have attributesâ substrings match the values are included in the segment.
- BEFORE - endpoints with attributes read as ISO_INSTANT datetimes before the value are included in the segment.
- AFTER - endpoints with attributes read as ISO_INSTANT datetimes after the value are included in the segment.
- ON - endpoints with attributes read as ISO_INSTANT dates on the value are included in the segment. Time is ignored in this comparison.
- BETWEEN - endpoints with attributes read as ISO_INSTANT datetimes between the values are included in the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the AttributeType property, endpoints are included or excluded from the segment if their attribute values match the criteria values.

(string)

EventType -> (structure)

The name of the event that causes the campaign to be sent or the journey activity to be performed. This can be a standard event that Amazon Pinpoint generates, such as _email.delivered. For campaigns, this can also be a custom event thatâs specific to your application. For information about standard events, see [Streaming Amazon Pinpoint Events](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams.html) in the *Amazon Pinpoint Developer Guide* .

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Metrics -> (map)

One or more custom metrics that your application reports to Amazon Pinpoint. You can use these metrics as selection criteria when you create an event filter.

key -> (string)

value -> (structure)

Specifies metric-based criteria for including or excluding endpoints from a segment. These criteria derive from custom metrics that you define for endpoints.

ComparisonOperator -> (string)

The operator to use when comparing metric values. Valid values are: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, and EQUAL.

Value -> (double)

The value to compare.

FilterType -> (string)

The type of event that causes the campaign to be sent. Valid values are: SYSTEM, sends the campaign when a system event occurs; and, ENDPOINT, sends the campaign when an endpoint event (Eventsresource) occurs.

QuietTime -> (structure)

Time during which the in-app message should not be shown to the user.

End -> (string)

The specific time when quiet time ends. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.

Start -> (string)

The specific time when quiet time begins. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.

SessionCap -> (integer)

Session cap which controls the number of times an in-app message can be shown to the endpoint during an application session.

TotalCap -> (integer)

Total cap which controls the number of times an in-app message can be shown to the endpoint.

TreatmentId -> (string)

Treatment id of the campaign.