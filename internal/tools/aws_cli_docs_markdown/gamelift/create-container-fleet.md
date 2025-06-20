# create-container-fleetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-container-fleet.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-container-fleet.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# create-container-fleet

## Description

Creates a managed fleet of Amazon Elastic Compute Cloud (Amazon EC2) instances to host your containerized game servers. Use this operation to define how to deploy a container architecture onto each fleet instance and configure fleet settings. You can create a container fleet in any Amazon Web Services Regions that Amazon GameLift supports for multi-location fleets. A container fleet can be deployed to a single location or multiple locations. Container fleets are deployed with Amazon Linux 2023 as the instance operating system.

Define the fleetâs container architecture using container group definitions. Each fleet can have one of the following container group types:

- The game server container group runs your game server build and dependent software. Amazon GameLift deploys one or more replicas of this container group to each fleet instance. The number of replicas depends on the computing capabilities of the fleet instance in use.
- An optional per-instance container group might be used to run other software that only needs to run once per instance, such as background services, logging, or test processes. One per-instance container group is deployed to each fleet instance.

Each container group can include the definition for one or more containers. A container definition specifies a container image that is stored in an Amazon Elastic Container Registry (Amazon ECR) public or private repository.

**Request options**

Use this operation to make the following types of requests. Most fleet settings have default values, so you can create a working fleet with a minimal configuration and default values, which you can customize later.

- Create a fleet with no container groups. You can configure a container fleet and then add container group definitions later. In this scenario, no fleet instances are deployed, and the fleet canât host game sessions until you add a game server container group definition. Provide the following required parameter values:
- `FleetRoleArn`
- Create a fleet with a game server container group. Provide the following required parameter values:
- `FleetRoleArn`
- `GameServerContainerGroupDefinitionName`
- Create a fleet with a game server container group and a per-instance container group. Provide the following required parameter values:
- `FleetRoleArn`
- `GameServerContainerGroupDefinitionName`
- `PerInstanceContainerGroupDefinitionName`

**Results**

If successful, this operation creates a new container fleet resource, places it in `PENDING` status, and initiates the [fleet creation workflow](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-all.html#fleets-creation-workflow) . For fleets with container groups, this workflow starts a fleet deployment and transitions the status to `ACTIVE` . Fleets without a container group are placed in `CREATED` status.

You can update most of the properties of a fleet, including container group definitions, and deploy the update across all fleet instances. Use a fleet update to deploy a new game server version update across the container fleet.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/CreateContainerFleet)

## Synopsis

