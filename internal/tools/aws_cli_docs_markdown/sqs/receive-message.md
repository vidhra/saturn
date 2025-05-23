# receive-messageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/receive-message.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/receive-message.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sqs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/index.html#cli-aws-sqs) ]

# receive-message

## Description

Retrieves one or more messages (up to 10), from the specified queue. Using the `WaitTimeSeconds` parameter enables long-poll support. For more information, see [Amazon SQS Long Polling](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-long-polling.html) in the *Amazon SQS Developer Guide* .

Short poll is the default behavior where a weighted random set of machines is sampled on a `ReceiveMessage` call. Therefore, only the messages on the sampled machines are returned. If the number of messages in the queue is small (fewer than 1,000), you most likely get fewer messages than you requested per `ReceiveMessage` call. If the number of messages in the queue is extremely small, you might not receive any messages in a particular `ReceiveMessage` response. If this happens, repeat the request.

For each message returned, the response includes the following:

- The message body.
- An MD5 digest of the message body. For information about MD5, see [RFC1321](https://www.ietf.org/rfc/rfc1321.txt) .
- The `MessageId` you received when you sent the message to the queue.
- The receipt handle.
- The message attributes.
- An MD5 digest of the message attributes.

The receipt handle is the identifier you must provide when deleting the message. For more information, see [Queue and Message Identifiers](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-message-identifiers.html) in the *Amazon SQS Developer Guide* .

You can provide the `VisibilityTimeout` parameter in your request. The parameter is applied to the messages that Amazon SQS returns in the response. If you donât include the parameter, the overall visibility timeout for the queue is used for the returned messages. The default visibility timeout for a queue is 30 seconds.

### Note

In the future, new attributes might be added. If you write code that calls this action, we recommend that you structure your code so that it can handle new attributes gracefully.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sqs-2012-11-05/ReceiveMessage)

## Synopsis

```
receive-message
--queue-url <value>
[--attribute-names <value>]
[--message-system-attribute-names <value>]
[--message-attribute-names <value>]
[--max-number-of-messages <value>]
[--visibility-timeout <value>]
[--wait-time-seconds <value>]
[--receive-request-attempt-id <value>]
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

The URL of the Amazon SQS queue from which messages are received.

Queue URLs and names are case-sensitive.

`--attribute-names` (list)

### Warning

This parameter has been discontinued but will be supported for backward compatibility. To provide attribute names, you are encouraged to use `MessageSystemAttributeNames` .

A list of attributes that need to be returned along with each message. These attributes include:

- `All` â Returns all values.
- `ApproximateFirstReceiveTimestamp` â Returns the time the message was first received from the queue ([epoch time](http://en.wikipedia.org/wiki/Unix_time) in milliseconds).
- `ApproximateReceiveCount` â Returns the number of times a message has been received across all queues but not deleted.
- `AWSTraceHeader` â Returns the X-Ray trace header string.
- `SenderId`
- For a user, returns the user ID, for example `ABCDEFGHI1JKLMNOPQ23R` .
- For an IAM role, returns the IAM role ID, for example `ABCDE1F2GH3I4JK5LMNOP:i-a123b456` .
- `SentTimestamp` â Returns the time the message was sent to the queue ([epoch time](http://en.wikipedia.org/wiki/Unix_time) in milliseconds).
- `SqsManagedSseEnabled` â Enables server-side queue encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (for example, [SSE-KMS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sse-existing-queue.html) or [SSE-SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sqs-sse-queue.html) ).
- `MessageDeduplicationId` â Returns the value provided by the producer that calls the ``  SendMessage `` action.
- `MessageGroupId` â Returns the value provided by the producer that calls the ``  SendMessage `` action. Messages with the same `MessageGroupId` are returned in sequence.
- `SequenceNumber` â Returns the value provided by Amazon SQS.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  All
  Policy
  VisibilityTimeout
  MaximumMessageSize
  MessageRetentionPeriod
  ApproximateNumberOfMessages
  ApproximateNumberOfMessagesNotVisible
  CreatedTimestamp
  LastModifiedTimestamp
  QueueArn
  ApproximateNumberOfMessagesDelayed
  DelaySeconds
  ReceiveMessageWaitTimeSeconds
  RedrivePolicy
  FifoQueue
  ContentBasedDeduplication
  KmsMasterKeyId
  KmsDataKeyReusePeriodSeconds
  DeduplicationScope
  FifoThroughputLimit
  RedriveAllowPolicy
  SqsManagedSseEnabled
```

`--message-system-attribute-names` (list)

A list of attributes that need to be returned along with each message. These attributes include:

