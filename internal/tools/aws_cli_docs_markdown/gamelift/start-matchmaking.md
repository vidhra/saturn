# start-matchmakingÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/start-matchmaking.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/start-matchmaking.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# start-matchmaking

## Description

Uses FlexMatch to create a game match for a group of players based on custom matchmaking rules. With games that use Amazon GameLift managed hosting, this operation also triggers Amazon GameLift to find hosting resources and start a new game session for the new match. Each matchmaking request includes information on one or more players and specifies the FlexMatch matchmaker to use. When a request is for multiple players, FlexMatch attempts to build a match that includes all players in the request, placing them in the same team and finding additional players as needed to fill the match.

To start matchmaking, provide a unique ticket ID, specify a matchmaking configuration, and include the players to be matched. You must also include any player attributes that are required by the matchmaking configurationâs rule set. If successful, a matchmaking ticket is returned with status set to `QUEUED` .

Track matchmaking events to respond as needed and acquire game session connection information for successfully completed matches. Ticket status updates are tracked using event notification through Amazon Simple Notification Service, which is defined in the matchmaking configuration.

**Learn more**

[Add FlexMatch to a game client](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-client.html)

[Set Up FlexMatch event notification](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html)

[How Amazon GameLift FlexMatch works](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/gamelift-match.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/StartMatchmaking)

## Synopsis

```
start-matchmaking
[--ticket-id <value>]
--configuration-name <value>
--players <value>
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

`--ticket-id` (string)

A unique identifier for a matchmaking ticket. If no ticket ID is specified here, Amazon GameLift will generate one in the form of a UUID. Use this identifier to track the matchmaking ticket status and retrieve match results.

`--configuration-name` (string)

Name of the matchmaking configuration to use for this request. Matchmaking configurations must exist in the same Region as this request. You can use either the configuration name or ARN value.

`--players` (list)

Information on each player to be matched. This information must include a player ID, and may contain player attributes and latency data to be used in the matchmaking process. After a successful match, `Player` objects contain the name of the team the player is assigned to.

You can include up to 10 `Players` in a `StartMatchmaking` request.

(structure)

Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.

PlayerId -> (string)

A unique identifier for a player

PlayerAttributes -> (map)

A collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the *playerAttributes* used in a matchmaking rule set. Example: `"PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S": "deathmatch"}}` .

You can provide up to 10 `PlayerAttributes` .

key -> (string)

value -> (structure)

Values for use in player attribute key-value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array, or data map. Each `AttributeValue` object can use only one of the available properties.

S -> (string)

For single string values. Maximum string length is 100 characters.

N -> (double)

For number values, expressed as double.

SL -> (list)

For a list of up to 100 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.

(string)

SDM -> (map)

For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters.

key -> (string)

value -> (double)

Team -> (string)

Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.

LatencyInMs -> (map)

A set of values, expressed in milliseconds, that indicates the amount of latency that a player experiences when connected to Amazon Web Services Regions. If this property is present, FlexMatch considers placing the match only in Regions for which latency is reported.

If a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no Regions are available to the player and the ticket is not matchable.

key -> (string)

value -> (integer)

Shorthand Syntax:

```
PlayerId=string,PlayerAttributes={KeyName1={S=string,N=double,SL=[string,string],SDM={KeyName1=double,KeyName2=double}},KeyName2={S=string,N=double,SL=[string,string],SDM={KeyName1=double,KeyName2=double}}},Team=string,LatencyInMs={KeyName1=integer,KeyName2=integer} ...
```

JSON Syntax:

```
[
  {
    "PlayerId": "string",
    "PlayerAttributes": {"string": {
          "S": "string",
          "N": double,
          "SL": ["string", ...],
          "SDM": {"string": double
            ...}
        }
      ...},
    "Team": "string",
    "LatencyInMs": {"string": integer
      ...}
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

MatchmakingTicket -> (structure)

Ticket representing the matchmaking request. This object include the information included in the request, ticket status, and match results as generated during the matchmaking process.

TicketId -> (string)

A unique identifier for a matchmaking ticket.

ConfigurationName -> (string)

Name of the matchmaking configuration that is used with this ticket. Matchmaking configurations determine how players are grouped into a match and how a new game session is created for the match.

ConfigurationArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) associated with the GameLift matchmaking configuration resource that is used with this ticket.

Status -> (string)

Current status of the matchmaking request.

- **QUEUED** â The matchmaking request has been received and is currently waiting to be processed.
- **SEARCHING** â The matchmaking request is currently being processed.
- **REQUIRES_ACCEPTANCE** â A match has been proposed and the players must accept the match. This status is used only with requests that use a matchmaking configuration with a player acceptance requirement.
- **PLACING** â The FlexMatch engine has matched players and is in the process of placing a new game session for the match.
- **COMPLETED** â Players have been matched and a game session is ready to host the players. A ticket in this state contains the necessary connection information for players.
- **FAILED** â The matchmaking request was not completed.
- **CANCELLED** â The matchmaking request was canceled. This may be the result of a `StopMatchmaking` operation or a proposed match that one or more players failed to accept.
- **TIMED_OUT** â The matchmaking request was not successful within the duration specified in the matchmaking configuration.

### Note

Matchmaking requests that fail to successfully complete (statuses FAILED, CANCELLED, TIMED_OUT) can be resubmitted as new requests with new ticket IDs.

StatusReason -> (string)

Code to explain the current status. For example, a status reason may indicate when a ticket has returned to `SEARCHING` status after a proposed match fails to receive player acceptances.

StatusMessage -> (string)

Additional information about the current status.

StartTime -> (timestamp)

Time stamp indicating when this matchmaking request was received. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ).

