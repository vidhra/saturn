# create-container-recipeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-container-recipe.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-container-recipe.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [imagebuilder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/index.html#cli-aws-imagebuilder) ]

# create-container-recipe

## Description

Creates a new container recipe. Container recipes define how images are configured, tested, and assessed.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/imagebuilder-2019-12-02/CreateContainerRecipe)

## Synopsis

```
create-container-recipe
--container-type <value>
--name <value>
[--description <value>]
--semantic-version <value>
--components <value>
[--instance-configuration <value>]
[--dockerfile-template-data <value>]
[--dockerfile-template-uri <value>]
[--platform-override <value>]
[--image-os-version-override <value>]
--parent-image <value>
[--tags <value>]
[--working-directory <value>]
--target-repository <value>
[--kms-key-id <value>]
[--client-token <value>]
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

`--container-type` (string)

The type of container to create.

Possible values:

- `DOCKER`

`--name` (string)

The name of the container recipe.

`--description` (string)

The description of the container recipe.

`--semantic-version` (string)

The semantic version of the container recipe. This version follows the semantic version syntax.

### Note

The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.

**Assignment:** For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.

**Patterns:** You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.

`--components` (list)

Components for build and test that are included in the container recipe. Recipes require a minimum of one build component, and can have a maximum of 20 build and test components in any combination.

(structure)

Configuration details of the component.

componentArn -> (string)

The Amazon Resource Name (ARN) of the component.

parameters -> (list)

A group of parameter settings that Image Builder uses to configure the component for a specific recipe.

(structure)

Contains a key/value pair that sets the named component parameter.

name -> (string)

The name of the component parameter to set.

value -> (list)

Sets the value for the named component parameter.

(string)

JSON Syntax:

```
[
  {
    "componentArn": "string",
    "parameters": [
      {
        "name": "string",
        "value": ["string", ...]
      }
      ...
    ]
  }
  ...
]
```

`--instance-configuration` (structure)

A group of options that can be used to configure an instance for building and testing container images.

image -> (string)

The base image for a container build and test instance. This can contain an AMI ID or it can specify an Amazon Web Services Systems Manager (SSM) Parameter Store Parameter, prefixed by `ssm:` , followed by the parameter name or ARN.

If not specified, Image Builder uses the appropriate ECS-optimized AMI as a base image.

blockDeviceMappings -> (list)

Defines the block devices to attach for building an instance from this Image Builder AMI.

(structure)

Defines block device mappings for the instance used to configure your image.

deviceName -> (string)

The device to which these mappings apply.

ebs -> (structure)

Use to manage Amazon EBS-specific configuration for this mapping.

encrypted -> (boolean)

Use to configure device encryption.

deleteOnTermination -> (boolean)

Use to configure delete on termination of the associated device.

iops -> (integer)

Use to configure device IOPS.

kmsKeyId -> (string)

Use to configure the KMS key to use when encrypting the device.

snapshotId -> (string)

The snapshot that defines the device contents.

volumeSize -> (integer)

Use to override the deviceâs volume size.

volumeType -> (string)

Use to override the deviceâs volume type.

throughput -> (integer)

**For GP3 volumes only** â The throughput in MiB/s that the volume supports.

virtualName -> (string)

Use to manage instance ephemeral devices.

noDevice -> (string)

Use to remove a mapping from the base image.

JSON Syntax:

```
{
  "image": "string",
  "blockDeviceMappings": [
    {
      "deviceName": "string",
      "ebs": {
        "encrypted": true|false,
        "deleteOnTermination": true|false,
        "iops": integer,
        "kmsKeyId": "string",
        "snapshotId": "string",
        "volumeSize": integer,
        "volumeType": "standard"|"io1"|"io2"|"gp2"|"gp3"|"sc1"|"st1",
        "throughput": integer
      },
      "virtualName": "string",
      "noDevice": "string"
    }
    ...
  ]
}
```

`--dockerfile-template-data` (string)

The Dockerfile template used to build your image as an inline data blob.

`--dockerfile-template-uri` (string)

The Amazon S3 URI for the Dockerfile that will be used to build your container image.

`--platform-override` (string)

Specifies the operating system platform when you use a custom base image.

Possible values:

- `Windows`
- `Linux`
- `macOS`

`--image-os-version-override` (string)

Specifies the operating system version for the base image.

`--parent-image` (string)

The base image for the container recipe.

`--tags` (map)

Tags that are attached to the container recipe.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--working-directory` (string)

The working directory for use during build and test workflows.

`--target-repository` (structure)

The destination repository for the container image.

service -> (string)

Specifies the service in which this image was registered.

repositoryName -> (string)

The name of the container repository where the output container image is stored. This name is prefixed by the repository location. For example, `<repository location url>/repository_name` .

Shorthand Syntax:

```
service=string,repositoryName=string
```

JSON Syntax:

```
{
  "service": "ECR",
  "repositoryName": "string"
}
```

`--kms-key-id` (string)

Identifies which KMS key is used to encrypt the Dockerfile template.

`--client-token` (string)

Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference* .

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

requestId -> (string)

The request ID that uniquely identifies this request.

clientToken -> (string)

The client token that uniquely identifies the request.

containerRecipeArn -> (string)

Returns the Amazon Resource Name (ARN) of the container recipe that the request created.