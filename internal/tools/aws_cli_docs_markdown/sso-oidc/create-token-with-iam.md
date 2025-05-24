# create-token-with-iamÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-oidc/create-token-with-iam.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-oidc/create-token-with-iam.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sso-oidc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-oidc/index.html#cli-aws-sso-oidc) ]

# create-token-with-iam

## Description

Creates and returns access and refresh tokens for clients and applications that are authenticated using IAM entities. The access token can be used to fetch short-lived credentials for the assigned Amazon Web Services accounts or to access application APIs using `bearer` authentication.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sso-oidc-2019-06-10/CreateTokenWithIAM)

## Synopsis

```
create-token-with-iam
--client-id <value>
--grant-type <value>
[--code <value>]
[--refresh-token <value>]
[--assertion <value>]
[--scope <value>]
[--redirect-uri <value>]
[--subject-token <value>]
[--subject-token-type <value>]
[--requested-token-type <value>]
[--code-verifier <value>]
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

`--client-id` (string)

The unique identifier string for the client or application. This value is an application ARN that has OAuth grants configured.

`--grant-type` (string)

Supports the following OAuth grant types: Authorization Code, Refresh Token, JWT Bearer, and Token Exchange. Specify one of the following values, depending on the grant type that you want:

- Authorization Code - `authorization_code`
- Refresh Token - `refresh_token`
- JWT Bearer - `urn:ietf:params:oauth:grant-type:jwt-bearer`
- Token Exchange - `urn:ietf:params:oauth:grant-type:token-exchange`

`--code` (string)

Used only when calling this API for the Authorization Code grant type. This short-lived code is used to identify this authorization request. The code is obtained through a redirect from IAM Identity Center to a redirect URI persisted in the Authorization Code GrantOptions for the application.

`--refresh-token` (string)

Used only when calling this API for the Refresh Token grant type. This token is used to refresh short-lived tokens, such as the access token, that might expire.

For more information about the features and limitations of the current IAM Identity Center OIDC implementation, see *Considerations for Using this Guide* in the [IAM Identity Center OIDC API Reference](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/Welcome.html) .

`--assertion` (string)

Used only when calling this API for the JWT Bearer grant type. This value specifies the JSON Web Token (JWT) issued by a trusted token issuer. To authorize a trusted token issuer, configure the JWT Bearer GrantOptions for the application.

`--scope` (list)

The list of scopes for which authorization is requested. The access token that is issued is limited to the scopes that are granted. If the value is not specified, IAM Identity Center authorizes all scopes configured for the application, including the following default scopes: `openid` , `aws` , `sts:identity_context` .

(string)

Syntax:

```
"string" "string" ...
```

`--redirect-uri` (string)

Used only when calling this API for the Authorization Code grant type. This value specifies the location of the client or application that has registered to receive the authorization code.

`--subject-token` (string)

Used only when calling this API for the Token Exchange grant type. This value specifies the subject of the exchange. The value of the subject token must be an access token issued by IAM Identity Center to a different client or application. The access token must have authorized scopes that indicate the requested application as a target audience.

`--subject-token-type` (string)

Used only when calling this API for the Token Exchange grant type. This value specifies the type of token that is passed as the subject of the exchange. The following value is supported:

- Access Token - `urn:ietf:params:oauth:token-type:access_token`

`--requested-token-type` (string)

Used only when calling this API for the Token Exchange grant type. This value specifies the type of token that the requester can receive. The following values are supported:

- Access Token - `urn:ietf:params:oauth:token-type:access_token`
- Refresh Token - `urn:ietf:params:oauth:token-type:refresh_token`

`--code-verifier` (string)

Used only when calling this API for the Authorization Code grant type. This value is generated by the client and presented to validate the original code challenge value the client passed at authorization time.

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

## Output

accessToken -> (string)

A bearer token to access Amazon Web Services accounts and applications assigned to a user.

tokenType -> (string)

Used to notify the requester that the returned token is an access token. The supported token type is `Bearer` .

expiresIn -> (integer)

Indicates the time in seconds when an access token will expire.

refreshToken -> (string)

A token that, if present, can be used to refresh a previously issued access token that might have expired.

For more information about the features and limitations of the current IAM Identity Center OIDC implementation, see *Considerations for Using this Guide* in the [IAM Identity Center OIDC API Reference](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/Welcome.html) .

idToken -> (string)

A JSON Web Token (JWT) that identifies the user associated with the issued access token.

issuedTokenType -> (string)

Indicates the type of tokens that are issued by IAM Identity Center. The following values are supported:

- Access Token - `urn:ietf:params:oauth:token-type:access_token`
- Refresh Token - `urn:ietf:params:oauth:token-type:refresh_token`

scope -> (list)

The list of scopes for which authorization is granted. The access token that is issued is limited to the scopes that are granted.

(string)

awsAdditionalDetails -> (structure)

A structure containing information from the `idToken` . Only the `identityContext` is in it, which is a value extracted from the `idToken` . This provides direct access to identity information without requiring JWT parsing.

identityContext -> (string)

STS context assertion that carries a user identifier to the Amazon Web Services service that it calls and can be used to obtain an identity-enhanced IAM role session. This value corresponds to the `sts:identity_context` claim in the ID token.