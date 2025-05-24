# send-chat-integration-eventÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/send-chat-integration-event.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/send-chat-integration-event.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# send-chat-integration-event

## Description

Processes chat integration events from Amazon Web Services or external integrations to Amazon Connect. A chat integration event includes:

- SourceId, DestinationId, and Subtype: a set of identifiers, uniquely representing a chat
- ChatEvent: details of the chat action to perform such as sending a message, event, or disconnecting from a chat

When a chat integration event is sent with chat identifiers that do not map to an active chat contact, a new chat contact is also created before handling chat action.

Access to this API is currently restricted to Amazon Web Services End User Messaging for supporting SMS integration.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/SendChatIntegrationEvent)

## Synopsis

```
send-chat-integration-event
--source-id <value>
--destination-id <value>
[--subtype <value>]
--event <value>
[--new-session-details <value>]
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

`--source-id` (string)

External identifier of chat customer participant, used in part to uniquely identify a chat. For SMS, this is the E164 phone number of the chat customer participant.

`--destination-id` (string)

Chat system identifier, used in part to uniquely identify chat. This is associated with the Amazon Connect instance and flow to be used to start chats. For Server Migration Service, this is the phone number destination of inbound Server Migration Service messages represented by an Amazon Web Services End User Messaging phone number ARN.

`--subtype` (string)

Classification of a channel. This is used in part to uniquely identify chat.

Valid value: `["connect:sms", connect:"WhatsApp"]`

`--event` (structure)

Chat integration event payload

Type -> (string)

Type of chat integration event.

ContentType -> (string)

Type of content. This is required when `Type` is `MESSAGE` or `EVENT` .

- For allowed message content types, see the `ContentType` parameter in the [SendMessage](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_SendMessage.html) topic in the *Amazon Connect Participant Service API Reference* .
- For allowed event content types, see the `ContentType` parameter in the [SendEvent](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_SendEvent.html) topic in the *Amazon Connect Participant Service API Reference* .

Content -> (string)

Content of the message or event. This is required when `Type` is `MESSAGE` and for certain `ContentTypes` when `Type` is `EVENT` .

- For allowed message content, see the `Content` parameter in the [SendMessage](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_SendMessage.html) topic in the *Amazon Connect Participant Service API Reference* .
- For allowed event content, see the `Content` parameter in the [SendEvent](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_SendEvent.html) topic in the *Amazon Connect Participant Service API Reference* .

Shorthand Syntax:

```
Type=string,ContentType=string,Content=string
```

JSON Syntax:

```
{
  "Type": "DISCONNECT"|"MESSAGE"|"EVENT",
  "ContentType": "string",
  "Content": "string"
}
```

`--new-session-details` (structure)

Contact properties to apply when starting a new chat. If the integration event is handled with an existing chat, this is ignored.

SupportedMessagingContentTypes -> (list)

The supported chat message content types. Supported types are `text/plain` , `text/markdown` , `application/json` , `application/vnd.amazonaws.connect.message.interactive` , and `application/vnd.amazonaws.connect.message.interactive.response` .

Content types must always contain `text/plain` . You can then put any other supported type in the list. For example, all the following lists are valid because they contain `text/plain` : `[text/plain, text/markdown, application/json]` , `[text/markdown, text/plain]` , `[text/plain, application/json, application/vnd.amazonaws.connect.message.interactive.response]` .

(string)

ParticipantDetails -> (structure)

The customerâs details.

DisplayName -> (string)

Display name of the participant.

Attributes -> (map)

A custom key-value pair using an attribute map. The attributes are standard Amazon Connect attributes. They can be accessed in flows just like any other contact attributes.

There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters.

key -> (string)

value -> (string)

StreamingConfiguration -> (structure)

The streaming configuration, such as the Amazon SNS streaming endpoint.

StreamingEndpointArn -> (string)

The Amazon Resource Name (ARN) of the standard Amazon SNS topic. The Amazon Resource Name (ARN) of the streaming endpoint that is used to publish real-time message streaming for chat conversations.

Shorthand Syntax:

```
SupportedMessagingContentTypes=string,string,ParticipantDetails={DisplayName=string},Attributes={KeyName1=string,KeyName2=string},StreamingConfiguration={StreamingEndpointArn=string}
```

JSON Syntax:

```
{
  "SupportedMessagingContentTypes": ["string", ...],
  "ParticipantDetails": {
    "DisplayName": "string"
  },
  "Attributes": {"string": "string"
    ...},
  "StreamingConfiguration": {
    "StreamingEndpointArn": "string"
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

InitialContactId -> (string)

Identifier of chat contact used to handle integration event. This may be null if the integration event is not valid without an already existing chat contact.

NewChatCreated -> (boolean)

Whether handling the integration event resulted in creating a new chat or acting on existing chat.