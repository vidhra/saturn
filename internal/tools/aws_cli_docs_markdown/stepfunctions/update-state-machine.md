# update-state-machineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/update-state-machine.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/update-state-machine.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [stepfunctions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/index.html#cli-aws-stepfunctions) ]

# update-state-machine

## Description

Updates an existing state machine by modifying its `definition` , `roleArn` , `loggingConfiguration` , or `EncryptionConfiguration` . Running executions will continue to use the previous `definition` and `roleArn` . You must include at least one of `definition` or `roleArn` or you will receive a `MissingRequiredParameter` error.

A qualified state machine ARN refers to a *Distributed Map state* defined within a state machine. For example, the qualified state machine ARN `arn:partition:states:region:account-id:stateMachine:stateMachineName/mapStateLabel` refers to a *Distributed Map state* with a label `mapStateLabel` in the state machine named `stateMachineName` .

A qualified state machine ARN can either refer to a *Distributed Map state* defined within a state machine, a version ARN, or an alias ARN.

The following are some examples of qualified and unqualified state machine ARNs:

- The following qualified state machine ARN refers to a *Distributed Map state* with a label `mapStateLabel` in a state machine named `myStateMachine` .  `arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel`

### Note

If you provide a qualified state machine ARN that refers to a *Distributed Map state* , the request fails with `ValidationException` .

- The following qualified state machine ARN refers to an alias named `PROD` .  `arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine:PROD>`

### Note

If you provide a qualified state machine ARN that refers to a version ARN or an alias ARN, the request starts execution for that version or alias.

- The following unqualified state machine ARN refers to a state machine named `myStateMachine` .  `arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine>`

After you update your state machine, you can set the `publish` parameter to `true` in the same action to publish a new [version](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html) . This way, you can opt-in to strict versioning of your state machine.

### Note

Step Functions assigns monotonically increasing integers for state machine versions, starting at version number 1.

### Note

All `StartExecution` calls within a few seconds use the updated `definition` and `roleArn` . Executions started immediately after you call `UpdateStateMachine` may use the previous state machine `definition` and `roleArn` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/UpdateStateMachine)

## Synopsis

```
update-state-machine
--state-machine-arn <value>
[--definition <value>]
[--role-arn <value>]
[--logging-configuration <value>]
[--tracing-configuration <value>]
[--publish | --no-publish]
[--version-description <value>]
[--encryption-configuration <value>]
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

The Amazon Resource Name (ARN) of the state machine.

`--definition` (string)

The Amazon States Language definition of the state machine. See [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html) .

`--role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role of the state machine.

`--logging-configuration` (structure)

Use the `LoggingConfiguration` data type to set CloudWatch Logs options.

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

JSON Syntax:

```
{
  "level": "ALL"|"ERROR"|"FATAL"|"OFF",
  "includeExecutionData": true|false,
  "destinations": [
    {
      "cloudWatchLogsLogGroup": {
        "logGroupArn": "string"
      }
    }
    ...
  ]
}
```

`--tracing-configuration` (structure)

Selects whether X-Ray tracing is enabled.

enabled -> (boolean)

When set to `true` , X-Ray tracing is enabled.

Shorthand Syntax:

```
enabled=boolean
```

JSON Syntax:

```
{
  "enabled": true|false
}
```

`--publish` | `--no-publish` (boolean)

Specifies whether the state machine version is published. The default is `false` . To publish a version after updating the state machine, set `publish` to `true` .

`--version-description` (string)

An optional description of the state machine version to publish.

You can only specify the `versionDescription` parameter if youâve set `publish` to `true` .

`--encryption-configuration` (structure)

Settings to configure server-side encryption.

kmsKeyId -> (string)

An alias, alias ARN, key ID, or key ARN of a symmetric encryption KMS key to encrypt data. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.

kmsDataKeyReusePeriodSeconds -> (integer)

Maximum duration that Step Functions will reuse data keys. When the period expires, Step Functions will call `GenerateDataKey` . Only applies to customer managed keys.

type -> (string)

Encryption type

Shorthand Syntax:

```
kmsKeyId=string,kmsDataKeyReusePeriodSeconds=integer,type=string
```

JSON Syntax:

```
{
  "kmsKeyId": "string",
  "kmsDataKeyReusePeriodSeconds": integer,
  "type": "AWS_OWNED_KEY"|"CUSTOMER_MANAGED_KMS_KEY"
}
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

## Output

updateDate -> (timestamp)

The date and time the state machine was updated.

revisionId -> (string)

The revision identifier for the updated state machine.

stateMachineVersionArn -> (string)

The Amazon Resource Name (ARN) of the published state machine version.

If the `publish` parameter isnât set to `true` , this field returns null.