# detectiveÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# detective

## Description

Detective uses machine learning and purpose-built visualizations to help you to analyze and investigate security issues across your Amazon Web Services (Amazon Web Services) workloads. Detective automatically extracts time-based events such as login attempts, API calls, and network traffic from CloudTrail and Amazon Virtual Private Cloud (Amazon VPC) flow logs. It also extracts findings detected by Amazon GuardDuty.

The Detective API primarily supports the creation and management of behavior graphs. A behavior graph contains the extracted data from a set of member accounts, and is created and managed by an administrator account.

To add a member account to the behavior graph, the administrator account sends an invitation to the account. When the account accepts the invitation, it becomes a member account in the behavior graph.

Detective is also integrated with Organizations. The organization management account designates the Detective administrator account for the organization. That account becomes the administrator account for the organization behavior graph. The Detective administrator account is also the delegated administrator account for Detective in Organizations.

The Detective administrator account can enable any organization account as a member account in the organization behavior graph. The organization accounts do not receive invitations. The Detective administrator account can also invite other accounts to the organization behavior graph.

Every behavior graph is specific to a Region. You can only use the API to manage behavior graphs that belong to the Region that is associated with the currently selected endpoint.

The administrator account for a behavior graph can use the Detective API to do the following:

- Enable and disable Detective. Enabling Detective creates a new behavior graph.
- View the list of member accounts in a behavior graph.
- Add member accounts to a behavior graph.
- Remove member accounts from a behavior graph.
- Apply tags to a behavior graph.

The organization management account can use the Detective API to select the delegated administrator for Detective.

The Detective administrator account for an organization can use the Detective API to do the following:

- Perform all of the functions of an administrator account.
- Determine whether to automatically enable new organization accounts as member accounts in the organization behavior graph.

An invited member account can use the Detective API to do the following:

- View the list of behavior graphs that they are invited to.
- Accept an invitation to contribute to a behavior graph.
- Decline an invitation to contribute to a behavior graph.
- Remove their account from a behavior graph.

All API actions are logged as CloudTrail events. See [Logging Detective API Calls with CloudTrail](https://docs.aws.amazon.com/detective/latest/userguide/logging-using-cloudtrail.html) .

### Note

We replaced the term âmaster accountâ with the term âadministrator accountâ. An administrator account is used to centrally manage multiple accounts. In the case of Detective, the administrator account manages the accounts in their behavior graph.

## Available Commands

- [accept-invitation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/accept-invitation.html)
- [batch-get-graph-member-datasources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/batch-get-graph-member-datasources.html)
- [batch-get-membership-datasources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/batch-get-membership-datasources.html)
- [create-graph](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/create-graph.html)
- [create-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/create-members.html)
- [delete-graph](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/delete-graph.html)
- [delete-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/delete-members.html)
- [describe-organization-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/describe-organization-configuration.html)
- [disable-organization-admin-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/disable-organization-admin-account.html)
- [disassociate-membership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/disassociate-membership.html)
- [enable-organization-admin-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/enable-organization-admin-account.html)
- [get-investigation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/get-investigation.html)
- [get-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/get-members.html)
- [list-datasource-packages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-datasource-packages.html)
- [list-graphs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-graphs.html)
- [list-indicators](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-indicators.html)
- [list-investigations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-investigations.html)
- [list-invitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-invitations.html)
- [list-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-members.html)
- [list-organization-admin-accounts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-organization-admin-accounts.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-tags-for-resource.html)
- [reject-invitation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/reject-invitation.html)
- [start-investigation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/start-investigation.html)
- [start-monitoring-member](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/start-monitoring-member.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/untag-resource.html)
- [update-datasource-packages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/update-datasource-packages.html)
- [update-investigation-state](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/update-investigation-state.html)
- [update-organization-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/update-organization-configuration.html)