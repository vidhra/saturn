# start-game-session-placementÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/start-game-session-placement.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/start-game-session-placement.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# start-game-session-placement

## Description

Makes a request to start a new game session using a game session queue. When processing a placement request, Amazon GameLift looks for the best possible available resource to host the game session, based on how the queue is configured to prioritize factors such as resource cost, latency, and location. After selecting an available resource, Amazon GameLift prompts the resource to start a game session. A placement request can include a list of players to create a set of player sessions. The request can also include information to pass to the new game session, such as to specify a game map or other options.

**Request options**

Use this operation to make the following types of requests.

- Request a placement using the queueâs default prioritization process (see the default prioritization described in [PriorityConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_PriorityConfiguration.html) ). Include these required parameters:
- `GameSessionQueueName`
- `MaximumPlayerSessionCount`
- `PlacementID`
- Request a placement and prioritize based on latency. Include these parameters:
- Required parameters `GameSessionQueueName` , `MaximumPlayerSessionCount` , `PlacementID` .
- `PlayerLatencies` . Include a set of latency values for destinations in the queue. When a request includes latency data, Amazon GameLift automatically reorder the queueâs locations priority list based on lowest available latency values. If a request includes latency data for multiple players, Amazon GameLift calculates each locationâs average latency for all players and reorders to find the lowest latency across all players.
- Donât include `PriorityConfigurationOverride` .
- Prioritize based on a custom list of locations. If youâre using a queue thatâs configured to prioritize location first (see [PriorityConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_PriorityConfiguration.html) for game session queues), you can optionally use the *PriorityConfigurationOverride* parameter to substitute a different location priority list for this placement request. Amazon GameLift searches each location on the priority override list to find an available hosting resource for the new game session. Specify a fallback strategy to use in the event that Amazon GameLift fails to place the game session in any of the locations on the override list.
- Request a placement and prioritized based on a custom list of locations.
- You can request new player sessions for a group of players. Include the *DesiredPlayerSessions* parameter and include at minimum a unique player ID for each. You can also include player-specific data to pass to the new game session.

**Result**

If successful, this operation generates a new game session placement request and adds it to the game session queue for processing. You can track the status of individual placement requests by calling [DescribeGameSessionPlacement](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeGameSessionPlacement.html) or by monitoring queue notifications. When the request status is `FULFILLED` , a new game session has started and the placement request is updated with connection information for the game session (IP address and port). If the request included player session data, Amazon GameLift creates a player session for each player ID in the request.

The request results in a `InvalidRequestException` in the following situations:

- If the request includes both *PlayerLatencies* and *PriorityConfigurationOverride* parameters.
- If the request includes the *PriorityConfigurationOverride* parameter and specifies a queue that doesnât prioritize locations.

Amazon GameLift continues to retry each placement request until it reaches the queueâs timeout setting. If a request times out, you can resubmit the request to the same queue or try a different queue.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/StartGameSessionPlacement)

## Synopsis

