# describe-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [stepfunctions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/index.html#cli-aws-stepfunctions) ]

# describe-execution

## Description

Provides information about a state machine execution, such as the state machine associated with the execution, the execution input and output, and relevant execution metadata. If youâve [redriven](https://docs.aws.amazon.com/step-functions/latest/dg/redrive-executions.html) an execution, you can use this API action to return information about the redrives of that execution. In addition, you can use this API action to return the Map Run Amazon Resource Name (ARN) if the execution was dispatched by a Map Run.

If you specify a version or alias ARN when you call the  StartExecution API action, `DescribeExecution` returns that ARN.

### Note

This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.

Executions of an `EXPRESS` state machine arenât supported by `DescribeExecution` unless a Map Run dispatched them.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/DescribeExecution)

## Synopsis

```
describe-execution
--execution-arn <value>
[--included-data <value>]
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

`--execution-arn` (string)

The Amazon Resource Name (ARN) of the execution to describe.

`--included-data` (string)

If your state machine definition is encrypted with a KMS key, callers must have `kms:Decrypt` permission to decrypt the definition. Alternatively, you can call DescribeStateMachine API with `includedData = METADATA_ONLY` to get a successful response without the encrypted definition.

Possible values:

- `ALL_DATA`
- `METADATA_ONLY`

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

executionArn -> (string)

The Amazon Resource Name (ARN) that identifies the execution.

stateMachineArn -> (string)

The Amazon Resource Name (ARN) of the executed stated machine.

name -> (string)

The name of the execution.

A name must *not* contain:

- white space
- brackets `< > { } [ ]`
- wildcard characters `? *`
- special characters `" # % \ ^ | ~ ` $ & , ; : /`
- control characters (`U+0000-001F` , `U+007F-009F` )

To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.

status -> (string)

The current status of the execution.

startDate -> (timestamp)

The date the execution is started.

stopDate -> (timestamp)

If the execution ended, the date the execution stopped.

input -> (string)

The string that contains the JSON input data of the execution. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.

inputDetails -> (structure)

Provides details about execution input or output.

included -> (boolean)

Indicates whether input or output was included in the response. Always `true` for API calls.

output -> (string)

The JSON output data of the execution. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.

### Note

This field is set only if the execution succeeds. If the execution fails, this field is null.

outputDetails -> (structure)

Provides details about execution input or output.

included -> (boolean)

Indicates whether input or output was included in the response. Always `true` for API calls.

traceHeader -> (string)

The X-Ray trace header that was passed to the execution.

mapRunArn -> (string)

The Amazon Resource Name (ARN) that identifies a Map Run, which dispatched this execution.

error -> (string)

The error string if the state machine execution failed.

cause -> (string)

The cause string if the state machine execution failed.

stateMachineVersionArn -> (string)

The Amazon Resource Name (ARN) of the state machine version associated with the execution. The version ARN is a combination of state machine ARN and the version number separated by a colon (:). For example, `stateMachineARN:1` .

If you start an execution from a `StartExecution` request without specifying a state machine version or alias ARN, Step Functions returns a null value.

stateMachineAliasArn -> (string)

The Amazon Resource Name (ARN) of the state machine alias associated with the execution. The alias ARN is a combination of state machine ARN and the alias name separated by a colon (:). For example, `stateMachineARN:PROD` .

If you start an execution from a `StartExecution` request with a state machine version ARN, this field will be null.

redriveCount -> (integer)

The number of times youâve redriven an execution. If you have not yet redriven an execution, the `redriveCount` is 0. This count is only updated if you successfully redrive an execution.

redriveDate -> (timestamp)

The date the execution was last redriven. If you have not yet redriven an execution, the `redriveDate` is null.

The `redriveDate` is unavailable if you redrive a Map Run that starts child workflow executions of type `EXPRESS` .

redriveStatus -> (string)

Indicates whether or not an execution can be redriven at a given point in time.

- For executions of type `STANDARD` , `redriveStatus` is `NOT_REDRIVABLE` if calling the  RedriveExecution API action would return the `ExecutionNotRedrivable` error.
- For a Distributed Map that includes child workflows of type `STANDARD` , `redriveStatus` indicates whether or not the Map Run can redrive child workflow executions.
- For a Distributed Map that includes child workflows of type `EXPRESS` , `redriveStatus` indicates whether or not the Map Run can redrive child workflow executions. You can redrive failed or timed out `EXPRESS` workflows *only if* theyâre a part of a Map Run. When you [redrive](https://docs.aws.amazon.com/step-functions/latest/dg/redrive-map-run.html) the Map Run, these workflows are restarted using the  StartExecution API action.

redriveStatusReason -> (string)

When `redriveStatus` is `NOT_REDRIVABLE` , `redriveStatusReason` specifies the reason why an execution cannot be redriven.

- For executions of type `STANDARD` , or for a Distributed Map that includes child workflows of type `STANDARD` , `redriveStatusReason` can include one of the following reasons:
- `State machine is in DELETING status` .
- `Execution is RUNNING and cannot be redriven` .
- `Execution is SUCCEEDED and cannot be redriven` .
- `Execution was started before the launch of RedriveExecution` .
- `Execution history event limit exceeded` .
- `Execution has exceeded the max execution time` .
- `Execution redrivable period exceeded` .
- For a Distributed Map that includes child workflows of type `EXPRESS` , `redriveStatusReason` is only returned if the child workflows are not redrivable. This happens when the child workflow executions have completed successfully.