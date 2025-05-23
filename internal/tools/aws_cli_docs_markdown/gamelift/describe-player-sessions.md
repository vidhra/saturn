# describe-player-sessionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-player-sessions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-player-sessions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# describe-player-sessions

## Description

Retrieves properties for one or more player sessions.

This action can be used in the following ways:

- To retrieve a specific player session, provide the player session ID only.
- To retrieve all player sessions in a game session, provide the game session ID only.
- To retrieve all player sessions for a specific player, provide a player ID only.

To request player sessions, specify either a player session ID, game session ID, or player ID. You can filter this request by player session status. If you provide a specific `PlayerSessionId` or `PlayerId` , Amazon GameLift ignores the filter criteria. Use the pagination parameters to retrieve results as a set of sequential pages.

If successful, a `PlayerSession` object is returned for each session that matches the request.

**Related actions**

[All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribePlayerSessions)

`describe-player-sessions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `PlayerSessions`

## Synopsis

```
describe-player-sessions
[--game-session-id <value>]
[--player-id <value>]
[--player-session-id <value>]
[--player-session-status-filter <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

A unique identifier for the game session to retrieve player sessions for.

`--player-id` (string)

A unique identifier for a player to retrieve player sessions for.

`--player-session-id` (string)

A unique identifier for a player session to retrieve.

`--player-session-status-filter` (string)

Player session status to filter results on. Note that when a PlayerSessionId or PlayerId is provided in a DescribePlayerSessions request, then the PlayerSessionStatusFilter has no effect on the response.

Possible player session statuses include the following:

- **RESERVED** â The player session request has been received, but the player has not yet connected to the server process and/or been validated.
- **ACTIVE** â The player has been validated by the server process and is currently connected.
- **COMPLETED** â The player connection has been dropped.
- **TIMEDOUT** â A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds).

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

PlayerSessions -> (list)

A collection of objects containing properties for each player session that matches the request.

(structure)

Represents a player session. Player sessions are created either for a specific game session, or as part of a game session placement or matchmaking request. A player session can represents a reserved player slot in a game session (when status is `RESERVED` ) or actual player activity in a game session (when status is `ACTIVE` ). A player session object, including player data, is automatically passed to a game session when the player connects to the game session and is validated. After the game session ends, player sessions information is retained for 30 days and then removed.

**Related actions**

[All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

PlayerSessionId -> (string)

A unique identifier for a player session.

PlayerId -> (string)

A unique identifier for a player that is associated with this player session.

GameSessionId -> (string)

A unique identifier for the game session that the player session is connected to.

FleetId -> (string)

A unique identifier for the fleet that the playerâs game session is running on.

FleetArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) associated with the GameLift fleet that the playerâs game session is running on.

CreationTime -> (timestamp)

A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ).

TerminationTime -> (timestamp)

A time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ).

Status -> (string)

Current status of the player session.

Possible player session statuses include the following:

- **RESERVED** â The player session request has been received, but the player has not yet connected to the server process and/or been validated.
- **ACTIVE** â The player has been validated by the server process and is currently connected.
- **COMPLETED** â The player connection has been dropped.
- **TIMEDOUT** â A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds).

IpAddress -> (string)

The IP address of the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.

DnsName -> (string)

The DNS identifier assigned to the instance that is running the game session. Values have the following format:

- TLS-enabled fleets: `<unique identifier>.<region identifier>.amazongamelift.com` .
- Non-TLS-enabled fleets: `ec2-<unique identifier>.compute.amazonaws.com` . (See [Amazon EC2 Instance IP Addressing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses) .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

Port -> (integer)

Port number for the game session. To connect to a Amazon GameLift server process, an app needs both the IP address and port number.

PlayerData -> (string)

Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game.

NextToken -> (string)

A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.