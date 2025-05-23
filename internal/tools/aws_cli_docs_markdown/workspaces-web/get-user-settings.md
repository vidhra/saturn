# get-user-settingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces-web/get-user-settings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces-web/get-user-settings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workspaces-web](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces-web/index.html#cli-aws-workspaces-web) ]

# get-user-settings

## Description

Gets user settings.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workspaces-web-2020-07-08/GetUserSettings)

## Synopsis

```
get-user-settings
--user-settings-arn <value>
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

`--user-settings-arn` (string)

The ARN of the user settings.

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

userSettings -> (structure)

The user settings.

additionalEncryptionContext -> (map)

The additional encryption context of the user settings.

key -> (string)

value -> (string)

associatedPortalArns -> (list)

A list of web portal ARNs that this user settings is associated with.

(string)

cookieSynchronizationConfiguration -> (structure)

The configuration that specifies which cookies should be synchronized from the end userâs local browser to the remote browser.

allowlist -> (list)

The list of cookie specifications that are allowed to be synchronized to the remote browser.

(structure)

Specifies a single cookie or set of cookies in an end userâs browser.

domain -> (string)

The domain of the cookie.

name -> (string)

The name of the cookie.

path -> (string)

The path of the cookie.

blocklist -> (list)

The list of cookie specifications that are blocked from being synchronized to the remote browser.

(structure)

Specifies a single cookie or set of cookies in an end userâs browser.

domain -> (string)

The domain of the cookie.

name -> (string)

The name of the cookie.

path -> (string)

The path of the cookie.

copyAllowed -> (string)

Specifies whether the user can copy text from the streaming session to the local device.

customerManagedKey -> (string)

The customer managed key used to encrypt sensitive information in the user settings.

deepLinkAllowed -> (string)

Specifies whether the user can use deep links that open automatically when connecting to a session.

disconnectTimeoutInMinutes -> (integer)

The amount of time that a streaming session remains active after users disconnect.

downloadAllowed -> (string)

Specifies whether the user can download files from the streaming session to the local device.

idleDisconnectTimeoutInMinutes -> (integer)

The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.

pasteAllowed -> (string)

Specifies whether the user can paste text from the local device to the streaming session.

printAllowed -> (string)

Specifies whether the user can print to the local device.

toolbarConfiguration -> (structure)

The configuration of the toolbar. This allows administrators to select the toolbar type and visual mode, set maximum display resolution for sessions, and choose which items are visible to end users during their sessions. If administrators do not modify these settings, end users retain control over their toolbar preferences.

hiddenToolbarItems -> (list)

The list of toolbar items to be hidden.

(string)

maxDisplayResolution -> (string)

The maximum display resolution that is allowed for the session.

toolbarType -> (string)

The type of toolbar displayed during the session.

visualMode -> (string)

The visual mode of the toolbar.

uploadAllowed -> (string)

Specifies whether the user can upload files from the local device to the streaming session.

userSettingsArn -> (string)

The ARN of the user settings.