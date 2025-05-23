# get-message-insightsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-message-insights.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-message-insights.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sesv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/index.html#cli-aws-sesv2) ]

# get-message-insights

## Description

Provides information about a specific message, including the from address, the subject, the recipient address, email tags, as well as events associated with the message.

You can execute this operation no more than once per second.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sesv2-2019-09-27/GetMessageInsights)

## Synopsis

```
get-message-insights
--message-id <value>
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

`--message-id` (string)

A `MessageId` is a unique identifier for a message, and is returned when sending emails through Amazon SES.

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

MessageId -> (string)

A unique identifier for the message.

FromEmailAddress -> (string)

The from address used to send the message.

Subject -> (string)

The subject line of the message.

EmailTags -> (list)

A list of tags, in the form of name/value pairs, that were applied to the email you sent, along with Amazon SES [Auto-Tags](https://docs.aws.amazon.com/ses/latest/dg/monitor-using-event-publishing.html) .

(structure)

Contains the name and value of a tag that you apply to an email. You can use message tags when you publish email sending events.

Name -> (string)

The name of the message tag. The message tag name has to meet the following criteria:

- It can only contain ASCII letters (aâz, AâZ), numbers (0â9), underscores (_), or dashes (-).
- It can contain no more than 256 characters.

Value -> (string)

The value of the message tag. The message tag value has to meet the following criteria:

- It can only contain ASCII letters (aâz, AâZ), numbers (0â9), underscores (_), or dashes (-).
- It can contain no more than 256 characters.

Insights -> (list)

A set of insights associated with the message.

(structure)

An emailâs insights contain metadata and delivery information about a specific email.

Destination -> (string)

The recipient of the email.

Isp -> (string)

The recipientâs ISP (e.g., `Gmail` , `Yahoo` , etc.).

Events -> (list)

A list of events associated with the sent email.

(structure)

An object containing details about a specific event.

Timestamp -> (timestamp)

The timestamp of the event.

Type -> (string)

The type of event:

- `SEND` - The send request was successful and SES will attempt to deliver the message to the recipientâs mail server. (If account-level or global suppression is being used, SES will still count it as a send, but delivery is suppressed.)
- `DELIVERY` - SES successfully delivered the email to the recipientâs mail server. Excludes deliveries to the mailbox simulator, and those from emails addressed to more than one recipient.
- `BOUNCE` - Feedback received for delivery failures. Additional details about the bounce are provided in the `Details` object. Excludes bounces from the mailbox simulator, and those from emails addressed to more than one recipient.
- `COMPLAINT` - Complaint received for the email. Additional details about the complaint are provided in the `Details` object. This excludes complaints from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those from emails addressed to more than one recipient.
- `OPEN` - Open event for emails including open trackers. Excludes opens for emails addressed to more than one recipient.
- `CLICK` - Click event for emails including wrapped links. Excludes clicks for emails addressed to more than one recipient.

Details -> (structure)

Details about bounce or complaint events.

Bounce -> (structure)

Information about a `Bounce` event.

BounceType -> (string)

The type of the bounce, as determined by SES. Can be one of `UNDETERMINED` , `TRANSIENT` , or `PERMANENT`

BounceSubType -> (string)

The subtype of the bounce, as determined by SES.

DiagnosticCode -> (string)

The status code issued by the reporting Message Transfer Authority (MTA). This field only appears if a delivery status notification (DSN) was attached to the bounce and the `Diagnostic-Code` was provided in the DSN.

Complaint -> (structure)

Information about a `Complaint` event.

ComplaintSubType -> (string)

Can either be `null` or `OnAccountSuppressionList` . If the value is `OnAccountSuppressionList` , SES accepted the message, but didnât attempt to send it because it was on the account-level suppression list.

ComplaintFeedbackType -> (string)

The value of the `Feedback-Type` field from the feedback report received from the ISP.