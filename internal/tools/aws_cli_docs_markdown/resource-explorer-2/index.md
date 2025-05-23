# resource-explorer-2Â¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# resource-explorer-2

## Description

Amazon Web Services Resource Explorer is a resource search and discovery service. By using Resource Explorer, you can explore your resources using an internet search engine-like experience. Examples of resources include Amazon Relational Database Service (Amazon RDS) instances, Amazon Simple Storage Service (Amazon S3) buckets, or Amazon DynamoDB tables. You can search for your resources using resource metadata like names, tags, and IDs. Resource Explorer can search across all of the Amazon Web Services Regions in your account in which you turn the service on, to simplify your cross-Region workloads.

Resource Explorer scans the resources in each of the Amazon Web Services Regions in your Amazon Web Services account in which you turn on Resource Explorer. Resource Explorer [creates and maintains an index](https://docs.aws.amazon.com/resource-explorer/latest/userguide/getting-started-terms-and-concepts.html#term-index) in each Region, with the details of that Regionâs resources.

You can [search across all of the indexed Regions in your account](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html) by designating one of your Amazon Web Services Regions to contain the aggregator index for the account. When you [promote a local index in a Region to become the aggregator index for the account](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region-turn-on.html) , Resource Explorer automatically replicates the index information from all local indexes in the other Regions to the aggregator index. Therefore, the Region with the aggregator index has a copy of all resource information for all Regions in the account where you turned on Resource Explorer. As a result, views in the aggregator index Region include resources from all of the indexed Regions in your account.

For more information about Amazon Web Services Resource Explorer, including how to enable and configure the service, see the [Amazon Web Services Resource Explorer User Guide](https://docs.aws.amazon.com/resource-explorer/latest/userguide/) .

## Available Commands

- [associate-default-view](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/associate-default-view.html)
- [batch-get-view](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/batch-get-view.html)
- [create-index](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/create-index.html)
- [create-view](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/create-view.html)
- [delete-index](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/delete-index.html)
- [delete-view](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/delete-view.html)
- [disassociate-default-view](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/disassociate-default-view.html)
- [get-account-level-service-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/get-account-level-service-configuration.html)
- [get-default-view](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/get-default-view.html)
- [get-index](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/get-index.html)
- [get-managed-view](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/get-managed-view.html)
- [get-view](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/get-view.html)
- [list-indexes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/list-indexes.html)
- [list-indexes-for-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/list-indexes-for-members.html)
- [list-managed-views](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/list-managed-views.html)
- [list-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/list-resources.html)
- [list-supported-resource-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/list-supported-resource-types.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/list-tags-for-resource.html)
- [list-views](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/list-views.html)
- [search](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/search.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/untag-resource.html)
- [update-index-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/update-index-type.html)
- [update-view](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/update-view.html)