# create-journeyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-journey.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-journey.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/index.html#cli-aws-pinpoint) ]

# create-journey

## Description

Creates a journey for an application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/CreateJourney)

## Synopsis

```
create-journey
--application-id <value>
--write-journey-request <value>
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

`--write-journey-request` (structure)

Specifies the configuration and other settings for a journey.

Activities -> (map)

A map that contains a set of Activity objects, one object for each activity in the journey. For each Activity object, the key is the unique identifier (string) for an activity and the value is the settings for the activity. An activity identifier can contain a maximum of 100 characters. The characters must be alphanumeric characters.

key -> (string)

value -> (structure)

Specifies the configuration and other settings for an activity in a journey.

CUSTOM -> (structure)

The settings for a custom message activity. This type of activity calls an AWS Lambda function or web hook that sends messages to participants.

DeliveryUri -> (string)

The destination to send the campaign or treatment to. This value can be one of the following:

- The name or Amazon Resource Name (ARN) of an AWS Lambda function to invoke to handle delivery of the campaign or treatment.
- The URL for a web application or service that supports HTTPS and can receive the message. The URL has to be a full URL, including the HTTPS protocol.

EndpointTypes -> (list)

The types of endpoints to send the custom message to. Each valid value maps to a type of channel that you can associate with an endpoint by using the ChannelType property of an endpoint.

(string)

MessageConfig -> (structure)

Specifies the message data included in a custom channel message thatâs sent to participants in a journey.

Data -> (string)

The message content thatâs passed to an AWS Lambda function or to a web hook.

NextActivity -> (string)

The unique identifier for the next activity to perform, after Amazon Pinpoint calls the AWS Lambda function or web hook.

TemplateName -> (string)

The name of the custom message template to use for the message. If specified, this value must match the name of an existing message template.

TemplateVersion -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

ConditionalSplit -> (structure)

The settings for a yes/no split activity. This type of activity sends participants down one of two paths in a journey, based on conditions that you specify.

Condition -> (structure)

The conditions that define the paths for the activity, and the relationship between the conditions.

Conditions -> (list)

The conditions to evaluate for the activity.

(structure)

Specifies a condition to evaluate for an activity in a journey.

EventCondition -> (structure)

The dimension settings for the event thatâs associated with the activity.

Dimensions -> (structure)

The dimensions for the event filter to use for the activity.

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

MessageActivity -> (string)

The message identifier (message_id) for the message to use when determining whether message events meet the condition.

SegmentCondition -> (structure)

The segment thatâs associated with the activity.

SegmentId -> (string)

The unique identifier for the segment to associate with the activity.

SegmentDimensions -> (structure)

The dimension settings for the segment thatâs associated with the activity.

Attributes -> (map)

One or more custom attributes to use as criteria for the segment.

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

Behavior -> (structure)

The behavior-based criteria, such as how recently users have used your app, for the segment.

Recency -> (structure)

The dimension settings that are based on how recently an endpoint was active.

Duration -> (string)

The duration to use when determining whether an endpoint is active or inactive.

RecencyType -> (string)

The type of recency dimension to use for the segment. Valid values are: ACTIVE, endpoints that were active within the specified duration are included in the segment; and, INACTIVE, endpoints that werenât active within the specified duration are included in the segment.

Demographic -> (structure)

The demographic-based criteria, such as device platform, for the segment.

AppVersion -> (structure)

The app version criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Channel -> (structure)

The channel criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

DeviceType -> (structure)

The device type criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Make -> (structure)

The device make criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Model -> (structure)

The device model criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Platform -> (structure)

The device platform criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Location -> (structure)

The location-based criteria, such as region or GPS coordinates, for the segment.

Country -> (structure)

The country or region code, in ISO 3166-1 alpha-2 format, for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

GPSPoint -> (structure)

The GPS location and range for the segment.

Coordinates -> (structure)

The GPS coordinates to measure distance from.

Latitude -> (double)

The latitude coordinate of the location.

Longitude -> (double)

The longitude coordinate of the location.

RangeInKilometers -> (double)

The range, in kilometers, from the GPS coordinates.

Metrics -> (map)

One or more custom metrics to use as criteria for the segment.

key -> (string)

value -> (structure)

Specifies metric-based criteria for including or excluding endpoints from a segment. These criteria derive from custom metrics that you define for endpoints.

ComparisonOperator -> (string)

The operator to use when comparing metric values. Valid values are: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, and EQUAL.

Value -> (double)

The value to compare.

UserAttributes -> (map)

One or more custom user attributes to use as criteria for the segment.

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

Operator -> (string)

Specifies how to handle multiple conditions for the activity. For example, if you specify two conditions for an activity, whether both or only one of the conditions must be met for the activity to be performed.

EvaluationWaitTime -> (structure)

The amount of time to wait before determining whether the conditions are met, or the date and time when Amazon Pinpoint determines whether the conditions are met.

WaitFor -> (string)

The amount of time to wait, as a duration in ISO 8601 format, before determining whether the activityâs conditions have been met or moving participants to the next activity in the journey.

WaitUntil -> (string)

The date and time, in ISO 8601 format, when Amazon Pinpoint determines whether the activityâs conditions have been met or the activity moves participants to the next activity in the journey.

FalseActivity -> (string)

The unique identifier for the activity to perform if the conditions arenât met.

TrueActivity -> (string)

The unique identifier for the activity to perform if the conditions are met.

Description -> (string)

The custom description of the activity.

EMAIL -> (structure)

The settings for an email activity. This type of activity sends an email message to participants.

MessageConfig -> (structure)

Specifies the sender address for an email message thatâs sent to participants in the journey.

FromAddress -> (string)

The verified email address to send the email message from. The default address is the FromAddress specified for the email channel for the application.

NextActivity -> (string)

The unique identifier for the next activity to perform, after the message is sent.

TemplateName -> (string)

The name of the email message template to use for the message. If specified, this value must match the name of an existing message template.

TemplateVersion -> (string)

The unique identifier for the version of the email template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

Holdout -> (structure)

The settings for a holdout activity. This type of activity stops a journey for a specified percentage of participants.

NextActivity -> (string)

The unique identifier for the next activity to perform, after performing the holdout activity.

Percentage -> (integer)

The percentage of participants who shouldnât continue the journey.

To determine which participants are held out, Amazon Pinpoint applies a probability-based algorithm to the percentage that you specify. Therefore, the actual percentage of participants who are held out may not be equal to the percentage that you specify.

MultiCondition -> (structure)

The settings for a multivariate split activity. This type of activity sends participants down one of as many as five paths (including a default *Else* path) in a journey, based on conditions that you specify.

Branches -> (list)

The paths for the activity, including the conditions for entering each path and the activity to perform for each path.

(structure)

Specifies a condition to evaluate for an activity path in a journey.

Condition -> (structure)

The condition to evaluate for the activity path.

EventCondition -> (structure)

The dimension settings for the event thatâs associated with the activity.

Dimensions -> (structure)

The dimensions for the event filter to use for the activity.

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

MessageActivity -> (string)

The message identifier (message_id) for the message to use when determining whether message events meet the condition.

SegmentCondition -> (structure)

The segment thatâs associated with the activity.

SegmentId -> (string)

The unique identifier for the segment to associate with the activity.

SegmentDimensions -> (structure)

The dimension settings for the segment thatâs associated with the activity.

Attributes -> (map)

One or more custom attributes to use as criteria for the segment.

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

Behavior -> (structure)

The behavior-based criteria, such as how recently users have used your app, for the segment.

Recency -> (structure)

The dimension settings that are based on how recently an endpoint was active.

Duration -> (string)

The duration to use when determining whether an endpoint is active or inactive.

RecencyType -> (string)

The type of recency dimension to use for the segment. Valid values are: ACTIVE, endpoints that were active within the specified duration are included in the segment; and, INACTIVE, endpoints that werenât active within the specified duration are included in the segment.

Demographic -> (structure)

The demographic-based criteria, such as device platform, for the segment.

AppVersion -> (structure)

The app version criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Channel -> (structure)

The channel criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

DeviceType -> (structure)

The device type criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Make -> (structure)

The device make criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Model -> (structure)

The device model criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Platform -> (structure)

The device platform criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Location -> (structure)

The location-based criteria, such as region or GPS coordinates, for the segment.

Country -> (structure)

The country or region code, in ISO 3166-1 alpha-2 format, for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

GPSPoint -> (structure)

The GPS location and range for the segment.

Coordinates -> (structure)

The GPS coordinates to measure distance from.

Latitude -> (double)

The latitude coordinate of the location.

Longitude -> (double)

The longitude coordinate of the location.

RangeInKilometers -> (double)

The range, in kilometers, from the GPS coordinates.

Metrics -> (map)

One or more custom metrics to use as criteria for the segment.

key -> (string)

value -> (structure)

Specifies metric-based criteria for including or excluding endpoints from a segment. These criteria derive from custom metrics that you define for endpoints.

ComparisonOperator -> (string)

The operator to use when comparing metric values. Valid values are: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, and EQUAL.

Value -> (double)

The value to compare.

UserAttributes -> (map)

One or more custom user attributes to use as criteria for the segment.

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

NextActivity -> (string)

The unique identifier for the next activity to perform, after completing the activity for the path.

DefaultActivity -> (string)

The unique identifier for the activity to perform for participants who donât meet any of the conditions specified for other paths in the activity.

EvaluationWaitTime -> (structure)

The amount of time to wait or the date and time when Amazon Pinpoint determines whether the conditions are met.

WaitFor -> (string)

The amount of time to wait, as a duration in ISO 8601 format, before determining whether the activityâs conditions have been met or moving participants to the next activity in the journey.

WaitUntil -> (string)

The date and time, in ISO 8601 format, when Amazon Pinpoint determines whether the activityâs conditions have been met or the activity moves participants to the next activity in the journey.

PUSH -> (structure)

The settings for a push notification activity. This type of activity sends a push notification to participants.

MessageConfig -> (structure)

Specifies the time to live (TTL) value for push notifications that are sent to participants in a journey.

TimeToLive -> (string)

The number of seconds that the push notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

NextActivity -> (string)

The unique identifier for the next activity to perform, after the message is sent.

TemplateName -> (string)

The name of the push notification template to use for the message. If specified, this value must match the name of an existing message template.

TemplateVersion -> (string)

The unique identifier for the version of the push notification template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

RandomSplit -> (structure)

The settings for a random split activity. This type of activity randomly sends specified percentages of participants down one of as many as five paths in a journey, based on conditions that you specify.

Branches -> (list)

The paths for the activity, including the percentage of participants to enter each path and the activity to perform for each path.

(structure)

Specifies the settings for a path in a random split activity in a journey.

NextActivity -> (string)

The unique identifier for the next activity to perform, after completing the activity for the path.

Percentage -> (integer)

The percentage of participants to send down the activity path.

To determine which participants are sent down each path, Amazon Pinpoint applies a probability-based algorithm to the percentages that you specify for the paths. Therefore, the actual percentage of participants who are sent down a path may not be equal to the percentage that you specify.

SMS -> (structure)

The settings for an SMS activity. This type of activity sends a text message to participants.

MessageConfig -> (structure)

Specifies the sender ID and message type for an SMS message thatâs sent to participants in a journey.

MessageType -> (string)

The SMS message type. Valid values are TRANSACTIONAL (for messages that are critical or time-sensitive, such as a one-time passwords) and PROMOTIONAL (for messsages that arenât critical or time-sensitive, such as marketing messages).

OriginationNumber -> (string)

The long code to send the SMS message from. This value should be one of the dedicated long codes thatâs assigned to your AWS account. Although it isnât required, we recommend that you specify the long code using an E.164 format to ensure prompt and accurate delivery of the message. For example, +12065550100.

SenderId -> (string)

The sender ID to display as the sender of the message on a recipientâs device. Support for sender IDs varies by country or region. For more information, see [Supported Countries and Regions](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-countries.html) in the Amazon Pinpoint User Guide.

EntityId -> (string)

The entity ID or Principal Entity (PE) id received from the regulatory body for sending SMS in your country.

TemplateId -> (string)

The template ID received from the regulatory body for sending SMS in your country.

NextActivity -> (string)

The unique identifier for the next activity to perform, after the message is sent.

TemplateName -> (string)

The name of the SMS message template to use for the message. If specified, this value must match the name of an existing message template.

TemplateVersion -> (string)

The unique identifier for the version of the SMS template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

Wait -> (structure)

The settings for a wait activity. This type of activity waits for a certain amount of time or until a specific date and time before moving participants to the next activity in a journey.

NextActivity -> (string)

The unique identifier for the next activity to perform, after performing the wait activity.

WaitTime -> (structure)

The amount of time to wait or the date and time when the activity moves participants to the next activity in the journey.

WaitFor -> (string)

The amount of time to wait, as a duration in ISO 8601 format, before determining whether the activityâs conditions have been met or moving participants to the next activity in the journey.

WaitUntil -> (string)

The date and time, in ISO 8601 format, when Amazon Pinpoint determines whether the activityâs conditions have been met or the activity moves participants to the next activity in the journey.

ContactCenter -> (structure)

The settings for a connect activity. This type of activity initiates a contact center call to participants.

NextActivity -> (string)

The unique identifier for the next activity to perform after the this activity.

CreationDate -> (string)

The date, in ISO 8601 format, when the journey was created.

LastModifiedDate -> (string)

The date, in ISO 8601 format, when the journey was last modified.

Limits -> (structure)

The messaging and entry limits for the journey.

DailyCap -> (integer)

The maximum number of messages that the journey can send to a single participant during a 24-hour period. The maximum value is 100.

EndpointReentryCap -> (integer)

The maximum number of times that a participant can enter the journey. The maximum value is 100. To allow participants to enter the journey an unlimited number of times, set this value to 0.

MessagesPerSecond -> (integer)

The maximum number of messages that the journey can send each second.

EndpointReentryInterval -> (string)

Minimum time that must pass before an endpoint can re-enter a given journey. The duration should use an ISO 8601 format, such as PT1H.

TimeframeCap -> (structure)

The number of messages that an endpoint can receive during the specified timeframe.

Cap -> (integer)

The maximum number of messages that all journeys can send to an endpoint during the specified timeframe. The maximum value is 100. If set to 0, this limit will not apply.

Days -> (integer)

The length of the timeframe in days. The maximum value is 30. If set to 0, this limit will not apply.

TotalCap -> (integer)

The maximum number of messages a journey can sent to a single endpoint. The maximum value is 100. If set to 0, this limit will not apply.

LocalTime -> (boolean)

Specifies whether the journeyâs scheduled start and end times use each participantâs local time. To base the schedule on each participantâs local time, set this value to true.

Name -> (string)

The name of the journey. A journey name can contain a maximum of 150 characters. The characters can be alphanumeric characters or symbols, such as underscores (_) or hyphens (-). A journey name canât contain any spaces.

QuietTime -> (structure)

The quiet time settings for the journey. Quiet time is a specific time range when a journey doesnât send messages to participants, if all the following conditions are met:

- The EndpointDemographic.Timezone property of the endpoint for the participant is set to a valid value.
- The current time in the participantâs time zone is later than or equal to the time specified by the QuietTime.Start property for the journey.
- The current time in the participantâs time zone is earlier than or equal to the time specified by the QuietTime.End property for the journey.

If any of the preceding conditions isnât met, the participant will receive messages from the journey, even if quiet time is enabled.

End -> (string)

The specific time when quiet time ends. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.

Start -> (string)

The specific time when quiet time begins. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.

RefreshFrequency -> (string)

The frequency with which Amazon Pinpoint evaluates segment and event data for the journey, as a duration in ISO 8601 format.

Schedule -> (structure)

The schedule settings for the journey.

EndTime -> (timestamp)

The scheduled time, in ISO 8601 format, when the journey ended or will end.

StartTime -> (timestamp)

The scheduled time, in ISO 8601 format, when the journey began or will begin.

Timezone -> (string)

The starting UTC offset for the journey schedule, if the value of the journeyâs LocalTime property is true. Valid values are: UTC, UTC+01, UTC+02, UTC+03, UTC+03:30, UTC+04, UTC+04:30, UTC+05, UTC+05:30, UTC+05:45, UTC+06, UTC+06:30, UTC+07, UTC+08, UTC+08:45, UTC+09, UTC+09:30, UTC+10, UTC+10:30, UTC+11, UTC+12, UTC+12:45, UTC+13, UTC+13:45, UTC-02, UTC-02:30, UTC-03, UTC-03:30, UTC-04, UTC-05, UTC-06, UTC-07, UTC-08, UTC-09, UTC-09:30, UTC-10, and UTC-11.

StartActivity -> (string)

The unique identifier for the first activity in the journey. The identifier for this activity can contain a maximum of 128 characters. The characters must be alphanumeric characters.

StartCondition -> (structure)

The segment that defines which users are participants in the journey.

Description -> (string)

The custom description of the condition.

EventStartCondition -> (structure)

Specifies the settings for an event that causes a journey activity to start.

EventFilter -> (structure)

Specifies the settings for an event that causes a campaign to be sent or a journey activity to be performed.

Dimensions -> (structure)

The dimensions for the event filter to use for the campaign or the journey activity.

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

The type of event that causes the campaign to be sent or the journey activity to be performed. Valid values are: SYSTEM, sends the campaign or performs the activity when a system event occurs; and, ENDPOINT, sends the campaign or performs the activity when an endpoint event (Events resource) occurs.

SegmentId -> (string)

SegmentStartCondition -> (structure)

The segment thatâs associated with the first activity in the journey. This segment determines which users are participants in the journey.

SegmentId -> (string)

The unique identifier for the segment to associate with the activity.

State -> (string)

The status of the journey. Valid values are:

- DRAFT - Saves the journey and doesnât publish it.
- ACTIVE - Saves and publishes the journey. Depending on the journeyâs schedule, the journey starts running immediately or at the scheduled start time. If a journeyâs status is ACTIVE, you canât add, change, or remove activities from it.

PAUSED, CANCELLED, COMPLETED, and CLOSED states are not supported in requests to create or update a journey. To cancel, pause, or resume a journey, use the Journey Stateresource.

WaitForQuietTime -> (boolean)

Specifies whether endpoints in quiet hours should enter a wait till the end of their quiet hours.

RefreshOnSegmentUpdate -> (boolean)

Indicates whether the journey participants should be refreshed when a segment is updated.

JourneyChannelSettings -> (structure)

The channel-specific configurations for the journey.

ConnectCampaignArn -> (string)

Amazon Resource Name (ARN) of the Connect Campaign.

ConnectCampaignExecutionRoleArn -> (string)

IAM role ARN to be assumed when invoking Connect campaign execution APIs for dialing.

SendingSchedule -> (boolean)

Indicates if journey has Advance Quiet Time enabled. This flag should be set to true in order to allow using OpenHours and ClosedDays.

OpenHours -> (structure)

The time when journey allow to send messages. QuietTime should be configured first and SendingSchedule should be set to true.

EMAIL -> (map)

Specifies the schedule settings for the email channel.

key -> (string)

Day of a week when the rule will be applied. Valid values are [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]

value -> (list)

Open Hour Rules.

(structure)

Open Hour Rule Details.

StartTime -> (string)

The start of the scheduled time, in ISO 8601 format, when the channel can send messages.

EndTime -> (string)

The end of the scheduled time, in ISO 8601 format, when the channel canât send messages.

SMS -> (map)

Specifies the schedule settings for the SMS channel.

key -> (string)

Day of a week when the rule will be applied. Valid values are [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]

value -> (list)

Open Hour Rules.

(structure)

Open Hour Rule Details.

StartTime -> (string)

The start of the scheduled time, in ISO 8601 format, when the channel can send messages.

EndTime -> (string)

The end of the scheduled time, in ISO 8601 format, when the channel canât send messages.

PUSH -> (map)

Specifies the schedule settings for the push channel.

key -> (string)

Day of a week when the rule will be applied. Valid values are [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]

value -> (list)

Open Hour Rules.

(structure)

Open Hour Rule Details.

StartTime -> (string)

The start of the scheduled time, in ISO 8601 format, when the channel can send messages.

EndTime -> (string)

The end of the scheduled time, in ISO 8601 format, when the channel canât send messages.

VOICE -> (map)

Specifies the schedule settings for the voice channel.

key -> (string)

Day of a week when the rule will be applied. Valid values are [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]

value -> (list)

Open Hour Rules.

(structure)

Open Hour Rule Details.

StartTime -> (string)

The start of the scheduled time, in ISO 8601 format, when the channel can send messages.

EndTime -> (string)

The end of the scheduled time, in ISO 8601 format, when the channel canât send messages.

CUSTOM -> (map)

Specifies the schedule settings for the custom channel.

key -> (string)

Day of a week when the rule will be applied. Valid values are [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]

value -> (list)

Open Hour Rules.

(structure)

Open Hour Rule Details.

StartTime -> (string)

The start of the scheduled time, in ISO 8601 format, when the channel can send messages.

EndTime -> (string)

The end of the scheduled time, in ISO 8601 format, when the channel canât send messages.

ClosedDays -> (structure)

The time when journey will stop sending messages. QuietTime should be configured first and SendingSchedule should be set to true.

EMAIL -> (list)

Rules for the Email channel.

(structure)

ClosedDays rule details.

Name -> (string)

The name of the closed day rule.

StartDateTime -> (string)

Start DateTime ISO 8601 format

EndDateTime -> (string)

End DateTime ISO 8601 format

SMS -> (list)

Rules for the SMS channel.

(structure)

ClosedDays rule details.

Name -> (string)

The name of the closed day rule.

StartDateTime -> (string)

Start DateTime ISO 8601 format

EndDateTime -> (string)

End DateTime ISO 8601 format

PUSH -> (list)

Rules for the Push channel.

(structure)

ClosedDays rule details.

Name -> (string)

The name of the closed day rule.

StartDateTime -> (string)

Start DateTime ISO 8601 format

EndDateTime -> (string)

End DateTime ISO 8601 format

VOICE -> (list)

Rules for the Voice channel.

(structure)

ClosedDays rule details.

Name -> (string)

The name of the closed day rule.

StartDateTime -> (string)

Start DateTime ISO 8601 format

EndDateTime -> (string)

End DateTime ISO 8601 format

CUSTOM -> (list)

Rules for the Custom channel.

(structure)

ClosedDays rule details.

Name -> (string)

The name of the closed day rule.

StartDateTime -> (string)

Start DateTime ISO 8601 format

EndDateTime -> (string)

End DateTime ISO 8601 format

TimezoneEstimationMethods -> (list)

An array of time zone estimation methods, if any, to use for determining an [Endpoints](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html) time zone if the Endpoint does not have a value for the Demographic.Timezone attribute.

- PHONE_NUMBER - A time zone is determined based on the Endpoint.Address and Endpoint.Location.Country.
- POSTAL_CODE - A time zone is determined based on the Endpoint.Location.PostalCode and Endpoint.Location.Country.

### Note

POSTAL_CODE detection is only supported in the United States, United Kingdom, Australia, New Zealand, Canada, France, Italy, Spain, Germany and in regions where Amazon Pinpoint is available.

(string)

JSON Syntax:

```
{
  "Activities": {"string": {
        "CUSTOM": {
          "DeliveryUri": "string",
          "EndpointTypes": ["PUSH"|"GCM"|"APNS"|"APNS_SANDBOX"|"APNS_VOIP"|"APNS_VOIP_SANDBOX"|"ADM"|"SMS"|"VOICE"|"EMAIL"|"BAIDU"|"CUSTOM"|"IN_APP", ...],
          "MessageConfig": {
            "Data": "string"
          },
          "NextActivity": "string",
          "TemplateName": "string",
          "TemplateVersion": "string"
        },
        "ConditionalSplit": {
          "Condition": {
            "Conditions": [
              {
                "EventCondition": {
                  "Dimensions": {
                    "Attributes": {"string": {
                          "AttributeType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEFORE"|"AFTER"|"ON"|"BETWEEN",
                          "Values": ["string", ...]
                        }
                      ...},
                    "EventType": {
                      "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                      "Values": ["string", ...]
                    },
                    "Metrics": {"string": {
                          "ComparisonOperator": "string",
                          "Value": double
                        }
                      ...}
                  },
                  "MessageActivity": "string"
                },
                "SegmentCondition": {
                  "SegmentId": "string"
                },
                "SegmentDimensions": {
                  "Attributes": {"string": {
                        "AttributeType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEFORE"|"AFTER"|"ON"|"BETWEEN",
                        "Values": ["string", ...]
                      }
                    ...},
                  "Behavior": {
                    "Recency": {
                      "Duration": "HR_24"|"DAY_7"|"DAY_14"|"DAY_30",
                      "RecencyType": "ACTIVE"|"INACTIVE"
                    }
                  },
                  "Demographic": {
                    "AppVersion": {
                      "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                      "Values": ["string", ...]
                    },
                    "Channel": {
                      "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                      "Values": ["string", ...]
                    },
                    "DeviceType": {
                      "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                      "Values": ["string", ...]
                    },
                    "Make": {
                      "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                      "Values": ["string", ...]
                    },
                    "Model": {
                      "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                      "Values": ["string", ...]
                    },
                    "Platform": {
                      "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                      "Values": ["string", ...]
                    }
                  },
                  "Location": {
                    "Country": {
                      "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                      "Values": ["string", ...]
                    },
                    "GPSPoint": {
                      "Coordinates": {
                        "Latitude": double,
                        "Longitude": double
                      },
                      "RangeInKilometers": double
                    }
                  },
                  "Metrics": {"string": {
                        "ComparisonOperator": "string",
                        "Value": double
                      }
                    ...},
                  "UserAttributes": {"string": {
                        "AttributeType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEFORE"|"AFTER"|"ON"|"BETWEEN",
                        "Values": ["string", ...]
                      }
                    ...}
                }
              }
              ...
            ],
            "Operator": "ALL"|"ANY"
          },
          "EvaluationWaitTime": {
            "WaitFor": "string",
            "WaitUntil": "string"
          },
          "FalseActivity": "string",
          "TrueActivity": "string"
        },
        "Description": "string",
        "EMAIL": {
          "MessageConfig": {
            "FromAddress": "string"
          },
          "NextActivity": "string",
          "TemplateName": "string",
          "TemplateVersion": "string"
        },
        "Holdout": {
          "NextActivity": "string",
          "Percentage": integer
        },
        "MultiCondition": {
          "Branches": [
            {
              "Condition": {
                "EventCondition": {
                  "Dimensions": {
                    "Attributes": {"string": {
                          "AttributeType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEFORE"|"AFTER"|"ON"|"BETWEEN",
                          "Values": ["string", ...]
                        }
                      ...},
                    "EventType": {
                      "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                      "Values": ["string", ...]
                    },
                    "Metrics": {"string": {
                          "ComparisonOperator": "string",
                          "Value": double
                        }
                      ...}
                  },
                  "MessageActivity": "string"
                },
                "SegmentCondition": {
                  "SegmentId": "string"
                },
                "SegmentDimensions": {
                  "Attributes": {"string": {
                        "AttributeType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEFORE"|"AFTER"|"ON"|"BETWEEN",
                        "Values": ["string", ...]
                      }
                    ...},
                  "Behavior": {
                    "Recency": {
                      "Duration": "HR_24"|"DAY_7"|"DAY_14"|"DAY_30",
                      "RecencyType": "ACTIVE"|"INACTIVE"
                    }
                  },
                  "Demographic": {
                    "AppVersion": {
                      "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                      "Values": ["string", ...]
                    },
                    "Channel": {
                      "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                      "Values": ["string", ...]
                    },
                    "DeviceType": {
                      "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                      "Values": ["string", ...]
                    },
                    "Make": {
                      "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                      "Values": ["string", ...]
                    },
                    "Model": {
                      "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                      "Values": ["string", ...]
                    },
                    "Platform": {
                      "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                      "Values": ["string", ...]
                    }
                  },
                  "Location": {
                    "Country": {
                      "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
                      "Values": ["string", ...]
                    },
                    "GPSPoint": {
                      "Coordinates": {
                        "Latitude": double,
                        "Longitude": double
                      },
                      "RangeInKilometers": double
                    }
                  },
                  "Metrics": {"string": {
                        "ComparisonOperator": "string",
                        "Value": double
                      }
                    ...},
                  "UserAttributes": {"string": {
                        "AttributeType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEFORE"|"AFTER"|"ON"|"BETWEEN",
                        "Values": ["string", ...]
                      }
                    ...}
                }
              },
              "NextActivity": "string"
            }
            ...
          ],
          "DefaultActivity": "string",
          "EvaluationWaitTime": {
            "WaitFor": "string",
            "WaitUntil": "string"
          }
        },
        "PUSH": {
          "MessageConfig": {
            "TimeToLive": "string"
          },
          "NextActivity": "string",
          "TemplateName": "string",
          "TemplateVersion": "string"
        },
        "RandomSplit": {
          "Branches": [
            {
              "NextActivity": "string",
              "Percentage": integer
            }
            ...
          ]
        },
        "SMS": {
          "MessageConfig": {
            "MessageType": "TRANSACTIONAL"|"PROMOTIONAL",
            "OriginationNumber": "string",
            "SenderId": "string",
            "EntityId": "string",
            "TemplateId": "string"
          },
          "NextActivity": "string",
          "TemplateName": "string",
          "TemplateVersion": "string"
        },
        "Wait": {
          "NextActivity": "string",
          "WaitTime": {
            "WaitFor": "string",
            "WaitUntil": "string"
          }
        },
        "ContactCenter": {
          "NextActivity": "string"
        }
      }
    ...},
  "CreationDate": "string",
  "LastModifiedDate": "string",
  "Limits": {
    "DailyCap": integer,
    "EndpointReentryCap": integer,
    "MessagesPerSecond": integer,
    "EndpointReentryInterval": "string",
    "TimeframeCap": {
      "Cap": integer,
      "Days": integer
    },
    "TotalCap": integer
  },
  "LocalTime": true|false,
  "Name": "string",
  "QuietTime": {
    "End": "string",
    "Start": "string"
  },
  "RefreshFrequency": "string",
  "Schedule": {
    "EndTime": timestamp,
    "StartTime": timestamp,
    "Timezone": "string"
  },
  "StartActivity": "string",
  "StartCondition": {
    "Description": "string",
    "EventStartCondition": {
      "EventFilter": {
        "Dimensions": {
          "Attributes": {"string": {
                "AttributeType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEFORE"|"AFTER"|"ON"|"BETWEEN",
                "Values": ["string", ...]
              }
            ...},
          "EventType": {
            "DimensionType": "INCLUSIVE"|"EXCLUSIVE",
            "Values": ["string", ...]
          },
          "Metrics": {"string": {
                "ComparisonOperator": "string",
                "Value": double
              }
            ...}
        },
        "FilterType": "SYSTEM"|"ENDPOINT"
      },
      "SegmentId": "string"
    },
    "SegmentStartCondition": {
      "SegmentId": "string"
    }
  },
  "State": "DRAFT"|"ACTIVE"|"COMPLETED"|"CANCELLED"|"CLOSED"|"PAUSED",
  "WaitForQuietTime": true|false,
  "RefreshOnSegmentUpdate": true|false,
  "JourneyChannelSettings": {
    "ConnectCampaignArn": "string",
    "ConnectCampaignExecutionRoleArn": "string"
  },
  "SendingSchedule": true|false,
  "OpenHours": {
    "EMAIL": {"MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY"|"SATURDAY"|"SUNDAY": [
          {
            "StartTime": "string",
            "EndTime": "string"
          }
          ...
        ]
      ...},
    "SMS": {"MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY"|"SATURDAY"|"SUNDAY": [
          {
            "StartTime": "string",
            "EndTime": "string"
          }
          ...
        ]
      ...},
    "PUSH": {"MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY"|"SATURDAY"|"SUNDAY": [
          {
            "StartTime": "string",
            "EndTime": "string"
          }
          ...
        ]
      ...},
    "VOICE": {"MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY"|"SATURDAY"|"SUNDAY": [
          {
            "StartTime": "string",
            "EndTime": "string"
          }
          ...
        ]
      ...},
    "CUSTOM": {"MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY"|"SATURDAY"|"SUNDAY": [
          {
            "StartTime": "string",
            "EndTime": "string"
          }
          ...
        ]
      ...}
  },
  "ClosedDays": {
    "EMAIL": [
      {
        "Name": "string",
        "StartDateTime": "string",
        "EndDateTime": "string"
      }
      ...
    ],
    "SMS": [
      {
        "Name": "string",
        "StartDateTime": "string",
        "EndDateTime": "string"
      }
      ...
    ],
    "PUSH": [
      {
        "Name": "string",
        "StartDateTime": "string",
        "EndDateTime": "string"
      }
      ...
    ],
    "VOICE": [
      {
        "Name": "string",
        "StartDateTime": "string",
        "EndDateTime": "string"
      }
      ...
    ],
    "CUSTOM": [
      {
        "Name": "string",
        "StartDateTime": "string",
        "EndDateTime": "string"
      }
      ...
    ]
  },
  "TimezoneEstimationMethods": ["PHONE_NUMBER"|"POSTAL_CODE", ...]
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

JourneyResponse -> (structure)

Provides information about the status, configuration, and other settings for a journey.

Activities -> (map)

A map that contains a set of Activity objects, one object for each activity in the journey. For each Activity object, the key is the unique identifier (string) for an activity and the value is the settings for the activity.

key -> (string)

value -> (structure)

Specifies the configuration and other settings for an activity in a journey.

CUSTOM -> (structure)

The settings for a custom message activity. This type of activity calls an AWS Lambda function or web hook that sends messages to participants.

DeliveryUri -> (string)

The destination to send the campaign or treatment to. This value can be one of the following:

- The name or Amazon Resource Name (ARN) of an AWS Lambda function to invoke to handle delivery of the campaign or treatment.
- The URL for a web application or service that supports HTTPS and can receive the message. The URL has to be a full URL, including the HTTPS protocol.

EndpointTypes -> (list)

The types of endpoints to send the custom message to. Each valid value maps to a type of channel that you can associate with an endpoint by using the ChannelType property of an endpoint.

(string)

MessageConfig -> (structure)

Specifies the message data included in a custom channel message thatâs sent to participants in a journey.

Data -> (string)

The message content thatâs passed to an AWS Lambda function or to a web hook.

NextActivity -> (string)

The unique identifier for the next activity to perform, after Amazon Pinpoint calls the AWS Lambda function or web hook.

TemplateName -> (string)

The name of the custom message template to use for the message. If specified, this value must match the name of an existing message template.

TemplateVersion -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

ConditionalSplit -> (structure)

The settings for a yes/no split activity. This type of activity sends participants down one of two paths in a journey, based on conditions that you specify.

Condition -> (structure)

The conditions that define the paths for the activity, and the relationship between the conditions.

Conditions -> (list)

The conditions to evaluate for the activity.

(structure)

Specifies a condition to evaluate for an activity in a journey.

EventCondition -> (structure)

The dimension settings for the event thatâs associated with the activity.

Dimensions -> (structure)

The dimensions for the event filter to use for the activity.

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

MessageActivity -> (string)

The message identifier (message_id) for the message to use when determining whether message events meet the condition.

SegmentCondition -> (structure)

The segment thatâs associated with the activity.

SegmentId -> (string)

The unique identifier for the segment to associate with the activity.

SegmentDimensions -> (structure)

The dimension settings for the segment thatâs associated with the activity.

Attributes -> (map)

One or more custom attributes to use as criteria for the segment.

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

Behavior -> (structure)

The behavior-based criteria, such as how recently users have used your app, for the segment.

Recency -> (structure)

The dimension settings that are based on how recently an endpoint was active.

Duration -> (string)

The duration to use when determining whether an endpoint is active or inactive.

RecencyType -> (string)

The type of recency dimension to use for the segment. Valid values are: ACTIVE, endpoints that were active within the specified duration are included in the segment; and, INACTIVE, endpoints that werenât active within the specified duration are included in the segment.

Demographic -> (structure)

The demographic-based criteria, such as device platform, for the segment.

AppVersion -> (structure)

The app version criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Channel -> (structure)

The channel criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

DeviceType -> (structure)

The device type criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Make -> (structure)

The device make criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Model -> (structure)

The device model criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Platform -> (structure)

The device platform criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Location -> (structure)

The location-based criteria, such as region or GPS coordinates, for the segment.

Country -> (structure)

The country or region code, in ISO 3166-1 alpha-2 format, for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

GPSPoint -> (structure)

The GPS location and range for the segment.

Coordinates -> (structure)

The GPS coordinates to measure distance from.

Latitude -> (double)

The latitude coordinate of the location.

Longitude -> (double)

The longitude coordinate of the location.

RangeInKilometers -> (double)

The range, in kilometers, from the GPS coordinates.

Metrics -> (map)

One or more custom metrics to use as criteria for the segment.

key -> (string)

value -> (structure)

Specifies metric-based criteria for including or excluding endpoints from a segment. These criteria derive from custom metrics that you define for endpoints.

ComparisonOperator -> (string)

The operator to use when comparing metric values. Valid values are: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, and EQUAL.

Value -> (double)

The value to compare.

UserAttributes -> (map)

One or more custom user attributes to use as criteria for the segment.

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

Operator -> (string)

Specifies how to handle multiple conditions for the activity. For example, if you specify two conditions for an activity, whether both or only one of the conditions must be met for the activity to be performed.

EvaluationWaitTime -> (structure)

The amount of time to wait before determining whether the conditions are met, or the date and time when Amazon Pinpoint determines whether the conditions are met.

WaitFor -> (string)

The amount of time to wait, as a duration in ISO 8601 format, before determining whether the activityâs conditions have been met or moving participants to the next activity in the journey.

WaitUntil -> (string)

The date and time, in ISO 8601 format, when Amazon Pinpoint determines whether the activityâs conditions have been met or the activity moves participants to the next activity in the journey.

FalseActivity -> (string)

The unique identifier for the activity to perform if the conditions arenât met.

TrueActivity -> (string)

The unique identifier for the activity to perform if the conditions are met.

Description -> (string)

The custom description of the activity.

EMAIL -> (structure)

The settings for an email activity. This type of activity sends an email message to participants.

MessageConfig -> (structure)

Specifies the sender address for an email message thatâs sent to participants in the journey.

FromAddress -> (string)

The verified email address to send the email message from. The default address is the FromAddress specified for the email channel for the application.

NextActivity -> (string)

The unique identifier for the next activity to perform, after the message is sent.

TemplateName -> (string)

The name of the email message template to use for the message. If specified, this value must match the name of an existing message template.

TemplateVersion -> (string)

The unique identifier for the version of the email template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

Holdout -> (structure)

The settings for a holdout activity. This type of activity stops a journey for a specified percentage of participants.

NextActivity -> (string)

The unique identifier for the next activity to perform, after performing the holdout activity.

Percentage -> (integer)

The percentage of participants who shouldnât continue the journey.

To determine which participants are held out, Amazon Pinpoint applies a probability-based algorithm to the percentage that you specify. Therefore, the actual percentage of participants who are held out may not be equal to the percentage that you specify.

MultiCondition -> (structure)

The settings for a multivariate split activity. This type of activity sends participants down one of as many as five paths (including a default *Else* path) in a journey, based on conditions that you specify.

Branches -> (list)

The paths for the activity, including the conditions for entering each path and the activity to perform for each path.

(structure)

Specifies a condition to evaluate for an activity path in a journey.

Condition -> (structure)

The condition to evaluate for the activity path.

EventCondition -> (structure)

The dimension settings for the event thatâs associated with the activity.

Dimensions -> (structure)

The dimensions for the event filter to use for the activity.

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

MessageActivity -> (string)

The message identifier (message_id) for the message to use when determining whether message events meet the condition.

SegmentCondition -> (structure)

The segment thatâs associated with the activity.

SegmentId -> (string)

The unique identifier for the segment to associate with the activity.

SegmentDimensions -> (structure)

The dimension settings for the segment thatâs associated with the activity.

Attributes -> (map)

One or more custom attributes to use as criteria for the segment.

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

Behavior -> (structure)

The behavior-based criteria, such as how recently users have used your app, for the segment.

Recency -> (structure)

The dimension settings that are based on how recently an endpoint was active.

Duration -> (string)

The duration to use when determining whether an endpoint is active or inactive.

RecencyType -> (string)

The type of recency dimension to use for the segment. Valid values are: ACTIVE, endpoints that were active within the specified duration are included in the segment; and, INACTIVE, endpoints that werenât active within the specified duration are included in the segment.

Demographic -> (structure)

The demographic-based criteria, such as device platform, for the segment.

AppVersion -> (structure)

The app version criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Channel -> (structure)

The channel criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

DeviceType -> (structure)

The device type criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Make -> (structure)

The device make criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Model -> (structure)

The device model criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Platform -> (structure)

The device platform criteria for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

Location -> (structure)

The location-based criteria, such as region or GPS coordinates, for the segment.

Country -> (structure)

The country or region code, in ISO 3166-1 alpha-2 format, for the segment.

DimensionType -> (string)

The type of segment dimension to use. Valid values are: INCLUSIVE, endpoints that match the criteria are included in the segment; and, EXCLUSIVE, endpoints that match the criteria are excluded from the segment.

Values -> (list)

The criteria values to use for the segment dimension. Depending on the value of the DimensionType property, endpoints are included or excluded from the segment if their values match the criteria values.

(string)

GPSPoint -> (structure)

The GPS location and range for the segment.

Coordinates -> (structure)

The GPS coordinates to measure distance from.

Latitude -> (double)

The latitude coordinate of the location.

Longitude -> (double)

The longitude coordinate of the location.

RangeInKilometers -> (double)

The range, in kilometers, from the GPS coordinates.

Metrics -> (map)

One or more custom metrics to use as criteria for the segment.

key -> (string)

value -> (structure)

Specifies metric-based criteria for including or excluding endpoints from a segment. These criteria derive from custom metrics that you define for endpoints.

ComparisonOperator -> (string)

The operator to use when comparing metric values. Valid values are: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, and EQUAL.

Value -> (double)

The value to compare.

UserAttributes -> (map)

One or more custom user attributes to use as criteria for the segment.

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

NextActivity -> (string)

The unique identifier for the next activity to perform, after completing the activity for the path.

DefaultActivity -> (string)

The unique identifier for the activity to perform for participants who donât meet any of the conditions specified for other paths in the activity.

EvaluationWaitTime -> (structure)

The amount of time to wait or the date and time when Amazon Pinpoint determines whether the conditions are met.

WaitFor -> (string)

The amount of time to wait, as a duration in ISO 8601 format, before determining whether the activityâs conditions have been met or moving participants to the next activity in the journey.

WaitUntil -> (string)

The date and time, in ISO 8601 format, when Amazon Pinpoint determines whether the activityâs conditions have been met or the activity moves participants to the next activity in the journey.

PUSH -> (structure)

The settings for a push notification activity. This type of activity sends a push notification to participants.

MessageConfig -> (structure)

Specifies the time to live (TTL) value for push notifications that are sent to participants in a journey.

TimeToLive -> (string)

The number of seconds that the push notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

NextActivity -> (string)

The unique identifier for the next activity to perform, after the message is sent.

TemplateName -> (string)

The name of the push notification template to use for the message. If specified, this value must match the name of an existing message template.

TemplateVersion -> (string)

The unique identifier for the version of the push notification template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

RandomSplit -> (structure)

The settings for a random split activity. This type of activity randomly sends specified percentages of participants down one of as many as five paths in a journey, based on conditions that you specify.

Branches -> (list)

The paths for the activity, including the percentage of participants to enter each path and the activity to perform for each path.

(structure)

Specifies the settings for a path in a random split activity in a journey.

NextActivity -> (string)

The unique identifier for the next activity to perform, after completing the activity for the path.

Percentage -> (integer)

The percentage of participants to send down the activity path.

To determine which participants are sent down each path, Amazon Pinpoint applies a probability-based algorithm to the percentages that you specify for the paths. Therefore, the actual percentage of participants who are sent down a path may not be equal to the percentage that you specify.

SMS -> (structure)

The settings for an SMS activity. This type of activity sends a text message to participants.

MessageConfig -> (structure)

Specifies the sender ID and message type for an SMS message thatâs sent to participants in a journey.

MessageType -> (string)

The SMS message type. Valid values are TRANSACTIONAL (for messages that are critical or time-sensitive, such as a one-time passwords) and PROMOTIONAL (for messsages that arenât critical or time-sensitive, such as marketing messages).

OriginationNumber -> (string)

The long code to send the SMS message from. This value should be one of the dedicated long codes thatâs assigned to your AWS account. Although it isnât required, we recommend that you specify the long code using an E.164 format to ensure prompt and accurate delivery of the message. For example, +12065550100.

SenderId -> (string)

The sender ID to display as the sender of the message on a recipientâs device. Support for sender IDs varies by country or region. For more information, see [Supported Countries and Regions](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-countries.html) in the Amazon Pinpoint User Guide.

EntityId -> (string)

The entity ID or Principal Entity (PE) id received from the regulatory body for sending SMS in your country.

TemplateId -> (string)

The template ID received from the regulatory body for sending SMS in your country.

NextActivity -> (string)

The unique identifier for the next activity to perform, after the message is sent.

TemplateName -> (string)

The name of the SMS message template to use for the message. If specified, this value must match the name of an existing message template.

TemplateVersion -> (string)

The unique identifier for the version of the SMS template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

Wait -> (structure)

The settings for a wait activity. This type of activity waits for a certain amount of time or until a specific date and time before moving participants to the next activity in a journey.

NextActivity -> (string)

The unique identifier for the next activity to perform, after performing the wait activity.

WaitTime -> (structure)

The amount of time to wait or the date and time when the activity moves participants to the next activity in the journey.

WaitFor -> (string)

The amount of time to wait, as a duration in ISO 8601 format, before determining whether the activityâs conditions have been met or moving participants to the next activity in the journey.

WaitUntil -> (string)

The date and time, in ISO 8601 format, when Amazon Pinpoint determines whether the activityâs conditions have been met or the activity moves participants to the next activity in the journey.

ContactCenter -> (structure)

The settings for a connect activity. This type of activity initiates a contact center call to participants.

NextActivity -> (string)

The unique identifier for the next activity to perform after the this activity.

ApplicationId -> (string)

The unique identifier for the application that the journey applies to.

CreationDate -> (string)

The date, in ISO 8601 format, when the journey was created.

Id -> (string)

The unique identifier for the journey.

LastModifiedDate -> (string)

The date, in ISO 8601 format, when the journey was last modified.

Limits -> (structure)

The messaging and entry limits for the journey.

DailyCap -> (integer)

The maximum number of messages that the journey can send to a single participant during a 24-hour period. The maximum value is 100.

EndpointReentryCap -> (integer)

The maximum number of times that a participant can enter the journey. The maximum value is 100. To allow participants to enter the journey an unlimited number of times, set this value to 0.

MessagesPerSecond -> (integer)

The maximum number of messages that the journey can send each second.

EndpointReentryInterval -> (string)

Minimum time that must pass before an endpoint can re-enter a given journey. The duration should use an ISO 8601 format, such as PT1H.

TimeframeCap -> (structure)

The number of messages that an endpoint can receive during the specified timeframe.

Cap -> (integer)

The maximum number of messages that all journeys can send to an endpoint during the specified timeframe. The maximum value is 100. If set to 0, this limit will not apply.

Days -> (integer)

The length of the timeframe in days. The maximum value is 30. If set to 0, this limit will not apply.

TotalCap -> (integer)

The maximum number of messages a journey can sent to a single endpoint. The maximum value is 100. If set to 0, this limit will not apply.

LocalTime -> (boolean)

Specifies whether the journeyâs scheduled start and end times use each participantâs local time. If this value is true, the schedule uses each participantâs local time.

Name -> (string)

The name of the journey.

QuietTime -> (structure)

The quiet time settings for the journey. Quiet time is a specific time range when a journey doesnât send messages to participants, if all the following conditions are met:

- The EndpointDemographic.Timezone property of the endpoint for the participant is set to a valid value.
- The current time in the participantâs time zone is later than or equal to the time specified by the QuietTime.Start property for the journey.
- The current time in the participantâs time zone is earlier than or equal to the time specified by the QuietTime.End property for the journey.

If any of the preceding conditions isnât met, the participant will receive messages from the journey, even if quiet time is enabled.

End -> (string)

The specific time when quiet time ends. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.

Start -> (string)

The specific time when quiet time begins. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.

RefreshFrequency -> (string)

The frequency with which Amazon Pinpoint evaluates segment and event data for the journey, as a duration in ISO 8601 format.

Schedule -> (structure)

The schedule settings for the journey.

EndTime -> (timestamp)

The scheduled time, in ISO 8601 format, when the journey ended or will end.

StartTime -> (timestamp)

The scheduled time, in ISO 8601 format, when the journey began or will begin.

Timezone -> (string)

The starting UTC offset for the journey schedule, if the value of the journeyâs LocalTime property is true. Valid values are: UTC, UTC+01, UTC+02, UTC+03, UTC+03:30, UTC+04, UTC+04:30, UTC+05, UTC+05:30, UTC+05:45, UTC+06, UTC+06:30, UTC+07, UTC+08, UTC+08:45, UTC+09, UTC+09:30, UTC+10, UTC+10:30, UTC+11, UTC+12, UTC+12:45, UTC+13, UTC+13:45, UTC-02, UTC-02:30, UTC-03, UTC-03:30, UTC-04, UTC-05, UTC-06, UTC-07, UTC-08, UTC-09, UTC-09:30, UTC-10, and UTC-11.

StartActivity -> (string)

The unique identifier for the first activity in the journey.

StartCondition -> (structure)

The segment that defines which users are participants in the journey.

Description -> (string)

The custom description of the condition.

EventStartCondition -> (structure)

Specifies the settings for an event that causes a journey activity to start.

EventFilter -> (structure)

Specifies the settings for an event that causes a campaign to be sent or a journey activity to be performed.

Dimensions -> (structure)

The dimensions for the event filter to use for the campaign or the journey activity.

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

The type of event that causes the campaign to be sent or the journey activity to be performed. Valid values are: SYSTEM, sends the campaign or performs the activity when a system event occurs; and, ENDPOINT, sends the campaign or performs the activity when an endpoint event (Events resource) occurs.

SegmentId -> (string)

SegmentStartCondition -> (structure)

The segment thatâs associated with the first activity in the journey. This segment determines which users are participants in the journey.

SegmentId -> (string)

The unique identifier for the segment to associate with the activity.

State -> (string)

The current status of the journey. Possible values are:

- DRAFT - The journey is being developed and hasnât been published yet.
- ACTIVE - The journey has been developed and published. Depending on the journeyâs schedule, the journey may currently be running or scheduled to start running at a later time. If a journeyâs status is ACTIVE, you canât add, change, or remove activities from it.
- COMPLETED - The journey has been published and has finished running. All participants have entered the journey and no participants are waiting to complete the journey or any activities in the journey.
- CANCELLED - The journey has been stopped. If a journeyâs status is CANCELLED, you canât add, change, or remove activities or segment settings from the journey.
- CLOSED - The journey has been published and has started running. It may have also passed its scheduled end time, or passed its scheduled start time and a refresh frequency hasnât been specified for it. If a journeyâs status is CLOSED, you canât add participants to it, and no existing participants can enter the journey for the first time. However, any existing participants who are currently waiting to start an activity may continue the journey.

tags -> (map)

This object is not used or supported.

key -> (string)

value -> (string)

WaitForQuietTime -> (boolean)

Indicates whether endpoints in quiet hours should enter a wait activity until quiet hours have elapsed.

RefreshOnSegmentUpdate -> (boolean)

Indicates whether the journey participants should be refreshed when a segment is updated.

JourneyChannelSettings -> (structure)

The channel-specific configurations for the journey.

ConnectCampaignArn -> (string)

Amazon Resource Name (ARN) of the Connect Campaign.

ConnectCampaignExecutionRoleArn -> (string)

IAM role ARN to be assumed when invoking Connect campaign execution APIs for dialing.

SendingSchedule -> (boolean)

Indicates if journey has Advance Quiet Time enabled. This flag should be set to true in order to allow using OpenHours and ClosedDays.

OpenHours -> (structure)

The time when a journey can send messages. QuietTime should be configured first and SendingSchedule should be set to true.

EMAIL -> (map)

Specifies the schedule settings for the email channel.

key -> (string)

Day of a week when the rule will be applied. Valid values are [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]

value -> (list)

Open Hour Rules.

(structure)

Open Hour Rule Details.

StartTime -> (string)

The start of the scheduled time, in ISO 8601 format, when the channel can send messages.

EndTime -> (string)

The end of the scheduled time, in ISO 8601 format, when the channel canât send messages.

SMS -> (map)

Specifies the schedule settings for the SMS channel.

key -> (string)

Day of a week when the rule will be applied. Valid values are [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]

value -> (list)

Open Hour Rules.

(structure)

Open Hour Rule Details.

StartTime -> (string)

The start of the scheduled time, in ISO 8601 format, when the channel can send messages.

EndTime -> (string)

The end of the scheduled time, in ISO 8601 format, when the channel canât send messages.

PUSH -> (map)

Specifies the schedule settings for the push channel.

key -> (string)

Day of a week when the rule will be applied. Valid values are [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]

value -> (list)

Open Hour Rules.

(structure)

Open Hour Rule Details.

StartTime -> (string)

The start of the scheduled time, in ISO 8601 format, when the channel can send messages.

EndTime -> (string)

The end of the scheduled time, in ISO 8601 format, when the channel canât send messages.

VOICE -> (map)

Specifies the schedule settings for the voice channel.

key -> (string)

Day of a week when the rule will be applied. Valid values are [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]

value -> (list)

Open Hour Rules.

(structure)

Open Hour Rule Details.

StartTime -> (string)

The start of the scheduled time, in ISO 8601 format, when the channel can send messages.

EndTime -> (string)

The end of the scheduled time, in ISO 8601 format, when the channel canât send messages.

CUSTOM -> (map)

Specifies the schedule settings for the custom channel.

key -> (string)

Day of a week when the rule will be applied. Valid values are [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]

value -> (list)

Open Hour Rules.

(structure)

Open Hour Rule Details.

StartTime -> (string)

The start of the scheduled time, in ISO 8601 format, when the channel can send messages.

EndTime -> (string)

The end of the scheduled time, in ISO 8601 format, when the channel canât send messages.

ClosedDays -> (structure)

The time when a journey will not send messages. QuietTime should be configured first and SendingSchedule should be set to true.

EMAIL -> (list)

Rules for the Email channel.

(structure)

ClosedDays rule details.

Name -> (string)

The name of the closed day rule.

StartDateTime -> (string)

Start DateTime ISO 8601 format

EndDateTime -> (string)

End DateTime ISO 8601 format

SMS -> (list)

Rules for the SMS channel.

(structure)

ClosedDays rule details.

Name -> (string)

The name of the closed day rule.

StartDateTime -> (string)

Start DateTime ISO 8601 format

EndDateTime -> (string)

End DateTime ISO 8601 format

PUSH -> (list)

Rules for the Push channel.

(structure)

ClosedDays rule details.

Name -> (string)

The name of the closed day rule.

StartDateTime -> (string)

Start DateTime ISO 8601 format

EndDateTime -> (string)

End DateTime ISO 8601 format

VOICE -> (list)

Rules for the Voice channel.

(structure)

ClosedDays rule details.

Name -> (string)

The name of the closed day rule.

StartDateTime -> (string)

Start DateTime ISO 8601 format

EndDateTime -> (string)

End DateTime ISO 8601 format

CUSTOM -> (list)

Rules for the Custom channel.

(structure)

ClosedDays rule details.

Name -> (string)

The name of the closed day rule.

StartDateTime -> (string)

Start DateTime ISO 8601 format

EndDateTime -> (string)

End DateTime ISO 8601 format

TimezoneEstimationMethods -> (list)

An array of time zone estimation methods, if any, to use for determining an [Endpoints](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html) time zone if the Endpoint does not have a value for the Demographic.Timezone attribute.

- PHONE_NUMBER - A time zone is determined based on the Endpoint.Address and Endpoint.Location.Country.
- POSTAL_CODE - A time zone is determined based on the Endpoint.Location.PostalCode and Endpoint.Location.Country.

### Note

POSTAL_CODE detection is only supported in the United States, United Kingdom, Australia, New Zealand, Canada, France, Italy, Spain, Germany and in regions where Amazon Pinpoint is available.

(string)