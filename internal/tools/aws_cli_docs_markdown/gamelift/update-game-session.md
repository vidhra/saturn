# update-game-sessionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-session.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-session.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# update-game-session

## Description

Updates the mutable properties of a game session.

To update a game session, specify the game session ID and the values you want to change.

If successful, the updated `GameSession` object is returned.

[All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/UpdateGameSession)

## Synopsis

```
update-game-session
--game-session-id <value>
[--maximum-player-session-count <value>]
[--name <value>]
[--player-session-creation-policy <value>]
[--protection-policy <value>]
[--game-properties <value>]
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

`--game-session-id` (string)

A unique identifier for the game session to update.

`--maximum-player-session-count` (integer)

The maximum number of players that can be connected simultaneously to the game session.

`--name` (string)

A descriptive label that is associated with a game session. Session names do not need to be unique.

`--player-session-creation-policy` (string)

A policy that determines whether the game session is accepting new players.

Possible values:

- `ACCEPT_ALL`
- `DENY_ALL`

`--protection-policy` (string)

Game session protection policy to apply to this game session only.

- `NoProtection` â The game session can be terminated during a scale-down event.
- `FullProtection` â If the game session is in an `ACTIVE` status, it cannot be terminated during a scale-down event.

Possible values:

- `NoProtection`
- `FullProtection`

`--game-properties` (list)

A set of key-value pairs that can store custom data in a game session. For example: `{"Key": "difficulty", "Value": "novice"}` . You can use this parameter to modify game properties in an active game session. This action adds new properties and modifies existing properties. There is no way to delete properties. For an example, see [Update the value of a game property](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#game-properties-update) .

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

GameSession -> (structure)

The updated game session properties.

GameSessionId -> (string)

A unique identifier for the game session. A game session ARN has the following format: `arn:aws:gamelift:<location>::gamesession/<fleet ID>/<custom ID string or idempotency token>` .

Name -> (string)

A descriptive label that is associated with a game session. Session names do not need to be unique.

FleetId -> (string)

A unique identifier for the fleet that the game session is running on.

FleetArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) associated with the GameLift fleet that this game session is running on.

CreationTime -> (timestamp)

A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ).

TerminationTime -> (timestamp)

A time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ).

CurrentPlayerSessionCount -> (integer)

Number of players currently in the game session.

MaximumPlayerSessionCount -> (integer)

The maximum number of players that can be connected simultaneously to the game session.

Status -> (string)

Current status of the game session. A game session must have an `ACTIVE` status to have player sessions.

StatusReason -> (string)

Provides additional information about game session status.

- `INTERRUPTED` â The game session was hosted on an EC2 Spot instance that was reclaimed, causing the active game session to be stopped.
- `TRIGGERED_ON_PROCESS_TERMINATE` â The game session was stopped by calling `TerminateGameSession` with the termination mode `TRIGGER_ON_PROCESS_TERMINATE` .
- `FORCE_TERMINATED` â The game session was stopped by calling `TerminateGameSession` with the termination mode `FORCE_TERMINATE` .

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

IpAddress -> (string)

The IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.

DnsName -> (string)

The DNS identifier assigned to the instance that is running the game session. Values have the following format:

- TLS-enabled fleets: `<unique identifier>.<region identifier>.amazongamelift.com` .
- Non-TLS-enabled fleets: `ec2-<unique identifier>.compute.amazonaws.com` . (See [Amazon EC2 Instance IP Addressing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses) .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

Port -> (integer)

The port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.

PlayerSessionCreationPolicy -> (string)

Indicates whether the game session is accepting new players.

CreatorId -> (string)

A unique identifier for a player. This ID is used to enforce a resource protection policy (if one exists), that limits the number of game sessions a player can create.

GameSessionData -> (string)

A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see [Start a game session](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession) .

MatchmakerData -> (string)

Information about the matchmaking process that resulted in the game session, if matchmaking was used. Data is in JSON syntax, formatted as a string. Information includes the matchmaker ID as well as player attributes and team assignments. For more details on matchmaker data, see [Match Data](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-server.html#match-server-data) . Matchmaker data is updated whenever new players are added during a successful backfill (see [StartMatchBackfill](https://docs.aws.amazon.com/gamelift/latest/apireference/API_StartMatchBackfill.html) ).

Location -> (string)

The fleet location where the game session is running. This value might specify the fleetâs home Region or a remote location. Location is expressed as an Amazon Web Services Region code such as `us-west-2` .