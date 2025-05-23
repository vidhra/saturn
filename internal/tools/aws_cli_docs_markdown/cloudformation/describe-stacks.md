# describe-stacksÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stacks.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stacks.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# describe-stacks

## Description

Returns the description for the specified stack; if no stack name was specified, then it returns the description for all the stacks created. For more information about a stackâs event history, see [Understand CloudFormation stack creation events](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-resource-configuration-complete.html) in the *CloudFormation User Guide* .

### Note

If the stack doesnât exist, a `ValidationError` is returned.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStacks)

`describe-stacks` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Stacks`

## Synopsis

```
describe-stacks
[--stack-name <value>]
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

`--stack-name` (string)

### Note

If you donât pass a parameter to `StackName` , the API returns a response that describes all resources in the account, which can impact performance. This requires `ListStacks` and `DescribeStacks` permissions.

Consider using the  ListStacks API if youâre not passing a parameter to `StackName` .

The IAM policy below can be added to IAM policies when you want to limit resource-level permissions and avoid returning a response when no parameter is sent in the request:

{ âVersionâ: â2012-10-17â, âStatementâ: [{ âEffectâ: âDenyâ, âActionâ: âcloudformation:DescribeStacksâ, âNotResourceâ: âarn:aws:cloudformation:*:*:stack/*/*â }] }

The name or the unique stack ID thatâs associated with the stack, which arenât always interchangeable:

- Running stacks: You can specify either the stackâs name or its unique stack ID.
- Deleted stacks: You must specify the unique stack ID.

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

**To describe AWS CloudFormation stacks**

The following `describe-stacks` command shows summary information for the `myteststack` stack:

```
aws cloudformation describe-stacks --stack-name myteststack
```

Output:

```
{
    "Stacks":  [
        {
            "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/myteststack/466df9e0-0dff-08e3-8e2f-5088487c4896",
            "Description": "AWS CloudFormation Sample Template S3_Bucket: Sample template showing how to create a publicly accessible S3 bucket. **WARNING** This template creates an S3 bucket. You will be billed for the AWS resources used if you create a stack from this template.",
            "Tags": [],
            "Outputs": [
                {
                    "Description": "Name of S3 bucket to hold website content",
                    "OutputKey": "BucketName",
                    "OutputValue": "myteststack-s3bucket-jssofi1zie2w"
                }
            ],
            "StackStatusReason": null,
            "CreationTime": "2013-08-23T01:02:15.422Z",
            "Capabilities": [],
            "StackName": "myteststack",
            "StackStatus": "CREATE_COMPLETE",
            "DisableRollback": false
        }
    ]
}
```

For more information, see [Stacks](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/concept-stack.html) in the *AWS CloudFormation User Guide*.

## Output

Stacks -> (list)

A list of stack structures.

(structure)

The Stack data type.

StackId -> (string)

Unique identifier of the stack.

StackName -> (string)

The name associated with the stack.

ChangeSetId -> (string)

The unique ID of the change set.

Description -> (string)

A user-defined description associated with the stack.

Parameters -> (list)

A list of `Parameter` structures.

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

The time at which the stack was created.

DeletionTime -> (timestamp)

The time the stack was deleted.

LastUpdatedTime -> (timestamp)

The time the stack was last updated. This field will only be returned if the stack has been updated at least once.

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

StackStatus -> (string)

Current status of the stack.

StackStatusReason -> (string)

Success/failure message associated with the stack status.

DisableRollback -> (boolean)

Boolean to enable or disable rollback on stack creation failures:

- `true` : disable rollback.
- `false` : enable rollback.

NotificationARNs -> (list)

Amazon SNS topic Amazon Resource Names (ARNs) to which stack related events are published.

(string)

TimeoutInMinutes -> (integer)

The amount of time within which stack creation should complete.

Capabilities -> (list)

The capabilities allowed in the stack.

(string)

Outputs -> (list)

A list of output structures.

(structure)

The Output data type.

OutputKey -> (string)

The key associated with the output.

OutputValue -> (string)

The value associated with the output.

Description -> (string)

User defined description associated with the output.

ExportName -> (string)

The name of the export associated with the output.

RoleARN -> (string)

The Amazon Resource Name (ARN) of an IAM role thatâs associated with the stack. During a stack operation, CloudFormation uses this roleâs credentials to make calls on your behalf.

Tags -> (list)

A list of `Tag` s that specify information about the stack.

(structure)

The Tag type enables you to specify a key-value pair that can be used to store information about an CloudFormation stack.

Key -> (string)

*Required* . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services have the reserved prefix: `aws:` .

Value -> (string)

*Required* . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.

EnableTerminationProtection -> (boolean)

Whether termination protection is enabled for the stack.

For [nested stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html) , termination protection is set on the root stack and canât be changed directly on the nested stack. For more information, see [Protect a CloudFormation stack from being deleted](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html) in the *CloudFormation User Guide* .

ParentId -> (string)

For nested stacksâstacks created as resources for another stackâthe stack ID of the direct parent of this stack. For the first level of nested stacks, the root stack is also the parent stack.

For more information, see [Embed stacks within other stacks using nested stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html) in the *CloudFormation User Guide* .

RootId -> (string)

For nested stacksâstacks created as resources for another stackâthe stack ID of the top-level stack to which the nested stack ultimately belongs.

For more information, see [Embed stacks within other stacks using nested stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html) in the *CloudFormation User Guide* .

DriftInformation -> (structure)

Information about whether a stackâs actual configuration differs, or has *drifted* , from its expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see [Detect unmanaged configuration changes to stacks and resources with drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) .

StackDriftStatus -> (string)

Status of the stackâs actual configuration compared to its expected template configuration.

- `DRIFTED` : The stack differs from its expected template configuration. A stack is considered to have drifted if one or more of its resources have drifted.
- `NOT_CHECKED` : CloudFormation hasnât checked if the stack differs from its expected template configuration.
- `IN_SYNC` : The stackâs actual configuration matches its expected template configuration.
- `UNKNOWN` : This value is reserved for future use.

LastCheckTimestamp -> (timestamp)

Most recent time when a drift detection operation was initiated on the stack, or any of its individual resources that support drift detection.

RetainExceptOnCreate -> (boolean)

When set to `true` , newly created resources are deleted when the operation rolls back. This includes newly created resources marked with a deletion policy of `Retain` .

Default: `false`

DeletionMode -> (string)

Specifies the deletion mode for the stack. Possible values are:

- `STANDARD` - Use the standard behavior. Specifying this value is the same as not specifying this parameter.
- `FORCE_DELETE_STACK` - Delete the stack if itâs stuck in a `DELETE_FAILED` state due to resource deletion failure.

DetailedStatus -> (string)

The detailed status of the resource or stack. If `CONFIGURATION_COMPLETE` is present, the resource or resource configuration phase has completed and the stabilization of the resources is in progress. The stack sets `CONFIGURATION_COMPLETE` when all of the resources in the stack have reached that event. For more information, see [Understand CloudFormation stack creation events](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-resource-configuration-complete.html) in the *CloudFormation User Guide* .

NextToken -> (string)

If the output exceeds 1 MB in size, a string that identifies the next page of stacks. If no additional page exists, this value is null.