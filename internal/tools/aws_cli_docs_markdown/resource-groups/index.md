# resource-groupsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# resource-groups

## Description

Resource Groups lets you organize Amazon Web Services resources such as Amazon Elastic Compute Cloud instances, Amazon Relational Database Service databases, and Amazon Simple Storage Service buckets into groups using criteria that you define as tags. A resource group is a collection of resources that match the resource types specified in a query, and share one or more tags or portions of tags. You can create a group of resources based on their roles in your cloud infrastructure, lifecycle stages, regions, application layers, or virtually any criteria. Resource Groups enable you to automate management tasks, such as those in Amazon Web Services Systems Manager Automation documents, on tag-related resources in Amazon Web Services Systems Manager. Groups of tagged resources also let you quickly view a custom console in Amazon Web Services Systems Manager that shows Config compliance and other monitoring data about member resources.

To create a resource group, build a resource query, and specify tags that identify the criteria that members of the group have in common. Tags are key-value pairs.

For more information about Resource Groups, see the [Resource Groups User Guide](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html) .

Resource Groups uses a REST-compliant API that you can use to perform the following types of operations.

- Create, Read, Update, and Delete (CRUD) operations on resource groups and resource query entities
- Applying, editing, and removing tags from resource groups
- Resolving resource group member Amazon resource names (ARN)s so they can be returned as search results
- Getting data about resources that are members of a group
- Searching Amazon Web Services resources based on a resource query

## Available Commands

- [cancel-tag-sync-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/cancel-tag-sync-task.html)
- [create-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/create-group.html)
- [delete-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/delete-group.html)
- [get-account-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/get-account-settings.html)
- [get-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/get-group.html)
- [get-group-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/get-group-configuration.html)
- [get-group-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/get-group-query.html)
- [get-tag-sync-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/get-tag-sync-task.html)
- [get-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/get-tags.html)
- [group-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/group-resources.html)
- [list-group-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/list-group-resources.html)
- [list-grouping-statuses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/list-grouping-statuses.html)
- [list-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/list-groups.html)
- [list-tag-sync-tasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/list-tag-sync-tasks.html)
- [put-group-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/put-group-configuration.html)
- [search-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/search-resources.html)
- [start-tag-sync-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/start-tag-sync-task.html)
- [tag](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/tag.html)
- [ungroup-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/ungroup-resources.html)
- [untag](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/untag.html)
- [update-account-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/update-account-settings.html)
- [update-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/update-group.html)
- [update-group-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/update-group-query.html)