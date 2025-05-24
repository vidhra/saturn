# syntheticsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# synthetics

## Description

You can use Amazon CloudWatch Synthetics to continually monitor your services. You can create and manage *canaries* , which are modular, lightweight scripts that monitor your endpoints and APIs from the outside-in. You can set up your canaries to run 24 hours a day, once per minute. The canaries help you check the availability and latency of your web services and troubleshoot anomalies by investigating load time data, screenshots of the UI, logs, and metrics. The canaries seamlessly integrate with CloudWatch ServiceLens to help you trace the causes of impacted nodes in your applications. For more information, see [Using ServiceLens to Monitor the Health of Your Applications](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceLens.html) in the *Amazon CloudWatch User Guide* .

Before you create and manage canaries, be aware of the security considerations. For more information, see [Security Considerations for Synthetics Canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html) .

## Available Commands

- [associate-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/associate-resource.html)
- [create-canary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/create-canary.html)
- [create-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/create-group.html)
- [delete-canary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/delete-canary.html)
- [delete-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/delete-group.html)
- [describe-canaries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/describe-canaries.html)
- [describe-canaries-last-run](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/describe-canaries-last-run.html)
- [describe-runtime-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/describe-runtime-versions.html)
- [disassociate-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/disassociate-resource.html)
- [get-canary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/get-canary.html)
- [get-canary-runs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/get-canary-runs.html)
- [get-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/get-group.html)
- [list-associated-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/list-associated-groups.html)
- [list-group-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/list-group-resources.html)
- [list-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/list-groups.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/list-tags-for-resource.html)
- [start-canary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/start-canary.html)
- [start-canary-dry-run](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/start-canary-dry-run.html)
- [stop-canary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/stop-canary.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/untag-resource.html)
- [update-canary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/update-canary.html)