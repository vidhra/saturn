# create-configuration-set-event-destinationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-configuration-set-event-destination.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-configuration-set-event-destination.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sesv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/index.html#cli-aws-sesv2) ]

# create-configuration-set-event-destination

## Description

Create an event destination. *Events* include message sends, deliveries, opens, clicks, bounces, and complaints. *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon EventBridge and associate a rule to send the event to the specified target.

A single configuration set can include more than one event destination.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sesv2-2019-09-27/CreateConfigurationSetEventDestination)

## Synopsis

```
create-configuration-set-event-destination
--configuration-set-name <value>
--event-destination-name <value>
--event-destination <value>
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

The name of the configuration set .

`--event-destination-name` (string)

A name that identifies the event destination within the configuration set.

`--event-destination` (structure)

An object that defines the event destination.

Enabled -> (boolean)

If `true` , the event destination is enabled. When the event destination is enabled, the specified event types are sent to the destinations in this `EventDestinationDefinition` .

If `false` , the event destination is disabled. When the event destination is disabled, events arenât sent to the specified destinations.

MatchingEventTypes -> (list)

An array that specifies which events the Amazon SES API v2 should send to the destinations in this `EventDestinationDefinition` .

(string)

An email sending event type. For example, email sends, opens, and bounces are all email events.

KinesisFirehoseDestination -> (structure)

An object that defines an Amazon Kinesis Data Firehose destination for email events. You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.

IamRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that the Amazon SES API v2 uses to send email events to the Amazon Kinesis Data Firehose stream.

DeliveryStreamArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that the Amazon SES API v2 sends email events to.

CloudWatchDestination -> (structure)

An object that defines an Amazon CloudWatch destination for email events. You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.

DimensionConfigurations -> (list)

An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.

(structure)

An object that defines the dimension configuration to use when you send email events to Amazon CloudWatch.

DimensionName -> (string)

The name of an Amazon CloudWatch dimension associated with an email sending metric. The name has to meet the following criteria:

- It can only contain ASCII letters (aâz, AâZ), numbers (0â9), underscores (_), or dashes (-).
- It can contain no more than 256 characters.

DimensionValueSource -> (string)

The location where the Amazon SES API v2 finds the value of a dimension to publish to Amazon CloudWatch. To use the message tags that you specify using an `X-SES-MESSAGE-TAGS` header or a parameter to the `SendEmail` or `SendRawEmail` API, choose `messageTag` . To use your own email headers, choose `emailHeader` . To use link tags, choose `linkTags` .

DefaultDimensionValue -> (string)

The default value of the dimension that is published to Amazon CloudWatch if you donât provide the value of the dimension when you send an email. This value has to meet the following criteria:

- Can only contain ASCII letters (aâz, AâZ), numbers (0â9), underscores (_), or dashes (-), at signs (@), and periods (.).
- It can contain no more than 256 characters.

SnsDestination -> (structure)

An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to send notifications when certain email events occur.

TopicArn -> (string)

The Amazon Resource Name (ARN) of the Amazon SNS topic to publish email events to. For more information about Amazon SNS topics, see the [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) .

EventBridgeDestination -> (structure)

An object that defines an Amazon EventBridge destination for email events. You can use Amazon EventBridge to send notifications when certain email events occur.

EventBusArn -> (string)

The Amazon Resource Name (ARN) of the Amazon EventBridge bus to publish email events to. Only the default bus is supported.

PinpointDestination -> (structure)

An object that defines an Amazon Pinpoint project destination for email events. You can send email event data to a Amazon Pinpoint project to view metrics using the Transactional Messaging dashboards that are built in to Amazon Pinpoint. For more information, see [Transactional Messaging Charts](https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-transactional-messages.html) in the *Amazon Pinpoint User Guide* .

ApplicationArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Pinpoint project to send email events to.

JSON Syntax:

```
{
  "Enabled": true|false,
  "MatchingEventTypes": ["SEND"|"REJECT"|"BOUNCE"|"COMPLAINT"|"DELIVERY"|"OPEN"|"CLICK"|"RENDERING_FAILURE"|"DELIVERY_DELAY"|"SUBSCRIPTION", ...],
  "KinesisFirehoseDestination": {
    "IamRoleArn": "string",
    "DeliveryStreamArn": "string"
  },
  "CloudWatchDestination": {
    "DimensionConfigurations": [
      {
        "DimensionName": "string",
        "DimensionValueSource": "MESSAGE_TAG"|"EMAIL_HEADER"|"LINK_TAG",
        "DefaultDimensionValue": "string"
      }
      ...
    ]
  },
  "SnsDestination": {
    "TopicArn": "string"
  },
  "EventBridgeDestination": {
    "EventBusArn": "string"
  },
  "PinpointDestination": {
    "ApplicationArn": "string"
  }
}
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

None