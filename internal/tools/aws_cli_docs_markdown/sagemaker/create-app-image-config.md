# create-app-image-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-app-image-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-app-image-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-app-image-config

## Description

Creates a configuration for running a SageMaker AI image as a KernelGateway app. The configuration specifies the Amazon Elastic File System storage volume on the image, and a list of the kernels in the image.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateAppImageConfig)

## Synopsis

```
create-app-image-config
--app-image-config-name <value>
[--tags <value>]
[--kernel-gateway-image-config <value>]
[--jupyter-lab-app-image-config <value>]
[--code-editor-app-image-config <value>]
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

`--app-image-config-name` (string)

The name of the AppImageConfig. Must be unique to your account.

`--tags` (list)

A list of tags to apply to the AppImageConfig.

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--kernel-gateway-image-config` (structure)

The KernelGatewayImageConfig. You can only specify one image kernel in the AppImageConfig API. This kernel will be shown to users before the image starts. Once the image runs, all kernels are visible in JupyterLab.

KernelSpecs -> (list)

The specification of the Jupyter kernels in the image.

(structure)

The specification of a Jupyter kernel.

Name -> (string)

The name of the Jupyter kernel in the image. This value is case sensitive.

DisplayName -> (string)

The display name of the kernel.

FileSystemConfig -> (structure)

The Amazon Elastic File System storage configuration for a SageMaker AI image.

MountPath -> (string)

The path within the image to mount the userâs EFS home directory. The directory should be empty. If not specified, defaults to */home/sagemaker-user* .

DefaultUid -> (integer)

The default POSIX user ID (UID). If not specified, defaults to `1000` .

DefaultGid -> (integer)

The default POSIX group ID (GID). If not specified, defaults to `100` .

Shorthand Syntax:

```
KernelSpecs=[{Name=string,DisplayName=string},{Name=string,DisplayName=string}],FileSystemConfig={MountPath=string,DefaultUid=integer,DefaultGid=integer}
```

JSON Syntax:

```
{
  "KernelSpecs": [
    {
      "Name": "string",
      "DisplayName": "string"
    }
    ...
  ],
  "FileSystemConfig": {
    "MountPath": "string",
    "DefaultUid": integer,
    "DefaultGid": integer
  }
}
```

`--jupyter-lab-app-image-config` (structure)

The `JupyterLabAppImageConfig` . You can only specify one image kernel in the `AppImageConfig` API. This kernel is shown to users before the image starts. After the image runs, all kernels are visible in JupyterLab.

FileSystemConfig -> (structure)

The Amazon Elastic File System storage configuration for a SageMaker AI image.

MountPath -> (string)

The path within the image to mount the userâs EFS home directory. The directory should be empty. If not specified, defaults to */home/sagemaker-user* .

DefaultUid -> (integer)

The default POSIX user ID (UID). If not specified, defaults to `1000` .

DefaultGid -> (integer)

The default POSIX group ID (GID). If not specified, defaults to `100` .

ContainerConfig -> (structure)

The configuration used to run the application image container.

ContainerArguments -> (list)

The arguments for the container when youâre running the application.

(string)

ContainerEntrypoint -> (list)

The entrypoint used to run the application in the container.

(string)

ContainerEnvironmentVariables -> (map)

The environment variables to set in the container

key -> (string)

value -> (string)

Shorthand Syntax:

```
FileSystemConfig={MountPath=string,DefaultUid=integer,DefaultGid=integer},ContainerConfig={ContainerArguments=[string,string],ContainerEntrypoint=[string,string],ContainerEnvironmentVariables={KeyName1=string,KeyName2=string}}
```

JSON Syntax:

```
{
  "FileSystemConfig": {
    "MountPath": "string",
    "DefaultUid": integer,
    "DefaultGid": integer
  },
  "ContainerConfig": {
    "ContainerArguments": ["string", ...],
    "ContainerEntrypoint": ["string", ...],
    "ContainerEnvironmentVariables": {"string": "string"
      ...}
  }
}
```

`--code-editor-app-image-config` (structure)

The `CodeEditorAppImageConfig` . You can only specify one image kernel in the AppImageConfig API. This kernel is shown to users before the image starts. After the image runs, all kernels are visible in Code Editor.

FileSystemConfig -> (structure)

The Amazon Elastic File System storage configuration for a SageMaker AI image.

MountPath -> (string)

The path within the image to mount the userâs EFS home directory. The directory should be empty. If not specified, defaults to */home/sagemaker-user* .

DefaultUid -> (integer)

The default POSIX user ID (UID). If not specified, defaults to `1000` .

DefaultGid -> (integer)

The default POSIX group ID (GID). If not specified, defaults to `100` .

ContainerConfig -> (structure)

The configuration used to run the application image container.

ContainerArguments -> (list)

The arguments for the container when youâre running the application.

(string)

ContainerEntrypoint -> (list)

The entrypoint used to run the application in the container.

(string)

ContainerEnvironmentVariables -> (map)

The environment variables to set in the container

key -> (string)

value -> (string)

Shorthand Syntax:

```
FileSystemConfig={MountPath=string,DefaultUid=integer,DefaultGid=integer},ContainerConfig={ContainerArguments=[string,string],ContainerEntrypoint=[string,string],ContainerEnvironmentVariables={KeyName1=string,KeyName2=string}}
```

JSON Syntax:

```
{
  "FileSystemConfig": {
    "MountPath": "string",
    "DefaultUid": integer,
    "DefaultGid": integer
  },
  "ContainerConfig": {
    "ContainerArguments": ["string", ...],
    "ContainerEntrypoint": ["string", ...],
    "ContainerEnvironmentVariables": {"string": "string"
      ...}
  }
}
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

AppImageConfigArn -> (string)

The ARN of the AppImageConfig.