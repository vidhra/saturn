# update-portalÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces-web/update-portal.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces-web/update-portal.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workspaces-web](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces-web/index.html#cli-aws-workspaces-web) ]

# update-portal

## Description

Updates a web portal.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workspaces-web-2020-07-08/UpdatePortal)

## Synopsis

```
update-portal
[--authentication-type <value>]
[--display-name <value>]
[--instance-type <value>]
[--max-concurrent-sessions <value>]
--portal-arn <value>
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

`--authentication-type` (string)

The type of authentication integration points used when signing into the web portal. Defaults to `Standard` .

`Standard` web portals are authenticated directly through your identity provider. You need to call `CreateIdentityProvider` to integrate your identity provider with your web portal. User and group access to your web portal is controlled through your identity provider.

`IAM Identity Center` web portals are authenticated through IAM Identity Center. Identity sources (including external identity provider integration), plus user and group access to your web portal, can be configured in the IAM Identity Center.

Possible values:

- `Standard`
- `IAM_Identity_Center`

`--display-name` (string)

The name of the web portal. This is not visible to users who log into the web portal.

`--instance-type` (string)

The type and resources of the underlying instance.

Possible values:

- `standard.regular`
- `standard.large`
- `standard.xlarge`

`--max-concurrent-sessions` (integer)

The maximum number of concurrent sessions for the portal.

`--portal-arn` (string)

The ARN of the web portal.

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

portal -> (structure)

The web portal.

additionalEncryptionContext -> (map)

The additional encryption context of the portal.

key -> (string)

value -> (string)

authenticationType -> (string)

The type of authentication integration points used when signing into the web portal. Defaults to `Standard` .

`Standard` web portals are authenticated directly through your identity provider. You need to call `CreateIdentityProvider` to integrate your identity provider with your web portal. User and group access to your web portal is controlled through your identity provider.

`IAM Identity Center` web portals are authenticated through IAM Identity Center. Identity sources (including external identity provider integration), plus user and group access to your web portal, can be configured in the IAM Identity Center.

browserSettingsArn -> (string)

The ARN of the browser settings that is associated with this web portal.

browserType -> (string)

The browser that users see when using a streaming session.

creationDate -> (timestamp)

The creation date of the web portal.

customerManagedKey -> (string)

The customer managed key used to encrypt sensitive information in the portal.

dataProtectionSettingsArn -> (string)

The ARN of the data protection settings.

displayName -> (string)

The name of the web portal.

instanceType -> (string)

The type and resources of the underlying instance.

ipAccessSettingsArn -> (string)

The ARN of the IP access settings.

maxConcurrentSessions -> (integer)

The maximum number of concurrent sessions for the portal.

networkSettingsArn -> (string)

The ARN of the network settings that is associated with the web portal.

portalArn -> (string)

The ARN of the web portal.

portalEndpoint -> (string)

The endpoint URL of the web portal that users access in order to start streaming sessions.

portalStatus -> (string)

The status of the web portal.

rendererType -> (string)

The renderer that is used in streaming sessions.

statusReason -> (string)

A message that explains why the web portal is in its current status.

trustStoreArn -> (string)

The ARN of the trust store that is associated with the web portal.

userAccessLoggingSettingsArn -> (string)

The ARN of the user access logging settings that is associated with the web portal.

userSettingsArn -> (string)

The ARN of the user settings that is associated with the web portal.