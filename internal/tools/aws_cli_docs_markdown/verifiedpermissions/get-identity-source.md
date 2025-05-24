# get-identity-sourceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/get-identity-source.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/get-identity-source.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [verifiedpermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/index.html#cli-aws-verifiedpermissions) ]

# get-identity-source

## Description

Retrieves the details about the specified identity source.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/verifiedpermissions-2021-12-01/GetIdentitySource)

## Synopsis

```
get-identity-source
--policy-store-id <value>
--identity-source-id <value>
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

`--policy-store-id` (string)

Specifies the ID of the policy store that contains the identity source you want information about.

`--identity-source-id` (string)

Specifies the ID of the identity source you want information about.

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

**To retrieve details about an identity source**

The following `get-identity-source` example displays the details for the identity source with the specified Id.

```
aws verifiedpermissions get-identity-source \
    --identity-source  ISEXAMPLEabcdefg111111 \
    --policy-store-id PSEXAMPLEabcdefg111111
```

Output:

```
{
    "createdDate": "2023-06-12T22:27:49.150035+00:00",
    "details": {
        "clientIds": [ "a1b2c3d4e5f6g7h8i9j0kalbmc" ],
        "discoveryUrl": "https://cognito-idp.us-west-2.amazonaws.com/us-west-2_1a2b3c4d5",
        "openIdIssuer": "COGNITO",
        "userPoolArn": "arn:aws:cognito-idp:us-west-2:123456789012:userpool/us-west-2_1a2b3c4d5"
    },
    "identitySourceId": "ISEXAMPLEabcdefg111111",
    "lastUpdatedDate": "2023-06-12T22:27:49.150035+00:00",
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "principalEntityType": "User"
}
```

For more information about identity sources, see [Using Amazon Verified Permissions with identity providers](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/identity-providers.html) in the *Amazon Verified Permissions User Guide*.

## Output

createdDate -> (timestamp)

The date and time that the identity source was originally created.

details -> (structure)

A structure that describes the configuration of the identity source.

clientIds -> (list)

The application client IDs associated with the specified Amazon Cognito user pool that are enabled for this identity source.

(string)

userPoolArn -> (string)

The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Amazon Cognito user pool whose identities are accessible to this Verified Permissions policy store.

discoveryUrl -> (string)

The well-known URL that points to this user poolâs OIDC discovery endpoint. This is a URL string in the following format. This URL replaces the placeholders for both the Amazon Web Services Region and the user pool identifier with those appropriate for this user pool.

`https://cognito-idp.*<region>* .amazonaws.com/*<user-pool-id>* /.well-known/openid-configuration`

openIdIssuer -> (string)

A string that identifies the type of OIDC service represented by this identity source.

At this time, the only valid value is `cognito` .

identitySourceId -> (string)

The ID of the identity source.

lastUpdatedDate -> (timestamp)

The date and time that the identity source was most recently updated.

policyStoreId -> (string)

The ID of the policy store that contains the identity source.

principalEntityType -> (string)

The data type of principals generated for identities authenticated by this identity source.

configuration -> (tagged union structure)

Contains configuration information about an identity source.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `cognitoUserPoolConfiguration`, `openIdConnectConfiguration`.

cognitoUserPoolConfiguration -> (structure)

Contains configuration details of a Amazon Cognito user pool that Verified Permissions can use as a source of authenticated identities as entities. It specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of a Amazon Cognito user pool, the policy store entity that you want to assign to user groups, and one or more application client IDs.

Example: `"configuration":{"cognitoUserPoolConfiguration":{"userPoolArn":"arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5","clientIds": ["a1b2c3d4e5f6g7h8i9j0kalbmc"],"groupConfiguration": {"groupEntityType": "MyCorp::Group"}}}`

userPoolArn -> (string)

The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Amazon Cognito user pool that contains the identities to be authorized.

Example: `"userPoolArn": "arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5"`

clientIds -> (list)

The unique application client IDs that are associated with the specified Amazon Cognito user pool.

Example: `"clientIds": ["&ExampleCogClientId;"]`

(string)

issuer -> (string)

The OpenID Connect (OIDC) `issuer` ID of the Amazon Cognito user pool that contains the identities to be authorized.

Example: `"issuer": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_1a2b3c4d5"`

groupConfiguration -> (structure)

The type of entity that a policy store maps to groups from an Amazon Cognito user pool identity source.

groupEntityType -> (string)

The name of the schema entity type thatâs mapped to the user pool group. Defaults to `AWS::CognitoGroup` .

openIdConnectConfiguration -> (structure)

Contains configuration details of an OpenID Connect (OIDC) identity provider, or identity source, that Verified Permissions can use to generate entities from authenticated identities. It specifies the issuer URL, token type that you want to use, and policy store entity details.

Example:`"configuration":{"openIdConnectConfiguration":{"issuer":"https://auth.example.com","tokenSelection":{"accessTokenOnly":{"audiences":["https://myapp.example.com","https://myapp2.example.com"],"principalIdClaim":"sub"}},"entityIdPrefix":"MyOIDCProvider","groupConfiguration":{"groupClaim":"groups","groupEntityType":"MyCorp::UserGroup"}}}`

issuer -> (string)

The issuer URL of an OIDC identity provider. This URL must have an OIDC discovery endpoint at the path `.well-known/openid-configuration` .

entityIdPrefix -> (string)

A descriptive string that you want to prefix to user entities from your OIDC identity provider. For example, if you set an `entityIdPrefix` of `MyOIDCProvider` , you can reference principals in your policies in the format `MyCorp::User::MyOIDCProvider|Carlos` .

groupConfiguration -> (structure)

The claim in OIDC identity provider tokens that indicates a userâs group membership, and the entity type that you want to map it to. For example, this object can map the contents of a `groups` claim to `MyCorp::UserGroup` .

groupClaim -> (string)

The token claim that you want Verified Permissions to interpret as group membership. For example, `groups` .

groupEntityType -> (string)

The policy store entity type that you want to map your usersâ group claim to. For example, `MyCorp::UserGroup` . A group entity type is an entity that can have a user entity type as a member.

tokenSelection -> (tagged union structure)

The token type that you want to process from your OIDC identity provider. Your policy store can process either identity (ID) or access tokens from a given OIDC identity source.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `accessTokenOnly`, `identityTokenOnly`.

accessTokenOnly -> (structure)

The OIDC configuration for processing access tokens. Contains allowed audience claims, for example `https://auth.example.com` , and the claim that you want to map to the principal, for example `sub` .

principalIdClaim -> (string)

The claim that determines the principal in OIDC access tokens. For example, `sub` .

audiences -> (list)

The access token `aud` claim values that you want to accept in your policy store. For example, `https://myapp.example.com, https://myapp2.example.com` .

(string)

identityTokenOnly -> (structure)

The OIDC configuration for processing identity (ID) tokens. Contains allowed client ID claims, for example `1example23456789` , and the claim that you want to map to the principal, for example `sub` .

principalIdClaim -> (string)

The claim that determines the principal in OIDC access tokens. For example, `sub` .

clientIds -> (list)

The ID token audience, or client ID, claim values that you want to accept in your policy store from an OIDC identity provider. For example, `1example23456789, 2example10111213` .

(string)