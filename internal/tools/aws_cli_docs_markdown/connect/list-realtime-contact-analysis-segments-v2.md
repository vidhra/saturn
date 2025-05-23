# list-realtime-contact-analysis-segments-v2Â¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-realtime-contact-analysis-segments-v2.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-realtime-contact-analysis-segments-v2.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# list-realtime-contact-analysis-segments-v2

## Description

Provides a list of analysis segments for a real-time chat analysis session. This API supports CHAT channels only.

### Warning

This API does not support VOICE. If you attempt to use it for VOICE, an `InvalidRequestException` occurs.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListRealtimeContactAnalysisSegmentsV2)

## Synopsis

```
list-realtime-contact-analysis-segments-v2
--instance-id <value>
--contact-id <value>
[--max-results <value>]
[--next-token <value>]
--output-type <value>
--segment-types <value>
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

`--instance-id` (string)

The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.

`--contact-id` (string)

The identifier of the contact in this instance of Amazon Connect.

`--max-results` (integer)

The maximum number of results to return per page.

`--next-token` (string)

The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

`--output-type` (string)

The Contact Lens output type to be returned.

Possible values:

- `Raw`
- `Redacted`

`--segment-types` (list)

Enum with segment types . Each value corresponds to a segment type returned in the segments list of the API. Each segment type has its own structure. Different channels may have different sets of supported segment types.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  Transcript
  Categories
  Issues
  Event
  Attachments
  PostContactSummary
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

Channel -> (string)

The channel of the contact.

### Warning

Only `CHAT` is supported. This API does not support `VOICE` . If you attempt to use it for the VOICE channel, an `InvalidRequestException` error occurs.

Status -> (string)

Status of real-time contact analysis.

Segments -> (list)

An analyzed transcript or category.

(tagged union structure)

An analyzed segment for a real-time analysis session.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Transcript`, `Categories`, `Issues`, `Event`, `Attachments`, `PostContactSummary`.

Transcript -> (structure)

The analyzed transcript segment.

Id -> (string)

The identifier of the transcript.

ParticipantId -> (string)

The identifier of the participant.

ParticipantRole -> (string)

The role of the participant. For example, is it a customer, agent, or system.

DisplayName -> (string)

The display name of the participant.

Content -> (string)

The content of the transcript. Can be redacted.

ContentType -> (string)

The type of content of the item. For example, `text/plain` .

Time -> (tagged union structure)

Field describing the time of the event. It can have different representations of time.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `AbsoluteTime`.

AbsoluteTime -> (timestamp)

Time represented in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.

Redaction -> (structure)

Object describing redaction that was applied to the transcript. If transcript has the field it means part of the transcript was redacted.

CharacterOffsets -> (list)

List of character intervals each describing a part of the text that was redacted. For `OutputType.Raw` , part of the original text that contains data that can be redacted. For `OutputType.Redacted` , part of the string with redaction tag.

(structure)

Begin and end offsets for a part of text.

BeginOffsetChar -> (integer)

The beginning of the character interval.

EndOffsetChar -> (integer)

The end of the character interval.

Sentiment -> (string)

The sentiment detected for this piece of transcript.

Categories -> (structure)

The matched category rules.

MatchedDetails -> (map)

Map between the name of the matched rule and RealTimeContactAnalysisCategoryDetails.

key -> (string)

value -> (structure)

Provides information about the category rule that was matched.

PointsOfInterest -> (list)

List of PointOfInterest - objects describing a single match of a rule.

(structure)

The section of the contact transcript segment that category rule was detected.

TranscriptItems -> (list)

List of the transcript items (segments) that are associated with a given point of interest.

(structure)

Transcript representation containing Id and list of character intervals that are associated with analysis data. For example, this object within a `RealTimeContactAnalysisPointOfInterest` in `Category.MatchedDetails` would have character interval describing part of the text that matched category.

Id -> (string)

Transcript identifier. Matches the identifier from one of the TranscriptSegments.

CharacterOffsets -> (structure)

List of character intervals within transcript content/text.

BeginOffsetChar -> (integer)

The beginning of the character interval.

EndOffsetChar -> (integer)

The end of the character interval.

Issues -> (structure)

Segment type containing a list of detected issues.

IssuesDetected -> (list)

List of the issues detected.

(structure)

Potential issues that are detected based on an artificial intelligence analysis of each turn in the conversation.

TranscriptItems -> (list)

List of the transcript items (segments) that are associated with a given issue.

(structure)

Transcript representation containing Id, Content and list of character intervals that are associated with analysis data. For example, this object within an issue detected would describe both content that contains identified issue and intervals where that content is taken from.

Content -> (string)

Part of the transcript content that contains identified issue. Can be redacted

Id -> (string)

Transcript identifier. Matches the identifier from one of the TranscriptSegments.

CharacterOffsets -> (structure)

Begin and end offsets for a part of text.

BeginOffsetChar -> (integer)

The beginning of the character interval.

EndOffsetChar -> (integer)

The end of the character interval.

Event -> (structure)

Segment type describing a contact event.

Id -> (string)

The identifier of the contact event.

ParticipantId -> (string)

The identifier of the participant.

ParticipantRole -> (string)

The role of the participant. For example, is it a customer, agent, or system.

DisplayName -> (string)

The display name of the participant. Can be redacted.

EventType -> (string)

Type of the event. For example, `application/vnd.amazonaws.connect.event.participant.left` .

Time -> (tagged union structure)

Field describing the time of the event. It can have different representations of time.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `AbsoluteTime`.

AbsoluteTime -> (timestamp)

Time represented in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.

Attachments -> (structure)

The analyzed attachments.

Id -> (string)

The identifier of the segment.

ParticipantId -> (string)

The identifier of the participant.

ParticipantRole -> (string)

The role of the participant. For example, is it a customer, agent, or system.

DisplayName -> (string)

The display name of the participant. Can be redacted.

Attachments -> (list)

List of objects describing an individual attachment.

(structure)

Object that describes attached file.

AttachmentName -> (string)

A case-sensitive name of the attachment being uploaded. Can be redacted.

ContentType -> (string)

Describes the MIME file type of the attachment. For a list of supported file types, see [Feature specifications](https://docs.aws.amazon.com/connect/latest/adminguide/feature-limits.html) in the *Amazon Connect Administrator Guide* .

AttachmentId -> (string)

A unique identifier for the attachment.

Status -> (string)

Status of the attachment.

Time -> (tagged union structure)

Field describing the time of the event. It can have different representations of time.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `AbsoluteTime`.

AbsoluteTime -> (timestamp)

Time represented in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.

PostContactSummary -> (structure)

Information about the post-contact summary.

Content -> (string)

The content of the summary.

Status -> (string)

Whether the summary was successfully COMPLETED or FAILED to be generated.

FailureCode -> (string)

If the summary failed to be generated, one of the following failure codes occurs:

- `QUOTA_EXCEEDED` : The number of concurrent analytics jobs reached your service quota.
- `INSUFFICIENT_CONVERSATION_CONTENT` : The conversation needs to have at least one turn from both the participants in order to generate the summary.
- `FAILED_SAFETY_GUIDELINES` : The generated summary cannot be provided because it failed to meet system safety guidelines.
- `INVALID_ANALYSIS_CONFIGURATION` : This code occurs when, for example, youâre using a [language](https://docs.aws.amazon.com/connect/latest/adminguide/supported-languages.html#supported-languages-contact-lens) that isnât supported by generative AI-powered post-contact summaries.
- `INTERNAL_ERROR` : Internal system error.

NextToken -> (string)

If there are additional results, this is the token for the next set of results.