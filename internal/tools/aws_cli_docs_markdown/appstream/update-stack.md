# update-stackÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/update-stack.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/update-stack.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appstream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/index.html#cli-aws-appstream) ]

# update-stack

## Description

Updates the specified fields for the specified stack.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/UpdateStack)

## Synopsis

```
update-stack
[--display-name <value>]
[--description <value>]
--name <value>
[--storage-connectors <value>]
[--delete-storage-connectors | --no-delete-storage-connectors]
[--redirect-url <value>]
[--feedback-url <value>]
[--attributes-to-delete <value>]
[--user-settings <value>]
[--application-settings <value>]
[--access-endpoints <value>]
[--embed-host-domains <value>]
[--streaming-experience-settings <value>]
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

`--display-name` (string)

The stack name to display.

`--description` (string)

The description to display.

`--name` (string)

The name of the stack.

`--storage-connectors` (list)

The storage connectors to enable.

(structure)

Describes a connector that enables persistent storage for users.

ConnectorType -> (string)

The type of storage connector.

ResourceIdentifier -> (string)

The ARN of the storage connector.

Domains -> (list)

The names of the domains for the account.

(string)

GSuite domain for GDrive integration.

DomainsRequireAdminConsent -> (list)

The OneDrive for Business domains where you require admin consent when users try to link their OneDrive account to AppStream 2.0. The attribute can only be specified when ConnectorType=ONE_DRIVE.

(string)

GSuite domain for GDrive integration.

Shorthand Syntax:

```
ConnectorType=string,ResourceIdentifier=string,Domains=string,string,DomainsRequireAdminConsent=string,string ...
```

JSON Syntax:

```
[
  {
    "ConnectorType": "HOMEFOLDERS"|"GOOGLE_DRIVE"|"ONE_DRIVE",
    "ResourceIdentifier": "string",
    "Domains": ["string", ...],
    "DomainsRequireAdminConsent": ["string", ...]
  }
  ...
]
```

`--delete-storage-connectors` | `--no-delete-storage-connectors` (boolean)

Deletes the storage connectors currently enabled for the stack.

`--redirect-url` (string)

The URL that users are redirected to after their streaming session ends.

`--feedback-url` (string)

The URL that users are redirected to after they choose the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.

`--attributes-to-delete` (list)

The stack attributes to delete.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  STORAGE_CONNECTORS
  STORAGE_CONNECTOR_HOMEFOLDERS
  STORAGE_CONNECTOR_GOOGLE_DRIVE
  STORAGE_CONNECTOR_ONE_DRIVE
  REDIRECT_URL
  FEEDBACK_URL
  THEME_NAME
  USER_SETTINGS
  EMBED_HOST_DOMAINS
  IAM_ROLE_ARN
  ACCESS_ENDPOINTS
  STREAMING_EXPERIENCE_SETTINGS
```

`--user-settings` (list)

The actions that are enabled or disabled for users during their streaming sessions. By default, these actions are enabled.

(structure)

Describes an action and whether the action is enabled or disabled for users during their streaming sessions.

Action -> (string)

The action that is enabled or disabled.

Permission -> (string)

Indicates whether the action is enabled or disabled.

MaximumLength -> (integer)

Specifies the number of characters that can be copied by end users from the local device to the remote session, and to the local device from the remote session.

This can be specified only for the `CLIPBOARD_COPY_FROM_LOCAL_DEVICE` and `CLIPBOARD_COPY_TO_LOCAL_DEVICE` actions.

This defaults to 20,971,520 (20 MB) when unspecified and the permission is `ENABLED` . This canât be specified when the permission is `DISABLED` .

The value can be between 1 and 20,971,520 (20 MB).

Shorthand Syntax:

```
Action=string,Permission=string,MaximumLength=integer ...
```

JSON Syntax:

```
[
  {
    "Action": "CLIPBOARD_COPY_FROM_LOCAL_DEVICE"|"CLIPBOARD_COPY_TO_LOCAL_DEVICE"|"FILE_UPLOAD"|"FILE_DOWNLOAD"|"PRINTING_TO_LOCAL_DEVICE"|"DOMAIN_PASSWORD_SIGNIN"|"DOMAIN_SMART_CARD_SIGNIN"|"AUTO_TIME_ZONE_REDIRECTION",
    "Permission": "ENABLED"|"DISABLED",
    "MaximumLength": integer
  }
  ...
]
```

`--application-settings` (structure)

The persistent application settings for users of a stack. When these settings are enabled, changes that users make to applications and Windows settings are automatically saved after each session and applied to the next session.

Enabled -> (boolean)

Enables or disables persistent application settings for users during their streaming sessions.

SettingsGroup -> (string)

The path prefix for the S3 bucket where usersâ persistent application settings are stored. You can allow the same persistent application settings to be used across multiple stacks by specifying the same settings group for each stack.

Shorthand Syntax:

```
Enabled=boolean,SettingsGroup=string
```

