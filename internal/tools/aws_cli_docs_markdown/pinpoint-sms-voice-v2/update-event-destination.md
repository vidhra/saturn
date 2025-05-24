# update-event-destinationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/update-event-destination.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/update-event-destination.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint-sms-voice-v2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/index.html#cli-aws-pinpoint-sms-voice-v2) ]

# update-event-destination

## Description

Updates an existing event destination in a configuration set. You can update the IAM role ARN for CloudWatch Logs and Firehose. You can also enable or disable the event destination.

You may want to update an event destination to change its matching event types or updating the destination resource ARN. You canât change an event destinationâs type between CloudWatch Logs, Firehose, and Amazon SNS.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-sms-voice-v2-2022-03-31/UpdateEventDestination)

## Synopsis

```
update-event-destination
--configuration-set-name <value>
--event-destination-name <value>
[--enabled | --no-enabled]
[--matching-event-types <value>]
[--cloud-watch-logs-destination <value>]
[--kinesis-firehose-destination <value>]
[--sns-destination <value>]
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

The configuration set to update with the new event destination. Valid values for this can be the ConfigurationSetName or ConfigurationSetArn.

`--event-destination-name` (string)

The name to use for the event destination.

`--enabled` | `--no-enabled` (boolean)

When set to true logging is enabled.

`--matching-event-types` (list)

An array of event types that determine which events to log.

### Note

The `TEXT_SENT` event type is not supported.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  ALL
  TEXT_ALL
  TEXT_SENT
  TEXT_PENDING
  TEXT_QUEUED
  TEXT_SUCCESSFUL
  TEXT_DELIVERED
  TEXT_INVALID
  TEXT_INVALID_MESSAGE
  TEXT_UNREACHABLE
  TEXT_CARRIER_UNREACHABLE
  TEXT_BLOCKED
  TEXT_CARRIER_BLOCKED
  TEXT_SPAM
  TEXT_UNKNOWN
  TEXT_TTL_EXPIRED
  TEXT_PROTECT_BLOCKED
  VOICE_ALL
  VOICE_INITIATED
  VOICE_RINGING
  VOICE_ANSWERED
  VOICE_COMPLETED
  VOICE_BUSY
  VOICE_NO_ANSWER
  VOICE_FAILED
  VOICE_TTL_EXPIRED
  MEDIA_ALL
  MEDIA_PENDING
  MEDIA_QUEUED
  MEDIA_SUCCESSFUL
  MEDIA_DELIVERED
  MEDIA_INVALID
  MEDIA_INVALID_MESSAGE
  MEDIA_UNREACHABLE
  MEDIA_CARRIER_UNREACHABLE
  MEDIA_BLOCKED
  MEDIA_CARRIER_BLOCKED
  MEDIA_SPAM
  MEDIA_UNKNOWN
  MEDIA_TTL_EXPIRED
  MEDIA_FILE_INACCESSIBLE
  MEDIA_FILE_TYPE_UNSUPPORTED
  MEDIA_FILE_SIZE_EXCEEDED
```

`--cloud-watch-logs-destination` (structure)

An object that contains information about an event destination that sends data to CloudWatch Logs.

IamRoleArn -> (string)

The Amazon Resource Name (ARN) of an Identity and Access Management role that is able to write event data to an Amazon CloudWatch destination.

LogGroupArn -> (string)

The name of the Amazon CloudWatch log group that you want to record events in.

Shorthand Syntax:

```
IamRoleArn=string,LogGroupArn=string
```

JSON Syntax:

```
{
  "IamRoleArn": "string",
  "LogGroupArn": "string"
}
```

`--kinesis-firehose-destination` (structure)

An object that contains information about an event destination for logging to Firehose.

IamRoleArn -> (string)

The ARN of an Identity and Access Management role that is able to write event data to an Amazon Data Firehose destination.

DeliveryStreamArn -> (string)

The Amazon Resource Name (ARN) of the delivery stream.

Shorthand Syntax:

```
IamRoleArn=string,DeliveryStreamArn=string
```

JSON Syntax:

```
{
  "IamRoleArn": "string",
  "DeliveryStreamArn": "string"
}
```

`--sns-destination` (structure)

An object that contains information about an event destination that sends data to Amazon SNS.

TopicArn -> (string)

The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish events to.

Shorthand Syntax:

```
TopicArn=string
```

JSON Syntax:

```
{
  "TopicArn": "string"
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

ConfigurationSetArn -> (string)

The Amazon Resource Name (ARN) for the ConfigurationSet that was updated.

ConfigurationSetName -> (string)

The name of the configuration set.

EventDestination -> (structure)

An EventDestination object containing the details of where events will be logged.

EventDestinationName -> (string)

The name of the EventDestination.

Enabled -> (boolean)

When set to true events will be logged.

MatchingEventTypes -> (list)

An array of event types that determine which events to log.

### Note

The `TEXT_SENT` event type is not supported.

(string)

CloudWatchLogsDestination -> (structure)

An object that contains information about an event destination that sends logging events to Amazon CloudWatch logs.

IamRoleArn -> (string)

The Amazon Resource Name (ARN) of an Identity and Access Management role that is able to write event data to an Amazon CloudWatch destination.

LogGroupArn -> (string)

The name of the Amazon CloudWatch log group that you want to record events in.

KinesisFirehoseDestination -> (structure)

An object that contains information about an event destination for logging to Amazon Data Firehose.

IamRoleArn -> (string)

The ARN of an Identity and Access Management role that is able to write event data to an Amazon Data Firehose destination.

DeliveryStreamArn -> (string)

The Amazon Resource Name (ARN) of the delivery stream.

SnsDestination -> (structure)

An object that contains information about an event destination that sends logging events to Amazon SNS.

TopicArn -> (string)

The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish events to.