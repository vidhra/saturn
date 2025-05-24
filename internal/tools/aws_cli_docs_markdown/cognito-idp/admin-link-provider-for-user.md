# admin-link-provider-for-userÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-link-provider-for-user.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-link-provider-for-user.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cognito-idp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html#cli-aws-cognito-idp) ]

# admin-link-provider-for-user

## Description

Links an existing user account in a user pool, or `DestinationUser` , to an identity from an external IdP, or `SourceUser` , based on a specified attribute name and value from the external IdP.

This operation connects a local user profile with a user identity who hasnât yet signed in from their third-party IdP. When the user signs in with their IdP, they get access-control configuration from the local user profile. Linked local users can also sign in with SDK-based API operations like `InitiateAuth` after they sign in at least once through their IdP. For more information, see [Linking federated users](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation-consolidate-users.html) .

### Note

The maximum number of federated identities linked to a user is five.

### Warning

Because this API allows a user with an external federated identity to sign in as a local user, it is critical that it only be used with external IdPs and linked attributes that you trust.

### Note

Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.

**Learn more**

- [Signing Amazon Web Services API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
- [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminLinkProviderForUser)

## Synopsis

```
admin-link-provider-for-user
--user-pool-id <value>
--destination-user <value>
--source-user <value>
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

The ID of the user pool where you want to link a federated identity.

`--destination-user` (structure)

The existing user in the user pool that you want to assign to the external IdP user account. This user can be a local (Username + Password) Amazon Cognito user pools user or a federated user (for example, a SAML or Facebook user). If the user doesnât exist, Amazon Cognito generates an exception. Amazon Cognito returns this user when the new user (with the linked IdP attribute) signs in.

For a native username + password user, the `ProviderAttributeValue` for the `DestinationUser` should be the username in the user pool. For a federated user, it should be the provider-specific `user_id` .

The `ProviderAttributeName` of the `DestinationUser` is ignored.

The `ProviderName` should be set to `Cognito` for users in Cognito user pools.

### Warning

All attributes in the DestinationUser profile must be mutable. If you have assigned the user any immutable custom attributes, the operation wonât succeed.

ProviderName -> (string)

The name of the provider, such as Facebook, Google, or Login with Amazon.

ProviderAttributeName -> (string)

The name of the provider attribute to link to, such as `NameID` .

ProviderAttributeValue -> (string)

The value of the provider attribute to link to, such as `xxxxx_account` .

Shorthand Syntax:

```
ProviderName=string,ProviderAttributeName=string,ProviderAttributeValue=string
```

JSON Syntax:

```
{
  "ProviderName": "string",
  "ProviderAttributeName": "string",
  "ProviderAttributeValue": "string"
}
```

`--source-user` (structure)

An external IdP account for a user who doesnât exist yet in the user pool. This user must be a federated user (for example, a SAML or Facebook user), not another native user.

If the `SourceUser` is using a federated social IdP, such as Facebook, Google, or Login with Amazon, you must set the `ProviderAttributeName` to `Cognito_Subject` . For social IdPs, the `ProviderName` will be `Facebook` , `Google` , or `LoginWithAmazon` , and Amazon Cognito will automatically parse the Facebook, Google, and Login with Amazon tokens for `id` , `sub` , and `user_id` , respectively. The `ProviderAttributeValue` for the user must be the same value as the `id` , `sub` , or `user_id` value found in the social IdP token.

For OIDC, the `ProviderAttributeName` can be any mapped value from a claim in the ID token, or that your app retrieves from the `userInfo` endpoint. For SAML, the `ProviderAttributeName` can be any mapped value from a claim in the SAML assertion.

The following additional considerations apply to `SourceUser` for OIDC and SAML providers.

- You must map the claim to a user pool attribute in your IdP configuration, and set the user pool attribute name as the value of `ProviderAttributeName` in your `AdminLinkProviderForUser` request. For example, `email` .
- When you set `ProviderAttributeName` to `Cognito_Subject` , Amazon Cognito will automatically parse the default unique identifier found in the subject from the IdP token.

ProviderName -> (string)

The name of the provider, such as Facebook, Google, or Login with Amazon.

ProviderAttributeName -> (string)

The name of the provider attribute to link to, such as `NameID` .

ProviderAttributeValue -> (string)

The value of the provider attribute to link to, such as `xxxxx_account` .

Shorthand Syntax:

```
ProviderName=string,ProviderAttributeName=string,ProviderAttributeValue=string
```

JSON Syntax:

```
{
  "ProviderName": "string",
  "ProviderAttributeName": "string",
  "ProviderAttributeValue": "string"
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

**To link a local user to a federated user**

The following `admin-link-provider-for-user` example links the local user diego to a user who will do federated sign-in with Google.

```
aws cognito-idp admin-link-provider-for-user \
    --user-pool-id us-west-2_EXAMPLE \
    --destination-user ProviderName=Cognito,ProviderAttributeValue=diego \
    --source-user ProviderAttributeName=Cognito_Subject,ProviderAttributeValue=0000000000000000,ProviderName=Google
```

For more information, see [Linking federated users to an existing user profile](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation-consolidate-users.html) in the *Amazon Cognito Developer Guide*.

## Output

None