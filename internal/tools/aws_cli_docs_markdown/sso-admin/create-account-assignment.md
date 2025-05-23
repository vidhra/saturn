# create-account-assignmentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-account-assignment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-account-assignment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sso-admin](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/index.html#cli-aws-sso-admin) ]

# create-account-assignment

## Description

Assigns access to a principal for a specified Amazon Web Services account using a specified permission set.

### Note

The term *principal* here refers to a user or group that is defined in IAM Identity Center.

### Note

As part of a successful `CreateAccountAssignment` call, the specified permission set will automatically be provisioned to the account in the form of an IAM policy. That policy is attached to the IAM role created in IAM Identity Center. If the permission set is subsequently updated, the corresponding IAM policies attached to roles in your accounts will not be updated automatically. In this case, you must call ``  ProvisionPermissionSet `` to make these updates.

### Note

After a successful response, call `DescribeAccountAssignmentCreationStatus` to describe the status of an assignment creation request.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sso-admin-2020-07-20/CreateAccountAssignment)

## Synopsis

```
create-account-assignment
--instance-arn <value>
--target-id <value>
--target-type <value>
--permission-set-arn <value>
--principal-type <value>
--principal-id <value>
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

`--instance-arn` (string)

The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://awscli.amazonaws.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

`--target-id` (string)

TargetID is an Amazon Web Services account identifier, (For example, 123456789012).

`--target-type` (string)

The entity type for which the assignment will be created.

Possible values:

- `AWS_ACCOUNT`

`--permission-set-arn` (string)

The ARN of the permission set that the admin wants to grant the principal access to.

`--principal-type` (string)

The entity type for which the assignment will be created.

Possible values:

- `USER`
- `GROUP`

`--principal-id` (string)

An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the [IAM Identity Center Identity Store API Reference](https://awscli.amazonaws.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html) .

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

## Output

AccountAssignmentCreationStatus -> (structure)

The status object for the account assignment creation operation.

Status -> (string)

The status of the permission set provisioning process.

RequestId -> (string)

The identifier for tracking the request operation that is generated by the universally unique identifier (UUID) workflow.

FailureReason -> (string)

The message that contains an error or exception in case of an operation failure.

TargetId -> (string)

TargetID is an Amazon Web Services account identifier, (For example, 123456789012).

TargetType -> (string)

The entity type for which the assignment will be created.

PermissionSetArn -> (string)

The ARN of the permission set. For more information about ARNs, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://awscli.amazonaws.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

PrincipalType -> (string)

The entity type for which the assignment will be created.

PrincipalId -> (string)

An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the [IAM Identity Center Identity Store API Reference](https://awscli.amazonaws.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html) .

CreatedDate -> (timestamp)

The date that the permission set was created.