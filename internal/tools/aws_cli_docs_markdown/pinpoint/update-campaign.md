# update-campaignÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-campaign.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-campaign.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/index.html#cli-aws-pinpoint) ]

# update-campaign

## Description

Updates the configuration and other settings for a campaign.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/UpdateCampaign)

## Synopsis

```
update-campaign
--application-id <value>
--campaign-id <value>
--write-campaign-request <value>
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

`--campaign-id` (string)

The unique identifier for the campaign.

`--write-campaign-request` (structure)

Specifies the configuration and other settings for a campaign.

AdditionalTreatments -> (list)

An array of requests that defines additional treatments for the campaign, in addition to the default treatment for the campaign.

(structure)

Specifies the settings for a campaign treatment. A *treatment* is a variation of a campaign thatâs used for A/B testing of a campaign.

CustomDeliveryConfiguration -> (structure)

The delivery configuration settings for sending the treatment through a custom channel. This object is required if the MessageConfiguration object for the treatment specifies a CustomMessage object.

DeliveryUri -> (string)

The destination to send the campaign or treatment to. This value can be one of the following:

- The name or Amazon Resource Name (ARN) of an AWS Lambda function to invoke to handle delivery of the campaign or treatment.
- The URL for a web application or service that supports HTTPS and can receive the message. The URL has to be a full URL, including the HTTPS protocol.

EndpointTypes -> (list)

The types of endpoints to send the campaign or treatment to. Each valid value maps to a type of channel that you can associate with an endpoint by using the ChannelType property of an endpoint.

(string)

MessageConfiguration -> (structure)

The message configuration settings for the treatment.

ADMMessage -> (structure)

The message that the campaign sends through the ADM (Amazon Device Messaging) channel. If specified, this message overrides the default message.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

APNSMessage -> (structure)

The message that the campaign sends through the APNs (Apple Push Notification service) channel. If specified, this message overrides the default message.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

BaiduMessage -> (structure)

The message that the campaign sends through the Baidu (Baidu Cloud Push) channel. If specified, this message overrides the default message.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

CustomMessage -> (structure)

The message that the campaign sends through a custom channel, as specified by the delivery configuration (CustomDeliveryConfiguration) settings for the campaign. If specified, this message overrides the default message.

Data -> (string)

The raw, JSON-formatted string to use as the payload for the message. The maximum size is 5 KB.

DefaultMessage -> (structure)

The default message that the campaign sends through all the channels that are configured for the campaign.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

EmailMessage -> (structure)

The message that the campaign sends through the email channel. If specified, this message overrides the default message.

Body -> (string)

The body of the email for recipients whose email clients donât render HTML content.

FromAddress -> (string)

The verified email address to send the email from. The default address is the FromAddress specified for the email channel for the application.

Headers -> (list)

The list of [MessageHeaders](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id.html#apps-application-id-campaigns-campaign-id-model-messageheader) for the email. You can have up to 15 MessageHeaders for each email.

(structure)

Contains the name and value pair of an email header to add to your email. You can have up to 15 MessageHeaders. A header can contain information such as the sender, receiver, route, or timestamp.

Name -> (string)

The name of the message header. The header name can contain up to 126 characters.

Value -> (string)

The value of the message header. The header value can contain up to 870 characters, including the length of any rendered attributes. For example if you add the {CreationDate} attribute, it renders as YYYY-MM-DDTHH:MM:SS.SSSZ and is 24 characters in length.

HtmlBody -> (string)

The body of the email, in HTML format, for recipients whose email clients render HTML content.

Title -> (string)

The subject line, or title, of the email.

GCMMessage -> (structure)

The message that the campaign sends through the GCM channel, which enables Amazon Pinpoint to send push notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service. If specified, this message overrides the default message.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

SMSMessage -> (structure)

The message that the campaign sends through the SMS channel. If specified, this message overrides the default message.

Body -> (string)

The body of the SMS message.

MessageType -> (string)

The SMS message type. Valid values are TRANSACTIONAL (for messages that are critical or time-sensitive, such as a one-time passwords) and PROMOTIONAL (for messsages that arenât critical or time-sensitive, such as marketing messages).

OriginationNumber -> (string)

The long code to send the SMS message from. This value should be one of the dedicated long codes thatâs assigned to your AWS account. Although it isnât required, we recommend that you specify the long code using an E.164 format to ensure prompt and accurate delivery of the message. For example, +12065550100.

SenderId -> (string)

The sender ID to display on recipientsâ devices when they receive the SMS message.

EntityId -> (string)

The entity ID or Principal Entity (PE) id received from the regulatory body for sending SMS in your country.

TemplateId -> (string)

The template ID received from the regulatory body for sending SMS in your country.

InAppMessage -> (structure)

The in-app message configuration.

Body -> (string)

The message body of the notification, the email body or the text message.

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

Custom config to be sent to client.

key -> (string)

value -> (string)

Layout -> (string)

In-app message layout.

Schedule -> (structure)

The schedule settings for the treatment.

EndTime -> (string)

The scheduled time, in ISO 8601 format, when the campaign ended or will end.

EventFilter -> (structure)

The type of event that causes the campaign to be sent, if the value of the Frequency property is EVENT.

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

Frequency -> (string)

Specifies how often the campaign is sent or whether the campaign is sent in response to a specific event.

IsLocalTime -> (boolean)

Specifies whether the start and end times for the campaign schedule use each recipientâs local time. To base the schedule on each recipientâs local time, set this value to true.

QuietTime -> (structure)

The default quiet time for the campaign. Quiet time is a specific time range when a campaign doesnât send messages to endpoints, if all the following conditions are met:

- The EndpointDemographic.Timezone property of the endpoint is set to a valid value.
- The current time in the endpointâs time zone is later than or equal to the time specified by the QuietTime.Start property for the campaign.
- The current time in the endpointâs time zone is earlier than or equal to the time specified by the QuietTime.End property for the campaign.

If any of the preceding conditions isnât met, the endpoint will receive messages from the campaign, even if quiet time is enabled.

End -> (string)

The specific time when quiet time ends. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.

Start -> (string)

The specific time when quiet time begins. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.

StartTime -> (string)

The scheduled time when the campaign began or will begin. Valid values are: IMMEDIATE, to start the campaign immediately; or, a specific time in ISO 8601 format.

Timezone -> (string)

The starting UTC offset for the campaign schedule, if the value of the IsLocalTime property is true. Valid values are: UTC, UTC+01, UTC+02, UTC+03, UTC+03:30, UTC+04, UTC+04:30, UTC+05, UTC+05:30, UTC+05:45, UTC+06, UTC+06:30, UTC+07, UTC+08, UTC+09, UTC+09:30, UTC+10, UTC+10:30, UTC+11, UTC+12, UTC+13, UTC-02, UTC-03, UTC-04, UTC-05, UTC-06, UTC-07, UTC-08, UTC-09, UTC-10, and UTC-11.

SizePercent -> (integer)

The allocated percentage of users (segment members) to send the treatment to.

TemplateConfiguration -> (structure)

The message template to use for the treatment.

EmailTemplate -> (structure)

The email template to use for the message.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

PushTemplate -> (structure)

The push notification template to use for the message.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

SMSTemplate -> (structure)

The SMS template to use for the message.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

VoiceTemplate -> (structure)

The voice template to use for the message. This object isnât supported for campaigns.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

InAppTemplate -> (structure)

The InApp template to use for the message. The InApp template object is not supported for SendMessages.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

TreatmentDescription -> (string)

A custom description of the treatment.

TreatmentName -> (string)

A custom name for the treatment.

CustomDeliveryConfiguration -> (structure)

The delivery configuration settings for sending the campaign through a custom channel. This object is required if the MessageConfiguration object for the campaign specifies a CustomMessage object.

DeliveryUri -> (string)

The destination to send the campaign or treatment to. This value can be one of the following:

- The name or Amazon Resource Name (ARN) of an AWS Lambda function to invoke to handle delivery of the campaign or treatment.
- The URL for a web application or service that supports HTTPS and can receive the message. The URL has to be a full URL, including the HTTPS protocol.

EndpointTypes -> (list)

The types of endpoints to send the campaign or treatment to. Each valid value maps to a type of channel that you can associate with an endpoint by using the ChannelType property of an endpoint.

(string)

Description -> (string)

A custom description of the campaign.

HoldoutPercent -> (integer)

The allocated percentage of users (segment members) who shouldnât receive messages from the campaign.

Hook -> (structure)

The settings for the AWS Lambda function to invoke as a code hook for the campaign. You can use this hook to customize the segment thatâs used by the campaign.

LambdaFunctionName -> (string)

The name or Amazon Resource Name (ARN) of the AWS Lambda function that Amazon Pinpoint invokes to customize a segment for a campaign.

Mode -> (string)

The mode that Amazon Pinpoint uses to invoke the AWS Lambda function. Possible values are:

- FILTER - Invoke the function to customize the segment thatâs used by a campaign.
- DELIVERY - (Deprecated) Previously, invoked the function to send a campaign through a custom channel. This functionality is not supported anymore. To send a campaign through a custom channel, use the CustomDeliveryConfiguration and CampaignCustomMessage objects of the campaign.

WebUrl -> (string)

The web URL that Amazon Pinpoint calls to invoke the AWS Lambda function over HTTPS.

IsPaused -> (boolean)

Specifies whether to pause the campaign. A paused campaign doesnât run unless you resume it by changing this value to false.

Limits -> (structure)

The messaging limits for the campaign.

Daily -> (integer)

The maximum number of messages that a campaign can send to a single endpoint during a 24-hour period. For an application, this value specifies the default limit for the number of messages that campaigns and journeys can send to a single endpoint during a 24-hour period. The maximum value is 100.

MaximumDuration -> (integer)

The maximum amount of time, in seconds, that a campaign can attempt to deliver a message after the scheduled start time for the campaign. The minimum value is 60 seconds.

MessagesPerSecond -> (integer)

The maximum number of messages that a campaign can send each second. For an application, this value specifies the default limit for the number of messages that campaigns can send each second. The minimum value is 1. The maximum value is 20,000.

Total -> (integer)

The maximum number of messages that a campaign can send to a single endpoint during the course of the campaign. If a campaign recurs, this setting applies to all runs of the campaign. The maximum value is 100.

Session -> (integer)

The maximum total number of messages that the campaign can send per user session.

MessageConfiguration -> (structure)

The message configuration settings for the campaign.

ADMMessage -> (structure)

The message that the campaign sends through the ADM (Amazon Device Messaging) channel. If specified, this message overrides the default message.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

APNSMessage -> (structure)

The message that the campaign sends through the APNs (Apple Push Notification service) channel. If specified, this message overrides the default message.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

BaiduMessage -> (structure)

The message that the campaign sends through the Baidu (Baidu Cloud Push) channel. If specified, this message overrides the default message.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

CustomMessage -> (structure)

The message that the campaign sends through a custom channel, as specified by the delivery configuration (CustomDeliveryConfiguration) settings for the campaign. If specified, this message overrides the default message.

Data -> (string)

The raw, JSON-formatted string to use as the payload for the message. The maximum size is 5 KB.

DefaultMessage -> (structure)

The default message that the campaign sends through all the channels that are configured for the campaign.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

EmailMessage -> (structure)

The message that the campaign sends through the email channel. If specified, this message overrides the default message.

Body -> (string)

The body of the email for recipients whose email clients donât render HTML content.

FromAddress -> (string)

The verified email address to send the email from. The default address is the FromAddress specified for the email channel for the application.

Headers -> (list)

The list of [MessageHeaders](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id.html#apps-application-id-campaigns-campaign-id-model-messageheader) for the email. You can have up to 15 MessageHeaders for each email.

(structure)

Contains the name and value pair of an email header to add to your email. You can have up to 15 MessageHeaders. A header can contain information such as the sender, receiver, route, or timestamp.

Name -> (string)

The name of the message header. The header name can contain up to 126 characters.

Value -> (string)

The value of the message header. The header value can contain up to 870 characters, including the length of any rendered attributes. For example if you add the {CreationDate} attribute, it renders as YYYY-MM-DDTHH:MM:SS.SSSZ and is 24 characters in length.

HtmlBody -> (string)

The body of the email, in HTML format, for recipients whose email clients render HTML content.

Title -> (string)

The subject line, or title, of the email.

GCMMessage -> (structure)

The message that the campaign sends through the GCM channel, which enables Amazon Pinpoint to send push notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service. If specified, this message overrides the default message.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

SMSMessage -> (structure)

The message that the campaign sends through the SMS channel. If specified, this message overrides the default message.

Body -> (string)

The body of the SMS message.

MessageType -> (string)

The SMS message type. Valid values are TRANSACTIONAL (for messages that are critical or time-sensitive, such as a one-time passwords) and PROMOTIONAL (for messsages that arenât critical or time-sensitive, such as marketing messages).

OriginationNumber -> (string)

The long code to send the SMS message from. This value should be one of the dedicated long codes thatâs assigned to your AWS account. Although it isnât required, we recommend that you specify the long code using an E.164 format to ensure prompt and accurate delivery of the message. For example, +12065550100.

SenderId -> (string)

The sender ID to display on recipientsâ devices when they receive the SMS message.

EntityId -> (string)

The entity ID or Principal Entity (PE) id received from the regulatory body for sending SMS in your country.

TemplateId -> (string)

The template ID received from the regulatory body for sending SMS in your country.

InAppMessage -> (structure)

The in-app message configuration.

Body -> (string)

The message body of the notification, the email body or the text message.

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

Custom config to be sent to client.

key -> (string)

value -> (string)

Layout -> (string)

In-app message layout.

Name -> (string)

A custom name for the campaign.

Schedule -> (structure)

The schedule settings for the campaign.

EndTime -> (string)

The scheduled time, in ISO 8601 format, when the campaign ended or will end.

EventFilter -> (structure)

The type of event that causes the campaign to be sent, if the value of the Frequency property is EVENT.

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

Frequency -> (string)

Specifies how often the campaign is sent or whether the campaign is sent in response to a specific event.

IsLocalTime -> (boolean)

Specifies whether the start and end times for the campaign schedule use each recipientâs local time. To base the schedule on each recipientâs local time, set this value to true.

QuietTime -> (structure)

The default quiet time for the campaign. Quiet time is a specific time range when a campaign doesnât send messages to endpoints, if all the following conditions are met:

- The EndpointDemographic.Timezone property of the endpoint is set to a valid value.
- The current time in the endpointâs time zone is later than or equal to the time specified by the QuietTime.Start property for the campaign.
- The current time in the endpointâs time zone is earlier than or equal to the time specified by the QuietTime.End property for the campaign.

If any of the preceding conditions isnât met, the endpoint will receive messages from the campaign, even if quiet time is enabled.

End -> (string)

The specific time when quiet time ends. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.

Start -> (string)

The specific time when quiet time begins. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.

StartTime -> (string)

The scheduled time when the campaign began or will begin. Valid values are: IMMEDIATE, to start the campaign immediately; or, a specific time in ISO 8601 format.

Timezone -> (string)

The starting UTC offset for the campaign schedule, if the value of the IsLocalTime property is true. Valid values are: UTC, UTC+01, UTC+02, UTC+03, UTC+03:30, UTC+04, UTC+04:30, UTC+05, UTC+05:30, UTC+05:45, UTC+06, UTC+06:30, UTC+07, UTC+08, UTC+09, UTC+09:30, UTC+10, UTC+10:30, UTC+11, UTC+12, UTC+13, UTC-02, UTC-03, UTC-04, UTC-05, UTC-06, UTC-07, UTC-08, UTC-09, UTC-10, and UTC-11.

SegmentId -> (string)

The unique identifier for the segment to associate with the campaign.

SegmentVersion -> (integer)

The version of the segment to associate with the campaign.

tags -> (map)

### Note

As of **22-05-2023** tags has been deprecated for update operations. After this date any value in tags is not processed and an error code is not returned. To manage tags we recommend using either [Tags](https://docs.aws.amazon.com/pinpoint/latest/apireference/tags-resource-arn.html) in the *API Reference for Amazon Pinpoint* , [resourcegroupstaggingapi](https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/index.html) commands in the *AWS Command Line Interface Documentation* or [resourcegroupstaggingapi](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/resourcegroupstaggingapi/package-summary.html) in the *AWS SDK* .

(Deprecated) A string-to-string map of key-value pairs that defines the tags to associate with the campaign. Each tag consists of a required tag key and an associated tag value.

key -> (string)

value -> (string)

TemplateConfiguration -> (structure)

The message template to use for the campaign.

EmailTemplate -> (structure)

The email template to use for the message.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

PushTemplate -> (structure)

The push notification template to use for the message.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

SMSTemplate -> (structure)

The SMS template to use for the message.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

VoiceTemplate -> (structure)

The voice template to use for the message. This object isnât supported for campaigns.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

InAppTemplate -> (structure)

The InApp template to use for the message. The InApp template object is not supported for SendMessages.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

TreatmentDescription -> (string)

A custom description of the default treatment for the campaign.

TreatmentName -> (string)

A custom name of the default treatment for the campaign, if the campaign has multiple treatments. A *treatment* is a variation of a campaign thatâs used for A/B testing.

Priority -> (integer)

Defines the priority of the campaign, used to decide the order of messages displayed to user if there are multiple messages scheduled to be displayed at the same moment.

JSON Syntax:

```
{
  "AdditionalTreatments": [
    {
      "CustomDeliveryConfiguration": {
        "DeliveryUri": "string",
        "EndpointTypes": ["PUSH"|"GCM"|"APNS"|"APNS_SANDBOX"|"APNS_VOIP"|"APNS_VOIP_SANDBOX"|"ADM"|"SMS"|"VOICE"|"EMAIL"|"BAIDU"|"CUSTOM"|"IN_APP", ...]
      },
      "MessageConfiguration": {
        "ADMMessage": {
          "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
          "Body": "string",
          "ImageIconUrl": "string",
          "ImageSmallIconUrl": "string",
          "ImageUrl": "string",
          "JsonBody": "string",
          "MediaUrl": "string",
          "RawContent": "string",
          "SilentPush": true|false,
          "TimeToLive": integer,
          "Title": "string",
          "Url": "string"
        },
        "APNSMessage": {
          "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
          "Body": "string",
          "ImageIconUrl": "string",
          "ImageSmallIconUrl": "string",
          "ImageUrl": "string",
          "JsonBody": "string",
          "MediaUrl": "string",
          "RawContent": "string",
          "SilentPush": true|false,
          "TimeToLive": integer,
          "Title": "string",
          "Url": "string"
        },
        "BaiduMessage": {
          "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
          "Body": "string",
          "ImageIconUrl": "string",
          "ImageSmallIconUrl": "string",
          "ImageUrl": "string",
          "JsonBody": "string",
          "MediaUrl": "string",
          "RawContent": "string",
          "SilentPush": true|false,
          "TimeToLive": integer,
          "Title": "string",
          "Url": "string"
        },
        "CustomMessage": {
          "Data": "string"
        },
        "DefaultMessage": {
          "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
          "Body": "string",
          "ImageIconUrl": "string",
          "ImageSmallIconUrl": "string",
          "ImageUrl": "string",
          "JsonBody": "string",
          "MediaUrl": "string",
          "RawContent": "string",
          "SilentPush": true|false,
          "TimeToLive": integer,
          "Title": "string",
          "Url": "string"
        },
        "EmailMessage": {
          "Body": "string",
          "FromAddress": "string",
          "Headers": [
            {
              "Name": "string",
              "Value": "string"
            }
            ...
          ],
          "HtmlBody": "string",
          "Title": "string"
        },
        "GCMMessage": {
          "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
          "Body": "string",
          "ImageIconUrl": "string",
          "ImageSmallIconUrl": "string",
          "ImageUrl": "string",
          "JsonBody": "string",
          "MediaUrl": "string",
          "RawContent": "string",
          "SilentPush": true|false,
          "TimeToLive": integer,
          "Title": "string",
          "Url": "string"
        },
        "SMSMessage": {
          "Body": "string",
          "MessageType": "TRANSACTIONAL"|"PROMOTIONAL",
          "OriginationNumber": "string",
          "SenderId": "string",
          "EntityId": "string",
          "TemplateId": "string"
        },
        "InAppMessage": {
          "Body": "string",
          "Content": [
            {
              "BackgroundColor": "string",
              "BodyConfig": {
                "Alignment": "LEFT"|"CENTER"|"RIGHT",
                "Body": "string",
                "TextColor": "string"
              },
              "HeaderConfig": {
                "Alignment": "LEFT"|"CENTER"|"RIGHT",
                "Header": "string",
                "TextColor": "string"
              },
              "ImageUrl": "string",
              "PrimaryBtn": {
                "Android": {
                  "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
                  "Link": "string"
                },
                "DefaultConfig": {
                  "BackgroundColor": "string",
                  "BorderRadius": integer,
                  "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
                  "Link": "string",
                  "Text": "string",
                  "TextColor": "string"
                },
                "IOS": {
                  "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
                  "Link": "string"
                },
                "Web": {
                  "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
                  "Link": "string"
                }
              },
              "SecondaryBtn": {
                "Android": {
                  "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
                  "Link": "string"
                },
                "DefaultConfig": {
                  "BackgroundColor": "string",
                  "BorderRadius": integer,
                  "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
                  "Link": "string",
                  "Text": "string",
                  "TextColor": "string"
                },
                "IOS": {
                  "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
                  "Link": "string"
                },
                "Web": {
                  "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
                  "Link": "string"
                }
              }
            }
            ...
          ],
          "CustomConfig": {"string": "string"
            ...},
          "Layout": "BOTTOM_BANNER"|"TOP_BANNER"|"OVERLAYS"|"MOBILE_FEED"|"MIDDLE_BANNER"|"CAROUSEL"
        }
      },
      "Schedule": {
        "EndTime": "string",
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
        "Frequency": "ONCE"|"HOURLY"|"DAILY"|"WEEKLY"|"MONTHLY"|"EVENT"|"IN_APP_EVENT",
        "IsLocalTime": true|false,
        "QuietTime": {
          "End": "string",
          "Start": "string"
        },
        "StartTime": "string",
        "Timezone": "string"
      },
      "SizePercent": integer,
      "TemplateConfiguration": {
        "EmailTemplate": {
          "Name": "string",
          "Version": "string"
        },
        "PushTemplate": {
          "Name": "string",
          "Version": "string"
        },
        "SMSTemplate": {
          "Name": "string",
          "Version": "string"
        },
        "VoiceTemplate": {
          "Name": "string",
          "Version": "string"
        },
        "InAppTemplate": {
          "Name": "string",
          "Version": "string"
        }
      },
      "TreatmentDescription": "string",
      "TreatmentName": "string"
    }
    ...
  ],
  "CustomDeliveryConfiguration": {
    "DeliveryUri": "string",
    "EndpointTypes": ["PUSH"|"GCM"|"APNS"|"APNS_SANDBOX"|"APNS_VOIP"|"APNS_VOIP_SANDBOX"|"ADM"|"SMS"|"VOICE"|"EMAIL"|"BAIDU"|"CUSTOM"|"IN_APP", ...]
  },
  "Description": "string",
  "HoldoutPercent": integer,
  "Hook": {
    "LambdaFunctionName": "string",
    "Mode": "DELIVERY"|"FILTER",
    "WebUrl": "string"
  },
  "IsPaused": true|false,
  "Limits": {
    "Daily": integer,
    "MaximumDuration": integer,
    "MessagesPerSecond": integer,
    "Total": integer,
    "Session": integer
  },
  "MessageConfiguration": {
    "ADMMessage": {
      "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
      "Body": "string",
      "ImageIconUrl": "string",
      "ImageSmallIconUrl": "string",
      "ImageUrl": "string",
      "JsonBody": "string",
      "MediaUrl": "string",
      "RawContent": "string",
      "SilentPush": true|false,
      "TimeToLive": integer,
      "Title": "string",
      "Url": "string"
    },
    "APNSMessage": {
      "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
      "Body": "string",
      "ImageIconUrl": "string",
      "ImageSmallIconUrl": "string",
      "ImageUrl": "string",
      "JsonBody": "string",
      "MediaUrl": "string",
      "RawContent": "string",
      "SilentPush": true|false,
      "TimeToLive": integer,
      "Title": "string",
      "Url": "string"
    },
    "BaiduMessage": {
      "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
      "Body": "string",
      "ImageIconUrl": "string",
      "ImageSmallIconUrl": "string",
      "ImageUrl": "string",
      "JsonBody": "string",
      "MediaUrl": "string",
      "RawContent": "string",
      "SilentPush": true|false,
      "TimeToLive": integer,
      "Title": "string",
      "Url": "string"
    },
    "CustomMessage": {
      "Data": "string"
    },
    "DefaultMessage": {
      "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
      "Body": "string",
      "ImageIconUrl": "string",
      "ImageSmallIconUrl": "string",
      "ImageUrl": "string",
      "JsonBody": "string",
      "MediaUrl": "string",
      "RawContent": "string",
      "SilentPush": true|false,
      "TimeToLive": integer,
      "Title": "string",
      "Url": "string"
    },
    "EmailMessage": {
      "Body": "string",
      "FromAddress": "string",
      "Headers": [
        {
          "Name": "string",
          "Value": "string"
        }
        ...
      ],
      "HtmlBody": "string",
      "Title": "string"
    },
    "GCMMessage": {
      "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
      "Body": "string",
      "ImageIconUrl": "string",
      "ImageSmallIconUrl": "string",
      "ImageUrl": "string",
      "JsonBody": "string",
      "MediaUrl": "string",
      "RawContent": "string",
      "SilentPush": true|false,
      "TimeToLive": integer,
      "Title": "string",
      "Url": "string"
    },
    "SMSMessage": {
      "Body": "string",
      "MessageType": "TRANSACTIONAL"|"PROMOTIONAL",
      "OriginationNumber": "string",
      "SenderId": "string",
      "EntityId": "string",
      "TemplateId": "string"
    },
    "InAppMessage": {
      "Body": "string",
      "Content": [
        {
          "BackgroundColor": "string",
          "BodyConfig": {
            "Alignment": "LEFT"|"CENTER"|"RIGHT",
            "Body": "string",
            "TextColor": "string"
          },
          "HeaderConfig": {
            "Alignment": "LEFT"|"CENTER"|"RIGHT",
            "Header": "string",
            "TextColor": "string"
          },
          "ImageUrl": "string",
          "PrimaryBtn": {
            "Android": {
              "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
              "Link": "string"
            },
            "DefaultConfig": {
              "BackgroundColor": "string",
              "BorderRadius": integer,
              "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
              "Link": "string",
              "Text": "string",
              "TextColor": "string"
            },
            "IOS": {
              "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
              "Link": "string"
            },
            "Web": {
              "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
              "Link": "string"
            }
          },
          "SecondaryBtn": {
            "Android": {
              "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
              "Link": "string"
            },
            "DefaultConfig": {
              "BackgroundColor": "string",
              "BorderRadius": integer,
              "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
              "Link": "string",
              "Text": "string",
              "TextColor": "string"
            },
            "IOS": {
              "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
              "Link": "string"
            },
            "Web": {
              "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
              "Link": "string"
            }
          }
        }
        ...
      ],
      "CustomConfig": {"string": "string"
        ...},
      "Layout": "BOTTOM_BANNER"|"TOP_BANNER"|"OVERLAYS"|"MOBILE_FEED"|"MIDDLE_BANNER"|"CAROUSEL"
    }
  },
  "Name": "string",
  "Schedule": {
    "EndTime": "string",
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
    "Frequency": "ONCE"|"HOURLY"|"DAILY"|"WEEKLY"|"MONTHLY"|"EVENT"|"IN_APP_EVENT",
    "IsLocalTime": true|false,
    "QuietTime": {
      "End": "string",
      "Start": "string"
    },
    "StartTime": "string",
    "Timezone": "string"
  },
  "SegmentId": "string",
  "SegmentVersion": integer,
  "tags": {"string": "string"
    ...},
  "TemplateConfiguration": {
    "EmailTemplate": {
      "Name": "string",
      "Version": "string"
    },
    "PushTemplate": {
      "Name": "string",
      "Version": "string"
    },
    "SMSTemplate": {
      "Name": "string",
      "Version": "string"
    },
    "VoiceTemplate": {
      "Name": "string",
      "Version": "string"
    },
    "InAppTemplate": {
      "Name": "string",
      "Version": "string"
    }
  },
  "TreatmentDescription": "string",
  "TreatmentName": "string",
  "Priority": integer
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

CampaignResponse -> (structure)

Provides information about the status, configuration, and other settings for a campaign.

AdditionalTreatments -> (list)

An array of responses, one for each treatment that you defined for the campaign, in addition to the default treatment.

(structure)

Specifies the settings for a campaign treatment. A *treatment* is a variation of a campaign thatâs used for A/B testing of a campaign.

CustomDeliveryConfiguration -> (structure)

The delivery configuration settings for sending the treatment through a custom channel. This object is required if the MessageConfiguration object for the treatment specifies a CustomMessage object.

DeliveryUri -> (string)

The destination to send the campaign or treatment to. This value can be one of the following:

- The name or Amazon Resource Name (ARN) of an AWS Lambda function to invoke to handle delivery of the campaign or treatment.
- The URL for a web application or service that supports HTTPS and can receive the message. The URL has to be a full URL, including the HTTPS protocol.

EndpointTypes -> (list)

The types of endpoints to send the campaign or treatment to. Each valid value maps to a type of channel that you can associate with an endpoint by using the ChannelType property of an endpoint.

(string)

Id -> (string)

The unique identifier for the treatment.

MessageConfiguration -> (structure)

The message configuration settings for the treatment.

ADMMessage -> (structure)

The message that the campaign sends through the ADM (Amazon Device Messaging) channel. If specified, this message overrides the default message.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

APNSMessage -> (structure)

The message that the campaign sends through the APNs (Apple Push Notification service) channel. If specified, this message overrides the default message.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

BaiduMessage -> (structure)

The message that the campaign sends through the Baidu (Baidu Cloud Push) channel. If specified, this message overrides the default message.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

CustomMessage -> (structure)

The message that the campaign sends through a custom channel, as specified by the delivery configuration (CustomDeliveryConfiguration) settings for the campaign. If specified, this message overrides the default message.

Data -> (string)

The raw, JSON-formatted string to use as the payload for the message. The maximum size is 5 KB.

DefaultMessage -> (structure)

The default message that the campaign sends through all the channels that are configured for the campaign.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

EmailMessage -> (structure)

The message that the campaign sends through the email channel. If specified, this message overrides the default message.

Body -> (string)

The body of the email for recipients whose email clients donât render HTML content.

FromAddress -> (string)

The verified email address to send the email from. The default address is the FromAddress specified for the email channel for the application.

Headers -> (list)

The list of [MessageHeaders](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id.html#apps-application-id-campaigns-campaign-id-model-messageheader) for the email. You can have up to 15 MessageHeaders for each email.

(structure)

Contains the name and value pair of an email header to add to your email. You can have up to 15 MessageHeaders. A header can contain information such as the sender, receiver, route, or timestamp.

Name -> (string)

The name of the message header. The header name can contain up to 126 characters.

Value -> (string)

The value of the message header. The header value can contain up to 870 characters, including the length of any rendered attributes. For example if you add the {CreationDate} attribute, it renders as YYYY-MM-DDTHH:MM:SS.SSSZ and is 24 characters in length.

HtmlBody -> (string)

The body of the email, in HTML format, for recipients whose email clients render HTML content.

Title -> (string)

The subject line, or title, of the email.

GCMMessage -> (structure)

The message that the campaign sends through the GCM channel, which enables Amazon Pinpoint to send push notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service. If specified, this message overrides the default message.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

SMSMessage -> (structure)

The message that the campaign sends through the SMS channel. If specified, this message overrides the default message.

Body -> (string)

The body of the SMS message.

MessageType -> (string)

The SMS message type. Valid values are TRANSACTIONAL (for messages that are critical or time-sensitive, such as a one-time passwords) and PROMOTIONAL (for messsages that arenât critical or time-sensitive, such as marketing messages).

OriginationNumber -> (string)

The long code to send the SMS message from. This value should be one of the dedicated long codes thatâs assigned to your AWS account. Although it isnât required, we recommend that you specify the long code using an E.164 format to ensure prompt and accurate delivery of the message. For example, +12065550100.

SenderId -> (string)

The sender ID to display on recipientsâ devices when they receive the SMS message.

EntityId -> (string)

The entity ID or Principal Entity (PE) id received from the regulatory body for sending SMS in your country.

TemplateId -> (string)

The template ID received from the regulatory body for sending SMS in your country.

InAppMessage -> (structure)

The in-app message configuration.

Body -> (string)

The message body of the notification, the email body or the text message.

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

Custom config to be sent to client.

key -> (string)

value -> (string)

Layout -> (string)

In-app message layout.

Schedule -> (structure)

The schedule settings for the treatment.

EndTime -> (string)

The scheduled time, in ISO 8601 format, when the campaign ended or will end.

EventFilter -> (structure)

The type of event that causes the campaign to be sent, if the value of the Frequency property is EVENT.

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

Frequency -> (string)

Specifies how often the campaign is sent or whether the campaign is sent in response to a specific event.

IsLocalTime -> (boolean)

Specifies whether the start and end times for the campaign schedule use each recipientâs local time. To base the schedule on each recipientâs local time, set this value to true.

QuietTime -> (structure)

The default quiet time for the campaign. Quiet time is a specific time range when a campaign doesnât send messages to endpoints, if all the following conditions are met:

- The EndpointDemographic.Timezone property of the endpoint is set to a valid value.
- The current time in the endpointâs time zone is later than or equal to the time specified by the QuietTime.Start property for the campaign.
- The current time in the endpointâs time zone is earlier than or equal to the time specified by the QuietTime.End property for the campaign.

If any of the preceding conditions isnât met, the endpoint will receive messages from the campaign, even if quiet time is enabled.

End -> (string)

The specific time when quiet time ends. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.

Start -> (string)

The specific time when quiet time begins. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.

StartTime -> (string)

The scheduled time when the campaign began or will begin. Valid values are: IMMEDIATE, to start the campaign immediately; or, a specific time in ISO 8601 format.

Timezone -> (string)

The starting UTC offset for the campaign schedule, if the value of the IsLocalTime property is true. Valid values are: UTC, UTC+01, UTC+02, UTC+03, UTC+03:30, UTC+04, UTC+04:30, UTC+05, UTC+05:30, UTC+05:45, UTC+06, UTC+06:30, UTC+07, UTC+08, UTC+09, UTC+09:30, UTC+10, UTC+10:30, UTC+11, UTC+12, UTC+13, UTC-02, UTC-03, UTC-04, UTC-05, UTC-06, UTC-07, UTC-08, UTC-09, UTC-10, and UTC-11.

SizePercent -> (integer)

The allocated percentage of users (segment members) that the treatment is sent to.

State -> (structure)

The current status of the treatment.

CampaignStatus -> (string)

The current status of the campaign, or the current status of a treatment that belongs to an A/B test campaign.

If a campaign uses A/B testing, the campaign has a status of COMPLETED only if all campaign treatments have a status of COMPLETED. If you delete the segment thatâs associated with a campaign, the campaign fails and has a status of DELETED.

TemplateConfiguration -> (structure)

The message template to use for the treatment.

EmailTemplate -> (structure)

The email template to use for the message.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

PushTemplate -> (structure)

The push notification template to use for the message.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

SMSTemplate -> (structure)

The SMS template to use for the message.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

VoiceTemplate -> (structure)

The voice template to use for the message. This object isnât supported for campaigns.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

InAppTemplate -> (structure)

The InApp template to use for the message. The InApp template object is not supported for SendMessages.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

TreatmentDescription -> (string)

The custom description of the treatment.

TreatmentName -> (string)

The custom name of the treatment.

ApplicationId -> (string)

The unique identifier for the application that the campaign applies to.

Arn -> (string)

The Amazon Resource Name (ARN) of the campaign.

CreationDate -> (string)

The date, in ISO 8601 format, when the campaign was created.

CustomDeliveryConfiguration -> (structure)

The delivery configuration settings for sending the campaign through a custom channel.

DeliveryUri -> (string)

The destination to send the campaign or treatment to. This value can be one of the following:

- The name or Amazon Resource Name (ARN) of an AWS Lambda function to invoke to handle delivery of the campaign or treatment.
- The URL for a web application or service that supports HTTPS and can receive the message. The URL has to be a full URL, including the HTTPS protocol.

EndpointTypes -> (list)

The types of endpoints to send the campaign or treatment to. Each valid value maps to a type of channel that you can associate with an endpoint by using the ChannelType property of an endpoint.

(string)

DefaultState -> (structure)

The current status of the campaignâs default treatment. This value exists only for campaigns that have more than one treatment.

CampaignStatus -> (string)

The current status of the campaign, or the current status of a treatment that belongs to an A/B test campaign.

If a campaign uses A/B testing, the campaign has a status of COMPLETED only if all campaign treatments have a status of COMPLETED. If you delete the segment thatâs associated with a campaign, the campaign fails and has a status of DELETED.

Description -> (string)

The custom description of the campaign.

HoldoutPercent -> (integer)

The allocated percentage of users (segment members) who shouldnât receive messages from the campaign.

Hook -> (structure)

The settings for the AWS Lambda function to use as a code hook for the campaign. You can use this hook to customize the segment thatâs used by the campaign.

LambdaFunctionName -> (string)

The name or Amazon Resource Name (ARN) of the AWS Lambda function that Amazon Pinpoint invokes to customize a segment for a campaign.

Mode -> (string)

The mode that Amazon Pinpoint uses to invoke the AWS Lambda function. Possible values are:

- FILTER - Invoke the function to customize the segment thatâs used by a campaign.
- DELIVERY - (Deprecated) Previously, invoked the function to send a campaign through a custom channel. This functionality is not supported anymore. To send a campaign through a custom channel, use the CustomDeliveryConfiguration and CampaignCustomMessage objects of the campaign.

WebUrl -> (string)

The web URL that Amazon Pinpoint calls to invoke the AWS Lambda function over HTTPS.

Id -> (string)

The unique identifier for the campaign.

IsPaused -> (boolean)

Specifies whether the campaign is paused. A paused campaign doesnât run unless you resume it by changing this value to false.

LastModifiedDate -> (string)

The date, in ISO 8601 format, when the campaign was last modified.

Limits -> (structure)

The messaging limits for the campaign.

Daily -> (integer)

The maximum number of messages that a campaign can send to a single endpoint during a 24-hour period. For an application, this value specifies the default limit for the number of messages that campaigns and journeys can send to a single endpoint during a 24-hour period. The maximum value is 100.

MaximumDuration -> (integer)

The maximum amount of time, in seconds, that a campaign can attempt to deliver a message after the scheduled start time for the campaign. The minimum value is 60 seconds.

MessagesPerSecond -> (integer)

The maximum number of messages that a campaign can send each second. For an application, this value specifies the default limit for the number of messages that campaigns can send each second. The minimum value is 1. The maximum value is 20,000.

Total -> (integer)

The maximum number of messages that a campaign can send to a single endpoint during the course of the campaign. If a campaign recurs, this setting applies to all runs of the campaign. The maximum value is 100.

Session -> (integer)

The maximum total number of messages that the campaign can send per user session.

MessageConfiguration -> (structure)

The message configuration settings for the campaign.

ADMMessage -> (structure)

The message that the campaign sends through the ADM (Amazon Device Messaging) channel. If specified, this message overrides the default message.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

APNSMessage -> (structure)

The message that the campaign sends through the APNs (Apple Push Notification service) channel. If specified, this message overrides the default message.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

BaiduMessage -> (structure)

The message that the campaign sends through the Baidu (Baidu Cloud Push) channel. If specified, this message overrides the default message.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

CustomMessage -> (structure)

The message that the campaign sends through a custom channel, as specified by the delivery configuration (CustomDeliveryConfiguration) settings for the campaign. If specified, this message overrides the default message.

Data -> (string)

The raw, JSON-formatted string to use as the payload for the message. The maximum size is 5 KB.

DefaultMessage -> (structure)

The default message that the campaign sends through all the channels that are configured for the campaign.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

EmailMessage -> (structure)

The message that the campaign sends through the email channel. If specified, this message overrides the default message.

Body -> (string)

The body of the email for recipients whose email clients donât render HTML content.

FromAddress -> (string)

The verified email address to send the email from. The default address is the FromAddress specified for the email channel for the application.

Headers -> (list)

The list of [MessageHeaders](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id.html#apps-application-id-campaigns-campaign-id-model-messageheader) for the email. You can have up to 15 MessageHeaders for each email.

(structure)

Contains the name and value pair of an email header to add to your email. You can have up to 15 MessageHeaders. A header can contain information such as the sender, receiver, route, or timestamp.

Name -> (string)

The name of the message header. The header name can contain up to 126 characters.

Value -> (string)

The value of the message header. The header value can contain up to 870 characters, including the length of any rendered attributes. For example if you add the {CreationDate} attribute, it renders as YYYY-MM-DDTHH:MM:SS.SSSZ and is 24 characters in length.

HtmlBody -> (string)

The body of the email, in HTML format, for recipients whose email clients render HTML content.

Title -> (string)

The subject line, or title, of the email.

GCMMessage -> (structure)

The message that the campaign sends through the GCM channel, which enables Amazon Pinpoint to send push notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service. If specified, this message overrides the default message.

Action -> (string)

The action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of iOS and Android.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message. The maximum number of characters is 200.

ImageIconUrl -> (string)

The URL of the image to display as the push-notification icon, such as the icon for the app.

ImageSmallIconUrl -> (string)

The URL of the image to display as the small, push-notification icon, such as a small version of the icon for the app.

ImageUrl -> (string)

The URL of an image to display in the push notification.

JsonBody -> (string)

The JSON payload to use for a silent push notification.

MediaUrl -> (string)

The URL of the image or video to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration, displaying messages in an in-app message center, or supporting phone home functionality.

TimeToLive -> (integer)

The number of seconds that the push-notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when itâs sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

This value doesnât apply to messages that are sent through the Amazon Device Messaging (ADM) service.

Title -> (string)

The title to display above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

SMSMessage -> (structure)

The message that the campaign sends through the SMS channel. If specified, this message overrides the default message.

Body -> (string)

The body of the SMS message.

MessageType -> (string)

The SMS message type. Valid values are TRANSACTIONAL (for messages that are critical or time-sensitive, such as a one-time passwords) and PROMOTIONAL (for messsages that arenât critical or time-sensitive, such as marketing messages).

OriginationNumber -> (string)

The long code to send the SMS message from. This value should be one of the dedicated long codes thatâs assigned to your AWS account. Although it isnât required, we recommend that you specify the long code using an E.164 format to ensure prompt and accurate delivery of the message. For example, +12065550100.

SenderId -> (string)

The sender ID to display on recipientsâ devices when they receive the SMS message.

EntityId -> (string)

The entity ID or Principal Entity (PE) id received from the regulatory body for sending SMS in your country.

TemplateId -> (string)

The template ID received from the regulatory body for sending SMS in your country.

InAppMessage -> (structure)

The in-app message configuration.

Body -> (string)

The message body of the notification, the email body or the text message.

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

Custom config to be sent to client.

key -> (string)

value -> (string)

Layout -> (string)

In-app message layout.

Name -> (string)

The name of the campaign.

Schedule -> (structure)

The schedule settings for the campaign.

EndTime -> (string)

The scheduled time, in ISO 8601 format, when the campaign ended or will end.

EventFilter -> (structure)

The type of event that causes the campaign to be sent, if the value of the Frequency property is EVENT.

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

Frequency -> (string)

Specifies how often the campaign is sent or whether the campaign is sent in response to a specific event.

IsLocalTime -> (boolean)

Specifies whether the start and end times for the campaign schedule use each recipientâs local time. To base the schedule on each recipientâs local time, set this value to true.

QuietTime -> (structure)

The default quiet time for the campaign. Quiet time is a specific time range when a campaign doesnât send messages to endpoints, if all the following conditions are met:

- The EndpointDemographic.Timezone property of the endpoint is set to a valid value.
- The current time in the endpointâs time zone is later than or equal to the time specified by the QuietTime.Start property for the campaign.
- The current time in the endpointâs time zone is earlier than or equal to the time specified by the QuietTime.End property for the campaign.

If any of the preceding conditions isnât met, the endpoint will receive messages from the campaign, even if quiet time is enabled.

End -> (string)

The specific time when quiet time ends. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.

Start -> (string)

The specific time when quiet time begins. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.

StartTime -> (string)

The scheduled time when the campaign began or will begin. Valid values are: IMMEDIATE, to start the campaign immediately; or, a specific time in ISO 8601 format.

Timezone -> (string)

The starting UTC offset for the campaign schedule, if the value of the IsLocalTime property is true. Valid values are: UTC, UTC+01, UTC+02, UTC+03, UTC+03:30, UTC+04, UTC+04:30, UTC+05, UTC+05:30, UTC+05:45, UTC+06, UTC+06:30, UTC+07, UTC+08, UTC+09, UTC+09:30, UTC+10, UTC+10:30, UTC+11, UTC+12, UTC+13, UTC-02, UTC-03, UTC-04, UTC-05, UTC-06, UTC-07, UTC-08, UTC-09, UTC-10, and UTC-11.

SegmentId -> (string)

The unique identifier for the segment thatâs associated with the campaign.

SegmentVersion -> (integer)

The version number of the segment thatâs associated with the campaign.

State -> (structure)

The current status of the campaign.

CampaignStatus -> (string)

The current status of the campaign, or the current status of a treatment that belongs to an A/B test campaign.

If a campaign uses A/B testing, the campaign has a status of COMPLETED only if all campaign treatments have a status of COMPLETED. If you delete the segment thatâs associated with a campaign, the campaign fails and has a status of DELETED.

tags -> (map)

A string-to-string map of key-value pairs that identifies the tags that are associated with the campaign. Each tag consists of a required tag key and an associated tag value.

key -> (string)

value -> (string)

TemplateConfiguration -> (structure)

The message template thatâs used for the campaign.

EmailTemplate -> (structure)

The email template to use for the message.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

PushTemplate -> (structure)

The push notification template to use for the message.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

SMSTemplate -> (structure)

The SMS template to use for the message.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

VoiceTemplate -> (structure)

The voice template to use for the message. This object isnât supported for campaigns.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

InAppTemplate -> (structure)

The InApp template to use for the message. The InApp template object is not supported for SendMessages.

Name -> (string)

The name of the message template to use for the message. If specified, this value must match the name of an existing message template.

Version -> (string)

The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the Template Versionsresource.

If you donât specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template thatâs been most recently reviewed and approved for use, depending on your workflow. It isnât necessarily the latest version of a template.

TreatmentDescription -> (string)

The custom description of the default treatment for the campaign.

TreatmentName -> (string)

The custom name of the default treatment for the campaign, if the campaign has multiple treatments. A *treatment* is a variation of a campaign thatâs used for A/B testing.

Version -> (integer)

The version number of the campaign.

Priority -> (integer)

Defines the priority of the campaign, used to decide the order of messages displayed to user if there are multiple messages scheduled to be displayed at the same moment.