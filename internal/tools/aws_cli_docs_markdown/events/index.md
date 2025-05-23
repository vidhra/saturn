# eventsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# events

## Description

Amazon EventBridge helps you to respond to state changes in your Amazon Web Services resources. When your resources change state, they automatically send events to an event stream. You can create rules that match selected events in the stream and route them to targets to take action. You can also use rules to take action on a predetermined schedule. For example, you can configure rules to:

- Automatically invoke an Lambda function to update DNS entries when an event notifies you that Amazon EC2 instance enters the running state.
- Direct specific API records from CloudTrail to an Amazon Kinesis data stream for detailed analysis of potential security or availability risks.
- Periodically invoke a built-in target to create a snapshot of an Amazon EBS volume.

For more information about the features of Amazon EventBridge, see the [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide) .

## Available Commands

- [activate-event-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/activate-event-source.html)
- [cancel-replay](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/cancel-replay.html)
- [create-api-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/create-api-destination.html)
- [create-archive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/create-archive.html)
- [create-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/create-connection.html)
- [create-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/create-endpoint.html)
- [create-event-bus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/create-event-bus.html)
- [create-partner-event-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/create-partner-event-source.html)
- [deactivate-event-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/deactivate-event-source.html)
- [deauthorize-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/deauthorize-connection.html)
- [delete-api-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-api-destination.html)
- [delete-archive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-archive.html)
- [delete-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-connection.html)
- [delete-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-endpoint.html)
- [delete-event-bus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-event-bus.html)
- [delete-partner-event-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-partner-event-source.html)
- [delete-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-rule.html)
- [describe-api-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-api-destination.html)
- [describe-archive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-archive.html)
- [describe-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-connection.html)
- [describe-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-endpoint.html)
- [describe-event-bus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-event-bus.html)
- [describe-event-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-event-source.html)
- [describe-partner-event-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-partner-event-source.html)
- [describe-replay](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-replay.html)
- [describe-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-rule.html)
- [disable-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/disable-rule.html)
- [enable-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/enable-rule.html)
- [list-api-destinations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-api-destinations.html)
- [list-archives](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-archives.html)
- [list-connections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-connections.html)
- [list-endpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-endpoints.html)
- [list-event-buses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-event-buses.html)
- [list-event-sources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-event-sources.html)
- [list-partner-event-source-accounts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-partner-event-source-accounts.html)
- [list-partner-event-sources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-partner-event-sources.html)
- [list-replays](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-replays.html)
- [list-rule-names-by-target](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-rule-names-by-target.html)
- [list-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-rules.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-tags-for-resource.html)
- [list-targets-by-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-targets-by-rule.html)
- [put-events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-events.html)
- [put-partner-events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-partner-events.html)
- [put-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-permission.html)
- [put-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-rule.html)
- [put-targets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-targets.html)
- [remove-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/remove-permission.html)
- [remove-targets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/remove-targets.html)
- [start-replay](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/start-replay.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/tag-resource.html)
- [test-event-pattern](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/test-event-pattern.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/untag-resource.html)
- [update-api-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/update-api-destination.html)
- [update-archive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/update-archive.html)
- [update-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/update-connection.html)
- [update-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/update-endpoint.html)
- [update-event-bus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/update-event-bus.html)
- [wizard](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/wizard/index.html)