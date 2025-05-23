# notificationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# notifications

## Description

The *Amazon Web Services User Notifications API Reference* provides descriptions, API request parameters, and the JSON response for each of the User Notification API actions.

User Notification control plane APIs are currently available in US East (Virginia) - `us-east-1` .

[GetNotificationEvent](https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetNotificationEvent.html) and [ListNotificationEvents](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListNotificationEvents.html) APIs are currently available in [commercial partition Regions](https://docs.aws.amazon.com/notifications/latest/userguide/supported-regions.html) and only return notifications stored in the same Region in which theyâre called.

The User Notifications console can only be used in US East (Virginia). Your data however, is stored in each Region chosen as a [notification hub](https://docs.aws.amazon.com/notifications/latest/userguide/notification-hubs.html) in addition to US East (Virginia).

## Available Commands

- [associate-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/associate-channel.html)
- [associate-managed-notification-account-contact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/associate-managed-notification-account-contact.html)
- [associate-managed-notification-additional-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/associate-managed-notification-additional-channel.html)
- [create-event-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/create-event-rule.html)
- [create-notification-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/create-notification-configuration.html)
- [delete-event-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/delete-event-rule.html)
- [delete-notification-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/delete-notification-configuration.html)
- [deregister-notification-hub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/deregister-notification-hub.html)
- [disable-notifications-access-for-organization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/disable-notifications-access-for-organization.html)
- [disassociate-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/disassociate-channel.html)
- [disassociate-managed-notification-account-contact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/disassociate-managed-notification-account-contact.html)
- [disassociate-managed-notification-additional-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/disassociate-managed-notification-additional-channel.html)
- [enable-notifications-access-for-organization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/enable-notifications-access-for-organization.html)
- [get-event-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/get-event-rule.html)
- [get-managed-notification-child-event](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/get-managed-notification-child-event.html)
- [get-managed-notification-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/get-managed-notification-configuration.html)
- [get-managed-notification-event](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/get-managed-notification-event.html)
- [get-notification-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/get-notification-configuration.html)
- [get-notification-event](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/get-notification-event.html)
- [get-notifications-access-for-organization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/get-notifications-access-for-organization.html)
- [list-channels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/list-channels.html)
- [list-event-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/list-event-rules.html)
- [list-managed-notification-channel-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/list-managed-notification-channel-associations.html)
- [list-managed-notification-child-events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/list-managed-notification-child-events.html)
- [list-managed-notification-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/list-managed-notification-configurations.html)
- [list-managed-notification-events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/list-managed-notification-events.html)
- [list-notification-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/list-notification-configurations.html)
- [list-notification-events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/list-notification-events.html)
- [list-notification-hubs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/list-notification-hubs.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/list-tags-for-resource.html)
- [register-notification-hub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/register-notification-hub.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/untag-resource.html)
- [update-event-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/update-event-rule.html)
- [update-notification-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/notifications/update-notification-configuration.html)