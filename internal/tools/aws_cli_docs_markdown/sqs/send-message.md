# send-messageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/send-message.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/send-message.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sqs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/index.html#cli-aws-sqs) ]

# send-message

## Description

Delivers a message to the specified queue.

### Warning

A message can include only XML, JSON, and unformatted text. The following Unicode characters are allowed. For more information, see the [W3C specification for characters](http://www.w3.org/TR/REC-xml/#charsets) .

`#x9` | `#xA` | `#xD` | `#x20` to `#xD7FF` | `#xE000` to `#xFFFD` | `#x10000` to `#x10FFFF`

Amazon SQS does not throw an exception or completely reject the message if it contains invalid characters. Instead, it replaces those invalid characters with `U+FFFD` before storing the message in the queue, as long as the message body contains at least one valid character.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/SendMessage)

## Synopsis

```
send-message
--queue-url <value>
--message-body <value>
[--delay-seconds <value>]
[--message-attributes <value>]
[--message-system-attributes <value>]
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

`--queue-url` (string)

The URL of the Amazon SQS queue to which a message is sent.

Queue URLs and names are case-sensitive.

`--message-body` (string)

The message to send. The minimum size is one character. The maximum size is 256 KiB.

### Warning

A message can include only XML, JSON, and unformatted text. The following Unicode characters are allowed. For more information, see the [W3C specification for characters](http://www.w3.org/TR/REC-xml/#charsets) .

`#x9` | `#xA` | `#xD` | `#x20` to `#xD7FF` | `#xE000` to `#xFFFD` | `#x10000` to `#x10FFFF`

Amazon SQS does not throw an exception or completely reject the message if it contains invalid characters. Instead, it replaces those invalid characters with `U+FFFD` before storing the message in the queue, as long as the message body contains at least one valid character.

`--delay-seconds` (integer)

The length of time, in seconds, for which to delay a specific message. Valid values: 0 to 900. Maximum: 15 minutes. Messages with a positive `DelaySeconds` value become available for processing after the delay period is finished. If you donât specify a value, the default value for the queue applies.

### Note

When you set `FifoQueue` , you canât set `DelaySeconds` per message. You can set this parameter only on a queue level.

`--message-attributes` (map)

