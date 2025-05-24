# update-stack-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# update-stack-set

## Description

Updates the stack set and associated stack instances in the specified accounts and Amazon Web Services Regions.

Even if the stack set operation created by updating the stack set fails (completely or partially, below or above a specified failure tolerance), the stack set is updated with your changes. Subsequent  CreateStackInstances calls on the specified stack set use the updated stack set.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/UpdateStackSet)

## Synopsis

```
update-stack-set
--stack-set-name <value>
[--description <value>]
[--template-body <value>]
[--template-url <value>]
[--use-previous-template | --no-use-previous-template]
[--parameters <value>]
[--capabilities <value>]
[--tags <value>]
[--operation-preferences <value>]
[--administration-role-arn <value>]
[--execution-role-name <value>]
[--deployment-targets <value>]
[--permission-model <value>]
[--auto-deployment <value>]
[--operation-id <value>]
[--accounts <value>]
[--regions <value>]
[--call-as <value>]
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

The name or unique ID of the stack set that you want to update.

`--description` (string)

A brief description of updates that you are making.

`--template-body` (string)

The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.

Conditional: You must specify only one of the following parameters: `TemplateBody` or `TemplateURL` âor set `UsePreviousTemplate` to true.

`--template-url` (string)

The URL of a file that contains the template body. The URL must point to a template (maximum size: 1 MB) that is located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with `https://` .

Conditional: You must specify only one of the following parameters: `TemplateBody` or `TemplateURL` âor set `UsePreviousTemplate` to true.

`--use-previous-template` | `--no-use-previous-template` (boolean)

Use the existing template thatâs associated with the stack set that youâre updating.

Conditional: You must specify only one of the following parameters: `TemplateBody` or `TemplateURL` âor set `UsePreviousTemplate` to true.

`--parameters` (list)

A list of input parameters for the stack set template.

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

In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to update the stack set and its associated stack instances.

- `CAPABILITY_IAM` and `CAPABILITY_NAMED_IAM`   Some stack templates might include resources that can affect permissions in your Amazon Web Services account, for example, by creating new IAM users. For those stacks sets, you must explicitly acknowledge this by specifying one of these capabilities. The following IAM resources require you to specify either the `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM` capability.
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

- `CAPABILITY_AUTO_EXPAND`   Some templates reference macros. If your stack set template references one or more macros, you must update the stack set directly from the processed template, without first reviewing the resulting changes in a change set. To update the stack set directly, you must acknowledge this capability. For more information, see [Perform custom processing on CloudFormation templates with template macros](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html) .

### Warning

Stack sets with service-managed permissions do not currently support the use of macros in templates. (This includes the [AWS::Include](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-include.html) and [AWS::Serverless](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html) transforms, which are macros hosted by CloudFormation.) Even if you specify this capability for a stack set with service-managed permissions, if you reference a macro in your template the stack set operation will fail.

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

The key-value pairs to associate with this stack set and the stacks created from it. CloudFormation also propagates these tags to supported resources that are created in the stacks. You can specify a maximum number of 50 tags.

If you specify tags for this parameter, those tags replace any list of tags that are currently associated with this stack set. This means:

- If you donât specify this parameter, CloudFormation doesnât modify the stackâs tags.
- If you specify *any* tags using this parameter, you must specify *all* the tags that you want associated with this stack set, even tags youâve specified before (for example, when creating the stack set or during a previous update of the stack set.). Any tags that you donât include in the updated list of tags are removed from the stack set, and therefore from the stacks and resources as well.
- If you specify an empty value, CloudFormation removes all currently associated tags.

If you specify new tags as part of an `UpdateStackSet` action, CloudFormation checks to see if you have the required IAM permission to tag resources. If you omit tags that are currently associated with the stack set from the list of tags you specify, CloudFormation assumes that you want to remove those tags from the stack set, and checks to see if you have permission to untag resources. If you donât have the necessary permission(s), the entire `UpdateStackSet` action fails with an `access denied` error, and the stack set is not updated.

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

`--operation-preferences` (structure)

Preferences for how CloudFormation performs this stack set operation.

RegionConcurrencyType -> (string)

The concurrency type of deploying StackSets operations in Regions, could be in parallel or one Region at a time.

RegionOrder -> (list)

The order of the Regions where you want to perform the stack operation.

(string)

FailureToleranceCount -> (integer)

The number of accounts, per Region, for which this operation can fail before CloudFormation stops the operation in that Region. If the operation is stopped in a Region, CloudFormation doesnât attempt the operation in any subsequent Regions.

Conditional: You must specify either `FailureToleranceCount` or `FailureTolerancePercentage` (but not both).

By default, `0` is specified.

FailureTolerancePercentage -> (integer)

