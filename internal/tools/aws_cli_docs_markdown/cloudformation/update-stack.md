# update-stackÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# update-stack

## Description

Updates a stack as specified in the template. After the call completes successfully, the stack update starts. You can check the status of the stack through the  DescribeStacks action.

To get a copy of the template for an existing stack, you can use the  GetTemplate action.

For more information about updating a stack and monitoring the progress of the update, see [Managing Amazon Web Services resources as a single unit with CloudFormation stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html) in the *CloudFormation User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/UpdateStack)

## Synopsis

```
update-stack
--stack-name <value>
[--template-body <value>]
[--template-url <value>]
[--use-previous-template | --no-use-previous-template]
[--stack-policy-during-update-body <value>]
[--stack-policy-during-update-url <value>]
[--parameters <value>]
[--capabilities <value>]
[--resource-types <value>]
[--role-arn <value>]
[--rollback-configuration <value>]
[--stack-policy-body <value>]
[--stack-policy-url <value>]
[--notification-arns <value>]
[--tags <value>]
[--disable-rollback | --no-disable-rollback]
[--client-request-token <value>]
[--retain-except-on-create | --no-retain-except-on-create]
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

`--stack-name` (string)

The name or unique stack ID of the stack to update.

`--template-body` (string)

Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.

Conditional: You must specify only one of the following parameters: `TemplateBody` , `TemplateURL` , or set the `UsePreviousTemplate` to `true` .

`--template-url` (string)

The URL of a file containing the template body. The URL must point to a template thatâs located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with `https://` .

Conditional: You must specify only one of the following parameters: `TemplateBody` , `TemplateURL` , or set the `UsePreviousTemplate` to `true` .

`--use-previous-template` | `--no-use-previous-template` (boolean)

Reuse the existing template that is associated with the stack that you are updating.

Conditional: You must specify only one of the following parameters: `TemplateBody` , `TemplateURL` , or set the `UsePreviousTemplate` to `true` .

`--stack-policy-during-update-body` (string)

Structure containing the temporary overriding stack policy body. You can specify either the `StackPolicyDuringUpdateBody` or the `StackPolicyDuringUpdateURL` parameter, but not both.

If you want to update protected resources, specify a temporary overriding stack policy during this update. If you donât specify a stack policy, the current policy that is associated with the stack will be used.

`--stack-policy-during-update-url` (string)

Location of a file containing the temporary overriding stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same Region as the stack. The location for an Amazon S3 bucket must start with `https://` . You can specify either the `StackPolicyDuringUpdateBody` or the `StackPolicyDuringUpdateURL` parameter, but not both.

If you want to update protected resources, specify a temporary overriding stack policy during this update. If you donât specify a stack policy, the current policy that is associated with the stack will be used.

`--parameters` (list)

A list of `Parameter` structures that specify input parameters for the stack. For more information, see the [Parameter](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html) data type.

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

In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to update the stack.

- `CAPABILITY_IAM` and `CAPABILITY_NAMED_IAM`   Some stack templates might include resources that can affect permissions in your Amazon Web Services account, for example, by creating new IAM users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities. The following IAM resources require you to specify either the `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM` capability.
- If you have IAM resources, you can specify either capability.
- If you have IAM resources with custom names, you *must* specify `CAPABILITY_NAMED_IAM` .
- If you donât specify either of these capabilities, CloudFormation returns an `InsufficientCapabilities` error.

If your stack template contains these resources, we suggest that you review all permissions associated with them and edit their permissions if necessary.

- [AWS::IAM::AccessKey](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-accesskey.html)
- [AWS::IAM::Group](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-group.html)
- [AWS::IAM::InstanceProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html)
- [AWS::IAM::ManagedPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html)
- [AWS::IAM::Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html)
- [AWS::IAM::Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html)
- [AWS::IAM::User](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html)
- [AWS::IAM::UserToGroupAddition](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-usertogroupaddition.html)

For more information, see [Acknowledging IAM resources in CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities) .

- `CAPABILITY_AUTO_EXPAND`   Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually updating the stack. If your stack template contains one or more macros, and you choose to update a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the [AWS::Include](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-include.html) and [AWS::Serverless](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html) transforms, which are macros hosted by CloudFormation. If you want to update a stack from a stack template that contains macros *and* nested stacks, you must update the stack directly from the template using this capability.

### Warning

You should only update stacks directly from a stack template that contains macros if you know what processing the macro performs. Each macro relies on an underlying Lambda service function for processing stack templates. Be aware that the Lambda function owner can update the function operation without CloudFormation being notified.

For more information, see [Perform custom processing on CloudFormation templates with template macros](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html) .

### Note

Only one of the `Capabilities` and `ResourceType` parameters can be specified.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  CAPABILITY_IAM
  CAPABILITY_NAMED_IAM
  CAPABILITY_AUTO_EXPAND
