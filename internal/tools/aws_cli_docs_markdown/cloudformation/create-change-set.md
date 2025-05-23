# create-change-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-change-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-change-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# create-change-set

## Description

Creates a list of changes that will be applied to a stack so that you can review the changes before executing them. You can create a change set for a stack that doesnât exist or an existing stack. If you create a change set for a stack that doesnât exist, the change set shows all of the resources that CloudFormation will create. If you create a change set for an existing stack, CloudFormation compares the stackâs information with the information that you submit in the change set and lists the differences. Use change sets to understand which resources CloudFormation will create or change, and how it will change resources in an existing stack, before you create or update a stack.

To create a change set for a stack that doesnât exist, for the `ChangeSetType` parameter, specify `CREATE` . To create a change set for an existing stack, specify `UPDATE` for the `ChangeSetType` parameter. To create a change set for an import operation, specify `IMPORT` for the `ChangeSetType` parameter. After the `CreateChangeSet` call successfully completes, CloudFormation starts creating the change set. To check the status of the change set or to review it, use the  DescribeChangeSet action.

When you are satisfied with the changes the change set will make, execute the change set by using the  ExecuteChangeSet action. CloudFormation doesnât make changes until you execute the change set.

To create a change set for the entire stack hierarchy, set `IncludeNestedStacks` to `True` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet)

## Synopsis

```
create-change-set
--stack-name <value>
[--template-body <value>]
[--template-url <value>]
[--use-previous-template | --no-use-previous-template]
[--parameters <value>]
[--capabilities <value>]
[--resource-types <value>]
[--role-arn <value>]
[--rollback-configuration <value>]
[--notification-arns <value>]
[--tags <value>]
--change-set-name <value>
[--client-token <value>]
[--description <value>]
[--change-set-type <value>]
[--resources-to-import <value>]
[--include-nested-stacks | --no-include-nested-stacks]
[--on-stack-failure <value>]
[--import-existing-resources | --no-import-existing-resources]
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

The name or the unique ID of the stack for which you are creating a change set. CloudFormation generates the change set by comparing this stackâs information with the information that you submit, such as a modified template or different parameter input values.

`--template-body` (string)

A structure that contains the body of the revised template, with a minimum length of 1 byte and a maximum length of 51,200 bytes. CloudFormation generates the change set by comparing this template with the template of the stack that you specified.

Conditional: You must specify only `TemplateBody` or `TemplateURL` .

`--template-url` (string)

The URL of the file that contains the revised template. The URL must point to a template (max size: 1 MB) thatâs located in an Amazon S3 bucket or a Systems Manager document. CloudFormation generates the change set by comparing this template with the stack that you specified. The location for an Amazon S3 bucket must start with `https://` .

Conditional: You must specify only `TemplateBody` or `TemplateURL` .

`--use-previous-template` | `--no-use-previous-template` (boolean)

Whether to reuse the template thatâs associated with the stack to create the change set.

`--parameters` (list)

A list of `Parameter` structures that specify input parameters for the change set. For more information, see the  Parameter data type.

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

In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to create the stack.

- `CAPABILITY_IAM` and `CAPABILITY_NAMED_IAM`   Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new IAM users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities. The following IAM resources require you to specify either the `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM` capability.
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

- `CAPABILITY_AUTO_EXPAND`   Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually creating the stack. If your stack template contains one or more macros, and you choose to create a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the [AWS::Include](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-include.html) and [AWS::Serverless](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html) transforms, which are macros hosted by CloudFormation.

### Note

This capacity doesnât apply to creating change sets, and specifying it when creating change sets has no effect. If you want to create a stack from a stack template that contains macros *and* nested stacks, you must create or update the stack directly from the template using the  CreateStack or  UpdateStack action, and specifying this capability.

For more information about macros, see [Perform custom processing on CloudFormation templates with template macros](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html) .

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

The template resource types that you have permissions to work with if you execute this change set, such as `AWS::EC2::Instance` , `AWS::EC2::*` , or `Custom::MyCustomInstance` .

If the list of resource types doesnât include a resource type that youâre updating, the stack update fails. By default, CloudFormation grants permissions to all resource types. IAM uses this parameter for condition keys in IAM policies for CloudFormation. For more information, see [Control access with Identity and Access Management](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html) in the *CloudFormation User Guide* .

### Note

Only one of the `Capabilities` and `ResourceType` parameters can be specified.

(string)

Syntax:

```
"string" "string" ...
```

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes when executing the change set. CloudFormation uses the roleâs credentials to make calls on your behalf. CloudFormation uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users donât have permission to pass it. Ensure that the role grants least permission.

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

`--notification-arns` (list)

The Amazon Resource Names (ARNs) of Amazon SNS topics that CloudFormation associates with the stack. To remove all associated notification topics, specify an empty list.

(string)

Syntax:

```
"string" "string" ...
```

`--tags` (list)

