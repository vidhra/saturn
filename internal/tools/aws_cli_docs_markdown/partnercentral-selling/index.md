# partnercentral-sellingÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# partnercentral-selling

## Description

**AWS Partner Central API for Selling Reference Guide**

This Amazon Web Services (AWS) Partner Central API reference is designed to help [AWS Partners](http://aws.amazon.com/partners/programs/) integrate Customer Relationship Management (CRM) systems with AWS Partner Central. Partners can automate interactions with AWS Partner Central, which helps to ensure effective engagements in joint business activities.

The API provides standard AWS API functionality. Access it by either using API [Actions](https://docs.aws.amazon.com/partner-central/latest/selling-api/API_Operations.html) or by using an AWS SDK thatâs tailored to your programming language or platform. For more information, see [Getting Started with AWS](http://aws.amazon.com/getting-started) and [Tools to Build on AWS](http://aws.amazon.com/developer/tools/) .

**Features offered by AWS Partner Central API**

- **Opportunity management:** Manages coselling opportunities through API actions such as `CreateOpportunity` , `UpdateOpportunity` , `ListOpportunities` , `GetOpportunity` , and `AssignOpportunity` .
- **AWS referral management:** Manages referrals shared by AWS using actions such as `ListEngagementInvitations` , `GetEngagementInvitation` , `StartEngagementByAcceptingInvitation` , and `RejectEngagementInvitation` .
- **Entity association:** Associates related entities such as *AWS Products* , *Partner Solutions* , and *AWS Marketplace Private Offers* with opportunities using the actions `AssociateOpportunity` , and `DisassociateOpportunity` .
- **View AWS opportunity details:** Retrieves real-time summaries of AWS opportunities using the `GetAWSOpportunitySummary` action.
- **List solutions:** Provides list APIs for listing partner offers using `ListSolutions` .
- **Event subscription:** Subscribe to real-time opportunity updates through AWS EventBridge by using actions such as *Opportunity Created* , *Opportunity Updated* , *Engagement Invitation Accepted* , *Engagement Invitation Rejected* , and *Engagement Invitation Created* .

## Available Commands

- [accept-engagement-invitation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/accept-engagement-invitation.html)
- [assign-opportunity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/assign-opportunity.html)
- [associate-opportunity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/associate-opportunity.html)
- [create-engagement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/create-engagement.html)
- [create-engagement-invitation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/create-engagement-invitation.html)
- [create-opportunity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/create-opportunity.html)
- [create-resource-snapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/create-resource-snapshot.html)
- [create-resource-snapshot-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/create-resource-snapshot-job.html)
- [delete-resource-snapshot-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/delete-resource-snapshot-job.html)
- [disassociate-opportunity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/disassociate-opportunity.html)
- [get-aws-opportunity-summary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/get-aws-opportunity-summary.html)
- [get-engagement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/get-engagement.html)
- [get-engagement-invitation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/get-engagement-invitation.html)
- [get-opportunity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/get-opportunity.html)
- [get-resource-snapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/get-resource-snapshot.html)
- [get-resource-snapshot-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/get-resource-snapshot-job.html)
- [get-selling-system-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/get-selling-system-settings.html)
- [list-engagement-by-accepting-invitation-tasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/list-engagement-by-accepting-invitation-tasks.html)
- [list-engagement-from-opportunity-tasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/list-engagement-from-opportunity-tasks.html)
- [list-engagement-invitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/list-engagement-invitations.html)
- [list-engagement-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/list-engagement-members.html)
- [list-engagement-resource-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/list-engagement-resource-associations.html)
- [list-engagements](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/list-engagements.html)
- [list-opportunities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/list-opportunities.html)
- [list-resource-snapshot-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/list-resource-snapshot-jobs.html)
- [list-resource-snapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/list-resource-snapshots.html)
- [list-solutions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/list-solutions.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/list-tags-for-resource.html)
- [put-selling-system-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/put-selling-system-settings.html)
- [reject-engagement-invitation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/reject-engagement-invitation.html)
- [start-engagement-by-accepting-invitation-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/start-engagement-by-accepting-invitation-task.html)
- [start-engagement-from-opportunity-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/start-engagement-from-opportunity-task.html)
- [start-resource-snapshot-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/start-resource-snapshot-job.html)
- [stop-resource-snapshot-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/stop-resource-snapshot-job.html)
- [submit-opportunity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/submit-opportunity.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/untag-resource.html)
- [update-opportunity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/update-opportunity.html)