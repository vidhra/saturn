# simulate-custom-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/simulate-custom-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/simulate-custom-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iam](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html#cli-aws-iam) ]

# simulate-custom-policy

## Description

Simulate how a set of IAM policies and optionally a resource-based policy works with a list of API operations and Amazon Web Services resources to determine the policiesâ effective permissions. The policies are provided as strings.

The simulation does not perform the API operations; it only checks the authorization to determine if the simulated policies allow or deny the operations. You can simulate resources that donât exist in your account.

If you want to simulate existing policies that are attached to an IAM user, group, or role, use  SimulatePrincipalPolicy instead.

Context keys are variables that are maintained by Amazon Web Services and its services and which provide details about the context of an API query request. You can use the `Condition` element of an IAM policy to evaluate context keys. To get the list of context keys that the policies require for correct simulation, use  GetContextKeysForCustomPolicy .

If the output is long, you can use `MaxItems` and `Marker` parameters to paginate the results.

### Note

The IAM policy simulator evaluates statements in the identity-based policy and the inputs that you provide during simulation. The policy simulator results can differ from your live Amazon Web Services environment. We recommend that you check your policies against your live Amazon Web Services environment after testing using the policy simulator to confirm that you have the desired results. For more information about using the policy simulator, see [Testing IAM policies with the IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html) in the *IAM User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/SimulateCustomPolicy)

`simulate-custom-policy` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `EvaluationResults`

## Synopsis

