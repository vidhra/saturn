# update-game-session-queueÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-session-queue.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-session-queue.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# update-game-session-queue

## Description

Updates the configuration of a game session queue, which determines how the queue processes new game session requests. To update settings, specify the queue name to be updated and provide the new settings. When updating destinations, provide a complete list of destinations.

**Learn more**

[Using Multi-Region Queues](https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-intro.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/UpdateGameSessionQueue)

## Synopsis

```
update-game-session-queue
--name <value>
[--timeout-in-seconds <value>]
[--player-latency-policies <value>]
[--destinations <value>]
[--filter-configuration <value>]
[--priority-configuration <value>]
[--custom-event-data <value>]
[--notification-target <value>]
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

A descriptive label that is associated with game session queue. Queue names must be unique within each Region. You can use either the queue ID or ARN value.

`--timeout-in-seconds` (integer)

The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a `TIMED_OUT` status.

`--player-latency-policies` (list)

A set of policies that enforce a sliding cap on player latency when processing game sessions placement requests. Use multiple policies to gradually relax the cap over time if Amazon GameLift canât make a placement. Policies are evaluated in order starting with the lowest maximum latency value. When updating policies, provide a complete collection of policies.

(structure)

Sets a latency cap for individual players when placing a game session. With a latency policy in force, a game session cannot be placed in a fleet location where a player reports latency higher than the cap. Latency policies are used only with placement request that provide player latency information. Player latency policies can be stacked to gradually relax latency requirements over time.

MaximumIndividualPlayerLatencyMilliseconds -> (integer)

The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.

PolicyDurationSeconds -> (integer)

The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.

Shorthand Syntax:

```
MaximumIndividualPlayerLatencyMilliseconds=integer,PolicyDurationSeconds=integer ...
```

JSON Syntax:

```
[
  {
    "MaximumIndividualPlayerLatencyMilliseconds": integer,
    "PolicyDurationSeconds": integer
  }
  ...
]
```

`--destinations` (list)

A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue. Destinations are identified by either a fleet ARN or a fleet alias ARN, and are listed in order of placement preference. When updating this list, provide a complete list of destinations.

(structure)

A fleet or alias designated in a game session queue. Queues fulfill requests for new game sessions by placing a new game session on any of the queueâs destinations.

DestinationArn -> (string)

The Amazon Resource Name (ARN) that is assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a Region name, provide a unique identifier across all Regions.

Shorthand Syntax:

```
DestinationArn=string ...
```

JSON Syntax:

```
[
  {
    "DestinationArn": "string"
  }
  ...
]
```

`--filter-configuration` (structure)

A list of locations where a queue is allowed to place new game sessions. Locations are specified in the form of Amazon Web Services Region codes, such as `us-west-2` . If this parameter is not set, game sessions can be placed in any queue location. To remove an existing filter configuration, pass in an empty set.

AllowedLocations -> (list)

A list of locations to allow game session placement in, in the form of Amazon Web Services Region codes such as `us-west-2` .

(string)

Shorthand Syntax:

```
AllowedLocations=string,string
```

JSON Syntax:

```
{
  "AllowedLocations": ["string", ...]
}
```

`--priority-configuration` (structure)

Custom settings to use when prioritizing destinations and locations for game session placements. This configuration replaces the FleetIQ default prioritization process. Priority types that are not explicitly named will be automatically applied at the end of the prioritization process. To remove an existing priority configuration, pass in an empty set.

PriorityOrder -> (list)

A custom sequence to use when prioritizing where to place new game sessions. Each priority type is listed once.

- `LATENCY` â Amazon GameLift prioritizes locations where the average player latency is lowest. Player latency data is provided in each game session placement request.
- `COST` â Amazon GameLift prioritizes queue destinations with the lowest current hosting costs. Cost is evaluated based on the destinationâs location, instance type, and fleet type (Spot or On-Demand).
- `DESTINATION` â Amazon GameLift prioritizes based on the list order of destinations in the queue configuration.
- `LOCATION` â Amazon GameLift prioritizes based on the provided order of locations, as defined in `LocationOrder` .

(string)

LocationOrder -> (list)

The prioritization order to use for fleet locations, when the `PriorityOrder` property includes `LOCATION` . Locations can include Amazon Web Services Region codes (such as `us-west-2` ), local zones, and custom locations (for Anywhere fleets). Each location must be listed only once. For details, see [Amazon GameLift service locations.](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html)

(string)

Shorthand Syntax:

```
PriorityOrder=string,string,LocationOrder=string,string
```

JSON Syntax:

```
{
  "PriorityOrder": ["LATENCY"|"COST"|"DESTINATION"|"LOCATION", ...],
  "LocationOrder": ["string", ...]
}
```

`--custom-event-data` (string)

Information to be added to all events that are related to this game session queue.

`--notification-target` (string)

An SNS topic ARN that is set up to receive game session placement notifications. See [Setting up notifications for game session placement](https://docs.aws.amazon.com/gamelift/latest/developerguide/queue-notification.html) .

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

**To update a game session queue configuration**

The following `update-game-session-queue` example adds a new destination and updates the player latency policies for an existing game session queue.

```
aws gamelift update-game-session-queue \
    --name MegaFrogRace-NA \
    --destinations file://destinations.json \
    --player-latency-policies file://latency-policies.json
