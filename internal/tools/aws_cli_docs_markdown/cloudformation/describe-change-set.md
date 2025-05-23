# describe-change-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-change-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-change-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# describe-change-set

## Description

Returns the inputs for the change set and a list of changes that CloudFormation will make if you execute the change set. For more information, see [Update CloudFormation stacks using change sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html) in the *CloudFormation User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeChangeSet)

`describe-change-set` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Changes`

## Synopsis

```
describe-change-set
--change-set-name <value>
[--stack-name <value>]
[--include-property-values | --no-include-property-values]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--max-items <value>]
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

`--change-set-name` (string)

The name or Amazon Resource Name (ARN) of the change set that you want to describe.

`--stack-name` (string)

If you specified the name of a change set, specify the stack name or ID (ARN) of the change set you want to describe.

`--include-property-values` | `--no-include-property-values` (boolean)

If `true` , the returned changes include detailed changes in the property values.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To get information about a change set**

The following `describe-change-set` example displays the details of the change set specified by change set name and stack name.

```
aws cloudformation describe-change-set \
    --change-set-name my-change-set \
    --stack-name my-stack
```

The following `describe-change-set` example displays the details of the change set specified by the full ARN of the change set:

```
aws cloudformation describe-change-set \
    --change-set-name arn:aws:cloudformation:us-west-2:123456789012:changeSet/my-change-set/bc9555ba-a949-xmpl-bfb8-f41d04ec5784
```

Output:

```
{
    "Changes": [
        {
            "Type": "Resource",
            "ResourceChange": {
                "Action": "Modify",
                "LogicalResourceId": "function",
                "PhysicalResourceId": "my-function-SEZV4XMPL4S5",
                "ResourceType": "AWS::Lambda::Function",
                "Replacement": "False",
                "Scope": [
                    "Properties"
                ],
                "Details": [
                    {
                        "Target": {
                            "Attribute": "Properties",
                            "Name": "Timeout",
                            "RequiresRecreation": "Never"
                        },
                        "Evaluation": "Static",
                        "ChangeSource": "DirectModification"
                    }
                ]
            }
        }
    ],
    "ChangeSetName": "my-change-set",
    "ChangeSetId": "arn:aws:cloudformation:us-west-2:123456789012:changeSet/my-change-set/4eca1a01-e285-xmpl-8026-9a1967bfb4b0",
    "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204",
    "StackName": "my-stack",
    "Description": null,
    "Parameters": null,
    "CreationTime": "2019-10-02T05:20:56.651Z",
    "ExecutionStatus": "AVAILABLE",
    "Status": "CREATE_COMPLETE",
    "StatusReason": null,
    "NotificationARNs": [],
    "RollbackConfiguration": {},
    "Capabilities": [
        "CAPABILITY_IAM"
    ],
    "Tags": null
}
```

## Output

ChangeSetName -> (string)

The name of the change set.

ChangeSetId -> (string)

The Amazon Resource Name (ARN) of the change set.

StackId -> (string)

The Amazon Resource Name (ARN) of the stack thatâs associated with the change set.

StackName -> (string)

The name of the stack thatâs associated with the change set.

Description -> (string)

Information about the change set.

Parameters -> (list)

A list of `Parameter` structures that describes the input parameters and their values used to create the change set. For more information, see the [Parameter](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html) data type.

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

CreationTime -> (timestamp)

The start time when the change set was created, in UTC.

ExecutionStatus -> (string)

If the change set execution status is `AVAILABLE` , you can execute the change set. If you canât execute the change set, the status indicates why. For example, a change set might be in an `UNAVAILABLE` state because CloudFormation is still creating it or in an `OBSOLETE` state because the stack was already updated.

Status -> (string)

The current status of the change set, such as `CREATE_PENDING` , `CREATE_COMPLETE` , or `FAILED` .

StatusReason -> (string)

A description of the change setâs status. For example, if your attempt to create a change set failed, CloudFormation shows the error message.

NotificationARNs -> (list)

The ARNs of the Amazon SNS topics that will be associated with the stack if you execute the change set.

(string)

RollbackConfiguration -> (structure)

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

Capabilities -> (list)

If you execute the change set, the list of capabilities that were explicitly acknowledged when the change set was created.

(string)

Tags -> (list)

If you execute the change set, the tags that will be associated with the stack.

(structure)

The Tag type enables you to specify a key-value pair that can be used to store information about an CloudFormation stack.

