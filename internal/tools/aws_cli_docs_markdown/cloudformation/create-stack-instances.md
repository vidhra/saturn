# create-stack-instancesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack-instances.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack-instances.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# create-stack-instances

## Description

Creates stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region. You must specify at least one value for either `Accounts` or `DeploymentTargets` , and you must specify at least one value for `Regions` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateStackInstances)

## Synopsis

```
create-stack-instances
--stack-set-name <value>
[--accounts <value>]
[--deployment-targets <value>]
--regions <value>
[--parameter-overrides <value>]
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

The name or unique ID of the stack set that you want to create stack instances from.

`--accounts` (list)

[Self-managed permissions] The account IDs of one or more Amazon Web Services accounts that you want to create stack instances in the specified Region(s) for.

You can specify `Accounts` or `DeploymentTargets` , but not both.

(string)

Syntax:

```
"string" "string" ...
```

`--deployment-targets` (structure)

[Service-managed permissions] The Organizations accounts for which to create stack instances in the specified Amazon Web Services Regions.

You can specify `Accounts` or `DeploymentTargets` , but not both.

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

`--regions` (list)

The names of one or more Amazon Web Services Regions where you want to create stack instances using the specified Amazon Web Services accounts.

(string)

Syntax:

```
"string" "string" ...
```

`--parameter-overrides` (list)

A list of stack set parameters whose values you want to override in the selected stack instances.

Any overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions. When specifying parameters and their values, be aware of how CloudFormation sets parameter values during stack instance operations:

- To override the current value for a parameter, include the parameter and specify its value.
- To leave an overridden parameter set to its present value, include the parameter and specify `UsePreviousValue` as `true` . (You canât specify both a value and set `UsePreviousValue` to `true` .)
- To set an overridden parameter back to the value specified in the stack set, specify a parameter list but donât include the parameter in the list.
- To leave all parameters set to their present values, donât specify this property at all.

During stack set updates, any parameter values overridden for a stack instance arenât updated, but retain their overridden value.

You can only override the parameter *values* that are specified in the stack set; to add or delete a parameter itself, use [UpdateStackSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html) to update the stack set template.

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

`--operation-id` (string)

The unique identifier for this stack set operation.

The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that CloudFormation successfully received them.

If you donât specify an operation ID, the SDK generates one automatically.

Repeating this stack set operation with a new operation ID retries all stack instances whose status is `OUTDATED` .

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

**To create stack instances**

The following `create-stack-instances` example creates instances of a stack set in two accounts and in four regions. The fault tolerance setting ensures that the update is attempted in all accounts and regions, even if some stacks cannot be created.

```
aws cloudformation create-stack-instances \
    --stack-set-name my-stack-set \
    --accounts 123456789012 223456789012 \
    --regions us-east-1 us-east-2 us-west-1 us-west-2 \
    --operation-preferences FailureToleranceCount=7
```

Output:

```
{
    "OperationId": "d7995c31-83c2-xmpl-a3d4-e9ca2811563f"
}
```

To create a stack set, use the `create-stack-set` command.

## Output

OperationId -> (string)

The unique identifier for this stack set operation.