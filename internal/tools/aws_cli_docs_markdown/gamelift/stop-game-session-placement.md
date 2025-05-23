# stop-game-session-placementÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/stop-game-session-placement.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/stop-game-session-placement.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# stop-game-session-placement

## Description

Cancels a game session placement thatâs in `PENDING` status. To stop a placement, provide the placement ID value.

Results

If successful, this operation removes the placement request from the queue and moves the `GameSessionPlacement` to `CANCELLED` status.

This operation results in an `InvalidRequestExecption` (400) error if a game session has already been created for this placement. You can clean up an unneeded game session by calling [TerminateGameSession](https://docs.aws.amazon.com/gamelift/latest/apireference/API_TerminateGameSession) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/StopGameSessionPlacement)

## Synopsis

```
stop-game-session-placement
--placement-id <value>
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

A unique identifier for a game session placement to stop.

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

Object that describes the canceled game session placement, with `CANCELLED` status and an end time stamp.

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