JSON Syntax:

```
{
  "Enabled": true|false,
  "SettingsGroup": "string"
}
```

`--access-endpoints` (list)

The list of interface VPC endpoint (interface endpoint) objects. Users of the stack can connect to AppStream 2.0 only through the specified endpoints.

(structure)

Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.

EndpointType -> (string)

The type of interface endpoint.

VpceId -> (string)

The identifier (ID) of the VPC in which the interface endpoint is used.

Shorthand Syntax:

```
EndpointType=string,VpceId=string ...
```

JSON Syntax:

```
[
  {
    "EndpointType": "STREAMING",
    "VpceId": "string"
  }
  ...
]
```

`--embed-host-domains` (list)

The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded AppStream 2.0 streaming sessions.

(string)

Specifies a valid domain that can embed AppStream. Valid examples include: [âtestorigin.ttâcomâ, âtestingorigin.com.usâ, âtest.com.usâ] Invalid examples include: [âtest,comâ, â.comâ, âh*llo.comâ. ââ]

Syntax:

```
"string" "string" ...
```

`--streaming-experience-settings` (structure)

The streaming protocol you want your stack to prefer. This can be UDP or TCP. Currently, UDP is only supported in the Windows native client.

PreferredProtocol -> (string)

The preferred protocol that you want to use while streaming your application.

Shorthand Syntax:

```
PreferredProtocol=string
```

JSON Syntax:

```
{
  "PreferredProtocol": "TCP"|"UDP"
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

Stack -> (structure)

Information about the stack.

Arn -> (string)

The ARN of the stack.

Name -> (string)

The name of the stack.

Description -> (string)

The description to display.

DisplayName -> (string)

The stack name to display.

CreatedTime -> (timestamp)

The time the stack was created.

StorageConnectors -> (list)

The storage connectors to enable.

(structure)

Describes a connector that enables persistent storage for users.

ConnectorType -> (string)

The type of storage connector.

ResourceIdentifier -> (string)

The ARN of the storage connector.

Domains -> (list)

The names of the domains for the account.

(string)

GSuite domain for GDrive integration.

DomainsRequireAdminConsent -> (list)

The OneDrive for Business domains where you require admin consent when users try to link their OneDrive account to AppStream 2.0. The attribute can only be specified when ConnectorType=ONE_DRIVE.

(string)

GSuite domain for GDrive integration.

RedirectURL -> (string)

The URL that users are redirected to after their streaming session ends.

FeedbackURL -> (string)

The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.

StackErrors -> (list)

The errors for the stack.

(structure)

Describes a stack error.

ErrorCode -> (string)

The error code.

ErrorMessage -> (string)

The error message.

UserSettings -> (list)

The actions that are enabled or disabled for users during their streaming sessions. By default these actions are enabled.

(structure)

Describes an action and whether the action is enabled or disabled for users during their streaming sessions.

Action -> (string)

The action that is enabled or disabled.

Permission -> (string)

Indicates whether the action is enabled or disabled.

MaximumLength -> (integer)

Specifies the number of characters that can be copied by end users from the local device to the remote session, and to the local device from the remote session.

This can be specified only for the `CLIPBOARD_COPY_FROM_LOCAL_DEVICE` and `CLIPBOARD_COPY_TO_LOCAL_DEVICE` actions.

This defaults to 20,971,520 (20 MB) when unspecified and the permission is `ENABLED` . This canât be specified when the permission is `DISABLED` .

The value can be between 1 and 20,971,520 (20 MB).

ApplicationSettings -> (structure)

The persistent application settings for users of the stack.

Enabled -> (boolean)

Specifies whether persistent application settings are enabled for users during their streaming sessions.

SettingsGroup -> (string)

The path prefix for the S3 bucket where usersâ persistent application settings are stored.

S3BucketName -> (string)

The S3 bucket where usersâ persistent application settings are stored. When persistent application settings are enabled for the first time for an account in an AWS Region, an S3 bucket is created. The bucket is unique to the AWS account and the Region.

AccessEndpoints -> (list)

The list of virtual private cloud (VPC) interface endpoint objects. Users of the stack can connect to AppStream 2.0 only through the specified endpoints.

(structure)

Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.

EndpointType -> (string)

The type of interface endpoint.

VpceId -> (string)

The identifier (ID) of the VPC in which the interface endpoint is used.

EmbedHostDomains -> (list)

The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded AppStream 2.0 streaming sessions.

(string)

Specifies a valid domain that can embed AppStream. Valid examples include: [âtestorigin.ttâcomâ, âtestingorigin.com.usâ, âtest.com.usâ] Invalid examples include: [âtest,comâ, â.comâ, âh*llo.comâ. ââ]

StreamingExperienceSettings -> (structure)

The streaming protocol you want your stack to prefer. This can be UDP or TCP. Currently, UDP is only supported in the Windows native client.

PreferredProtocol -> (string)

The preferred protocol that you want to use while streaming your application.