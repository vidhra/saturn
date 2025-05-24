# detect-stack-set-driftÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/detect-stack-set-drift.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/detect-stack-set-drift.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# detect-stack-set-drift

## Description

Detect drift on a stack set. When CloudFormation performs drift detection on a stack set, it performs drift detection on the stack associated with each stack instance in the stack set. For more information, see [Performing drift detection on CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html) .

`DetectStackSetDrift` returns the `OperationId` of the stack set drift detection operation. Use this operation id with  DescribeStackSetOperation to monitor the progress of the drift detection operation. The drift detection operation may take some time, depending on the number of stack instances included in the stack set, in addition to the number of resources included in each stack.

Once the operation has completed, use the following actions to return drift information:

- Use  DescribeStackSet to return detailed information about the stack set, including detailed information about the last *completed* drift operation performed on the stack set. (Information about drift operations that are in progress isnât included.)
- Use  ListStackInstances to return a list of stack instances belonging to the stack set, including the drift status and last drift time checked of each instance.
- Use  DescribeStackInstance to return detailed information about a specific stack instance, including its drift status and last drift time checked.

You can only run a single drift detection operation on a given stack set at one time.

To stop a drift detection stack set operation, use  StopStackSetOperation .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DetectStackSetDrift)

## Synopsis

```
detect-stack-set-drift
--stack-set-name <value>
[--operation-preferences <value>]
[--operation-id <value>]
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

The name of the stack set on which to perform the drift detection operation.

`--operation-preferences` (structure)

The user-specified preferences for how CloudFormation performs a stack set operation.

For more information about maximum concurrent accounts and failure tolerance, see [Stack set operation options](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html#stackset-ops-options) .

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

`--operation-id` (string)

*The ID of the stack set operation.*

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

**To detect drift on a stack set and all associated stack instances**

The following `detect-stack-set-drift` example initiates drift detection operations on the specified stack set, including all the stack instances associated with that stack set, and returns an operation ID that can be used to track the status of the drift operation.

```
aws cloudformation detect-stack-set-drift \
    --stack-set-name stack-set-drift-example
```

Output:

```
{
    "OperationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

For more information, see [Detecting Unmanaged Configuration Changes in Stack Sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html) in the *AWS CloudFormation Users Guide*.

## Output

OperationId -> (string)

The ID of the drift detection stack set operation.

You can use this operation ID with  DescribeStackSetOperation to monitor the progress of the drift detection operation.