Key -> (string)

*Required* . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services have the reserved prefix: `aws:` .

Value -> (string)

*Required* . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.

Changes -> (list)

A list of `Change` structures that describes the resources CloudFormation changes if you execute the change set.

(structure)

The `Change` structure describes the changes CloudFormation will perform if you execute the change set.

Type -> (string)

The type of entity that CloudFormation changes.

- `Resource` This change is for a resource.

HookInvocationCount -> (integer)

Is either `null` , if no Hooks invoke for the resource, or contains the number of Hooks that will invoke for the resource.

ResourceChange -> (structure)

A `ResourceChange` structure that describes the resource and action that CloudFormation will perform.

PolicyAction -> (string)

The action that will be taken on the physical resource when the change set is executed.

- `Delete` The resource will be deleted.
- `Retain` The resource will be retained.
- `Snapshot` The resource will have a snapshot taken.
- `ReplaceAndDelete` The resource will be replaced and then deleted.
- `ReplaceAndRetain` The resource will be replaced and then retained.
- `ReplaceAndSnapshot` The resource will be replaced and then have a snapshot taken.

Action -> (string)

The action that CloudFormation takes on the resource, such as `Add` (adds a new resource), `Modify` (changes a resource), `Remove` (deletes a resource), `Import` (imports a resource), or `Dynamic` (exact action for the resource canât be determined).

LogicalResourceId -> (string)

The resourceâs logical ID, which is defined in the stackâs template.

PhysicalResourceId -> (string)

The resourceâs physical ID (resource name). Resources that you are adding donât have physical IDs because they havenât been created.

ResourceType -> (string)

The type of CloudFormation resource, such as `AWS::S3::Bucket` .

Replacement -> (string)

For the `Modify` action, indicates whether CloudFormation will replace the resource by creating a new one and deleting the old one. This value depends on the value of the `RequiresRecreation` property in the `ResourceTargetDefinition` structure. For example, if the `RequiresRecreation` field is `Always` and the `Evaluation` field is `Static` , `Replacement` is `True` . If the `RequiresRecreation` field is `Always` and the `Evaluation` field is `Dynamic` , `Replacement` is `Conditional` .

If you have multiple changes with different `RequiresRecreation` values, the `Replacement` value depends on the change with the most impact. A `RequiresRecreation` value of `Always` has the most impact, followed by `Conditional` , and then `Never` .

Scope -> (list)

For the `Modify` action, indicates which resource attribute is triggering this update, such as a change in the resource attributeâs `Metadata` , `Properties` , or `Tags` .

(string)

Details -> (list)

For the `Modify` action, a list of `ResourceChangeDetail` structures that describes the changes that CloudFormation will make to the resource.

(structure)

For a resource with `Modify` as the action, the `ResourceChange` structure describes the changes CloudFormation will make to that resource.

Target -> (structure)

A `ResourceTargetDefinition` structure that describes the field that CloudFormation will change and whether the resource will be recreated.

Attribute -> (string)

Indicates which resource attribute is triggering this update, such as a change in the resource attributeâs `Metadata` , `Properties` , or `Tags` .

Name -> (string)

If the `Attribute` value is `Properties` , the name of the property. For all other attributes, the value is null.

RequiresRecreation -> (string)

