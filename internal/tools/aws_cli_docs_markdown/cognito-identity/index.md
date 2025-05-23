# cognito-identityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# cognito-identity

## Description

Amazon Cognito Federated Identities is a web service that delivers scoped temporary credentials to mobile devices and other untrusted environments. It uniquely identifies a device and supplies the user with a consistent identity over the lifetime of an application.

Using Amazon Cognito Federated Identities, you can enable authentication with one or more third-party identity providers (Facebook, Google, or Login with Amazon) or an Amazon Cognito user pool, and you can also choose to support unauthenticated access from your app. Cognito delivers a unique identifier for each user and acts as an OpenID token provider trusted by Security Token Service (STS) to access temporary, limited-privilege Amazon Web Services credentials.

For a description of the authentication flow from the Amazon Cognito Developer Guide see [Authentication Flow](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html) .

For more information see [Amazon Cognito Federated Identities](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html) .

## Available Commands

- [create-identity-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/create-identity-pool.html)
- [delete-identities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/delete-identities.html)
- [delete-identity-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/delete-identity-pool.html)
- [describe-identity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/describe-identity.html)
- [describe-identity-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/describe-identity-pool.html)
- [get-credentials-for-identity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/get-credentials-for-identity.html)
- [get-id](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/get-id.html)
- [get-identity-pool-roles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/get-identity-pool-roles.html)
- [get-open-id-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/get-open-id-token.html)
- [get-open-id-token-for-developer-identity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/get-open-id-token-for-developer-identity.html)
- [get-principal-tag-attribute-map](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/get-principal-tag-attribute-map.html)
- [list-identities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/list-identities.html)
- [list-identity-pools](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/list-identity-pools.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/list-tags-for-resource.html)
- [lookup-developer-identity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/lookup-developer-identity.html)
- [merge-developer-identities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/merge-developer-identities.html)
- [set-identity-pool-roles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/set-identity-pool-roles.html)
- [set-principal-tag-attribute-map](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/set-principal-tag-attribute-map.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/tag-resource.html)
- [unlink-developer-identity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/unlink-developer-identity.html)
- [unlink-identity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/unlink-identity.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/untag-resource.html)
- [update-identity-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/update-identity-pool.html)