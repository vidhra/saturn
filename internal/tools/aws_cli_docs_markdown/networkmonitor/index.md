# networkmonitorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# networkmonitor

## Description

Amazon CloudWatch Network Monitor is an Amazon Web Services active network monitoring service that identifies if a network issues exists within the Amazon Web Services network or your own company network. Within Network Monitor youâll choose the source VPCs and subnets from the Amazon Web Services network in which you operate and then youâll choose the destination IP addresses from your on-premises network. From these sources and destinations, Network Monitor creates a monitor containing all the possible source and destination combinations, each of which is called a probe, within a single monitor. These probes then monitor network traffic to help you identify where network issues might be affecting your traffic.

Before you begin, ensure the Amazon Web Services CLI is configured in the Amazon Web Services Account where you will create the Network Monitor resource. Network Monitor doesnât support creation on cross-account resources, but you can create a Network Monitor in any subnet belonging to a VPC owned by your Account.

For more information, see [Using Amazon CloudWatch Network Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/what-is-network-monitor.html) in the *Amazon CloudWatch User Guide* .

## Available Commands

- [create-monitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/create-monitor.html)
- [create-probe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/create-probe.html)
- [delete-monitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/delete-monitor.html)
- [delete-probe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/delete-probe.html)
- [get-monitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/get-monitor.html)
- [get-probe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/get-probe.html)
- [list-monitors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/list-monitors.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/list-tags-for-resource.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/untag-resource.html)
- [update-monitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/update-monitor.html)
- [update-probe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmonitor/update-probe.html)