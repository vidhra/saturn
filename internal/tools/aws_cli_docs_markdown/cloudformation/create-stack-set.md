# create-stack-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# create-stack-set

## Description

Creates a stack set.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateStackSet)

## Synopsis

```
create-stack-set
--stack-set-name <value>
[--description <value>]
[--template-body <value>]
[--template-url <value>]
[--stack-id <value>]
[--parameters <value>]
[--capabilities <value>]
[--tags <value>]
[--administration-role-arn <value>]
[--execution-role-name <value>]
[--permission-model <value>]
[--auto-deployment <value>]
[--call-as <value>]
[--client-request-token <value>]
[--managed-execution <value>]
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

`--stack-set-name` (string)

The name to associate with the stack set. The name must be unique in the Region where you create your stack set.

### Note

A stack name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and canât be longer than 128 characters.

`--description` (string)

A description of the stack set. You can use the description to identify the stack setâs purpose or other important information.

`--template-body` (string)

The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.

Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.

`--template-url` (string)

The URL of a file that contains the template body. The URL must point to a template (maximum size: 1 MB) thatâs located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with `https://` .

Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.

`--stack-id` (string)

The stack ID you are importing into a new stack set. Specify the Amazon Resource Name (ARN) of the stack.

`--parameters` (list)

The input parameters for the stack set template.

(structure)

The Parameter data type.

ParameterKey -> (string)

The key associated with the parameter. If you donât specify a key and value for a particular parameter, CloudFormation uses the default value thatâs specified in your template.

ParameterValue -> (string)

The input value associated with the parameter.

UsePreviousValue -> (boolean)

During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify `true` , do not specify a parameter value.

ResolvedValue -> (string)

Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for Systems Manager parameter types in the template. For more information, see [Specify existing resources at runtime with CloudFormation-supplied parameter types](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-supplied-parameter-types.html) in the *CloudFormation User Guide* .

Shorthand Syntax:

```
ParameterKey=string,ParameterValue=string,UsePreviousValue=boolean,ResolvedValue=string ...
```

JSON Syntax:

```
[
  {
    "ParameterKey": "string",
    "ParameterValue": "string",
    "UsePreviousValue": true|false,
    "ResolvedValue": "string"
  }
  ...
]
```

`--capabilities` (list)

In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for CloudFormation to create the stack set and related stack instances.

- `CAPABILITY_IAM` and `CAPABILITY_NAMED_IAM`   Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new IAM users. For those stack sets, you must explicitly acknowledge this by specifying one of these capabilities. The following IAM resources require you to specify either the `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM` capability.
- If you have IAM resources, you can specify either capability.
- If you have IAM resources with custom names, you *must* specify `CAPABILITY_NAMED_IAM` .
- If you donât specify either of these capabilities, CloudFormation returns an `InsufficientCapabilities` error.

If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.

- [AWS::IAM::AccessKey](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-accesskey.html)
- [AWS::IAM::Group](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-group.html)
- [AWS::IAM::InstanceProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html)
- [AWS::IAM::Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html)
- [AWS::IAM::Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html)
- [AWS::IAM::User](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html)
- [AWS::IAM::UserToGroupAddition](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-usertogroupaddition.html)

For more information, see [Acknowledging IAM resources in CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities) .

- `CAPABILITY_AUTO_EXPAND`   Some templates reference macros. If your stack set template references one or more macros, you must create the stack set directly from the processed template, without first reviewing the resulting changes in a change set. To create the stack set directly, you must acknowledge this capability. For more information, see [Perform custom processing on CloudFormation templates with template macros](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html) .

### Warning

Stack sets with service-managed permissions donât currently support the use of macros in templates. (This includes the [AWS::Include](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-include.html) and [AWS::Serverless](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html) transforms, which are macros hosted by CloudFormation.) Even if you specify this capability for a stack set with service-managed permissions, if you reference a macro in your template the stack set operation will fail.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  CAPABILITY_IAM
  CAPABILITY_NAMED_IAM
  CAPABILITY_AUTO_EXPAND
