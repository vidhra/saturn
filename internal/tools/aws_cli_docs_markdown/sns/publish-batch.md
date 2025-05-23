# publish-batchÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/publish-batch.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/publish-batch.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sns](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/index.html#cli-aws-sns) ]

# publish-batch

## Description

Publishes up to ten messages to the specified topic. This is a batch version of `Publish` . For FIFO topics, multiple messages within a single batch are published in the order they are sent, and messages are deduplicated within the batch and across batches for 5 minutes.

The result of publishing each message is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of `200` .

The maximum allowed individual message size and the maximum total payload size (the sum of the individual lengths of all of the batched messages) are both 256 KB (262,144 bytes).

Some actions take lists of parameters. These lists are specified using the `param.n` notation. Values of `n` are integers starting from 1. For example, a parameter list with two elements looks like this:

&AttributeName.1=first

&AttributeName.2=second

If you send a batch message to a topic, Amazon SNS publishes the batch message to each endpoint that is subscribed to the topic. The format of the batch message depends on the notification protocol for each subscribed endpoint.

When a `messageId` is returned, the batch message is saved and Amazon SNS immediately delivers the message to subscribers.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/PublishBatch)

## Synopsis

```
publish-batch
--topic-arn <value>
--publish-batch-request-entries <value>
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

The Amazon resource name (ARN) of the topic you want to batch publish to.

`--publish-batch-request-entries` (list)

A list of `PublishBatch` request entries to be sent to the SNS topic.

(structure)

Contains the details of a single Amazon SNS message along with an `Id` that identifies a message within the batch.

Id -> (string)

An identifier for the message in this batch.

### Note

The `Ids` of a batch request must be unique within a request.

This identifier can have up to 80 characters. The following characters are accepted: alphanumeric characters, hyphens(-), and underscores (_).

Message -> (string)

The body of the message.

Subject -> (string)

The subject of the batch message.

MessageStructure -> (string)

Set `MessageStructure` to `json` if you want to send a different message for each protocol. For example, using one publish action, you can send a short message to your SMS subscribers and a longer message to your email subscribers. If you set `MessageStructure` to `json` , the value of the `Message` parameter must:

- be a syntactically valid JSON object; and
- contain at least a top-level JSON key of âdefaultâ with a value that is a string.

You can define other top-level keys that define the message you want to send to a specific transport protocol (e.g. http).

MessageAttributes -> (map)

Each message attribute consists of a `Name` , `Type` , and `Value` . For more information, see [Amazon SNS message attributes](https://docs.aws.amazon.com/sns/latest/dg/sns-message-attributes.html) in the Amazon SNS Developer Guide.

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

MessageDeduplicationId -> (string)

This parameter applies only to FIFO (first-in-first-out) topics.

- This parameter applies only to FIFO (first-in-first-out) topics. The `MessageDeduplicationId` can contain up to 128 alphanumeric characters `(a-z, A-Z, 0-9)` and punctuation `(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)` .
- Every message must have a unique `MessageDeduplicationId` , which is a token used for deduplication of sent messages within the 5 minute minimum deduplication interval.
- The scope of deduplication depends on the `FifoThroughputScope` attribute, when set to `Topic` the message deduplication scope is across the entire topic, when set to `MessageGroup` the message deduplication scope is within each individual message group.
- If a message with a particular `MessageDeduplicationId` is sent successfully, subsequent messages within the deduplication scope and interval, with the same `MessageDeduplicationId` , are accepted successfully but arenât delivered.
- Every message must have a unique `MessageDeduplicationId` .
- You may provide a `MessageDeduplicationId` explicitly.
- If you arenât able to provide a `MessageDeduplicationId` and you enable `ContentBasedDeduplication` for your topic, Amazon SNS uses a SHA-256 hash to generate the `MessageDeduplicationId` using the body of the message (but not the attributes of the message).
- If you donât provide a `MessageDeduplicationId` and the topic doesnât have `ContentBasedDeduplication` set, the action fails with an error.
- If the topic has a `ContentBasedDeduplication` set, your `MessageDeduplicationId` overrides the generated one.
- When `ContentBasedDeduplication` is in effect, messages with identical content sent within the deduplication scope and interval are treated as duplicates and only one copy of the message is delivered.
- If you send one message with `ContentBasedDeduplication` enabled, and then another message with a `MessageDeduplicationId` that is the same as the one generated for the first `MessageDeduplicationId` , the two messages are treated as duplicates, within the deduplication scope and interval, and only one copy of the message is delivered.

### Note

The `MessageDeduplicationId` is available to the consumer of the message (this can be useful for troubleshooting delivery issues).

If a message is sent successfully but the acknowledgement is lost and the message is resent with the same `MessageDeduplicationId` after the deduplication interval, Amazon SNS canât detect duplicate messages.

Amazon SNS continues to keep track of the message deduplication ID even after the message is received and deleted.

MessageGroupId -> (string)

This parameter applies only to FIFO (first-in-first-out) topics.

The tag that specifies that a message belongs to a specific message group. Messages that belong to the same message group are processed in a FIFO manner (however, messages in different message groups might be processed out of order). To interleave multiple ordered streams within a single topic, use `MessageGroupId` values (for example, session data for multiple users). In this scenario, multiple consumers can process the topic, but the session data of each user is processed in a FIFO fashion.

You must associate a non-empty `MessageGroupId` with a message. If you donât provide a `MessageGroupId` , the action fails.

The length of `MessageGroupId` is 128 characters.

`MessageGroupId` can contain alphanumeric characters `(a-z, A-Z, 0-9)` and punctuation `(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)` .

### Warning

`MessageGroupId` is required for FIFO topics. You canât use it for standard topics.

Shorthand Syntax:

```
Id=string,Message=string,Subject=string,MessageStructure=string,MessageAttributes={KeyName1={DataType=string,StringValue=string,BinaryValue=blob},KeyName2={DataType=string,StringValue=string,BinaryValue=blob}},MessageDeduplicationId=string,MessageGroupId=string ...
```

JSON Syntax:

```
[
  {
    "Id": "string",
    "Message": "string",
    "Subject": "string",
    "MessageStructure": "string",
    "MessageAttributes": {"string": {
          "DataType": "string",
          "StringValue": "string",
          "BinaryValue": blob
        }
      ...},
    "MessageDeduplicationId": "string",
    "MessageGroupId": "string"
  }
  ...
]
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

Successful -> (list)

A list of successful `PublishBatch` responses.

(structure)

Encloses data related to a successful message in a batch request for topic.

Id -> (string)

The `Id` of an entry in a batch request.

MessageId -> (string)

An identifier for the message.

SequenceNumber -> (string)

This parameter applies only to FIFO (first-in-first-out) topics.

The large, non-consecutive number that Amazon SNS assigns to each message.

The length of `SequenceNumber` is 128 bits. `SequenceNumber` continues to increase for a particular `MessageGroupId` .

Failed -> (list)

A list of failed `PublishBatch` responses.

(structure)

Gives a detailed description of failed messages in the batch.

Id -> (string)

The `Id` of an entry in a batch request

Code -> (string)

An error code representing why the action failed on this entry.

Message -> (string)

A message explaining why the action failed on this entry.

SenderFault -> (boolean)

Specifies whether the error happened due to the caller of the batch API action.