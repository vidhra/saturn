# get-command-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-command-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-command-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# get-command-execution

## Description

Gets information about the specific command execution on a single device.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetCommandExecution)

## Synopsis

```
get-command-execution
--execution-id <value>
--target-arn <value>
[--include-result | --no-include-result]
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

`--execution-id` (string)

The unique identifier for the command execution. This information is returned as a response of the `StartCommandExecution` API request.

`--target-arn` (string)

The Amazon Resource Number (ARN) of the device on which the command execution is being performed.

`--include-result` | `--no-include-result` (boolean)

Can be used to specify whether to include the result of the command execution in the `GetCommandExecution` API response. Your device can use this field to provide additional information about the command execution. You only need to specify this field when using the `AWS-IoT` namespace.

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

executionId -> (string)

The unique identifier of the command execution.

commandArn -> (string)

The Amazon Resource Number (ARN) of the command. For example, arn:aws:iot:<region>:<accountid>:command/<commandId>

targetArn -> (string)

The Amazon Resource Number (ARN) of the device on which the command execution is being performed.

status -> (string)

The status of the command execution. After your devices receive the command and start performing the operations specified in the command, it can use the `UpdateCommandExecution` MQTT API to update the status information.

statusReason -> (structure)

Your devices can use this parameter to provide additional context about the status of a command execution using a reason code and description.

reasonCode -> (string)

A code that provides additional context for the command execution status.

reasonDescription -> (string)

A literal string for devices to optionally provide additional information about the reason code for a command execution status.

result -> (map)

The result value for the current state of the command execution. The status provides information about the progress of the command execution. The device can use the result field to share additional details about the execution such as a return value of a remote function call.

### Note

If you use the `AWS-IoT-FleetWise` namespace, then this field is not applicable in the API response.

key -> (string)

value -> (structure)

The result value of the command execution. The device can use the result field to share additional details about the execution such as a return value of a remote function call.

### Note

This field is not applicable if you use the `AWS-IoT-FleetWise` namespace.

S -> (string)

An attribute of type String. For example:

`"S": "Hello"`

B -> (boolean)

An attribute of type Boolean. For example:

`"BOOL": true`

BIN -> (blob)

An attribute of type Binary.

parameters -> (map)

The list of parameters that the `StartCommandExecution` API used when performing the command on the device.

key -> (string)

value -> (structure)

The range of possible values thatâs used to describe a specific command parameter.

### Note

The `commandParameterValue` can only have one of the below fields listed.

S -> (string)

An attribute of type String. For example:

`"S": "Hello"`

B -> (boolean)

An attribute of type Boolean. For example:

`"BOOL": true`

I -> (integer)

An attribute of type Integer (Thirty-Two Bits).

L -> (long)

An attribute of type Long.

D -> (double)

An attribute of type Double (Sixty-Four Bits).

BIN -> (blob)

An attribute of type Binary. For example:

`"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"`

UL -> (string)

An attribute of type unsigned long.

executionTimeoutSeconds -> (long)

Specifies the amount of time in seconds that the device can take to finish a command execution. A timer starts when the command execution is created. If the command execution status is not set to another terminal state before the timer expires, it will automatically update to `TIMED_OUT` .

createdAt -> (timestamp)

The timestamp, when the command execution was created.

lastUpdatedAt -> (timestamp)

The timestamp, when the command execution was last updated.

startedAt -> (timestamp)

The timestamp, when the command execution was started.

completedAt -> (timestamp)

The timestamp, when the command execution was completed.

timeToLive -> (timestamp)

The time to live (TTL) parameter that indicates the duration for which executions will be retained in your account. The default value is six months.