```
create-container-fleet
--fleet-role-arn <value>
[--description <value>]
[--game-server-container-group-definition-name <value>]
[--per-instance-container-group-definition-name <value>]
[--instance-connection-port-range <value>]
[--instance-inbound-permissions <value>]
[--game-server-container-groups-per-instance <value>]
[--instance-type <value>]
[--billing-type <value>]
[--locations <value>]
[--metric-groups <value>]
[--new-game-session-protection-policy <value>]
[--game-session-creation-limit-policy <value>]
[--log-configuration <value>]
[--tags <value>]
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

`--fleet-role-arn` (string)

The unique identifier for an Identity and Access Management (IAM) role with permissions to run your containers on resources that are managed by Amazon GameLift. Use an IAM service role with the `GameLiftContainerFleetPolicy` managed policy attached. For more information, see [Set up an IAM service role](https://docs.aws.amazon.com/gamelift/latest/developerguide/setting-up-role.html) . You canât change this fleet property after the fleet is created.

IAM role ARN values use the following pattern: `arn:aws:iam::[Amazon Web Services account]:role/[role name]` .

`--description` (string)

A meaningful description of the container fleet.

`--game-server-container-group-definition-name` (string)

A container group definition resource that describes how to deploy containers with your game server build and support software onto each fleet instance. You can specify the container group definitionâs name to use the latest version. Alternatively, provide an ARN value with a specific version number.

Create a container group definition by calling [CreateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html) . This operation creates a [ContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html) resource.

`--per-instance-container-group-definition-name` (string)

The name of a container group definition resource that describes a set of axillary software. A fleet instance has one process for executables in this container group. A per-instance container group is optional. You can update the fleet to add or remove a per-instance container group at any time. You can specify the container group definitionâs name to use the latest version. Alternatively, provide an ARN value with a specific version number.

Create a container group definition by calling [https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html) . This operation creates a [https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html) resource.

`--instance-connection-port-range` (structure)

The set of port numbers to open on each fleet instance. A fleetâs connection ports map to container ports that are configured in the fleetâs container group definitions.

By default, Amazon GameLift calculates an optimal port range based on your fleet configuration. To use the calculated range, donât set this parameter. The values are:

- Port range: 4192 to a number calculated based on your fleet configuration. Amazon GameLift uses the following formula: `4192 + [# of game server container groups per fleet instance] * [# of container ports in the game server container group definition] + [# of container ports in the game server container group definition]`

You can also choose to manually set this parameter. When manually setting this parameter, you must use port numbers that match the fleetâs inbound permissions port range.

### Note

If you set values manually, Amazon GameLift no longer calculates a port range for you, even if you later remove the manual settings.

FromPort -> (integer)

Starting value for the port range.

ToPort -> (integer)

Ending value for the port. Port numbers are end-inclusive. This value must be equal to or greater than `FromPort` .

Shorthand Syntax:

```
FromPort=integer,ToPort=integer
```

JSON Syntax:

```
{
  "FromPort": integer,
  "ToPort": integer
}
```

`--instance-inbound-permissions` (list)

The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet. As a best practice, when remotely accessing a fleet instance, we recommend opening ports only when you need them and closing them when youâre finished.

By default, Amazon GameLift calculates an optimal port range based on your fleet configuration. To use the calculated range, donât set this parameter. The values are:

- Protocol: UDP
- Port range: 4192 to a number calculated based on your fleet configuration. Amazon GameLift uses the following formula: `4192 + [# of game server container groups per fleet instance] * [# of container ports in the game server container group definition] + [# of container ports in the game server container group definition]`

You can also choose to manually set this parameter. When manually setting this parameter, you must use port numbers that match the fleetâs connection port range.

### Note

If you set values manually, Amazon GameLift no longer calculates a port range for you, even if you later remove the manual settings.

(structure)

A range of IP addresses and port settings that allow inbound traffic to connect to processes on an instance in a fleet. Processes are assigned an IP address/port number combination, which must fall into the fleetâs allowed ranges.

For Amazon GameLift Realtime fleets, Amazon GameLift automatically opens two port ranges, one for TCP messaging and one for UDP.

FromPort -> (integer)

A starting value for a range of allowed port numbers.

For fleets using Linux builds, only ports `22` and `1026-60000` are valid.

For fleets using Windows builds, only ports `1026-60000` are valid.

ToPort -> (integer)

An ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than `FromPort` .

For fleets using Linux builds, only ports `22` and `1026-60000` are valid.

For fleets using Windows builds, only ports `1026-60000` are valid.

IpRange -> (string)

A range of allowed IP addresses. This value must be expressed in CIDR notation. Example: â`000.000.000.000/[subnet mask]` â or optionally the shortened version â`0.0.0.0/[subnet mask]` â.

Protocol -> (string)

The network communication protocol used by the fleet.

Shorthand Syntax:

```
FromPort=integer,ToPort=integer,IpRange=string,Protocol=string ...
```

JSON Syntax:

```
[
  {
    "FromPort": integer,
    "ToPort": integer,
    "IpRange": "string",
    "Protocol": "TCP"|"UDP"
  }
  ...
]
```

`--game-server-container-groups-per-instance` (integer)

The number of times to replicate the game server container group on each fleet instance.

By default, Amazon GameLift calculates the maximum number of game server container groups that can fit on each instance. This calculation is based on the CPU and memory resources of the fleetâs instance type). To use the calculated maximum, donât set this parameter. If you set this number manually, Amazon GameLift uses your value as long as itâs less than the calculated maximum.

`--instance-type` (string)

The Amazon EC2 instance type to use for all instances in the fleet. For multi-location fleets, the instance type must be available in the home region and all remote locations. Instance type determines the computing resources and processing power thatâs available to host your game servers. This includes including CPU, memory, storage, and networking capacity.

