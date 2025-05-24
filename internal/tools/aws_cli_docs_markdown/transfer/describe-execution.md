# describe-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transfer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/index.html#cli-aws-transfer) ]

# describe-execution

## Description

You can use `DescribeExecution` to check the details of the execution of the specified workflow.

### Note

This API call only returns details for in-progress workflows.

If you provide an ID for an execution that is not in progress, or if the execution doesnât match the specified workflow ID, you receive a `ResourceNotFound` exception.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/DescribeExecution)

## Synopsis

```
describe-execution
--execution-id <value>
--workflow-id <value>
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

`--execution-id` (string)

A unique identifier for the execution of a workflow.

`--workflow-id` (string)

A unique identifier for the workflow.

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

WorkflowId -> (string)

A unique identifier for the workflow.

Execution -> (structure)

The structure that contains the details of the workflowâ execution.

ExecutionId -> (string)

A unique identifier for the execution of a workflow.

InitialFileLocation -> (structure)

A structure that describes the Amazon S3 or EFS file location. This is the file location when the execution begins: if the file is being copied, this is the initial (as opposed to destination) file location.

S3FileLocation -> (structure)

Specifies the S3 details for the file being used, such as bucket, ETag, and so forth.

Bucket -> (string)

Specifies the S3 bucket that contains the file being used.

Key -> (string)

The name assigned to the file when it was created in Amazon S3. You use the object key to retrieve the object.

VersionId -> (string)

Specifies the file version.

Etag -> (string)

The entity tag is a hash of the object. The ETag reflects changes only to the contents of an object, not its metadata.

EfsFileLocation -> (structure)

Specifies the Amazon EFS identifier and the path for the file being used.

FileSystemId -> (string)

The identifier of the file system, assigned by Amazon EFS.

Path -> (string)

The pathname for the folder being used by a workflow.

ServiceMetadata -> (structure)

A container object for the session details that are associated with a workflow.

UserDetails -> (structure)

The Server ID (`ServerId` ), Session ID (`SessionId` ) and user (`UserName` ) make up the `UserDetails` .

UserName -> (string)

A unique string that identifies a Transfer Family user associated with a server.

ServerId -> (string)

The system-assigned unique identifier for a Transfer server instance.

SessionId -> (string)

The system-assigned unique identifier for a session that corresponds to the workflow.

ExecutionRole -> (string)

The IAM role associated with the execution.

LoggingConfiguration -> (structure)

The IAM logging role associated with the execution.

LoggingRole -> (string)

The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a server to turn on Amazon CloudWatch logging for Amazon S3 or Amazon EFS events. When set, you can view user activity in your CloudWatch logs.

LogGroupName -> (string)

The name of the CloudWatch logging group for the Transfer Family server to which this workflow belongs.

PosixProfile -> (structure)

The full POSIX identity, including user ID (`Uid` ), group ID (`Gid` ), and any secondary groups IDs (`SecondaryGids` ), that controls your usersâ access to your Amazon EFS file systems. The POSIX permissions that are set on files and directories in your file system determine the level of access your users get when transferring files into and out of your Amazon EFS file systems.

Uid -> (long)

The POSIX user ID used for all EFS operations by this user.

Gid -> (long)

The POSIX group ID used for all EFS operations by this user.

SecondaryGids -> (list)

The secondary POSIX group IDs used for all EFS operations by this user.

(long)

Status -> (string)

The status is one of the execution. Can be in progress, completed, exception encountered, or handling the exception.

Results -> (structure)

A structure that describes the execution results. This includes a list of the steps along with the details of each step, error type and message (if any), and the `OnExceptionSteps` structure.

Steps -> (list)

Specifies the details for the steps that are in the specified workflow.

(structure)

Specifies the following details for the step: error (if any), outputs (if any), and the step type.

StepType -> (string)

One of the available step types.

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-execution.html#id1)`COPY` ** - Copy the file to another location.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-execution.html#id3)`CUSTOM` ** - Perform a custom step with an Lambda function target.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-execution.html#id5)`DECRYPT` ** - Decrypt a file that was encrypted before it was uploaded.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-execution.html#id7)`DELETE` ** - Delete the file.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-execution.html#id9)`TAG` ** - Add a tag to the file.

Outputs -> (string)

The values for the key/value pair applied as a tag to the file. Only applicable if the step type is `TAG` .

Error -> (structure)

Specifies the details for an error, if it occurred during execution of the specified workflow step.

Type -> (string)

Specifies the error type.

- `ALREADY_EXISTS` : occurs for a copy step, if the overwrite option is not selected and a file with the same name already exists in the target location.
- `BAD_REQUEST` : a general bad request: for example, a step that attempts to tag an EFS file returns `BAD_REQUEST` , as only S3 files can be tagged.
- `CUSTOM_STEP_FAILED` : occurs when the custom step provided a callback that indicates failure.
- `INTERNAL_SERVER_ERROR` : a catch-all error that can occur for a variety of reasons.
- `NOT_FOUND` : occurs when a requested entity, for example a source file for a copy step, does not exist.
- `PERMISSION_DENIED` : occurs if your policy does not contain the correct permissions to complete one or more of the steps in the workflow.
- `TIMEOUT` : occurs when the execution times out.

### Note

You can set the `TimeoutSeconds` for a custom step, anywhere from 1 second to 1800 seconds (30 minutes).

- `THROTTLED` : occurs if you exceed the new execution refill rate of one workflow per second.

Message -> (string)

Specifies the descriptive message that corresponds to the `ErrorType` .

OnExceptionSteps -> (list)

Specifies the steps (actions) to take if errors are encountered during execution of the workflow.

(structure)

Specifies the following details for the step: error (if any), outputs (if any), and the step type.

StepType -> (string)

One of the available step types.

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-execution.html#id11)`COPY` ** - Copy the file to another location.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-execution.html#id13)`CUSTOM` ** - Perform a custom step with an Lambda function target.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-execution.html#id15)`DECRYPT` ** - Decrypt a file that was encrypted before it was uploaded.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-execution.html#id17)`DELETE` ** - Delete the file.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-execution.html#id19)`TAG` ** - Add a tag to the file.

Outputs -> (string)

The values for the key/value pair applied as a tag to the file. Only applicable if the step type is `TAG` .

Error -> (structure)

Specifies the details for an error, if it occurred during execution of the specified workflow step.

Type -> (string)

Specifies the error type.

- `ALREADY_EXISTS` : occurs for a copy step, if the overwrite option is not selected and a file with the same name already exists in the target location.
- `BAD_REQUEST` : a general bad request: for example, a step that attempts to tag an EFS file returns `BAD_REQUEST` , as only S3 files can be tagged.
- `CUSTOM_STEP_FAILED` : occurs when the custom step provided a callback that indicates failure.
- `INTERNAL_SERVER_ERROR` : a catch-all error that can occur for a variety of reasons.
- `NOT_FOUND` : occurs when a requested entity, for example a source file for a copy step, does not exist.
- `PERMISSION_DENIED` : occurs if your policy does not contain the correct permissions to complete one or more of the steps in the workflow.
- `TIMEOUT` : occurs when the execution times out.

### Note

You can set the `TimeoutSeconds` for a custom step, anywhere from 1 second to 1800 seconds (30 minutes).

- `THROTTLED` : occurs if you exceed the new execution refill rate of one workflow per second.

Message -> (string)

Specifies the descriptive message that corresponds to the `ErrorType` .