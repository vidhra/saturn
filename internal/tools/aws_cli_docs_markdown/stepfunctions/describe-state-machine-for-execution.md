# describe-state-machine-for-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-state-machine-for-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-state-machine-for-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [stepfunctions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/index.html#cli-aws-stepfunctions) ]

# describe-state-machine-for-execution

## Description

Provides information about a state machineâs definition, its execution role ARN, and configuration. If a Map Run dispatched the execution, this action returns the Map Run Amazon Resource Name (ARN) in the response. The state machine returned is the state machine associated with the Map Run.

### Note

This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.

This API action is not supported by `EXPRESS` state machines.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/DescribeStateMachineForExecution)

## Synopsis

```
describe-state-machine-for-execution
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

The Amazon Resource Name (ARN) of the execution you want state machine information for.

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

stateMachineArn -> (string)

The Amazon Resource Name (ARN) of the state machine associated with the execution.

name -> (string)

The name of the state machine associated with the execution.

definition -> (string)

The Amazon States Language definition of the state machine. See [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html) .

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role of the State Machine for the execution.

updateDate -> (timestamp)

The date and time the state machine associated with an execution was updated. For a newly created state machine, this is the creation date.

loggingConfiguration -> (structure)

The `LoggingConfiguration` data type is used to set CloudWatch Logs options.

level -> (string)

Defines which category of execution history events are logged.

includeExecutionData -> (boolean)

Determines whether execution data is included in your log. When set to `false` , data is excluded.

destinations -> (list)

An array of objects that describes where your execution history events will be logged. Limited to size 1. Required, if your log level is not set to `OFF` .

(structure)

cloudWatchLogsLogGroup -> (structure)

An object describing a CloudWatch log group. For more information, see [AWS::Logs::LogGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html) in the CloudFormation User Guide.

logGroupArn -> (string)

The ARN of the the CloudWatch log group to which you want your logs emitted to. The ARN must end with `:*`

tracingConfiguration -> (structure)

Selects whether X-Ray tracing is enabled.

enabled -> (boolean)

When set to `true` , X-Ray tracing is enabled.

mapRunArn -> (string)

The Amazon Resource Name (ARN) of the Map Run that started the child workflow execution. This field is returned only if the `executionArn` is a child workflow execution that was started by a Distributed Map state.

label -> (string)

A user-defined or an auto-generated string that identifies a `Map` state. This ï¬eld is returned only if the `executionArn` is a child workflow execution that was started by a Distributed Map state.

revisionId -> (string)

The revision identifier for the state machine. The first revision ID when you create the state machine is null.

Use the state machine `revisionId` parameter to compare the revision of a state machine with the configuration of the state machine used for executions without performing a diff of the properties, such as `definition` and `roleArn` .

encryptionConfiguration -> (structure)

Settings to configure server-side encryption.

kmsKeyId -> (string)

An alias, alias ARN, key ID, or key ARN of a symmetric encryption KMS key to encrypt data. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.

kmsDataKeyReusePeriodSeconds -> (integer)

Maximum duration that Step Functions will reuse data keys. When the period expires, Step Functions will call `GenerateDataKey` . Only applies to customer managed keys.

type -> (string)

Encryption type

variableReferences -> (map)

A map of **state name** to a list of variables referenced by that state. States that do not use variable references will not be shown in the response.

key -> (string)

value -> (list)

(string)