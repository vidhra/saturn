# update-applicationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/update-application.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/update-application.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appstream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/index.html#cli-aws-appstream) ]

# update-application

## Description

Updates the specified application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/UpdateApplication)

## Synopsis

```
update-application
--name <value>
[--display-name <value>]
[--description <value>]
[--icon-s3-location <value>]
[--launch-path <value>]
[--working-directory <value>]
[--launch-parameters <value>]
[--app-block-arn <value>]
[--attributes-to-delete <value>]
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

`--name` (string)

The name of the application. This name is visible to users when display name is not specified.

`--display-name` (string)

The display name of the application. This name is visible to users in the application catalog.

`--description` (string)

The description of the application.

`--icon-s3-location` (structure)

The icon S3 location of the application.

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

Shorthand Syntax:

```
S3Bucket=string,S3Key=string
```

JSON Syntax:

```
{
  "S3Bucket": "string",
  "S3Key": "string"
}
```

`--launch-path` (string)

The launch path of the application.

`--working-directory` (string)

The working directory of the application.

`--launch-parameters` (string)

The launch parameters of the application.

`--app-block-arn` (string)

The ARN of the app block.

`--attributes-to-delete` (list)

The attributes to delete for an application.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  LAUNCH_PARAMETERS
  WORKING_DIRECTORY
```

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

Application -> (structure)

Describes an application in the application catalog.

Name -> (string)

The name of the application.

DisplayName -> (string)

The application name to display.

IconURL -> (string)

The URL for the application icon. This URL might be time-limited.

LaunchPath -> (string)

The path to the application executable in the instance.

LaunchParameters -> (string)

The arguments that are passed to the application at launch.

Enabled -> (boolean)

If there is a problem, the application can be disabled after image creation.

Metadata -> (map)

Additional attributes that describe the application.

key -> (string)

value -> (string)

WorkingDirectory -> (string)

The working directory for the application.

Description -> (string)

The description of the application.

Arn -> (string)

The ARN of the application.

AppBlockArn -> (string)

The app block ARN of the application.

IconS3Location -> (structure)

The S3 location of the application icon.

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

Platforms -> (list)

The platforms on which the application can run.

(string)

InstanceFamilies -> (list)

The instance families for the application.

(string)

CreatedTime -> (timestamp)

The time at which the application was created within the app block.