The percentage of accounts, per Region, for which this stack operation can fail before CloudFormation stops the operation in that Region. If the operation is stopped in a Region, CloudFormation doesnât attempt the operation in any subsequent Regions.

When calculating the number of accounts based on the specified percentage, CloudFormation rounds *down* to the next whole number.

Conditional: You must specify either `FailureToleranceCount` or `FailureTolerancePercentage` , but not both.

By default, `0` is specified.

MaxConcurrentCount -> (integer)

The maximum number of accounts in which to perform this operation at one time. This can depend on the value of `FailureToleranceCount` depending on your `ConcurrencyMode` . `MaxConcurrentCount` is at most one more than the `FailureToleranceCount` if youâre using `STRICT_FAILURE_TOLERANCE` .

Note that this setting lets you specify the *maximum* for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.

Conditional: You must specify either `MaxConcurrentCount` or `MaxConcurrentPercentage` , but not both.

By default, `1` is specified.

MaxConcurrentPercentage -> (integer)

The maximum percentage of accounts in which to perform this operation at one time.

When calculating the number of accounts based on the specified percentage, CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.

Note that this setting lets you specify the *maximum* for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.

Conditional: You must specify either `MaxConcurrentCount` or `MaxConcurrentPercentage` , but not both.

By default, `1` is specified.

ConcurrencyMode -> (string)

Specifies how the concurrency level behaves during the operation execution.

- `STRICT_FAILURE_TOLERANCE` : This option dynamically lowers the concurrency level to ensure the number of failed accounts never exceeds the value of `FailureToleranceCount` +1. The initial actual concurrency is set to the lower of either the value of the `MaxConcurrentCount` , or the value of `FailureToleranceCount` +1. The actual concurrency is then reduced proportionally by the number of failures. This is the default behavior. If failure tolerance or Maximum concurrent accounts are set to percentages, the behavior is similar.
- `SOFT_FAILURE_TOLERANCE` : This option decouples `FailureToleranceCount` from the actual concurrency. This allows stack set operations to run at the concurrency level set by the `MaxConcurrentCount` value, or `MaxConcurrentPercentage` , regardless of the number of failures.

Shorthand Syntax:

```
RegionConcurrencyType=string,RegionOrder=string,string,FailureToleranceCount=integer,FailureTolerancePercentage=integer,MaxConcurrentCount=integer,MaxConcurrentPercentage=integer,ConcurrencyMode=string
```

JSON Syntax:

```
{
  "RegionConcurrencyType": "SEQUENTIAL"|"PARALLEL",
  "RegionOrder": ["string", ...],
  "FailureToleranceCount": integer,
  "FailureTolerancePercentage": integer,
  "MaxConcurrentCount": integer,
  "MaxConcurrentPercentage": integer,
  "ConcurrencyMode": "STRICT_FAILURE_TOLERANCE"|"SOFT_FAILURE_TOLERANCE"
}
```

`--administration-role-arn` (string)

[Self-managed permissions] The Amazon Resource Name (ARN) of the IAM role to use to update this stack set.

Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see [Grant self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html) in the *CloudFormation User Guide* .

If you specified a customized administrator role when you created the stack set, you must specify a customized administrator role, even if it is the same customized administrator role used with this stack set previously.

`--execution-role-name` (string)

[Self-managed permissions] The name of the IAM execution role to use to update the stack set. If you do not specify an execution role, CloudFormation uses the `AWSCloudFormationStackSetExecutionRole` role for the stack set operation.

Specify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their stack sets.

If you specify a customized execution role, CloudFormation uses that role to update the stack. If you do not specify a customized execution role, CloudFormation performs the update using the role previously associated with the stack set, so long as you have permissions to perform operations on the stack set.

`--deployment-targets` (structure)

[Service-managed permissions] The Organizations accounts in which to update associated stack instances.

To update all the stack instances associated with this stack set, do not specify `DeploymentTargets` or `Regions` .

If the stack set update includes changes to the template (that is, if `TemplateBody` or `TemplateURL` is specified), or the `Parameters` , CloudFormation marks all stack instances with a status of `OUTDATED` prior to updating the stack instances in the specified accounts and Amazon Web Services Regions. If the stack set update doesnât include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Regions, while leaving all other stack instances with their existing stack instance status.

Accounts -> (list)

The account IDs of the Amazon Web Services accounts. If you have many account numbers, you can provide those accounts using the `AccountsUrl` property instead.

(string)

AccountsUrl -> (string)

The Amazon S3 URL path to a file that contains a list of Amazon Web Services account IDs. The file format must be either `.csv` or `.txt` , and the data can be comma-separated or new-line-separated. There is currently a 10MB limit for the data (approximately 800,000 accounts).

