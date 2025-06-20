# update-runtime-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-runtime-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-runtime-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# update-runtime-configuration

## Description

Updates the runtime configuration for the specified fleet. The runtime configuration tells Amazon GameLift how to launch server processes on computes in managed EC2 and Anywhere fleets. You can update a fleetâs runtime configuration at any time after the fleet is created; it does not need to be in `ACTIVE` status.

To update runtime configuration, specify the fleet ID and provide a `RuntimeConfiguration` with an updated set of server process configurations.

If successful, the fleetâs runtime configuration settings are updated. Fleet computes that run game server processes regularly check for and receive updated runtime configurations. The computes immediately take action to comply with the new configuration by launching new server processes or by not replacing existing processes when they shut down. Updating a fleetâs runtime configuration never affects existing server processes.

**Learn more**

[Setting up Amazon GameLift fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/UpdateRuntimeConfiguration)

## Synopsis

```
update-runtime-configuration
--fleet-id <value>
--runtime-configuration <value>
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

`--fleet-id` (string)

A unique identifier for the fleet to update runtime configuration for. You can use either the fleet ID or ARN value.

`--runtime-configuration` (structure)

Instructions for launching server processes on fleet computes. Server processes run either a custom game build executable or a Amazon GameLift Realtime script. The runtime configuration lists the types of server processes to run, how to launch them, and the number of processes to run concurrently.

ServerProcesses -> (list)

A collection of server process configurations that identify what server processes to run on fleet computes.

(structure)

A set of instructions for launching server processes on fleet computes. Server processes run either an executable in a custom game build or a Amazon GameLift Realtime script. Server process configurations are part of a fleetâs runtime configuration.

LaunchPath -> (string)

The location of a game build executable or Realtime script. Game builds and Realtime scripts are installed on instances at the root:

- Windows (custom game builds only): `C:\game` . Example: â`C:\game\MyGame\server.exe` â
- Linux: `/local/game` . Examples: â`/local/game/MyGame/server.exe` â or â`/local/game/MyRealtimeScript.js` â

### Note

Amazon GameLift doesnât support the use of setup scripts that launch the game executable. For custom game builds, this parameter must indicate the executable that calls the server SDK operations `initSDK()` and `ProcessReady()` .

Parameters -> (string)

An optional list of parameters to pass to the server executable or Realtime script on launch.

ConcurrentExecutions -> (integer)

The number of server processes using this configuration that run concurrently on each instance or compute.

MaxConcurrentGameSessionActivations -> (integer)

The number of game sessions in status `ACTIVATING` to allow on an instance or compute. This setting limits the instance resources that can be used for new game activations at any one time.

GameSessionActivationTimeoutSeconds -> (integer)

The maximum amount of time (in seconds) allowed to launch a new game session and have it report ready to host players. During this time, the game session is in status `ACTIVATING` . If the game session does not become active before the timeout, it is ended and the game session status is changed to `TERMINATED` .

Shorthand Syntax:

```
ServerProcesses=[{LaunchPath=string,Parameters=string,ConcurrentExecutions=integer},{LaunchPath=string,Parameters=string,ConcurrentExecutions=integer}],MaxConcurrentGameSessionActivations=integer,GameSessionActivationTimeoutSeconds=integer
```

JSON Syntax:

```
{
  "ServerProcesses": [
    {
      "LaunchPath": "string",
      "Parameters": "string",
      "ConcurrentExecutions": integer
    }
    ...
  ],
  "MaxConcurrentGameSessionActivations": integer,
  "GameSessionActivationTimeoutSeconds": integer
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

RuntimeConfiguration -> (structure)

The runtime configuration currently in use by computes in the fleet. If the update is successful, all property changes are shown.

ServerProcesses -> (list)

A collection of server process configurations that identify what server processes to run on fleet computes.

(structure)

A set of instructions for launching server processes on fleet computes. Server processes run either an executable in a custom game build or a Amazon GameLift Realtime script. Server process configurations are part of a fleetâs runtime configuration.

LaunchPath -> (string)

The location of a game build executable or Realtime script. Game builds and Realtime scripts are installed on instances at the root:

- Windows (custom game builds only): `C:\game` . Example: â`C:\game\MyGame\server.exe` â
- Linux: `/local/game` . Examples: â`/local/game/MyGame/server.exe` â or â`/local/game/MyRealtimeScript.js` â

### Note

Amazon GameLift doesnât support the use of setup scripts that launch the game executable. For custom game builds, this parameter must indicate the executable that calls the server SDK operations `initSDK()` and `ProcessReady()` .

Parameters -> (string)

An optional list of parameters to pass to the server executable or Realtime script on launch.

ConcurrentExecutions -> (integer)

The number of server processes using this configuration that run concurrently on each instance or compute.

MaxConcurrentGameSessionActivations -> (integer)

The number of game sessions in status `ACTIVATING` to allow on an instance or compute. This setting limits the instance resources that can be used for new game activations at any one time.

GameSessionActivationTimeoutSeconds -> (integer)

The maximum amount of time (in seconds) allowed to launch a new game session and have it report ready to host players. During this time, the game session is in status `ACTIVATING` . If the game session does not become active before the timeout, it is ended and the game session status is changed to `TERMINATED` .