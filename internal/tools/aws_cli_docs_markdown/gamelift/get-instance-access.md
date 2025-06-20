# get-instance-accessÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/get-instance-access.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/get-instance-access.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# get-instance-access

## Description

Requests authorization to remotely connect to an instance in an Amazon GameLift managed fleet. Use this operation to connect to instances with game servers that use Amazon GameLift server SDK 4.x or earlier. To connect to instances with game servers that use server SDK 5.x or later, call [https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetComputeAccess](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetComputeAccess) .

To request access to an instance, specify IDs for the instance and the fleet it belongs to. You can retrieve instance IDs for a fleet by calling [DescribeInstances](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeInstances.html) with the fleet ID.

If successful, this operation returns an IP address and credentials. The returned credentials match the operating system of the instance, as follows:

- For a Windows instance: returns a user name and secret (password) for use with a Windows Remote Desktop client.
- For a Linux instance: returns a user name and secret (RSA private key) for use with an SSH client. You must save the secret to a `.pem` file. If youâre using the CLI, see the example [Get credentials for a Linux instance](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetInstanceAccess.html#API_GetInstanceAccess_Examples) for tips on automatically saving the secret to a `.pem` file.

**Learn more**

[Remotely connect to fleet instances](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-remote-access.html)

[Debug fleet issues](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-debug.html)

**Related actions**

[All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/GetInstanceAccess)

## Synopsis

```
get-instance-access
--fleet-id <value>
--instance-id <value>
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

A unique identifier for the fleet that contains the instance you want to access. You can request access to instances in EC2 fleets with the following statuses: `ACTIVATING` , `ACTIVE` , or `ERROR` . Use either a fleet ID or an ARN value.

### Note

You can access fleets in `ERROR` status for a short period of time before Amazon GameLift deletes them.

`--instance-id` (string)

A unique identifier for the instance you want to access. You can access an instance in any status.

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

InstanceAccess -> (structure)

The connection information for a fleet instance, including IP address and access credentials.

FleetId -> (string)

A unique identifier for the fleet containing the instance to be accessed.

InstanceId -> (string)

A unique identifier for the instance to be accessed.

IpAddress -> (string)

IP address assigned to the instance.

OperatingSystem -> (string)

Operating system that is running on the instance.

Credentials -> (structure)

Security credentials that are required to access the instance.

UserName -> (string)

A user name for logging in.

Secret -> (string)

Secret string. For Windows instances, the secret is a password for use with Windows Remote Desktop. For Linux instances, itâs a private key for use with SSH.