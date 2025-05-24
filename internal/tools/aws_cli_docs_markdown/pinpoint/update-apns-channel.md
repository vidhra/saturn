# update-apns-channelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-apns-channel.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-apns-channel.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/index.html#cli-aws-pinpoint) ]

# update-apns-channel

## Description

Enables the APNs channel for an application or updates the status and settings of the APNs channel for an application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/UpdateApnsChannel)

## Synopsis

```
update-apns-channel
--apns-channel-request <value>
--application-id <value>
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

`--apns-channel-request` (structure)

Specifies the status and settings of the APNs (Apple Push Notification service) channel for an application.

BundleId -> (string)

The bundle identifier thatâs assigned to your iOS app. This identifier is used for APNs tokens.

Certificate -> (string)

The APNs client certificate that you received from Apple, if you want Amazon Pinpoint to communicate with APNs by using an APNs certificate.

DefaultAuthenticationMethod -> (string)

The default authentication method that you want Amazon Pinpoint to use when authenticating with APNs, key or certificate.

Enabled -> (boolean)

Specifies whether to enable the APNs channel for the application.

PrivateKey -> (string)

The private key for the APNs client certificate that you want Amazon Pinpoint to use to communicate with APNs.

TeamId -> (string)

The identifier thatâs assigned to your Apple developer account team. This identifier is used for APNs tokens.

TokenKey -> (string)

The authentication key to use for APNs tokens.

TokenKeyId -> (string)

The key identifier thatâs assigned to your APNs signing key, if you want Amazon Pinpoint to communicate with APNs by using APNs tokens.

Shorthand Syntax:

```
BundleId=string,Certificate=string,DefaultAuthenticationMethod=string,Enabled=boolean,PrivateKey=string,TeamId=string,TokenKey=string,TokenKeyId=string
```

JSON Syntax:

```
{
  "BundleId": "string",
  "Certificate": "string",
  "DefaultAuthenticationMethod": "string",
  "Enabled": true|false,
  "PrivateKey": "string",
  "TeamId": "string",
  "TokenKey": "string",
  "TokenKeyId": "string"
}
```

`--application-id` (string)

The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console.

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

APNSChannelResponse -> (structure)

Provides information about the status and settings of the APNs (Apple Push Notification service) channel for an application.

ApplicationId -> (string)

The unique identifier for the application that the APNs channel applies to.

CreationDate -> (string)

The date and time when the APNs channel was enabled.

DefaultAuthenticationMethod -> (string)

The default authentication method that Amazon Pinpoint uses to authenticate with APNs for this channel, key or certificate.

Enabled -> (boolean)

Specifies whether the APNs channel is enabled for the application.

HasCredential -> (boolean)

(Not used) This property is retained only for backward compatibility.

HasTokenKey -> (boolean)

Specifies whether the APNs channel is configured to communicate with APNs by using APNs tokens. To provide an authentication key for APNs tokens, set the TokenKey property of the channel.

Id -> (string)

(Deprecated) An identifier for the APNs channel. This property is retained only for backward compatibility.

IsArchived -> (boolean)

Specifies whether the APNs channel is archived.

LastModifiedBy -> (string)

The user who last modified the APNs channel.

LastModifiedDate -> (string)

The date and time when the APNs channel was last modified.

Platform -> (string)

The type of messaging or notification platform for the channel. For the APNs channel, this value is APNS.

Version -> (integer)

The current version of the APNs channel.