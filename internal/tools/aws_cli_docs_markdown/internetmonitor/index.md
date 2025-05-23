# internetmonitorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# internetmonitor

## Description

Amazon CloudWatch Internet Monitor provides visibility into how internet issues impact the performance and availability between your applications hosted on Amazon Web Services and your end users. It can reduce the time it takes for you to diagnose internet issues from days to minutes. Internet Monitor uses the connectivity data that Amazon Web Services captures from its global networking footprint to calculate a baseline of performance and availability for internet traffic. This is the same data that Amazon Web Services uses to monitor internet uptime and availability. With those measurements as a baseline, Internet Monitor raises awareness for you when there are significant problems for your end users in the different geographic locations where your application runs.

Internet Monitor publishes internet measurements to CloudWatch Logs and CloudWatch Metrics, to easily support using CloudWatch tools with health information for geographies and networks specific to your application. Internet Monitor sends health events to Amazon EventBridge so that you can set up notifications. If an issue is caused by the Amazon Web Services network, you also automatically receive an Amazon Web Services Health Dashboard notification with the steps that Amazon Web Services is taking to mitigate the problem.

To use Internet Monitor, you create a *monitor* and associate your applicationâs resources with it - VPCs, NLBs, CloudFront distributions, or WorkSpaces directories - so Internet Monitor can determine where your applicationâs internet traffic is. Internet Monitor then provides internet measurements from Amazon Web Services that are specific to the locations and ASNs (typically, internet service providers or ISPs) that communicate with your application.

For more information, see [Using Amazon CloudWatch Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html) in the *Amazon CloudWatch User Guide* .

## Available Commands

- [create-monitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/create-monitor.html)
- [delete-monitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/delete-monitor.html)
- [get-health-event](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/get-health-event.html)
- [get-internet-event](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/get-internet-event.html)
- [get-monitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/get-monitor.html)
- [get-query-results](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/get-query-results.html)
- [get-query-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/get-query-status.html)
- [list-health-events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/list-health-events.html)
- [list-internet-events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/list-internet-events.html)
- [list-monitors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/list-monitors.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/list-tags-for-resource.html)
- [start-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/start-query.html)
- [stop-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/stop-query.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/untag-resource.html)
- [update-monitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/update-monitor.html)