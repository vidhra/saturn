# sshÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2-instance-connect/ssh.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2-instance-connect/ssh.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2-instance-connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2-instance-connect/index.html#cli-aws-ec2-instance-connect) ]

# ssh

## Description

Connect to your EC2 instance using your OpenSSH client.

## Synopsis

```
ssh
--instance-id <value>
[--instance-ip <value>]
[--private-key-file <value>]
[--os-user <value>]
[--ssh-port <value>]
[--local-forwarding <value>]
[--connection-type <value>]
[--eice-options <value>]
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
Specify the ID of the EC2 instance to connect to.

`--instance-ip` (string)
Specify the IP address of the instance to connect to.

`--private-key-file` (string)
Specify the path to the private key file for login.

`--os-user` (string)
Specify the OS SSH user. (Default: ec2-user)

`--ssh-port` (integer)
Specify the SSH port. (Default: 22)

`--local-forwarding` (string)
Specify the local forwarding specification as defined by your OpenSSH client. (Example: 3336:remote.host:3306)

`--connection-type` (string)
Specify how to SSH into the instance. (Default: auto)

- direct: SSH directly to the instance. The CLI tries to connect using the IP addresses in the following order:
- Public IPv4
- IPv6
- Private IPv4
- eice: SSH using EC2 Instance Connect Endpoint. The CLI always uses the private IPv4 address.
- auto: The CLI automatically determines the connection type (direct or eice) to use based on the instance info. Currently the CLI tries to connect using the IP addresses in the following order and with the corresponding connection type:
- Public IPv4: direct
- Private IPv4: eice
- IPv6: direct

In the future, we might change the behavior of the auto connection type. To ensure that your desired connection type is used, we recommend that you explicitly set the âconnection-type to either direct or eice.

`--eice-options` (structure)
Specify the options for your EC2 Instance Connect Endpoint.maxTunnelDuration -> (integer)

Specify the maximum duration (in seconds) for an established TCP connection. Default: 3600 seconds (1 hour).

endpointId -> (string)

Specify the EC2 Instance Connect Endpoint ID to use to open the tunnel.

dnsName -> (string)

Specify the EC2 Instance Connect Endpoint DNS name to use to open the tunnel. If this is specified, you must also specify endpointId.

Shorthand Syntax:

```
maxTunnelDuration=integer,endpointId=string,dnsName=string
```

JSON Syntax:

```
{
  "maxTunnelDuration": integer,
  "endpointId": "string",
  "dnsName": "string"
}
```

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