```
simulate-custom-policy
--policy-input-list <value>
[--permissions-boundary-policy-input-list <value>]
--action-names <value>
[--resource-arns <value>]
[--resource-policy <value>]
[--resource-owner <value>]
[--caller-arn <value>]
[--context-entries <value>]
[--resource-handling-option <value>]
[--max-items <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
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

`--policy-input-list` (list)

A list of policy documents to include in the simulation. Each document is specified as a string containing the complete, valid JSON text of an IAM policy. Do not include any resource-based policies in this parameter. Any resource-based policy must be submitted with the `ResourcePolicy` parameter. The policies cannot be âscope-downâ policies, such as you could include in a call to [GetFederationToken](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetFederationToken.html) or one of the [AssumeRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AssumeRole.html) API operations. In other words, do not use policies designed to restrict what a user can do while using the temporary credentials.

The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see [IAM and STS character quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length) .

The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:

- Any printable ASCII character ranging from the space character (`\u0020` ) through the end of the ASCII character range
- The printable characters in the Basic Latin and Latin-1 Supplement character set (through `\u00FF` )
- The special characters tab (`\u0009` ), line feed (`\u000A` ), and carriage return (`\u000D` )

(string)

Syntax:

```
"string" "string" ...
```

`--permissions-boundary-policy-input-list` (list)

The IAM permissions boundary policy to simulate. The permissions boundary sets the maximum permissions that an IAM entity can have. You can input only one permissions boundary when you pass a policy to this operation. For more information about permissions boundaries, see [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide* . The policy input is specified as a string that contains the complete, valid JSON text of a permissions boundary policy.

The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see [IAM and STS character quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length) .

The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:

- Any printable ASCII character ranging from the space character (`\u0020` ) through the end of the ASCII character range
- The printable characters in the Basic Latin and Latin-1 Supplement character set (through `\u00FF` )
- The special characters tab (`\u0009` ), line feed (`\u000A` ), and carriage return (`\u000D` )

(string)

Syntax:

```
"string" "string" ...
```

`--action-names` (list)

A list of names of API operations to evaluate in the simulation. Each operation is evaluated against each resource. Each operation must include the service identifier, such as `iam:CreateUser` . This operation does not support using wildcards (*) in an action name.

(string)

Syntax:

```
"string" "string" ...
```

`--resource-arns` (list)

A list of ARNs of Amazon Web Services resources to include in the simulation. If this parameter is not provided, then the value defaults to `*` (all resources). Each API in the `ActionNames` parameter is evaluated for each resource in this list. The simulation determines the access result (allowed or denied) of each combination and reports it in the response. You can simulate resources that donât exist in your account.

The simulation does not automatically retrieve policies for the specified resources. If you want to include a resource policy in the simulation, then you must include the policy as a string in the `ResourcePolicy` parameter.

If you include a `ResourcePolicy` , then it must be applicable to all of the resources included in the simulation or you receive an invalid input error.

For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

### Note

Simulation of resource-based policies isnât supported for IAM roles.

(string)

Syntax:

```
"string" "string" ...
```

`--resource-policy` (string)

A resource-based policy to include in the simulation provided as a string. Each resource in the simulation is treated as if it had this policy attached. You can include only one resource-based policy in a simulation.

The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see [IAM and STS character quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length) .

The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:

- Any printable ASCII character ranging from the space character (`\u0020` ) through the end of the ASCII character range
- The printable characters in the Basic Latin and Latin-1 Supplement character set (through `\u00FF` )
- The special characters tab (`\u0009` ), line feed (`\u000A` ), and carriage return (`\u000D` )

### Note

Simulation of resource-based policies isnât supported for IAM roles.

`--resource-owner` (string)

An ARN representing the Amazon Web Services account ID that specifies the owner of any simulated resource that does not identify its owner in the resource ARN. Examples of resource ARNs include an S3 bucket or object. If `ResourceOwner` is specified, it is also used as the account owner of any `ResourcePolicy` included in the simulation. If the `ResourceOwner` parameter is not specified, then the owner of the resources and the resource policy defaults to the account of the identity provided in `CallerArn` . This parameter is required only if you specify a resource-based policy and account that owns the resource is different from the account that owns the simulated calling user `CallerArn` .

The ARN for an account uses the following syntax: `arn:aws:iam::*AWS-account-ID* :root` . For example, to represent the account with the 112233445566 ID, use the following ARN: `arn:aws:iam::112233445566-ID:root` .

`--caller-arn` (string)

The ARN of the IAM user that you want to use as the simulated caller of the API operations. `CallerArn` is required if you include a `ResourcePolicy` so that the policyâs `Principal` element has a value to use in evaluating the policy.

You can specify only the ARN of an IAM user. You cannot specify the ARN of an assumed role, federated user, or a service principal.

`--context-entries` (list)

A list of context keys and corresponding values for the simulation to use. Whenever a context key is evaluated in one of the simulated IAM permissions policies, the corresponding value is supplied.

(structure)

Contains information about a condition context key. It includes the name of the key and specifies the value (or values, if the context key supports multiple values) to use in the simulation. This information is used when evaluating the `Condition` elements of the input policies.

This data type is used as an input parameter to  SimulateCustomPolicy and  SimulatePrincipalPolicy .

ContextKeyName -> (string)

The full name of a condition context key, including the service prefix. For example, `aws:SourceIp` or `s3:VersionId` .

ContextKeyValues -> (list)

The value (or values, if the condition context key supports multiple values) to provide to the simulation when the key is referenced by a `Condition` element in an input policy.

(string)

ContextKeyType -> (string)

The data type of the value (or values) specified in the `ContextKeyValues` parameter.

Shorthand Syntax:

```
ContextKeyName=string,ContextKeyValues=string,string,ContextKeyType=string ...
```

JSON Syntax:

```
[
  {
    "ContextKeyName": "string",
    "ContextKeyValues": ["string", ...],
    "ContextKeyType": "string"|"stringList"|"numeric"|"numericList"|"boolean"|"booleanList"|"ip"|"ipList"|"binary"|"binaryList"|"date"|"dateList"
  }
  ...
]
```

`--resource-handling-option` (string)

Specifies the type of simulation to run. Different API operations that support resource-based policies require different combinations of resources. By specifying the type of simulation to run, you enable the policy simulator to enforce the presence of the required resources to ensure reliable simulation results. If your simulation does not match one of the following scenarios, then you can omit this parameter. The following list shows each of the supported scenario values and the resources that you must define to run the simulation.

Each of the Amazon EC2 scenarios requires that you specify instance, image, and security group resources. If your scenario includes an EBS volume, then you must specify that volume as a resource. If the Amazon EC2 scenario includes VPC, then you must supply the network interface resource. If it includes an IP subnet, then you must specify the subnet resource. For more information on the Amazon EC2 scenario options, see [Supported platforms](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html) in the *Amazon EC2 User Guide* .

- **EC2-VPC-InstanceStore**   instance, image, security group, network interface
- **EC2-VPC-InstanceStore-Subnet**   instance, image, security group, network interface, subnet
- **EC2-VPC-EBS**   instance, image, security group, network interface, volume
- **EC2-VPC-EBS-Subnet**   instance, image, security group, network interface, subnet, volume

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

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

**Example 1: To simulate the effects of all IAM policies associated with an IAM user or role**

The following `simulate-custom-policy` shows how to provide both the policy and define variable values and simulate an API call to see if it is allowed or denied. The following example shows a policy that enables database access only after a specified date and time. The simulation succeeds because the simulated actions and the specified `aws:CurrentTime` variable all match the requirements of the policy.

```
aws iam simulate-custom-policy \
    --policy-input-list '{"Version":"2012-10-17","Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"*","Condition":{"DateGreaterThan":{"aws:CurrentTime":"2018-08-16T12:00:00Z"}}}}' \
    --action-names dynamodb:CreateBackup \
    --context-entries "ContextKeyName='aws:CurrentTime',ContextKeyValues='2019-04-25T11:00:00Z',ContextKeyType=date"
