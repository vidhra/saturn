# send-automation-signalÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/send-automation-signal.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/send-automation-signal.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# send-automation-signal

## Description

Sends a signal to an Automation execution to change the current behavior or status of the execution.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/SendAutomationSignal)

## Synopsis

```
send-automation-signal
--automation-execution-id <value>
--signal-type <value>
[--payload <value>]
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

`--automation-execution-id` (string)

The unique identifier for an existing Automation execution that you want to send the signal to.

`--signal-type` (string)

The type of signal to send to an Automation execution.

Possible values:

- `Approve`
- `Reject`
- `StartStep`
- `StopStep`
- `Resume`
- `Revoke`

`--payload` (map)

The data sent with the signal. The data schema depends on the type of signal used in the request.

For `Approve` and `Reject` signal types, the payload is an optional comment that you can send with the signal type. For example:

`Comment="Looks good"`

For `StartStep` and `Resume` signal types, you must send the name of the Automation step to start or resume as the payload. For example:

`StepName="step1"`

For the `StopStep` signal type, you must send the step execution ID as the payload. For example:

`StepExecutionId="97fff367-fc5a-4299-aed8-0123456789ab"`

key -> (string)

value -> (list)

(string)

Shorthand Syntax:

```
KeyName1=string,string,KeyName2=string,string
```

JSON Syntax:

```
{"string": ["string", ...]
  ...}
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To send a signal to an automation execution**

The following `send-automation-signal` example sends an Approve signal to an Automation execution.

```
aws ssm send-automation-signal \
    --automation-execution-id 73c8eef8-f4ee-4a05-820c-e354fEXAMPLE \
    --signal-type "Approve"
```

This command produces no output.

For more information, see [Running an Automation Workflow with Approvers](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing-approval.html) in the *AWS Systems Manager User Guide*.

## Output

None