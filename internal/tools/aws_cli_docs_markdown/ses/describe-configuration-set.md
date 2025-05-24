# describe-configuration-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/describe-configuration-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/describe-configuration-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/index.html#cli-aws-ses) ]

# describe-configuration-set

## Description

Returns the details of the specified configuration set. For information about using configuration sets, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html) .

You can execute this operation no more than once per second.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/DescribeConfigurationSet)

## Synopsis

```
describe-configuration-set
--configuration-set-name <value>
[--configuration-set-attribute-names <value>]
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

`--configuration-set-name` (string)

The name of the configuration set to describe.

`--configuration-set-attribute-names` (list)

A list of configuration set attributes to return.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  eventDestinations
  trackingOptions
  deliveryOptions
  reputationOptions
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

ConfigurationSet -> (structure)

The configuration set object associated with the specified configuration set.

Name -> (string)

The name of the configuration set. The name must meet the following requirements:

- Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
- Contain 64 characters or fewer.

EventDestinations -> (list)

A list of event destinations associated with the configuration set.

(structure)

Contains information about an event destination.

### Note

When you create or update an event destination, you must provide one, and only one, destination. The destination can be Amazon CloudWatch, Amazon Kinesis Firehose or Amazon Simple Notification Service (Amazon SNS).

Event destinations are associated with configuration sets, which enable you to publish email sending events to Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS). For information about using configuration sets, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html) .

Name -> (string)

The name of the event destination. The name must meet the following requirements:

- Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
- Contain 64 characters or fewer.

Enabled -> (boolean)

Sets whether Amazon SES publishes events to this destination when you send an email with the associated configuration set. Set to `true` to enable publishing to this destination; set to `false` to prevent publishing to this destination. The default value is `false` .

MatchingEventTypes -> (list)

The type of email sending events to publish to the event destination.

- `send` - The call was successful and Amazon SES is attempting to deliver the email.
- `reject` - Amazon SES determined that the email contained a virus and rejected it.
- `bounce` - The recipientâs mail server permanently rejected the email. This corresponds to a hard bounce.
- `complaint` - The recipient marked the email as spam.
- `delivery` - Amazon SES successfully delivered the email to the recipientâs mail server.
- `open` - The recipient received the email and opened it in their email client.
- `click` - The recipient clicked one or more links in the email.
- `renderingFailure` - Amazon SES did not send the email because of a template rendering issue.

(string)

KinesisFirehoseDestination -> (structure)

An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.

IAMRoleARN -> (string)

The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon Kinesis Firehose stream.

DeliveryStreamARN -> (string)

The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to.

CloudWatchDestination -> (structure)

An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination.

DimensionConfigurations -> (list)

A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch.

(structure)

Contains the dimension configuration to use when you publish email sending events to Amazon CloudWatch.

For information about publishing email sending events to Amazon CloudWatch, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html) .

DimensionName -> (string)

The name of an Amazon CloudWatch dimension associated with an email sending metric. The name must meet the following requirements:

- Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), dashes (-), or colons (:).
- Contain 256 characters or fewer.

DimensionValueSource -> (string)

The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch. To use the message tags that you specify using an `X-SES-MESSAGE-TAGS` header or a parameter to the `SendEmail` /`SendRawEmail` API, specify `messageTag` . To use your own email headers, specify `emailHeader` . To put a custom tag on any link included in your email, specify `linkTag` .

DefaultDimensionValue -> (string)

The default value of the dimension that is published to Amazon CloudWatch if you do not provide the value of the dimension when you send an email. The default value must meet the following requirements:

- Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), dashes (-), at signs (@), or periods (.).
- Contain 256 characters or fewer.

SNSDestination -> (structure)

An object that contains the topic ARN associated with an Amazon Simple Notification Service (Amazon SNS) event destination.

TopicARN -> (string)

The ARN of the Amazon SNS topic for email sending events. You can find the ARN of a topic by using the [ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html) Amazon SNS operation.

For more information about Amazon SNS topics, see the [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) .

TrackingOptions -> (structure)

The name of the custom open and click tracking domain associated with the configuration set.

CustomRedirectDomain -> (string)

The custom subdomain that is used to redirect email recipients to the Amazon SES event tracking domain.

DeliveryOptions -> (structure)

Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS).

TlsPolicy -> (string)

Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is `Require` , messages are only delivered if a TLS connection can be established. If the value is `Optional` , messages can be delivered in plain text if a TLS connection canât be established.

ReputationOptions -> (structure)

An object that represents the reputation settings for the configuration set.

SendingEnabled -> (boolean)

Describes whether email sending is enabled or disabled for the configuration set. If the value is `true` , then Amazon SES sends emails that use the configuration set. If the value is `false` , Amazon SES does not send emails that use the configuration set. The default value is `true` . You can change this setting using  UpdateConfigurationSetSendingEnabled .

ReputationMetricsEnabled -> (boolean)

Describes whether or not Amazon SES publishes reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch.

If the value is `true` , reputation metrics are published. If the value is `false` , reputation metrics are not published. The default value is `false` .

LastFreshStart -> (timestamp)

The date and time at which the reputation metrics for the configuration set were last reset. Resetting these metrics is known as a *fresh start* .

When you disable email sending for a configuration set using  UpdateConfigurationSetSendingEnabled and later re-enable it, the reputation metrics for the configuration set (but not for the entire Amazon SES account) are reset.

If email sending for the configuration set has never been disabled and later re-enabled, the value of this attribute is `null` .