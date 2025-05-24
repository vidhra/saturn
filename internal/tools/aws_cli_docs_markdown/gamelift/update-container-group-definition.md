# update-container-group-definitionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-container-group-definition.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-container-group-definition.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# update-container-group-definition

## Description

Updates properties in an existing container group definition. This operation doesnât replace the definition. Instead, it creates a new version of the definition and saves it separately. You can access all versions that you choose to retain.

The only property you canât update is the container group type.

**Request options:**

- Update based on the latest version of the container group definition. Specify the container group definition name only, or use an ARN value without a version number. Provide updated values for the properties that you want to change only. All other values remain the same as the latest version.
- Update based on a specific version of the container group definition. Specify the container group definition name and a source version number, or use an ARN value with a version number. Provide updated values for the properties that you want to change only. All other values remain the same as the source version.
- Change a game server container definition. Provide the updated container definition.
- Add or change a support container definition. Provide a complete set of container definitions, including the updated definition.
- Remove a support container definition. Provide a complete set of container definitions, excluding the definition to remove. If the container group has only one support container definition, provide an empty set.

**Results:**

If successful, this operation returns the complete properties of the new container group definition version.

If the container group definition version is used in an active fleets, the update automatically initiates a new fleet deployment of the new version. You can track a fleetâs deployments using [ListFleetDeployments](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListFleetDeployments.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/UpdateContainerGroupDefinition)

## Synopsis

