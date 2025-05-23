# get-current-user-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/get-current-user-data.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/get-current-user-data.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# get-current-user-data

## Description

Gets the real-time active user data from the specified Amazon Connect instance.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/GetCurrentUserData)

## Synopsis

```
get-current-user-data
--instance-id <value>
--filters <value>
[--next-token <value>]
[--max-results <value>]
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

`--filters` (structure)

The filters to apply to returned user data. You can filter up to the following limits:

- Queues: 100
- Routing profiles: 100
- Agents: 100
- Contact states: 9
- User hierarchy groups: 1

The user data is retrieved for only the specified values/resources in the filter. A maximum of one filter can be passed from queues, routing profiles, agents, and user hierarchy groups.

Currently tagging is only supported on the resources that are passed in the filter.

Queues -> (list)

A list of up to 100 queues or ARNs.

(string)

ContactFilter -> (structure)

A filter for the user data based on the contact information that is associated to the user. It contains a list of contact states.

ContactStates -> (list)

A list of up to 9 [contact states](https://docs.aws.amazon.com/connect/latest/adminguide/about-contact-states.html) .

(string)

RoutingProfiles -> (list)

A list of up to 100 routing profile IDs or ARNs.

(string)

Agents -> (list)

A list of up to 100 agent IDs or ARNs.

(string)

UserHierarchyGroups -> (list)

A UserHierarchyGroup ID or ARN.

(string)

Shorthand Syntax:

```
Queues=string,string,ContactFilter={ContactStates=[string,string]},RoutingProfiles=string,string,Agents=string,string,UserHierarchyGroups=string,string
```

JSON Syntax:

```
{
  "Queues": ["string", ...],
  "ContactFilter": {
    "ContactStates": ["INCOMING"|"PENDING"|"CONNECTING"|"CONNECTED"|"CONNECTED_ONHOLD"|"MISSED"|"ERROR"|"ENDED"|"REJECTED", ...]
  },
  "RoutingProfiles": ["string", ...],
  "Agents": ["string", ...],
  "UserHierarchyGroups": ["string", ...]
}
```

`--next-token` (string)

The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

`--max-results` (integer)

The maximum number of results to return per page.

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

NextToken -> (string)

If there are additional results, this is the token for the next set of results.

UserDataList -> (list)

A list of the user data that is returned.

(structure)

Data for a user.

User -> (structure)

Information about the user for the data that is returned. It contains the `resourceId` and ARN of the user.

Id -> (string)

The unique identifier for the user.

Arn -> (string)

The Amazon Resource Name (ARN) for the user.

RoutingProfile -> (structure)

Information about the routing profile that is assigned to the user.

Id -> (string)

The identifier of the routing profile.

Arn -> (string)

The Amazon Resource Name (ARN) of the routing profile.

HierarchyPath -> (structure)

Contains information about the levels of a hierarchy group assigned to a user.

LevelOne -> (structure)

Information about level one.

Id -> (string)

The unique identifier for the hierarchy group.

Arn -> (string)

The Amazon Resource Name (ARN) for the hierarchy group.

LevelTwo -> (structure)

Information about level two.

Id -> (string)

The unique identifier for the hierarchy group.

Arn -> (string)

The Amazon Resource Name (ARN) for the hierarchy group.

LevelThree -> (structure)

Information about level three.

Id -> (string)

The unique identifier for the hierarchy group.

Arn -> (string)

The Amazon Resource Name (ARN) for the hierarchy group.

LevelFour -> (structure)

Information about level four.

Id -> (string)

The unique identifier for the hierarchy group.

Arn -> (string)

The Amazon Resource Name (ARN) for the hierarchy group.

LevelFive -> (structure)

Information about level five.

Id -> (string)

The unique identifier for the hierarchy group.

Arn -> (string)

The Amazon Resource Name (ARN) for the hierarchy group.

Status -> (structure)

The status of the agent that they manually set in their Contact Control Panel (CCP), or that the supervisor manually changes in the real-time metrics report.

StatusStartTimestamp -> (timestamp)

The start timestamp of the agentâs status.

StatusArn -> (string)

The Amazon Resource Name (ARN) of the agentâs status.

StatusName -> (string)

The name of the agent status.

AvailableSlotsByChannel -> (map)

A map of available slots by channel. The key is a channel name. The value is an integer: the available number of slots.

key -> (string)

value -> (integer)

MaxSlotsByChannel -> (map)

A map of maximum slots by channel. The key is a channel name. The value is an integer: the maximum number of slots. This is calculated from [MediaConcurrency](https://docs.aws.amazon.com/connect/latest/APIReference/API_MediaConcurrency.html) of the `RoutingProfile` assigned to the agent.

key -> (string)

value -> (integer)

ActiveSlotsByChannel -> (map)

A map of active slots by channel. The key is a channel name. The value is an integer: the number of active slots.

key -> (string)

value -> (integer)

Contacts -> (list)

A list of contact reference information.

(structure)

Information about the [contact](https://docs.aws.amazon.com/connect/latest/APIReference/API_Contact.html) associated to the user.

ContactId -> (string)

The identifier of the contact in this instance of Amazon Connect.

Channel -> (string)

The channel of the contact.

InitiationMethod -> (string)

How the contact was initiated.

AgentContactState -> (string)

The [state of the contact](https://docs.aws.amazon.com/connect/latest/adminguide/about-contact-states.html) .

### Note

When `AgentContactState` is set to `CONNECTED_ONHOLD` , `StateStartTimestamp` is not changed. Instead, `StateStartTimestamp` reflects the time the contact was `CONNECTED` to the agent.

StateStartTimestamp -> (timestamp)

The epoch timestamp when the contact state started.

ConnectedToAgentTimestamp -> (timestamp)

The time at which the contact was connected to an agent.

Queue -> (structure)

Contains information about a queue resource for which metrics are returned.

Id -> (string)

The identifier of the queue.

Arn -> (string)

The Amazon Resource Name (ARN) of the queue.

NextStatus -> (string)

The Next status of the agent.

ApproximateTotalCount -> (long)

The total count of the result, regardless of the current page size.