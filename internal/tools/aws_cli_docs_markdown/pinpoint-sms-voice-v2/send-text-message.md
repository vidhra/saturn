# send-text-messageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/send-text-message.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/send-text-message.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint-sms-voice-v2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/index.html#cli-aws-pinpoint-sms-voice-v2) ]

# send-text-message

## Description

Creates a new text message and sends it to a recipientâs phone number. SendTextMessage only sends an SMS message to one recipient each time it is invoked.

SMS throughput limits are measured in Message Parts per Second (MPS). Your MPS limit depends on the destination country of your messages, as well as the type of phone number (origination number) that you use to send the message. For more information about MPS, see [Message Parts per Second (MPS) limits](https://docs.aws.amazon.com/sms-voice/latest/userguide/sms-limitations-mps.html) in the *AWS End User Messaging SMS User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-sms-voice-v2-2022-03-31/SendTextMessage)

## Synopsis

```
send-text-message
--destination-phone-number <value>
[--origination-identity <value>]
[--message-body <value>]
[--message-type <value>]
[--keyword <value>]
[--configuration-set-name <value>]
[--max-price <value>]
[--time-to-live <value>]
[--context <value>]
[--destination-country-parameters <value>]
[--dry-run | --no-dry-run]
[--protect-configuration-id <value>]
[--message-feedback-enabled | --no-message-feedback-enabled]
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

`--destination-phone-number` (string)

The destination phone number in E.164 format.

`--origination-identity` (string)

The origination identity of the message. This can be either the PhoneNumber, PhoneNumberId, PhoneNumberArn, SenderId, SenderIdArn, PoolId, or PoolArn.

### Warning

If you are using a shared AWS End User Messaging SMS and Voice resource then you must use the full Amazon Resource Name(ARN).

`--message-body` (string)

The body of the text message.

`--message-type` (string)

The type of message. Valid values are for messages that are critical or time-sensitive and PROMOTIONAL for messages that arenât critical or time-sensitive.

Possible values:

- `TRANSACTIONAL`
- `PROMOTIONAL`

`--keyword` (string)

When you register a short code in the US, you must specify a program name. If you donât have a US short code, omit this attribute.

`--configuration-set-name` (string)

The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.

`--max-price` (string)

The maximum amount that you want to spend, in US dollars, per each text message. If the calculated amount to send the text message is greater than `MaxPrice` , the message is not sent and an error is returned.

`--time-to-live` (integer)

How long the text message is valid for, in seconds. By default this is 72 hours. If the messages isnât handed off before the TTL expires we stop attempting to hand off the message and return `TTL_EXPIRED` event.

`--context` (map)

You can specify custom data in this field. If you do, that data is logged to the event destination.

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

`--destination-country-parameters` (map)

This field is used for any country-specific registration requirements. Currently, this setting is only used when you send messages to recipients in India using a sender ID. For more information see [Special requirements for sending SMS messages to recipients in India](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-senderid-india.html) .

- `IN_ENTITY_ID` The entity ID or Principal Entity (PE) ID that you received after completing the sender ID registration process.
- `IN_TEMPLATE_ID` The template ID that you received after completing the sender ID registration process.

### Warning

Make sure that the Template ID that you specify matches your message template exactly. If your message doesnât match the template that you provided during the registration process, the mobile carriers might reject your message.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string

Where valid key names are:
  IN_TEMPLATE_ID
  IN_ENTITY_ID
```

JSON Syntax:

```
{"IN_TEMPLATE_ID"|"IN_ENTITY_ID": "string"
  ...}
```

`--dry-run` | `--no-dry-run` (boolean)

When set to true, the message is checked and validated, but isnât sent to the end recipient. You are not charged for using `DryRun` .

The Message Parts per Second (MPS) limit when using `DryRun` is five. If your origination identity has a lower MPS limit then the lower MPS limit is used. For more information about MPS limits, see [Message Parts per Second (MPS) limits](https://docs.aws.amazon.com/sms-voice/latest/userguide/sms-limitations-mps.html) in the *AWS End User Messaging SMS User Guide* ..

`--protect-configuration-id` (string)

The unique identifier for the protect configuration.

`--message-feedback-enabled` | `--no-message-feedback-enabled` (boolean)

Set to true to enable message feedback for the message. When a user receives the message you need to update the message status using  PutMessageFeedback .

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

The unique identifier for the message.