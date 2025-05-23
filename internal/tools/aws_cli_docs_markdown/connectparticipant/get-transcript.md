# get-transcriptÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connectparticipant/get-transcript.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connectparticipant/get-transcript.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connectparticipant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connectparticipant/index.html#cli-aws-connectparticipant) ]

# get-transcript

## Description

Retrieves a transcript of the session, including details about any attachments. For information about accessing past chat contact transcripts for a persistent chat, see [Enable persistent chat](https://docs.aws.amazon.com/connect/latest/adminguide/chat-persistence.html) .

For security recommendations, see [Amazon Connect Chat security best practices](https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat) .

If you have a process that consumes events in the transcript of an chat that has ended, note that chat transcripts contain the following event content types if the event has occurred during the chat session:

- `application/vnd.amazonaws.connect.event.participant.left`
- `application/vnd.amazonaws.connect.event.participant.joined`
- `application/vnd.amazonaws.connect.event.chat.ended`
- `application/vnd.amazonaws.connect.event.transfer.succeeded`
- `application/vnd.amazonaws.connect.event.transfer.failed`

### Note

`ConnectionToken` is used for invoking this API instead of `ParticipantToken` .

The Amazon Connect Participant Service APIs do not use [Signature Version 4 authentication](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connectparticipant-2018-09-07/GetTranscript)

## Synopsis

```
get-transcript
[--contact-id <value>]
[--max-results <value>]
[--next-token <value>]
[--scan-direction <value>]
[--sort-order <value>]
[--start-position <value>]
--connection-token <value>
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

`--contact-id` (string)

The contactId from the current contact chain for which transcript is needed.

`--max-results` (integer)

The maximum number of results to return in the page. Default: 10.

`--next-token` (string)

The pagination token. Use the value returned previously in the next subsequent request to retrieve the next set of results.

`--scan-direction` (string)

The direction from StartPosition from which to retrieve message. Default: BACKWARD when no StartPosition is provided, FORWARD with StartPosition.

Possible values:

- `FORWARD`
- `BACKWARD`

`--sort-order` (string)

The sort order for the records. Default: DESCENDING.

Possible values:

- `DESCENDING`
- `ASCENDING`

`--start-position` (structure)

A filtering option for where to start.

Id -> (string)

The ID of the message or event where to start.

AbsoluteTime -> (string)

The time in ISO format where to start.

Itâs specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.

MostRecent -> (integer)

The start position of the most recent message where you want to start.

Shorthand Syntax:

```
Id=string,AbsoluteTime=string,MostRecent=integer
```

JSON Syntax:

```
{
  "Id": "string",
  "AbsoluteTime": "string",
  "MostRecent": integer
}
```

`--connection-token` (string)

The authentication token associated with the participantâs connection.

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

The initial contact ID for the contact.

Transcript -> (list)

The list of messages in the session.

(structure)

An item - message or event - that has been sent.

AbsoluteTime -> (string)

The time when the message or event was sent.

Itâs specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.

Content -> (string)

The content of the message or event.

ContentType -> (string)

The type of content of the item.

Id -> (string)

The ID of the item.

Type -> (string)

Type of the item: message or event.

ParticipantId -> (string)

The ID of the sender in the session.

DisplayName -> (string)

The chat display name of the sender.

ParticipantRole -> (string)

The role of the sender. For example, is it a customer, agent, or system.

Attachments -> (list)

Provides information about the attachments.

(structure)

The case-insensitive input to indicate standard MIME type that describes the format of the file that will be uploaded.

ContentType -> (string)

Describes the MIME file type of the attachment. For a list of supported file types, see [Feature specifications](https://docs.aws.amazon.com/connect/latest/adminguide/feature-limits.html) in the *Amazon Connect Administrator Guide* .

AttachmentId -> (string)

A unique identifier for the attachment.

AttachmentName -> (string)

A case-sensitive name of the attachment being uploaded.

Status -> (string)

Status of the attachment.

MessageMetadata -> (structure)

The metadata related to the message. Currently this supports only information related to message receipts.

MessageId -> (string)

The identifier of the message that contains the metadata information.

Receipts -> (list)

The list of receipt information for a message for different recipients.

(structure)

The receipt for the message delivered to the recipient.

DeliveredTimestamp -> (string)

The time when the message was delivered to the recipient.

ReadTimestamp -> (string)

The time when the message was read by the recipient.

RecipientParticipantId -> (string)

The identifier of the recipient of the message.

RelatedContactId -> (string)

The contactId on which the transcript item was originally sent. This field is only populated for persistent chats when the transcript item is from the past chat session. For more information, see [Enable persistent chat](https://docs.aws.amazon.com/connect/latest/adminguide/chat-persistence.html) .

ContactId -> (string)

The contactId on which the transcript item was originally sent. This field is populated only when the transcript item is from the current chat session.

NextToken -> (string)

The pagination token. Use the value returned previously in the next subsequent request to retrieve the next set of results.