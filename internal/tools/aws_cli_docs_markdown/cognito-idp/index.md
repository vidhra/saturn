# cognito-idpÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# cognito-idp

## Description

With the Amazon Cognito user pools API, you can configure user pools and authenticate users. To authenticate users from third-party identity providers (IdPs) in this API, you can [link IdP users to native user profiles](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation-consolidate-users.html) . Learn more about the authentication and authorization of federated users at [Adding user pool sign-in through a third party](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation.html) and in the [User pool federation endpoints and managed login reference](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-userpools-server-contract-reference.html) .

This API reference provides detailed information about API operations and object types in Amazon Cognito.

Along with resource management operations, the Amazon Cognito user pools API includes classes of operations and authorization models for client-side and server-side authentication of users. You can interact with operations in the Amazon Cognito user pools API as any of the following subjects.

- An administrator who wants to configure user pools, app clients, users, groups, or other user pool functions.
- A server-side app, like a web application, that wants to use its Amazon Web Services privileges to manage, authenticate, or authorize a user.
- A client-side app, like a mobile app, that wants to make unauthenticated requests to manage, authenticate, or authorize a user.

For more information, see [Understanding API, OIDC, and managed login pages authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-public-server-side.html#user-pools-API-operations) in the *Amazon Cognito Developer Guide* .

With your Amazon Web Services SDK, you can build the logic to support operational flows in every use case for this API. You can also make direct REST API requests to [Amazon Cognito user pools service endpoints](https://docs.aws.amazon.com/general/latest/gr/cognito_identity.html#cognito_identity_your_user_pools_region) . The following links can get you started with the `CognitoIdentityProvider` client in supported Amazon Web Services SDKs.

To get started with an Amazon Web Services SDK, see [Tools to Build on Amazon Web Services](http://aws.amazon.com/developer/tools/) . For example actions and scenarios, see [Code examples for Amazon Cognito Identity Provider using Amazon Web Services SDKs](https://docs.aws.amazon.com/cognito/latest/developerguide/service_code_examples_cognito-identity-provider.html) .

## Available Commands

- [add-custom-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/add-custom-attributes.html)
- [admin-add-user-to-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-add-user-to-group.html)
- [admin-confirm-sign-up](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-confirm-sign-up.html)
- [admin-create-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-create-user.html)
- [admin-delete-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-delete-user.html)
- [admin-delete-user-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-delete-user-attributes.html)
- [admin-disable-provider-for-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-disable-provider-for-user.html)
- [admin-disable-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-disable-user.html)
- [admin-enable-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-enable-user.html)
- [admin-forget-device](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-forget-device.html)
- [admin-get-device](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-get-device.html)
- [admin-get-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-get-user.html)
- [admin-initiate-auth](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-initiate-auth.html)
- [admin-link-provider-for-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-link-provider-for-user.html)
- [admin-list-devices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-list-devices.html)
- [admin-list-groups-for-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-list-groups-for-user.html)
- [admin-list-user-auth-events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-list-user-auth-events.html)
- [admin-remove-user-from-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-remove-user-from-group.html)
- [admin-reset-user-password](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-reset-user-password.html)
- [admin-respond-to-auth-challenge](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-respond-to-auth-challenge.html)
- [admin-set-user-mfa-preference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-set-user-mfa-preference.html)
- [admin-set-user-password](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-set-user-password.html)
- [admin-set-user-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-set-user-settings.html)
- [admin-update-auth-event-feedback](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-update-auth-event-feedback.html)
- [admin-update-device-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-update-device-status.html)
- [admin-update-user-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-update-user-attributes.html)
- [admin-user-global-sign-out](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-user-global-sign-out.html)
- [associate-software-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/associate-software-token.html)
- [change-password](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/change-password.html)
- [complete-web-authn-registration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/complete-web-authn-registration.html)
- [confirm-device](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/confirm-device.html)
- [confirm-forgot-password](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/confirm-forgot-password.html)
- [confirm-sign-up](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/confirm-sign-up.html)
- [create-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-group.html)
- [create-identity-provider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-identity-provider.html)
- [create-managed-login-branding](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-managed-login-branding.html)
- [create-resource-server](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-resource-server.html)
- [create-user-import-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-import-job.html)
- [create-user-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-pool.html)
- [create-user-pool-client](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-pool-client.html)
- [create-user-pool-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-pool-domain.html)
- [delete-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-group.html)
- [delete-identity-provider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-identity-provider.html)
- [delete-managed-login-branding](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-managed-login-branding.html)
- [delete-resource-server](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-resource-server.html)
- [delete-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user.html)
- [delete-user-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user-attributes.html)
- [delete-user-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user-pool.html)
- [delete-user-pool-client](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user-pool-client.html)
- [delete-user-pool-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user-pool-domain.html)
- [delete-web-authn-credential](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-web-authn-credential.html)
- [describe-identity-provider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-identity-provider.html)
- [describe-managed-login-branding](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-managed-login-branding.html)
- [describe-managed-login-branding-by-client](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-managed-login-branding-by-client.html)
- [describe-resource-server](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-resource-server.html)
- [describe-risk-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-risk-configuration.html)
- [describe-user-import-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-user-import-job.html)
- [describe-user-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-user-pool.html)
- [describe-user-pool-client](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-user-pool-client.html)
- [describe-user-pool-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-user-pool-domain.html)
- [forget-device](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/forget-device.html)
- [forgot-password](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/forgot-password.html)
- [get-csv-header](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-csv-header.html)
- [get-device](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-device.html)
- [get-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-group.html)
- [get-identity-provider-by-identifier](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-identity-provider-by-identifier.html)
- [get-log-delivery-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-log-delivery-configuration.html)
- [get-signing-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-signing-certificate.html)
- [get-tokens-from-refresh-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-tokens-from-refresh-token.html)
- [get-ui-customization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-ui-customization.html)
- [get-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-user.html)
- [get-user-attribute-verification-code](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-user-attribute-verification-code.html)
- [get-user-auth-factors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-user-auth-factors.html)
- [get-user-pool-mfa-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-user-pool-mfa-config.html)
- [global-sign-out](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/global-sign-out.html)
- [initiate-auth](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/initiate-auth.html)
- [list-devices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-devices.html)
- [list-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-groups.html)
- [list-identity-providers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-identity-providers.html)
- [list-resource-servers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-resource-servers.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-tags-for-resource.html)
- [list-user-import-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-user-import-jobs.html)
- [list-user-pool-clients](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-user-pool-clients.html)
- [list-user-pools](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-user-pools.html)
- [list-users](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-users.html)
- [list-users-in-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-users-in-group.html)
- [list-web-authn-credentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-web-authn-credentials.html)
- [resend-confirmation-code](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/resend-confirmation-code.html)
- [respond-to-auth-challenge](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/respond-to-auth-challenge.html)
- [revoke-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/revoke-token.html)
- [set-log-delivery-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/set-log-delivery-configuration.html)
- [set-risk-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/set-risk-configuration.html)
- [set-ui-customization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/set-ui-customization.html)
- [set-user-mfa-preference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/set-user-mfa-preference.html)
- [set-user-pool-mfa-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/set-user-pool-mfa-config.html)
- [set-user-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/set-user-settings.html)
- [sign-up](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/sign-up.html)
- [start-user-import-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/start-user-import-job.html)
- [start-web-authn-registration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/start-web-authn-registration.html)
- [stop-user-import-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/stop-user-import-job.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/untag-resource.html)
- [update-auth-event-feedback](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-auth-event-feedback.html)
- [update-device-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-device-status.html)
- [update-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-group.html)
- [update-identity-provider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-identity-provider.html)
- [update-managed-login-branding](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-managed-login-branding.html)
- [update-resource-server](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-resource-server.html)
- [update-user-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-attributes.html)
- [update-user-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-pool.html)
- [update-user-pool-client](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-pool-client.html)
- [update-user-pool-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-pool-domain.html)
- [verify-software-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/verify-software-token.html)
- [verify-user-attribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/verify-user-attribute.html)