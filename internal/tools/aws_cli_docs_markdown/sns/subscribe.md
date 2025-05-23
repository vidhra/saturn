# subscribeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/subscribe.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/subscribe.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sns](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/index.html#cli-aws-sns) ]

# subscribe

## Description

Subscribes an endpoint to an Amazon SNS topic. If the endpoint type is HTTP/S or email, or if the endpoint and the topic are not in the same Amazon Web Services account, the endpoint owner must run the `ConfirmSubscription` action to confirm the subscription.

You call the `ConfirmSubscription` action with the token from the subscription response. Confirmation tokens are valid for two days.

This action is throttled at 100 transactions per second (TPS).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/Subscribe)

## Synopsis

```
subscribe
--topic-arn <value>
--protocol <value>
[--attributes <value>]
[--return-subscription-arn | --no-return-subscription-arn]
[--notification-endpoint <value>]
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

The ARN of the topic you want to subscribe to.

`--protocol` (string)

The protocol that you want to use. Supported protocols include:

- `http` â delivery of JSON-encoded message via HTTP POST
- `https` â delivery of JSON-encoded message via HTTPS POST
- `email` â delivery of message via SMTP
- `email-json` â delivery of JSON-encoded message via SMTP
- `sms` â delivery of message via SMS
- `sqs` â delivery of JSON-encoded message to an Amazon SQS queue
- `application` â delivery of JSON-encoded message to an EndpointArn for a mobile app and device
- `lambda` â delivery of JSON-encoded message to an Lambda function
- `firehose` â delivery of JSON-encoded message to an Amazon Kinesis Data Firehose delivery stream.

`--attributes` (map)

A map of attributes with their corresponding values.

The following lists the names, descriptions, and values of the special request parameters that the `Subscribe` action uses:

- `DeliveryPolicy` â The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.
- `FilterPolicy` â The simple JSON object that lets your subscriber receive only a subset of messages, rather than receiving every message published to the topic.
- `FilterPolicyScope` â This attribute lets you choose the filtering scope by using one of the following string value types:
- `MessageAttributes` (default) â The filter is applied on the message attributes.
- `MessageBody` â The filter is applied on the message body.
- `RawMessageDelivery` â When set to `true` , enables raw message delivery to Amazon SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON formatting, which is otherwise created for Amazon SNS metadata.
- `RedrivePolicy` â When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue. Messages that canât be delivered due to client errors (for example, when the subscribed endpoint is unreachable) or server errors (for example, when the service that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue for further analysis or reprocessing.

The following attribute applies only to Amazon Data Firehose delivery stream subscriptions:

- `SubscriptionRoleArn` â The ARN of the IAM role that has the following:
- Permission to write to the Firehose delivery stream
- Amazon SNS listed as a trusted entity

Specifying a valid ARN for this attribute is required for Firehose delivery stream subscriptions. For more information, see [Fanout to Firehose delivery streams](https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html) in the *Amazon SNS Developer Guide* .

The following attributes apply only to [FIFO topics](https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html) :

- `ReplayPolicy` â Adds or updates an inline policy document for a subscription to replay messages stored in the specified Amazon SNS topic.
- `ReplayStatus` â Retrieves the status of the subscription message replay, which can be one of the following:
- `Completed` â The replay has successfully redelivered all messages, and is now delivering newly published messages. If an ending point was specified in the `ReplayPolicy` then the subscription will no longer receive newly published messages.
- `In progress` â The replay is currently replaying the selected messages.
- `Failed` â The replay was unable to complete.
- `Pending` â The default state while the replay initiates.

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

`--return-subscription-arn` | `--no-return-subscription-arn` (boolean)

Sets whether the response from the `Subscribe` request includes the subscription ARN, even if the subscription is not yet confirmed.

If you set this parameter to `true` , the response includes the ARN in all cases, even if the subscription is not yet confirmed. In addition to the ARN for confirmed subscriptions, the response also includes the `pending subscription` ARN value for subscriptions that arenât yet confirmed. A subscription becomes confirmed when the subscriber calls the `ConfirmSubscription` action with a confirmation token.

The default value is `false` .

`--notification-endpoint` (string)

The endpoint that you want to receive notifications. Endpoints vary by protocol:

- For the `http` protocol, the (public) endpoint is a URL beginning with `http://` .
- For the `https` protocol, the (public) endpoint is a URL beginning with `https://` .
- For the `email` protocol, the endpoint is an email address.
- For the `email-json` protocol, the endpoint is an email address.
- For the `sms` protocol, the endpoint is a phone number of an SMS-enabled device.
- For the `sqs` protocol, the endpoint is the ARN of an Amazon SQS queue.
- For the `application` protocol, the endpoint is the EndpointArn of a mobile app and device.
- For the `lambda` protocol, the endpoint is the ARN of an Lambda function.
- For the `firehose` protocol, the endpoint is the ARN of an Amazon Kinesis Data Firehose delivery stream.

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

**To subscribe to a topic**

The following `subscribe` command subscribes an email address to the specified topic.

```
aws sns subscribe \
    --topic-arn arn:aws:sns:us-west-2:123456789012:my-topic \
    --protocol email \
    --notification-endpoint my-email@example.com
```

Output:

```
{
    "SubscriptionArn": "pending confirmation"
}
```

## Output

SubscriptionArn -> (string)

The ARN of the subscription if it is confirmed, or the string âpending confirmationâ if the subscription requires confirmation. However, if the API request parameter `ReturnSubscriptionArn` is true, then the value is always the subscription ARN, even if the subscription requires confirmation.