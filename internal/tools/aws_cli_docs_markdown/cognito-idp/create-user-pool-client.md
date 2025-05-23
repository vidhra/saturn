# create-user-pool-clientÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-pool-client.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-pool-client.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cognito-idp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html#cli-aws-cognito-idp) ]

# create-user-pool-client

## Description

Creates an app client in a user pool. This operation sets basic and advanced configuration options.

Unlike app clients created in the console, Amazon Cognito doesnât automatically assign a branding style to app clients that you configure with this API operation. Managed login and classic hosted UI pages arenât available for your client until after you apply a branding style.

### Warning

If you donât provide a value for an attribute, Amazon Cognito sets it to its default value.

### Note

Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.

**Learn more**

- [Signing Amazon Web Services API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
- [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/CreateUserPoolClient)

## Synopsis

```
create-user-pool-client
--user-pool-id <value>
--client-name <value>
[--generate-secret | --no-generate-secret]
[--refresh-token-validity <value>]
[--access-token-validity <value>]
[--id-token-validity <value>]
[--token-validity-units <value>]
[--read-attributes <value>]
[--write-attributes <value>]
[--explicit-auth-flows <value>]
[--supported-identity-providers <value>]
[--callback-urls <value>]
[--logout-urls <value>]
[--default-redirect-uri <value>]
[--allowed-o-auth-flows <value>]
[--allowed-o-auth-scopes <value>]
[--allowed-o-auth-flows-user-pool-client | --no-allowed-o-auth-flows-user-pool-client]
[--analytics-configuration <value>]
[--prevent-user-existence-errors <value>]
[--enable-token-revocation | --no-enable-token-revocation]
[--enable-propagate-additional-user-context-data | --no-enable-propagate-additional-user-context-data]
[--auth-session-validity <value>]
[--refresh-token-rotation <value>]
[--cli-input-json | --cli-input-yaml]
[--generate-cli-skeleton <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--user-pool-id` (string)

The ID of the user pool where you want to create an app client.

`--client-name` (string)

A friendly name for the app client that you want to create.

`--generate-secret` | `--no-generate-secret` (boolean)

When `true` , generates a client secret for the app client. Client secrets are used with server-side and machine-to-machine applications. Client secrets are automatically generated; you canât specify a secret value. For more information, see [App client types](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html#user-pool-settings-client-app-client-types) .

`--refresh-token-validity` (integer)

The refresh token time limit. After this limit expires, your user canât use their refresh token. To specify the time unit for `RefreshTokenValidity` as `seconds` , `minutes` , `hours` , or `days` , set a `TokenValidityUnits` value in your API request.

For example, when you set `RefreshTokenValidity` as `10` and `TokenValidityUnits` as `days` , your user can refresh their session and retrieve new access and ID tokens for 10 days.

The default time unit for `RefreshTokenValidity` in an API request is days. You canât set `RefreshTokenValidity` to 0. If you do, Amazon Cognito overrides the value with the default value of 30 days. *Valid range* is displayed below in seconds.

If you donât specify otherwise in the configuration of your app client, your refresh tokens are valid for 30 days.

`--access-token-validity` (integer)

The access token time limit. After this limit expires, your user canât use their access token. To specify the time unit for `AccessTokenValidity` as `seconds` , `minutes` , `hours` , or `days` , set a `TokenValidityUnits` value in your API request.

For example, when you set `AccessTokenValidity` to `10` and `TokenValidityUnits` to `hours` , your user can authorize access with their access token for 10 hours.

The default time unit for `AccessTokenValidity` in an API request is hours. *Valid range* is displayed below in seconds.

If you donât specify otherwise in the configuration of your app client, your access tokens are valid for one hour.

`--id-token-validity` (integer)

The ID token time limit. After this limit expires, your user canât use their ID token. To specify the time unit for `IdTokenValidity` as `seconds` , `minutes` , `hours` , or `days` , set a `TokenValidityUnits` value in your API request.

For example, when you set `IdTokenValidity` as `10` and `TokenValidityUnits` as `hours` , your user can authenticate their session with their ID token for 10 hours.

The default time unit for `IdTokenValidity` in an API request is hours. *Valid range* is displayed below in seconds.

If you donât specify otherwise in the configuration of your app client, your ID tokens are valid for one hour.

`--token-validity-units` (structure)

The units that validity times are represented in. The default unit for refresh tokens is days, and the default for ID and access tokens are hours.

AccessToken -> (string)

A time unit for the value that you set in the `AccessTokenValidity` parameter. The default `AccessTokenValidity` time unit is `hours` . `AccessTokenValidity` duration can range from five minutes to one day.

IdToken -> (string)

A time unit for the value that you set in the `IdTokenValidity` parameter. The default `IdTokenValidity` time unit is `hours` . `IdTokenValidity` duration can range from five minutes to one day.

RefreshToken -> (string)

A time unit for the value that you set in the `RefreshTokenValidity` parameter. The default `RefreshTokenValidity` time unit is `days` . `RefreshTokenValidity` duration can range from 60 minutes to 10 years.

Shorthand Syntax:

```
AccessToken=string,IdToken=string,RefreshToken=string
```

JSON Syntax:

```
{
  "AccessToken": "seconds"|"minutes"|"hours"|"days",
  "IdToken": "seconds"|"minutes"|"hours"|"days",
  "RefreshToken": "seconds"|"minutes"|"hours"|"days"
}
```

`--read-attributes` (list)

The list of user attributes that you want your app client to have read access to. After your user authenticates in your app, their access token authorizes them to read their own attribute value for any attribute in this list.

When you donât specify the `ReadAttributes` for your app client, your app can read the values of `email_verified` , `phone_number_verified` , and the standard attributes of your user pool. When your user pool app client has read access to these default attributes, `ReadAttributes` doesnât return any information. Amazon Cognito only populates `ReadAttributes` in the API response if you have specified your own custom set of read attributes.

(string)

Syntax:

```
"string" "string" ...
```

`--write-attributes` (list)

The list of user attributes that you want your app client to have write access to. After your user authenticates in your app, their access token authorizes them to set or modify their own attribute value for any attribute in this list.

When you donât specify the `WriteAttributes` for your app client, your app can write the values of the Standard attributes of your user pool. When your user pool has write access to these default attributes, `WriteAttributes` doesnât return any information. Amazon Cognito only populates `WriteAttributes` in the API response if you have specified your own custom set of write attributes.

If your app client allows users to sign in through an IdP, this array must include all attributes that you have mapped to IdP attributes. Amazon Cognito updates mapped attributes when users sign in to your application through an IdP. If your app client does not have write access to a mapped attribute, Amazon Cognito throws an error when it tries to update the attribute. For more information, see [Specifying IdP Attribute Mappings for Your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html) .

(string)

Syntax:

```
"string" "string" ...
```

`--explicit-auth-flows` (list)

The [authentication flows](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow-methods.html) that you want your user pool client to support. For each app client in your user pool, you can sign in your users with any combination of one or more flows, including with a user name and Secure Remote Password (SRP), a user name and password, or a custom authentication process that you define with Lambda functions.

### Note

If you donât specify a value for `ExplicitAuthFlows` , your app client supports `ALLOW_REFRESH_TOKEN_AUTH` , `ALLOW_USER_SRP_AUTH` , and `ALLOW_CUSTOM_AUTH` .

The values for authentication flow options include the following.

- `ALLOW_USER_AUTH` : Enable selection-based sign-in with `USER_AUTH` . This setting covers username-password, secure remote password (SRP), passwordless, and passkey authentication. This authentiation flow can do username-password and SRP authentication without other `ExplicitAuthFlows` permitting them. For example users can complete an SRP challenge through `USER_AUTH` without the flow `USER_SRP_AUTH` being active for the app client. This flow doesnât include `CUSTOM_AUTH` .  To activate this setting, your user pool must be in the [Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.
- `ALLOW_ADMIN_USER_PASSWORD_AUTH` : Enable admin based user password authentication flow `ADMIN_USER_PASSWORD_AUTH` . This setting replaces the `ADMIN_NO_SRP_AUTH` setting. With this authentication flow, your app passes a user name and password to Amazon Cognito in the request, instead of using the Secure Remote Password (SRP) protocol to securely transmit the password.
- `ALLOW_CUSTOM_AUTH` : Enable Lambda trigger based authentication.
- `ALLOW_USER_PASSWORD_AUTH` : Enable user password-based authentication. In this flow, Amazon Cognito receives the password in the request instead of using the SRP protocol to verify passwords.
- `ALLOW_USER_SRP_AUTH` : Enable SRP-based authentication.
- `ALLOW_REFRESH_TOKEN_AUTH` : Enable authflow to refresh tokens.

In some environments, you will see the values `ADMIN_NO_SRP_AUTH` , `CUSTOM_AUTH_FLOW_ONLY` , or `USER_PASSWORD_AUTH` . You canât assign these legacy `ExplicitAuthFlows` values to user pool clients at the same time as values that begin with `ALLOW_` , like `ALLOW_USER_SRP_AUTH` .

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  ADMIN_NO_SRP_AUTH
  CUSTOM_AUTH_FLOW_ONLY
  USER_PASSWORD_AUTH
  ALLOW_ADMIN_USER_PASSWORD_AUTH
  ALLOW_CUSTOM_AUTH
  ALLOW_USER_PASSWORD_AUTH
  ALLOW_USER_SRP_AUTH
  ALLOW_REFRESH_TOKEN_AUTH
  ALLOW_USER_AUTH
```

`--supported-identity-providers` (list)

A list of provider names for the identity providers (IdPs) that are supported on this client. The following are supported: `COGNITO` , `Facebook` , `Google` , `SignInWithApple` , and `LoginWithAmazon` . You can also specify the names that you configured for the SAML and OIDC IdPs in your user pool, for example `MySAMLIdP` or `MyOIDCIdP` .

This parameter sets the IdPs that [managed login](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html) will display on the login page for your app client. The removal of `COGNITO` from this list doesnât prevent authentication operations for local users with the user pools API in an Amazon Web Services SDK. The only way to prevent SDK-based authentication is to block access with a [WAF rule](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-waf.html) .

(string)

Syntax:

```
"string" "string" ...
```

`--callback-urls` (list)

A list of allowed redirect, or callback, URLs for managed login authentication. These URLs are the paths where you want to send your usersâ browsers after they complete authentication with managed login or a third-party IdP. Typically, callback URLs are the home of an application that uses OAuth or OIDC libraries to process authentication outcomes.

A redirect URI must meet the following requirements:

- Be an absolute URI.
- Be registered with the authorization server. Amazon Cognito doesnât accept authorization requests with `redirect_uri` values that arenât in the list of `CallbackURLs` that you provide in this parameter.
- Not include a fragment component.

See [OAuth 2.0 - Redirection Endpoint](https://tools.ietf.org/html/rfc6749#section-3.1.2) .

Amazon Cognito requires HTTPS over HTTP except for [http://localhost](http://localhost) for testing purposes only.

App callback URLs such as myapp://example are also supported.

(string)

Syntax:

```
"string" "string" ...
```

`--logout-urls` (list)

A list of allowed logout URLs for managed login authentication. When you pass `logout_uri` and `client_id` parameters to `/logout` , Amazon Cognito signs out your user and redirects them to the logout URL. This parameter describes the URLs that you want to be the permitted targets of `logout_uri` . A typical use of these URLs is when a user selects âSign outâ and you redirect them to your public homepage. For more information, see [Logout endpoint](https://docs.aws.amazon.com/cognito/latest/developerguide/logout-endpoint.html) .

(string)

Syntax:

```
"string" "string" ...
```

`--default-redirect-uri` (string)

The default redirect URI. In app clients with one assigned IdP, replaces `redirect_uri` in authentication requests. Must be in the `CallbackURLs` list.

`--allowed-o-auth-flows` (list)

The OAuth grant types that you want your app client to generate for clients in managed login authentication. To create an app client that generates client credentials grants, you must add `client_credentials` as the only allowed OAuth flow.

code

Use a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the `/oauth2/token` endpoint.

implicit

Issue the access token, and the ID token when scopes like `openid` and `profile` are requested, directly to your user.

client_credentials

Issue the access token from the `/oauth2/token` endpoint directly to a non-person user, authorized by a combination of the client ID and client secret.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  code
  implicit
  client_credentials
```

`--allowed-o-auth-scopes` (list)

The OAuth, OpenID Connect (OIDC), and custom scopes that you want to permit your app client to authorize access with. Scopes govern access control to user pool self-service API operations, user data from the `userInfo` endpoint, and third-party APIs. Scope values include `phone` , `email` , `openid` , and `profile` . The `aws.cognito.signin.user.admin` scope authorizes user self-service operations. Custom scopes with resource servers authorize access to external APIs.

(string)

Syntax:

```
"string" "string" ...
```

`--allowed-o-auth-flows-user-pool-client` | `--no-allowed-o-auth-flows-user-pool-client` (boolean)

Set to `true` to use OAuth 2.0 authorization server features in your app client.

This parameter must have a value of `true` before you can configure the following features in your app client.

- `CallBackURLs` : Callback URLs.
- `LogoutURLs` : Sign-out redirect URLs.
- `AllowedOAuthScopes` : OAuth 2.0 scopes.
- `AllowedOAuthFlows` : Support for authorization code, implicit, and client credentials OAuth 2.0 grants.

To use authorization server features, configure one of these features in the Amazon Cognito console or set `AllowedOAuthFlowsUserPoolClient` to `true` in a `CreateUserPoolClient` or `UpdateUserPoolClient` API request. If you donât set a value for `AllowedOAuthFlowsUserPoolClient` in a request with the CLI or SDKs, it defaults to `false` . When `false` , only SDK-based API sign-in is permitted.

`--analytics-configuration` (structure)

The user pool analytics configuration for collecting metrics and sending them to your Amazon Pinpoint campaign.

In Amazon Web Services Regions where Amazon Pinpoint isnât available, user pools might not have access to analytics or might be configurable with campaigns in the US East (N. Virginia) Region. For more information, see [Using Amazon Pinpoint analytics](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-pinpoint-integration.html) .

ApplicationId -> (string)

Your Amazon Pinpoint project ID.

ApplicationArn -> (string)

The Amazon Resource Name (ARN) of an Amazon Pinpoint project that you want to connect to your user pool app client. Amazon Cognito publishes events to the Amazon Pinpoint project that `ApplicationArn` declares. You can also configure your application to pass an endpoint ID in the `AnalyticsMetadata` parameter of sign-in operations. The endpoint ID is information about the destination for push notifications

RoleArn -> (string)

The ARN of an Identity and Access Management role that has the permissions required for Amazon Cognito to publish events to Amazon Pinpoint analytics.

ExternalId -> (string)

The [external ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html) of the role that Amazon Cognito assumes to send analytics data to Amazon Pinpoint.

UserDataShared -> (boolean)

If `UserDataShared` is `true` , Amazon Cognito includes user data in the events that it publishes to Amazon Pinpoint analytics.

Shorthand Syntax:

```
ApplicationId=string,ApplicationArn=string,RoleArn=string,ExternalId=string,UserDataShared=boolean
```

JSON Syntax:

```
{
  "ApplicationId": "string",
  "ApplicationArn": "string",
  "RoleArn": "string",
  "ExternalId": "string",
  "UserDataShared": true|false
}
```

`--prevent-user-existence-errors` (string)

When `ENABLED` , suppresses messages that might indicate a valid user exists when someone attempts sign-in. This parameters sets your preference for the errors and responses that you want Amazon Cognito APIs to return during authentication, account confirmation, and password recovery when the user doesnât exist in the user pool. When set to `ENABLED` and the user doesnât exist, authentication returns an error indicating either the username or password was incorrect. Account confirmation and password recovery return a response indicating a code was sent to a simulated destination. When set to `LEGACY` , those APIs return a `UserNotFoundException` exception if the user doesnât exist in the user pool.

Defaults to `LEGACY` .

Possible values:

- `LEGACY`
- `ENABLED`

`--enable-token-revocation` | `--no-enable-token-revocation` (boolean)

Activates or deactivates [token revocation](https://docs.aws.amazon.com/cognito/latest/developerguide/token-revocation.html) in the target app client.

If you donât include this parameter, token revocation is automatically activated for the new user pool client.

`--enable-propagate-additional-user-context-data` | `--no-enable-propagate-additional-user-context-data` (boolean)

When `true` , your application can include additional `UserContextData` in authentication requests. This data includes the IP address, and contributes to analysis by threat protection features. For more information about propagation of user context data, see [Adding session data to API requests](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.html#user-pool-settings-adaptive-authentication-device-fingerprint) . If you donât include this parameter, you canât send the source IP address to Amazon Cognito threat protection features. You can only activate `EnablePropagateAdditionalUserContextData` in an app client that has a client secret.

`--auth-session-validity` (integer)

Amazon Cognito creates a session token for each API request in an authentication flow. `AuthSessionValidity` is the duration, in minutes, of that session token. Your user pool native user must respond to each authentication challenge before the session expires.

`--refresh-token-rotation` (structure)

The configuration of your app client for refresh token rotation. When enabled, your app client issues new ID, access, and refresh tokens when users renew their sessions with refresh tokens. When disabled, token refresh issues only ID and access tokens.

Feature -> (string)

The state of refresh token rotation for the current app client.

RetryGracePeriodSeconds -> (integer)

When you request a token refresh with `GetTokensFromRefreshToken` , the original refresh token that youâre rotating out can remain valid for a period of time of up to 60 seconds. This allows for client-side retries. When `RetryGracePeriodSeconds` is `0` , the grace period is disabled and a successful request immediately invalidates the submitted refresh token.

Shorthand Syntax:

```
Feature=string,RetryGracePeriodSeconds=integer
```

JSON Syntax:

```
{
  "Feature": "ENABLED"|"DISABLED",
  "RetryGracePeriodSeconds": integer
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a user pool client**

The following `create-user-pool-client` example creates a new user pool client with a client secret, explicit read and write attributes, sign in with username-password and SRP flows, sign-in with three IdPs, access to a subset of OAuth scopes, PinPoint analytics, and an extended authentication session validity.

```
aws cognito-idp create-user-pool-client \
    --user-pool-id us-west-2_EXAMPLE \
    --client-name MyTestClient \
    --generate-secret \
    --refresh-token-validity 10 \
    --access-token-validity 60 \
    --id-token-validity 60 \
    --token-validity-units AccessToken=minutes,IdToken=minutes,RefreshToken=days \
    --read-attributes email phone_number email_verified phone_number_verified \
    --write-attributes email phone_number \
    --explicit-auth-flows ALLOW_USER_PASSWORD_AUTH ALLOW_USER_SRP_AUTH ALLOW_REFRESH_TOKEN_AUTH \
    --supported-identity-providers Google Facebook MyOIDC \
    --callback-urls https://www.amazon.com https://example.com http://localhost:8001 myapp://example \
    --allowed-o-auth-flows code implicit \
    --allowed-o-auth-scopes openid profile aws.cognito.signin.user.admin solar-system-data/asteroids.add \
    --allowed-o-auth-flows-user-pool-client \
    --analytics-configuration ApplicationArn=arn:aws:mobiletargeting:us-west-2:767671399759:apps/thisisanexamplepinpointapplicationid,UserDataShared=TRUE \
    --prevent-user-existence-errors ENABLED \
    --enable-token-revocation \
    --enable-propagate-additional-user-context-data \
    --auth-session-validity 4
```

Output:

```
{
    "UserPoolClient": {
        "UserPoolId": "us-west-2_EXAMPLE",
        "ClientName": "MyTestClient",
        "ClientId": "123abc456defEXAMPLE",
        "ClientSecret": "this1234is5678my91011example1213client1415secret",
        "LastModifiedDate": 1726788459.464,
        "CreationDate": 1726788459.464,
        "RefreshTokenValidity": 10,
        "AccessTokenValidity": 60,
        "IdTokenValidity": 60,
        "TokenValidityUnits": {
            "AccessToken": "minutes",
            "IdToken": "minutes",
            "RefreshToken": "days"
        },
        "ReadAttributes": [
            "email_verified",
            "phone_number_verified",
            "phone_number",
            "email"
        ],
        "WriteAttributes": [
            "phone_number",
            "email"
        ],
        "ExplicitAuthFlows": [
            "ALLOW_USER_PASSWORD_AUTH",
            "ALLOW_USER_SRP_AUTH",
            "ALLOW_REFRESH_TOKEN_AUTH"
        ],
        "SupportedIdentityProviders": [
            "Google",
            "MyOIDC",
            "Facebook"
        ],
        "CallbackURLs": [
            "https://example.com",
            "https://www.amazon.com",
            "myapp://example",
            "http://localhost:8001"
        ],
        "AllowedOAuthFlows": [
            "implicit",
            "code"
        ],
        "AllowedOAuthScopes": [
            "aws.cognito.signin.user.admin",
            "openid",
            "profile",
            "solar-system-data/asteroids.add"
        ],
        "AllowedOAuthFlowsUserPoolClient": true,
        "AnalyticsConfiguration": {
            "ApplicationArn": "arn:aws:mobiletargeting:us-west-2:123456789012:apps/thisisanexamplepinpointapplicationid",
            "RoleArn": "arn:aws:iam::123456789012:role/aws-service-role/cognito-idp.amazonaws.com/AWSServiceRoleForAmazonCognitoIdp",
            "UserDataShared": true
        },
        "PreventUserExistenceErrors": "ENABLED",
        "EnableTokenRevocation": true,
        "EnablePropagateAdditionalUserContextData": true,
        "AuthSessionValidity": 4
    }
}
```

For more information, see [Application-specific settings with app clients](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html) in the *Amazon Cognito Developer Guide*.

## Output

UserPoolClient -> (structure)

The details of the new app client.

UserPoolId -> (string)

The ID of the user pool associated with the app client.

ClientName -> (string)

The name of the app client.

ClientId -> (string)

The ID of the app client.

ClientSecret -> (string)

The app client secret.

LastModifiedDate -> (timestamp)

The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.

CreationDate -> (timestamp)

The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.

RefreshTokenValidity -> (integer)

The refresh token time limit. After this limit expires, your user canât use their refresh token. To specify the time unit for `RefreshTokenValidity` as `seconds` , `minutes` , `hours` , or `days` , set a `TokenValidityUnits` value in your API request.

For example, when you set `RefreshTokenValidity` as `10` and `TokenValidityUnits` as `days` , your user can refresh their session and retrieve new access and ID tokens for 10 days.

The default time unit for `RefreshTokenValidity` in an API request is days. You canât set `RefreshTokenValidity` to 0. If you do, Amazon Cognito overrides the value with the default value of 30 days. *Valid range* is displayed below in seconds.

If you donât specify otherwise in the configuration of your app client, your refresh tokens are valid for 30 days.

AccessTokenValidity -> (integer)

The access token time limit. After this limit expires, your user canât use their access token. To specify the time unit for `AccessTokenValidity` as `seconds` , `minutes` , `hours` , or `days` , set a `TokenValidityUnits` value in your API request.

For example, when you set `AccessTokenValidity` to `10` and `TokenValidityUnits` to `hours` , your user can authorize access with their access token for 10 hours.

The default time unit for `AccessTokenValidity` in an API request is hours. *Valid range* is displayed below in seconds.

If you donât specify otherwise in the configuration of your app client, your access tokens are valid for one hour.

IdTokenValidity -> (integer)

The ID token time limit. After this limit expires, your user canât use their ID token. To specify the time unit for `IdTokenValidity` as `seconds` , `minutes` , `hours` , or `days` , set a `TokenValidityUnits` value in your API request.

For example, when you set `IdTokenValidity` as `10` and `TokenValidityUnits` as `hours` , your user can authenticate their session with their ID token for 10 hours.

The default time unit for `IdTokenValidity` in an API request is hours. *Valid range* is displayed below in seconds.

If you donât specify otherwise in the configuration of your app client, your ID tokens are valid for one hour.

TokenValidityUnits -> (structure)

The time units that, with `IdTokenValidity` , `AccessTokenValidity` , and `RefreshTokenValidity` , set and display the duration of ID, access, and refresh tokens for an app client. You can assign a separate token validity unit to each type of token.

AccessToken -> (string)

A time unit for the value that you set in the `AccessTokenValidity` parameter. The default `AccessTokenValidity` time unit is `hours` . `AccessTokenValidity` duration can range from five minutes to one day.

IdToken -> (string)

A time unit for the value that you set in the `IdTokenValidity` parameter. The default `IdTokenValidity` time unit is `hours` . `IdTokenValidity` duration can range from five minutes to one day.

RefreshToken -> (string)

A time unit for the value that you set in the `RefreshTokenValidity` parameter. The default `RefreshTokenValidity` time unit is `days` . `RefreshTokenValidity` duration can range from 60 minutes to 10 years.

ReadAttributes -> (list)

The list of user attributes that you want your app client to have read access to. After your user authenticates in your app, their access token authorizes them to read their own attribute value for any attribute in this list.

When you donât specify the `ReadAttributes` for your app client, your app can read the values of `email_verified` , `phone_number_verified` , and the standard attributes of your user pool. When your user pool app client has read access to these default attributes, `ReadAttributes` doesnât return any information. Amazon Cognito only populates `ReadAttributes` in the API response if you have specified your own custom set of read attributes.

(string)

WriteAttributes -> (list)

The list of user attributes that you want your app client to have write access to. After your user authenticates in your app, their access token authorizes them to set or modify their own attribute value for any attribute in this list.

When you donât specify the `WriteAttributes` for your app client, your app can write the values of the Standard attributes of your user pool. When your user pool has write access to these default attributes, `WriteAttributes` doesnât return any information. Amazon Cognito only populates `WriteAttributes` in the API response if you have specified your own custom set of write attributes.

If your app client allows users to sign in through an IdP, this array must include all attributes that you have mapped to IdP attributes. Amazon Cognito updates mapped attributes when users sign in to your application through an IdP. If your app client does not have write access to a mapped attribute, Amazon Cognito throws an error when it tries to update the attribute. For more information, see [Specifying IdP Attribute Mappings for Your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html) .

(string)

ExplicitAuthFlows -> (list)

The [authentication flows](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow-methods.html) that you want your user pool client to support. For each app client in your user pool, you can sign in your users with any combination of one or more flows, including with a user name and Secure Remote Password (SRP), a user name and password, or a custom authentication process that you define with Lambda functions.

### Note

If you donât specify a value for `ExplicitAuthFlows` , your app client supports `ALLOW_REFRESH_TOKEN_AUTH` , `ALLOW_USER_SRP_AUTH` , and `ALLOW_CUSTOM_AUTH` .

The values for authentication flow options include the following.

- `ALLOW_USER_AUTH` : Enable selection-based sign-in with `USER_AUTH` . This setting covers username-password, secure remote password (SRP), passwordless, and passkey authentication. This authentiation flow can do username-password and SRP authentication without other `ExplicitAuthFlows` permitting them. For example users can complete an SRP challenge through `USER_AUTH` without the flow `USER_SRP_AUTH` being active for the app client. This flow doesnât include `CUSTOM_AUTH` .  To activate this setting, your user pool must be in the [Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.
- `ALLOW_ADMIN_USER_PASSWORD_AUTH` : Enable admin based user password authentication flow `ADMIN_USER_PASSWORD_AUTH` . This setting replaces the `ADMIN_NO_SRP_AUTH` setting. With this authentication flow, your app passes a user name and password to Amazon Cognito in the request, instead of using the Secure Remote Password (SRP) protocol to securely transmit the password.
- `ALLOW_CUSTOM_AUTH` : Enable Lambda trigger based authentication.
- `ALLOW_USER_PASSWORD_AUTH` : Enable user password-based authentication. In this flow, Amazon Cognito receives the password in the request instead of using the SRP protocol to verify passwords.
- `ALLOW_USER_SRP_AUTH` : Enable SRP-based authentication.
- `ALLOW_REFRESH_TOKEN_AUTH` : Enable authflow to refresh tokens.

In some environments, you will see the values `ADMIN_NO_SRP_AUTH` , `CUSTOM_AUTH_FLOW_ONLY` , or `USER_PASSWORD_AUTH` . You canât assign these legacy `ExplicitAuthFlows` values to user pool clients at the same time as values that begin with `ALLOW_` , like `ALLOW_USER_SRP_AUTH` .

(string)

SupportedIdentityProviders -> (list)

A list of provider names for the identity providers (IdPs) that are supported on this client. The following are supported: `COGNITO` , `Facebook` , `Google` , `SignInWithApple` , and `LoginWithAmazon` . You can also specify the names that you configured for the SAML and OIDC IdPs in your user pool, for example `MySAMLIdP` or `MyOIDCIdP` .

This parameter sets the IdPs that [managed login](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html) will display on the login page for your app client. The removal of `COGNITO` from this list doesnât prevent authentication operations for local users with the user pools API in an Amazon Web Services SDK. The only way to prevent SDK-based authentication is to block access with a [WAF rule](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-waf.html) .

(string)

CallbackURLs -> (list)

A list of allowed redirect (callback) URLs for the IdPs.

A redirect URI must:

- Be an absolute URI.
- Be registered with the authorization server.
- Not include a fragment component.

See [OAuth 2.0 - Redirection Endpoint](https://tools.ietf.org/html/rfc6749#section-3.1.2) .

Amazon Cognito requires HTTPS over HTTP except for [http://localhost](http://localhost) for testing purposes only.

App callback URLs such as myapp://example are also supported.

(string)

LogoutURLs -> (list)

A list of allowed logout URLs for the IdPs.

(string)

DefaultRedirectURI -> (string)

The default redirect URI. Must be in the `CallbackURLs` list.

A redirect URI must:

- Be an absolute URI.
- Be registered with the authorization server.
- Not include a fragment component.

See [OAuth 2.0 - Redirection Endpoint](https://tools.ietf.org/html/rfc6749#section-3.1.2) .

Amazon Cognito requires HTTPS over HTTP except for [http://localhost](http://localhost) for testing purposes only.

App callback URLs such as myapp://example are also supported.

AllowedOAuthFlows -> (list)

The OAuth grant types that you want your app client to generate. To create an app client that generates client credentials grants, you must add `client_credentials` as the only allowed OAuth flow.

code

Use a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the `/oauth2/token` endpoint.

implicit

Issue the access token (and, optionally, ID token, based on scopes) directly to your user.

client_credentials

Issue the access token from the `/oauth2/token` endpoint directly to a non-person user using a combination of the client ID and client secret.

(string)

AllowedOAuthScopes -> (list)

The OAuth 2.0 scopes that you want your app client to support. Can include standard OAuth scopes like `phone` , `email` , `openid` , and `profile` . Can also include the `aws.cognito.signin.user.admin` scope that authorizes user profile self-service operations and custom scopes from resource servers.

(string)

AllowedOAuthFlowsUserPoolClient -> (boolean)

Set to `true` to use OAuth 2.0 authorization server features in your app client.

This parameter must have a value of `true` before you can configure the following features in your app client.

- `CallBackURLs` : Callback URLs.
- `LogoutURLs` : Sign-out redirect URLs.
- `AllowedOAuthScopes` : OAuth 2.0 scopes.
- `AllowedOAuthFlows` : Support for authorization code, implicit, and client credentials OAuth 2.0 grants.

To use authorization server features, configure one of these features in the Amazon Cognito console or set `AllowedOAuthFlowsUserPoolClient` to `true` in a `CreateUserPoolClient` or `UpdateUserPoolClient` API request. If you donât set a value for `AllowedOAuthFlowsUserPoolClient` in a request with the CLI or SDKs, it defaults to `false` . When `false` , only SDK-based API sign-in is permitted.

AnalyticsConfiguration -> (structure)

The user pool analytics configuration for collecting metrics and sending them to your Amazon Pinpoint campaign.

### Note

In Amazon Web Services Regions where Amazon Pinpoint isnât available, user pools only support sending events to Amazon Pinpoint projects in Amazon Web Services Region us-east-1. In Regions where Amazon Pinpoint is available, user pools support sending events to Amazon Pinpoint projects within that same Region.

ApplicationId -> (string)

Your Amazon Pinpoint project ID.

ApplicationArn -> (string)

The Amazon Resource Name (ARN) of an Amazon Pinpoint project that you want to connect to your user pool app client. Amazon Cognito publishes events to the Amazon Pinpoint project that `ApplicationArn` declares. You can also configure your application to pass an endpoint ID in the `AnalyticsMetadata` parameter of sign-in operations. The endpoint ID is information about the destination for push notifications

RoleArn -> (string)

The ARN of an Identity and Access Management role that has the permissions required for Amazon Cognito to publish events to Amazon Pinpoint analytics.

ExternalId -> (string)

The [external ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html) of the role that Amazon Cognito assumes to send analytics data to Amazon Pinpoint.

UserDataShared -> (boolean)

If `UserDataShared` is `true` , Amazon Cognito includes user data in the events that it publishes to Amazon Pinpoint analytics.

PreventUserExistenceErrors -> (string)

When `ENABLED` , suppresses messages that might indicate a valid user exists when someone attempts sign-in. This parameters sets your preference for the errors and responses that you want Amazon Cognito APIs to return during authentication, account confirmation, and password recovery when the user doesnât exist in the user pool. When set to `ENABLED` and the user doesnât exist, authentication returns an error indicating either the username or password was incorrect. Account confirmation and password recovery return a response indicating a code was sent to a simulated destination. When set to `LEGACY` , those APIs return a `UserNotFoundException` exception if the user doesnât exist in the user pool.

Defaults to `LEGACY` .

EnableTokenRevocation -> (boolean)

Indicates whether token revocation is activated for the user pool client. When you create a new user pool client, token revocation is activated by default.

EnablePropagateAdditionalUserContextData -> (boolean)

When `EnablePropagateAdditionalUserContextData` is true, Amazon Cognito accepts an `IpAddress` value that you send in the `UserContextData` parameter. The `UserContextData` parameter sends information to Amazon Cognito threat protection for risk analysis. You can send `UserContextData` when you sign in Amazon Cognito native users with the `InitiateAuth` and `RespondToAuthChallenge` API operations.

When `EnablePropagateAdditionalUserContextData` is false, you canât send your userâs source IP address to Amazon Cognito threat protection with unauthenticated API operations. `EnablePropagateAdditionalUserContextData` doesnât affect whether you can send a source IP address in a `ContextData` parameter with the authenticated API operations `AdminInitiateAuth` and `AdminRespondToAuthChallenge` .

You can only activate `EnablePropagateAdditionalUserContextData` in an app client that has a client secret. For more information about propagation of user context data, see [Adding user device and session data to API requests](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.html#user-pool-settings-adaptive-authentication-device-fingerprint) .

AuthSessionValidity -> (integer)

Amazon Cognito creates a session token for each API request in an authentication flow. `AuthSessionValidity` is the duration, in minutes, of that session token. Your user pool native user must respond to each authentication challenge before the session expires.

RefreshTokenRotation -> (structure)

The configuration of your app client for refresh token rotation. When enabled, your app client issues new ID, access, and refresh tokens when users renew their sessions with refresh tokens. When disabled, token refresh issues only ID and access tokens.

Feature -> (string)

The state of refresh token rotation for the current app client.

RetryGracePeriodSeconds -> (integer)

When you request a token refresh with `GetTokensFromRefreshToken` , the original refresh token that youâre rotating out can remain valid for a period of time of up to 60 seconds. This allows for client-side retries. When `RetryGracePeriodSeconds` is `0` , the grace period is disabled and a successful request immediately invalidates the submitted refresh token.