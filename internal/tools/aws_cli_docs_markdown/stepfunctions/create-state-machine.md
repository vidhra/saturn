# create-state-machineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/create-state-machine.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/create-state-machine.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [stepfunctions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/index.html#cli-aws-stepfunctions) ]

# create-state-machine

## Description

Creates a state machine. A state machine consists of a collection of states that can do work (`Task` states), determine to which states to transition next (`Choice` states), stop an execution with an error (`Fail` states), and so on. State machines are specified using a JSON-based, structured language. For more information, see [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html) in the Step Functions User Guide.

If you set the `publish` parameter of this API action to `true` , it publishes version `1` as the first revision of the state machine.

For additional control over security, you can encrypt your data using a **customer-managed key** for Step Functions state machines. You can configure a symmetric KMS key and data key reuse period when creating or updating a **State Machine** . The execution history and state machine definition will be encrypted with the key applied to the State Machine.

### Note

This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.

### Note

`CreateStateMachine` is an idempotent API. Subsequent requests wonât create a duplicate resource if it was already created. `CreateStateMachine` âs idempotency check is based on the state machine `name` , `definition` , `type` , `LoggingConfiguration` , `TracingConfiguration` , and `EncryptionConfiguration` The check is also based on the `publish` and `versionDescription` parameters. If a following request has a different `roleArn` or `tags` , Step Functions will ignore these differences and treat it as an idempotent request of the previous. In this case, `roleArn` and `tags` will not be updated, even if they are different.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/CreateStateMachine)

## Synopsis

```
create-state-machine
--name <value>
--definition <value>
--role-arn <value>
[--type <value>]
[--logging-configuration <value>]
[--tags <value>]
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

`--name` (string)

The name of the state machine.

A name must *not* contain:

- white space
- brackets `< > { } [ ]`
- wildcard characters `? *`
- special characters `" # % \ ^ | ~ ` $ & , ; : /`
- control characters (`U+0000-001F` , `U+007F-009F` )

To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.

`--definition` (string)

The Amazon States Language definition of the state machine. See [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html) .

`--role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role to use for this state machine.

`--type` (string)

Determines whether a Standard or Express state machine is created. The default is `STANDARD` . You cannot update the `type` of a state machine once it has been created.

Possible values:

- `STANDARD`
- `EXPRESS`

`--logging-configuration` (structure)

Defines what execution history events are logged and where they are logged.

### Note

By default, the `level` is set to `OFF` . For more information see [Log Levels](https://docs.aws.amazon.com/step-functions/latest/dg/cloudwatch-log-level.html) in the Step Functions User Guide.

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

`--tags` (list)

Tags to be added when creating a state machine.

An array of key-value pairs. For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *Amazon Web Services Billing and Cost Management User Guide* , and [Controlling Access Using IAM Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html) .

Tags may only contain Unicode letters, digits, white space, or these symbols: `_ . : / = + - @` .

(structure)

Tags are key-value pairs that can be associated with Step Functions state machines and activities.

An array of key-value pairs. For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *Amazon Web Services Billing and Cost Management User Guide* , and [Controlling Access Using IAM Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html) .

Tags may only contain Unicode letters, digits, white space, or these symbols: `_ . : / = + - @` .

key -> (string)

The key of a tag.

value -> (string)

The value of a tag.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
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

Set to `true` to publish the first version of the state machine during creation. The default is `false` .

`--version-description` (string)

Sets description about the state machine version. You can only set the description if the `publish` parameter is set to `true` . Otherwise, if you set `versionDescription` , but `publish` to `false` , this API action throws `ValidationException` .

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

stateMachineArn -> (string)

The Amazon Resource Name (ARN) that identifies the created state machine.

creationDate -> (timestamp)

The date the state machine is created.

stateMachineVersionArn -> (string)

The Amazon Resource Name (ARN) that identifies the created state machine version. If you do not set the `publish` parameter to `true` , this field returns null value.