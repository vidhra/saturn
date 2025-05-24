# get-container-recipeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-container-recipe.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-container-recipe.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [imagebuilder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/index.html#cli-aws-imagebuilder) ]

# get-container-recipe

## Description

Retrieves a container recipe.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/imagebuilder-2019-12-02/GetContainerRecipe)

## Synopsis

```
get-container-recipe
--container-recipe-arn <value>
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

`--container-recipe-arn` (string)

The Amazon Resource Name (ARN) of the container recipe to retrieve.

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

containerRecipe -> (structure)

The container recipe object that is returned.

arn -> (string)

The Amazon Resource Name (ARN) of the container recipe.

### Note

Semantic versioning is included in each objectâs Amazon Resource Name (ARN), at the level that applies to that object as follows:

- Versionless ARNs and Name ARNs do not include specific values in any of the nodes. The nodes are either left off entirely, or they are specified as wildcards, for example: x.x.x.
- Version ARNs have only the first three nodes: <major>.<minor>.<patch>
- Build version ARNs have all four nodes, and point to a specific build for a specific version of an object.

containerType -> (string)

Specifies the type of container, such as Docker.

name -> (string)

The name of the container recipe.

description -> (string)

The description of the container recipe.

platform -> (string)

The system platform for the container, such as Windows or Linux.

owner -> (string)

The owner of the container recipe.

version -> (string)

The semantic version of the container recipe.

### Note

The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.

**Assignment:** For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.

**Patterns:** You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.

**Filtering:** With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.

components -> (list)

Build and test components that are included in the container recipe. Recipes require a minimum of one build component, and can have a maximum of 20 build and test components in any combination.

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

instanceConfiguration -> (structure)

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

dockerfileTemplateData -> (string)

Dockerfiles are text documents that are used to build Docker containers, and ensure that they contain all of the elements required by the application running inside. The template data consists of contextual variables where Image Builder places build information or scripts, based on your container image recipe.

kmsKeyId -> (string)

Identifies which KMS key is used to encrypt the container image for distribution to the target Region.

encrypted -> (boolean)

A flag that indicates if the target container is encrypted.

parentImage -> (string)

The base image for customizations specified in the container recipe. This can contain an Image Builder image resource ARN or a container image URI, for example `amazonlinux:latest` .

dateCreated -> (string)

The date when this container recipe was created.

tags -> (map)

Tags that are attached to the container recipe.

key -> (string)

value -> (string)

workingDirectory -> (string)

The working directory for use during build and test workflows.

targetRepository -> (structure)

The destination repository for the container image.

service -> (string)

Specifies the service in which this image was registered.

repositoryName -> (string)

The name of the container repository where the output container image is stored. This name is prefixed by the repository location. For example, `<repository location url>/repository_name` .