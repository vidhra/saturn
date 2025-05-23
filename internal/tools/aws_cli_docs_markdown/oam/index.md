# oamÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# oam

## Description

Use Amazon CloudWatch Observability Access Manager to create and manage links between source accounts and monitoring accounts by using *CloudWatch cross-account observability* . With CloudWatch cross-account observability, you can monitor and troubleshoot applications that span multiple accounts within a Region. Seamlessly search, visualize, and analyze your metrics, logs, traces, Application Signals services and service level objectives (SLOs), Application Insights applications, and internet monitors in any of the linked accounts without account boundaries.

Set up one or more Amazon Web Services accounts as *monitoring accounts* and link them with multiple *source accounts* . A monitoring account is a central Amazon Web Services account that can view and interact with observability data generated from source accounts. A source account is an individual Amazon Web Services account that generates observability data for the resources that reside in it. Source accounts share their observability data with the monitoring account. The shared observability data can include metrics in Amazon CloudWatch, logs in Amazon CloudWatch Logs, traces in X-Ray, Application Signals services and service level objectives (SLOs), applications in Amazon CloudWatch Application Insights, and internet monitors in CloudWatch Internet Monitor.

When you set up a link, you can choose to share the metrics from all namespaces with the monitoring account, or filter to a subset of namespaces. And for CloudWatch Logs, you can choose to share all log groups with the monitoring account, or filter to a subset of log groups.

## Available Commands

- [create-link](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/create-link.html)
- [create-sink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/create-sink.html)
- [delete-link](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/delete-link.html)
- [delete-sink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/delete-sink.html)
- [get-link](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/get-link.html)
- [get-sink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/get-sink.html)
- [get-sink-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/get-sink-policy.html)
- [list-attached-links](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/list-attached-links.html)
- [list-links](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/list-links.html)
- [list-sinks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/list-sinks.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/list-tags-for-resource.html)
- [put-sink-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/put-sink-policy.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/untag-resource.html)
- [update-link](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/update-link.html)