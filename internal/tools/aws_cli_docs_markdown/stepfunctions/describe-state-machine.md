# describe-state-machineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-state-machine.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-state-machine.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [stepfunctions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/index.html#cli-aws-stepfunctions) ]

# describe-state-machine

## Description

Provides information about a state machineâs definition, its IAM role Amazon Resource Name (ARN), and configuration.

A qualified state machine ARN can either refer to a *Distributed Map state* defined within a state machine, a version ARN, or an alias ARN.

The following are some examples of qualified and unqualified state machine ARNs:

- The following qualified state machine ARN refers to a *Distributed Map state* with a label `mapStateLabel` in a state machine named `myStateMachine` .  `arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel`

### Note

If you provide a qualified state machine ARN that refers to a *Distributed Map state* , the request fails with `ValidationException` .

- The following qualified state machine ARN refers to an alias named `PROD` .  `arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine:PROD>`

### Note

If you provide a qualified state machine ARN that refers to a version ARN or an alias ARN, the request starts execution for that version or alias.

- The following unqualified state machine ARN refers to a state machine named `myStateMachine` .  `arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine>`

This API action returns the details for a state machine version if the `stateMachineArn` you specify is a state machine version ARN.

### Note

This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/DescribeStateMachine)

## Synopsis

```
describe-state-machine
--state-machine-arn <value>
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

The Amazon Resource Name (ARN) of the state machine for which you want the information.

If you specify a state machine version ARN, this API returns details about that version. The version ARN is a combination of state machine ARN and the version number separated by a colon (:). For example, `stateMachineARN:1` .

`--included-data` (string)

If your state machine definition is encrypted with a KMS key, callers must have `kms:Decrypt` permission to decrypt the definition. Alternatively, you can call the API with `includedData = METADATA_ONLY` to get a successful response without the encrypted definition.

### Note

When calling a labelled ARN for an encrypted state machine, the `includedData = METADATA_ONLY` parameter will not apply because Step Functions needs to decrypt the entire state machine definition to get the Distributed Map stateâs definition. In this case, the API caller needs to have `kms:Decrypt` permission.

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

The Amazon Resource Name (ARN) that identifies the state machine.

If you specified a state machine version ARN in your request, the API returns the version ARN. The version ARN is a combination of state machine ARN and the version number separated by a colon (:). For example, `stateMachineARN:1` .

name -> (string)

The name of the state machine.

A name must *not* contain:

- white space
- brackets `< > { } [ ]`
- wildcard characters `? *`
- special characters `" # % \ ^ | ~ ` $ & , ; : /`
- control characters (`U+0000-001F` , `U+007F-009F` )

To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.

status -> (string)

The current status of the state machine.

definition -> (string)

The Amazon States Language definition of the state machine. See [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html) .

If called with `includedData = METADATA_ONLY` , the returned definition will be `{}` .

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role used when creating this state machine. (The IAM role maintains security by granting Step Functions access to Amazon Web Services resources.)

type -> (string)

The `type` of the state machine (`STANDARD` or `EXPRESS` ).

creationDate -> (timestamp)

The date the state machine is created.

For a state machine version, `creationDate` is the date the version was created.

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

label -> (string)

A user-defined or an auto-generated string that identifies a `Map` state. This parameter is present only if the `stateMachineArn` specified in input is a qualified state machine ARN.

revisionId -> (string)

The revision identifier for the state machine.

Use the `revisionId` parameter to compare between versions of a state machine configuration used for executions without performing a diff of the properties, such as `definition` and `roleArn` .

description -> (string)

The description of the state machine version.

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