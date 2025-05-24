# publishÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/publish.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/publish.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sns](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/index.html#cli-aws-sns) ]

# publish

## Description

Sends a message to an Amazon SNS topic, a text message (SMS message) directly to a phone number, or a message to a mobile platform endpoint (when you specify the `TargetArn` ).

If you send a message to a topic, Amazon SNS delivers the message to each endpoint that is subscribed to the topic. The format of the message depends on the notification protocol for each subscribed endpoint.

When a `messageId` is returned, the message is saved and Amazon SNS immediately delivers it to subscribers.

To use the `Publish` action for publishing a message to a mobile endpoint, such as an app on a Kindle device or mobile phone, you must specify the EndpointArn for the TargetArn parameter. The EndpointArn is returned when making a call with the `CreatePlatformEndpoint` action.

For more information about formatting messages, see [Send Custom Platform-Specific Payloads in Messages to Mobile Devices](https://docs.aws.amazon.com/sns/latest/dg/mobile-push-send-custommessage.html) .

### Warning

You can publish messages only to topics and endpoints in the same Amazon Web Services Region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/Publish)

## Synopsis

```
publish
[--topic-arn <value>]
[--target-arn <value>]
[--phone-number <value>]
--message <value>
[--subject <value>]
[--message-structure <value>]
[--message-attributes <value>]
[--message-deduplication-id <value>]
[--message-group-id <value>]
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

`--topic-arn` (string)

The topic you want to publish to.

If you donât specify a value for the `TopicArn` parameter, you must specify a value for the `PhoneNumber` or `TargetArn` parameters.

`--target-arn` (string)

If you donât specify a value for the `TargetArn` parameter, you must specify a value for the `PhoneNumber` or `TopicArn` parameters.

`--phone-number` (string)

The phone number to which you want to deliver an SMS message. Use E.164 format.

If you donât specify a value for the `PhoneNumber` parameter, you must specify a value for the `TargetArn` or `TopicArn` parameters.

`--message` (string)

The message you want to send.

If you are publishing to a topic and you want to send the same message to all transport protocols, include the text of the message as a String value. If you want to send different messages for each transport protocol, set the value of the `MessageStructure` parameter to `json` and use a JSON object for the `Message` parameter.

Constraints:

- With the exception of SMS, messages must be UTF-8 encoded strings and at most 256 KB in size (262,144 bytes, not 262,144 characters).
- For SMS, each message can contain up to 140 characters. This character limit depends on the encoding schema. For example, an SMS message can contain 160 GSM characters, 140 ASCII characters, or 70 UCS-2 characters. If you publish a message that exceeds this size limit, Amazon SNS sends the message as multiple messages, each fitting within the size limit. Messages arenât truncated mid-word but are cut off at whole-word boundaries. The total size limit for a single SMS `Publish` action is 1,600 characters.

JSON-specific constraints:

- Keys in the JSON object that correspond to supported transport protocols must have simple JSON string values.
- The values will be parsed (unescaped) before they are used in outgoing messages.
- Outbound notifications are JSON encoded (meaning that the characters will be reescaped for sending).
- Values have a minimum length of 0 (the empty string, ââ, is allowed).
- Values have a maximum length bounded by the overall message size (so, including multiple protocols may limit message sizes).
- Non-string values will cause the key to be ignored.
- Keys that do not correspond to supported transport protocols are ignored.
- Duplicate keys are not allowed.
- Failure to parse or validate any key or value in the message will cause the `Publish` call to return an error (no partial delivery).

`--subject` (string)

Optional parameter to be used as the âSubjectâ line when the message is delivered to email endpoints. This field will also be included, if present, in the standard JSON messages delivered to other endpoints.

Constraints: Subjects must be UTF-8 text with no line breaks or control characters, and less than 100 characters long.

`--message-structure` (string)

Set `MessageStructure` to `json` if you want to send a different message for each protocol. For example, using one publish action, you can send a short message to your SMS subscribers and a longer message to your email subscribers. If you set `MessageStructure` to `json` , the value of the `Message` parameter must:

- be a syntactically valid JSON object; and
- contain at least a top-level JSON key of âdefaultâ with a value that is a string.

You can define other top-level keys that define the message you want to send to a specific transport protocol (e.g., âhttpâ).

Valid value: `json`

`--message-attributes` (map)

Message attributes for Publish action.

Name -> (string)

Value -> (structure)

The user-specified message attribute value. For string data types, the value attribute has the same restrictions on the content as the message body. For more information, see [Publish](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html) .

Name, type, and value must not be empty or null. In addition, the message body should not be empty or null. All parts of the message attribute, including name, type, and value, are included in the message size restriction, which is currently 256 KB (262,144 bytes). For more information, see [Amazon SNS message attributes](https://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html) and [Publishing to a mobile phone](https://docs.aws.amazon.com/sns/latest/dg/sms_publish-to-phone.html) in the *Amazon SNS Developer Guide.*

DataType -> (string)

Amazon SNS supports the following logical data types: String, String.Array, Number, and Binary. For more information, see [Message Attribute Data Types](https://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html#SNSMessageAttributes.DataTypes) .

StringValue -> (string)

Strings are Unicode with UTF8 binary encoding. For a list of code values, see [ASCII Printable Characters](https://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters) .

BinaryValue -> (blob)

Binary type attributes can store any binary data, for example, compressed data, encrypted data, or images.

Shorthand Syntax:

```
KeyName1=DataType=string,StringValue=string,BinaryValue=blob,KeyName2=DataType=string,StringValue=string,BinaryValue=blob
```

JSON Syntax:

```
{"string": {
      "DataType": "string",
      "StringValue": "string",
      "BinaryValue": blob
    }
  ...}
