# start-web-rtc-contactÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/start-web-rtc-contact.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/start-web-rtc-contact.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# start-web-rtc-contact

## Description

Places an inbound in-app, web, or video call to a contact, and then initiates the flow. It performs the actions in the flow that are specified (in ContactFlowId) and present in the Amazon Connect instance (specified as InstanceId).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/StartWebRTCContact)

## Synopsis

```
start-web-rtc-contact
[--attributes <value>]
[--client-token <value>]
--contact-flow-id <value>
--instance-id <value>
[--allowed-capabilities <value>]
--participant-details <value>
[--related-contact-id <value>]
[--references <value>]
[--description <value>]
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

`--attributes` (map)

A custom key-value pair using an attribute map. The attributes are standard Amazon Connect attributes, and can be accessed in flows just like any other contact attributes.

There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, -, and _ characters.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) .

The token is valid for 7 days after creation. If a contact is already started, the contact ID is returned.

`--contact-flow-id` (string)

The identifier of the flow for the call. To see the ContactFlowId in the Amazon Connect admin website, on the navigation menu go to **Routing** , **Flows** . Choose the flow. On the flow page, under the name of the flow, choose **Show additional flow information** . The ContactFlowId is the last part of the ARN, shown here in bold:

arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/**846ec553-a005-41c0-8341-xxxxxxxxxxxx**

`--instance-id` (string)

The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.

`--allowed-capabilities` (structure)

Information about the video sharing capabilities of the participants (customer, agent).

Customer -> (structure)

Information about the customerâs video sharing capabilities.

Video -> (string)

The configuration having the video and screen sharing capabilities for participants over the call.

ScreenShare -> (string)

The screen sharing capability that is enabled for the participant. `SEND` indicates the participant can share their screen.

Agent -> (structure)

Information about the agentâs video sharing capabilities.

Video -> (string)

The configuration having the video and screen sharing capabilities for participants over the call.

ScreenShare -> (string)

The screen sharing capability that is enabled for the participant. `SEND` indicates the participant can share their screen.

Shorthand Syntax:

```
Customer={Video=string,ScreenShare=string},Agent={Video=string,ScreenShare=string}
```

JSON Syntax:

```
{
  "Customer": {
    "Video": "SEND",
    "ScreenShare": "SEND"
  },
  "Agent": {
    "Video": "SEND",
    "ScreenShare": "SEND"
  }
}
```

`--participant-details` (structure)

The customerâs details.

DisplayName -> (string)

Display name of the participant.

Shorthand Syntax:

```
DisplayName=string
```

JSON Syntax:

```
{
  "DisplayName": "string"
}
```

`--related-contact-id` (string)

The unique identifier for an Amazon Connect contact. This identifier is related to the contact starting.

`--references` (map)

A formatted URL that is shown to an agent in the Contact Control Panel (CCP). Tasks can have the following reference types at the time of creation: `URL` | `NUMBER` | `STRING` | `DATE` | `EMAIL` . `ATTACHMENT` is not a supported reference type during task creation.

key -> (string)

value -> (structure)

Well-formed data on a contact, used by agents to complete a contact request. You can have up to 4,096 UTF-8 bytes across all references for a contact.

Value -> (string)

A valid value for the reference. For example, for a URL reference, a formatted URL that is displayed to an agent in the Contact Control Panel (CCP).

Type -> (string)

The type of the reference. `DATE` must be of type Epoch timestamp.

Status -> (string)

Status of the attachment reference type.

Arn -> (string)

The Amazon Resource Name (ARN) of the reference

StatusReason -> (string)

Relevant details why the reference was not successfully created.

Shorthand Syntax:

```
KeyName1=Value=string,Type=string,Status=string,Arn=string,StatusReason=string,KeyName2=Value=string,Type=string,Status=string,Arn=string,StatusReason=string
```

JSON Syntax:

```
{"string": {
      "Value": "string",
      "Type": "URL"|"ATTACHMENT"|"CONTACT_ANALYSIS"|"NUMBER"|"STRING"|"DATE"|"EMAIL"|"EMAIL_MESSAGE",
      "Status": "AVAILABLE"|"DELETED"|"APPROVED"|"REJECTED"|"PROCESSING"|"FAILED",
      "Arn": "string",
      "StatusReason": "string"
    }
  ...}
```

`--description` (string)

A description of the task that is shown to an agent in the Contact Control Panel (CCP).

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

ConnectionData -> (structure)

Information required for the client application (mobile application or website) to connect to the call.

Attendee -> (structure)

The attendee information, including attendee ID and join token.

AttendeeId -> (string)

The Amazon Chime SDK attendee ID.

JoinToken -> (string)

The join token used by the Amazon Chime SDK attendee.

Meeting -> (structure)

A meeting created using the Amazon Chime SDK.

MediaRegion -> (string)

The Amazon Web Services Region in which you create the meeting.

MediaPlacement -> (structure)

The media placement for the meeting.

AudioHostUrl -> (string)

The audio host URL.

AudioFallbackUrl -> (string)

The audio fallback URL.

SignalingUrl -> (string)

The signaling URL.

TurnControlUrl -> (string)

The turn control URL.

EventIngestionUrl -> (string)

The event ingestion URL to which you send client meeting events.

MeetingFeatures -> (structure)

The configuration settings of the features available to a meeting.

Audio -> (structure)

The configuration settings for the audio features available to a meeting.

EchoReduction -> (string)

Makes echo reduction available to clients who connect to the meeting.

MeetingId -> (string)

The Amazon Chime SDK meeting ID.

ContactId -> (string)

The identifier of the contact in this instance of Amazon Connect.

ParticipantId -> (string)

The identifier for a contact participant. The `ParticipantId` for a contact participant is the same throughout the contact lifecycle.

ParticipantToken -> (string)

The token used by the contact participant to call the [CreateParticipantConnection](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html) API. The participant token is valid for the lifetime of a contact participant.