By default, Amazon GameLift selects an instance type that fits the needs of your container groups and is available in all selected fleet locations. You can also choose to manually set this parameter. See [Amazon Elastic Compute Cloud Instance Types](http://aws.amazon.com/ec2/instance-types/) for detailed descriptions of Amazon EC2 instance types.

You canât update this fleet property later.

`--billing-type` (string)

Indicates whether to use On-Demand or Spot instances for this fleet. Learn more about when to use [On-Demand versus Spot Instances](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot) . This fleet property canât be changed after the fleet is created.

By default, this property is set to `ON_DEMAND` .

You canât update this fleet property later.

Possible values:

- `ON_DEMAND`
- `SPOT`

`--locations` (list)

A set of locations to deploy container fleet instances to. You can add any Amazon Web Services Region or Local Zone thatâs supported by Amazon GameLift. Provide a list of one or more Amazon Web Services Region codes, such as `us-west-2` , or Local Zone names. Also include the fleetâs home Region, which is the Amazon Web Services Region where the fleet is created. For a list of supported Regions and Local Zones, see [Amazon GameLift service locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html) for managed hosting.

(structure)

A remote location where a multi-location fleet can deploy game servers for game hosting.

Location -> (string)

An Amazon Web Services Region code, such as `us-west-2` . For a list of supported Regions and Local Zones, see [Amazon GameLift service locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html) for managed hosting.

Shorthand Syntax:

```
Location=string ...
```

JSON Syntax:

```
[
  {
    "Location": "string"
  }
  ...
]
```

`--metric-groups` (list)

The name of an Amazon Web Services CloudWatch metric group to add this fleet to. You can use a metric group to aggregate metrics for multiple fleets. You can specify an existing metric group name or use a new name to create a new metric group. Each fleet can have only one metric group, but you can change this value at any time.

(string)

Syntax:

```
"string" "string" ...
```

`--new-game-session-protection-policy` (string)

Determines whether Amazon GameLift can shut down game sessions on the fleet that are actively running and hosting players. Amazon GameLift might prompt an instance shutdown when scaling down fleet capacity or when retiring unhealthy instances. You can also set game session protection for individual game sessions using [UpdateGameSession](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/gamelift/latest/apireference/API_UpdateGameSession.html) .

- **NoProtection** â Game sessions can be shut down during active gameplay.
- **FullProtection** â Game sessions in `ACTIVE` status canât be shut down.

By default, this property is set to `NoProtection` .

Possible values:

- `NoProtection`
- `FullProtection`

`--game-session-creation-limit-policy` (structure)

A policy that limits the number of game sessions that each individual player can create on instances in this fleet. The limit applies for a specified span of time.

NewGameSessionsPerCreator -> (integer)

A policy that puts limits on the number of game sessions that a player can create within a specified span of time. With this policy, you can control playersâ ability to consume available resources.

The policy evaluates when a player tries to create a new game session. On receiving a `CreateGameSession` request, Amazon GameLift checks that the player (identified by `CreatorId` ) has created fewer than game session limit in the specified time period.

PolicyPeriodInMinutes -> (integer)

The time span used in evaluating the resource creation limit policy.

Shorthand Syntax:

```
NewGameSessionsPerCreator=integer,PolicyPeriodInMinutes=integer
```

JSON Syntax:

```
{
  "NewGameSessionsPerCreator": integer,
  "PolicyPeriodInMinutes": integer
}
```

`--log-configuration` (structure)

A method for collecting container logs for the fleet. Amazon GameLift saves all standard output for each container in logs, including game session logs. You can select from the following methods:

- `CLOUDWATCH` â Send logs to an Amazon CloudWatch log group that you define. Each container emits a log stream, which is organized in the log group.
- `S3` â Store logs in an Amazon S3 bucket that you define.
- `NONE` â Donât collect container logs.

By default, this property is set to `CLOUDWATCH` .

Amazon GameLift requires permissions to send logs other Amazon Web Services services in your account. These permissions are included in the IAM fleet role for this container fleet (see `FleetRoleArn)` .

LogDestination -> (string)

The type of log collection to use for a fleet.

- `CLOUDWATCH` â (default value) Send logs to an Amazon CloudWatch log group that you define. Each container emits a log stream, which is organized in the log group.
- `S3` â Store logs in an Amazon S3 bucket that you define. This bucket must reside in the fleetâs home Amazon Web Services Region.
- `NONE` â Donât collect container logs.

S3BucketName -> (string)

If log destination is `S3` , logs are sent to the specified Amazon S3 bucket name.

LogGroupArn -> (string)

If log destination is `CLOUDWATCH` , logs are sent to the specified log group in Amazon CloudWatch.

Shorthand Syntax:

```
LogDestination=string,S3BucketName=string,LogGroupArn=string
```

JSON Syntax:

```
{
  "LogDestination": "NONE"|"CLOUDWATCH"|"S3",
  "S3BucketName": "string",
  "LogGroupArn": "string"
}
```

`--tags` (list)

A list of labels to assign to the new fleet resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources are useful for resource management, access management and cost allocation. For more information, see [Tagging Amazon Web Services Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference* .

(structure)

A label that you can assign to a Amazon GameLift resource.

**Learn more**

[Tagging Amazon Web Services Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference*

[Amazon Web Services Tagging Strategies](http://aws.amazon.com/answers/account-management/aws-tagging-strategies/)

**Related actions**

[All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

Key -> (string)

The key for a developer-defined key value pair for tagging an Amazon Web Services resource.

Value -> (string)

The value for a developer-defined key value pair for tagging an Amazon Web Services resource.

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

ContainerFleet -> (structure)

The properties for the new container fleet, including current status. All fleets are initially placed in `PENDING` status.

FleetId -> (string)

A unique identifier for the container fleet to retrieve.

FleetArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) that is assigned to a Amazon GameLift fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912` . In a GameLift fleet ARN, the resource ID matches the `FleetId` value.

FleetRoleArn -> (string)

The unique identifier for an Identity and Access Management (IAM) role with permissions to run your containers on resources that are managed by Amazon GameLift. See [Set up an IAM service role](https://docs.aws.amazon.com/gamelift/latest/developerguide/setting-up-role.html) . This fleet property canât be changed.

GameServerContainerGroupDefinitionName -> (string)

The name of the fleetâs game server container group definition, which describes how to deploy containers with your game server build and support software onto each fleet instance.

GameServerContainerGroupDefinitionArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) that is assigned to the fleetâs game server container group. The ARN value also identifies the specific container group definition version in use.

PerInstanceContainerGroupDefinitionName -> (string)

The name of the fleetâs per-instance container group definition.

PerInstanceContainerGroupDefinitionArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) that is assigned to the fleetâs per-instance container group. The ARN value also identifies the specific container group definition version in use.

InstanceConnectionPortRange -> (structure)

The set of port numbers to open on each instance in a container fleet. Connection ports are used by inbound traffic to connect with processes that are running in containers on the fleet.

FromPort -> (integer)

Starting value for the port range.

ToPort -> (integer)

Ending value for the port. Port numbers are end-inclusive. This value must be equal to or greater than `FromPort` .

InstanceInboundPermissions -> (list)

The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet.

(structure)

A range of IP addresses and port settings that allow inbound traffic to connect to processes on an instance in a fleet. Processes are assigned an IP address/port number combination, which must fall into the fleetâs allowed ranges.

For Amazon GameLift Realtime fleets, Amazon GameLift automatically opens two port ranges, one for TCP messaging and one for UDP.

FromPort -> (integer)

A starting value for a range of allowed port numbers.

For fleets using Linux builds, only ports `22` and `1026-60000` are valid.

For fleets using Windows builds, only ports `1026-60000` are valid.

ToPort -> (integer)

An ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than `FromPort` .

For fleets using Linux builds, only ports `22` and `1026-60000` are valid.

For fleets using Windows builds, only ports `1026-60000` are valid.

IpRange -> (string)

A range of allowed IP addresses. This value must be expressed in CIDR notation. Example: â`000.000.000.000/[subnet mask]` â or optionally the shortened version â`0.0.0.0/[subnet mask]` â.

Protocol -> (string)

The network communication protocol used by the fleet.

GameServerContainerGroupsPerInstance -> (integer)

The number of times to replicate the game server container group on each fleet instance.

MaximumGameServerContainerGroupsPerInstance -> (integer)

The calculated maximum number of game server container group that can be deployed on each fleet instance. The calculation depends on the resource needs of the container group and the CPU and memory resources of the fleetâs instance type.

InstanceType -> (string)

The Amazon EC2 instance type to use for all instances in the fleet. Instance type determines the computing resources and processing power thatâs available to host your game servers. This includes including CPU, memory, storage, and networking capacity. You canât update this fleet property.

BillingType -> (string)

Indicates whether the fleet uses On-Demand or Spot instances for this fleet. Learn more about when to use [On-Demand versus Spot Instances](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot) . You canât update this fleet property.

By default, this property is set to `ON_DEMAND` .

Description -> (string)

A meaningful description of the container fleet.

CreationTime -> (timestamp)

A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ).

MetricGroups -> (list)

The name of an Amazon Web Services CloudWatch metric group to add this fleet to. Metric groups aggregate metrics for multiple fleets.

(string)

NewGameSessionProtectionPolicy -> (string)

Determines whether Amazon GameLift can shut down game sessions on the fleet that are actively running and hosting players. Amazon GameLift might prompt an instance shutdown when scaling down fleet capacity or when retiring unhealthy instances. You can also set game session protection for individual game sessions using [UpdateGameSession](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/gamelift/latest/apireference/API_UpdateGameSession.html) .

- **NoProtection** â Game sessions can be shut down during active gameplay.
- **FullProtection** â Game sessions in `ACTIVE` status canât be shut down.

GameSessionCreationLimitPolicy -> (structure)

A policy that limits the number of game sessions that each individual player can create on instances in this fleet. The limit applies for a specified span of time.

NewGameSessionsPerCreator -> (integer)

A policy that puts limits on the number of game sessions that a player can create within a specified span of time. With this policy, you can control playersâ ability to consume available resources.

The policy evaluates when a player tries to create a new game session. On receiving a `CreateGameSession` request, Amazon GameLift checks that the player (identified by `CreatorId` ) has created fewer than game session limit in the specified time period.

PolicyPeriodInMinutes -> (integer)

The time span used in evaluating the resource creation limit policy.

Status -> (string)

The current status of the container fleet.

- `PENDING` â A new container fleet has been requested.
- `CREATING` â A new container fleet resource is being created.
- `CREATED` â A new container fleet resource has been created. No fleet instances have been deployed.
- `ACTIVATING` â New container fleet instances are being deployed.
- `ACTIVE` â The container fleet has been deployed and is ready to host game sessions.
- `UPDATING` â Updates to the container fleet is being updated. A deployment is in progress.

DeploymentDetails -> (structure)

Information about the most recent deployment for the container fleet.

LatestDeploymentId -> (string)

A unique identifier for a fleet deployment.

LogConfiguration -> (structure)

The method that is used to collect container logs for the fleet. Amazon GameLift saves all standard output for each container in logs, including game session logs.

- `CLOUDWATCH` â Send logs to an Amazon CloudWatch log group that you define. Each container emits a log stream, which is organized in the log group.
- `S3` â Store logs in an Amazon S3 bucket that you define.
- `NONE` â Donât collect container logs.

LogDestination -> (string)

The type of log collection to use for a fleet.

- `CLOUDWATCH` â (default value) Send logs to an Amazon CloudWatch log group that you define. Each container emits a log stream, which is organized in the log group.
- `S3` â Store logs in an Amazon S3 bucket that you define. This bucket must reside in the fleetâs home Amazon Web Services Region.
- `NONE` â Donât collect container logs.

S3BucketName -> (string)

If log destination is `S3` , logs are sent to the specified Amazon S3 bucket name.

LogGroupArn -> (string)

If log destination is `CLOUDWATCH` , logs are sent to the specified log group in Amazon CloudWatch.

LocationAttributes -> (list)

Information about the container fleetâs remote locations where fleet instances are deployed.

(structure)

Details about a location in a multi-location container fleet.

Location -> (string)

A location identifier.

Status -> (string)

The status of fleet activity in the location.

- `PENDING` â A new container fleet has been requested.
- `CREATING` â A new container fleet resource is being created.
- `CREATED` â A new container fleet resource has been created. No fleet instances have been deployed.
- `ACTIVATING` â New container fleet instances are being deployed.
- `ACTIVE` â The container fleet has been deployed and is ready to host game sessions.
- `UPDATING` â Updates to the container fleet is being updated. A deployment is in progress.