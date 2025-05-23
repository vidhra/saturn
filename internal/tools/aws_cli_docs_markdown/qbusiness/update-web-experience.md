# update-web-experienceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/update-web-experience.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/update-web-experience.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qbusiness](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/index.html#cli-aws-qbusiness) ]

# update-web-experience

## Description

Updates an Amazon Q Business web experience.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qbusiness-2023-11-27/UpdateWebExperience)

## Synopsis

```
update-web-experience
--application-id <value>
--web-experience-id <value>
[--role-arn <value>]
[--authentication-configuration <value>]
[--title <value>]
[--subtitle <value>]
[--welcome-message <value>]
[--sample-prompts-control-mode <value>]
[--identity-provider-configuration <value>]
[--origins <value>]
[--browser-extension-configuration <value>]
[--customization-configuration <value>]
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

`--application-id` (string)

The identifier of the Amazon Q Business application attached to the web experience.

`--web-experience-id` (string)

The identifier of the Amazon Q Business web experience.

`--role-arn` (string)

The Amazon Resource Name (ARN) of the role with permission to access the Amazon Q Business web experience and required resources.

`--authentication-configuration` (tagged union structure)

The authentication configuration of the Amazon Q Business web experience.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `samlConfiguration`.

samlConfiguration -> (structure)

Provides the SAML 2.0 compliant identity provider (IdP) configuration information Amazon Q Business needs to deploy a Amazon Q Business web experience.

metadataXML -> (string)

The metadata XML that your IdP generated.

roleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role assumed by users when they authenticate into their Amazon Q Business web experience, containing the relevant Amazon Q Business permissions for conversing with Amazon Q Business.

userIdAttribute -> (string)

The user attribute name in your IdP that maps to the user email.

userGroupAttribute -> (string)

The group attribute name in your IdP that maps to user groups.

Shorthand Syntax:

```
samlConfiguration={metadataXML=string,roleArn=string,userIdAttribute=string,userGroupAttribute=string}
```

JSON Syntax:

```
{
  "samlConfiguration": {
    "metadataXML": "string",
    "roleArn": "string",
    "userIdAttribute": "string",
    "userGroupAttribute": "string"
  }
}
```

`--title` (string)

The title of the Amazon Q Business web experience.

`--subtitle` (string)

The subtitle of the Amazon Q Business web experience.

`--welcome-message` (string)

A customized welcome message for an end user in an Amazon Q Business web experience.

`--sample-prompts-control-mode` (string)

Determines whether sample prompts are enabled in the web experience for an end user.

Possible values:

- `ENABLED`
- `DISABLED`

`--identity-provider-configuration` (tagged union structure)

Information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `samlConfiguration`, `openIDConnectConfiguration`.

samlConfiguration -> (structure)

Information about the SAML 2.0-compliant identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.

authenticationUrl -> (string)

The URL where Amazon Q Business end users will be redirected for authentication.

openIDConnectConfiguration -> (structure)

Information about the OIDC-compliant identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.

secretsArn -> (string)

The Amazon Resource Name (ARN) of a Secrets Manager secret containing the OIDC client secret.

secretsRole -> (string)

An IAM role with permissions to access KMS to decrypt the Secrets Manager secret containing your OIDC client secret.

Shorthand Syntax:

```
samlConfiguration={authenticationUrl=string},openIDConnectConfiguration={secretsArn=string,secretsRole=string}
```

JSON Syntax:

```
{
  "samlConfiguration": {
    "authenticationUrl": "string"
  },
  "openIDConnectConfiguration": {
    "secretsArn": "string",
    "secretsRole": "string"
  }
}
```

`--origins` (list)

Updates the website domain origins that are allowed to embed the Amazon Q Business web experience. The *domain origin* refers to the *base URL* for accessing a website including the protocol (`http/https` ), the domain name, and the port number (if specified).

### Note

- Any values except `null` submitted as part of this update will replace all previous values.
- You must only submit a *base URL* and not a full path. For example, `https://docs.aws.amazon.com` .

(string)

Syntax:

```
"string" "string" ...
```

`--browser-extension-configuration` (structure)

The browser extension configuration for an Amazon Q Business web experience.

### Note

For Amazon Q Business application using external OIDC-compliant identity providers (IdPs). The IdP administrator must add the browser extension sign-in redirect URLs to the IdP application. For more information, see [Configure external OIDC identity provider for your browser extensions.](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/browser-extensions.html) .

enabledBrowserExtensions -> (list)

Specify the browser extensions allowed for your Amazon Q web experience.

- `CHROME` â Enables the extension for Chromium-based browsers (Google Chrome, Microsoft Edge, Opera, etc.).
- `FIREFOX` â Enables the extension for Mozilla Firefox.
- `CHROME` and `FIREFOX` â Enable the extension for Chromium-based browsers and Mozilla Firefox.

(string)

Shorthand Syntax:

```
enabledBrowserExtensions=string,string
```

JSON Syntax:

```
{
  "enabledBrowserExtensions": ["FIREFOX"|"CHROME", ...]
}
```

`--customization-configuration` (structure)

Updates the custom logo, favicon, font, and color used in the Amazon Q web experience.

customCSSUrl -> (string)

Provides the URL where the custom CSS file is hosted for an Amazon Q web experience.

logoUrl -> (string)

Provides the URL where the custom logo file is hosted for an Amazon Q web experience.

fontUrl -> (string)

Provides the URL where the custom font file is hosted for an Amazon Q web experience.

faviconUrl -> (string)

Provides the URL where the custom favicon file is hosted for an Amazon Q web experience.

Shorthand Syntax:

```
customCSSUrl=string,logoUrl=string,fontUrl=string,faviconUrl=string
```

JSON Syntax:

```
{
  "customCSSUrl": "string",
  "logoUrl": "string",
  "fontUrl": "string",
  "faviconUrl": "string"
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