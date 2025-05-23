# describe-tunnelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/describe-tunnel.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/describe-tunnel.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotsecuretunneling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/index.html#cli-aws-iotsecuretunneling) ]

# describe-tunnel

## Description

Gets information about a tunnel identified by the unique tunnel id.

Requires permission to access the [DescribeTunnel](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotsecuretunneling-2018-10-05/DescribeTunnel)

## Synopsis

```
describe-tunnel
--tunnel-id <value>
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

`--tunnel-id` (string)

The tunnel to describe.

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

tunnel -> (structure)

The tunnel being described.

tunnelId -> (string)

A unique alpha-numeric ID that identifies a tunnel.

tunnelArn -> (string)

The Amazon Resource Name (ARN) of a tunnel.

status -> (string)

The status of a tunnel. Valid values are: Open and Closed.

sourceConnectionState -> (structure)

The connection state of the source application.

status -> (string)

The connection status of the tunnel. Valid values are `CONNECTED` and `DISCONNECTED` .

lastUpdatedAt -> (timestamp)

The last time the connection status was updated.

destinationConnectionState -> (structure)

The connection state of the destination application.

status -> (string)

The connection status of the tunnel. Valid values are `CONNECTED` and `DISCONNECTED` .

lastUpdatedAt -> (timestamp)

The last time the connection status was updated.

description -> (string)

A description of the tunnel.

destinationConfig -> (structure)

The destination configuration that specifies the thing name of the destination device and a service name that the local proxy uses to connect to the destination application.

thingName -> (string)

The name of the IoT thing to which you want to connect.

services -> (list)

A list of service names that identify the target application. The IoT client running on the destination device reads this value and uses it to look up a port or an IP address and a port. The IoT client instantiates the local proxy, which uses this information to connect to the destination application.

(string)

timeoutConfig -> (structure)

Timeout configuration for the tunnel.

maxLifetimeTimeoutMinutes -> (integer)

The maximum amount of time (in minutes) a tunnel can remain open. If not specified, maxLifetimeTimeoutMinutes defaults to 720 minutes. Valid values are from 1 minute to 12 hours (720 minutes)

tags -> (list)

A list of tag metadata associated with the secure tunnel.

(structure)

An arbitary key/value pair used to add searchable metadata to secure tunnel resources.

key -> (string)

The key of the tag.

value -> (string)

The value of the tag.

createdAt -> (timestamp)

The time when the tunnel was created.

lastUpdatedAt -> (timestamp)

The last time the tunnel was updated.