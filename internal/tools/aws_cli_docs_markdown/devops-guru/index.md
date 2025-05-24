# devops-guruÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# devops-guru

## Description

Amazon DevOps Guru is a fully managed service that helps you identify anomalous behavior in business critical operational applications. You specify the Amazon Web Services resources that you want DevOps Guru to cover, then the Amazon CloudWatch metrics and Amazon Web Services CloudTrail events related to those resources are analyzed. When anomalous behavior is detected, DevOps Guru creates an *insight* that includes recommendations, related events, and related metrics that can help you improve your operational applications. For more information, see [What is Amazon DevOps Guru](https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html) .

You can specify 1 or 2 Amazon Simple Notification Service topics so you are notified every time a new insight is created. You can also enable DevOps Guru to generate an OpsItem in Amazon Web Services Systems Manager for each insight to help you manage and track your work addressing insights.

To learn about the DevOps Guru workflow, see [How DevOps Guru works](https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html#how-it-works) . To learn about DevOps Guru concepts, see [Concepts in DevOps Guru](https://docs.aws.amazon.com/devops-guru/latest/userguide/concepts.html) .

## Available Commands

- [add-notification-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/add-notification-channel.html)
- [delete-insight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/delete-insight.html)
- [describe-account-health](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/describe-account-health.html)
- [describe-account-overview](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/describe-account-overview.html)
- [describe-anomaly](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/describe-anomaly.html)
- [describe-event-sources-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/describe-event-sources-config.html)
- [describe-feedback](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/describe-feedback.html)
- [describe-insight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/describe-insight.html)
- [describe-organization-health](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/describe-organization-health.html)
- [describe-organization-overview](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/describe-organization-overview.html)
- [describe-organization-resource-collection-health](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/describe-organization-resource-collection-health.html)
- [describe-resource-collection-health](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/describe-resource-collection-health.html)
- [describe-service-integration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/describe-service-integration.html)
- [get-cost-estimation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/get-cost-estimation.html)
- [get-resource-collection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/get-resource-collection.html)
- [list-anomalies-for-insight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/list-anomalies-for-insight.html)
- [list-anomalous-log-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/list-anomalous-log-groups.html)
- [list-events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/list-events.html)
- [list-insights](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/list-insights.html)
- [list-monitored-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/list-monitored-resources.html)
- [list-notification-channels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/list-notification-channels.html)
- [list-organization-insights](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/list-organization-insights.html)
- [list-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/list-recommendations.html)
- [put-feedback](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/put-feedback.html)
- [remove-notification-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/remove-notification-channel.html)
- [search-insights](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/search-insights.html)
- [search-organization-insights](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/search-organization-insights.html)
- [start-cost-estimation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/start-cost-estimation.html)
- [update-event-sources-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/update-event-sources-config.html)
- [update-resource-collection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/update-resource-collection.html)
- [update-service-integration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/update-service-integration.html)