# start-sync-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/start-sync-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/start-sync-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [stepfunctions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/index.html#cli-aws-stepfunctions) ]

# start-sync-execution

## Description

Starts a Synchronous Express state machine execution. `StartSyncExecution` is not available for `STANDARD` workflows.

### Note

`StartSyncExecution` will return a `200 OK` response, even if your execution fails, because the status code in the API response doesnât reflect function errors. Error codes are reserved for errors that prevent your execution from running, such as permissions errors, limit errors, or issues with your state machine code and configuration.

### Note

This API action isnât logged in CloudTrail.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/StartSyncExecution)

## Synopsis

```
start-sync-execution
--state-machine-arn <value>
[--name <value>]
[--input <value>]
[--trace-header <value>]
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

`--state-machine-arn` (string)

The Amazon Resource Name (ARN) of the state machine to execute.

`--name` (string)

The name of the execution.

`--input` (string)

The string that contains the JSON input data for the execution, for example:

`"input": "{\"first_name\" : \"test\"}"`

### Note

If you donât include any JSON input data, you still must include the two braces, for example: `"input": "{}"`

Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.

`--trace-header` (string)

Passes the X-Ray trace header. The trace header can also be passed in the request payload.

`--included-data` (string)

If your state machine definition is encrypted with a KMS key, callers must have `kms:Decrypt` permission to decrypt the definition. Alternatively, you can call the API with `includedData = METADATA_ONLY` to get a successful response without the encrypted definition.

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

The Amazon Resource Name (ARN) that identifies the state machine.

name -> (string)

The name of the execution.

startDate -> (timestamp)

The date the execution is started.

stopDate -> (timestamp)

If the execution has already ended, the date the execution stopped.

status -> (string)

The current status of the execution.

error -> (string)

The error code of the failure.

cause -> (string)

A more detailed explanation of the cause of the failure.

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

billingDetails -> (structure)

An object that describes workflow billing details, including billed duration and memory use.

billedMemoryUsedInMB -> (long)

Billed memory consumption of your workflow, in MB.

billedDurationInMilliseconds -> (long)

Billed duration of your workflow, in milliseconds.