```

Output:

```
{
    "EvaluationResults": [
        {
            "EvalActionName": "dynamodb:CreateBackup",
            "EvalResourceName": "*",
            "EvalDecision": "allowed",
            "MatchedStatements": [
                {
                    "SourcePolicyId": "PolicyInputList.1",
                    "StartPosition": {
                        "Line": 1,
                        "Column": 38
                    },
                    "EndPosition": {
                        "Line": 1,
                        "Column": 167
                    }
                }
            ],
            "MissingContextValues": []
        }
    ]
}
```

**Example 2: To simulate a command that is prohibited by the policy**

The following `simulate-custom-policy` example shows the results of simulating a command that is prohibited by the policy. In this example, the provided date is before that required by the policyâs condition.

```
aws iam simulate-custom-policy \
    --policy-input-list '{"Version":"2012-10-17","Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"*","Condition":{"DateGreaterThan":{"aws:CurrentTime":"2018-08-16T12:00:00Z"}}}}' \
    --action-names dynamodb:CreateBackup \
    --context-entries "ContextKeyName='aws:CurrentTime',ContextKeyValues='2014-04-25T11:00:00Z',ContextKeyType=date"
```

Output:

```
{
    "EvaluationResults": [
        {
            "EvalActionName": "dynamodb:CreateBackup",
            "EvalResourceName": "*",
            "EvalDecision": "implicitDeny",
            "MatchedStatements": [],
            "MissingContextValues": []
        }
    ]
}
```

For more information, see [Testing IAM policies with the IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html) in the *AWS IAM User Guide*.

## Output

EvaluationResults -> (list)

The results of the simulation.

(structure)

Contains the results of a simulation.

This data type is used by the return parameter of ``  SimulateCustomPolicy `` and ``  SimulatePrincipalPolicy `` .

EvalActionName -> (string)

The name of the API operation tested on the indicated resource.

EvalResourceName -> (string)

The ARN of the resource that the indicated API operation was tested on.

EvalDecision -> (string)

The result of the simulation.

MatchedStatements -> (list)

A list of the statements in the input policies that determine the result for this scenario. Remember that even if multiple statements allow the operation on the resource, if only one statement denies that operation, then the explicit deny overrides any allow. In addition, the deny statement is the only entry included in the result.

(structure)

Contains a reference to a `Statement` element in a policy document that determines the result of the simulation.

This data type is used by the `MatchedStatements` member of the ``  EvaluationResult `` type.

SourcePolicyId -> (string)

The identifier of the policy that was provided as an input.

SourcePolicyType -> (string)

The type of the policy.

StartPosition -> (structure)

The row and column of the beginning of the `Statement` in an IAM policy.

Line -> (integer)

The line containing the specified position in the document.

Column -> (integer)

The column in the line containing the specified position in the document.

EndPosition -> (structure)

The row and column of the end of a `Statement` in an IAM policy.

Line -> (integer)

The line containing the specified position in the document.

Column -> (integer)

The column in the line containing the specified position in the document.

MissingContextValues -> (list)

A list of context keys that are required by the included input policies but that were not provided by one of the input parameters. This list is used when the resource in a simulation is â*â, either explicitly, or when the `ResourceArns` parameter blank. If you include a list of resources, then any missing context values are instead included under the `ResourceSpecificResults` section. To discover the context keys used by a set of policies, you can call  GetContextKeysForCustomPolicy or  GetContextKeysForPrincipalPolicy .

(string)

OrganizationsDecisionDetail -> (structure)

A structure that details how Organizations and its service control policies affect the results of the simulation. Only applies if the simulated userâs account is part of an organization.

AllowedByOrganizations -> (boolean)

Specifies whether the simulated operation is allowed by the Organizations service control policies that impact the simulated userâs account.

PermissionsBoundaryDecisionDetail -> (structure)

Contains information about the effect that a permissions boundary has on a policy simulation when the boundary is applied to an IAM entity.

AllowedByPermissionsBoundary -> (boolean)

Specifies whether an action is allowed by a permissions boundary that is applied to an IAM entity (user or role). A value of `true` means that the permissions boundary does not deny the action. This means that the policy includes an `Allow` statement that matches the request. In this case, if an identity-based policy also allows the action, the request is allowed. A value of `false` means that either the requested action is not allowed (implicitly denied) or that the action is explicitly denied by the permissions boundary. In both of these cases, the action is not allowed, regardless of the identity-based policy.

EvalDecisionDetails -> (map)

Additional details about the results of the cross-account evaluation decision. This parameter is populated for only cross-account simulations. It contains a brief summary of how each policy type contributes to the final evaluation decision.

If the simulation evaluates policies within the same account and includes a resource ARN, then the parameter is present but the response is empty. If the simulation evaluates policies within the same account and specifies all resources (`*` ), then the parameter is not returned.

When you make a cross-account request, Amazon Web Services evaluates the request in the trusting account and the trusted account. The request is allowed only if both evaluations return `true` . For more information about how policies are evaluated, see [Evaluating policies within a single account](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html#policy-eval-basics) .

If an Organizations SCP included in the evaluation denies access, the simulation ends. In this case, policy evaluation does not proceed any further and this parameter is not returned.

key -> (string)

value -> (string)

ResourceSpecificResults -> (list)

The individual results of the simulation of the API operation specified in EvalActionName on each resource.

(structure)

Contains the result of the simulation of a single API operation call on a single resource.

This data type is used by a member of the  EvaluationResult data type.

EvalResourceName -> (string)

The name of the simulated resource, in Amazon Resource Name (ARN) format.

EvalResourceDecision -> (string)

The result of the simulation of the simulated API operation on the resource specified in `EvalResourceName` .

MatchedStatements -> (list)

A list of the statements in the input policies that determine the result for this part of the simulation. Remember that even if multiple statements allow the operation on the resource, if *any* statement denies that operation, then the explicit deny overrides any allow. In addition, the deny statement is the only entry included in the result.

(structure)

Contains a reference to a `Statement` element in a policy document that determines the result of the simulation.

This data type is used by the `MatchedStatements` member of the ``  EvaluationResult `` type.

SourcePolicyId -> (string)

The identifier of the policy that was provided as an input.

SourcePolicyType -> (string)

The type of the policy.

StartPosition -> (structure)

The row and column of the beginning of the `Statement` in an IAM policy.

Line -> (integer)

The line containing the specified position in the document.

Column -> (integer)

The column in the line containing the specified position in the document.

EndPosition -> (structure)

The row and column of the end of a `Statement` in an IAM policy.

Line -> (integer)

The line containing the specified position in the document.

Column -> (integer)

The column in the line containing the specified position in the document.

MissingContextValues -> (list)

A list of context keys that are required by the included input policies but that were not provided by one of the input parameters. This list is used when a list of ARNs is included in the `ResourceArns` parameter instead of â*â. If you do not specify individual resources, by setting `ResourceArns` to â*â or by not including the `ResourceArns` parameter, then any missing context values are instead included under the `EvaluationResults` section. To discover the context keys used by a set of policies, you can call  GetContextKeysForCustomPolicy or  GetContextKeysForPrincipalPolicy .

(string)

EvalDecisionDetails -> (map)

Additional details about the results of the evaluation decision on a single resource. This parameter is returned only for cross-account simulations. This parameter explains how each policy type contributes to the resource-specific evaluation decision.

key -> (string)

value -> (string)

PermissionsBoundaryDecisionDetail -> (structure)

Contains information about the effect that a permissions boundary has on a policy simulation when that boundary is applied to an IAM entity.

AllowedByPermissionsBoundary -> (boolean)

Specifies whether an action is allowed by a permissions boundary that is applied to an IAM entity (user or role). A value of `true` means that the permissions boundary does not deny the action. This means that the policy includes an `Allow` statement that matches the request. In this case, if an identity-based policy also allows the action, the request is allowed. A value of `false` means that either the requested action is not allowed (implicitly denied) or that the action is explicitly denied by the permissions boundary. In both of these cases, the action is not allowed, regardless of the identity-based policy.

IsTruncated -> (boolean)

A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the `Marker` request parameter to retrieve more items. Note that IAM might return fewer than the `MaxItems` number of results even when there are more results available. We recommend that you check `IsTruncated` after every call to ensure that you receive all your results.

Marker -> (string)

When `IsTruncated` is `true` , this element is present and contains the value to use for the `Marker` parameter in a subsequent pagination request.