```
update-container-group-definition
--name <value>
[--game-server-container-definition <value>]
[--support-container-definitions <value>]
[--total-memory-limit-mebibytes <value>]
[--total-vcpu-limit <value>]
[--version-description <value>]
[--source-version-number <value>]
[--operating-system <value>]
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

A descriptive identifier for the container group definition. The name value must be unique in an Amazon Web Services Region.

`--game-server-container-definition` (structure)

An updated definition for the game server container in this group. Define a game server container only when the container group type is `GAME_SERVER` . You can pass in your container definitions as a JSON file.

ContainerName -> (string)

A string that uniquely identifies the container definition within a container group.

DependsOn -> (list)

Establishes dependencies between this container and the status of other containers in the same container group. A container can have dependencies on multiple different containers.

You can use dependencies to establish a startup/shutdown sequence across the container group. For example, you might specify that *ContainerB* has a `START` dependency on *ContainerA* . This dependency means that *ContainerB* canât start until after *ContainerA* has started. This dependency is reversed on shutdown, which means that *ContainerB* must shut down before *ContainerA* can shut down.

(structure)

A containerâs dependency on another container in the same container group. The dependency impacts how the dependent container is able to start or shut down based the status of the other container.

For example, *ContainerA* is configured with the following dependency: a `START` dependency on *ContainerB* . This means that *ContainerA* canât start until *ContainerB* has started. It also means that *ContainerA* must shut down before *ContainerB* .

**Part of:** [GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html) , [GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html) , [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html) , [SupportContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

ContainerName -> (string)

A descriptive label for the container definition that this container depends on.

Condition -> (string)

The condition that the dependency container must reach before the dependent container can start. Valid conditions include:

- START - The dependency container must have started.
- COMPLETE - The dependency container has run to completion (exits). Use this condition with nonessential containers, such as those that run a script and then exit. The dependency container canât be an essential container.
- SUCCESS - The dependency container has run to completion and exited with a zero status. The dependency container canât be an essential container.
- HEALTHY - The dependency container has passed its Docker health check. Use this condition with dependency containers that have health checks configured. This condition is confirmed at container group startup only.

MountPoints -> (list)

A mount point that binds a path inside the container to a file or directory on the host system and lets it access the file or directory.

(structure)

A mount point that binds a container to a file or directory on the host system.

**Part of:** [GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html) , [https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html) , [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html) , [https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

InstancePath -> (string)

The path to the source file or directory.

ContainerPath -> (string)

The mount path on the container. If this property isnât set, the instance path is used.

AccessLevel -> (string)

The type of access for the container.

EnvironmentOverride -> (list)

A set of environment variables to pass to the container on startup. See the [ContainerDefinition::environment](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment) parameter in the *Amazon Elastic Container Service API Reference* .

(structure)

An environment variable to set inside a container, in the form of a key-value pair.

**Part of:** [GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html) , [GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html) , [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html) , [SupportContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

Name -> (string)

The environment variable name.

Value -> (string)

The environment variable value.

ImageUri -> (string)

The location of the container image to deploy to a container fleet. Provide an image in an Amazon Elastic Container Registry public or private repository. The repository must be in the same Amazon Web Services account and Amazon Web Services Region where youâre creating the container group definition. For limits on image size, see [Amazon GameLift endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/gamelift.html) . You can use any of the following image URI formats:

- Image ID only: `[AWS account].dkr.ecr.[AWS region].amazonaws.com/[repository ID]`
- Image ID and digest: `[AWS account].dkr.ecr.[AWS region].amazonaws.com/[repository ID]@[digest]`
- Image ID and tag: `[AWS account].dkr.ecr.[AWS region].amazonaws.com/[repository ID]:[tag]`

PortConfiguration -> (structure)

A set of ports that Amazon GameLift can assign to processes in the container. Processes, must be assigned a container port to accept inbound traffic connections. For example, a game server process requires a container port to allow game clients to connect to it. Container ports arenât directly accessed by inbound traffic. Instead, Amazon GameLift maps container ports to externally accessible connection ports (see the container fleet property `ConnectionPortRange` ).

ContainerPortRanges -> (list)

A set of one or more container port number ranges. The ranges canât overlap.

(structure)

A set of one or more port numbers that can be opened on the container.

**Part of:** [ContainerPortConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerPortConfiguration.html)

FromPort -> (integer)

A starting value for the range of allowed port numbers.

ToPort -> (integer)

An ending value for the range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than `FromPort` .

Protocol -> (string)

The network protocol that these ports support.

ServerSdkVersion -> (string)

The Amazon GameLift server SDK version that the game server is integrated with. Only game servers using 5.2.0 or higher are compatible with container fleets.

JSON Syntax:

```
{
  "ContainerName": "string",
  "DependsOn": [
    {
      "ContainerName": "string",
      "Condition": "START"|"COMPLETE"|"SUCCESS"|"HEALTHY"
    }
    ...
  ],
  "MountPoints": [
    {
      "InstancePath": "string",
      "ContainerPath": "string",
      "AccessLevel": "READ_ONLY"|"READ_AND_WRITE"
    }
    ...
  ],
  "EnvironmentOverride": [
    {
      "Name": "string",
      "Value": "string"
    }
    ...
  ],
  "ImageUri": "string",
  "PortConfiguration": {
    "ContainerPortRanges": [
      {
        "FromPort": integer,
        "ToPort": integer,
        "Protocol": "TCP"|"UDP"
      }
      ...
    ]
  },
  "ServerSdkVersion": "string"
}
```

`--support-container-definitions` (list)

One or more definitions for support containers in this group. You can define a support container in any type of container group. You can pass in your container definitions as a JSON file.

(structure)

Describes a support container in a container group. You can define a support container in either a game server container group or a per-instance container group. Support containers donât run game server processes.

This definition includes container configuration, resources, and start instructions. Use this data type when creating or updating a container group definition. For properties of a deployed support container, see [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html) .

**Use with:** [CreateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html) , [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html)

ContainerName -> (string)

A string that uniquely identifies the container definition within a container group.

DependsOn -> (list)

Establishes dependencies between this container and the status of other containers in the same container group. A container can have dependencies on multiple different containers.

.

You can use dependencies to establish a startup/shutdown sequence across the container group. For example, you might specify that *ContainerB* has a `START` dependency on *ContainerA* . This dependency means that *ContainerB* canât start until after *ContainerA* has started. This dependency is reversed on shutdown, which means that *ContainerB* must shut down before *ContainerA* can shut down.

(structure)

A containerâs dependency on another container in the same container group. The dependency impacts how the dependent container is able to start or shut down based the status of the other container.

For example, *ContainerA* is configured with the following dependency: a `START` dependency on *ContainerB* . This means that *ContainerA* canât start until *ContainerB* has started. It also means that *ContainerA* must shut down before *ContainerB* .

**Part of:** [GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html) , [GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html) , [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html) , [SupportContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

ContainerName -> (string)

A descriptive label for the container definition that this container depends on.

Condition -> (string)

The condition that the dependency container must reach before the dependent container can start. Valid conditions include:

- START - The dependency container must have started.
- COMPLETE - The dependency container has run to completion (exits). Use this condition with nonessential containers, such as those that run a script and then exit. The dependency container canât be an essential container.
- SUCCESS - The dependency container has run to completion and exited with a zero status. The dependency container canât be an essential container.
- HEALTHY - The dependency container has passed its Docker health check. Use this condition with dependency containers that have health checks configured. This condition is confirmed at container group startup only.

MountPoints -> (list)

A mount point that binds a path inside the container to a file or directory on the host system and lets it access the file or directory.

(structure)

A mount point that binds a container to a file or directory on the host system.

**Part of:** [GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html) , [https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html) , [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html) , [https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

InstancePath -> (string)

The path to the source file or directory.

ContainerPath -> (string)

The mount path on the container. If this property isnât set, the instance path is used.

AccessLevel -> (string)

The type of access for the container.

EnvironmentOverride -> (list)

A set of environment variables to pass to the container on startup. See the [ContainerDefinition::environment](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment) parameter in the *Amazon Elastic Container Service API Reference* .

(structure)

An environment variable to set inside a container, in the form of a key-value pair.

**Part of:** [GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html) , [GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html) , [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html) , [SupportContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

Name -> (string)

The environment variable name.

Value -> (string)

The environment variable value.

Essential -> (boolean)

Flags the container as vital for the container group to function properly. If an essential container fails, the entire container group restarts. At least one support container in a per-instance container group must be essential. When flagging a container as essential, also configure a health check so that the container can signal that itâs healthy.

HealthCheck -> (structure)

Configuration for a non-terminal health check. A container automatically restarts if it stops functioning. With a health check, you can define additional reasons to flag a container as unhealthy and restart it. If an essential container fails a health check, the entire container group restarts.

Command -> (list)

A string array that specifies the command that the container runs to determine if itâs healthy.

(string)

Interval -> (integer)

The time period (in seconds) between each health check.

Retries -> (integer)

The number of times to retry a failed health check before flagging the container unhealthy. The first run of the command does not count as a retry.

StartPeriod -> (integer)

The optional grace period (in seconds) to give a container time to bootstrap before the first failed health check counts toward the number of retries.

Timeout -> (integer)

The time period (in seconds) to wait for a health check to succeed before counting a failed health check.

ImageUri -> (string)

The location of the container image to deploy to a container fleet. Provide an image in an Amazon Elastic Container Registry public or private repository. The repository must be in the same Amazon Web Services account and Amazon Web Services Region where youâre creating the container group definition. For limits on image size, see [Amazon GameLift endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/gamelift.html) . You can use any of the following image URI formats:

- Image ID only: `[AWS account].dkr.ecr.[AWS region].amazonaws.com/[repository ID]`
- Image ID and digest: `[AWS account].dkr.ecr.[AWS region].amazonaws.com/[repository ID]@[digest]`
- Image ID and tag: `[AWS account].dkr.ecr.[AWS region].amazonaws.com/[repository ID]:[tag]`

MemoryHardLimitMebibytes -> (integer)

A specified amount of memory (in MiB) to reserve for this container. If you donât specify a container-specific memory limit, the container shares the container groupâs total memory allocation.

**Related data type:** [ContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html) TotalMemoryLimitMebibytes

PortConfiguration -> (structure)

A set of ports that Amazon GameLift can assign to processes in the container. Any processes that accept inbound traffic connections must be assigned a port from this set. The container port range must be large enough to assign one to each process in the container that needs one.

Container ports arenât directly accessed by inbound traffic. Amazon GameLift maps these container ports to externally accessible connection ports, which are assigned as needed from the container fleetâs `ConnectionPortRange` .

ContainerPortRanges -> (list)

A set of one or more container port number ranges. The ranges canât overlap.

(structure)

A set of one or more port numbers that can be opened on the container.

**Part of:** [ContainerPortConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerPortConfiguration.html)

FromPort -> (integer)

A starting value for the range of allowed port numbers.

ToPort -> (integer)

An ending value for the range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than `FromPort` .

Protocol -> (string)

The network protocol that these ports support.

Vcpu -> (double)

The number of vCPU units to reserve for this container. The container can use more resources when needed, if available. If you donât reserve CPU units for this container, it shares the container groupâs total vCPU limit.

**Related data type:** [ContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html) TotalCpuLimit

JSON Syntax:

```
[
  {
    "ContainerName": "string",
    "DependsOn": [
      {
        "ContainerName": "string",
        "Condition": "START"|"COMPLETE"|"SUCCESS"|"HEALTHY"
      }
      ...
    ],
    "MountPoints": [
      {
        "InstancePath": "string",
        "ContainerPath": "string",
        "AccessLevel": "READ_ONLY"|"READ_AND_WRITE"
      }
      ...
    ],
    "EnvironmentOverride": [
      {
        "Name": "string",
        "Value": "string"
      }
      ...
    ],
    "Essential": true|false,
    "HealthCheck": {
      "Command": ["string", ...],
      "Interval": integer,
      "Retries": integer,
      "StartPeriod": integer,
      "Timeout": integer
    },
    "ImageUri": "string",
    "MemoryHardLimitMebibytes": integer,
    "PortConfiguration": {
      "ContainerPortRanges": [
        {
          "FromPort": integer,
          "ToPort": integer,
          "Protocol": "TCP"|"UDP"
        }
        ...
      ]
    },
    "Vcpu": double
  }
  ...
]
```

`--total-memory-limit-mebibytes` (integer)

The maximum amount of memory (in MiB) to allocate to the container group. All containers in the group share this memory. If you specify memory limits for an individual container, the total value must be greater than any individual containerâs memory limit.

`--total-vcpu-limit` (double)

The maximum amount of vCPU units to allocate to the container group (1 vCPU is equal to 1024 CPU units). All containers in the group share this memory. If you specify vCPU limits for individual containers, the total value must be equal to or greater than the sum of the CPU limits for all containers in the group.

`--version-description` (string)

A description for this update to the container group definition.

`--source-version-number` (integer)

The container group definition version to update. The new version starts with values from the source version, and then updates values included in this request.

`--operating-system` (string)

The platform that all containers in the group use. Containers in a group must run on the same operating system.

### Note

Amazon Linux 2 (AL2) will reach end of support on 6/30/2025. See more details in the [Amazon Linux 2 FAQs](https://aws.amazon.com/amazon-linux-2/faqs/) . For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See [Migrate to server SDK version 5.](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html)

Possible values:

- `AMAZON_LINUX_2023`

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

ContainerGroupDefinition -> (structure)

The properties of the updated container group definition version.

ContainerGroupDefinitionArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) that is assigned to an Amazon GameLift `ContainerGroupDefinition` resource. It uniquely identifies the resource across all Amazon Web Services Regions. Format is `arn:aws:gamelift:[region]::containergroupdefinition/[container group definition name]:[version]` .

CreationTime -> (timestamp)

A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ).

OperatingSystem -> (string)

The platform that all containers in the container group definition run on.

### Note

Amazon Linux 2 (AL2) will reach end of support on 6/30/2025. See more details in the [Amazon Linux 2 FAQs](https://aws.amazon.com/amazon-linux-2/faqs/) . For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See [Migrate to server SDK version 5.](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html)

Name -> (string)

A descriptive identifier for the container group definition. The name value is unique in an Amazon Web Services Region.

ContainerGroupType -> (string)

The type of container group. Container group type determines how Amazon GameLift deploys the container group on each fleet instance.

TotalMemoryLimitMebibytes -> (integer)

The amount of memory (in MiB) on a fleet instance to allocate for the container group. All containers in the group share these resources.

You can set a limit for each container definition in the group. If individual containers have limits, this total value must be greater than any individual containerâs memory limit.

TotalVcpuLimit -> (double)

The amount of vCPU units on a fleet instance to allocate for the container group (1 vCPU is equal to 1024 CPU units). All containers in the group share these resources. You can set a limit for each container definition in the group. If individual containers have limits, this total value must be equal to or greater than the sum of the limits for each container in the group.

GameServerContainerDefinition -> (structure)

The definition for the game server container in this group. This property is used only when the container group type is `GAME_SERVER` . This container definition specifies a container image with the game server build.

ContainerName -> (string)

The container definition identifier. Container names are unique within a container group definition.

DependsOn -> (list)

Indicates that the container relies on the status of other containers in the same container group during startup and shutdown sequences. A container might have dependencies on multiple containers.

(structure)

A containerâs dependency on another container in the same container group. The dependency impacts how the dependent container is able to start or shut down based the status of the other container.

For example, *ContainerA* is configured with the following dependency: a `START` dependency on *ContainerB* . This means that *ContainerA* canât start until *ContainerB* has started. It also means that *ContainerA* must shut down before *ContainerB* .

**Part of:** [GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html) , [GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html) , [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html) , [SupportContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

ContainerName -> (string)

A descriptive label for the container definition that this container depends on.

Condition -> (string)

The condition that the dependency container must reach before the dependent container can start. Valid conditions include:

- START - The dependency container must have started.
- COMPLETE - The dependency container has run to completion (exits). Use this condition with nonessential containers, such as those that run a script and then exit. The dependency container canât be an essential container.
- SUCCESS - The dependency container has run to completion and exited with a zero status. The dependency container canât be an essential container.
- HEALTHY - The dependency container has passed its Docker health check. Use this condition with dependency containers that have health checks configured. This condition is confirmed at container group startup only.

MountPoints -> (list)

A mount point that binds a path inside the container to a file or directory on the host system and lets it access the file or directory.

(structure)

A mount point that binds a container to a file or directory on the host system.

**Part of:** [GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html) , [https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html) , [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html) , [https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

InstancePath -> (string)

The path to the source file or directory.

ContainerPath -> (string)

The mount path on the container. If this property isnât set, the instance path is used.

AccessLevel -> (string)

The type of access for the container.

EnvironmentOverride -> (list)

A set of environment variables thatâs passed to the container on startup. See the [ContainerDefinition::environment](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment) parameter in the *Amazon Elastic Container Service API Reference* .

(structure)

An environment variable to set inside a container, in the form of a key-value pair.

**Part of:** [GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html) , [GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html) , [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html) , [SupportContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

Name -> (string)

The environment variable name.

Value -> (string)

The environment variable value.

ImageUri -> (string)

The URI to the image that Amazon GameLift uses when deploying this container to a container fleet. For a more specific identifier, see `ResolvedImageDigest` .

PortConfiguration -> (structure)

The set of ports that are available to bind to processes in the container. For example, a game server process requires a container port to allow game clients to connect to it. Container ports arenât directly accessed by inbound traffic. Amazon GameLift maps these container ports to externally accessible connection ports, which are assigned as needed from the container fleetâs `ConnectionPortRange` .

ContainerPortRanges -> (list)

A set of one or more container port number ranges. The ranges canât overlap.

(structure)

A set of one or more port numbers that can be opened on the container.

**Part of:** [ContainerPortConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerPortConfiguration.html)

FromPort -> (integer)

A starting value for the range of allowed port numbers.

ToPort -> (integer)

An ending value for the range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than `FromPort` .

Protocol -> (string)

The network protocol that these ports support.

ResolvedImageDigest -> (string)

A unique and immutable identifier for the container image. The digest is a SHA 256 hash of the container image manifest.

ServerSdkVersion -> (string)

The Amazon GameLift server SDK version that the game server is integrated with. Only game servers using 5.2.0 or higher are compatible with container fleets.

SupportContainerDefinitions -> (list)

The set of definitions for support containers in this group. A container group definition might have zero support container definitions. Support container can be used in any type of container group.

(structure)

Describes a support container in a container group. A support container might be in a game server container group or a per-instance container group. Support containers donât run game server processes.

You can update a support container definition and deploy the updates to an existing fleet. When creating or updating a game server container group definition, use the property [GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html) .

**Part of:** [ContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html)

**Returned by:** [DescribeContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeContainerGroupDefinition.html) , [ListContainerGroupDefinitions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitions.html) , [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html)

ContainerName -> (string)

The container definition identifier. Container names are unique within a container group definition.

DependsOn -> (list)

Indicates that the container relies on the status of other containers in the same container group during its startup and shutdown sequences. A container might have dependencies on multiple containers.

(structure)

A containerâs dependency on another container in the same container group. The dependency impacts how the dependent container is able to start or shut down based the status of the other container.

For example, *ContainerA* is configured with the following dependency: a `START` dependency on *ContainerB* . This means that *ContainerA* canât start until *ContainerB* has started. It also means that *ContainerA* must shut down before *ContainerB* .

**Part of:** [GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html) , [GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html) , [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html) , [SupportContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

ContainerName -> (string)

A descriptive label for the container definition that this container depends on.

Condition -> (string)

The condition that the dependency container must reach before the dependent container can start. Valid conditions include:

- START - The dependency container must have started.
- COMPLETE - The dependency container has run to completion (exits). Use this condition with nonessential containers, such as those that run a script and then exit. The dependency container canât be an essential container.
- SUCCESS - The dependency container has run to completion and exited with a zero status. The dependency container canât be an essential container.
- HEALTHY - The dependency container has passed its Docker health check. Use this condition with dependency containers that have health checks configured. This condition is confirmed at container group startup only.

MountPoints -> (list)

A mount point that binds a path inside the container to a file or directory on the host system and lets it access the file or directory.

(structure)

A mount point that binds a container to a file or directory on the host system.

**Part of:** [GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html) , [https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html) , [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html) , [https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

InstancePath -> (string)

The path to the source file or directory.

ContainerPath -> (string)

The mount path on the container. If this property isnât set, the instance path is used.

AccessLevel -> (string)

The type of access for the container.

EnvironmentOverride -> (list)

A set of environment variables thatâs passed to the container on startup. See the [ContainerDefinition::environment](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment) parameter in the *Amazon Elastic Container Service API Reference* .

(structure)

An environment variable to set inside a container, in the form of a key-value pair.

**Part of:** [GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html) , [GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html) , [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html) , [SupportContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

Name -> (string)

The environment variable name.

Value -> (string)

The environment variable value.

Essential -> (boolean)

Indicates whether the container is vital to the container group. If an essential container fails, the entire container group restarts.

HealthCheck -> (structure)

A configuration for a non-terminal health check. A support container automatically restarts if it stops functioning or if it fails this health check.

Command -> (list)

A string array that specifies the command that the container runs to determine if itâs healthy.

(string)

Interval -> (integer)

The time period (in seconds) between each health check.

Retries -> (integer)

The number of times to retry a failed health check before flagging the container unhealthy. The first run of the command does not count as a retry.

StartPeriod -> (integer)

The optional grace period (in seconds) to give a container time to bootstrap before the first failed health check counts toward the number of retries.

Timeout -> (integer)

The time period (in seconds) to wait for a health check to succeed before counting a failed health check.

ImageUri -> (string)

The URI to the image that Amazon GameLift deploys to a container fleet. For a more specific identifier, see `ResolvedImageDigest` .

MemoryHardLimitMebibytes -> (integer)

The amount of memory that Amazon GameLift makes available to the container. If memory limits arenât set for an individual container, the container shares the container groupâs total memory allocation.

**Related data type:** [ContainerGroupDefinition TotalMemoryLimitMebibytes](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html)

PortConfiguration -> (structure)

A set of ports that allow access to the container from external users. Processes running in the container can bind to a one of these ports. Container ports arenât directly accessed by inbound traffic. Amazon GameLift maps these container ports to externally accessible connection ports, which are assigned as needed from the container fleetâs `ConnectionPortRange` .

ContainerPortRanges -> (list)

A set of one or more container port number ranges. The ranges canât overlap.

(structure)

A set of one or more port numbers that can be opened on the container.

**Part of:** [ContainerPortConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerPortConfiguration.html)

FromPort -> (integer)

A starting value for the range of allowed port numbers.

ToPort -> (integer)

An ending value for the range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than `FromPort` .

Protocol -> (string)

The network protocol that these ports support.

ResolvedImageDigest -> (string)

A unique and immutable identifier for the container image. The digest is a SHA 256 hash of the container image manifest.

Vcpu -> (double)

The number of vCPU units that are reserved for the container. If no resources are reserved, the container shares the total vCPU limit for the container group.

**Related data type:** [ContainerGroupDefinition TotalVcpuLimit](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html)

VersionNumber -> (integer)

Indicates the version of a particular container group definition. This number is incremented automatically when you update a container group definition. You can view, update, or delete individual versions or the entire container group definition.

VersionDescription -> (string)

An optional description that was provided for a container group definition update. Each version can have a unique description.

Status -> (string)

Current status of the container group definition resource. Values include:

- `COPYING` â Amazon GameLift is in the process of making copies of all container images that are defined in the group. While in this state, the resource canât be used to create a container fleet.
- `READY` â Amazon GameLift has copied the registry images for all containers that are defined in the group. You can use a container group definition in this status to create a container fleet.
- `FAILED` â Amazon GameLift failed to create a valid container group definition resource. For more details on the cause of the failure, see `StatusReason` . A container group definition resource in failed status will be deleted within a few minutes.

StatusReason -> (string)

Additional information about a container group definition thatâs in `FAILED` status. Possible reasons include:

- An internal issue prevented Amazon GameLift from creating the container group definition resource. Delete the failed resource and call [CreateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html) again.
- An access-denied message means that you donât have permissions to access the container image on ECR. See [IAM permission examples](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-iam-policy-examples.html.html) for help setting up required IAM permissions for Amazon GameLift.
- The `ImageUri` value for at least one of the containers in the container group definition was invalid or not found in the current Amazon Web Services account.
- At least one of the container images referenced in the container group definition exceeds the allowed size. For size limits, see [Amazon GameLift endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/gamelift.html) .
- At least one of the container images referenced in the container group definition uses a different operating system than the one defined for the container group.