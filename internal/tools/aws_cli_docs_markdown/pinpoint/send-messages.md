# send-messagesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/send-messages.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/send-messages.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/index.html#cli-aws-pinpoint) ]

# send-messages

## Description

Creates and sends a direct message.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/SendMessages)

## Synopsis

```
send-messages
--application-id <value>
--message-request <value>
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

`--message-request` (structure)

Specifies the configuration and other settings for a message.

Addresses -> (map)

A map of key-value pairs, where each key is an address and each value is an [AddressConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-addressconfiguration) object. An address can be a push notification token, a phone number, or an email address. You can use an [AddressConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-addressconfiguration) object to tailor the message for an address by specifying settings such as content overrides and message variables.

key -> (string)

value -> (structure)

Specifies address-based configuration settings for a message thatâs sent directly to an endpoint.

BodyOverride -> (string)

The message body to use instead of the default message body. This value overrides the default message body.

ChannelType -> (string)

The channel to use when sending the message.

Context -> (map)

An object that maps custom attributes to attributes for the address and is attached to the message. Attribute names are case sensitive.

For a push notification, this payload is added to the data.pinpoint object. For an email or text message, this payload is added to email/SMS delivery receipt event attributes.

key -> (string)

value -> (string)

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the message. If specified, this value overrides all other values for the message.

Substitutions -> (map)

A map of the message variables to merge with the variables specified by properties of the DefaultMessage object. The variables specified in this map take precedence over all other variables.

key -> (string)

value -> (list)

(string)

TitleOverride -> (string)

The message title to use instead of the default message title. This value overrides the default message title.

Context -> (map)

A map of custom attributes to attach to the message. For a push notification, this payload is added to the data.pinpoint object. For an email or text message, this payload is added to email/SMS delivery receipt event attributes.

key -> (string)

value -> (string)

Endpoints -> (map)

A map of key-value pairs, where each key is an endpoint ID and each value is an [EndpointSendConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-endpointsendconfiguration) object. You can use an [EndpointSendConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-endpointsendconfiguration) object to tailor the message for an endpoint by specifying settings such as content overrides and message variables.

key -> (string)

value -> (structure)

Specifies the content, including message variables and attributes, to use in a message thatâs sent directly to an endpoint.

BodyOverride -> (string)

The body of the message. If specified, this value overrides the default message body.

Context -> (map)

A map of custom attributes to attach to the message for the address. Attribute names are case sensitive.

For a push notification, this payload is added to the data.pinpoint object. For an email or text message, this payload is added to email/SMS delivery receipt event attributes.

key -> (string)

value -> (string)

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the message. If specified, this value overrides all other values for the message.

Substitutions -> (map)

A map of the message variables to merge with the variables specified for the default message (DefaultMessage.Substitutions). The variables specified in this map take precedence over all other variables.

key -> (string)

value -> (list)

(string)

TitleOverride -> (string)

The title or subject line of the message. If specified, this value overrides the default message title or subject line.

MessageConfiguration -> (structure)

The settings and content for the default message and any default messages that you defined for specific channels.

ADMMessage -> (structure)

The default push notification message for the ADM (Amazon Device Messaging) channel. This message overrides the default push notification message (DefaultPushNotificationMessage).

Action -> (string)

The action to occur if the recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This action uses the deep-linking features of the Android platform.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message.

ConsolidationKey -> (string)

An arbitrary string that indicates that multiple messages are logically the same and that Amazon Device Messaging (ADM) can drop previously enqueued messages in favor of this message.

Data -> (map)

The JSON data payload to use for the push notification, if the notification is a silent push notification. This payload is added to the data.pinpoint.jsonBody object of the notification.

key -> (string)

value -> (string)

ExpiresAfter -> (string)

The amount of time, in seconds, that ADM should store the message if the recipientâs device is offline. Amazon Pinpoint specifies this value in the expiresAfter parameter when it sends the notification message to ADM.

IconReference -> (string)

The icon image name of the asset saved in your app.

ImageIconUrl -> (string)

The URL of the large icon image to display in the content view of the push notification.

ImageUrl -> (string)

The URL of an image to display in the push notification.

MD5 -> (string)

The base64-encoded, MD5 checksum of the value specified by the Data property. ADM uses the MD5 value to verify the integrity of the data.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration or supporting phone home functionality.

SmallImageIconUrl -> (string)

The URL of the small icon image to display in the status bar and the content view of the push notification.

Sound -> (string)

The sound to play when the recipient receives the push notification. You can use the default stream or specify the file name of a sound resource thatâs bundled in your app. On an Android platform, the sound file must reside in /res/raw/.

Substitutions -> (map)

The default message variables to use in the notification message. You can override the default variables with individual address variables.

key -> (string)

value -> (list)

(string)

Title -> (string)

The title to display above the notification message on the recipientâs device.

Url -> (string)

The URL to open in the recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

APNSMessage -> (structure)

The default push notification message for the APNs (Apple Push Notification service) channel. This message overrides the default push notification message (DefaultPushNotificationMessage).

APNSPushType -> (string)

The type of push notification to send. Valid values are:

- alert - For a standard notification thatâs displayed on recipientsâ devices and prompts a recipient to interact with the notification.
- background - For a silent notification that delivers content in the background and isnât displayed on recipientsâ devices.
- complication - For a notification that contains update information for an appâs complication timeline.
- fileprovider - For a notification that signals changes to a File Provider extension.
- mdm - For a notification that tells managed devices to contact the MDM server.
- voip - For a notification that provides information about an incoming VoIP call.

Amazon Pinpoint specifies this value in the apns-push-type request header when it sends the notification message to APNs. If you donât specify a value for this property, Amazon Pinpoint sets the value to alert or background automatically, based on the value that you specify for the SilentPush or RawContent property of the message.

For more information about the apns-push-type request header, see [Sending Notification Requests to APNs](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns) on the Apple Developer website.

Action -> (string)

The action to occur if the recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of the iOS platform.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Badge -> (integer)

The key that indicates whether and how to modify the badge of your appâs icon when the recipient receives the push notification. If this key isnât included in the dictionary, the badge doesnât change. To remove the badge, set this value to 0.

Body -> (string)

The body of the notification message.

Category -> (string)

The key that indicates the notification type for the push notification. This key is a value thatâs defined by the identifier property of one of your appâs registered categories.

CollapseId -> (string)

An arbitrary identifier that, if assigned to multiple messages, APNs uses to coalesce the messages into a single push notification instead of delivering each message individually. This value canât exceed 64 bytes.

Amazon Pinpoint specifies this value in the apns-collapse-id request header when it sends the notification message to APNs.

Data -> (map)

The JSON payload to use for a silent push notification. This payload is added to the data.pinpoint.jsonBody object of the notification.

key -> (string)

value -> (string)

MediaUrl -> (string)

The URL of an image or video to display in the push notification.

PreferredAuthenticationMethod -> (string)

The authentication method that you want Amazon Pinpoint to use when authenticating with APNs, CERTIFICATE or TOKEN.

Priority -> (string)

para>5 - Low priority, the notification might be delayed, delivered as part of a group, or throttled.

/listitem>
* 10 - High priority, the notification is sent immediately. This is the default value. A high priority notification should trigger an alert, play a sound, or badge your appâs icon on the recipientâs device.
/para>

Amazon Pinpoint specifies this value in the apns-priority request header when it sends the notification message to APNs.

The equivalent values for Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), are normal, for 5, and high, for 10. If you specify an FCM value for this property, Amazon Pinpoint accepts and converts the value to the corresponding APNs value.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

### Note

If you specify the raw content of an APNs push notification, the message payload has to include the content-available key. The value of the content-available key has to be an integer, and can only be 0 or 1. If youâre sending a standard notification, set the value of content-available to 0. If youâre sending a silent (background) notification, set the value of content-available to 1. Additionally, silent notification payloads canât include the alert, badge, or sound keys. For more information, see [Generating a Remote Notification](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/generating_a_remote_notification) and [Pushing Background Updates to Your App](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) on the Apple Developer website.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification. A silent (or background) push notification isnât displayed on recipientsâ devices. You can use silent push notifications to make small updates to your app, or to display messages in an in-app message center.

Amazon Pinpoint uses this property to determine the correct value for the apns-push-type request header when it sends the notification message to APNs. If you specify a value of true for this property, Amazon Pinpoint sets the value for the apns-push-type header field to background.

### Note

If you specify the raw content of an APNs push notification, the message payload has to include the content-available key. For silent (background) notifications, set the value of content-available to 1. Additionally, the message payload for a silent notification canât include the alert, badge, or sound keys. For more information, see [Generating a Remote Notification](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/generating_a_remote_notification) and [Pushing Background Updates to Your App](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) on the Apple Developer website.

Apple has indicated that they will throttle âexcessiveâ background notifications based on current traffic volumes. To prevent your notifications being throttled, Apple recommends that you send no more than 3 silent push notifications to each recipient per hour.

Sound -> (string)

The key for the sound to play when the recipient receives the push notification. The value for this key is the name of a sound file in your appâs main bundle or the Library/Sounds folder in your appâs data container. If the sound file canât be found or you specify default for the value, the system plays the default alert sound.

Substitutions -> (map)

The default message variables to use in the notification message. You can override these default variables with individual address variables.

key -> (string)

value -> (list)

(string)

ThreadId -> (string)

The key that represents your app-specific identifier for grouping notifications. If you provide a Notification Content app extension, you can use this value to group your notifications together.

TimeToLive -> (integer)

The amount of time, in seconds, that APNs should store and attempt to deliver the push notification, if the service is unable to deliver the notification the first time. If this value is 0, APNs treats the notification as if it expires immediately and the service doesnât store or try to deliver the notification again.

Amazon Pinpoint specifies this value in the apns-expiration request header when it sends the notification message to APNs.

Title -> (string)

The title to display above the notification message on the recipientâs device.

Url -> (string)

The URL to open in the recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

BaiduMessage -> (structure)

The default push notification message for the Baidu (Baidu Cloud Push) channel. This message overrides the default push notification message (DefaultPushNotificationMessage).

Action -> (string)

The action to occur if the recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This action uses the deep-linking features of the Android platform.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message.

Data -> (map)

The JSON data payload to use for the push notification, if the notification is a silent push notification. This payload is added to the data.pinpoint.jsonBody object of the notification.

key -> (string)

value -> (string)

IconReference -> (string)

The icon image name of the asset saved in your app.

ImageIconUrl -> (string)

The URL of the large icon image to display in the content view of the push notification.

ImageUrl -> (string)

The URL of an image to display in the push notification.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration or supporting phone home functionality.

SmallImageIconUrl -> (string)

The URL of the small icon image to display in the status bar and the content view of the push notification.

Sound -> (string)

The sound to play when the recipient receives the push notification. You can use the default stream or specify the file name of a sound resource thatâs bundled in your app. On an Android platform, the sound file must reside in /res/raw/.

Substitutions -> (map)

The default message variables to use in the notification message. You can override the default variables with individual address variables.

key -> (string)

value -> (list)

(string)

TimeToLive -> (integer)

The amount of time, in seconds, that the Baidu Cloud Push service should store the message if the recipientâs device is offline. The default value and maximum supported time is 604,800 seconds (7 days).

Title -> (string)

The title to display above the notification message on the recipientâs device.

Url -> (string)

The URL to open in the recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

DefaultMessage -> (structure)

The default message for all channels.

Body -> (string)

The default body of the message.

Substitutions -> (map)

The default message variables to use in the message. You can override these default variables with individual address variables.

key -> (string)

value -> (list)

(string)

DefaultPushNotificationMessage -> (structure)

The default push notification message for all push notification channels.

Action -> (string)

The default action to occur if a recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of the iOS and Android platforms.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The default body of the notification message.

Data -> (map)

The JSON data payload to use for the default push notification, if the notification is a silent push notification. This payload is added to the data.pinpoint.jsonBody object of the notification.

key -> (string)

value -> (string)

SilentPush -> (boolean)

Specifies whether the default notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration or delivering messages to an in-app notification center.

Substitutions -> (map)

The default message variables to use in the notification message. You can override the default variables with individual address variables.

key -> (string)

value -> (list)

(string)

Title -> (string)

The default title to display above the notification message on a recipientâs device.

Url -> (string)

The default URL to open in a recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

EmailMessage -> (structure)

The default message for the email channel. This message overrides the default message (DefaultMessage).

Body -> (string)

The body of the email message.

FeedbackForwardingAddress -> (string)

The email address to forward bounces and complaints to, if feedback forwarding is enabled.

FromAddress -> (string)

The verified email address to send the email message from. The default value is the FromAddress specified for the email channel.

RawEmail -> (structure)

The email message, represented as a raw MIME message.

Data -> (blob)

The email message, represented as a raw MIME message. The entire message must be base64 encoded.

ReplyToAddresses -> (list)

The reply-to email address(es) for the email message. If a recipient replies to the email, each reply-to address receives the reply.

(string)

SimpleEmail -> (structure)

The email message, composed of a subject, a text part, and an HTML part.

HtmlPart -> (structure)

The body of the email message, in HTML format. We recommend using HTML format for email clients that render HTML content. You can include links, formatted text, and more in an HTML message.

Charset -> (string)

The applicable character set for the message content.

Data -> (string)

The textual data of the message content.

Subject -> (structure)

The subject line, or title, of the email.

Charset -> (string)

The applicable character set for the message content.

Data -> (string)

The textual data of the message content.

TextPart -> (structure)

The body of the email message, in plain text format. We recommend using plain text format for email clients that donât render HTML content and clients that are connected to high-latency networks, such as mobile devices.

Charset -> (string)

The applicable character set for the message content.

Data -> (string)

The textual data of the message content.

Headers -> (list)

The list of MessageHeaders for the email. You can have up to 15 Headers.

(structure)

Contains the name and value pair of an email header to add to your email. You can have up to 15 MessageHeaders. A header can contain information such as the sender, receiver, route, or timestamp.

Name -> (string)

The name of the message header. The header name can contain up to 126 characters.

Value -> (string)

The value of the message header. The header value can contain up to 870 characters, including the length of any rendered attributes. For example if you add the {CreationDate} attribute, it renders as YYYY-MM-DDTHH:MM:SS.SSSZ and is 24 characters in length.

Substitutions -> (map)

The default message variables to use in the email message. You can override the default variables with individual address variables.

key -> (string)

value -> (list)

(string)

GCMMessage -> (structure)

The default push notification message for the GCM channel, which is used to send notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service. This message overrides the default push notification message (DefaultPushNotificationMessage).

Action -> (string)

The action to occur if the recipient taps the push notification. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This action uses the deep-linking features of the Android platform.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The body of the notification message.

CollapseKey -> (string)

An arbitrary string that identifies a group of messages that can be collapsed to ensure that only the last message is sent when delivery can resume. This helps avoid sending too many instances of the same messages when the recipientâs device comes online again or becomes active.

Amazon Pinpoint specifies this value in the Firebase Cloud Messaging (FCM) collapse_key parameter when it sends the notification message to FCM.

Data -> (map)

The JSON data payload to use for the push notification, if the notification is a silent push notification. This payload is added to the data.pinpoint.jsonBody object of the notification.

key -> (string)

value -> (string)

IconReference -> (string)

The icon image name of the asset saved in your app.

ImageIconUrl -> (string)

The URL of the large icon image to display in the content view of the push notification.

ImageUrl -> (string)

The URL of an image to display in the push notification.

PreferredAuthenticationMethod -> (string)

The preferred authentication method, with valid values âKEYâ or âTOKENâ. If a value isnât provided then the **DefaultAuthenticationMethod** is used.

Priority -> (string)

para>normal â The notification might be delayed. Delivery is optimized for battery usage on the recipientâs device. Use this value unless immediate delivery is required.

/listitem>
* high â The notification is sent immediately and might wake a sleeping device.
/para>

Amazon Pinpoint specifies this value in the FCM priority parameter when it sends the notification message to FCM.

The equivalent values for Apple Push Notification service (APNs) are 5, for normal, and 10, for high. If you specify an APNs value for this property, Amazon Pinpoint accepts and converts the value to the corresponding FCM value.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.

RestrictedPackageName -> (string)

The package name of the application where registration tokens must match in order for the recipient to receive the message.

SilentPush -> (boolean)

Specifies whether the notification is a silent push notification, which is a push notification that doesnât display on a recipientâs device. Silent push notifications can be used for cases such as updating an appâs configuration or supporting phone home functionality.

SmallImageIconUrl -> (string)

The URL of the small icon image to display in the status bar and the content view of the push notification.

Sound -> (string)

The sound to play when the recipient receives the push notification. You can use the default stream or specify the file name of a sound resource thatâs bundled in your app. On an Android platform, the sound file must reside in /res/raw/.

Substitutions -> (map)

The default message variables to use in the notification message. You can override the default variables with individual address variables.

key -> (string)

value -> (list)

(string)

TimeToLive -> (integer)

The amount of time, in seconds, that FCM should store and attempt to deliver the push notification, if the service is unable to deliver the notification the first time. If you donât specify this value, FCM defaults to the maximum value, which is 2,419,200 seconds (28 days).

Amazon Pinpoint specifies this value in the FCM time_to_live parameter when it sends the notification message to FCM.

Title -> (string)

The title to display above the notification message on the recipientâs device.

Url -> (string)

The URL to open in the recipientâs default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.

SMSMessage -> (structure)

The default message for the SMS channel. This message overrides the default message (DefaultMessage).

Body -> (string)

The body of the SMS message.

Keyword -> (string)

The SMS program name that you provided to AWS Support when you requested your dedicated number.

MediaUrl -> (string)

This field is reserved for future use.

MessageType -> (string)

The SMS message type. Valid values are TRANSACTIONAL (for messages that are critical or time-sensitive, such as a one-time passwords) and PROMOTIONAL (for messsages that arenât critical or time-sensitive, such as marketing messages).

OriginationNumber -> (string)

The number to send the SMS message from. This value should be one of the dedicated long or short codes thatâs assigned to your AWS account. If you donât specify a long or short code, Amazon Pinpoint assigns a random long code to the SMS message and sends the message from that code.

SenderId -> (string)

The sender ID to display as the sender of the message on a recipientâs device. Support for sender IDs varies by country or region.

Substitutions -> (map)

The message variables to use in the SMS message. You can override the default variables with individual address variables.

key -> (string)

value -> (list)

(string)

EntityId -> (string)

The entity ID or Principal Entity (PE) id received from the regulatory body for sending SMS in your country.

TemplateId -> (string)

The template ID received from the regulatory body for sending SMS in your country.

VoiceMessage -> (structure)

The default message for the voice channel. This message overrides the default message (DefaultMessage).

Body -> (string)

The text of the script to use for the voice message.

LanguageCode -> (string)

The code for the language to use when synthesizing the text of the message script. For a list of supported languages and the code for each one, see the [Amazon Polly Developer Guide](https://docs.aws.amazon.com/polly/latest/dg/what-is.html) .

OriginationNumber -> (string)

The long code to send the voice message from. This value should be one of the dedicated long codes thatâs assigned to your AWS account. Although it isnât required, we recommend that you specify the long code in E.164 format, for example +12065550100, to ensure prompt and accurate delivery of the message.

Substitutions -> (map)

The default message variables to use in the voice message. You can override the default variables with individual address variables.

key -> (string)

value -> (list)

(string)

VoiceId -> (string)

The name of the voice to use when delivering the message. For a list of supported voices, see the [Amazon Polly Developer Guide](https://docs.aws.amazon.com/polly/latest/dg/what-is.html) .

TemplateConfiguration -> (structure)

The message template to use for the message.

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

TraceId -> (string)

The unique identifier for tracing the message. This identifier is visible to message recipients.

JSON Syntax:

```
{
  "Addresses": {"string": {
        "BodyOverride": "string",
        "ChannelType": "PUSH"|"GCM"|"APNS"|"APNS_SANDBOX"|"APNS_VOIP"|"APNS_VOIP_SANDBOX"|"ADM"|"SMS"|"VOICE"|"EMAIL"|"BAIDU"|"CUSTOM"|"IN_APP",
        "Context": {"string": "string"
          ...},
        "RawContent": "string",
        "Substitutions": {"string": ["string", ...]
          ...},
        "TitleOverride": "string"
      }
    ...},
  "Context": {"string": "string"
    ...},
  "Endpoints": {"string": {
        "BodyOverride": "string",
        "Context": {"string": "string"
          ...},
        "RawContent": "string",
        "Substitutions": {"string": ["string", ...]
          ...},
        "TitleOverride": "string"
      }
    ...},
  "MessageConfiguration": {
    "ADMMessage": {
      "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
      "Body": "string",
      "ConsolidationKey": "string",
      "Data": {"string": "string"
        ...},
      "ExpiresAfter": "string",
      "IconReference": "string",
      "ImageIconUrl": "string",
      "ImageUrl": "string",
      "MD5": "string",
      "RawContent": "string",
      "SilentPush": true|false,
      "SmallImageIconUrl": "string",
      "Sound": "string",
      "Substitutions": {"string": ["string", ...]
        ...},
      "Title": "string",
      "Url": "string"
    },
    "APNSMessage": {
      "APNSPushType": "string",
      "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
      "Badge": integer,
      "Body": "string",
      "Category": "string",
      "CollapseId": "string",
      "Data": {"string": "string"
        ...},
      "MediaUrl": "string",
      "PreferredAuthenticationMethod": "string",
      "Priority": "string",
      "RawContent": "string",
      "SilentPush": true|false,
      "Sound": "string",
      "Substitutions": {"string": ["string", ...]
        ...},
      "ThreadId": "string",
      "TimeToLive": integer,
      "Title": "string",
      "Url": "string"
    },
    "BaiduMessage": {
      "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
      "Body": "string",
      "Data": {"string": "string"
        ...},
      "IconReference": "string",
      "ImageIconUrl": "string",
      "ImageUrl": "string",
      "RawContent": "string",
      "SilentPush": true|false,
      "SmallImageIconUrl": "string",
      "Sound": "string",
      "Substitutions": {"string": ["string", ...]
        ...},
      "TimeToLive": integer,
      "Title": "string",
      "Url": "string"
    },
    "DefaultMessage": {
      "Body": "string",
      "Substitutions": {"string": ["string", ...]
        ...}
    },
    "DefaultPushNotificationMessage": {
      "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
      "Body": "string",
      "Data": {"string": "string"
        ...},
      "SilentPush": true|false,
      "Substitutions": {"string": ["string", ...]
        ...},
      "Title": "string",
      "Url": "string"
    },
    "EmailMessage": {
      "Body": "string",
      "FeedbackForwardingAddress": "string",
      "FromAddress": "string",
      "RawEmail": {
        "Data": blob
      },
      "ReplyToAddresses": ["string", ...],
      "SimpleEmail": {
        "HtmlPart": {
          "Charset": "string",
          "Data": "string"
        },
        "Subject": {
          "Charset": "string",
          "Data": "string"
        },
        "TextPart": {
          "Charset": "string",
          "Data": "string"
        },
        "Headers": [
          {
            "Name": "string",
            "Value": "string"
          }
          ...
        ]
      },
      "Substitutions": {"string": ["string", ...]
        ...}
    },
    "GCMMessage": {
      "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
      "Body": "string",
      "CollapseKey": "string",
      "Data": {"string": "string"
        ...},
      "IconReference": "string",
      "ImageIconUrl": "string",
      "ImageUrl": "string",
      "PreferredAuthenticationMethod": "string",
      "Priority": "string",
      "RawContent": "string",
      "RestrictedPackageName": "string",
      "SilentPush": true|false,
      "SmallImageIconUrl": "string",
      "Sound": "string",
      "Substitutions": {"string": ["string", ...]
        ...},
      "TimeToLive": integer,
      "Title": "string",
      "Url": "string"
    },
    "SMSMessage": {
      "Body": "string",
      "Keyword": "string",
      "MediaUrl": "string",
      "MessageType": "TRANSACTIONAL"|"PROMOTIONAL",
      "OriginationNumber": "string",
      "SenderId": "string",
      "Substitutions": {"string": ["string", ...]
        ...},
      "EntityId": "string",
      "TemplateId": "string"
    },
    "VoiceMessage": {
      "Body": "string",
      "LanguageCode": "string",
      "OriginationNumber": "string",
      "Substitutions": {"string": ["string", ...]
        ...},
      "VoiceId": "string"
    }
  },
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
  "TraceId": "string"
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To send SMS message using the endpoint of an application**

The following `send-messages` example sends a direct message for an application with an endpoint.

```
aws pinpoint send-messages \
    --application-id 611e3e3cdd47474c9c1399a505665b91 \
    --message-request file://myfile.json \
    --region us-west-2
```

Contents of `myfile.json`:

```
{
    "MessageConfiguration": {
        "SMSMessage": {
            "Body": "hello, how are you?"
        }
    },
    "Endpoints": {
        "testendpoint": {}
    }
}
```

Output:

```
{
    "MessageResponse": {
        "ApplicationId": "611e3e3cdd47474c9c1399a505665b91",
        "EndpointResult": {
            "testendpoint": {
                "Address": "+12345678900",
                "DeliveryStatus": "SUCCESSFUL",
                "MessageId": "itnuqhai5alf1n6ahv3udc05n7hhddr6gb3lq6g0",
                "StatusCode": 200,
                "StatusMessage": "MessageId: itnuqhai5alf1n6ahv3udc05n7hhddr6gb3lq6g0"
            }
        },
        "RequestId": "c7e23264-04b2-4a46-b800-d24923f74753"
    }
}
```

For more information, see [Amazon Pinpoint SMS channel](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms.html) in the *Amazon Pinpoint User Guide*.

## Output

MessageResponse -> (structure)

Provides information about the results of a request to send a message to an endpoint address.

ApplicationId -> (string)

The unique identifier for the application that was used to send the message.

EndpointResult -> (map)

A map that contains a multipart response for each address that the message was sent to. In the map, the endpoint ID is the key and the result is the value.

key -> (string)

value -> (structure)

Provides information about the delivery status and results of sending a message directly to an endpoint.

Address -> (string)

The endpoint address that the message was delivered to.

DeliveryStatus -> (string)

The delivery status of the message. Possible values are:

- DUPLICATE - The endpoint address is a duplicate of another endpoint address. Amazon Pinpoint wonât attempt to send the message again.
- OPT_OUT - The user whoâs associated with the endpoint has opted out of receiving messages from you. Amazon Pinpoint wonât attempt to send the message again.
- PERMANENT_FAILURE - An error occurred when delivering the message to the endpoint. Amazon Pinpoint wonât attempt to send the message again.
- SUCCESSFUL - The message was successfully delivered to the endpoint.
- TEMPORARY_FAILURE - A temporary error occurred. Amazon Pinpoint wonât attempt to send the message again.
- THROTTLED - Amazon Pinpoint throttled the operation to send the message to the endpoint.
- UNKNOWN_FAILURE - An unknown error occurred.

MessageId -> (string)

The unique identifier for the message that was sent.

StatusCode -> (integer)

The downstream service status code for delivering the message.

StatusMessage -> (string)

The status message for delivering the message.

UpdatedToken -> (string)

For push notifications that are sent through the GCM channel, specifies whether the endpointâs device registration token was updated as part of delivering the message.

RequestId -> (string)

The identifier for the original request that the message was delivered for.

Result -> (map)

A map that contains a multipart response for each address (email address, phone number, or push notification token) that the message was sent to. In the map, the address is the key and the result is the value.

key -> (string)

value -> (structure)

Provides information about the results of sending a message directly to an endpoint address.

DeliveryStatus -> (string)

The delivery status of the message. Possible values are:

- DUPLICATE - The endpoint address is a duplicate of another endpoint address. Amazon Pinpoint wonât attempt to send the message again.
- OPT_OUT - The user whoâs associated with the endpoint address has opted out of receiving messages from you. Amazon Pinpoint wonât attempt to send the message again.
- PERMANENT_FAILURE - An error occurred when delivering the message to the endpoint address. Amazon Pinpoint wonât attempt to send the message again.
- SUCCESSFUL - The message was successfully delivered to the endpoint address.
- TEMPORARY_FAILURE - A temporary error occurred. Amazon Pinpoint wonât attempt to send the message again.
- THROTTLED - Amazon Pinpoint throttled the operation to send the message to the endpoint address.
- UNKNOWN_FAILURE - An unknown error occurred.

MessageId -> (string)

The unique identifier for the message that was sent.

StatusCode -> (integer)

The downstream service status code for delivering the message.

StatusMessage -> (string)

The status message for delivering the message.

UpdatedToken -> (string)

For push notifications that are sent through the GCM channel, specifies whether the endpointâs device registration token was updated as part of delivering the message.