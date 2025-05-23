# open-tunnelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2-instance-connect/open-tunnel.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2-instance-connect/open-tunnel.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2-instance-connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2-instance-connect/index.html#cli-aws-ec2-instance-connect) ]

# open-tunnel

## Description

Opens a websocket tunnel to the specified EC2 Instance or private ip.

## Synopsis

```
open-tunnel
[--instance-id <value>]
[--instance-connect-endpoint-id <value>]
[--instance-connect-endpoint-dns-name <value>]
[--private-ip-address <value>]
[--remote-port <value>]
[--local-port <value>]
[--max-tunnel-duration <value>]
[--max-websocket-connections <value>]
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

`--instance-id` (string)
Specify the id of the EC2 instance that a tunnel should be opened for.

`--instance-connect-endpoint-id` (string)
Specify the EC2 Instance Connect Endpoint Id that should be used to open the tunnel.

`--instance-connect-endpoint-dns-name` (string)
Specify the EC2 Instance Connect Endpoint DNS Name that should be used to open the tunnel. If this is specified, you must specify instance-connect-endpoint-id.

`--private-ip-address` (string)
Specify the private ip address to open a tunnel for. If this is specified, you must specify instance-connect-endpoint-id.

`--remote-port` (integer)
Specify the remote port to connect to on the instance. This defaults to port 22.

`--local-port` (integer)
Specify the local port to listen on. Each new connection will have a separate websocket tunnel read and write to it.

`--max-tunnel-duration` (integer)
Specify the maximum time, in seconds, to keep a websocket tunnel alive for. This defaults to 3600 seconds.

`--max-websocket-connections` (integer)
Specify the maximum amount of websocket connections allowed when local-port is specified. This value defaults to 10.

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