# create-identity-poolÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/create-identity-pool.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/create-identity-pool.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cognito-identity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/index.html#cli-aws-cognito-identity) ]

# create-identity-pool

## Description

Creates a new identity pool. The identity pool is a store of user identity information that is specific to your Amazon Web Services account. The keys for `SupportedLoginProviders` are as follows:

- Facebook: `graph.facebook.com`
- Google: `accounts.google.com`
- Sign in With Apple: `appleid.apple.com`
- Amazon: `www.amazon.com`
- Twitter: `api.twitter.com`
- Digits: `www.digits.com`

### Warning

If you donât provide a value for a parameter, Amazon Cognito sets it to its default value.

You must use Amazon Web Services developer credentials to call this operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cognito-identity-2014-06-30/CreateIdentityPool)

## Synopsis

```
create-identity-pool
--identity-pool-name <value>
--allow-unauthenticated-identities | --no-allow-unauthenticated-identities
[--allow-classic-flow | --no-allow-classic-flow]
[--supported-login-providers <value>]
[--developer-provider-name <value>]
[--open-id-connect-provider-arns <value>]
[--cognito-identity-providers <value>]
[--saml-provider-arns <value>]
[--identity-pool-tags <value>]
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

`--identity-pool-name` (string)

A string that you provide.

`--allow-unauthenticated-identities` | `--no-allow-unauthenticated-identities` (boolean)

TRUE if the identity pool supports unauthenticated logins.

`--allow-classic-flow` | `--no-allow-classic-flow` (boolean)

Enables or disables the Basic (Classic) authentication flow. For more information, see [Identity Pools (Federated Identities) Authentication Flow](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html) in the *Amazon Cognito Developer Guide* .

`--supported-login-providers` (map)

Optional key:value pairs mapping provider names to provider app IDs.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--developer-provider-name` (string)

The âdomainâ by which Cognito will refer to your users. This name acts as a placeholder that allows your backend and the Cognito service to communicate about the developer provider. For the `DeveloperProviderName` , you can use letters as well as period (`.` ), underscore (`_` ), and dash (`-` ).

Once you have set a developer provider name, you cannot change it. Please take care in setting this parameter.

`--open-id-connect-provider-arns` (list)

The Amazon Resource Names (ARN) of the OpenID Connect providers.

(string)

Syntax:

```
"string" "string" ...
```

`--cognito-identity-providers` (list)

An array of Amazon Cognito user pools and their client IDs.

(structure)

A provider representing an Amazon Cognito user pool and its client ID.

ProviderName -> (string)

The provider name for an Amazon Cognito user pool. For example, `cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789` .

ClientId -> (string)

The client ID for the Amazon Cognito user pool.

ServerSideTokenCheck -> (boolean)

TRUE if server-side token validation is enabled for the identity providerâs token.

Once you set `ServerSideTokenCheck` to TRUE for an identity pool, that identity pool will check with the integrated user pools to make sure that the user has not been globally signed out or deleted before the identity pool provides an OIDC token or Amazon Web Services credentials for the user.

If the user is signed out or deleted, the identity pool will return a 400 Not Authorized error.

Shorthand Syntax:

```
ProviderName=string,ClientId=string,ServerSideTokenCheck=boolean ...
```

JSON Syntax:

```
[
  {
    "ProviderName": "string",
    "ClientId": "string",
    "ServerSideTokenCheck": true|false
  }
  ...
]
```

`--saml-provider-arns` (list)

An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.

(string)

Syntax:

```
"string" "string" ...
```

`--identity-pool-tags` (map)

Tags to assign to the identity pool. A tag is a label that you can apply to identity pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

**To create an identity pool with Cognito identity pool provider**

This example creates an identity pool named MyIdentityPool. It has a Cognito identity pool provider.
Unauthenticated identities are not allowed.

Command:

```
aws cognito-identity create-identity-pool --identity-pool-name MyIdentityPool --no-allow-unauthenticated-identities --cognito-identity-providers ProviderName="cognito-idp.us-west-2.amazonaws.com/us-west-2_aaaaaaaaa",ClientId="3n4b5urk1ft4fl3mg5e62d9ado",ServerSideTokenCheck=false
```

Output:

```
{
  "IdentityPoolId": "us-west-2:11111111-1111-1111-1111-111111111111",
  "IdentityPoolName": "MyIdentityPool",
  "AllowUnauthenticatedIdentities": false,
  "CognitoIdentityProviders": [
      {
          "ProviderName": "cognito-idp.us-west-2.amazonaws.com/us-west-2_111111111",
          "ClientId": "3n4b5urk1ft4fl3mg5e62d9ado",
          "ServerSideTokenCheck": false
      }
  ]
}
```

## Output

IdentityPoolId -> (string)

An identity pool ID in the format REGION:GUID.

IdentityPoolName -> (string)

A string that you provide.

AllowUnauthenticatedIdentities -> (boolean)

TRUE if the identity pool supports unauthenticated logins.

AllowClassicFlow -> (boolean)

Enables or disables the Basic (Classic) authentication flow. For more information, see [Identity Pools (Federated Identities) Authentication Flow](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html) in the *Amazon Cognito Developer Guide* .

SupportedLoginProviders -> (map)

Optional key:value pairs mapping provider names to provider app IDs.

key -> (string)

value -> (string)

DeveloperProviderName -> (string)

The âdomainâ by which Cognito will refer to your users.

OpenIdConnectProviderARNs -> (list)

The ARNs of the OpenID Connect providers.

(string)

CognitoIdentityProviders -> (list)

A list representing an Amazon Cognito user pool and its client ID.

(structure)

A provider representing an Amazon Cognito user pool and its client ID.

ProviderName -> (string)

The provider name for an Amazon Cognito user pool. For example, `cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789` .

ClientId -> (string)

The client ID for the Amazon Cognito user pool.

ServerSideTokenCheck -> (boolean)

TRUE if server-side token validation is enabled for the identity providerâs token.

Once you set `ServerSideTokenCheck` to TRUE for an identity pool, that identity pool will check with the integrated user pools to make sure that the user has not been globally signed out or deleted before the identity pool provides an OIDC token or Amazon Web Services credentials for the user.

If the user is signed out or deleted, the identity pool will return a 400 Not Authorized error.

SamlProviderARNs -> (list)

An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.

(string)

IdentityPoolTags -> (map)

The tags that are assigned to the identity pool. A tag is a label that you can apply to identity pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.

key -> (string)

value -> (string)