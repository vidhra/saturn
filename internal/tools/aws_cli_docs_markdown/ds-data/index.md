# ds-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# ds-data

## Description

Amazon Web Services Directory Service Data is an extension of Directory Service. This API reference provides detailed information about Directory Service Data operations and object types.

With Directory Service Data, you can create, read, update, and delete users, groups, and memberships from your Managed Microsoft AD without additional costs and without deploying dedicated management instances. You can also perform built-in object management tasks across directories without direct network connectivity, which simplifies provisioning and access management to achieve fully automated deployments. Directory Service Data supports user and group write operations, such as `CreateUser` and `CreateGroup` , within the organizational unit (OU) of your Managed Microsoft AD. Directory Service Data supports read operations, such as `ListUsers` and `ListGroups` , on all users, groups, and group memberships within your Managed Microsoft AD and across trusted realms. Directory Service Data supports adding and removing group members in your OU and the Amazon Web Services Delegated Groups OU, so you can grant and deny access to specific roles and permissions. For more information, see [Manage users and groups](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups.html) in the *Directory Service Administration Guide* .

### Note

Directory management operations and configuration changes made against the Directory Service API will also reflect in Directory Service Data API with eventual consistency. You can expect a short delay between management changes, such as adding a new directory trust and calling the Directory Service Data API for the newly created trusted realm.

Directory Service Data connects to your Managed Microsoft AD domain controllers and performs operations on underlying directory objects. When you create your Managed Microsoft AD, you choose subnets for domain controllers that Directory Service creates on your behalf. If a domain controller is unavailable, Directory Service Data uses an available domain controller. As a result, you might notice eventual consistency while objects replicate from one domain controller to another domain controller. For more information, see [What gets created](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.html) in the *Directory Service Administration Guide* . Directory limits vary by Managed Microsoft AD edition:

- **Standard edition** â Supports 8 transactions per second (TPS) for read operations and 4 TPS for write operations per directory. Thereâs a concurrency limit of 10 concurrent requests.
- **Enterprise edition** â Supports 16 transactions per second (TPS) for read operations and 8 TPS for write operations per directory. Thereâs a concurrency limit of 10 concurrent requests.
- **Amazon Web Services Account** - Supports a total of 100 TPS for Directory Service Data operations across all directories.

Directory Service Data only supports the Managed Microsoft AD directory type and is only available in the primary Amazon Web Services Region. For more information, see [Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) and [Primary vs additional Regions](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/multi-region-global-primary-additional.html) in the *Directory Service Administration Guide* .

## Available Commands

- [add-group-member](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/add-group-member.html)
- [create-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/create-group.html)
- [create-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/create-user.html)
- [delete-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/delete-group.html)
- [delete-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/delete-user.html)
- [describe-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/describe-group.html)
- [describe-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/describe-user.html)
- [disable-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/disable-user.html)
- [list-group-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/list-group-members.html)
- [list-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/list-groups.html)
- [list-groups-for-member](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/list-groups-for-member.html)
- [list-users](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/list-users.html)
- [remove-group-member](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/remove-group-member.html)
- [search-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/search-groups.html)
- [search-users](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/search-users.html)
- [update-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/update-group.html)
- [update-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/update-user.html)