Key-value pairs to associate with this stack. CloudFormation also propagates these tags to resources in the stack. You can specify a maximum of 50 tags.

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

`--change-set-name` (string)

The name of the change set. The name must be unique among all change sets that are associated with the specified stack.

A change set name can contain only alphanumeric, case sensitive characters, and hyphens. It must start with an alphabetical character and canât exceed 128 characters.

`--client-token` (string)

A unique identifier for this `CreateChangeSet` request. Specify this token if you plan to retry requests so that CloudFormation knows that youâre not attempting to create another change set with the same name. You might retry `CreateChangeSet` requests to ensure that CloudFormation successfully received them.

`--description` (string)

A description to help you identify this change set.

`--change-set-type` (string)

The type of change set operation. To create a change set for a new stack, specify `CREATE` . To create a change set for an existing stack, specify `UPDATE` . To create a change set for an import operation, specify `IMPORT` .

If you create a change set for a new stack, CloudFormation creates a stack with a unique stack ID, but no template or resources. The stack will be in the `REVIEW_IN_PROGRESS` state until you execute the change set.

By default, CloudFormation specifies `UPDATE` . You canât use the `UPDATE` type to create a change set for a new stack or the `CREATE` type to create a change set for an existing stack.

Possible values:

- `CREATE`
- `UPDATE`
- `IMPORT`

`--resources-to-import` (list)

The resources to import into your stack.

(structure)

Describes the target resource of an import operation.

ResourceType -> (string)

The type of resource to import into your stack, such as `AWS::S3::Bucket` . For a list of supported resource types, see [Resource type support for imports and drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html) in the *CloudFormation User Guide* .

LogicalResourceId -> (string)

The logical ID of the target resource as specified in the template.

ResourceIdentifier -> (map)

A key-value pair that identifies the target resource. The key is an identifier property (for example, `BucketName` for `AWS::S3::Bucket` resources) and the value is the actual property value (for example, `MyS3Bucket` ).

key -> (string)

value -> (string)

Shorthand Syntax:

```
ResourceType=string,LogicalResourceId=string,ResourceIdentifier={KeyName1=string,KeyName2=string} ...
```

JSON Syntax:

```
[
  {
    "ResourceType": "string",
    "LogicalResourceId": "string",
    "ResourceIdentifier": {"string": "string"
      ...}
  }
  ...
]
```

`--include-nested-stacks` | `--no-include-nested-stacks` (boolean)

Creates a change set for the all nested stacks specified in the template. The default behavior of this action is set to `False` . To include nested sets in a change set, specify `True` .

`--on-stack-failure` (string)

Determines what action will be taken if stack creation fails. If this parameter is specified, the `DisableRollback` parameter to the [ExecuteChangeSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html) API operation must not be specified. This must be one of these values:

- `DELETE` - Deletes the change set if the stack creation fails. This is only valid when the `ChangeSetType` parameter is set to `CREATE` . If the deletion of the stack fails, the status of the stack is `DELETE_FAILED` .
- `DO_NOTHING` - if the stack creation fails, do nothing. This is equivalent to specifying `true` for the `DisableRollback` parameter to the [ExecuteChangeSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html) API operation.
- `ROLLBACK` - if the stack creation fails, roll back the stack. This is equivalent to specifying `false` for the `DisableRollback` parameter to the [ExecuteChangeSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html) API operation.

For nested stacks, when the `OnStackFailure` parameter is set to `DELETE` for the change set for the parent stack, any failure in a child stack will cause the parent stack creation to fail and all stacks to be deleted.

Possible values:

- `DO_NOTHING`
- `ROLLBACK`
- `DELETE`

`--import-existing-resources` | `--no-import-existing-resources` (boolean)

Indicates if the change set imports resources that already exist.

### Note

This parameter can only import resources that have custom names in templates. For more information, see [name type](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html) in the *CloudFormation User Guide* . To import resources that do not accept custom names, such as EC2 instances, use the resource import feature instead. For more information, see [Import Amazon Web Services resources into a CloudFormation stack with a resource import](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import.html) in the *CloudFormation User Guide* .

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

**To create a change set**

The following `create-change-set` example creates a change set with the `CAPABILITY_IAM` capability. The file `template.yaml` is an AWS CloudFormation template in the current folder that defines a stack that includes IAM resources.

```
aws cloudformation create-change-set \
    --stack-name my-application \
    --change-set-name my-change-set \
    --template-body file://template.yaml \
    --capabilities CAPABILITY_IAM
```

Output:

```
{
    "Id": "arn:aws:cloudformation:us-west-2:123456789012:changeSet/my-change-set/bc9555ba-a949-xmpl-bfb8-f41d04ec5784",
    "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-application/d0a825a0-e4cd-xmpl-b9fb-061c69e99204"
}
```

## Output

Id -> (string)

The Amazon Resource Name (ARN) of the change set.

StackId -> (string)

The unique ID of the stack.