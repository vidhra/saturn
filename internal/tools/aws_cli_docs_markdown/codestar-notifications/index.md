# codestar-notificationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# codestar-notifications

## Description

This AWS CodeStar Notifications API Reference provides descriptions and usage examples of the operations and data types for the AWS CodeStar Notifications API. You can use the AWS CodeStar Notifications API to work with the following objects:

Notification rules, by calling the following:

- CreateNotificationRule , which creates a notification rule for a resource in your account.
- DeleteNotificationRule , which deletes a notification rule.
- DescribeNotificationRule , which provides information about a notification rule.
- ListNotificationRules , which lists the notification rules associated with your account.
- UpdateNotificationRule , which changes the name, events, or targets associated with a notification rule.
- Subscribe , which subscribes a target to a notification rule.
- Unsubscribe , which removes a target from a notification rule.

Targets, by calling the following:

- DeleteTarget , which removes a notification rule target from a notification rule.
- ListTargets , which lists the targets associated with a notification rule.

Events, by calling the following:

- ListEventTypes , which lists the event types you can include in a notification rule.

Tags, by calling the following:

- ListTagsForResource , which lists the tags already associated with a notification rule in your account.
- TagResource , which associates a tag you provide with a notification rule in your account.
- UntagResource , which removes a tag from a notification rule in your account.

For information about how to use AWS CodeStar Notifications, see the [Amazon Web Services Developer Tools Console User Guide](https://docs.aws.amazon.com/dtconsole/latest/userguide/what-is-dtconsole.html) .

## Available Commands

- [create-notification-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/create-notification-rule.html)
- [delete-notification-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/delete-notification-rule.html)
- [delete-target](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/delete-target.html)
- [describe-notification-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/describe-notification-rule.html)
- [list-event-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/list-event-types.html)
- [list-notification-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/list-notification-rules.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/list-tags-for-resource.html)
- [list-targets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/list-targets.html)
- [subscribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/subscribe.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/tag-resource.html)
- [unsubscribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/unsubscribe.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/untag-resource.html)
- [update-notification-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/update-notification-rule.html)