- `All` â Returns all values.
- `ApproximateFirstReceiveTimestamp` â Returns the time the message was first received from the queue ([epoch time](http://en.wikipedia.org/wiki/Unix_time) in milliseconds).
- `ApproximateReceiveCount` â Returns the number of times a message has been received across all queues but not deleted.
- `AWSTraceHeader` â Returns the X-Ray trace header string.
- `SenderId`
- For a user, returns the user ID, for example `ABCDEFGHI1JKLMNOPQ23R` .
- For an IAM role, returns the IAM role ID, for example `ABCDE1F2GH3I4JK5LMNOP:i-a123b456` .
- `SentTimestamp` â Returns the time the message was sent to the queue ([epoch time](http://en.wikipedia.org/wiki/Unix_time) in milliseconds).
- `SqsManagedSseEnabled` â Enables server-side queue encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (for example, [SSE-KMS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sse-existing-queue.html) or [SSE-SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sqs-sse-queue.html) ).
- `MessageDeduplicationId` â Returns the value provided by the producer that calls the ``  SendMessage `` action.
- `MessageGroupId` â Returns the value provided by the producer that calls the ``  SendMessage `` action. Messages with the same `MessageGroupId` are returned in sequence.
- `SequenceNumber` â Returns the value provided by Amazon SQS.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  All
  SenderId
  SentTimestamp
  ApproximateReceiveCount
  ApproximateFirstReceiveTimestamp
  SequenceNumber
  MessageDeduplicationId
  MessageGroupId
  AWSTraceHeader
  DeadLetterQueueSourceArn
```

`--message-attribute-names` (list)

The name of the message attribute, where *N* is the index.

- The name can contain alphanumeric characters and the underscore (`_` ), hyphen (`-` ), and period (`.` ).
- The name is case-sensitive and must be unique among all attribute names for the message.
- The name must not start with AWS-reserved prefixes such as `AWS.` or `Amazon.` (or any casing variants).
- The name must not start or end with a period (`.` ), and it should not have periods in succession (`..` ).
- The name can be up to 256 characters long.

When using `ReceiveMessage` , you can send a list of attribute names to receive, or you can return all of the attributes by specifying `All` or `.*` in your request. You can also use all message attributes starting with a prefix, for example `bar.*` .

(string)

Syntax:

```
"string" "string" ...
```

`--max-number-of-messages` (integer)

The maximum number of messages to return. Amazon SQS never returns more messages than this value (however, fewer messages might be returned). Valid values: 1 to 10. Default: 1.

`--visibility-timeout` (integer)

The duration (in seconds) that the received messages are hidden from subsequent retrieve requests after being retrieved by a `ReceiveMessage` request. If not specified, the default visibility timeout for the queue is used, which is 30 seconds.

Understanding `VisibilityTimeout` :

- When a message is received from a queue, it becomes temporarily invisible to other consumers for the duration of the visibility timeout. This prevents multiple consumers from processing the same message simultaneously. If the message is not deleted or its visibility timeout is not extended before the timeout expires, it becomes visible again and can be retrieved by other consumers.
- Setting an appropriate visibility timeout is crucial. If itâs too short, the message might become visible again before processing is complete, leading to duplicate processing. If itâs too long, it delays the reprocessing of messages if the initial processing fails.
- You can adjust the visibility timeout using the `--visibility-timeout` parameter in the `receive-message` command to match the processing time required by your application.
- A message that isnât deleted or a message whose visibility isnât extended before the visibility timeout expires counts as a failed receive. Depending on the configuration of the queue, the message might be sent to the dead-letter queue.

For more information, see [Visibility Timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) in the *Amazon SQS Developer Guide* .

`--wait-time-seconds` (integer)

The duration (in seconds) for which the call waits for a message to arrive in the queue before returning. If a message is available, the call returns sooner than `WaitTimeSeconds` . If no messages are available and the wait time expires, the call does not return a message list. If you are using the Java SDK, it returns a `ReceiveMessageResponse` object, which has a empty list instead of a Null object.

### Warning

To avoid HTTP errors, ensure that the HTTP response timeout for `ReceiveMessage` requests is longer than the `WaitTimeSeconds` parameter. For example, with the Java SDK, you can set HTTP transport settings using the [NettyNioAsyncHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/nio/netty/NettyNioAsyncHttpClient.html) for asynchronous clients, or the [ApacheHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/apache/ApacheHttpClient.html) for synchronous clients.

`--receive-request-attempt-id` (string)

This parameter applies only to FIFO (first-in-first-out) queues.

The token used for deduplication of `ReceiveMessage` calls. If a networking issue occurs after a `ReceiveMessage` action, and instead of a response you receive a generic error, it is possible to retry the same action with an identical `ReceiveRequestAttemptId` to retrieve the same set of messages, even if their visibility timeout has not yet expired.

- You can use `ReceiveRequestAttemptId` only for 5 minutes after a `ReceiveMessage` action.
- When you set `FifoQueue` , a caller of the `ReceiveMessage` action can provide a `ReceiveRequestAttemptId` explicitly.
- It is possible to retry the `ReceiveMessage` action with the same `ReceiveRequestAttemptId` if none of the messages have been modified (deleted or had their visibility changes).
- During a visibility timeout, subsequent calls with the same `ReceiveRequestAttemptId` return the same messages and receipt handles. If a retry occurs within the deduplication interval, it resets the visibility timeout. For more information, see [Visibility Timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) in the *Amazon SQS Developer Guide* .

### Warning

If a caller of the `ReceiveMessage` action still processes messages when the visibility timeout expires and messages become visible, another worker consuming from the same queue can receive the same messages and therefore process duplicates. Also, if a consumer whose message processing time is longer than the visibility timeout tries to delete the processed messages, the action fails with an error. To mitigate this effect, ensure that your application observes a safe threshold before the visibility timeout expires and extend the visibility timeout as necessary.

- While messages with a particular `MessageGroupId` are invisible, no more messages belonging to the same `MessageGroupId` are returned until the visibility timeout expires. You can still receive messages with another `MessageGroupId` as long as it is also visible.
- If a caller of `ReceiveMessage` canât track the `ReceiveRequestAttemptId` , no retries work until the original visibility timeout expires. As a result, delays might occur but the messages in the queue remain in a strict order.

The maximum length of `ReceiveRequestAttemptId` is 128 characters. `ReceiveRequestAttemptId` can contain alphanumeric characters (`a-z` , `A-Z` , `0-9` ) and punctuation (`!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~` ).

For best practices of using `ReceiveRequestAttemptId` , see [Using the ReceiveRequestAttemptId Request Parameter](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-receiverequestattemptid-request-parameter.html) in the *Amazon SQS Developer Guide* .

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

**To receive a message**

This example receives up to 10 available messages, returning all available attributes.

Command:

```
aws sqs receive-message --queue-url https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue --attribute-names All --message-attribute-names All --max-number-of-messages 10
```

Output:

```
{
  "Messages": [
    {
      "Body": "My first message.",
      "ReceiptHandle": "AQEBzbVv...fqNzFw==",
      "MD5OfBody": "1000f835...a35411fa",
      "MD5OfMessageAttributes": "9424c491...26bc3ae7",
      "MessageId": "d6790f8d-d575-4f01-bc51-40122EXAMPLE",
      "Attributes": {
        "ApproximateFirstReceiveTimestamp": "1442428276921",
        "SenderId": "AIDAIAZKMSNQ7TEXAMPLE",
        "ApproximateReceiveCount": "5",
        "SentTimestamp": "1442428276921"
      },
      "MessageAttributes": {
        "PostalCode": {
          "DataType": "String",
          "StringValue": "ABC123"
        },
        "City": {
          "DataType": "String",
          "StringValue": "Any City"
        }
      }
    }
  ]
}
```

This example receives the next available message, returning only the SenderId and SentTimestamp attributes as well as the PostalCode message attribute.

Command:

```
aws sqs receive-message --queue-url https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue --attribute-names SenderId SentTimestamp --message-attribute-names PostalCode
```

Output:

```
{
  "Messages": [
    {
      "Body": "My first message.",
      "ReceiptHandle": "AQEB6nR4...HzlvZQ==",
      "MD5OfBody": "1000f835...a35411fa",
      "MD5OfMessageAttributes": "b8e89563...e088e74f",
      "MessageId": "d6790f8d-d575-4f01-bc51-40122EXAMPLE",
      "Attributes": {
        "SenderId": "AIDAIAZKMSNQ7TEXAMPLE",
        "SentTimestamp": "1442428276921"
      },
      "MessageAttributes": {
        "PostalCode": {
          "DataType": "String",
          "StringValue": "ABC123"
        }
      }
    }
  ]
}
```

## Output

Messages -> (list)

A list of messages.

(structure)

An Amazon SQS message.

MessageId -> (string)

A unique identifier for the message. A `MessageId` is considered unique across all Amazon Web Services accounts for an extended period of time.

ReceiptHandle -> (string)

An identifier associated with the act of receiving the message. A new receipt handle is returned every time you receive a message. When deleting a message, you provide the last received receipt handle to delete the message.

MD5OfBody -> (string)

An MD5 digest of the non-URL-encoded message body string.

Body -> (string)

The messageâs contents (not URL-encoded).

Attributes -> (map)

A map of the attributes requested in ``  ReceiveMessage `` to their respective values. Supported attributes:

- `ApproximateReceiveCount`
- `ApproximateFirstReceiveTimestamp`
- `MessageDeduplicationId`
- `MessageGroupId`
- `SenderId`
- `SentTimestamp`
- `SequenceNumber`

`ApproximateFirstReceiveTimestamp` and `SentTimestamp` are each returned as an integer representing the [epoch time](http://en.wikipedia.org/wiki/Unix_time) in milliseconds.

key -> (string)

value -> (string)

MD5OfMessageAttributes -> (string)

An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see [RFC1321](https://www.ietf.org/rfc/rfc1321.txt) .

MessageAttributes -> (map)

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