EndTime -> (timestamp)

Time stamp indicating when the matchmaking request stopped being processed due to successful completion, timeout, or cancellation. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ).

Players -> (list)

A set of `Player` objects, each representing a player to find matches for. Players are identified by a unique player ID and may include latency data for use during matchmaking. If the ticket is in status `COMPLETED` , the `Player` objects include the team the players were assigned to in the resulting match.

(structure)

Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.

PlayerId -> (string)

A unique identifier for a player

PlayerAttributes -> (map)

A collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the *playerAttributes* used in a matchmaking rule set. Example: `"PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S": "deathmatch"}}` .

You can provide up to 10 `PlayerAttributes` .

key -> (string)

value -> (structure)

Values for use in player attribute key-value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array, or data map. Each `AttributeValue` object can use only one of the available properties.

S -> (string)

For single string values. Maximum string length is 100 characters.

N -> (double)

For number values, expressed as double.

SL -> (list)

For a list of up to 100 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.

(string)

SDM -> (map)

For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters.

key -> (string)

value -> (double)

Team -> (string)

Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.

LatencyInMs -> (map)

A set of values, expressed in milliseconds, that indicates the amount of latency that a player experiences when connected to Amazon Web Services Regions. If this property is present, FlexMatch considers placing the match only in Regions for which latency is reported.

If a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no Regions are available to the player and the ticket is not matchable.

key -> (string)

value -> (integer)

GameSessionConnectionInfo -> (structure)

Connection information for a new game session. Once a match is made, the FlexMatch engine creates a new game session for it. This information is added to the matchmaking ticket, which you can be retrieve by calling [DescribeMatchmaking](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeMatchmaking.html) .

GameSessionArn -> (string)

A unique identifier for the game session. Use the game session ID.

IpAddress -> (string)

The IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.

DnsName -> (string)

The DNS identifier assigned to the instance that is running the game session. Values have the following format:

- TLS-enabled fleets: `<unique identifier>.<region identifier>.amazongamelift.com` .
- Non-TLS-enabled fleets: `ec2-<unique identifier>.compute.amazonaws.com` . (See [Amazon EC2 Instance IP Addressing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses) .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

Port -> (integer)

The port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.

MatchedPlayerSessions -> (list)

A collection of player session IDs, one for each player ID that was included in the original matchmaking request.

(structure)

Represents a new player session that is created as a result of a successful FlexMatch match. A successful match automatically creates new player sessions for every player ID in the original matchmaking request.

When players connect to the matchâs game session, they must include both player ID and player session ID in order to claim their assigned player slot.

PlayerId -> (string)

A unique identifier for a player

PlayerSessionId -> (string)

A unique identifier for a player session

EstimatedWaitTime -> (integer)

Average amount of time (in seconds) that players are currently waiting for a match. If there is not enough recent data, this property may be empty.