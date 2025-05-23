# modify-verified-access-trust-providerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-verified-access-trust-provider.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-verified-access-trust-provider.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# modify-verified-access-trust-provider

## Description

Modifies the configuration of the specified Amazon Web Services Verified Access trust provider.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyVerifiedAccessTrustProvider)

## Synopsis

```
modify-verified-access-trust-provider
--verified-access-trust-provider-id <value>
[--oidc-options <value>]
[--device-options <value>]
[--description <value>]
[--dry-run | --no-dry-run]
[--client-token <value>]
[--sse-specification <value>]
[--native-application-oidc-options <value>]
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

`--verified-access-trust-provider-id` (string)

The ID of the Verified Access trust provider.

`--oidc-options` (structure)

The options for an OpenID Connect-compatible user-identity trust provider.

Issuer -> (string)

The OIDC issuer.

AuthorizationEndpoint -> (string)

The OIDC authorization endpoint.

TokenEndpoint -> (string)

The OIDC token endpoint.

UserInfoEndpoint -> (string)

The OIDC user info endpoint.

ClientId -> (string)

The client identifier.

ClientSecret -> (string)

The client secret.

Scope -> (string)

OpenID Connect (OIDC) scopes are used by an application during authentication to authorize access to a userâs details. Each scope returns a specific set of user attributes.

Shorthand Syntax:

```
Issuer=string,AuthorizationEndpoint=string,TokenEndpoint=string,UserInfoEndpoint=string,ClientId=string,ClientSecret=string,Scope=string
```

JSON Syntax:

```
{
  "Issuer": "string",
  "AuthorizationEndpoint": "string",
  "TokenEndpoint": "string",
  "UserInfoEndpoint": "string",
  "ClientId": "string",
  "ClientSecret": "string",
  "Scope": "string"
}
```

`--device-options` (structure)

The options for a device-based trust provider. This parameter is required when the provider type is `device` .

PublicSigningKeyUrl -> (string)

The URL Amazon Web Services Verified Access will use to verify the authenticity of the device tokens.

Shorthand Syntax:

```
PublicSigningKeyUrl=string
```

JSON Syntax:

```
{
  "PublicSigningKeyUrl": "string"
}
```

`--description` (string)

A description for the Verified Access trust provider.

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--client-token` (string)

A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html) .

`--sse-specification` (structure)

The options for server side encryption.

CustomerManagedKeyEnabled -> (boolean)

Enable or disable the use of customer managed KMS keys for server side encryption.

Valid values: `True` | `False`

KmsKeyArn -> (string)

The ARN of the KMS key.

Shorthand Syntax:

```
CustomerManagedKeyEnabled=boolean,KmsKeyArn=string
```

JSON Syntax:

```
{
  "CustomerManagedKeyEnabled": true|false,
  "KmsKeyArn": "string"
}
```

`--native-application-oidc-options` (structure)

The OpenID Connect (OIDC) options.

PublicSigningKeyEndpoint -> (string)

The public signing key endpoint.

Issuer -> (string)

The OIDC issuer identifier of the IdP.

AuthorizationEndpoint -> (string)

The authorization endpoint of the IdP.

TokenEndpoint -> (string)

The token endpoint of the IdP.

UserInfoEndpoint -> (string)

The user info endpoint of the IdP.

ClientId -> (string)

The OAuth 2.0 client identifier.

ClientSecret -> (string)

The OAuth 2.0 client secret.

Scope -> (string)

The set of user claims to be requested from the IdP.

Shorthand Syntax:

```
PublicSigningKeyEndpoint=string,Issuer=string,AuthorizationEndpoint=string,TokenEndpoint=string,UserInfoEndpoint=string,ClientId=string,ClientSecret=string,Scope=string
```

JSON Syntax:

```
{
  "PublicSigningKeyEndpoint": "string",
  "Issuer": "string",
  "AuthorizationEndpoint": "string",
  "TokenEndpoint": "string",
  "UserInfoEndpoint": "string",
  "ClientId": "string",
  "ClientSecret": "string",
  "Scope": "string"
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

**To modify the configuration of a Verified Access trust provider**

The following `modify-verified-access-trust-provider` example adds the specified description to the specified Verified Access trust provider.

```
aws ec2 modify-verified-access-trust-provider \
    --verified-access-trust-provider-id vatp-0bb32de759a3e19e7 \
    --description "Testing Verified Access"
```

Output:

```
{
    "VerifiedAccessTrustProvider": {
        "VerifiedAccessTrustProviderId": "vatp-0bb32de759a3e19e7",
        "Description": "Testing Verified Access",
        "TrustProviderType": "user",
        "UserTrustProviderType": "iam-identity-center",
        "PolicyReferenceName": "idc",
        "CreationTime": "2023-08-25T19:00:38",
        "LastUpdatedTime": "2023-08-25T19:18:21"
    }
}
```

For more information, see [Trust providers for Verified Access](https://docs.aws.amazon.com/verified-access/latest/ug/trust-providers.html) in the *AWS Verified Access User Guide*.

## Output

VerifiedAccessTrustProvider -> (structure)

Details about the Verified Access trust provider.

VerifiedAccessTrustProviderId -> (string)

The ID of the Amazon Web Services Verified Access trust provider.

Description -> (string)

A description for the Amazon Web Services Verified Access trust provider.

TrustProviderType -> (string)

The type of Verified Access trust provider.

UserTrustProviderType -> (string)

The type of user-based trust provider.

DeviceTrustProviderType -> (string)

The type of device-based trust provider.

OidcOptions -> (structure)

The options for an OpenID Connect-compatible user-identity trust provider.

Issuer -> (string)

The OIDC issuer.

AuthorizationEndpoint -> (string)

The OIDC authorization endpoint.

TokenEndpoint -> (string)

The OIDC token endpoint.

UserInfoEndpoint -> (string)

The OIDC user info endpoint.

ClientId -> (string)

The client identifier.

ClientSecret -> (string)

The client secret.

Scope -> (string)

The OpenID Connect (OIDC) scope specified.

DeviceOptions -> (structure)

The options for device-identity trust provider.

TenantId -> (string)

The ID of the tenant application with the device-identity provider.

PublicSigningKeyUrl -> (string)

The URL Amazon Web Services Verified Access will use to verify the authenticity of the device tokens.

PolicyReferenceName -> (string)

The identifier to be used when working with policy rules.

CreationTime -> (string)

The creation time.

LastUpdatedTime -> (string)

The last updated time.

Tags -> (list)

The tags.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

SseSpecification -> (structure)

The options in use for server side encryption.

CustomerManagedKeyEnabled -> (boolean)

Indicates whether customer managed KMS keys are in use for server side encryption.

Valid values: `True` | `False`

KmsKeyArn -> (string)

The ARN of the KMS key.

NativeApplicationOidcOptions -> (structure)

The OpenID Connect (OIDC) options.

PublicSigningKeyEndpoint -> (string)

The public signing key endpoint.

Issuer -> (string)

The OIDC issuer identifier of the IdP.

AuthorizationEndpoint -> (string)

The authorization endpoint of the IdP.

TokenEndpoint -> (string)

The token endpoint of the IdP.

UserInfoEndpoint -> (string)

The user info endpoint of the IdP.

ClientId -> (string)

The OAuth 2.0 client identifier.

Scope -> (string)

The set of user claims to be requested from the IdP.