OrganizationalUnitIds -> (list)

The organization root ID or organizational unit (OU) IDs.

(string)

AccountFilterType -> (string)

Limit deployment targets to individual accounts or include additional accounts with provided OUs.

The following is a list of possible values for the `AccountFilterType` operation.

- `INTERSECTION` : StackSets deploys to the accounts specified in `Accounts` parameter.
- `DIFFERENCE` : StackSets excludes the accounts specified in `Accounts` parameter. This enables user to avoid certain accounts within an OU such as suspended accounts.
- `UNION` : StackSets includes additional accounts deployment targets.  This is the default value if `AccountFilterType` is not provided. This enables user to update an entire OU and individual accounts from a different OU in one request, which used to be two separate requests.
- `NONE` : Deploys to all the accounts in specified organizational units (OU).

Shorthand Syntax:

```
Accounts=string,string,AccountsUrl=string,OrganizationalUnitIds=string,string,AccountFilterType=string
```

JSON Syntax:

```
{
  "Accounts": ["string", ...],
  "AccountsUrl": "string",
  "OrganizationalUnitIds": ["string", ...],
  "AccountFilterType": "NONE"|"INTERSECTION"|"DIFFERENCE"|"UNION"
}
```

`--permission-model` (string)

Describes how the IAM roles required for stack set operations are created. You cannot modify `PermissionModel` if there are stack instances associated with your stack set.

- With `self-managed` permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see [Grant self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html) .
- With `service-managed` permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see [Activate trusted access for stack sets with Organizations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-activate-trusted-access.html) .

Possible values:

- `SERVICE_MANAGED`
- `SELF_MANAGED`

`--auto-deployment` (structure)

[Service-managed permissions] Describes whether StackSets automatically deploys to Organizations accounts that are added to a target organization or organizational unit (OU). For more information, see [Manage automatic deployments for CloudFormation StackSets that use service-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-manage-auto-deployment.html) in the *CloudFormation User Guide* .

If you specify `AutoDeployment` , donât specify `DeploymentTargets` or `Regions` .

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

`--operation-id` (string)

The unique ID for this stack set operation.

The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that CloudFormation successfully received them.

If you donât specify an operation ID, CloudFormation generates one automatically.

Repeating this stack set operation with a new operation ID retries all stack instances whose status is `OUTDATED` .

`--accounts` (list)

[Self-managed permissions] The accounts in which to update associated stack instances. If you specify accounts, you must also specify the Amazon Web Services Regions in which to update stack set instances.

To update *all* the stack instances associated with this stack set, donât specify the `Accounts` or `Regions` properties.

If the stack set update includes changes to the template (that is, if the `TemplateBody` or `TemplateURL` properties are specified), or the `Parameters` property, CloudFormation marks all stack instances with a status of `OUTDATED` prior to updating the stack instances in the specified accounts and Amazon Web Services Regions. If the stack set update does not include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Amazon Web Services Regions, while leaving all other stack instances with their existing stack instance status.

(string)

Syntax:

```
"string" "string" ...
```

`--regions` (list)

The Amazon Web Services Regions in which to update associated stack instances. If you specify Regions, you must also specify accounts in which to update stack set instances.

To update *all* the stack instances associated with this stack set, do not specify the `Accounts` or `Regions` properties.

If the stack set update includes changes to the template (that is, if the `TemplateBody` or `TemplateURL` properties are specified), or the `Parameters` property, CloudFormation marks all stack instances with a status of `OUTDATED` prior to updating the stack instances in the specified accounts and Regions. If the stack set update does not include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Regions, while leaving all other stack instances with their existing stack instance status.

(string)

Syntax:

```
"string" "string" ...
```

`--call-as` (string)

[Service-managed permissions] Specifies whether you are acting as an account administrator in the organizationâs management account or as a delegated administrator in a member account.

By default, `SELF` is specified. Use `SELF` for stack sets with self-managed permissions.

- If you are signed in to the management account, specify `SELF` .
- If you are signed in to a delegated administrator account, specify `DELEGATED_ADMIN` . Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see [Register a delegated administrator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html) in the *CloudFormation User Guide* .

Possible values:

- `SELF`
- `DELEGATED_ADMIN`

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

**To update a stack set**

The following `update-stack-set` example adds a tag with the key name `Owner` and a value of `IT` to the stack instances in the specified stack set.

```
aws cloudformation update-stack-set \
    --stack-set-name my-stack-set \
    --use-previous-template \
    --tags Key=Owner,Value=IT
```

Output:

```
{
    "OperationId": "e2b60321-6cab-xmpl-bde7-530c6f47950e"
}
```

## Output

OperationId -> (string)

The unique ID for this stack set operation.