```
start-game-session-placement
--placement-id <value>
--game-session-queue-name <value>
[--game-properties <value>]
--maximum-player-session-count <value>
[--game-session-name <value>]
[--player-latencies <value>]
[--desired-player-sessions <value>]
[--game-session-data <value>]
[--priority-configuration-override <value>]
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

`--placement-id` (string)

A unique identifier to assign to the new game session placement. This value is developer-defined. The value must be unique across all Regions and cannot be reused.

`--game-session-queue-name` (string)

Name of the queue to use to place the new game session. You can use either the queue name or ARN value.

`--game-properties` (list)

A set of key-value pairs that can store custom data in a game session. For example: `{"Key": "difficulty", "Value": "novice"}` .

(structure)

This key-value pair can store custom data about a game session. For example, you might use a `GameProperty` to track a game sessionâs map, level of difficulty, or remaining time. The difficulty level could be specified like this: `{"Key": "difficulty", "Value":"Novice"}` .

You can set game properties when creating a game session. You can also modify game properties of an active game session. When searching for game sessions, you can filter on game property keys and values. You canât delete game properties from a game session.

For examples of working with game properties, see [Create a game session with properties](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#game-properties) .

Key -> (string)

The game property identifier.

Value -> (string)

The game property value.

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

`--maximum-player-session-count` (integer)

The maximum number of players that can be connected simultaneously to the game session.

`--game-session-name` (string)

A descriptive label that is associated with a game session. Session names do not need to be unique.

`--player-latencies` (list)

A set of values, expressed in milliseconds, that indicates the amount of latency that a player experiences when connected to Amazon Web Services Regions. This information is used to try to place the new game session where it can offer the best possible gameplay experience for the players.

(structure)

Regional latency information for a player, used when requesting a new game session. This value indicates the amount of time lag that exists when the player is connected to a fleet in the specified Region. The relative difference between a playerâs latency values for multiple Regions are used to determine which fleets are best suited to place a new game session for the player.

PlayerId -> (string)

A unique identifier for a player associated with the latency data.

RegionIdentifier -> (string)

Name of the Region that is associated with the latency value.

LatencyInMilliseconds -> (float)

Amount of time that represents the time lag experienced by the player when connected to the specified Region.

Shorthand Syntax:

```
PlayerId=string,RegionIdentifier=string,LatencyInMilliseconds=float ...
```

JSON Syntax:

```
[
  {
    "PlayerId": "string",
    "RegionIdentifier": "string",
    "LatencyInMilliseconds": float
  }
  ...
]
```

`--desired-player-sessions` (list)

Set of information on each player to create a player session for.

(structure)

Player information for use when creating player sessions using a game session placement request.

PlayerId -> (string)

A unique identifier for a player to associate with the player session.

PlayerData -> (string)

Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game.

Shorthand Syntax:

```
PlayerId=string,PlayerData=string ...
```

JSON Syntax:

```
[
  {
    "PlayerId": "string",
    "PlayerData": "string"
  }
  ...
]
```

`--game-session-data` (string)

A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see [Start a game session](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession) .

`--priority-configuration-override` (structure)

A prioritized list of locations to use for the game session placement and instructions on how to use it. This list overrides a queueâs prioritized location list for this game session placement request only. You can include Amazon Web Services Regions, local zones, and custom locations (for Anywhere fleets). You can choose to limit placements to locations on the override list only, or you can prioritize locations on the override list first and then fall back to the queueâs other locations if needed. Choose a fallback strategy to use in the event that Amazon GameLift fails to place a game session in any of the locations on the priority override list.

PlacementFallbackStrategy -> (string)

Instructions for how to proceed if placement fails in every location on the priority override list. Valid strategies include:

- `DEFAULT_AFTER_SINGLE_PASS` â After attempting to place a new game session in every location on the priority override list, try to place a game session in queueâs other locations. This is the default behavior.
- `NONE` â Limit placements to locations on the priority override list only.

LocationOrder -> (list)

A prioritized list of hosting locations. The list can include Amazon Web Services Regions (such as `us-west-2` ), local zones, and custom locations (for Anywhere fleets). Each location must be listed only once. For details, see [Amazon GameLift service locations.](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html)

(string)

Shorthand Syntax:

```
PlacementFallbackStrategy=string,LocationOrder=string,string
```

JSON Syntax:

```
{
  "PlacementFallbackStrategy": "DEFAULT_AFTER_SINGLE_PASS"|"NONE",
  "LocationOrder": ["string", ...]
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

GameSessionPlacement -> (structure)

Object that describes the newly created game session placement. This object includes all the information provided in the request, as well as start/end time stamps and placement status.

PlacementId -> (string)

A unique identifier for a game session placement.

GameSessionQueueName -> (string)

A descriptive label that is associated with game session queue. Queue names must be unique within each Region.

Status -> (string)

Current status of the game session placement request.

- **PENDING** â The placement request is in the queue waiting to be processed. Game session properties are not yet final.
- **FULFILLED** â A new game session has been successfully placed. Game session properties are now final.
- **CANCELLED** â The placement request was canceled.
- **TIMED_OUT** â A new game session was not successfully created before the time limit expired. You can resubmit the placement request as needed.
- **FAILED** â Amazon GameLift is not able to complete the process of placing the game session. Common reasons are the game session terminated before the placement process was completed, or an unexpected internal error.

GameProperties -> (list)

A set of key-value pairs that can store custom data in a game session. For example: `{"Key": "difficulty", "Value": "novice"}` .

(structure)

This key-value pair can store custom data about a game session. For example, you might use a `GameProperty` to track a game sessionâs map, level of difficulty, or remaining time. The difficulty level could be specified like this: `{"Key": "difficulty", "Value":"Novice"}` .

You can set game properties when creating a game session. You can also modify game properties of an active game session. When searching for game sessions, you can filter on game property keys and values. You canât delete game properties from a game session.

For examples of working with game properties, see [Create a game session with properties](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#game-properties) .

Key -> (string)

The game property identifier.

Value -> (string)

The game property value.

MaximumPlayerSessionCount -> (integer)

The maximum number of players that can be connected simultaneously to the game session.

GameSessionName -> (string)

A descriptive label that is associated with a game session. Session names do not need to be unique.

GameSessionId -> (string)

A unique identifier for the game session. This value isnât final until placement status is `FULFILLED` .

GameSessionArn -> (string)

Identifier for the game session created by this placement request. This identifier is unique across all Regions. This value isnât final until placement status is `FULFILLED` .

GameSessionRegion -> (string)

Name of the Region where the game session created by this placement request is running. This value isnât final until placement status is `FULFILLED` .

PlayerLatencies -> (list)

A set of values, expressed in milliseconds, that indicates the amount of latency that a player experiences when connected to Amazon Web Services Regions.

(structure)

Regional latency information for a player, used when requesting a new game session. This value indicates the amount of time lag that exists when the player is connected to a fleet in the specified Region. The relative difference between a playerâs latency values for multiple Regions are used to determine which fleets are best suited to place a new game session for the player.

PlayerId -> (string)

A unique identifier for a player associated with the latency data.

RegionIdentifier -> (string)

Name of the Region that is associated with the latency value.

LatencyInMilliseconds -> (float)

Amount of time that represents the time lag experienced by the player when connected to the specified Region.

StartTime -> (timestamp)

Time stamp indicating when this request was placed in the queue. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ).

EndTime -> (timestamp)

Time stamp indicating when this request was completed, canceled, or timed out.

IpAddress -> (string)

The IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number. This value isnât final until placement status is `FULFILLED` .

DnsName -> (string)

The DNS identifier assigned to the instance that is running the game session. Values have the following format:

- TLS-enabled fleets: `<unique identifier>.<region identifier>.amazongamelift.com` .
- Non-TLS-enabled fleets: `ec2-<unique identifier>.compute.amazonaws.com` . (See [Amazon EC2 Instance IP Addressing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses) .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

Port -> (integer)

The port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number. This value isnât final until placement status is `FULFILLED` .

PlacedPlayerSessions -> (list)

A collection of information on player sessions created in response to the game session placement request. These player sessions are created only after a new game session is successfully placed (placement status is `FULFILLED` ). This information includes the player ID, provided in the placement request, and a corresponding player session ID.

(structure)

Information about a player session. This object contains only the player ID and player session ID. To retrieve full details on a player session, call [DescribePlayerSessions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribePlayerSessions.html) with the player session ID.

PlayerId -> (string)

A unique identifier for a player that is associated with this player session.

PlayerSessionId -> (string)

A unique identifier for a player session.

GameSessionData -> (string)

A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see [Start a game session](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession) .

MatchmakerData -> (string)

Information on the matchmaking process for this game. Data is in JSON syntax, formatted as a string. It identifies the matchmaking configuration used to create the match, and contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see [Match Data](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-server.html#match-server-data) .

PriorityConfigurationOverride -> (structure)

An alternative priority list of locations thatâs included with a game session placement request. When provided, the list overrides a queueâs location order list for this game session placement request only. The list might include Amazon Web Services Regions, local zones, and custom locations (for Anywhere fleets). The fallback strategy tells Amazon GameLift what action to take (if any) in the event that it failed to place a new game session.

PlacementFallbackStrategy -> (string)

Instructions for how to proceed if placement fails in every location on the priority override list. Valid strategies include:

- `DEFAULT_AFTER_SINGLE_PASS` â After attempting to place a new game session in every location on the priority override list, try to place a game session in queueâs other locations. This is the default behavior.
- `NONE` â Limit placements to locations on the priority override list only.

LocationOrder -> (list)

A prioritized list of hosting locations. The list can include Amazon Web Services Regions (such as `us-west-2` ), local zones, and custom locations (for Anywhere fleets). Each location must be listed only once. For details, see [Amazon GameLift service locations.](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html)

(string)