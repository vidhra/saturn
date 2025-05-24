# list-container-group-definitionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-container-group-definitions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-container-group-definitions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# list-container-group-definitions

## Description

Retrieves container group definitions for the Amazon Web Services account and Amazon Web Services Region. Use the pagination parameters to retrieve results in a set of sequential pages.

This operation returns only the latest version of each definition. To retrieve all versions of a container group definition, use [ListContainerGroupDefinitionVersions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitionVersions.html) .

**Request options:**

- Retrieve the most recent versions of all container group definitions.
- Retrieve the most recent versions of all container group definitions, filtered by type. Specify the container group type to filter on.

**Results:**

If successful, this operation returns the complete properties of a set of container group definition versions that match the request.

### Note

This operation returns the list of container group definitions in no particular order.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/ListContainerGroupDefinitions)

`list-container-group-definitions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ContainerGroupDefinitions`

## Synopsis

```
list-container-group-definitions
[--container-group-type <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--container-group-type` (string)

The type of container group to retrieve. Container group type determines how Amazon GameLift deploys the container group on each fleet instance.

Possible values:

- `GAME_SERVER`
- `PER_INSTANCE`

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

ContainerGroupDefinitions -> (list)

A result set of container group definitions that match the request.

(structure)

The properties that describe a container group resource. You can update all properties of a container group definition properties. Updates to a container group definition are saved as new versions.

**Used with:** [CreateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html)

**Returned by:** [DescribeContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeContainerGroupDefinition.html) , [ListContainerGroupDefinitions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitions.html) , [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html)

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

NextToken -> (string)

A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.