```

`--resource-types` (list)

The template resource types that you have permissions to work with for this update stack action, such as `AWS::EC2::Instance` , `AWS::EC2::*` , or `Custom::MyCustomInstance` .

If the list of resource types doesnât include a resource that youâre updating, the stack update fails. By default, CloudFormation grants permissions to all resource types. IAM uses this parameter for CloudFormation-specific condition keys in IAM policies. For more information, see [Control access with Identity and Access Management](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html) .

### Note

Only one of the `Capabilities` and `ResourceType` parameters can be specified.

(string)

Syntax:

```
"string" "string" ...
```

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to update the stack. CloudFormation uses the roleâs credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users donât have permission to pass it. Ensure that the role grants least privilege.

If you donât specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that is generated from your user credentials.

`--rollback-configuration` (structure)

The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.

RollbackTriggers -> (list)

The triggers to monitor during stack creation or update actions.

By default, CloudFormation saves the rollback triggers specified for a stack and applies them to any subsequent update operations for the stack, unless you specify otherwise. If you do specify rollback triggers for this parameter, those triggers replace any list of triggers previously specified for the stack. This means:

- To use the rollback triggers previously specified for this stack, if any, donât specify this parameter.
- To specify new or updated rollback triggers, you must specify *all* the triggers that you want used for this stack, even triggers youâve specified before (for example, when creating the stack or during a previous stack update). Any triggers that you donât include in the updated list of triggers are no longer applied to the stack.
- To remove all currently specified triggers, specify an empty list for this parameter.

If a specified trigger is missing, the entire stack operation fails and is rolled back.

(structure)

A rollback trigger CloudFormation monitors during creation and updating of stacks. If any of the alarms you specify goes to ALARM state during the stack operation or within the specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.

Arn -> (string)

The Amazon Resource Name (ARN) of the rollback trigger.

If a specified trigger is missing, the entire stack operation fails and is rolled back.

Type -> (string)

The resource type of the rollback trigger. Specify either [AWS::CloudWatch::Alarm](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html) or [AWS::CloudWatch::CompositeAlarm](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html) resource types.

MonitoringTimeInMinutes -> (integer)

The amount of time, in minutes, during which CloudFormation should monitor all the rollback triggers after the stack creation or update operation deploys all necessary resources.

The default is 0 minutes.

If you specify a monitoring period but donât specify any rollback triggers, CloudFormation still waits the specified period of time before cleaning up old resources after update operations. You can use this monitoring period to perform any manual stack validation desired, and manually cancel the stack creation or update (using [CancelUpdateStack](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html) , for example) as necessary.

If you specify 0 for this parameter, CloudFormation still monitors the specified rollback triggers during stack creation and update operations. Then, for update operations, it begins disposing of old resources immediately once the operation completes.

Shorthand Syntax:

```
RollbackTriggers=[{Arn=string,Type=string},{Arn=string,Type=string}],MonitoringTimeInMinutes=integer
```

JSON Syntax:

```
{
  "RollbackTriggers": [
    {
      "Arn": "string",
      "Type": "string"
    }
    ...
  ],
  "MonitoringTimeInMinutes": integer
}
```

`--stack-policy-body` (string)

Structure containing a new stack policy body. You can specify either the `StackPolicyBody` or the `StackPolicyURL` parameter, but not both.

You might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you donât specify a stack policy, the current policy that is associated with the stack is unchanged.

`--stack-policy-url` (string)

Location of a file containing the updated stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same Region as the stack. The location for an Amazon S3 bucket must start with `https://` . You can specify either the `StackPolicyBody` or the `StackPolicyURL` parameter, but not both.

You might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you donât specify a stack policy, the current policy that is associated with the stack is unchanged.

`--notification-arns` (list)

Amazon Simple Notification Service topic Amazon Resource Names (ARNs) that CloudFormation associates with the stack. Specify an empty list to remove all notification topics.

(string)

Syntax:

```
"string" "string" ...
```

`--tags` (list)

Key-value pairs to associate with this stack. CloudFormation also propagates these tags to supported resources in the stack. You can specify a maximum number of 50 tags.

If you donât specify this parameter, CloudFormation doesnât modify the stackâs tags. If you specify an empty value, CloudFormation removes all associated tags.

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

`--disable-rollback` | `--no-disable-rollback` (boolean)

Preserve the state of previously provisioned resources when an operation fails.

Default: `False`

`--client-request-token` (string)

A unique identifier for this `UpdateStack` request. Specify this token if you plan to retry requests so that CloudFormation knows that youâre not attempting to update a stack with the same name. You might retry `UpdateStack` requests to ensure that CloudFormation successfully received them.

All events triggered by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a `CreateStack` operation with the token `token1` , then all the `StackEvents` generated by that operation will have `ClientRequestToken` set as `token1` .

In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format *Console-StackOperation-ID* , which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: `Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002` .

`--retain-except-on-create` | `--no-retain-except-on-create` (boolean)

When set to `true` , newly created resources are deleted when the operation rolls back. This includes newly created resources marked with a deletion policy of `Retain` .

Default: `false`

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

**To update AWS CloudFormation stacks**

The following `update-stack` command updates the template and input parameters for the `mystack` stack:

```
aws cloudformation update-stack --stack-name mystack --template-url https://s3.amazonaws.com/sample/updated.template --parameters ParameterKey=KeyPairName,ParameterValue=SampleKeyPair ParameterKey=SubnetIDs,ParameterValue=SampleSubnetID1\\,SampleSubnetID2
```

The following `update-stack` command updates just the `SubnetIDs` parameter value for the `mystack` stack. If you
donât specify a parameter value, the default value that is specified in the template is used:

```
aws cloudformation update-stack --stack-name mystack --template-url https://s3.amazonaws.com/sample/updated.template --parameters ParameterKey=KeyPairName,UsePreviousValue=true ParameterKey=SubnetIDs,ParameterValue=SampleSubnetID1\\,UpdatedSampleSubnetID2
```

The following `update-stack` command adds two stack notification topics to the `mystack` stack:

```
aws cloudformation update-stack --stack-name mystack --use-previous-template --notification-arns "arn:aws:sns:use-east-1:123456789012:mytopic1" "arn:aws:sns:us-east-1:123456789012:mytopic2"
```

For more information, see [AWS CloudFormation stack updates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html) in the *AWS CloudFormation User Guide*.

## Output

StackId -> (string)

Unique identifier of the stack.