```

`--message-deduplication-id` (string)

- This parameter applies only to FIFO (first-in-first-out) topics. The `MessageDeduplicationId` can contain up to 128 alphanumeric characters `(a-z, A-Z, 0-9)` and punctuation `(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)` .
- Every message must have a unique `MessageDeduplicationId` , which is a token used for deduplication of sent messages within the 5 minute minimum deduplication interval.
- The scope of deduplication depends on the `FifoThroughputScope` attribute, when set to `Topic` the message deduplication scope is across the entire topic, when set to `MessageGroup` the message deduplication scope is within each individual message group.
- If a message with a particular `MessageDeduplicationId` is sent successfully, subsequent messages within the deduplication scope and interval, with the same `MessageDeduplicationId` , are accepted successfully but arenât delivered.
- Every message must have a unique `MessageDeduplicationId` :
- You may provide a `MessageDeduplicationId` explicitly.
- If you arenât able to provide a `MessageDeduplicationId` and you enable `ContentBasedDeduplication` for your topic, Amazon SNS uses a SHA-256 hash to generate the `MessageDeduplicationId` using the body of the message (but not the attributes of the message).
- If you donât provide a `MessageDeduplicationId` and the topic doesnât have `ContentBasedDeduplication` set, the action fails with an error.
- If the topic has a `ContentBasedDeduplication` set, your `MessageDeduplicationId` overrides the generated one.
- When `ContentBasedDeduplication` is in effect, messages with identical content sent within the deduplication scope and interval are treated as duplicates and only one copy of the message is delivered.
- If you send one message with `ContentBasedDeduplication` enabled, and then another message with a `MessageDeduplicationId` that is the same as the one generated for the first `MessageDeduplicationId` , the two messages are treated as duplicates, within the deduplication scope and interval, and only one copy of the message is delivered.

`--message-group-id` (string)

This parameter applies only to FIFO (first-in-first-out) topics. The `MessageGroupId` can contain up to 128 alphanumeric characters `(a-z, A-Z, 0-9)` and punctuation `(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)` .

The `MessageGroupId` is a tag that specifies that a message belongs to a specific message group. Messages that belong to the same message group are processed in a FIFO manner (however, messages in different message groups might be processed out of order). Every message must include a `MessageGroupId` .

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To publish a message to a topic**

The following `publish` example publishes the specified message to the specified SNS topic. The message comes from a text file, which enables you to include line breaks.

```
aws sns publish \
    --topic-arn "arn:aws:sns:us-west-2:123456789012:my-topic" \
    --message file://message.txt
```

Contents of `message.txt`:

```
Hello World
Second Line
```

Output:

```
{
    "MessageId": "123a45b6-7890-12c3-45d6-111122223333"
}
```

**Example 2: To publish an SMS message to a phone number**

The following `publish` example publishes the message `Hello world!` to the phone number `+1-555-555-0100`.

```
aws sns publish \
    --message "Hello world!" \
    --phone-number +1-555-555-0100
```

Output:

```
{
    "MessageId": "123a45b6-7890-12c3-45d6-333322221111"
}
```

## Output

MessageId -> (string)

Unique identifier assigned to the published message.

Length Constraint: Maximum 100 characters

SequenceNumber -> (string)

This response element applies only to FIFO (first-in-first-out) topics.

The sequence number is a large, non-consecutive number that Amazon SNS assigns to each message. The length of `SequenceNumber` is 128 bits. `SequenceNumber` continues to increase for each `MessageGroupId` .