```

Contents of `destinations.json`:

```
{
    "Destinations": [
        {"DestinationArn": "arn:aws:gamelift:us-west-2::fleet/fleet-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d"},
        {"DestinationArn": "arn:aws:gamelift:us-east-1::fleet/fleet-5c6d3c4d-5e6f-7a8b-9c0d-1e2f3a4b5a2b"},
        {"DestinationArn": "arn:aws:gamelift:us-east-1::alias/alias-11aa22bb-3c4d-5e6f-000a-1111aaaa22bb"}
    ]
}
```

Contents of `latency-policies.json`:

```
{
    "PlayerLatencyPolicies": [
        {"MaximumIndividualPlayerLatencyMilliseconds": 200},
        {"MaximumIndividualPlayerLatencyMilliseconds": 150, "PolicyDurationSeconds": 120},
        {"MaximumIndividualPlayerLatencyMilliseconds": 100, "PolicyDurationSeconds": 120}
    ]
}
```

Output:

```
{
    "GameSessionQueue": {
        "Destinations": [
            {"DestinationArn": "arn:aws:gamelift:us-west-2::fleet/fleet-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d"},
            {"DestinationArn": "arn:aws:gamelift:us-east-1::fleet/fleet-5c6d3c4d-5e6f-7a8b-9c0d-1e2f3a4b5a2b"},
            {"DestinationArn": "arn:aws:gamelift:us-east-1::alias/alias-11aa22bb-3c4d-5e6f-000a-1111aaaa22bb"}
        ],
        "GameSessionQueueArn": "arn:aws:gamelift:us-west-2:111122223333:gamesessionqueue/MegaFrogRace-NA",
        "Name": "MegaFrogRace-NA",
        "TimeoutInSeconds": 600,
        "PlayerLatencyPolicies": [
            {"MaximumIndividualPlayerLatencyMilliseconds": 200},
            {"MaximumIndividualPlayerLatencyMilliseconds": 150, "PolicyDurationSeconds": 120},
            {"MaximumIndividualPlayerLatencyMilliseconds": 100, "PolicyDurationSeconds": 120}
        ]
    }
}
```

For more information, see [Using Multi-Region Queues](https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-intro.html) in the *Amazon GameLift Developer Guide*.

## Output

GameSessionQueue -> (structure)

An object that describes the newly updated game session queue.

Name -> (string)

A descriptive label that is associated with game session queue. Queue names must be unique within each Region.

GameSessionQueueArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) that is assigned to a Amazon GameLift game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::gamesessionqueue/<queue name>` . In a Amazon GameLift game session queue ARN, the resource ID matches the *Name* value.

TimeoutInSeconds -> (integer)

The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a `TIMED_OUT` status.

PlayerLatencyPolicies -> (list)

A set of policies that enforce a sliding cap on player latency when processing game sessions placement requests. Use multiple policies to gradually relax the cap over time if Amazon GameLift canât make a placement. Policies are evaluated in order starting with the lowest maximum latency value.

(structure)

Sets a latency cap for individual players when placing a game session. With a latency policy in force, a game session cannot be placed in a fleet location where a player reports latency higher than the cap. Latency policies are used only with placement request that provide player latency information. Player latency policies can be stacked to gradually relax latency requirements over time.

MaximumIndividualPlayerLatencyMilliseconds -> (integer)

The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.

PolicyDurationSeconds -> (integer)

The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.

Destinations -> (list)

A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue. Destinations are identified by either a fleet ARN or a fleet alias ARN, and are listed in order of placement preference.

(structure)

A fleet or alias designated in a game session queue. Queues fulfill requests for new game sessions by placing a new game session on any of the queueâs destinations.

DestinationArn -> (string)

The Amazon Resource Name (ARN) that is assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a Region name, provide a unique identifier across all Regions.

FilterConfiguration -> (structure)

A list of locations where a queue is allowed to place new game sessions. Locations are specified in the form of Amazon Web Services Region codes, such as `us-west-2` . If this parameter is not set, game sessions can be placed in any queue location.

AllowedLocations -> (list)

A list of locations to allow game session placement in, in the form of Amazon Web Services Region codes such as `us-west-2` .

(string)

PriorityConfiguration -> (structure)

Custom settings to use when prioritizing destinations and locations for game session placements. This configuration replaces the FleetIQ default prioritization process. Priority types that are not explicitly named will be automatically applied at the end of the prioritization process.

PriorityOrder -> (list)

A custom sequence to use when prioritizing where to place new game sessions. Each priority type is listed once.

- `LATENCY` â Amazon GameLift prioritizes locations where the average player latency is lowest. Player latency data is provided in each game session placement request.
- `COST` â Amazon GameLift prioritizes queue destinations with the lowest current hosting costs. Cost is evaluated based on the destinationâs location, instance type, and fleet type (Spot or On-Demand).
- `DESTINATION` â Amazon GameLift prioritizes based on the list order of destinations in the queue configuration.
- `LOCATION` â Amazon GameLift prioritizes based on the provided order of locations, as defined in `LocationOrder` .

(string)

LocationOrder -> (list)

The prioritization order to use for fleet locations, when the `PriorityOrder` property includes `LOCATION` . Locations can include Amazon Web Services Region codes (such as `us-west-2` ), local zones, and custom locations (for Anywhere fleets). Each location must be listed only once. For details, see [Amazon GameLift service locations.](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html)

(string)

CustomEventData -> (string)

Information that is added to all events that are related to this game session queue.

NotificationTarget -> (string)

An SNS topic ARN that is set up to receive game session placement notifications. See [Setting up notifications for game session placement](https://docs.aws.amazon.com/gamelift/latest/developerguide/queue-notification.html) .