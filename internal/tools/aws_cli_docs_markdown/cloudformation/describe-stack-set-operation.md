# describe-stack-set-operationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-set-operation.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-set-operation.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# describe-stack-set-operation

## Description

Returns the description of the specified StackSet operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStackSetOperation)

## Synopsis

```
describe-stack-set-operation
--stack-set-name <value>
--operation-id <value>
[--call-as <value>]
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

The name or the unique stack ID of the stack set for the stack operation.

`--operation-id` (string)

The unique ID of the stack set operation.

`--call-as` (string)

[Service-managed permissions] Specifies whether you are acting as an account administrator in the organizationâs management account or as a delegated administrator in a member account.

By default, `SELF` is specified. Use `SELF` for stack sets with self-managed permissions.

- If you are signed in to the management account, specify `SELF` .
- If you are signed in to a delegated administrator account, specify `DELEGATED_ADMIN` . Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see [Register a delegated administrator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html) in the *CloudFormation User Guide* .

Possible values:

- `SELF`
- `DELEGATED_ADMIN`

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

**To get information about a stack set operation**

The following describe-stack-set-operation` example displays details for an update operation on the specified stack set.

```
aws cloudformation describe-stack-set-operation \
    --stack-set-name enable-config \
    --operation-id 35d45ebc-ed88-xmpl-ab59-0197a1fc83a0
```

Output:

```
{
    "StackSetOperation": {
        "OperationId": "35d45ebc-ed88-xmpl-ab59-0197a1fc83a0",
        "StackSetId": "enable-config:296a3360-xmpl-40af-be78-9341e95bf743",
        "Action": "UPDATE",
        "Status": "SUCCEEDED",
        "OperationPreferences": {
            "RegionOrder": [
                "us-east-1",
                "us-west-2",
                "eu-west-1",
                "us-west-1"
            ],
            "FailureToleranceCount": 7,
            "MaxConcurrentCount": 2
        },
        "AdministrationRoleARN": "arn:aws:iam::123456789012:role/AWSCloudFormationStackSetAdministrationRole",
        "ExecutionRoleName": "AWSCloudFormationStackSetExecutionRole",
        "CreationTimestamp": "2019-10-03T16:28:44.377Z",
        "EndTimestamp": "2019-10-03T16:42:08.607Z"
    }
}
```

## Output

StackSetOperation -> (structure)

The specified stack set operation.

OperationId -> (string)

The unique ID of a stack set operation.

StackSetId -> (string)

The ID of the stack set.

Action -> (string)

The type of stack set operation: `CREATE` , `UPDATE` , or `DELETE` . Create and delete operations affect only the specified stack set instances that are associated with the specified stack set. Update operations affect both the stack set itself, in addition to *all* associated stack set instances.

Status -> (string)

The status of the operation.

- `FAILED` : The operation exceeded the specified failure tolerance. The failure tolerance value that youâve set for an operation is applied for each Region during stack create and update operations. If the number of failed stacks within a Region exceeds the failure tolerance, the status of the operation in the Region is set to `FAILED` . This in turn sets the status of the operation as a whole to `FAILED` , and CloudFormation cancels the operation in any remaining Regions.
- `QUEUED` : [Service-managed permissions] For automatic deployments that require a sequence of operations, the operation is queued to be performed. For more information, see the [StackSets status codes](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html#stackset-status-codes) in the *CloudFormation User Guide* .
- `RUNNING` : The operation is currently being performed.
- `STOPPED` : The user has canceled the operation.
- `STOPPING` : The operation is in the process of stopping, at user request.
- `SUCCEEDED` : The operation completed creating or updating all the specified stacks without exceeding the failure tolerance for the operation.

OperationPreferences -> (structure)

The preferences for how CloudFormation performs this stack set operation.

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

RetainStacks -> (boolean)

For stack set operations of action type `DELETE` , specifies whether to remove the stack instances from the specified stack set, but doesnât delete the stacks. You canât re-associate a retained stack, or add an existing, saved stack to a new stack set.

AdministrationRoleARN -> (string)

The Amazon Resource Name (ARN) of the IAM role used to perform this stack set operation.

Use customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see [Grant self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html) in the *CloudFormation User Guide* .

ExecutionRoleName -> (string)

The name of the IAM execution role used to create or update the stack set.

Use customized execution roles to control which stack resources users and groups can include in their stack sets.

CreationTimestamp -> (timestamp)

The time at which the operation was initiated. Note that the creation times for the stack set operation might differ from the creation time of the individual stacks themselves. This is because CloudFormation needs to perform preparatory work for the operation, such as dispatching the work to the requested Regions, before actually creating the first stacks.

EndTimestamp -> (timestamp)

The time at which the stack set operation ended, across all accounts and Regions specified. Note that this doesnât necessarily mean that the stack set operation was successful, or even attempted, in each account or Region.

DeploymentTargets -> (structure)

[Service-managed permissions] The Organizations accounts affected by the stack operation.

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

StackSetDriftDetectionDetails -> (structure)

Detailed information about the drift status of the stack set. This includes information about drift operations currently being performed on the stack set.

This information will only be present for stack set operations whose `Action` type is `DETECT_DRIFT` .

For more information, see [Performing drift detection on CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html) in the *CloudFormation User Guide* .

DriftStatus -> (string)

Status of the stack setâs actual configuration compared to its expected template and parameter configuration. A stack set is considered to have drifted if one or more of its stack instances have drifted from their expected template and parameter configuration.

- `DRIFTED` : One or more of the stack instances belonging to the stack set stack differs from the expected template and parameter configuration. A stack instance is considered to have drifted if one or more of the resources in the associated stack have drifted.
- `NOT_CHECKED` : CloudFormation hasnât checked the stack set for drift.
- `IN_SYNC` : All of the stack instances belonging to the stack set stack match from the expected template and parameter configuration.

DriftDetectionStatus -> (string)

The status of the stack set drift detection operation.

- `COMPLETED` : The drift detection operation completed without failing on any stack instances.
- `FAILED` : The drift detection operation exceeded the specified failure tolerance.
- `PARTIAL_SUCCESS` : The drift detection operation completed without exceeding the failure tolerance for the operation.
- `IN_PROGRESS` : The drift detection operation is currently being performed.
- `STOPPED` : The user has canceled the drift detection operation.

LastDriftCheckTimestamp -> (timestamp)

Most recent time when CloudFormation performed a drift detection operation on the stack set. This value will be `NULL` for any stack set on which drift detection hasnât yet been performed.

TotalStackInstancesCount -> (integer)

The total number of stack instances belonging to this stack set.

The total number of stack instances is equal to the total of:

- Stack instances that match the stack set configuration.
- Stack instances that have drifted from the stack set configuration.
- Stack instances where the drift detection operation has failed.
- Stack instances currently being checked for drift.

DriftedStackInstancesCount -> (integer)

The number of stack instances that have drifted from the expected template and parameter configuration of the stack set. A stack instance is considered to have drifted if one or more of the resources in the associated stack donât match their expected configuration.

InSyncStackInstancesCount -> (integer)

The number of stack instances which match the expected template and parameter configuration of the stack set.

InProgressStackInstancesCount -> (integer)

The number of stack instances that are currently being checked for drift.

FailedStackInstancesCount -> (integer)

The number of stack instances for which the drift detection operation failed.

StatusReason -> (string)

The status of the operation in details.

StatusDetails -> (structure)

Detailed information about the StackSet operation.

FailedStackInstancesCount -> (integer)

The number of stack instances for which the StackSet operation failed.