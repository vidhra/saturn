# describe-workflowÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-workflow.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-workflow.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transfer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/index.html#cli-aws-transfer) ]

# describe-workflow

## Description

Describes the specified workflow.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/DescribeWorkflow)

## Synopsis

```
describe-workflow
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

Workflow -> (structure)

The structure that contains the details of the workflow.

Arn -> (string)

Specifies the unique Amazon Resource Name (ARN) for the workflow.

Description -> (string)

Specifies the text description for the workflow.

Steps -> (list)

Specifies the details for the steps that are in the specified workflow.

(structure)

The basic building block of a workflow.

Type -> (string)

Currently, the following step types are supported.

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-workflow.html#id1)`COPY` ** - Copy the file to another location.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-workflow.html#id3)`CUSTOM` ** - Perform a custom step with an Lambda function target.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-workflow.html#id5)`DECRYPT` ** - Decrypt a file that was encrypted before it was uploaded.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-workflow.html#id7)`DELETE` ** - Delete the file.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-workflow.html#id9)`TAG` ** - Add a tag to the file.

CopyStepDetails -> (structure)

Details for a step that performs a file copy.

Consists of the following values:

- A description
- An Amazon S3 location for the destination of the file copy.
- A flag that indicates whether to overwrite an existing file of the same name. The default is `FALSE` .

Name -> (string)

The name of the step, used as an identifier.

DestinationFileLocation -> (structure)

Specifies the location for the file being copied. Use `${Transfer:UserName}` or `${Transfer:UploadDate}` in this field to parametrize the destination prefix by username or uploaded date.

- Set the value of `DestinationFileLocation` to `${Transfer:UserName}` to copy uploaded files to an Amazon S3 bucket that is prefixed with the name of the Transfer Family user that uploaded the file.
- Set the value of `DestinationFileLocation` to `${Transfer:UploadDate}` to copy uploaded files to an Amazon S3 bucket that is prefixed with the date of the upload.

### Note

The system resolves `UploadDate` to a date format of *YYYY-MM-DD* , based on the date the file is uploaded in UTC.

S3FileLocation -> (structure)

Specifies the details for the Amazon S3 file thatâs being copied or decrypted.

Bucket -> (string)

Specifies the S3 bucket for the customer input file.

Key -> (string)

The name assigned to the file when it was created in Amazon S3. You use the object key to retrieve the object.

EfsFileLocation -> (structure)

Specifies the details for the Amazon Elastic File System (Amazon EFS) file thatâs being decrypted.

FileSystemId -> (string)

The identifier of the file system, assigned by Amazon EFS.

Path -> (string)

The pathname for the folder being used by a workflow.

OverwriteExisting -> (string)

A flag that indicates whether to overwrite an existing file of the same name. The default is `FALSE` .

If the workflow is processing a file that has the same name as an existing file, the behavior is as follows:

- If `OverwriteExisting` is `TRUE` , the existing file is replaced with the file being processed.
- If `OverwriteExisting` is `FALSE` , nothing happens, and the workflow processing stops.

SourceFileLocation -> (string)

Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.

- To use the previous file as the input, enter `${previous.file}` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.
- To use the originally uploaded file location as input for this step, enter `${original.file}` .

CustomStepDetails -> (structure)

Details for a step that invokes an Lambda function.

Consists of the Lambda functionâs name, target, and timeout (in seconds).

Name -> (string)

The name of the step, used as an identifier.

Target -> (string)

The ARN for the Lambda function that is being called.

TimeoutSeconds -> (integer)

Timeout, in seconds, for the step.

SourceFileLocation -> (string)

Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.

- To use the previous file as the input, enter `${previous.file}` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.
- To use the originally uploaded file location as input for this step, enter `${original.file}` .

DeleteStepDetails -> (structure)

Details for a step that deletes the file.

Name -> (string)

The name of the step, used as an identifier.

SourceFileLocation -> (string)

Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.

- To use the previous file as the input, enter `${previous.file}` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.
- To use the originally uploaded file location as input for this step, enter `${original.file}` .

TagStepDetails -> (structure)

Details for a step that creates one or more tags.

You specify one or more tags. Each tag contains a key-value pair.

Name -> (string)

The name of the step, used as an identifier.

Tags -> (list)

Array that contains from 1 to 10 key/value pairs.

(structure)

Specifies the key-value pair that are assigned to a file during the execution of a Tagging step.

Key -> (string)

The name assigned to the tag that you create.

Value -> (string)

The value that corresponds to the key.

SourceFileLocation -> (string)

Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.

- To use the previous file as the input, enter `${previous.file}` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.
- To use the originally uploaded file location as input for this step, enter `${original.file}` .

DecryptStepDetails -> (structure)

Details for a step that decrypts an encrypted file.

Consists of the following values:

- A descriptive name
- An Amazon S3 or Amazon Elastic File System (Amazon EFS) location for the source file to decrypt.
- An S3 or Amazon EFS location for the destination of the file decryption.
- A flag that indicates whether to overwrite an existing file of the same name. The default is `FALSE` .
- The type of encryption thatâs used. Currently, only PGP encryption is supported.

Name -> (string)

The name of the step, used as an identifier.

Type -> (string)

The type of encryption used. Currently, this value must be `PGP` .

SourceFileLocation -> (string)

Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.

- To use the previous file as the input, enter `${previous.file}` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.
- To use the originally uploaded file location as input for this step, enter `${original.file}` .

OverwriteExisting -> (string)

A flag that indicates whether to overwrite an existing file of the same name. The default is `FALSE` .

If the workflow is processing a file that has the same name as an existing file, the behavior is as follows:

- If `OverwriteExisting` is `TRUE` , the existing file is replaced with the file being processed.
- If `OverwriteExisting` is `FALSE` , nothing happens, and the workflow processing stops.

DestinationFileLocation -> (structure)

Specifies the location for the file being decrypted. Use `${Transfer:UserName}` or `${Transfer:UploadDate}` in this field to parametrize the destination prefix by username or uploaded date.

- Set the value of `DestinationFileLocation` to `${Transfer:UserName}` to decrypt uploaded files to an Amazon S3 bucket that is prefixed with the name of the Transfer Family user that uploaded the file.
- Set the value of `DestinationFileLocation` to `${Transfer:UploadDate}` to decrypt uploaded files to an Amazon S3 bucket that is prefixed with the date of the upload.

### Note

The system resolves `UploadDate` to a date format of *YYYY-MM-DD* , based on the date the file is uploaded in UTC.

S3FileLocation -> (structure)

Specifies the details for the Amazon S3 file thatâs being copied or decrypted.

Bucket -> (string)

Specifies the S3 bucket for the customer input file.

Key -> (string)

The name assigned to the file when it was created in Amazon S3. You use the object key to retrieve the object.

EfsFileLocation -> (structure)

Specifies the details for the Amazon Elastic File System (Amazon EFS) file thatâs being decrypted.

FileSystemId -> (string)

The identifier of the file system, assigned by Amazon EFS.

Path -> (string)

The pathname for the folder being used by a workflow.

OnExceptionSteps -> (list)

Specifies the steps (actions) to take if errors are encountered during execution of the workflow.

(structure)

The basic building block of a workflow.

Type -> (string)

Currently, the following step types are supported.

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-workflow.html#id11)`COPY` ** - Copy the file to another location.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-workflow.html#id13)`CUSTOM` ** - Perform a custom step with an Lambda function target.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-workflow.html#id15)`DECRYPT` ** - Decrypt a file that was encrypted before it was uploaded.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-workflow.html#id17)`DELETE` ** - Delete the file.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-workflow.html#id19)`TAG` ** - Add a tag to the file.

CopyStepDetails -> (structure)

Details for a step that performs a file copy.

Consists of the following values:

- A description
- An Amazon S3 location for the destination of the file copy.
- A flag that indicates whether to overwrite an existing file of the same name. The default is `FALSE` .

Name -> (string)

The name of the step, used as an identifier.

DestinationFileLocation -> (structure)

Specifies the location for the file being copied. Use `${Transfer:UserName}` or `${Transfer:UploadDate}` in this field to parametrize the destination prefix by username or uploaded date.

- Set the value of `DestinationFileLocation` to `${Transfer:UserName}` to copy uploaded files to an Amazon S3 bucket that is prefixed with the name of the Transfer Family user that uploaded the file.
- Set the value of `DestinationFileLocation` to `${Transfer:UploadDate}` to copy uploaded files to an Amazon S3 bucket that is prefixed with the date of the upload.

### Note

The system resolves `UploadDate` to a date format of *YYYY-MM-DD* , based on the date the file is uploaded in UTC.

S3FileLocation -> (structure)

Specifies the details for the Amazon S3 file thatâs being copied or decrypted.

Bucket -> (string)

Specifies the S3 bucket for the customer input file.

Key -> (string)

The name assigned to the file when it was created in Amazon S3. You use the object key to retrieve the object.

EfsFileLocation -> (structure)

Specifies the details for the Amazon Elastic File System (Amazon EFS) file thatâs being decrypted.

FileSystemId -> (string)

The identifier of the file system, assigned by Amazon EFS.

Path -> (string)

The pathname for the folder being used by a workflow.

OverwriteExisting -> (string)

A flag that indicates whether to overwrite an existing file of the same name. The default is `FALSE` .

If the workflow is processing a file that has the same name as an existing file, the behavior is as follows:

- If `OverwriteExisting` is `TRUE` , the existing file is replaced with the file being processed.
- If `OverwriteExisting` is `FALSE` , nothing happens, and the workflow processing stops.

SourceFileLocation -> (string)

Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.

- To use the previous file as the input, enter `${previous.file}` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.
- To use the originally uploaded file location as input for this step, enter `${original.file}` .

CustomStepDetails -> (structure)

Details for a step that invokes an Lambda function.

Consists of the Lambda functionâs name, target, and timeout (in seconds).

Name -> (string)

The name of the step, used as an identifier.

Target -> (string)

The ARN for the Lambda function that is being called.

TimeoutSeconds -> (integer)

Timeout, in seconds, for the step.

SourceFileLocation -> (string)

Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.

- To use the previous file as the input, enter `${previous.file}` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.
- To use the originally uploaded file location as input for this step, enter `${original.file}` .

DeleteStepDetails -> (structure)

Details for a step that deletes the file.

Name -> (string)

The name of the step, used as an identifier.

SourceFileLocation -> (string)

Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.

- To use the previous file as the input, enter `${previous.file}` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.
- To use the originally uploaded file location as input for this step, enter `${original.file}` .

TagStepDetails -> (structure)

Details for a step that creates one or more tags.

You specify one or more tags. Each tag contains a key-value pair.

Name -> (string)

The name of the step, used as an identifier.

Tags -> (list)

Array that contains from 1 to 10 key/value pairs.

(structure)

Specifies the key-value pair that are assigned to a file during the execution of a Tagging step.

Key -> (string)

The name assigned to the tag that you create.

Value -> (string)

The value that corresponds to the key.

SourceFileLocation -> (string)

Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.

- To use the previous file as the input, enter `${previous.file}` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.
- To use the originally uploaded file location as input for this step, enter `${original.file}` .

DecryptStepDetails -> (structure)

Details for a step that decrypts an encrypted file.

Consists of the following values:

- A descriptive name
- An Amazon S3 or Amazon Elastic File System (Amazon EFS) location for the source file to decrypt.
- An S3 or Amazon EFS location for the destination of the file decryption.
- A flag that indicates whether to overwrite an existing file of the same name. The default is `FALSE` .
- The type of encryption thatâs used. Currently, only PGP encryption is supported.

Name -> (string)

The name of the step, used as an identifier.

Type -> (string)

The type of encryption used. Currently, this value must be `PGP` .

SourceFileLocation -> (string)

Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.

- To use the previous file as the input, enter `${previous.file}` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.
- To use the originally uploaded file location as input for this step, enter `${original.file}` .

OverwriteExisting -> (string)

A flag that indicates whether to overwrite an existing file of the same name. The default is `FALSE` .

If the workflow is processing a file that has the same name as an existing file, the behavior is as follows:

- If `OverwriteExisting` is `TRUE` , the existing file is replaced with the file being processed.
- If `OverwriteExisting` is `FALSE` , nothing happens, and the workflow processing stops.

DestinationFileLocation -> (structure)

Specifies the location for the file being decrypted. Use `${Transfer:UserName}` or `${Transfer:UploadDate}` in this field to parametrize the destination prefix by username or uploaded date.

- Set the value of `DestinationFileLocation` to `${Transfer:UserName}` to decrypt uploaded files to an Amazon S3 bucket that is prefixed with the name of the Transfer Family user that uploaded the file.
- Set the value of `DestinationFileLocation` to `${Transfer:UploadDate}` to decrypt uploaded files to an Amazon S3 bucket that is prefixed with the date of the upload.

### Note

The system resolves `UploadDate` to a date format of *YYYY-MM-DD* , based on the date the file is uploaded in UTC.

S3FileLocation -> (structure)

Specifies the details for the Amazon S3 file thatâs being copied or decrypted.

Bucket -> (string)

Specifies the S3 bucket for the customer input file.

Key -> (string)

The name assigned to the file when it was created in Amazon S3. You use the object key to retrieve the object.

EfsFileLocation -> (structure)

Specifies the details for the Amazon Elastic File System (Amazon EFS) file thatâs being decrypted.

FileSystemId -> (string)

The identifier of the file system, assigned by Amazon EFS.

Path -> (string)

The pathname for the folder being used by a workflow.

WorkflowId -> (string)

A unique identifier for the workflow.

Tags -> (list)

Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.

(structure)

Creates a key-value pair for a specific resource. Tags are metadata that you can use to search for and group a resource for various purposes. You can apply tags to servers, users, and roles. A tag key can take more than one value. For example, to group servers for accounting purposes, you might create a tag called `Group` and assign the values `Research` and `Accounting` to that group.

Key -> (string)

The name assigned to the tag that you create.

Value -> (string)

Contains one or more values that you assigned to the key name you create.