# create-routing-profileÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-routing-profile.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-routing-profile.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# create-routing-profile

## Description

Creates a new routing profile.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/CreateRoutingProfile)

## Synopsis

```
create-routing-profile
--instance-id <value>
--name <value>
--description <value>
--default-outbound-queue-id <value>
[--queue-configs <value>]
--media-concurrencies <value>
[--tags <value>]
[--agent-availability-timer <value>]
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

`--instance-id` (string)

The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.

`--name` (string)

The name of the routing profile. Must not be more than 127 characters.

`--description` (string)

Description of the routing profile. Must not be more than 250 characters.

`--default-outbound-queue-id` (string)

The default outbound queue for the routing profile.

`--queue-configs` (list)

The inbound queues associated with the routing profile. If no queue is added, the agent can make only outbound calls.

The limit of 10 array members applies to the maximum number of `RoutingProfileQueueConfig` objects that can be passed during a CreateRoutingProfile API request. It is different from the quota of 50 queues per routing profile per instance that is listed in [Amazon Connect service quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html) .

(structure)

Contains information about the queue and channel for which priority and delay can be set.

QueueReference -> (structure)

Contains information about a queue resource.

QueueId -> (string)

The identifier for the queue.

Channel -> (string)

The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.

Priority -> (integer)

The order in which contacts are to be handled for the queue. For more information, see [Queues: priority and delay](https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html) .

Delay -> (integer)

The delay, in seconds, a contact should be in the queue before they are routed to an available agent. For more information, see [Queues: priority and delay](https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html) in the *Amazon Connect Administrator Guide* .

Shorthand Syntax:

```
QueueReference={QueueId=string,Channel=string},Priority=integer,Delay=integer ...
```

JSON Syntax:

```
[
  {
    "QueueReference": {
      "QueueId": "string",
      "Channel": "VOICE"|"CHAT"|"TASK"|"EMAIL"
    },
    "Priority": integer,
    "Delay": integer
  }
  ...
]
```

`--media-concurrencies` (list)

The channels that agents can handle in the Contact Control Panel (CCP) for this routing profile.

(structure)

Contains information about which channels are supported, and how many contacts an agent can have on a channel simultaneously.

Channel -> (string)

The channels that agents can handle in the Contact Control Panel (CCP).

Concurrency -> (integer)

The number of contacts an agent can have on a channel simultaneously.

Valid Range for `VOICE` : Minimum value of 1. Maximum value of 1.

Valid Range for `CHAT` : Minimum value of 1. Maximum value of 10.

Valid Range for `TASK` : Minimum value of 1. Maximum value of 10.

CrossChannelBehavior -> (structure)

Defines the cross-channel routing behavior for each channel that is enabled for this Routing Profile. For example, this allows you to offer an agent a different contact from another channel when they are currently working with a contact from a Voice channel.

BehaviorType -> (string)

Specifies the other channels that can be routed to an agent handling their current channel.

Shorthand Syntax:

```
Channel=string,Concurrency=integer,CrossChannelBehavior={BehaviorType=string} ...
```

JSON Syntax:

```
[
  {
    "Channel": "VOICE"|"CHAT"|"TASK"|"EMAIL",
    "Concurrency": integer,
    "CrossChannelBehavior": {
      "BehaviorType": "ROUTE_CURRENT_CHANNEL_ONLY"|"ROUTE_ANY_CHANNEL"
    }
  }
  ...
]
```

`--tags` (map)

The tags used to organize, track, or control access for this resource. For example, { âTagsâ: {âkey1â:âvalue1â, âkey2â:âvalue2â} }.

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

`--agent-availability-timer` (string)

Whether agents with this routing profile will have their routing order calculated based on *longest idle time* or *time since their last inbound contact* .

Possible values:

- `TIME_SINCE_LAST_ACTIVITY`
- `TIME_SINCE_LAST_INBOUND`

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

RoutingProfileArn -> (string)

The Amazon Resource Name (ARN) of the routing profile.

RoutingProfileId -> (string)

The identifier of the routing profile.