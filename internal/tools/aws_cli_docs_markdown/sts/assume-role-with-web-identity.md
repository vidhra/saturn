# assume-role-with-web-identityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-role-with-web-identity.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-role-with-web-identity.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/index.html#cli-aws-sts) ]

# assume-role-with-web-identity

## Description

Returns a set of temporary security credentials for users who have been authenticated in a mobile or web application with a web identity provider. Example providers include the OAuth 2.0 providers Login with Amazon and Facebook, or any OpenID Connect-compatible identity provider such as Google or [Amazon Cognito federated identities](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html) .

### Note

For mobile applications, we recommend that you use Amazon Cognito. You can use Amazon Cognito with the [Amazon Web Services SDK for iOS Developer Guide](http://aws.amazon.com/sdkforios/) and the [Amazon Web Services SDK for Android Developer Guide](http://aws.amazon.com/sdkforandroid/) to uniquely identify a user. You can also supply the user with a consistent identity throughout the lifetime of an application.

To learn more about Amazon Cognito, see [Amazon Cognito identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html) in *Amazon Cognito Developer Guide* .

Calling `AssumeRoleWithWebIdentity` does not require the use of Amazon Web Services security credentials. Therefore, you can distribute an application (for example, on mobile devices) that requests temporary security credentials without including long-term Amazon Web Services credentials in the application. You also donât need to deploy server-based proxy services that use long-term Amazon Web Services credentials. Instead, the identity of the caller is validated by using a token from the web identity provider. For a comparison of `AssumeRoleWithWebIdentity` with the other API operations that produce temporary credentials, see [Requesting Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html) and [Compare STS credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_sts-comparison.html) in the *IAM User Guide* .

The temporary security credentials returned by this API consist of an access key ID, a secret access key, and a security token. Applications can use these temporary security credentials to sign calls to Amazon Web Services service API operations.

**Session Duration**

By default, the temporary security credentials created by `AssumeRoleWithWebIdentity` last for one hour. However, you can use the optional `DurationSeconds` parameter to specify the duration of your session. You can provide a value from 900 seconds (15 minutes) up to the maximum session duration setting for the role. This setting can have a value from 1 hour to 12 hours. To learn how to view the maximum value for your role, see [Update the maximum session duration for a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-role-settings.html#id_roles_update-session-duration) in the *IAM User Guide* . The maximum session duration limit applies when you use the `AssumeRole*` API operations or the `assume-role*` CLI commands. However the limit does not apply when you use those operations to create a console URL. For more information, see [Using IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html) in the *IAM User Guide* .

**Permissions**

The temporary security credentials created by `AssumeRoleWithWebIdentity` can be used to make API calls to any Amazon Web Services service with the following exception: you cannot call the STS `GetFederationToken` or `GetSessionToken` API operations.

(Optional) You can pass inline or managed [session policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session) to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policy Amazon Resource Names (ARNs) to use as managed session policies. The plaintext that you use for both inline and managed session policies canât exceed 2,048 characters. Passing policies to this operation returns new temporary credentials. The resulting sessionâs permissions are the intersection of the roleâs identity-based policy and the session policies. You can use the roleâs temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see [Session Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session) in the *IAM User Guide* .

**Tags**

(Optional) You can configure your IdP to pass attributes into your web identity token as session tags. Each session tag consists of a key name and an associated value. For more information about session tags, see [Passing Session Tags in STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html) in the *IAM User Guide* .

You can pass up to 50 session tags. The plaintext session tag keys canât exceed 128 characters and the values canât exceed 256 characters. For these and additional limits, see [IAM and STS Character Limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html#reference_iam-limits-entity-length) in the *IAM User Guide* .

### Note

An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The `PackedPolicySize` response element indicates by percentage how close the policies and tags for your request are to the upper size limit.

You can pass a session tag with the same key as a tag that is attached to the role. When you do, the session tag overrides the role tag with the same key.

An administrator must grant you the permissions necessary to pass session tags. The administrator can also create granular permissions to allow you to pass only specific session tags. For more information, see [Tutorial: Using Tags for Attribute-Based Access Control](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide* .

You can set the session tags as transitive. Transitive tags persist during role chaining. For more information, see [Chaining Roles with Session Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_role-chaining) in the *IAM User Guide* .

**Identities**

Before your application can call `AssumeRoleWithWebIdentity` , you must have an identity token from a supported identity provider and create a role that the application can assume. The role that your application assumes must trust the identity provider that is associated with the identity token. In other words, the identity provider must be specified in the roleâs trust policy.

### Warning

Calling `AssumeRoleWithWebIdentity` can result in an entry in your CloudTrail logs. The entry includes the [Subject](http://openid.net/specs/openid-connect-core-1_0.html#Claims) of the provided web identity token. We recommend that you avoid using any personally identifiable information (PII) in this field. For example, you could instead use a GUID or a pairwise identifier, as [suggested in the OIDC specification](http://openid.net/specs/openid-connect-core-1_0.html#SubjectIDTypes) .

For more information about how to use OIDC federation and the `AssumeRoleWithWebIdentity` API, see the following resources:

- [Using Web Identity Federation API Operations for Mobile Apps](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc_manual.html) and [Federation Through a Web-based Identity Provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_assumerolewithwebidentity) .
- [Amazon Web Services SDK for iOS Developer Guide](http://aws.amazon.com/sdkforios/) and [Amazon Web Services SDK for Android Developer Guide](http://aws.amazon.com/sdkforandroid/) . These toolkits contain sample apps that show how to invoke the identity providers. The toolkits then show how to use the information from these providers to get and use temporary security credentials.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sts-2011-06-15/AssumeRoleWithWebIdentity)

## Synopsis

```
assume-role-with-web-identity
--role-arn <value>
--role-session-name <value>
--web-identity-token <value>
[--provider-id <value>]
[--policy-arns <value>]
[--policy <value>]
[--duration-seconds <value>]
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

`--role-arn` (string)

The Amazon Resource Name (ARN) of the role that the caller is assuming.

### Note

Additional considerations apply to Amazon Cognito identity pools that assume [cross-account IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) . The trust policies of these roles must accept the `cognito-identity.amazonaws.com` service principal and must contain the `cognito-identity.amazonaws.com:aud` condition key to restrict role assumption to users from your intended identity pools. A policy that trusts Amazon Cognito identity pools without this condition creates a risk that a user from an unintended identity pool can assume the role. For more information, see [Trust policies for IAM roles in Basic (Classic) authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/iam-roles.html#trust-policies) in the *Amazon Cognito Developer Guide* .

`--role-session-name` (string)

An identifier for the assumed role session. Typically, you pass the name or identifier that is associated with the user who is using your application. That way, the temporary security credentials that your application will use are associated with that user. This session name is included as part of the ARN and assumed role ID in the `AssumedRoleUser` response element.

For security purposes, administrators can view this field in [CloudTrail logs](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html#cloudtrail-integration_signin-tempcreds) to help identify who performed an action in Amazon Web Services. Your administrator might require that you specify your user name as the session name when you assume the role. For more information, see ` `sts:RoleSessionName` [https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys).html#ck_rolesessionname`__ .

The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-

`--web-identity-token` (string)

The OAuth 2.0 access token or OpenID Connect ID token that is provided by the identity provider. Your application must get this token by authenticating the user who is using your application with a web identity provider before the application makes an `AssumeRoleWithWebIdentity` call. Timestamps in the token must be formatted as either an integer or a long integer. Tokens must be signed using either RSA keys (RS256, RS384, or RS512) or ECDSA keys (ES256, ES384, or ES512).

`--provider-id` (string)

The fully qualified host component of the domain name of the OAuth 2.0 identity provider. Do not specify this value for an OpenID Connect identity provider.

Currently `www.amazon.com` and `graph.facebook.com` are the only supported identity providers for OAuth 2.0 access tokens. Do not include URL schemes and port numbers.

Do not specify this value for OpenID Connect ID tokens.

`--policy-arns` (list)

The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. The policies must exist in the same account as the role.

This parameter is optional. You can provide up to 10 managed policy ARNs. However, the plaintext that you use for both inline and managed session policies canât exceed 2,048 characters. For more information about ARNs, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the Amazon Web Services General Reference.

### Note

An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The `PackedPolicySize` response element indicates by percentage how close the policies and tags for your request are to the upper size limit.

Passing policies to this operation returns new temporary credentials. The resulting sessionâs permissions are the intersection of the roleâs identity-based policy and the session policies. You can use the roleâs temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see [Session Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session) in the *IAM User Guide* .

(structure)

A reference to the IAM managed policy that is passed as a session policy for a role session or a federated user session.

arn -> (string)

The Amazon Resource Name (ARN) of the IAM managed policy to use as a session policy for the role. For more information about ARNs, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

Shorthand Syntax:

```
arn=string ...
```

JSON Syntax:

```
[
  {
    "arn": "string"
  }
  ...
]
```

`--policy` (string)

An IAM policy in JSON format that you want to use as an inline session policy.

This parameter is optional. Passing policies to this operation returns new temporary credentials. The resulting sessionâs permissions are the intersection of the roleâs identity-based policy and the session policies. You can use the roleâs temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see [Session Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session) in the *IAM User Guide* .

The plaintext that you use for both inline and managed session policies canât exceed 2,048 characters. The JSON policy characters can be any ASCII character from the space character to the end of the valid character list (u0020 through u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.

For more information about role session permissions, see [Session policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session) .

### Note

An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The `PackedPolicySize` response element indicates by percentage how close the policies and tags for your request are to the upper size limit.

`--duration-seconds` (integer)

The duration, in seconds, of the role session. The value can range from 900 seconds (15 minutes) up to the maximum session duration setting for the role. This setting can have a value from 1 hour to 12 hours. If you specify a value higher than this setting, the operation fails. For example, if you specify a session duration of 12 hours, but your administrator set the maximum session duration to 6 hours, your operation fails. To learn how to view the maximum value for your role, see [View the Maximum Session Duration Setting for a Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html#id_roles_use_view-role-max-session) in the *IAM User Guide* .

By default, the value is set to `3600` seconds.

### Note

The `DurationSeconds` parameter is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a `SessionDuration` parameter that specifies the maximum length of the console session. For more information, see [Creating a URL that Enables Federated Users to Access the Amazon Web Services Management Console](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html) in the *IAM User Guide* .

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

**To get short-term credentials for a role authenticated with Web Identity (OAuth 2.â0)**

The following `assume-role-with-web-identity` command retrieves a set of short-term credentials for the IAM role `app1`. The request is authenticated by using the web identity token supplied by the specified web identity provider. Two additional policies are applied to the session to further restrict what the user can do. The returned credentials expire one hour after they are generated.

```
aws sts assume-role-with-web-identity \
    --duration-seconds 3600 \
    --role-session-name "app1" \
    --provider-id "www.amazon.com" \
    --policy-arns "arn:aws:iam::123456789012:policy/q=webidentitydemopolicy1","arn:aws:iam::123456789012:policy/webidentitydemopolicy2" \
    --role-arn arn:aws:iam::123456789012:role/FederatedWebIdentityRole \
    --web-identity-token "Atza%7CIQEBLjAsAhRFiXuWpUXuRvQ9PZL3GMFcYevydwIUFAHZwXZXXXXXXXXJnrulxKDHwy87oGKPznh0D6bEQZTSCzyoCtL_8S07pLpr0zMbn6w1lfVZKNTBdDansFBmtGnIsIapjI6xKR02Yc_2bQ8LZbUXSGm6Ry6_BG7PrtLZtj_dfCTj92xNGed-CrKqjG7nPBjNIL016GGvuS5gSvPRUxWES3VYfm1wl7WTI7jn-Pcb6M-buCgHhFOzTQxod27L9CqnOLio7N3gZAGpsp6n1-AJBOCJckcyXe2c6uD0srOJeZlKUm2eTDVMf8IehDVI0r1QOnTV6KzzAI3OY87Vd_cVMQ"
```

Output:

```
{
    "SubjectFromWebIdentityToken": "amzn1.account.AF6RHO7KZU5XRVQJGXK6HB56KR2A",
    "Audience": "client.5498841531868486423.1548@apps.example.com",
    "AssumedRoleUser": {
        "Arn": "arn:aws:sts::123456789012:assumed-role/FederatedWebIdentityRole/app1",
        "AssumedRoleId": "AROACLKWSDQRAOEXAMPLE:app1"
    },
    "Credentials": {
        "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY",
        "SessionToken": "AQoEXAMPLEH4aoAH0gNCAPyJxz4BlCFFxWNE1OPTgk5TthT+FvwqnKwRcOIfrRh3c/LTo6UDdyJwOOvEVPvLXCrrrUtdnniCEXAMPLE/IvU1dYUg2RVAJBanLiHb4IgRmpRV3zrkuWJOgQs8IZZaIv2BXIa2R4OlgkBN9bkUDNCJiBeb/AXlzBBko7b15fjrBs2+cTQtpZ3CYWFXG8C5zqx37wnOE49mRl/+OtkIKGO7fAE",
        "Expiration": "2020-05-19T18:06:10+00:00"
    },
    "Provider": "www.amazon.com"
}
```

For more information, see [Requesting Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_assumerolewithwebidentity) in the *AWS IAM User Guide*.

## Output

Credentials -> (structure)

The temporary security credentials, which include an access key ID, a secret access key, and a security token.

### Note

The size of the security token that STS API operations return is not fixed. We strongly recommend that you make no assumptions about the maximum size.

AccessKeyId -> (string)

The access key ID that identifies the temporary security credentials.

SecretAccessKey -> (string)

The secret access key that can be used to sign requests.

SessionToken -> (string)

The token that users must pass to the service API to use the temporary credentials.

Expiration -> (timestamp)

The date on which the current credentials expire.

SubjectFromWebIdentityToken -> (string)

The unique user identifier that is returned by the identity provider. This identifier is associated with the `WebIdentityToken` that was submitted with the `AssumeRoleWithWebIdentity` call. The identifier is typically unique to the user and the application that acquired the `WebIdentityToken` (pairwise identifier). For OpenID Connect ID tokens, this field contains the value returned by the identity provider as the tokenâs `sub` (Subject) claim.

AssumedRoleUser -> (structure)

The Amazon Resource Name (ARN) and the assumed role ID, which are identifiers that you can use to refer to the resulting temporary security credentials. For example, you can reference these credentials as a principal in a resource-based policy by using the ARN or assumed role ID. The ARN and ID include the `RoleSessionName` that you specified when you called `AssumeRole` .

AssumedRoleId -> (string)

A unique identifier that contains the role ID and the role session name of the role that is being assumed. The role ID is generated by Amazon Web Services when the role is created.

Arn -> (string)

The ARN of the temporary security credentials that are returned from the  AssumeRole action. For more information about ARNs and how to use them in policies, see [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html) in the *IAM User Guide* .

PackedPolicySize -> (integer)

A percentage value that indicates the packed size of the session policies and session tags combined passed in the request. The request fails if the packed size is greater than 100 percent, which means the policies and tags exceeded the allowed space.

Provider -> (string)

The issuing authority of the web identity token presented. For OpenID Connect ID tokens, this contains the value of the `iss` field. For OAuth 2.0 access tokens, this contains the value of the `ProviderId` parameter that was passed in the `AssumeRoleWithWebIdentity` request.

Audience -> (string)

The intended audience (also known as client ID) of the web identity token. This is traditionally the client identifier issued to the application that requested the web identity token.

SourceIdentity -> (string)

The value of the source identity that is returned in the JSON web token (JWT) from the identity provider.

You can require users to set a source identity value when they assume a role. You do this by using the `sts:SourceIdentity` condition key in a role trust policy. That way, actions that are taken with the role are associated with that user. After the source identity is set, the value cannot be changed. It is present in the request for all actions that are taken by the role and persists across [chained role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#id_roles_terms-and-concepts) sessions. You can configure your identity provider to use an attribute associated with your users, like user name or email, as the source identity when calling `AssumeRoleWithWebIdentity` . You do this by adding a claim to the JSON web token. To learn more about OIDC tokens and claims, see [Using Tokens with User Pools](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-with-identity-providers.html) in the *Amazon Cognito Developer Guide* . For more information about using source identity, see [Monitor and control actions taken with assumed roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html) in the *IAM User Guide* .

The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-