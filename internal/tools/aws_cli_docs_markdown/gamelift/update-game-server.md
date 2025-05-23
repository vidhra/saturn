# update-game-serverÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-server.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-server.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# update-game-server

## Description

**This operation is used with the Amazon GameLift FleetIQ solution and game server groups.**

Updates information about a registered game server to help Amazon GameLift FleetIQ track game server availability. This operation is called by a game server process that is running on an instance in a game server group.

Use this operation to update the following types of game server information. You can make all three types of updates in the same request:

- To update the game serverâs utilization status from `AVAILABLE` (when the game server is available to be claimed) to `UTILIZED` (when the game server is currently hosting games). Identify the game server and game server group and specify the new utilization status. You canât change the status from to `UTILIZED` to `AVAILABLE` .
- To report health status, identify the game server and game server group and set health check to `HEALTHY` . If a game server does not report health status for a certain length of time, the game server is no longer considered healthy. As a result, it will be eventually deregistered from the game server group to avoid affecting utilization metrics. The best practice is to report health every 60 seconds.
- To change game server metadata, provide updated game server data.

Once a game server is successfully updated, the relevant statuses and timestamps are updated.

**Learn more**

[Amazon GameLift FleetIQ Guide](https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/UpdateGameServer)

## Synopsis

```
update-game-server
--game-server-group-name <value>
--game-server-id <value>
[--game-server-data <value>]
[--utilization-status <value>]
[--health-check <value>]
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

`--game-server-group-name` (string)

A unique identifier for the game server group where the game server is running.

`--game-server-id` (string)

A custom string that uniquely identifies the game server to update.

`--game-server-data` (string)

A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service when it requests information on game servers.

`--utilization-status` (string)

Indicates if the game server is available or is currently hosting gameplay. You can update a game server status from `AVAILABLE` to `UTILIZED` , but you canât change a the status from `UTILIZED` to `AVAILABLE` .

Possible values:

- `AVAILABLE`
- `UTILIZED`

`--health-check` (string)

Indicates health status of the game server. A request that includes this parameter updates the game serverâs *LastHealthCheckTime* timestamp.

Possible values:

- `HEALTHY`

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

GameServer -> (structure)

Object that describes the newly updated game server.

GameServerGroupName -> (string)

A unique identifier for the game server group where the game server is running.

GameServerGroupArn -> (string)

The ARN identifier for the game server group where the game server is located.

GameServerId -> (string)

A custom string that uniquely identifies the game server. Game server IDs are developer-defined and are unique across all game server groups in an Amazon Web Services account.

InstanceId -> (string)

The unique identifier for the instance where the game server is running. This ID is available in the instance metadata. EC2 instance IDs use a 17-character format, for example: `i-1234567890abcdef0` .

ConnectionInfo -> (string)

The port and IP address that must be used to establish a client connection to the game server.

GameServerData -> (string)

A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service when it requests information on game servers.

ClaimStatus -> (string)

Indicates when an available game server has been reserved for gameplay but has not yet started hosting a game. Once it is claimed, the game server remains in `CLAIMED` status for a maximum of one minute. During this time, game clients connect to the game server to start the game and trigger the game server to update its utilization status. After one minute, the game server claim status reverts to null.

UtilizationStatus -> (string)

Indicates whether the game server is currently available for new games or is busy. Possible statuses include:

- `AVAILABLE` - The game server is available to be claimed. A game server that has been claimed remains in this status until it reports game hosting activity.
- `UTILIZED` - The game server is currently hosting a game session with players.

RegistrationTime -> (timestamp)

Timestamp that indicates when the game server registered. The format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ).

LastClaimTime -> (timestamp)

Timestamp that indicates the last time the game server was claimed. The format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ). This value is used to calculate when a claimed game serverâs status should revert to null.

LastHealthCheckTime -> (timestamp)

Timestamp that indicates the last time the game server was updated with health status. The format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ). After game server registration, this property is only changed when a game server update specifies a health check value.