# channel-flow-callbackÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-messaging/channel-flow-callback.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-messaging/channel-flow-callback.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [chime-sdk-messaging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-messaging/index.html#cli-aws-chime-sdk-messaging) ]

# channel-flow-callback

## Description

Calls back Amazon Chime SDK messaging with a processing response message. This should be invoked from the processor Lambda. This is a developer API.

You can return one of the following processing responses:

- Update message content or metadata
- Deny a message
- Make no changes to the message

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/chime-sdk-messaging-2021-05-15/ChannelFlowCallback)

## Synopsis

```
channel-flow-callback
[--callback-id <value>]
--channel-arn <value>
[--delete-resource | --no-delete-resource]
--channel-message <value>
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

`--callback-id` (string)

The identifier passed to the processor by the service when invoked. Use the identifier to call back the service.

`--channel-arn` (string)

The ARN of the channel.

`--delete-resource` | `--no-delete-resource` (boolean)

When a processor determines that a message needs to be `DENIED` , pass this parameter with a value of true.

`--channel-message` (structure)

Stores information about the processed message.

MessageId -> (string)

The message ID.

Content -> (string)

The message content. For Amazon Lex V2 bot responses, this field holds a list of messages originating from the bot. For more information, refer to [Processing responses from an AppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html) in the *Amazon Chime SDK Messaging Developer Guide* .

Metadata -> (string)

The message metadata.

PushNotification -> (structure)

The push notification configuration of the message.

Title -> (string)

The title of the push notification.

Body -> (string)

The body of the push notification.

Type -> (string)

Enum value that indicates the type of the push notification for a message. `DEFAULT` : Normal mobile push notification. `VOIP` : VOIP mobile push notification.

MessageAttributes -> (map)

The attributes for the channel message. For Amazon Lex V2 bot responses, the attributes are mapped to specific fields from the bot. For more information, refer to [Processing responses from an AppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html) in the *Amazon Chime SDK Messaging Developer Guide* .

key -> (string)

value -> (structure)

A list of message attribute values.

StringValues -> (list)

The strings in a message attribute value.

(string)

SubChannelId -> (string)

The ID of the SubChannel.

ContentType -> (string)

The content type of the call-back message. For Amazon Lex V2 bot responses, the content type is `application/amz-chime-lex-msgs` for success responses and `application/amz-chime-lex-error` for failure responses. For more information, refer to [Processing responses from an AppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html) in the *Amazon Chime SDK Messaging Developer Guide* .

Shorthand Syntax:

```
MessageId=string,Content=string,Metadata=string,PushNotification={Title=string,Body=string,Type=string},MessageAttributes={KeyName1={StringValues=[string,string]},KeyName2={StringValues=[string,string]}},SubChannelId=string,ContentType=string
```

JSON Syntax:

```
{
  "MessageId": "string",
  "Content": "string",
  "Metadata": "string",
  "PushNotification": {
    "Title": "string",
    "Body": "string",
    "Type": "DEFAULT"|"VOIP"
  },
  "MessageAttributes": {"string": {
        "StringValues": ["string", ...]
      }
    ...},
  "SubChannelId": "string",
  "ContentType": "string"
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

ChannelArn -> (string)

The ARN of the channel.

CallbackId -> (string)

The call back ID passed in the request.