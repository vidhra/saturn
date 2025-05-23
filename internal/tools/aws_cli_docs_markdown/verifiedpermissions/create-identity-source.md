# create-identity-sourceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/create-identity-source.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/create-identity-source.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [verifiedpermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/index.html#cli-aws-verifiedpermissions) ]

# create-identity-source

## Description

Adds an identity source to a policy storeâan Amazon Cognito user pool or OpenID Connect (OIDC) identity provider (IdP).

After you create an identity source, you can use the identities provided by the IdP as proxies for the principal in authorization queries that use the [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) or [BatchIsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorizedWithToken.html) API operations. These identities take the form of tokens that contain claims about the user, such as IDs, attributes and group memberships. Identity sources provide identity (ID) tokens and access tokens. Verified Permissions derives information about your user and session from token claims. Access tokens provide action `context` to your policies, and ID tokens provide principal `Attributes` .

### Warning

Tokens from an identity source user continue to be usable until they expire. Token revocation and resource deletion have no effect on the validity of a token in your policy store

### Note

To reference a user from this identity source in your Cedar policies, refer to the following syntax examples.

- Amazon Cognito user pool: `Namespace::[Entity type]::[User pool ID]|[user principal attribute]` , for example `MyCorp::User::us-east-1_EXAMPLE|a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` .
- OpenID Connect (OIDC) provider: `Namespace::[Entity type]::[entityIdPrefix]|[user principal attribute]` , for example `MyCorp::User::MyOIDCProvider|a1b2c3d4-5678-90ab-cdef-EXAMPLE22222` .

### Note

Verified Permissions is * [eventually consistent](https://wikipedia.org/wiki/Eventual_consistency) * . It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/verifiedpermissions-2021-12-01/CreateIdentitySource)

## Synopsis

```
create-identity-source
[--client-token <value>]
--policy-store-id <value>
--configuration <value>
[--principal-entity-type <value>]
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

`--client-token` (string)

Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier) .

If you donât provide this value, then Amazon Web Services generates a random one for you.

If you retry the operation with the same `ClientToken` , but with different parameters, the retry fails with an `ConflictException` error.

Verified Permissions recognizes a `ClientToken` for eight hours. After eight hours, the next request with the same parameters performs the operation again regardless of the value of `ClientToken` .

`--policy-store-id` (string)

Specifies the ID of the policy store in which you want to store this identity source. Only policies and requests made using this policy store can reference identities from the identity provider configured in the new identity source.

`--configuration` (tagged union structure)

Specifies the details required to communicate with the identity provider (IdP) associated with this identity source.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `cognitoUserPoolConfiguration`, `openIdConnectConfiguration`.

cognitoUserPoolConfiguration -> (structure)

Contains configuration details of a Amazon Cognito user pool that Verified Permissions can use as a source of authenticated identities as entities. It specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of a Amazon Cognito user pool and one or more application client IDs.

Example: `"configuration":{"cognitoUserPoolConfiguration":{"userPoolArn":"arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5","clientIds": ["a1b2c3d4e5f6g7h8i9j0kalbmc"],"groupConfiguration": {"groupEntityType": "MyCorp::Group"}}}`

userPoolArn -> (string)

The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Amazon Cognito user pool that contains the identities to be authorized.

Example: `"UserPoolArn": "arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5"`

clientIds -> (list)

The unique application client IDs that are associated with the specified Amazon Cognito user pool.

Example: `"ClientIds": ["&ExampleCogClientId;"]`

(string)

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

JSON Syntax:

```
{
  "cognitoUserPoolConfiguration": {
    "userPoolArn": "string",
    "clientIds": ["string", ...],
    "groupConfiguration": {
      "groupEntityType": "string"
    }
  },
  "openIdConnectConfiguration": {
    "issuer": "string",
    "entityIdPrefix": "string",
    "groupConfiguration": {
      "groupClaim": "string",
      "groupEntityType": "string"
    },
    "tokenSelection": {
      "accessTokenOnly": {
        "principalIdClaim": "string",
        "audiences": ["string", ...]
      },
      "identityTokenOnly": {
        "principalIdClaim": "string",
        "clientIds": ["string", ...]
      }
    }
  }
}
```

`--principal-entity-type` (string)

Specifies the namespace and data type of the principals generated for identities authenticated by the new identity source.

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

**To create an identity source**

The following `create-identity-source` example creates an identity source that lets you reference identities stored in the specified Amazon Cognito user pool. Those identities are available in Verified Permissions as entities of type `User`.

```
aws verifiedpermissions create-identity-source \
    --configuration file://config.txt \
    --principal-entity-type "User" \
    --policy-store-id PSEXAMPLEabcdefg111111
```

Contents of `config.txt`:

```
{
    "cognitoUserPoolConfiguration": {
        "userPoolArn": "arn:aws:cognito-idp:us-west-2:123456789012:userpool/us-west-2_1a2b3c4d5",
        "clientIds":["a1b2c3d4e5f6g7h8i9j0kalbmc"]
    }
}
```

Output:

```
{
    "createdDate": "2023-05-19T20:30:28.214829+00:00",
    "identitySourceId": "ISEXAMPLEabcdefg111111",
    "lastUpdatedDate": "2023-05-19T20:30:28.214829+00:00",
    "policyStoreId": "PSEXAMPLEabcdefg111111"
}
```

For more information about identity sources, see [Using Amazon Verified Permissions with identity providers](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/identity-providers.html) in the *Amazon Verified Permissions User Guide*.

## Output

createdDate -> (timestamp)

The date and time the identity source was originally created.

identitySourceId -> (string)

The unique ID of the new identity source.

lastUpdatedDate -> (timestamp)

The date and time the identity source was most recently updated.

policyStoreId -> (string)

The ID of the policy store that contains the identity source.