If the `Attribute` value is `Properties` , indicates whether a change to this property causes the resource to be recreated. The value can be `Never` , `Always` , or `Conditionally` . To determine the conditions for a `Conditionally` recreation, see the update behavior for that property in the [Amazon Web Services resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the *CloudFormation User Guide* .

Path -> (string)

The property path of the property.

BeforeValue -> (string)

The value of the property before the change is executed. Large values can be truncated.

AfterValue -> (string)

The value of the property after the change is executed. Large values can be truncated.

AttributeChangeType -> (string)

The type of change to be made to the property if the change is executed.

- `Add` The item will be added.
- `Remove` The item will be removed.
- `Modify` The item will be modified.

Evaluation -> (string)

Indicates whether CloudFormation can determine the target value, and whether the target value will change before you execute a change set.

For `Static` evaluations, CloudFormation can determine that the target value will change, and its value. For example, if you directly modify the `InstanceType` property of an EC2 instance, CloudFormation knows that this property value will change, and its value, so this is a `Static` evaluation.

For `Dynamic` evaluations, canât determine the target value because it depends on the result of an intrinsic function, such as a `Ref` or `Fn::GetAtt` intrinsic function, when the stack is updated. For example, if your template includes a reference to a resource thatâs conditionally recreated, the value of the reference (the physical ID of the resource) might change, depending on if the resource is recreated. If the resource is recreated, it will have a new physical ID, so all references to that resource will also be updated.

ChangeSource -> (string)

The group to which the `CausingEntity` value belongs. There are five entity groups:

- `ResourceReference` entities are `Ref` intrinsic functions that refer to resources in the template, such as `{ "Ref" : "MyEC2InstanceResource" }` .
- `ParameterReference` entities are `Ref` intrinsic functions that get template parameter values, such as `{ "Ref" : "MyPasswordParameter" }` .
- `ResourceAttribute` entities are `Fn::GetAtt` intrinsic functions that get resource attribute values, such as `{ "Fn::GetAtt" : [ "MyEC2InstanceResource", "PublicDnsName" ] }` .
- `DirectModification` entities are changes that are made directly to the template.
- `Automatic` entities are `AWS::CloudFormation::Stack` resource types, which are also known as nested stacks. If you made no changes to the `AWS::CloudFormation::Stack` resource, CloudFormation sets the `ChangeSource` to `Automatic` because the nested stackâs template might have changed. Changes to a nested stackâs template arenât visible to CloudFormation until you run an update on the parent stack.

CausingEntity -> (string)

The identity of the entity that triggered this change. This entity is a member of the group thatâs specified by the `ChangeSource` field. For example, if you modified the value of the `KeyPairName` parameter, the `CausingEntity` is the name of the parameter (`KeyPairName` ).

If the `ChangeSource` value is `DirectModification` , no value is given for `CausingEntity` .

ChangeSetId -> (string)

The change set ID of the nested change set.

ModuleInfo -> (structure)

Contains information about the module from which the resource was created, if the resource was created from a module included in the stack template.

TypeHierarchy -> (string)

A concatenated list of the module type or types containing the resource. Module types are listed starting with the inner-most nested module, and separated by `/` .

In the following example, the resource was created from a module of type `AWS::First::Example::MODULE` , thatâs nested inside a parent module of type `AWS::Second::Example::MODULE` .

`AWS::First::Example::MODULE/AWS::Second::Example::MODULE`

LogicalIdHierarchy -> (string)

A concatenated list of the logical IDs of the module or modules containing the resource. Modules are listed starting with the inner-most nested module, and separated by `/` .

In the following example, the resource was created from a module, `moduleA` , thatâs nested inside a parent module, `moduleB` .

`moduleA/moduleB`

For more information, see [Reference module resources in CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/module-ref-resources.html) in the *CloudFormation User Guide* .

BeforeContext -> (string)

An encoded JSON string containing the context of the resource before the change is executed.

AfterContext -> (string)

An encoded JSON string containing the context of the resource after the change is executed.

NextToken -> (string)

If the output exceeds 1 MB, a string that identifies the next page of changes. If there is no additional page, this value is null.

IncludeNestedStacks -> (boolean)

Verifies if `IncludeNestedStacks` is set to `True` .

ParentChangeSetId -> (string)

Specifies the change set ID of the parent change set in the current nested change set hierarchy.

RootChangeSetId -> (string)

Specifies the change set ID of the root change set in the current nested change set hierarchy.

OnStackFailure -> (string)

Determines what action will be taken if stack creation fails. When this parameter is specified, the `DisableRollback` parameter to the [ExecuteChangeSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html) API operation must not be specified. This must be one of these values:

- `DELETE` - Deletes the change set if the stack creation fails. This is only valid when the `ChangeSetType` parameter is set to `CREATE` . If the deletion of the stack fails, the status of the stack is `DELETE_FAILED` .
- `DO_NOTHING` - if the stack creation fails, do nothing. This is equivalent to specifying `true` for the `DisableRollback` parameter to the [ExecuteChangeSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html) API operation.
- `ROLLBACK` - if the stack creation fails, roll back the stack. This is equivalent to specifying `false` for the `DisableRollback` parameter to the [ExecuteChangeSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html) API operation.

ImportExistingResources -> (boolean)

Indicates if the change set imports resources that already exist.

### Note

This parameter can only import resources that have [custom names](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html) in templates. To import resources that do not accept custom names, such as EC2 instances, use the [resource import](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import.html) feature instead.