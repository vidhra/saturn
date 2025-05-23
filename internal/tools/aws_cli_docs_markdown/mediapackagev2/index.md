# mediapackagev2Â¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# mediapackagev2

## Description

### Note

This guide is intended for creating AWS Elemental MediaPackage resources in MediaPackage Version 2 (v2) starting from May 2023. To get started with MediaPackage v2, create your MediaPackage resources. There isnât an automated process to migrate your resources from MediaPackage v1 to MediaPackage v2.

The names of the entities that you use to access this API, like URLs and ARNs, all have the versioning information added, like âv2â, to distinguish from the prior version. If you used MediaPackage prior to this release, you canât use the MediaPackage v2 CLI or the MediaPackage v2 API to access any MediaPackage v1 resources.

If you created resources in MediaPackage v1, use video on demand (VOD) workflows, and arenât looking to migrate to MediaPackage v2 yet, see the [MediaPackage v1 Live API Reference](https://docs.aws.amazon.com/mediapackage/latest/apireference/what-is.html) .

This is the AWS Elemental MediaPackage v2 Live REST API Reference. It describes all the MediaPackage API operations for live content in detail, and provides sample requests, responses, and errors for the supported web services protocols.

We assume that you have the IAM permissions that you need to use MediaPackage via the REST API. We also assume that you are familiar with the features and operations of MediaPackage, as described in the AWS Elemental MediaPackage User Guide.

## Available Commands

- [cancel-harvest-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/cancel-harvest-job.html)
- [create-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/create-channel.html)
- [create-channel-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/create-channel-group.html)
- [create-harvest-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/create-harvest-job.html)
- [create-origin-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/create-origin-endpoint.html)
- [delete-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/delete-channel.html)
- [delete-channel-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/delete-channel-group.html)
- [delete-channel-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/delete-channel-policy.html)
- [delete-origin-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/delete-origin-endpoint.html)
- [delete-origin-endpoint-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/delete-origin-endpoint-policy.html)
- [get-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/get-channel.html)
- [get-channel-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/get-channel-group.html)
- [get-channel-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/get-channel-policy.html)
- [get-harvest-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/get-harvest-job.html)
- [get-origin-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/get-origin-endpoint.html)
- [get-origin-endpoint-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/get-origin-endpoint-policy.html)
- [list-channel-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/list-channel-groups.html)
- [list-channels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/list-channels.html)
- [list-harvest-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/list-harvest-jobs.html)
- [list-origin-endpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/list-origin-endpoints.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/list-tags-for-resource.html)
- [put-channel-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/put-channel-policy.html)
- [put-origin-endpoint-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/put-origin-endpoint-policy.html)
- [reset-channel-state](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/reset-channel-state.html)
- [reset-origin-endpoint-state](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/reset-origin-endpoint-state.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/untag-resource.html)
- [update-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/update-channel.html)
- [update-channel-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/update-channel-group.html)
- [update-origin-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/update-origin-endpoint.html)
- [wait](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/wait/index.html)