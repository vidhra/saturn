# networkflowmonitorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# networkflowmonitor

## Description

Network Flow Monitor is a feature of Amazon CloudWatch Network Monitoring that provides visibility into the performance of network flows for your Amazon Web Services workloads, between instances in subnets, as well as to and from Amazon Web Services. Lightweight agents that you install on the instances capture performance metrics for your network flows, such as packet loss and latency, and send them to the Network Flow Monitor backend. Then, you can view and analyze metrics from the top contributors for each metric type, to help troubleshoot issues.

In addition, when you create a monitor, Network Flow Monitor provides a network health indicator (NHI) that informs you whether there were Amazon Web Services network issues for one or more of the network flows tracked by a monitor, during a time period that you choose. By using this value, you can independently determine if the Amazon Web Services network is impacting your workload during a specific time frame, to help you focus troubleshooting efforts.

To learn more about Network Flow Monitor, see the [Network Flow Monitor User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor.html) in the Amazon CloudWatch User Guide.

## Available Commands

- [create-monitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/create-monitor.html)
- [create-scope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/create-scope.html)
- [delete-monitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/delete-monitor.html)
- [delete-scope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/delete-scope.html)
- [get-monitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/get-monitor.html)
- [get-query-results-monitor-top-contributors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/get-query-results-monitor-top-contributors.html)
- [get-query-results-workload-insights-top-contributors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/get-query-results-workload-insights-top-contributors.html)
- [get-query-results-workload-insights-top-contributors-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/get-query-results-workload-insights-top-contributors-data.html)
- [get-query-status-monitor-top-contributors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/get-query-status-monitor-top-contributors.html)
- [get-query-status-workload-insights-top-contributors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/get-query-status-workload-insights-top-contributors.html)
- [get-query-status-workload-insights-top-contributors-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/get-query-status-workload-insights-top-contributors-data.html)
- [get-scope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/get-scope.html)
- [list-monitors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/list-monitors.html)
- [list-scopes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/list-scopes.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/list-tags-for-resource.html)
- [start-query-monitor-top-contributors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/start-query-monitor-top-contributors.html)
- [start-query-workload-insights-top-contributors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/start-query-workload-insights-top-contributors.html)
- [start-query-workload-insights-top-contributors-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/start-query-workload-insights-top-contributors-data.html)
- [stop-query-monitor-top-contributors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/stop-query-monitor-top-contributors.html)
- [stop-query-workload-insights-top-contributors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/stop-query-workload-insights-top-contributors.html)
- [stop-query-workload-insights-top-contributors-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/stop-query-workload-insights-top-contributors-data.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/untag-resource.html)
- [update-monitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/update-monitor.html)
- [update-scope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/update-scope.html)