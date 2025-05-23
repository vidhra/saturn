# put-application-grantÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/put-application-grant.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/put-application-grant.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sso-admin](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/index.html#cli-aws-sso-admin) ]

# put-application-grant

## Description

Creates a configuration for an application to use grants. Conceptually grants are authorization to request actions related to tokens. This configuration will be used when parties are requesting and receiving tokens during the trusted identity propagation process. For more information on the IAM Identity Center supported grant workflows, see [SAML 2.0 and OAuth 2.0](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-oauth2.html) .

A grant is created between your applications and Identity Center instance which enables an application to use specified mechanisms to obtain tokens. These tokens are used by your applications to gain access to Amazon Web Services resources on behalf of users. The following elements are within these exchanges:

- **Requester** - The application requesting access to Amazon Web Services resources.
- **Subject** - Typically the user that is requesting access to Amazon Web Services resources.
- **Grant** - Conceptually, a grant is authorization to access Amazon Web Services resources. These grants authorize token generation for authenticating access to the requester and for the request to make requests on behalf of the subjects. There are four types of grants:
- **AuthorizationCode** - Allows an application to request authorization through a series of user-agent redirects.
- **JWT bearer** - Authorizes an application to exchange a JSON Web Token that came from an external identity provider. To learn more, see [RFC 6479](https://datatracker.ietf.org/doc/html/rfc6749) .
- **Refresh token** - Enables application to request new access tokens to replace expiring or expired access tokens.
- **Exchange token** - A grant that requests tokens from the authorization server by providing a âsubjectâ token with access scope authorizing trusted identity propagation to this application. To learn more, see [RFC 8693](https://datatracker.ietf.org/doc/html/rfc8693) .
- **Authorization server** - IAM Identity Center requests tokens.

User credentials are never shared directly within these exchanges. Instead, applications use grants to request access tokens from IAM Identity Center. For more information, see [RFC 6479](https://datatracker.ietf.org/doc/html/rfc6749) .

**Use cases**

- Connecting to custom applications.
- Configuring an Amazon Web Services service to make calls to another Amazon Web Services services using JWT tokens.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sso-admin-2020-07-20/PutApplicationGrant)

## Synopsis

```
put-application-grant
--application-arn <value>
--grant-type <value>
--grant <value>
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

`--application-arn` (string)

Specifies the ARN of the application to update.

`--grant-type` (string)

Specifies the type of grant to update.

Possible values:

- `authorization_code`
- `refresh_token`
- `urn:ietf:params:oauth:grant-type:jwt-bearer`
- `urn:ietf:params:oauth:grant-type:token-exchange`

`--grant` (tagged union structure)

Specifies a structure that describes the grant to update.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `AuthorizationCode`, `JwtBearer`, `RefreshToken`, `TokenExchange`.

AuthorizationCode -> (structure)

Configuration options for the `authorization_code` grant type.

RedirectUris -> (list)

A list of URIs that are valid locations to redirect a userâs browser after the user is authorized.

### Note

RedirectUris is required when the grant type is `authorization_code` .

(string)

JwtBearer -> (structure)

Configuration options for the `urn:ietf:params:oauth:grant-type:jwt-bearer` grant type.

AuthorizedTokenIssuers -> (list)

A list of allowed token issuers trusted by the Identity Center instances for this application.

### Note

`AuthorizedTokenIssuers` is required when the grant type is `JwtBearerGrant` .

(structure)

A structure that describes a trusted token issuer and associates it with a set of authorized audiences.

TrustedTokenIssuerArn -> (string)

The ARN of the trusted token issuer.

AuthorizedAudiences -> (list)

An array list of authorized audiences, or applications, that can consume the tokens generated by the associated trusted token issuer.

(string)

RefreshToken -> (structure)

Configuration options for the `refresh_token` grant type.

TokenExchange -> (structure)

Configuration options for the `urn:ietf:params:oauth:grant-type:token-exchange` grant type.

JSON Syntax:

```
{
  "AuthorizationCode": {
    "RedirectUris": ["string", ...]
  },
  "JwtBearer": {
    "AuthorizedTokenIssuers": [
      {
        "TrustedTokenIssuerArn": "string",
        "AuthorizedAudiences": ["string", ...]
      }
      ...
    ]
  },
  "RefreshToken": {

  },
  "TokenExchange": {

  }
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

## Output

None