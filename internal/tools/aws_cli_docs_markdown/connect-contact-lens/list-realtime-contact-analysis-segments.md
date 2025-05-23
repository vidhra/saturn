# list-realtime-contact-analysis-segmentsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect-contact-lens/list-realtime-contact-analysis-segments.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect-contact-lens/list-realtime-contact-analysis-segments.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect-contact-lens](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect-contact-lens/index.html#cli-aws-connect-contact-lens) ]

# list-realtime-contact-analysis-segments

## Description

Provides a list of analysis segments for a real-time analysis session.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-contact-lens-2020-08-21/ListRealtimeContactAnalysisSegments)

## Synopsis

```
list-realtime-contact-analysis-segments
--instance-id <value>
--contact-id <value>
[--max-results <value>]
[--next-token <value>]
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

The identifier of the Amazon Connect instance.

`--contact-id` (string)

The identifier of the contact.

`--max-results` (integer)

The maximum number of results to return per page.

`--next-token` (string)

The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

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

Segments -> (list)

An analyzed transcript or category.

(structure)

An analyzed segment for a real-time analysis session.

Transcript -> (structure)

The analyzed transcript.

Id -> (string)

The identifier of the transcript.

ParticipantId -> (string)

The identifier of the participant. Valid values are CUSTOMER or AGENT.

ParticipantRole -> (string)

The role of participant. For example, is it a customer, agent, or system.

Content -> (string)

The content of the transcript.

BeginOffsetMillis -> (integer)

The beginning offset in the contact for this transcript.

EndOffsetMillis -> (integer)

The end offset in the contact for this transcript.

Sentiment -> (string)

The sentiment detected for this piece of transcript.

IssuesDetected -> (list)

List of positions where issues were detected on the transcript.

(structure)

Potential issues that are detected based on an artificial intelligence analysis of each turn in the conversation.

CharacterOffsets -> (structure)

The offset for when the issue was detected in the segment.

BeginOffsetChar -> (integer)

The beginning of the issue.

EndOffsetChar -> (integer)

The end of the issue.

Categories -> (structure)

The matched category rules.

MatchedCategories -> (list)

The category rules that have been matched in the analyzed segment.

(string)

MatchedDetails -> (map)

The category rule that was matched and when it occurred in the transcript.

key -> (string)

value -> (structure)

Provides information about the category rule that was matched.

PointsOfInterest -> (list)

The section of audio where the category rule was detected.

(structure)

The section of the contact audio where that category rule was detected.

BeginOffsetMillis -> (integer)

The beginning offset in milliseconds where the category rule was detected.

EndOffsetMillis -> (integer)

The ending offset in milliseconds where the category rule was detected.

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

If there are additional results, this is the token for the next set of results. If response includes `nextToken` there are two possible scenarios:

- There are more segments so another call is required to get them.
- There are no more segments at this time, but more may be available later (real-time analysis is in progress) so the client should call the operation again to get new segments.

If response does not include `nextToken` , the analysis is completed (successfully or failed) and there are no more segments to retrieve.