Each message attribute consists of a `Name` , `Type` , and `Value` . For more information, see [Amazon SQS message attributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html#sqs-message-attributes) in the *Amazon SQS Developer Guide* .

key -> (string)

value -> (structure)

The user-specified message attribute value. For string data types, the `Value` attribute has the same restrictions on the content as the message body. For more information, see ``  SendMessage .``

`Name` , `type` , `value` and the message body must not be empty or null. All parts of the message attribute, including `Name` , `Type` , and `Value` , are part of the message size restriction (256 KiB or 262,144 bytes).

StringValue -> (string)

Strings are Unicode with UTF-8 binary encoding. For a list of code values, see [ASCII Printable Characters](http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters) .

BinaryValue -> (blob)

Binary type attributes can store any binary data, such as compressed data, encrypted data, or images.

StringListValues -> (list)

Not implemented. Reserved for future use.

(string)

BinaryListValues -> (list)

Not implemented. Reserved for future use.

(blob)

DataType -> (string)

Amazon SQS supports the following logical data types: `String` , `Number` , and `Binary` . For the `Number` data type, you must use `StringValue` .

You can also append custom labels. For more information, see [Amazon SQS Message Attributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html#sqs-message-attributes) in the *Amazon SQS Developer Guide* .

Shorthand Syntax:

```
KeyName1=StringValue=string,BinaryValue=blob,StringListValues=string,string,BinaryListValues=blob,blob,DataType=string,KeyName2=StringValue=string,BinaryValue=blob,StringListValues=string,string,BinaryListValues=blob,blob,DataType=string
```

JSON Syntax:

```
{"string": {
      "StringValue": "string",
      "BinaryValue": blob,
      "StringListValues": ["string", ...],
      "BinaryListValues": [blob, ...],
      "DataType": "string"
    }
  ...}
```

`--message-system-attributes` (map)

The message system attribute to send. Each message system attribute consists of a `Name` , `Type` , and `Value` .

### Warning

- Currently, the only supported message system attribute is `AWSTraceHeader` . Its type must be `String` and its value must be a correctly formatted X-Ray trace header string.
- The size of a message system attribute doesnât count towards the total size of a message.

key -> (string)

value -> (structure)

The user-specified message system attribute value. For string data types, the `Value` attribute has the same restrictions on the content as the message body. For more information, see ``  SendMessage .``

`Name` , `type` , `value` and the message body must not be empty or null.

StringValue -> (string)

Strings are Unicode with UTF-8 binary encoding. For a list of code values, see [ASCII Printable Characters](http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters) .

BinaryValue -> (blob)

Binary type attributes can store any binary data, such as compressed data, encrypted data, or images.

StringListValues -> (list)

Not implemented. Reserved for future use.

(string)

BinaryListValues -> (list)

Not implemented. Reserved for future use.

(blob)

DataType -> (string)

Amazon SQS supports the following logical data types: `String` , `Number` , and `Binary` . For the `Number` data type, you must use `StringValue` .

You can also append custom labels. For more information, see [Amazon SQS Message Attributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html#sqs-message-attributes) in the *Amazon SQS Developer Guide* .

Shorthand Syntax:

```
KeyName1=StringValue=string,BinaryValue=blob,StringListValues=string,string,BinaryListValues=blob,blob,DataType=string,KeyName2=StringValue=string,BinaryValue=blob,StringListValues=string,string,BinaryListValues=blob,blob,DataType=string

Where valid key names are:
  AWSTraceHeader
```

JSON Syntax:

```
{"AWSTraceHeader": {
      "StringValue": "string",
      "BinaryValue": blob,
      "StringListValues": ["string", ...],
      "BinaryListValues": [blob, ...],
      "DataType": "string"
    }
  ...}
```

`--message-deduplication-id` (string)

This parameter applies only to FIFO (first-in-first-out) queues.

The token used for deduplication of sent messages. If a message with a particular `MessageDeduplicationId` is sent successfully, any messages sent with the same `MessageDeduplicationId` are accepted successfully but arenât delivered during the 5-minute deduplication interval. For more information, see [Exactly-once processing](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html) in the *Amazon SQS Developer Guide* .

- Every message must have a unique `MessageDeduplicationId` ,
- You may provide a `MessageDeduplicationId` explicitly.
- If you arenât able to provide a `MessageDeduplicationId` and you enable `ContentBasedDeduplication` for your queue, Amazon SQS uses a SHA-256 hash to generate the `MessageDeduplicationId` using the body of the message (but not the attributes of the message).
- If you donât provide a `MessageDeduplicationId` and the queue doesnât have `ContentBasedDeduplication` set, the action fails with an error.
- If the queue has `ContentBasedDeduplication` set, your `MessageDeduplicationId` overrides the generated one.
- When `ContentBasedDeduplication` is in effect, messages with identical content sent within the deduplication interval are treated as duplicates and only one copy of the message is delivered.
- If you send one message with `ContentBasedDeduplication` enabled and then another message with a `MessageDeduplicationId` that is the same as the one generated for the first `MessageDeduplicationId` , the two messages are treated as duplicates and only one copy of the message is delivered.

### Note

The `MessageDeduplicationId` is available to the consumer of the message (this can be useful for troubleshooting delivery issues).

If a message is sent successfully but the acknowledgement is lost and the message is resent with the same `MessageDeduplicationId` after the deduplication interval, Amazon SQS canât detect duplicate messages.

Amazon SQS continues to keep track of the message deduplication ID even after the message is received and deleted.

The maximum length of `MessageDeduplicationId` is 128 characters. `MessageDeduplicationId` can contain alphanumeric characters (`a-z` , `A-Z` , `0-9` ) and punctuation (`!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~` ).

For best practices of using `MessageDeduplicationId` , see [Using the MessageDeduplicationId Property](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html) in the *Amazon SQS Developer Guide* .

`--message-group-id` (string)

This parameter applies only to FIFO (first-in-first-out) queues.

The tag that specifies that a message belongs to a specific message group. Messages that belong to the same message group are processed in a FIFO manner (however, messages in different message groups might be processed out of order). To interleave multiple ordered streams within a single queue, use `MessageGroupId` values (for example, session data for multiple users). In this scenario, multiple consumers can process the queue, but the session data of each user is processed in a FIFO fashion.

- You must associate a non-empty `MessageGroupId` with a message. If you donât provide a `MessageGroupId` , the action fails.
- `ReceiveMessage` might return messages with multiple `MessageGroupId` values. For each `MessageGroupId` , the messages are sorted by time sent. The caller canât specify a `MessageGroupId` .

The maximum length of `MessageGroupId` is 128 characters. Valid values: alphanumeric characters and punctuation `(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)` .

For best practices of using `MessageGroupId` , see [Using the MessageGroupId Property](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagegroupid-property.html) in the *Amazon SQS Developer Guide* .

### Warning

`MessageGroupId` is required for FIFO queues. You canât use it for Standard queues.

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

**To send a message**

This example sends a message with the specified message body, delay period, and message attributes, to the specified queue.

Command:

```
aws sqs send-message --queue-url https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue --message-body "Information about the largest city in Any Region." --delay-seconds 10 --message-attributes file://send-message.json
```

Input file (send-message.json):

```
{
  "City": {
    "DataType": "String",
    "StringValue": "Any City"
  },
  "Greeting": {
    "DataType": "Binary",
    "BinaryValue": "Hello, World!"
  },
  "Population": {
    "DataType": "Number",
    "StringValue": "1250800"
  }
}
```

Output:

```
{
  "MD5OfMessageBody": "51b0a325...39163aa0",
  "MD5OfMessageAttributes": "00484c68...59e48f06",
  "MessageId": "da68f62c-0c07-4bee-bf5f-7e856EXAMPLE"
}
```

## Output

MD5OfMessageBody -> (string)

An MD5 digest of the non-URL-encoded message body string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see [RFC1321](https://www.ietf.org/rfc/rfc1321.txt) .

MD5OfMessageAttributes -> (string)

An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see [RFC1321](https://www.ietf.org/rfc/rfc1321.txt) .

MD5OfMessageSystemAttributes -> (string)

An MD5 digest of the non-URL-encoded message system attribute string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest.

MessageId -> (string)

An attribute containing the `MessageId` of the message sent to the queue. For more information, see [Queue and Message Identifiers](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-message-identifiers.html) in the *Amazon SQS Developer Guide* .

SequenceNumber -> (string)

This parameter applies only to FIFO (first-in-first-out) queues.

The large, non-consecutive number that Amazon SQS assigns to each message.

The length of `SequenceNumber` is 128 bits. `SequenceNumber` continues to increase for a particular `MessageGroupId` .