# send-otp-messageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/send-otp-message.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/send-otp-message.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/index.html#cli-aws-pinpoint) ]

# send-otp-message

## Description

Send an OTP message

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/SendOTPMessage)

## Synopsis

```
send-otp-message
--application-id <value>
--send-otp-message-request-parameters <value>
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

The unique ID of your Amazon Pinpoint application.

`--send-otp-message-request-parameters` (structure)

Send OTP message request parameters.

AllowedAttempts -> (integer)

The attempts allowed to validate an OTP.

BrandName -> (string)

The brand name that will be substituted into the OTP message body. Should be owned by calling AWS account.

Channel -> (string)

Channel type for the OTP message. Supported values: [SMS].

CodeLength -> (integer)

The number of characters in the generated OTP.

DestinationIdentity -> (string)

The destination identity to send OTP to.

EntityId -> (string)

A unique Entity ID received from DLT after entity registration is approved.

Language -> (string)

The language to be used for the outgoing message body containing the OTP.

OriginationIdentity -> (string)

The origination identity used to send OTP from.

ReferenceId -> (string)

Developer-specified reference identifier. Required to match during OTP verification.

TemplateId -> (string)

A unique Template ID received from DLT after entity registration is approved.

ValidityPeriod -> (integer)

The time in minutes before the OTP is no longer valid.

Shorthand Syntax:

```
AllowedAttempts=integer,BrandName=string,Channel=string,CodeLength=integer,DestinationIdentity=string,EntityId=string,Language=string,OriginationIdentity=string,ReferenceId=string,TemplateId=string,ValidityPeriod=integer
```

JSON Syntax:

```
{
  "AllowedAttempts": integer,
  "BrandName": "string",
  "Channel": "string",
  "CodeLength": integer,
  "DestinationIdentity": "string",
  "EntityId": "string",
  "Language": "string",
  "OriginationIdentity": "string",
  "ReferenceId": "string",
  "TemplateId": "string",
  "ValidityPeriod": integer
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

MessageResponse -> (structure)

Provides information about the results of a request to send a message to an endpoint address.

ApplicationId -> (string)

The unique identifier for the application that was used to send the message.

EndpointResult -> (map)

A map that contains a multipart response for each address that the message was sent to. In the map, the endpoint ID is the key and the result is the value.

key -> (string)

value -> (structure)

Provides information about the delivery status and results of sending a message directly to an endpoint.

Address -> (string)

The endpoint address that the message was delivered to.

DeliveryStatus -> (string)

The delivery status of the message. Possible values are:

- DUPLICATE - The endpoint address is a duplicate of another endpoint address. Amazon Pinpoint wonât attempt to send the message again.
- OPT_OUT - The user whoâs associated with the endpoint has opted out of receiving messages from you. Amazon Pinpoint wonât attempt to send the message again.
- PERMANENT_FAILURE - An error occurred when delivering the message to the endpoint. Amazon Pinpoint wonât attempt to send the message again.
- SUCCESSFUL - The message was successfully delivered to the endpoint.
- TEMPORARY_FAILURE - A temporary error occurred. Amazon Pinpoint wonât attempt to send the message again.
- THROTTLED - Amazon Pinpoint throttled the operation to send the message to the endpoint.
- UNKNOWN_FAILURE - An unknown error occurred.

MessageId -> (string)

The unique identifier for the message that was sent.

StatusCode -> (integer)

The downstream service status code for delivering the message.

StatusMessage -> (string)

The status message for delivering the message.

UpdatedToken -> (string)

For push notifications that are sent through the GCM channel, specifies whether the endpointâs device registration token was updated as part of delivering the message.

RequestId -> (string)

The identifier for the original request that the message was delivered for.

Result -> (map)

A map that contains a multipart response for each address (email address, phone number, or push notification token) that the message was sent to. In the map, the address is the key and the result is the value.

key -> (string)

value -> (structure)

Provides information about the results of sending a message directly to an endpoint address.

DeliveryStatus -> (string)

The delivery status of the message. Possible values are:

- DUPLICATE - The endpoint address is a duplicate of another endpoint address. Amazon Pinpoint wonât attempt to send the message again.
- OPT_OUT - The user whoâs associated with the endpoint address has opted out of receiving messages from you. Amazon Pinpoint wonât attempt to send the message again.
- PERMANENT_FAILURE - An error occurred when delivering the message to the endpoint address. Amazon Pinpoint wonât attempt to send the message again.
- SUCCESSFUL - The message was successfully delivered to the endpoint address.
- TEMPORARY_FAILURE - A temporary error occurred. Amazon Pinpoint wonât attempt to send the message again.
- THROTTLED - Amazon Pinpoint throttled the operation to send the message to the endpoint address.
- UNKNOWN_FAILURE - An unknown error occurred.

MessageId -> (string)

The unique identifier for the message that was sent.

StatusCode -> (integer)

The downstream service status code for delivering the message.

StatusMessage -> (string)

The status message for delivering the message.

UpdatedToken -> (string)

For push notifications that are sent through the GCM channel, specifies whether the endpointâs device registration token was updated as part of delivering the message.