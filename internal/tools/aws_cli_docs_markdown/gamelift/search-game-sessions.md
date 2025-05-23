# search-game-sessionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/search-game-sessions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/search-game-sessions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# search-game-sessions

## Description

Retrieves all active game sessions that match a set of search criteria and sorts them into a specified order.

This operation is not designed to continually track game session status because that practice can cause you to exceed your API limit and generate errors. Instead, configure an Amazon Simple Notification Service (Amazon SNS) topic to receive notifications from a matchmaker or a game session placement queue.

When searching for game sessions, you specify exactly where you want to search and provide a search filter expression, a sort expression, or both. A search request can search only one fleet, but it can search all of a fleetâs locations.

This operation can be used in the following ways:

- To search all game sessions that are currently running on all locations in a fleet, provide a fleet or alias ID. This approach returns game sessions in the fleetâs home Region and all remote locations that fit the search criteria.
- To search all game sessions that are currently running on a specific fleet location, provide a fleet or alias ID and a location name. For location, you can specify a fleetâs home Region or any remote location.

Use the pagination parameters to retrieve results as a set of sequential pages.

If successful, a `GameSession` object is returned for each game session that matches the request. Search finds game sessions that are in `ACTIVE` status only. To retrieve information on game sessions in other statuses, use [DescribeGameSessions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeGameSessions.html) .

To set search and sort criteria, create a filter expression using the following game session attributes. For game session search examples, see the Examples section of this topic.

- **gameSessionId** â A unique identifier for the game session. You can use either a `GameSessionId` or `GameSessionArn` value.
- **gameSessionName** â Name assigned to a game session. Game session names do not need to be unique to a game session.
- **gameSessionProperties** â A set of key-value pairs that can store custom data in a game session. For example: `{"Key": "difficulty", "Value": "novice"}` . The filter expression must specify the [https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameProperty](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameProperty) â a `Key` and a string `Value` to search for the game sessions. For example, to search for the above key-value pair, specify the following search filter: `gameSessionProperties.difficulty = "novice"` . All game property values are searched as strings. For examples of searching game sessions, see the ones below, and also see [Search game sessions by game property](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#game-properties-search) .
- **maximumSessions** â Maximum number of player sessions allowed for a game session.
- **creationTimeMillis** â Value indicating when a game session was created. It is expressed in Unix time as milliseconds.
- **playerSessionCount** â Number of players currently connected to a game session. This value changes rapidly as players join the session or drop out.
- **hasAvailablePlayerSessions** â Boolean value indicating whether a game session has reached its maximum number of players. It is highly recommended that all search requests include this filter attribute to optimize search performance and return only sessions that players can join.

### Note

Returned values for `playerSessionCount` and `hasAvailablePlayerSessions` change quickly as players join sessions and others drop out. Results should be considered a snapshot in time. Be sure to refresh search results often, and handle sessions that fill up before a player can join.

[All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/SearchGameSessions)

`search-game-sessions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `GameSessions`

## Synopsis

```
search-game-sessions
[--fleet-id <value>]
[--alias-id <value>]
[--location <value>]
[--filter-expression <value>]
[--sort-expression <value>]
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

`--fleet-id` (string)

A unique identifier for the fleet to search for active game sessions. You can use either the fleet ID or ARN value. Each request must reference either a fleet ID or alias ID, but not both.

`--alias-id` (string)

A unique identifier for the alias associated with the fleet to search for active game sessions. You can use either the alias ID or ARN value. Each request must reference either a fleet ID or alias ID, but not both.

`--location` (string)

A fleet location to search for game sessions. You can specify a fleetâs home Region or a remote location. Use the Amazon Web Services Region code format, such as `us-west-2` .

`--filter-expression` (string)

String containing the search criteria for the session search. If no filter expression is included, the request returns results for all game sessions in the fleet that are in `ACTIVE` status.

A filter expression can contain one or multiple conditions. Each condition consists of the following:

- **Operand** â Name of a game session attribute. Valid values are `gameSessionName` , `gameSessionId` , `gameSessionProperties` , `maximumSessions` , `creationTimeMillis` , `playerSessionCount` , `hasAvailablePlayerSessions` .
- **Comparator** â Valid comparators are: `=` , `<>` , `<` , `>` , `<=` , `>=` .
- **Value** â Value to be searched for. Values may be numbers, boolean values (true/false) or strings depending on the operand. String values are case sensitive and must be enclosed in single quotes. Special characters must be escaped. Boolean and string values can only be used with the comparators `=` and `<>` . For example, the following filter expression searches on `gameSessionName` : â`FilterExpression": "gameSessionName = 'Matt\\'s Awesome Game 1'"` .

To chain multiple conditions in a single expression, use the logical keywords `AND` , `OR` , and `NOT` and parentheses as needed. For example: `x AND y AND NOT z` , `NOT (x OR y)` .

Session search evaluates conditions from left to right using the following precedence rules:

- `=` , `<>` , `<` , `>` , `<=` , `>=`
- Parentheses
- NOT
- AND
- OR

For example, this filter expression retrieves game sessions hosting at least ten players that have an open player slot: `"maximumSessions>=10 AND hasAvailablePlayerSessions=true"` .

`--sort-expression` (string)

Instructions on how to sort the search results. If no sort expression is included, the request returns results in random order. A sort expression consists of the following elements:

- **Operand** â Name of a game session attribute. Valid values are `gameSessionName` , `gameSessionId` , `gameSessionProperties` , `maximumSessions` , `creationTimeMillis` , `playerSessionCount` , `hasAvailablePlayerSessions` .
- **Order** â Valid sort orders are `ASC` (ascending) and `DESC` (descending).

For example, this sort expression returns the oldest active sessions first: `"SortExpression": "creationTimeMillis ASC"` . Results with a null value for the sort operand are returned at the end of the list.

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

GameSessions -> (list)

A collection of objects containing game session properties for each session that matches the request.

(structure)

Properties describing a game session.

A game session in ACTIVE status can host players. When a game session ends, its status is set to `TERMINATED` .

Amazon GameLift retains a game session resource for 30 days after the game session ends. You can reuse idempotency token values after this time. Game session logs are retained for 14 days.

[All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

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

NextToken -> (string)

A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.