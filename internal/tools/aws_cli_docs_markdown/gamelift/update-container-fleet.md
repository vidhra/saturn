# update-container-fleetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-container-fleet.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-container-fleet.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# update-container-fleet

## Description

Updates the properties of a managed container fleet. Depending on the properties being updated, this operation might initiate a fleet deployment. You can track deployments for a fleet using [https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetDeployment.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetDeployment.html) .

**Request options**

As with CreateContainerFleet, many fleet properties use common defaults or are calculated based on the fleetâs container group definitions.

- Update fleet properties that result in a fleet deployment. Include only those properties that you want to change. Specify deployment configuration settings.
- Update fleet properties that donât result in a fleet deployment. Include only those properties that you want to change.

Changes to the following properties initiate a fleet deployment:

- `GameServerContainerGroupDefinition`
- `PerInstanceContainerGroupDefinition`
- `GameServerContainerGroupsPerInstance`
- `InstanceInboundPermissions`
- `InstanceConnectionPortRange`
- `LogConfiguration`

**Results**

If successful, this operation updates the container fleet resource, and might initiate a new deployment of fleet resources using the deployment configuration provided. A deployment replaces existing fleet instances with new instances that are deployed with the updated fleet properties. The fleet is placed in `UPDATING` status until the deployment is complete, then return to `ACTIVE` .

You can have only one update deployment active at a time for a fleet. If a second update request initiates a deployment while another deployment is in progress, the first deployment is cancelled.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/UpdateContainerFleet)

## Synopsis

```
update-container-fleet
--fleet-id <value>
[--game-server-container-group-definition-name <value>]
[--per-instance-container-group-definition-name <value>]
[--game-server-container-groups-per-instance <value>]
[--instance-connection-port-range <value>]
[--instance-inbound-permission-authorizations <value>]
[--instance-inbound-permission-revocations <value>]
[--deployment-configuration <value>]
[--description <value>]
[--metric-groups <value>]
[--new-game-session-protection-policy <value>]
[--game-session-creation-limit-policy <value>]
[--log-configuration <value>]
[--remove-attributes <value>]
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

`--fleet-id` (string)

A unique identifier for the container fleet to update. You can use either the fleet ID or ARN value.

`--game-server-container-group-definition-name` (string)

The name or ARN value of a new game server container group definition to deploy on the fleet. If youâre updating the fleet to a specific version of a container group definition, use the ARN value and include the version number. If youâre updating the fleet to the latest version of a container group definition, you can use the name value. You canât remove a fleetâs game server container group definition, you can only update or replace it with another definition.

Update a container group definition by calling [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html) . This operation creates a [ContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html) resource with an incremented version.

`--per-instance-container-group-definition-name` (string)

The name or ARN value of a new per-instance container group definition to deploy on the fleet. If youâre updating the fleet to a specific version of a container group definition, use the ARN value and include the version number. If youâre updating the fleet to the latest version of a container group definition, you can use the name value.

Update a container group definition by calling [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html) . This operation creates a [ContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html) resource with an incremented version.

To remove a fleetâs per-instance container group definition, leave this parameter empty and use the parameter `RemoveAttributes` .

`--game-server-container-groups-per-instance` (integer)

The number of times to replicate the game server container group on each fleet instance. By default, Amazon GameLift calculates the maximum number of game server container groups that can fit on each instance. You can remove this property value to use the calculated value, or set it manually. If you set this number manually, Amazon GameLift uses your value as long as itâs less than the calculated maximum.

`--instance-connection-port-range` (structure)

A revised set of port numbers to open on each fleet instance. By default, Amazon GameLift calculates an optimal port range based on your fleet configuration. If you previously set this parameter manually, you canât reset this to use the calculated settings.

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

`--instance-inbound-permission-authorizations` (list)

A set of ports to add to the container fleetâs inbound permissions.

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

`--instance-inbound-permission-revocations` (list)

A set of ports to remove from the container fleetâs inbound permissions.

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

`--deployment-configuration` (structure)

Instructions for how to deploy updates to a container fleet, if the fleet update initiates a deployment. The deployment configuration lets you determine how to replace fleet instances and what actions to take if the deployment fails.

ProtectionStrategy -> (string)

Determines how fleet deployment activity affects active game sessions on the fleet. With protection, a deployment honors game session protection, and delays actions that would interrupt a protected active game session until the game session ends. Without protection, deployment activity can shut down all running tasks, including active game sessions, regardless of game session protection.

MinimumHealthyPercentage -> (integer)

Sets a minimum level of healthy tasks to maintain during deployment activity.

ImpairmentStrategy -> (string)

Determines what actions to take if a deployment fails. If the fleet is multi-location, this strategy applies across all fleet locations. With a rollback strategy, updated fleet instances are rolled back to the last successful deployment. Alternatively, you can maintain a few impaired containers for the purpose of debugging, while all other tasks return to the last successful deployment.

Shorthand Syntax:

```
ProtectionStrategy=string,MinimumHealthyPercentage=integer,ImpairmentStrategy=string
```

JSON Syntax:

```
{
  "ProtectionStrategy": "WITH_PROTECTION"|"IGNORE_PROTECTION",
  "MinimumHealthyPercentage": integer,
  "ImpairmentStrategy": "MAINTAIN"|"ROLLBACK"
}
```

`--description` (string)

A meaningful description of the container fleet.

`--metric-groups` (list)

The name of an Amazon Web Services CloudWatch metric group to add this fleet to.

(string)

Syntax:

```
"string" "string" ...
```

`--new-game-session-protection-policy` (string)

The game session protection policy to apply to all new game sessions that are started in this fleet. Game sessions that already exist are not affected.

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

The method for collecting container logs for the fleet.

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

`--remove-attributes` (list)

If set, this update removes a fleetâs per-instance container group definition. You canât remove a fleetâs game server container group definition.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  PER_INSTANCE_CONTAINER_GROUP_DEFINITION
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

A collection of container fleet objects for all fleets that match the request criteria.

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