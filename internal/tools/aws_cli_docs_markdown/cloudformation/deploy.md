# deployÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/deploy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/deploy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# deploy

## Description

Deploys the specified AWS CloudFormation template by creating and then executing
a change set. The command terminates after AWS CloudFormation executes the
change set. If you want to view the change set before AWS CloudFormation
executes it, use the `--no-execute-changeset` flag.

To update a stack, specify the name of an existing stack. To create a new stack,
specify a new stack name.

## Synopsis

```
deploy
--template-file <value>
--stack-name <value>
[--s3-bucket <value>]
[--force-upload]
[--s3-prefix <value>]
[--kms-key-id <value>]
[--parameter-overrides <value> [<value>...]]
[--capabilities <value> [<value>...]]
[--no-execute-changeset]
[--disable-rollback | --no-disable-rollback]
[--role-arn <value>]
[--notification-arns <value> [<value>...]]
[--fail-on-empty-changeset | --no-fail-on-empty-changeset]
[--tags <value> [<value>...]]
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

`--template-file` (string)
The path where your AWS CloudFormation template is located.

`--stack-name` (string)
The name of the AWS CloudFormation stack youâre deploying to. If you specify an existing stack, the command updates the stack. If you specify a new stack, the command creates it.

`--s3-bucket` (string)
The name of the S3 bucket where this command uploads your CloudFormation template. This is required the deployments of templates sized greater than 51,200 bytes

`--force-upload` (boolean)
Indicates whether to override existing files in the S3 bucket. Specify this flag to upload artifacts even if they match existing artifacts in the S3 bucket.

`--s3-prefix` (string)
A prefix name that the command adds to the artifactsâ name when it uploads them to the S3 bucket. The prefix name is a path name (folder name) for the S3 bucket.

`--kms-key-id` (string)
The ID of an AWS KMS key that the command uses to encrypt artifacts that are at rest in the S3 bucket.

`--parameter-overrides` (string)
A list of parameter structures that specify input parameters for your stack template. If youâre updating a stack and you donât specify a parameter, the command uses the stackâs existing value. For new stacks, you must specify parameters that donât have a default value. Syntax: ParameterKey1=ParameterValue1 ParameterKey2=ParameterValue2 â¦ or JSON file (see Examples)

`--capabilities` (list)
A list of capabilities that you must specify before AWS Cloudformation can create certain stacks. Some stack templates might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge their capabilities by specifying this parameter. The only valid values are CAPABILITY_IAM and CAPABILITY_NAMED_IAM. If you have IAM resources, you can specify either capability. If you have IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM. If you donât specify this parameter, this action returns an InsufficientCapabilities error.(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  CAPABILITY_IAM
  CAPABILITY_NAMED_IAM
```

`--no-execute-changeset` (boolean)
Indicates whether to execute the change set. Specify this flag if you want to view your stack changes before executing the change set. The command creates an AWS CloudFormation change set and then exits without executing the change set. After you view the change set, execute it to implement your changes.

`--disable-rollback` | `--no-disable-rollback` (boolean)
Preserve the state of previously provisioned resources when the execute-change-set operation fails.

`--role-arn` (string)
The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes when executing the change set.

`--notification-arns` (list)
Amazon Simple Notification Service topic Amazon Resource Names (ARNs) that AWS CloudFormation associates with the stack.(string)

Syntax:

```
"string" "string" ...
```

`--fail-on-empty-changeset` | `--no-fail-on-empty-changeset` (boolean)
Specify if the CLI should return a non-zero exit code when there are no changes to be made to the stack. By default, a zero exit code is returned, and this is the same behavior that occurs when âno-fail-on-empty-changeset is specified. If âfail-on-empty-changeset is specified, then the CLI will return a non-zero exit code.

`--tags` (list)
A list of tags to associate with the stack that is created or updated. AWS CloudFormation also propagates these tags to resources in the stack if the resource supports it. Syntax: TagKey1=TagValue1 TagKey2=TagValue2 â¦(string)

Syntax:

```
"string" "string" ...
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

Following command deploys template named `template.json` to a stack named
`my-new-stack`:

```
aws cloudformation deploy --template-file /path_to_template/template.json --stack-name my-new-stack --parameter-overrides Key1=Value1 Key2=Value2 --tags Key1=Value1 Key2=Value2
```

or the same command using parameters from JSON file `parameters.json`:

```
aws cloudformation deploy --template-file /path_to_template/template.json --stack-name my-new-stack --parameter-overrides file://path_to_parameters/parameters.json --tags Key1=Value1 Key2=Value2
```

### Supported JSON syntax

Original format:

```
[
    "Key1=Value1",
    "Key2=Value2"
]
```

CloudFormation like format:

```
[
   {
        "ParameterKey": "Key1",
        "ParameterValue": "Value1"
    },
    {
        "ParameterKey": "Key2",
        "ParameterValue": "Value2"
    }
]
```

### Note

Only ParameterKey and ParameterValue are expected keys, command will throw an exception if receives unexpected keys (e.g. UsePreviousValue or ResolvedValue).

CodePipeline like format:

```
[
    "Parameters": {
        "Key1": "Value1",
        "Key2": "Value2"
    }
]
```