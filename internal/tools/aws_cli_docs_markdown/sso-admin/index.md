# sso-adminÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# sso-admin

## Description

IAM Identity Center is the Amazon Web Services solution for connecting your workforce users to Amazon Web Services managed applications and other Amazon Web Services resources. You can connect your existing identity provider and synchronize users and groups from your directory, or create and manage your users directly in IAM Identity Center. You can then use IAM Identity Center for either or both of the following:

- User access to applications
- User access to Amazon Web Services accounts

This guide provides information about single sign-on operations that you can use for access to applications and Amazon Web Services accounts. For information about IAM Identity Center features, see the [IAM Identity Center User Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) .

### Note

IAM Identity Center uses the `sso` and `identitystore` API namespaces.

Many API operations for IAM Identity Center rely on identifiers for users and groups, known as principals. For more information about how to work with principals and principal IDs in IAM Identity Center, see the [Identity Store API Reference](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html) .

### Note

Amazon Web Services provides SDKs that consist of libraries and sample code for various programming languages and platforms (Java, Ruby, .Net, iOS, Android, and more). The SDKs provide a convenient way to create programmatic access to IAM Identity Center and other Amazon Web Services services. For more information about the Amazon Web Services SDKs, including how to download and install them, see [Tools for Amazon Web Services](http://aws.amazon.com/tools/) .

## Available Commands

- [attach-customer-managed-policy-reference-to-permission-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/attach-customer-managed-policy-reference-to-permission-set.html)
- [attach-managed-policy-to-permission-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/attach-managed-policy-to-permission-set.html)
- [create-account-assignment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-account-assignment.html)
- [create-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-application.html)
- [create-application-assignment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-application-assignment.html)
- [create-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-instance.html)
- [create-instance-access-control-attribute-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-instance-access-control-attribute-configuration.html)
- [create-permission-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-permission-set.html)
- [create-trusted-token-issuer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-trusted-token-issuer.html)
- [delete-account-assignment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-account-assignment.html)
- [delete-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-application.html)
- [delete-application-access-scope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-application-access-scope.html)
- [delete-application-assignment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-application-assignment.html)
- [delete-application-authentication-method](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-application-authentication-method.html)
- [delete-application-grant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-application-grant.html)
- [delete-inline-policy-from-permission-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-inline-policy-from-permission-set.html)
- [delete-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-instance.html)
- [delete-instance-access-control-attribute-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-instance-access-control-attribute-configuration.html)
- [delete-permission-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-permission-set.html)
- [delete-permissions-boundary-from-permission-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-permissions-boundary-from-permission-set.html)
- [delete-trusted-token-issuer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-trusted-token-issuer.html)
- [describe-account-assignment-creation-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/describe-account-assignment-creation-status.html)
- [describe-account-assignment-deletion-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/describe-account-assignment-deletion-status.html)
- [describe-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/describe-application.html)
- [describe-application-assignment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/describe-application-assignment.html)
- [describe-application-provider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/describe-application-provider.html)
- [describe-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/describe-instance.html)
- [describe-instance-access-control-attribute-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/describe-instance-access-control-attribute-configuration.html)
- [describe-permission-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/describe-permission-set.html)
- [describe-permission-set-provisioning-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/describe-permission-set-provisioning-status.html)
- [describe-trusted-token-issuer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/describe-trusted-token-issuer.html)
- [detach-customer-managed-policy-reference-from-permission-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/detach-customer-managed-policy-reference-from-permission-set.html)
- [detach-managed-policy-from-permission-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/detach-managed-policy-from-permission-set.html)
- [get-application-access-scope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/get-application-access-scope.html)
- [get-application-assignment-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/get-application-assignment-configuration.html)
- [get-application-authentication-method](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/get-application-authentication-method.html)
- [get-application-grant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/get-application-grant.html)
- [get-inline-policy-for-permission-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/get-inline-policy-for-permission-set.html)
- [get-permissions-boundary-for-permission-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/get-permissions-boundary-for-permission-set.html)
- [list-account-assignment-creation-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-account-assignment-creation-status.html)
- [list-account-assignment-deletion-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-account-assignment-deletion-status.html)
- [list-account-assignments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-account-assignments.html)
- [list-account-assignments-for-principal](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-account-assignments-for-principal.html)
- [list-accounts-for-provisioned-permission-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-accounts-for-provisioned-permission-set.html)
- [list-application-access-scopes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-application-access-scopes.html)
- [list-application-assignments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-application-assignments.html)
- [list-application-assignments-for-principal](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-application-assignments-for-principal.html)
- [list-application-authentication-methods](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-application-authentication-methods.html)
- [list-application-grants](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-application-grants.html)
- [list-application-providers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-application-providers.html)
- [list-applications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-applications.html)
- [list-customer-managed-policy-references-in-permission-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-customer-managed-policy-references-in-permission-set.html)
- [list-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-instances.html)
- [list-managed-policies-in-permission-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-managed-policies-in-permission-set.html)
- [list-permission-set-provisioning-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-permission-set-provisioning-status.html)
- [list-permission-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-permission-sets.html)
- [list-permission-sets-provisioned-to-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-permission-sets-provisioned-to-account.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-tags-for-resource.html)
- [list-trusted-token-issuers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-trusted-token-issuers.html)
- [provision-permission-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/provision-permission-set.html)
- [put-application-access-scope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/put-application-access-scope.html)
- [put-application-assignment-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/put-application-assignment-configuration.html)
- [put-application-authentication-method](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/put-application-authentication-method.html)
- [put-application-grant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/put-application-grant.html)
- [put-inline-policy-to-permission-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/put-inline-policy-to-permission-set.html)
- [put-permissions-boundary-to-permission-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/put-permissions-boundary-to-permission-set.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/untag-resource.html)
- [update-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/update-application.html)
- [update-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/update-instance.html)
- [update-instance-access-control-attribute-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/update-instance-access-control-attribute-configuration.html)
- [update-permission-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/update-permission-set.html)
- [update-trusted-token-issuer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/update-trusted-token-issuer.html)