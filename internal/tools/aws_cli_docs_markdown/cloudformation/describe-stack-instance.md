# describe-stack-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# describe-stack-instance

## Description

Returns the stack instance thatâs associated with the specified StackSet, Amazon Web Services account, and Amazon Web Services Region.

For a list of stack instances that are associated with a specific StackSet, use  ListStackInstances .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStackInstance)

## Synopsis

```
describe-stack-instance
--stack-set-name <value>
--stack-instance-account <value>
--stack-instance-region <value>
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

The name or the unique stack ID of the stack set that you want to get stack instance information for.

`--stack-instance-account` (string)

The ID of an Amazon Web Services account thatâs associated with this stack instance.

`--stack-instance-region` (string)

The name of a Region thatâs associated with this stack instance.

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

**To describe a stack instance**

The following command describes an instance of the specified stack set in the specified account and Region. The stack set is in the current region and account, and the instance is in the `us-west-2` region in account `123456789012`.:

```
aws cloudformation describe-stack-instance \
    --stack-set-name my-stack-set \
    --stack-instance-account 123456789012 \
    --stack-instance-region us-west-2
```

Output:

```
{
    "StackInstance": {
        "StackSetId": "enable-config:296a3360-xmpl-40af-be78-9341e95bf743",
        "Region": "us-west-2",
        "Account": "123456789012",
        "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/StackSet-enable-config-e6cac20f-xmpl-46e9-8314-53e0d4591532/4287f9a0-e615-xmpl-894a-12b31d3117be",
        "ParameterOverrides": [],
        "Status": "OUTDATED",
        "StatusReason": "ResourceLogicalId:ConfigBucket, ResourceType:AWS::S3::Bucket, ResourceStatusReason:You have attempted to create more buckets than allowed (Service: Amazon S3; Status Code: 400; Error Code: TooManyBuckets; Request ID: F7F21CXMPL580224; S3 Extended Request ID: egd/Fdt89BXMPLyiqbMNljVk55Yqqvi3NYW2nKLUVWhUGEhNfCmZdyj967lhriaG/dWMobSO40o=)."
    }
}
```

## Output

StackInstance -> (structure)

The stack instance that matches the specified request parameters.

StackSetId -> (string)

The name or unique ID of the stack set that the stack instance is associated with.

Region -> (string)

The name of the Amazon Web Services Region that the stack instance is associated with.

Account -> (string)

[Self-managed permissions] The name of the Amazon Web Services account that the stack instance is associated with.

StackId -> (string)

The ID of the stack instance.

ParameterOverrides -> (list)

A list of parameters from the stack set template whose values have been overridden in this stack instance.

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

Status -> (string)

The status of the stack instance, in terms of its synchronization with its associated stack set.

- `INOPERABLE` : A `DeleteStackInstances` operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further `UpdateStackSet` operations. You might need to perform a `DeleteStackInstances` operation, with `RetainStacks` set to `true` , to delete the stack instance, and then delete the stack manually. `INOPERABLE` can be returned here when the cause is a failed import. If itâs due to a failed import, the operation can be retried once the failures are fixed. To see if this is due to a failed import, look at the `DetailedStatus` member in the `StackInstanceSummary` member that is a peer to this `Status` member.
- `OUTDATED` : The stack isnât currently up to date with the stack set because:
- The associated stack failed during a `CreateStackSet` or `UpdateStackSet` operation.
- The stack was part of a `CreateStackSet` or `UpdateStackSet` operation that failed or was stopped before the stack was created or updated.
- `CURRENT` : The stack is currently up to date with the stack set.

StackInstanceStatus -> (structure)

The detailed status of the stack instance.

DetailedStatus -> (string)

- `CANCELLED` : The operation in the specified account and Region has been canceled. This is either because a user has stopped the stack set operation, or because the failure tolerance of the stack set operation has been exceeded.
- `FAILED` : The operation in the specified account and Region failed. If the stack set operation fails in enough accounts within a Region, the failure tolerance for the stack set operation as a whole might be exceeded.
- `FAILED_IMPORT` : The import of the stack instance in the specified account and Region failed and left the stack in an unstable state. Once the issues causing the failure are fixed, the import operation can be retried. If enough stack set operations fail in enough accounts within a Region, the failure tolerance for the stack set operation as a whole might be exceeded.
- `INOPERABLE` : A `DeleteStackInstances` operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further `UpdateStackSet` operations. You might need to perform a `DeleteStackInstances` operation, with `RetainStacks` set to `true` , to delete the stack instance, and then delete the stack manually.
- `PENDING` : The operation in the specified account and Region has yet to start.
- `RUNNING` : The operation in the specified account and Region is currently in progress.
- `SKIPPED_SUSPENDED_ACCOUNT` : The operation in the specified account and Region has been skipped because the account was suspended at the time of the operation.
- `SUCCEEDED` : The operation in the specified account and Region completed successfully.

StatusReason -> (string)

The explanation for the specific status code thatâs assigned to this stack instance.

OrganizationalUnitId -> (string)

[Service-managed permissions] The organization root ID or organizational unit (OU) IDs that you specified for [DeploymentTargets](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeploymentTargets.html) .

DriftStatus -> (string)

Status of the stack instanceâs actual configuration compared to the expected template and parameter configuration of the stack set to which it belongs.

- `DRIFTED` : The stack differs from the expected template and parameter configuration of the stack set to which it belongs. A stack instance is considered to have drifted if one or more of the resources in the associated stack have drifted.
- `NOT_CHECKED` : CloudFormation hasnât checked if the stack instance differs from its expected stack set configuration.
- `IN_SYNC` : The stack instanceâs actual configuration matches its expected stack set configuration.
- `UNKNOWN` : This value is reserved for future use.

LastDriftCheckTimestamp -> (timestamp)

Most recent time when CloudFormation performed a drift detection operation on the stack instance. This value will be `NULL` for any stack instance on which drift detection hasnât yet been performed.

LastOperationId -> (string)

The last unique ID of a StackSet operation performed on a stack instance.