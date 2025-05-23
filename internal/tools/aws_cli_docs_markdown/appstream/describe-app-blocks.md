# describe-app-blocksÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-app-blocks.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-app-blocks.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appstream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/index.html#cli-aws-appstream) ]

# describe-app-blocks

## Description

Retrieves a list that describes one or more app blocks.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeAppBlocks)

## Synopsis

```
describe-app-blocks
[--arns <value>]
[--next-token <value>]
[--max-results <value>]
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

`--arns` (list)

The ARNs of the app blocks.

(string)

Syntax:

```
"string" "string" ...
```

`--next-token` (string)

The pagination token used to retrieve the next page of results for this operation.

`--max-results` (integer)

The maximum size of each page of results.

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

AppBlocks -> (list)

The app blocks in the list.

(structure)

Describes an app block.

App blocks are an Amazon AppStream 2.0 resource that stores the details about the virtual hard disk in an S3 bucket. It also stores the setup script with details about how to mount the virtual hard disk. The virtual hard disk includes the application binaries and other files necessary to launch your applications. Multiple applications can be assigned to a single app block.

This is only supported for Elastic fleets.

Name -> (string)

The name of the app block.

Arn -> (string)

The ARN of the app block.

Description -> (string)

The description of the app block.

DisplayName -> (string)

The display name of the app block.

SourceS3Location -> (structure)

The source S3 location of the app block.

S3Bucket -> (string)

The S3 bucket of the S3 object.

S3Key -> (string)

The S3 key of the S3 object.

This is required when used for the following:

- IconS3Location (Actions: CreateApplication and UpdateApplication)
- SessionScriptS3Location (Actions: CreateFleet and UpdateFleet)
- ScriptDetails (Actions: CreateAppBlock)
- SourceS3Location when creating an app block with `CUSTOM` PackagingType (Actions: CreateAppBlock)
- SourceS3Location when creating an app block with `APPSTREAM2` PackagingType, and using an existing application package (VHD file). In this case, `S3Key` refers to the VHD file. If a new application package is required, then `S3Key` is not required. (Actions: CreateAppBlock)

SetupScriptDetails -> (structure)

The setup script details of the app block.

This only applies to app blocks with PackagingType `CUSTOM` .

ScriptS3Location -> (structure)

The S3 object location for the script.

S3Bucket -> (string)

The S3 bucket of the S3 object.

S3Key -> (string)

The S3 key of the S3 object.

This is required when used for the following:

- IconS3Location (Actions: CreateApplication and UpdateApplication)
- SessionScriptS3Location (Actions: CreateFleet and UpdateFleet)
- ScriptDetails (Actions: CreateAppBlock)
- SourceS3Location when creating an app block with `CUSTOM` PackagingType (Actions: CreateAppBlock)
- SourceS3Location when creating an app block with `APPSTREAM2` PackagingType, and using an existing application package (VHD file). In this case, `S3Key` refers to the VHD file. If a new application package is required, then `S3Key` is not required. (Actions: CreateAppBlock)

ExecutablePath -> (string)

The run path for the script.

ExecutableParameters -> (string)

The runtime parameters passed to the run path for the script.

TimeoutInSeconds -> (integer)

The run timeout, in seconds, for the script.

CreatedTime -> (timestamp)

The created time of the app block.

PostSetupScriptDetails -> (structure)

The post setup script details of the app block.

This only applies to app blocks with PackagingType `APPSTREAM2` .

ScriptS3Location -> (structure)

The S3 object location for the script.

S3Bucket -> (string)

The S3 bucket of the S3 object.

S3Key -> (string)

The S3 key of the S3 object.

This is required when used for the following:

- IconS3Location (Actions: CreateApplication and UpdateApplication)
- SessionScriptS3Location (Actions: CreateFleet and UpdateFleet)
- ScriptDetails (Actions: CreateAppBlock)
- SourceS3Location when creating an app block with `CUSTOM` PackagingType (Actions: CreateAppBlock)
- SourceS3Location when creating an app block with `APPSTREAM2` PackagingType, and using an existing application package (VHD file). In this case, `S3Key` refers to the VHD file. If a new application package is required, then `S3Key` is not required. (Actions: CreateAppBlock)

ExecutablePath -> (string)

The run path for the script.

ExecutableParameters -> (string)

The runtime parameters passed to the run path for the script.

TimeoutInSeconds -> (integer)

The run timeout, in seconds, for the script.

PackagingType -> (string)

The packaging type of the app block.

State -> (string)

The state of the app block.

An app block with AppStream 2.0 packaging will be in the `INACTIVE` state if no application package (VHD) is assigned to it. After an application package (VHD) is created by an app block builder for an app block, it becomes `ACTIVE` .

Custom app blocks are always in the `ACTIVE` state and no action is required to use them.

AppBlockErrors -> (list)

The errors of the app block.

(structure)

The error details.

ErrorCode -> (string)

The error code.

ErrorMessage -> (string)

The error message.

NextToken -> (string)

The pagination token used to retrieve the next page of results for this operation.