```

`--tags` (list)

The key-value pairs to associate with this stack set and the stacks created from it. CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.

If you specify tags as part of a `CreateStackSet` action, CloudFormation checks to see if you have the required IAM permission to tag resources. If you donât, the entire `CreateStackSet` action fails with an `access denied` error, and the stack set is not created.

(structure)

The Tag type enables you to specify a key-value pair that can be used to store information about an CloudFormation stack.

Key -> (string)

*Required* . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services have the reserved prefix: `aws:` .

Value -> (string)

*Required* . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--administration-role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role to use to create this stack set.

Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see [Grant self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html) in the *CloudFormation User Guide* .

Valid only if the permissions model is `SELF_MANAGED` .

`--execution-role-name` (string)

The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, CloudFormation uses the `AWSCloudFormationStackSetExecutionRole` role for the stack set operation.

Specify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their stack sets.

Valid only if the permissions model is `SELF_MANAGED` .

`--permission-model` (string)

Describes how the IAM roles required for stack set operations are created. By default, `SELF-MANAGED` is specified.

- With `self-managed` permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see [Grant self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html) .
- With `service-managed` permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see [Activate trusted access for stack sets with Organizations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-activate-trusted-access.html) .

Possible values:

- `SERVICE_MANAGED`
- `SELF_MANAGED`

`--auto-deployment` (structure)

Describes whether StackSets automatically deploys to Organizations accounts that are added to the target organization or organizational unit (OU). For more information, see [Manage automatic deployments for CloudFormation StackSets that use service-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-manage-auto-deployment.html) in the *CloudFormation User Guide* .

Required if the permissions model is `SERVICE_MANAGED` . (Not used with self-managed permissions.)

Enabled -> (boolean)

If set to `true` , StackSets automatically deploys additional stack instances to Organizations accounts that are added to a target organization or organizational unit (OU) in the specified Regions. If an account is removed from a target organization or OU, StackSets deletes stack instances from the account in the specified Regions.

RetainStacksOnAccountRemoval -> (boolean)

If set to `true` , stack resources are retained when an account is removed from a target organization or OU. If set to `false` , stack resources are deleted. Specify only if `Enabled` is set to `True` .

Shorthand Syntax:

```
Enabled=boolean,RetainStacksOnAccountRemoval=boolean
```

JSON Syntax:

```
{
  "Enabled": true|false,
  "RetainStacksOnAccountRemoval": true|false
}
```

`--call-as` (string)

Specifies whether you are acting as an account administrator in the organizationâs management account or as a delegated administrator in a member account.

By default, `SELF` is specified. Use `SELF` for stack sets with self-managed permissions.

- To create a stack set with service-managed permissions while signed in to the management account, specify `SELF` .
- To create a stack set with service-managed permissions while signed in to a delegated administrator account, specify `DELEGATED_ADMIN` . Your Amazon Web Services account must be registered as a delegated admin in the management account. For more information, see [Register a delegated administrator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html) in the *CloudFormation User Guide* .

Stack sets with service-managed permissions are created in the management account, including stack sets that are created by delegated administrators.

Valid only if the permissions model is `SERVICE_MANAGED` .

Possible values:

- `SELF`
- `DELEGATED_ADMIN`

`--client-request-token` (string)

A unique identifier for this `CreateStackSet` request. Specify this token if you plan to retry requests so that CloudFormation knows that youâre not attempting to create another stack set with the same name. You might retry `CreateStackSet` requests to ensure that CloudFormation successfully received them.

If you donât specify an operation ID, the SDK generates one automatically.

`--managed-execution` (structure)

Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.

Active -> (boolean)

When `true` , StackSets performs non-conflicting operations concurrently and queues conflicting operations. After conflicting operations finish, StackSets starts queued operations in request order.

### Note

If there are already running or queued operations, StackSets queues all incoming operations even if they are non-conflicting.

You canât modify your stack setâs execution configuration while there are running or queued operations for that stack set.

When `false` (default), StackSets performs one operation at a time in request order.

Shorthand Syntax:

```
Active=boolean
```

JSON Syntax:

```
{
  "Active": true|false
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a stack set**

The following `create-stack-set` example creates a stack set using the specified YAML file temlplate. `template.yaml` is an AWS CloudFormation template in the current folder that defines a stack.

```
aws cloudformation create-stack-set \
    --stack-set-name my-stack-set \
    --template-body file://template.yaml \
    --description "SNS topic"
```

Output:

```
{
    "StackSetId": "my-stack-set:8d0f160b-d157-xmpl-a8e6-c0ce8e5d8cc1"
}
```

To add stack instances to the stack set, use the `create-stack-instances` command.

## Output

StackSetId -> (string)

The ID of the stack set that youâre creating.