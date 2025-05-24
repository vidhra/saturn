# workmailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# workmail

## Description

WorkMail is a secure, managed business email and calendaring service with support for existing desktop and mobile email clients. You can access your email, contacts, and calendars using Microsoft Outlook, your browser, or other native iOS and Android email applications. You can integrate WorkMail with your existing corporate directory and control both the keys that encrypt your data and the location in which your data is stored.

The WorkMail API is designed for the following scenarios:

- Listing and describing organizations
- Managing users
- Managing groups
- Managing resources

All WorkMail API operations are Amazon-authenticated and certificate-signed. They not only require the use of the AWS SDK, but also allow for the exclusive use of AWS Identity and Access Management users and roles to help facilitate access, trust, and permission policies. By creating a role and allowing an IAM user to access the WorkMail site, the IAM user gains full administrative visibility into the entire WorkMail organization (or as set in the IAM policy). This includes, but is not limited to, the ability to create, update, and delete users, groups, and resources. This allows developers to perform the scenarios listed above, as well as give users the ability to grant access on a selective basis using the IAM model.

## Available Commands

- [associate-delegate-to-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/associate-delegate-to-resource.html)
- [associate-member-to-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/associate-member-to-group.html)
- [assume-impersonation-role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/assume-impersonation-role.html)
- [cancel-mailbox-export-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/cancel-mailbox-export-job.html)
- [create-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-alias.html)
- [create-availability-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-availability-configuration.html)
- [create-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-group.html)
- [create-identity-center-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-identity-center-application.html)
- [create-impersonation-role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-impersonation-role.html)
- [create-mobile-device-access-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-mobile-device-access-rule.html)
- [create-organization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-organization.html)
- [create-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-resource.html)
- [create-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-user.html)
- [delete-access-control-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-access-control-rule.html)
- [delete-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-alias.html)
- [delete-availability-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-availability-configuration.html)
- [delete-email-monitoring-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-email-monitoring-configuration.html)
- [delete-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-group.html)
- [delete-identity-center-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-identity-center-application.html)
- [delete-identity-provider-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-identity-provider-configuration.html)
- [delete-impersonation-role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-impersonation-role.html)
- [delete-mailbox-permissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-mailbox-permissions.html)
- [delete-mobile-device-access-override](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-mobile-device-access-override.html)
- [delete-mobile-device-access-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-mobile-device-access-rule.html)
- [delete-organization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-organization.html)
- [delete-personal-access-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-personal-access-token.html)
- [delete-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-resource.html)
- [delete-retention-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-retention-policy.html)
- [delete-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-user.html)
- [deregister-from-work-mail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/deregister-from-work-mail.html)
- [deregister-mail-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/deregister-mail-domain.html)
- [describe-email-monitoring-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-email-monitoring-configuration.html)
- [describe-entity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-entity.html)
- [describe-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-group.html)
- [describe-identity-provider-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-identity-provider-configuration.html)
- [describe-inbound-dmarc-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-inbound-dmarc-settings.html)
- [describe-mailbox-export-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-mailbox-export-job.html)
- [describe-organization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-organization.html)
- [describe-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-resource.html)
- [describe-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-user.html)
- [disassociate-delegate-from-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/disassociate-delegate-from-resource.html)
- [disassociate-member-from-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/disassociate-member-from-group.html)
- [get-access-control-effect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/get-access-control-effect.html)
- [get-default-retention-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/get-default-retention-policy.html)
- [get-impersonation-role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/get-impersonation-role.html)
- [get-impersonation-role-effect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/get-impersonation-role-effect.html)
- [get-mail-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/get-mail-domain.html)
- [get-mailbox-details](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/get-mailbox-details.html)
- [get-mobile-device-access-effect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/get-mobile-device-access-effect.html)
- [get-mobile-device-access-override](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/get-mobile-device-access-override.html)
- [get-personal-access-token-metadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/get-personal-access-token-metadata.html)
- [list-access-control-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-access-control-rules.html)
- [list-aliases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-aliases.html)
- [list-availability-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-availability-configurations.html)
- [list-group-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-group-members.html)
- [list-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-groups.html)
- [list-groups-for-entity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-groups-for-entity.html)
- [list-impersonation-roles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-impersonation-roles.html)
- [list-mail-domains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-mail-domains.html)
- [list-mailbox-export-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-mailbox-export-jobs.html)
- [list-mailbox-permissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-mailbox-permissions.html)
- [list-mobile-device-access-overrides](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-mobile-device-access-overrides.html)
- [list-mobile-device-access-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-mobile-device-access-rules.html)
- [list-organizations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-organizations.html)
- [list-personal-access-tokens](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-personal-access-tokens.html)
- [list-resource-delegates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-resource-delegates.html)
- [list-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-resources.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-tags-for-resource.html)
- [list-users](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-users.html)
- [put-access-control-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/put-access-control-rule.html)
- [put-email-monitoring-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/put-email-monitoring-configuration.html)
- [put-identity-provider-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/put-identity-provider-configuration.html)
- [put-inbound-dmarc-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/put-inbound-dmarc-settings.html)
- [put-mailbox-permissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/put-mailbox-permissions.html)
- [put-mobile-device-access-override](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/put-mobile-device-access-override.html)
- [put-retention-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/put-retention-policy.html)
- [register-mail-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/register-mail-domain.html)
- [register-to-work-mail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/register-to-work-mail.html)
- [reset-password](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/reset-password.html)
- [start-mailbox-export-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/start-mailbox-export-job.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/tag-resource.html)
- [test-availability-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/test-availability-configuration.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/untag-resource.html)
- [update-availability-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-availability-configuration.html)
- [update-default-mail-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-default-mail-domain.html)
- [update-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-group.html)
- [update-impersonation-role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-impersonation-role.html)
- [update-mailbox-quota](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-mailbox-quota.html)
- [update-mobile-device-access-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-mobile-device-access-rule.html)
- [update-primary-email-address](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-primary-email-address.html)
- [update-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-resource.html)
- [update-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-user.html)