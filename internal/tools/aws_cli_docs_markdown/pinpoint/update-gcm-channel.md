# update-gcm-channelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-gcm-channel.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-gcm-channel.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/index.html#cli-aws-pinpoint) ]

# update-gcm-channel

## Description

Enables the GCM channel for an application or updates the status and settings of the GCM channel for an application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/UpdateGcmChannel)

## Synopsis

```
update-gcm-channel
--application-id <value>
--gcm-channel-request <value>
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

The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console.

`--gcm-channel-request` (structure)

Specifies the status and settings of the GCM channel for an application. This channel enables Amazon Pinpoint to send push notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service.

ApiKey -> (string)

The Web API Key, also referred to as an *API_KEY* or *server key* , that you received from Google to communicate with Google services.

DefaultAuthenticationMethod -> (string)

The default authentication method used for GCM. Values are either âTOKENâ or âKEYâ. Defaults to âKEYâ.

Enabled -> (boolean)

Specifies whether to enable the GCM channel for the application.

ServiceJson -> (string)

The contents of the JSON file provided by Google during registration in order to generate an access token for authentication. For more information see [Migrate from legacy FCM APIs to HTTP v1](https://firebase.google.com/docs/cloud-messaging/migrate-v1) .

Shorthand Syntax:

```
ApiKey=string,DefaultAuthenticationMethod=string,Enabled=boolean,ServiceJson=string
```

JSON Syntax:

```
{
  "ApiKey": "string",
  "DefaultAuthenticationMethod": "string",
  "Enabled": true|false,
  "ServiceJson": "string"
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

GCMChannelResponse -> (structure)

Provides information about the status and settings of the GCM channel for an application. The GCM channel enables Amazon Pinpoint to send push notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service.

ApplicationId -> (string)

The unique identifier for the application that the GCM channel applies to.

CreationDate -> (string)

The date and time when the GCM channel was enabled.

Credential -> (string)

The Web API Key, also referred to as an *API_KEY* or *server key* , that you received from Google to communicate with Google services.

DefaultAuthenticationMethod -> (string)

The default authentication method used for GCM. Values are either âTOKENâ or âKEYâ. Defaults to âKEYâ.

Enabled -> (boolean)

Specifies whether the GCM channel is enabled for the application.

HasCredential -> (boolean)

(Not used) This property is retained only for backward compatibility.

HasFcmServiceCredentials -> (boolean)

Returns true if the JSON file provided by Google during registration process was used in the **ServiceJson** field of the request.

Id -> (string)

(Deprecated) An identifier for the GCM channel. This property is retained only for backward compatibility.

IsArchived -> (boolean)

Specifies whether the GCM channel is archived.

LastModifiedBy -> (string)

The user who last modified the GCM channel.

LastModifiedDate -> (string)

The date and time when the GCM channel was last modified.

Platform -> (string)

The type of messaging or notification platform for the channel. For the GCM channel, this value is GCM.

Version -> (integer)

The current version of the GCM channel.