# create-topicÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/create-topic.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/create-topic.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sns](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/index.html#cli-aws-sns) ]

# create-topic

## Description

Creates a topic to which notifications can be published. Users can create at most 100,000 standard topics (at most 1,000 FIFO topics). For more information, see [Creating an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html) in the *Amazon SNS Developer Guide* . This action is idempotent, so if the requester already owns a topic with the specified name, that topicâs ARN is returned without creating a new topic.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/CreateTopic)

## Synopsis

```
create-topic
--name <value>
[--attributes <value>]
[--tags <value>]
[--data-protection-policy <value>]
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

`--name` (string)

The name of the topic you want to create.

Constraints: Topic names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long.

For a FIFO (first-in-first-out) topic, the name must end with the `.fifo` suffix.

`--attributes` (map)

A map of attributes with their corresponding values.

The following lists names, descriptions, and values of the special request parameters that the `CreateTopic` action uses:

- `DeliveryPolicy` â The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.
- `DisplayName` â The display name to use for a topic with SMS subscriptions.
- `FifoTopic` â Set to true to create a FIFO topic.
- `Policy` â The policy that defines who can access your topic. By default, only the topic owner can publish or subscribe to the topic.
- `SignatureVersion` â The signature version corresponds to the hashing algorithm used while creating the signature of the notifications, subscription confirmations, or unsubscribe confirmation messages sent by Amazon SNS. By default, `SignatureVersion` is set to `1` .
- `TracingConfig` â Tracing mode of an Amazon SNS topic. By default `TracingConfig` is set to `PassThrough` , and the topic passes through the tracing header it receives from an Amazon SNS publisher to its subscriptions. If set to `Active` , Amazon SNS will vend X-Ray segment data to topic owner account if the sampled flag in the tracing header is true. This is only supported on standard topics.

The following attribute applies only to [server-side encryption](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html) :

- `KmsMasterKeyId` â The ID of an Amazon Web Services managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms) . For more examples, see [KeyId](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters) in the *Key Management Service API Reference* .

The following attributes apply only to [FIFO topics](https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html) :

- `ArchivePolicy` â The policy that sets the retention period for messages stored in the message archive of an Amazon SNS FIFO topic.
- `ContentBasedDeduplication` â Enables content-based deduplication for FIFO topics.
- By default, `ContentBasedDeduplication` is set to `false` . If you create a FIFO topic and this attribute is `false` , you must specify a value for the `MessageDeduplicationId` parameter for the [Publish](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html) action.
- When you set `ContentBasedDeduplication` to `true` , Amazon SNS uses a SHA-256 hash to generate the `MessageDeduplicationId` using the body of the message (but not the attributes of the message). (Optional) To override the generated value, you can specify a value for the `MessageDeduplicationId` parameter for the `Publish` action.
- `FifoThroughputScope` â Enables higher throughput for your FIFO topic by adjusting the scope of deduplication. This attribute has two possible values:
- `Topic` â The scope of message deduplication is across the entire topic. This is the default value and maintains existing behavior, with a maximum throughput of 3000 messages per second or 20MB per second, whichever comes first.
- `MessageGroup` â The scope of deduplication is within each individual message group, which enables higher throughput per topic subject to regional quotas. For more information on quotas or to request an increase, see [Amazon SNS service quotas](https://docs.aws.amazon.com/general/latest/gr/sns.html) in the Amazon Web Services General Reference.

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

`--tags` (list)

The list of tags to add to a new topic.

### Note

To be able to tag a topic on creation, you must have the `sns:CreateTopic` and `sns:TagResource` permissions.

(structure)

The list of tags to be added to the specified topic.

Key -> (string)

The required key portion of the tag.

Value -> (string)

The optional value portion of the tag.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--data-protection-policy` (string)

The body of the policy document you want to use for this topic.

You can only add one policy per topic.

The policy must be in JSON string format.

Length Constraints: Maximum length of 30,720.

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

**To create an SNS topic**

The following `create-topic` example creates an SNS topic named `my-topic`.

```
aws sns create-topic \
    --name my-topic
```

Output:

```
{
    "ResponseMetadata": {
        "RequestId": "1469e8d7-1642-564e-b85d-a19b4b341f83"
    },
    "TopicArn": "arn:aws:sns:us-west-2:123456789012:my-topic"
}
```

For more information, see [Using the AWS Command Line Interface with Amazon SQS and Amazon SNS](https://docs.aws.amazon.com/cli/latest/userguide/cli-sqs-queue-sns-topic.html) in the *AWS Command Line Interface User Guide*.

## Output

TopicArn -> (string)

The Amazon Resource Name (ARN) assigned to the created topic.