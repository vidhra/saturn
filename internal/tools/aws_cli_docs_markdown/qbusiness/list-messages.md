# list-messagesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/list-messages.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/list-messages.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qbusiness](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/index.html#cli-aws-qbusiness) ]

# list-messages

## Description

Gets a list of messages associated with an Amazon Q Business web experience.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qbusiness-2023-11-27/ListMessages)

`list-messages` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

`list-messages` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `messages`

## Synopsis

```
list-messages
--conversation-id <value>
--application-id <value>
[--user-id <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--conversation-id` (string)

The identifier of the Amazon Q Business web experience conversation.

`--application-id` (string)

The identifier for the Amazon Q Business application.

`--user-id` (string)

The identifier of the user involved in the Amazon Q Business web experience conversation.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

messages -> (list)

An array of information on one or more messages.

(structure)

A message in an Amazon Q Business web experience.

messageId -> (string)

The identifier of the Amazon Q Business web experience message.

body -> (string)

The content of the Amazon Q Business web experience message.

time -> (timestamp)

The timestamp of the first Amazon Q Business web experience message.

type -> (string)

The type of Amazon Q Business message, whether `HUMAN` or `AI` generated.

attachments -> (list)

A file directly uploaded into an Amazon Q Business web experience chat.

(structure)

The details of a file uploaded during chat.

name -> (string)

The name of a file uploaded during chat.

status -> (string)

The status of a file uploaded during chat.

error -> (structure)

An error associated with a file uploaded during chat.

errorMessage -> (string)

The message explaining the Amazon Q Business request error.

errorCode -> (string)

The code associated with the Amazon Q Business request error.

attachmentId -> (string)

The unique identifier of the Amazon Q Business attachment.

conversationId -> (string)

The unique identifier of the Amazon Q Business conversation.

sourceAttribution -> (list)

The source documents used to generate Amazon Q Business web experience message.

(structure)

The documents used to generate an Amazon Q Business web experience response.

title -> (string)

The title of the document which is the source for the Amazon Q Business generated response.

snippet -> (string)

The content extract from the document on which the generated response is based.

url -> (string)

The URL of the document which is the source for the Amazon Q Business generated response.

citationNumber -> (integer)

The number attached to a citation in an Amazon Q Business generated response.

updatedAt -> (timestamp)

The Unix timestamp when the Amazon Q Business application was last updated.

textMessageSegments -> (list)

A text extract from a source document that is used for source attribution.

(structure)

Provides information about a text extract in a chat response that can be attributed to a source document.

beginOffset -> (integer)

The zero-based location in the response string where the source attribution starts.

endOffset -> (integer)

The zero-based location in the response string where the source attribution ends.

snippetExcerpt -> (structure)

The relevant text excerpt from a source that was used to generate a citation text segment in an Amazon Q Business chat response.

text -> (string)

The relevant text excerpt from a source that was used to generate a citation text segment in an Amazon Q chat response.

mediaId -> (string)

The identifier of the media object associated with the text segment in the source attribution.

mediaMimeType -> (string)

The MIME type (image/png) of the media object associated with the text segment in the source attribution.

sourceDetails -> (tagged union structure)

Source information for a segment of extracted text, including its media type.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `imageSourceDetails`, `audioSourceDetails`, `videoSourceDetails`.

imageSourceDetails -> (structure)

Details specific to image content within the source.

mediaId -> (string)

Unique identifier for the image file.

mediaMimeType -> (string)

The MIME type of the image file.

audioSourceDetails -> (structure)

Details specific to audio content within the source.

mediaId -> (string)

Unique identifier for the audio media file.

mediaMimeType -> (string)

The MIME type of the audio file (e.g., audio/mp3, audio/wav).

startTimeMilliseconds -> (long)

The starting timestamp in milliseconds for the relevant audio segment.

endTimeMilliseconds -> (long)

The ending timestamp in milliseconds for the relevant audio segment.

audioExtractionType -> (string)

The type of audio extraction performed on the content.

videoSourceDetails -> (structure)

Details specific to video content within the source.

mediaId -> (string)

Unique identifier for the video media file.

mediaMimeType -> (string)

The MIME type of the video file (e.g., video/mp4, video/avi).

startTimeMilliseconds -> (long)

The starting timestamp in milliseconds for the relevant video segment.

endTimeMilliseconds -> (long)

The ending timestamp in milliseconds for the relevant video segment.

videoExtractionType -> (string)

The type of video extraction performed on the content.

actionReview -> (structure)

An output event that Amazon Q Business returns to an user who wants to perform a plugin action during a non-streaming chat conversation. It contains information about the selected action with a list of possible user input fields, some pre-populated by Amazon Q Business.

pluginId -> (string)

The identifier of the plugin associated with the action review.

pluginType -> (string)

The type of plugin.

payload -> (map)

Field values that an end user needs to provide to Amazon Q Business for Amazon Q Business to perform the requested plugin action.

key -> (string)

value -> (structure)

A user input field in an plugin action review payload.

displayName -> (string)

The name of the field.

displayOrder -> (integer)

The display order of fields in a payload.

displayDescription -> (string)

The field level description of each action review input field. This could be an explanation of the field. In the Amazon Q Business web experience, these descriptions could be used to display as tool tips to help users understand the field.

type -> (string)

The type of field.

value -> (document)

The field value.

allowedValues -> (list)

Information about the field values that an end user can use to provide to Amazon Q Business for Amazon Q Business to perform the requested plugin action.

(structure)

Information about the field values that an end user can use to provide to Amazon Q Business for Amazon Q Business to perform the requested plugin action.

value -> (document)

The field value.

displayValue -> (document)

The name of the field.

allowedFormat -> (string)

The expected data format for the action review input field value. For example, in PTO request, `from` and `to` would be of `datetime` allowed format.

arrayItemJsonSchema -> (document)

Use to create a custom form with array fields (fields with nested objects inside an array).

required -> (boolean)

Information about whether the field is required.

payloadFieldNameSeparator -> (string)

A string used to retain information about the hierarchical contexts within an action review payload.

actionExecution -> (structure)

Performs an Amazon Q Business plugin action during a non-streaming chat conversation.

pluginId -> (string)

The identifier of the plugin the action is attached to.

payload -> (map)

A mapping of field names to the field values in input that an end user provides to Amazon Q Business requests to perform their plugin action.

key -> (string)

value -> (structure)

A user input field in an plugin action execution payload.

value -> (document)

The content of a user input field in an plugin action execution payload.

payloadFieldNameSeparator -> (string)

A string used to retain information about the hierarchical contexts within an action execution event payload.

nextToken -> (string)

If the response is truncated, Amazon Q Business returns this token, which you can use in a later request to list the next set of messages.