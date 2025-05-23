# create-fleetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-fleet.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-fleet.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# create-fleet

## Description

Creates a fleet of compute resources to host your game servers. Use this operation to set up the following types of fleets based on compute type:

**Managed EC2 fleet**

An EC2 fleet is a set of Amazon Elastic Compute Cloud (Amazon EC2) instances. Your game server build is deployed to each fleet instance. Amazon GameLift manages the fleetâs instances and controls the lifecycle of game server processes, which host game sessions for players. EC2 fleets can have instances in multiple locations. Each instance in the fleet is designated a `Compute` .

To create an EC2 fleet, provide these required parameters:

- Either `BuildId` or `ScriptId`
- `ComputeType` set to `EC2` (the default value)
- `EC2InboundPermissions`
- `EC2InstanceType`
- `FleetType`
- `Name`
- `RuntimeConfiguration` with at least one `ServerProcesses` configuration

If successful, this operation creates a new fleet resource and places it in `NEW` status while Amazon GameLift initiates the [fleet creation workflow](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-all.html#fleets-creation-workflow) . To debug your fleet, fetch logs, view performance metrics or other actions on the fleet, create a development fleet with port 22/3389 open. As a best practice, we recommend opening ports for remote access only when you need them and closing them when youâre finished.

When the fleet status is ACTIVE, you can adjust capacity settings and turn autoscaling on/off for each location.

**Anywhere fleet**

An Anywhere fleet represents compute resources that are not owned or managed by Amazon GameLift. You might create an Anywhere fleet with your local machine for testing, or use one to host game servers with on-premises hardware or other game hosting solutions.

To create an Anywhere fleet, provide these required parameters:

- `ComputeType` set to `ANYWHERE`
- `Locations` specifying a custom location
- `Name`

If successful, this operation creates a new fleet resource and places it in `ACTIVE` status. You can register computes with a fleet in `ACTIVE` status.

**Learn more**

[Setting up fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

[Debug fleet creation issues](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-debug.html#fleets-creating-debug-creation)

[Multi-location fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/CreateFleet)

## Synopsis

```
create-fleet
--name <value>
[--description <value>]
[--build-id <value>]
[--script-id <value>]
[--server-launch-path <value>]
[--server-launch-parameters <value>]
[--log-paths <value>]
[--ec2-instance-type <value>]
[--ec2-inbound-permissions <value>]
[--new-game-session-protection-policy <value>]
[--runtime-configuration <value>]
[--resource-creation-limit-policy <value>]
[--metric-groups <value>]
[--peer-vpc-aws-account-id <value>]
[--peer-vpc-id <value>]
[--fleet-type <value>]
[--instance-role-arn <value>]
[--certificate-configuration <value>]
[--locations <value>]
[--tags <value>]
[--compute-type <value>]
[--anywhere-configuration <value>]
[--instance-role-credentials-provider <value>]
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

A descriptive label that is associated with a fleet. Fleet names do not need to be unique.

`--description` (string)

A description for the fleet.

`--build-id` (string)

The unique identifier for a custom game server build to be deployed to a fleet with compute type `EC2` . You can use either the build ID or ARN. The build must be uploaded to Amazon GameLift and in `READY` status. This fleet property canât be changed after the fleet is created.

`--script-id` (string)

The unique identifier for a Realtime configuration script to be deployed to a fleet with compute type `EC2` . You can use either the script ID or ARN. Scripts must be uploaded to Amazon GameLift prior to creating the fleet. This fleet property canât be changed after the fleet is created.

`--server-launch-path` (string)

**This parameter is no longer used.** Specify a server launch path using the `RuntimeConfiguration` parameter. Requests that use this parameter instead continue to be valid.

`--server-launch-parameters` (string)

**This parameter is no longer used.** Specify server launch parameters using the `RuntimeConfiguration` parameter. Requests that use this parameter instead continue to be valid.

`--log-paths` (list)

**This parameter is no longer used.** To specify where Amazon GameLift should store log files once a server process shuts down, use the Amazon GameLift server API `ProcessReady()` and specify one or more directory paths in `logParameters` . For more information, see [Initialize the server process](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-initialize) in the *Amazon GameLift Developer Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--ec2-instance-type` (string)

The Amazon GameLift-supported Amazon EC2 instance type to use with managed EC2 fleets. Instance type determines the computing resources that will be used to host your game servers, including CPU, memory, storage, and networking capacity. See [Amazon Elastic Compute Cloud Instance Types](http://aws.amazon.com/ec2/instance-types/) for detailed descriptions of Amazon EC2 instance types.

Possible values:

- `t2.micro`
- `t2.small`
- `t2.medium`
- `t2.large`
- `c3.large`
- `c3.xlarge`
- `c3.2xlarge`
- `c3.4xlarge`
- `c3.8xlarge`
- `c4.large`
- `c4.xlarge`
- `c4.2xlarge`
- `c4.4xlarge`
- `c4.8xlarge`
- `c5.large`
- `c5.xlarge`
- `c5.2xlarge`
- `c5.4xlarge`
- `c5.9xlarge`
- `c5.12xlarge`
- `c5.18xlarge`
- `c5.24xlarge`
- `c5a.large`
- `c5a.xlarge`
- `c5a.2xlarge`
- `c5a.4xlarge`
- `c5a.8xlarge`
- `c5a.12xlarge`
- `c5a.16xlarge`
- `c5a.24xlarge`
- `r3.large`
- `r3.xlarge`
- `r3.2xlarge`
- `r3.4xlarge`
- `r3.8xlarge`
- `r4.large`
- `r4.xlarge`
- `r4.2xlarge`
- `r4.4xlarge`
- `r4.8xlarge`
- `r4.16xlarge`
- `r5.large`
- `r5.xlarge`
- `r5.2xlarge`
- `r5.4xlarge`
- `r5.8xlarge`
- `r5.12xlarge`
- `r5.16xlarge`
- `r5.24xlarge`
- `r5a.large`
- `r5a.xlarge`
- `r5a.2xlarge`
- `r5a.4xlarge`
- `r5a.8xlarge`
- `r5a.12xlarge`
- `r5a.16xlarge`
- `r5a.24xlarge`
- `m3.medium`
- `m3.large`
- `m3.xlarge`
- `m3.2xlarge`
- `m4.large`
- `m4.xlarge`
- `m4.2xlarge`
- `m4.4xlarge`
- `m4.10xlarge`
- `m5.large`
- `m5.xlarge`
- `m5.2xlarge`
- `m5.4xlarge`
- `m5.8xlarge`
- `m5.12xlarge`
- `m5.16xlarge`
- `m5.24xlarge`
- `m5a.large`
- `m5a.xlarge`
- `m5a.2xlarge`
- `m5a.4xlarge`
- `m5a.8xlarge`
- `m5a.12xlarge`
- `m5a.16xlarge`
- `m5a.24xlarge`
- `c5d.large`
- `c5d.xlarge`
- `c5d.2xlarge`
- `c5d.4xlarge`
- `c5d.9xlarge`
- `c5d.12xlarge`
- `c5d.18xlarge`
- `c5d.24xlarge`
- `c6a.large`
- `c6a.xlarge`
- `c6a.2xlarge`
- `c6a.4xlarge`
- `c6a.8xlarge`
- `c6a.12xlarge`
- `c6a.16xlarge`
- `c6a.24xlarge`
- `c6i.large`
- `c6i.xlarge`
- `c6i.2xlarge`
- `c6i.4xlarge`
- `c6i.8xlarge`
- `c6i.12xlarge`
- `c6i.16xlarge`
- `c6i.24xlarge`
- `r5d.large`
- `r5d.xlarge`
- `r5d.2xlarge`
- `r5d.4xlarge`
- `r5d.8xlarge`
- `r5d.12xlarge`
- `r5d.16xlarge`
- `r5d.24xlarge`
- `m6g.medium`
- `m6g.large`
- `m6g.xlarge`
- `m6g.2xlarge`
- `m6g.4xlarge`
- `m6g.8xlarge`
- `m6g.12xlarge`
- `m6g.16xlarge`
- `c6g.medium`
- `c6g.large`
- `c6g.xlarge`
- `c6g.2xlarge`
- `c6g.4xlarge`
- `c6g.8xlarge`
- `c6g.12xlarge`
- `c6g.16xlarge`
- `r6g.medium`
- `r6g.large`
- `r6g.xlarge`
- `r6g.2xlarge`
- `r6g.4xlarge`
- `r6g.8xlarge`
- `r6g.12xlarge`
- `r6g.16xlarge`
- `c6gn.medium`
- `c6gn.large`
- `c6gn.xlarge`
- `c6gn.2xlarge`
- `c6gn.4xlarge`
- `c6gn.8xlarge`
- `c6gn.12xlarge`
- `c6gn.16xlarge`
- `c7g.medium`
- `c7g.large`
- `c7g.xlarge`
- `c7g.2xlarge`
- `c7g.4xlarge`
- `c7g.8xlarge`
- `c7g.12xlarge`
- `c7g.16xlarge`
- `r7g.medium`
- `r7g.large`
- `r7g.xlarge`
- `r7g.2xlarge`
- `r7g.4xlarge`
- `r7g.8xlarge`
- `r7g.12xlarge`
- `r7g.16xlarge`
- `m7g.medium`
- `m7g.large`
- `m7g.xlarge`
- `m7g.2xlarge`
- `m7g.4xlarge`
- `m7g.8xlarge`
- `m7g.12xlarge`
- `m7g.16xlarge`
- `g5g.xlarge`
- `g5g.2xlarge`
- `g5g.4xlarge`
- `g5g.8xlarge`
- `g5g.16xlarge`
- `r6i.large`
- `r6i.xlarge`
- `r6i.2xlarge`
- `r6i.4xlarge`
- `r6i.8xlarge`
- `r6i.12xlarge`
- `r6i.16xlarge`
- `c6gd.medium`
- `c6gd.large`
- `c6gd.xlarge`
- `c6gd.2xlarge`
- `c6gd.4xlarge`
- `c6gd.8xlarge`
- `c6gd.12xlarge`
- `c6gd.16xlarge`
- `c6in.large`
- `c6in.xlarge`
- `c6in.2xlarge`
- `c6in.4xlarge`
- `c6in.8xlarge`
- `c6in.12xlarge`
- `c6in.16xlarge`
- `c7a.medium`
- `c7a.large`
- `c7a.xlarge`
- `c7a.2xlarge`
- `c7a.4xlarge`
- `c7a.8xlarge`
- `c7a.12xlarge`
- `c7a.16xlarge`
- `c7gd.medium`
- `c7gd.large`
- `c7gd.xlarge`
- `c7gd.2xlarge`
- `c7gd.4xlarge`
- `c7gd.8xlarge`
- `c7gd.12xlarge`
- `c7gd.16xlarge`
- `c7gn.medium`
- `c7gn.large`
- `c7gn.xlarge`
- `c7gn.2xlarge`
- `c7gn.4xlarge`
- `c7gn.8xlarge`
- `c7gn.12xlarge`
- `c7gn.16xlarge`
- `c7i.large`
- `c7i.xlarge`
- `c7i.2xlarge`
- `c7i.4xlarge`
- `c7i.8xlarge`
- `c7i.12xlarge`
- `c7i.16xlarge`
- `m6a.large`
- `m6a.xlarge`
- `m6a.2xlarge`
- `m6a.4xlarge`
- `m6a.8xlarge`
- `m6a.12xlarge`
- `m6a.16xlarge`
- `m6gd.medium`
- `m6gd.large`
- `m6gd.xlarge`
- `m6gd.2xlarge`
- `m6gd.4xlarge`
- `m6gd.8xlarge`
- `m6gd.12xlarge`
- `m6gd.16xlarge`
- `m6i.large`
- `m6i.xlarge`
- `m6i.2xlarge`
- `m6i.4xlarge`
- `m6i.8xlarge`
- `m6i.12xlarge`
- `m6i.16xlarge`
- `m7a.medium`
- `m7a.large`
- `m7a.xlarge`
- `m7a.2xlarge`
- `m7a.4xlarge`
- `m7a.8xlarge`
- `m7a.12xlarge`
- `m7a.16xlarge`
- `m7gd.medium`
- `m7gd.large`
- `m7gd.xlarge`
- `m7gd.2xlarge`
- `m7gd.4xlarge`
- `m7gd.8xlarge`
- `m7gd.12xlarge`
- `m7gd.16xlarge`
- `m7i.large`
- `m7i.xlarge`
- `m7i.2xlarge`
- `m7i.4xlarge`
- `m7i.8xlarge`
- `m7i.12xlarge`
- `m7i.16xlarge`
- `r6gd.medium`
- `r6gd.large`
- `r6gd.xlarge`
- `r6gd.2xlarge`
- `r6gd.4xlarge`
- `r6gd.8xlarge`
- `r6gd.12xlarge`
- `r6gd.16xlarge`
- `r7a.medium`
- `r7a.large`
- `r7a.xlarge`
- `r7a.2xlarge`
- `r7a.4xlarge`
- `r7a.8xlarge`
- `r7a.12xlarge`
- `r7a.16xlarge`
- `r7gd.medium`
- `r7gd.large`
- `r7gd.xlarge`
- `r7gd.2xlarge`
- `r7gd.4xlarge`
- `r7gd.8xlarge`
- `r7gd.12xlarge`
- `r7gd.16xlarge`
- `r7i.large`
- `r7i.xlarge`
- `r7i.2xlarge`
- `r7i.4xlarge`
- `r7i.8xlarge`
- `r7i.12xlarge`
- `r7i.16xlarge`
- `r7i.24xlarge`
- `r7i.48xlarge`
- `c5ad.large`
- `c5ad.xlarge`
- `c5ad.2xlarge`
- `c5ad.4xlarge`
- `c5ad.8xlarge`
- `c5ad.12xlarge`
- `c5ad.16xlarge`
- `c5ad.24xlarge`
- `c5n.large`
- `c5n.xlarge`
- `c5n.2xlarge`
- `c5n.4xlarge`
- `c5n.9xlarge`
- `c5n.18xlarge`
- `r5ad.large`
- `r5ad.xlarge`
- `r5ad.2xlarge`
- `r5ad.4xlarge`
- `r5ad.8xlarge`
- `r5ad.12xlarge`
- `r5ad.16xlarge`
- `r5ad.24xlarge`
- `c6id.large`
- `c6id.xlarge`
- `c6id.2xlarge`
- `c6id.4xlarge`
- `c6id.8xlarge`
- `c6id.12xlarge`
- `c6id.16xlarge`
- `c6id.24xlarge`
- `c6id.32xlarge`
- `c8g.medium`
- `c8g.large`
- `c8g.xlarge`
- `c8g.2xlarge`
- `c8g.4xlarge`
- `c8g.8xlarge`
- `c8g.12xlarge`
- `c8g.16xlarge`
- `c8g.24xlarge`
- `c8g.48xlarge`
- `m5ad.large`
- `m5ad.xlarge`
- `m5ad.2xlarge`
- `m5ad.4xlarge`
- `m5ad.8xlarge`
- `m5ad.12xlarge`
- `m5ad.16xlarge`
- `m5ad.24xlarge`
- `m5d.large`
- `m5d.xlarge`
- `m5d.2xlarge`
- `m5d.4xlarge`
- `m5d.8xlarge`
- `m5d.12xlarge`
- `m5d.16xlarge`
- `m5d.24xlarge`
- `m5dn.large`
- `m5dn.xlarge`
- `m5dn.2xlarge`
- `m5dn.4xlarge`
- `m5dn.8xlarge`
- `m5dn.12xlarge`
- `m5dn.16xlarge`
- `m5dn.24xlarge`
- `m5n.large`
- `m5n.xlarge`
- `m5n.2xlarge`
- `m5n.4xlarge`
- `m5n.8xlarge`
- `m5n.12xlarge`
- `m5n.16xlarge`
- `m5n.24xlarge`
- `m6id.large`
- `m6id.xlarge`
- `m6id.2xlarge`
- `m6id.4xlarge`
- `m6id.8xlarge`
- `m6id.12xlarge`
- `m6id.16xlarge`
- `m6id.24xlarge`
- `m6id.32xlarge`
- `m6idn.large`
- `m6idn.xlarge`
- `m6idn.2xlarge`
- `m6idn.4xlarge`
- `m6idn.8xlarge`
- `m6idn.12xlarge`
- `m6idn.16xlarge`
- `m6idn.24xlarge`
- `m6idn.32xlarge`
- `m6in.large`
- `m6in.xlarge`
- `m6in.2xlarge`
- `m6in.4xlarge`
- `m6in.8xlarge`
- `m6in.12xlarge`
- `m6in.16xlarge`
- `m6in.24xlarge`
- `m6in.32xlarge`
- `m8g.medium`
- `m8g.large`
- `m8g.xlarge`
- `m8g.2xlarge`
- `m8g.4xlarge`
- `m8g.8xlarge`
- `m8g.12xlarge`
- `m8g.16xlarge`
- `m8g.24xlarge`
- `m8g.48xlarge`
- `r5dn.large`
- `r5dn.xlarge`
- `r5dn.2xlarge`
- `r5dn.4xlarge`
- `r5dn.8xlarge`
- `r5dn.12xlarge`
- `r5dn.16xlarge`
- `r5dn.24xlarge`
- `r5n.large`
- `r5n.xlarge`
- `r5n.2xlarge`
- `r5n.4xlarge`
- `r5n.8xlarge`
- `r5n.12xlarge`
- `r5n.16xlarge`
- `r5n.24xlarge`
- `r6a.large`
- `r6a.xlarge`
- `r6a.2xlarge`
- `r6a.4xlarge`
- `r6a.8xlarge`
- `r6a.12xlarge`
- `r6a.16xlarge`
- `r6a.24xlarge`
- `r6a.32xlarge`
- `r6a.48xlarge`
- `r6id.large`
- `r6id.xlarge`
- `r6id.2xlarge`
- `r6id.4xlarge`
- `r6id.8xlarge`
- `r6id.12xlarge`
- `r6id.16xlarge`
- `r6id.24xlarge`
- `r6id.32xlarge`
- `r6idn.large`
- `r6idn.xlarge`
- `r6idn.2xlarge`
- `r6idn.4xlarge`
- `r6idn.8xlarge`
- `r6idn.12xlarge`
- `r6idn.16xlarge`
- `r6idn.24xlarge`
- `r6idn.32xlarge`
- `r6in.large`
- `r6in.xlarge`
- `r6in.2xlarge`
- `r6in.4xlarge`
- `r6in.8xlarge`
- `r6in.12xlarge`
- `r6in.16xlarge`
- `r6in.24xlarge`
- `r6in.32xlarge`
- `r8g.medium`
- `r8g.large`
- `r8g.xlarge`
- `r8g.2xlarge`
- `r8g.4xlarge`
- `r8g.8xlarge`
- `r8g.12xlarge`
- `r8g.16xlarge`
- `r8g.24xlarge`
- `r8g.48xlarge`
- `m4.16xlarge`
- `c6a.32xlarge`
- `c6a.48xlarge`
- `c6i.32xlarge`
- `r6i.24xlarge`
- `r6i.32xlarge`
- `c6in.24xlarge`
- `c6in.32xlarge`
- `c7a.24xlarge`
- `c7a.32xlarge`
- `c7a.48xlarge`
- `c7i.24xlarge`
- `c7i.48xlarge`
- `m6a.24xlarge`
- `m6a.32xlarge`
- `m6a.48xlarge`
- `m6i.24xlarge`
- `m6i.32xlarge`
- `m7a.24xlarge`
- `m7a.32xlarge`
- `m7a.48xlarge`
- `m7i.24xlarge`
- `m7i.48xlarge`
- `r7a.24xlarge`
- `r7a.32xlarge`
- `r7a.48xlarge`

`--ec2-inbound-permissions` (list)

The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet. Set this parameter for managed EC2 fleets. You can leave this parameter empty when creating the fleet, but you must call [https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetPortSettings](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetPortSettings) to set it before players can connect to game sessions. As a best practice, we recommend opening ports for remote access only when you need them and closing them when youâre finished. For Amazon GameLift Realtime fleets, Amazon GameLift automatically sets TCP and UDP ranges.

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

`--new-game-session-protection-policy` (string)

The status of termination protection for active game sessions on the fleet. By default, this property is set to `NoProtection` . You can also set game session protection for an individual game session by calling [UpdateGameSession](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/gamelift/latest/apireference/API_UpdateGameSession.html) .

- **NoProtection** - Game sessions can be terminated during active gameplay as a result of a scale-down event.
- **FullProtection** - Game sessions in `ACTIVE` status cannot be terminated during a scale-down event.

Possible values:

- `NoProtection`
- `FullProtection`

`--runtime-configuration` (structure)

Instructions for how to launch and run server processes on the fleet. Set runtime configuration for managed EC2 fleets. For an Anywhere fleets, set this parameter only if the fleet is running the Amazon GameLift Agent. The runtime configuration defines one or more server process configurations. Each server process identifies a game executable or Realtime script file and the number of processes to run concurrently.

### Note

This parameter replaces the parameters `ServerLaunchPath` and `ServerLaunchParameters` , which are still supported for backward compatibility.

ServerProcesses -> (list)

A collection of server process configurations that identify what server processes to run on fleet computes.

(structure)

A set of instructions for launching server processes on fleet computes. Server processes run either an executable in a custom game build or a Amazon GameLift Realtime script. Server process configurations are part of a fleetâs runtime configuration.

LaunchPath -> (string)

The location of a game build executable or Realtime script. Game builds and Realtime scripts are installed on instances at the root:

- Windows (custom game builds only): `C:\game` . Example: â`C:\game\MyGame\server.exe` â
- Linux: `/local/game` . Examples: â`/local/game/MyGame/server.exe` â or â`/local/game/MyRealtimeScript.js` â

### Note

Amazon GameLift doesnât support the use of setup scripts that launch the game executable. For custom game builds, this parameter must indicate the executable that calls the server SDK operations `initSDK()` and `ProcessReady()` .

Parameters -> (string)

An optional list of parameters to pass to the server executable or Realtime script on launch.

ConcurrentExecutions -> (integer)

The number of server processes using this configuration that run concurrently on each instance or compute.

MaxConcurrentGameSessionActivations -> (integer)

The number of game sessions in status `ACTIVATING` to allow on an instance or compute. This setting limits the instance resources that can be used for new game activations at any one time.

GameSessionActivationTimeoutSeconds -> (integer)

The maximum amount of time (in seconds) allowed to launch a new game session and have it report ready to host players. During this time, the game session is in status `ACTIVATING` . If the game session does not become active before the timeout, it is ended and the game session status is changed to `TERMINATED` .

Shorthand Syntax:

```
ServerProcesses=[{LaunchPath=string,Parameters=string,ConcurrentExecutions=integer},{LaunchPath=string,Parameters=string,ConcurrentExecutions=integer}],MaxConcurrentGameSessionActivations=integer,GameSessionActivationTimeoutSeconds=integer
```

JSON Syntax:

```
{
  "ServerProcesses": [
    {
      "LaunchPath": "string",
      "Parameters": "string",
      "ConcurrentExecutions": integer
    }
    ...
  ],
  "MaxConcurrentGameSessionActivations": integer,
  "GameSessionActivationTimeoutSeconds": integer
}
```

`--resource-creation-limit-policy` (structure)

A policy that limits the number of game sessions that an individual player can create on instances in this fleet within a specified span of time.

NewGameSessionsPerCreator -> (integer)

A policy that puts limits on the number of game sessions that a player can create within a specified span of time. With this policy, you can control playersâ ability to consume available resources.

The policy is evaluated when a player tries to create a new game session. On receiving a `CreateGameSession` request, Amazon GameLift checks that the player (identified by `CreatorId` ) has created fewer than game session limit in the specified time period.

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

`--metric-groups` (list)

The name of an Amazon Web Services CloudWatch metric group to add this fleet to. A metric group is used to aggregate the metrics for multiple fleets. You can specify an existing metric group name or set a new name to create a new metric group. A fleet can be included in only one metric group at a time.

(string)

Syntax:

```
"string" "string" ...
```

`--peer-vpc-aws-account-id` (string)

Used when peering your Amazon GameLift fleet with a VPC, the unique identifier for the Amazon Web Services account that owns the VPC. You can find your account ID in the Amazon Web Services Management Console under account settings.

`--peer-vpc-id` (string)

A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the [VPC Dashboard](https://console.aws.amazon.com/vpc/) in the Amazon Web Services Management Console. Learn more about VPC peering in [VPC Peering with Amazon GameLift Fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html) .

`--fleet-type` (string)

Indicates whether to use On-Demand or Spot instances for this fleet. By default, this property is set to `ON_DEMAND` . Learn more about when to use [On-Demand versus Spot Instances](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot) . This fleet property canât be changed after the fleet is created.

Possible values:

- `ON_DEMAND`
- `SPOT`

`--instance-role-arn` (string)

A unique identifier for an IAM role that manages access to your Amazon Web Services services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a roleâs ARN by using the [IAM dashboard](https://console.aws.amazon.com/iam/) in the Amazon Web Services Management Console. Learn more about using on-box credentials for your game servers at [Access external resources from a game server](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html) . This fleet property canât be changed after the fleet is created.

`--certificate-configuration` (structure)

Prompts Amazon GameLift to generate a TLS/SSL certificate for the fleet. Amazon GameLift uses the certificates to encrypt traffic between game clients and the game servers running on Amazon GameLift. By default, the `CertificateConfiguration` is `DISABLED` . You canât change this property after you create the fleet.

Certificate Manager (ACM) certificates expire after 13 months. Certificate expiration can cause fleets to fail, preventing players from connecting to instances in the fleet. We recommend you replace fleets before 13 months, consider using fleet aliases for a smooth transition.

### Note

ACM isnât available in all Amazon Web Services regions. A fleet creation request with certificate generation enabled in an unsupported Region, fails with a 4xx error. For more information about the supported Regions, see [Supported Regions](https://docs.aws.amazon.com/acm/latest/userguide/acm-regions.html) in the *Certificate Manager User Guide* .

CertificateType -> (string)

Indicates whether a TLS/SSL certificate is generated for a fleet.

Valid values include:

- **GENERATED** - Generate a TLS/SSL certificate for this fleet.
- **DISABLED** - (default) Do not generate a TLS/SSL certificate for this fleet.

Shorthand Syntax:

```
CertificateType=string
```

JSON Syntax:

```
{
  "CertificateType": "DISABLED"|"GENERATED"
}
```

`--locations` (list)

A set of remote locations to deploy additional instances to and manage as a multi-location fleet. Use this parameter when creating a fleet in Amazon Web Services Regions that support multiple locations. You can add any Amazon Web Services Region or Local Zone thatâs supported by Amazon GameLift. Provide a list of one or more Amazon Web Services Region codes, such as `us-west-2` , or Local Zone names. When using this parameter, Amazon GameLift requires you to include your home location in the request. For a list of supported Regions and Local Zones, see [Amazon GameLift service locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html) for managed hosting.

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

`--compute-type` (string)

The type of compute resource used to host your game servers.

- `EC2` â The game server build is deployed to Amazon EC2 instances for cloud hosting. This is the default setting.
- `ANYWHERE` â Game servers and supporting software are deployed to compute resources that you provide and manage. With this compute type, you can also set the `AnywhereConfiguration` parameter.

Possible values:

- `EC2`
- `ANYWHERE`

`--anywhere-configuration` (structure)

Amazon GameLift Anywhere configuration options.

Cost -> (string)

The cost to run your fleet per hour. Amazon GameLift uses the provided cost of your fleet to balance usage in queues. For more information about queues, see [Setting up queues](https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-intro.html) in the *Amazon GameLift Developer Guide* .

Shorthand Syntax:

```
Cost=string
```

JSON Syntax:

```
{
  "Cost": "string"
}
```

`--instance-role-credentials-provider` (string)

Prompts Amazon GameLift to generate a shared credentials file for the IAM role thatâs defined in `InstanceRoleArn` . The shared credentials file is stored on each fleet instance and refreshed as needed. Use shared credentials for applications that are deployed along with the game server executable, if the game server is integrated with server SDK version 5.x. For more information about using shared credentials, see [Communicate with other Amazon Web Services resources from your fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html) .

Possible values:

- `SHARED_CREDENTIAL_FILE`

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To create a basic Linux fleet**

The following `create-fleet` example creates a minimally configured fleet of on-demand Linux instances to host a custom server build. You can complete the configuration by using `update-fleet`.

```
aws gamelift create-fleet \
    --name MegaFrogRaceServer.NA.v2 \
    --description 'Hosts for v2 North America' \
    --build-id build-1111aaaa-22bb-33cc-44dd-5555eeee66ff \
    --certificate-configuration 'CertificateType=GENERATED' \
    --ec2-instance-type c4.large \
    --fleet-type ON_DEMAND \
    --runtime-configuration 'ServerProcesses=[{LaunchPath=/local/game/release-na/MegaFrogRace_Server.exe,ConcurrentExecutions=1}]'
```

Output:

```
{
    "FleetAttributes": {
        "BuildId": "build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "CertificateConfiguration": {
            "CertificateType": "GENERATED"
        },
        "CreationTime": 1496365885.44,
        "Description": "Hosts for v2 North America",
        "FleetArn": "arn:aws:gamelift:us-west-2:444455556666:fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "FleetType": "ON_DEMAND",
        "InstanceType": "c4.large",
        "MetricGroups": ["default"],
        "Name": "MegaFrogRace.NA.v2",
        "NewGameSessionProtectionPolicy": "NoProtection",
        "OperatingSystem": "AMAZON_LINUX",
        "ServerLaunchPath": "/local/game/release-na/MegaFrogRace_Server.exe",
        "Status": "NEW"
    }
}
```

**Example 2: To create a basic Windows fleet**

The following `create-fleet` example creates a minimally configured fleet of spot Windows instances to host a custom server build. You can complete the configuration by using `update-fleet`.

```
aws gamelift create-fleet \
    --name MegaFrogRace.NA.v2 \
    --description 'Hosts for v2 North America' \
    --build-id build-2222aaaa-33bb-44cc-55dd-6666eeee77ff  \
    --certificate-configuration 'CertificateType=GENERATED' \
    --ec2-instance-type c4.large \
    --fleet-type SPOT \
    --runtime-configuration 'ServerProcesses=[{LaunchPath=C:\game\Bin64.Release.Dedicated\MegaFrogRace_Server.exe,ConcurrentExecutions=1}]'
```

Output:

```
{
    "FleetAttributes": {
        "BuildId": "build-2222aaaa-33bb-44cc-55dd-6666eeee77ff",
        "CertificateConfiguration": {
            "CertificateType": "GENERATED"
        },
        "CreationTime": 1496365885.44,
        "Description": "Hosts for v2 North America",
        "FleetArn": "arn:aws:gamelift:us-west-2:444455556666:fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "FleetType": "SPOT",
        "InstanceType": "c4.large",
        "MetricGroups": ["default"],
        "Name": "MegaFrogRace.NA.v2",
        "NewGameSessionProtectionPolicy": "NoProtection",
        "OperatingSystem": "WINDOWS_2012",
        "ServerLaunchPath": "C:\game\Bin64.Release.Dedicated\MegaFrogRace_Server.exe",
        "Status": "NEW"
    }
}
```

**Example 3: To create a fully configured fleet**

The following `create-fleet` example creates a fleet of Spot Windows instances for a custom server build, with most commonly used configuration settings provided.

```
aws gamelift create-fleet \
    --name MegaFrogRace.NA.v2 \
    --description 'Hosts for v2 North America' \
    --build-id build-2222aaaa-33bb-44cc-55dd-6666eeee77ff \
    --certificate-configuration 'CertificateType=GENERATED' \
    --ec2-instance-type c4.large \
    --ec2-inbound-permissions 'FromPort=33435,ToPort=33435,IpRange=10.24.34.0/23,Protocol=UDP' \
    --fleet-type SPOT \
    --new-game-session-protection-policy FullProtection \
    --runtime-configuration file://runtime-config.json \
    --metric-groups default \
    --instance-role-arn 'arn:aws:iam::444455556666:role/GameLiftS3Access'
```

Contents of `runtime-config.json`:

```
GameSessionActivationTimeoutSeconds=300,
 MaxConcurrentGameSessionActivations=2,
 ServerProcesses=[
   {LaunchPath=C:\game\Bin64.Release.Dedicated\MegaFrogRace_Server.exe,Parameters=-debug,ConcurrentExecutions=1},
   {LaunchPath=C:\game\Bin64.Release.Dedicated\MegaFrogRace_Server.exe,ConcurrentExecutions=1}]
```

Output:

```
{
    "FleetAttributes": {
        "InstanceRoleArn": "arn:aws:iam::444455556666:role/GameLiftS3Access",
        "Status": "NEW",
        "InstanceType": "c4.large",
        "FleetArn": "arn:aws:gamelift:us-west-2:444455556666:fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "Description": "Hosts for v2 North America",
        "FleetType": "SPOT",
        "OperatingSystem": "WINDOWS_2012",
        "Name": "MegaFrogRace.NA.v2",
        "CreationTime": 1569309011.11,
        "MetricGroups": [
            "default"
        ],
        "BuildId": "build-2222aaaa-33bb-44cc-55dd-6666eeee77ff",
        "ServerLaunchParameters": "abc",
        "ServerLaunchPath": "C:\\game\\Bin64.Release.Dedicated\\MegaFrogRace_Server.exe",
        "NewGameSessionProtectionPolicy": "FullProtection",
        "CertificateConfiguration": {
            "CertificateType": "GENERATED"
        }
    }
}
```

**Example 4: To create a Realtime Servers fleet**

The following `create-fleet` example creates a fleet of Spot instances with a Realtime configuration script that has been uploaded to Amazon GameLift. All Realtime servers are deployed onto Linux machines. For the purposes of this example, assume that the uploaded Realtime script includes multiple script files, with the `Init()` function located in the script file called `MainScript.js`. As shown, this file is identified as the launch script in the runtime configuration.

```
aws gamelift create-fleet \
    --name MegaFrogRace.NA.realtime \
    --description 'Mega Frog Race Realtime fleet' \
    --script-id script-1111aaaa-22bb-33cc-44dd-5555eeee66ff \
    --ec2-instance-type c4.large \
    --fleet-type SPOT \
    --certificate-configuration 'CertificateType=GENERATED' --runtime-configuration 'ServerProcesses=[{LaunchPath=/local/game/MainScript.js,Parameters=+map Winter444,ConcurrentExecutions=5}]'
```

Output:

```
{
    "FleetAttributes": {
        "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "Status": "NEW",
        "CreationTime": 1569310745.212,
        "InstanceType": "c4.large",
        "NewGameSessionProtectionPolicy": "NoProtection",
        "CertificateConfiguration": {
            "CertificateType": "GENERATED"
        },
        "Name": "MegaFrogRace.NA.realtime",
        "ScriptId": "script-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "FleetArn": "arn:aws:gamelift:us-west-2:444455556666:fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "FleetType": "SPOT",
        "MetricGroups": [
            "default"
        ],
        "Description": "Mega Frog Race Realtime fleet",
        "OperatingSystem": "AMAZON_LINUX"
    }
}
```

## Output

FleetAttributes -> (structure)

The properties for the new fleet, including the current status. All fleets are placed in `NEW` status on creation.

FleetId -> (string)

A unique identifier for the fleet.

FleetArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) that is assigned to a Amazon GameLift fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912` . In a GameLift fleet ARN, the resource ID matches the `FleetId` value.

FleetType -> (string)

Indicates whether the fleet uses On-Demand or Spot instances. For more information, see [On-Demand versus Spot Instances](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot) . This fleet property canât be changed after the fleet is created.

InstanceType -> (string)

The Amazon EC2 instance type that the fleet uses. Instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. See [Amazon Elastic Compute Cloud Instance Types](http://aws.amazon.com/ec2/instance-types/) for detailed descriptions. This attribute is used with fleets where `ComputeType` is `EC2` .

Description -> (string)

A human-readable description of the fleet.

Name -> (string)

A descriptive label that is associated with a fleet. Fleet names do not need to be unique.

CreationTime -> (timestamp)

A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ).

TerminationTime -> (timestamp)

A time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ).

Status -> (string)

Current status of the fleet. Possible fleet statuses include the following:

- NEW â A new fleet resource has been defined and Amazon GameLift has started creating the fleet. Desired instances is set to 1.
- DOWNLOADING/VALIDATING/BUILDING â Amazon GameLift is download the game server build, running install scripts, and then validating the build files. When complete, Amazon GameLift launches a fleet instance.
- ACTIVATING â Amazon GameLift is launching a game server process and testing its connectivity with the Amazon GameLift service.
- ACTIVE â The fleet is now ready to host game sessions.
- ERROR â An error occurred when downloading, validating, building, or activating the fleet.
- DELETING â Hosts are responding to a delete fleet request.
- TERMINATED â The fleet no longer exists.

BuildId -> (string)

A unique identifier for the build resource that is deployed on instances in this fleet. This attribute is used with fleets where `ComputeType` is âEC2â.

BuildArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) associated with the Amazon GameLift build resource that is deployed on instances in this fleet. In a GameLift build ARN, the resource ID matches the `BuildId` value. This attribute is used with fleets where `ComputeType` is âEC2â.

ScriptId -> (string)

A unique identifier for the Realtime script resource that is deployed on instances in this fleet. This attribute is used with fleets where `ComputeType` is âEC2â.

ScriptArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) associated with the GameLift script resource that is deployed on instances in this fleet. In a GameLift script ARN, the resource ID matches the `ScriptId` value.

ServerLaunchPath -> (string)

**This parameter is no longer used.** Server launch paths are now defined using the fleetâs [RuntimeConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/RuntimeConfiguration.html) . Requests that use this parameter continue to be valid.

ServerLaunchParameters -> (string)

**This parameter is no longer used.** Server launch parameters are now defined using the fleetâs runtime configuration. Requests that use this parameter continue to be valid.

LogPaths -> (list)

**This parameter is no longer used.** Game session log paths are now defined using the Amazon GameLift server API `ProcessReady()` `logParameters` . See more information in the [Server API Reference](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api-ref.html#gamelift-sdk-server-api-ref-dataypes-process) .

(string)

NewGameSessionProtectionPolicy -> (string)

The type of game session protection to set on all new instances that are started in the fleet. This attribute is used with fleets where `ComputeType` is `EC2` .

- **NoProtection** â The game session can be terminated during a scale-down event.
- **FullProtection** â If the game session is in an `ACTIVE` status, it cannot be terminated during a scale-down event.

OperatingSystem -> (string)

The operating system of the fleetâs computing resources. A fleetâs operating system is determined by the OS of the build or script that is deployed on this fleet. This attribute is used with fleets where `ComputeType` is `EC2` .

### Note

Amazon Linux 2 (AL2) will reach end of support on 6/30/2025. See more details in the [Amazon Linux 2 FAQs](https://aws.amazon.com/amazon-linux-2/faqs/) . For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See [Migrate to server SDK version 5.](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html)

ResourceCreationLimitPolicy -> (structure)

A policy that puts limits on the number of game sessions that a player can create within a specified span of time. With this policy, you can control playersâ ability to consume available resources.

The policy is evaluated when a player tries to create a new game session. On receiving a `CreateGameSession` request, Amazon GameLift checks that the player (identified by `CreatorId` ) has created fewer than game session limit in the specified time period.

NewGameSessionsPerCreator -> (integer)

A policy that puts limits on the number of game sessions that a player can create within a specified span of time. With this policy, you can control playersâ ability to consume available resources.

The policy is evaluated when a player tries to create a new game session. On receiving a `CreateGameSession` request, Amazon GameLift checks that the player (identified by `CreatorId` ) has created fewer than game session limit in the specified time period.

PolicyPeriodInMinutes -> (integer)

The time span used in evaluating the resource creation limit policy.

MetricGroups -> (list)

Name of a metric group that metrics for this fleet are added to. In Amazon CloudWatch, you can view aggregated metrics for fleets that are in a metric group. A fleet can be included in only one metric group at a time. This attribute is used with fleets where `ComputeType` is `EC2` .

(string)

StoppedActions -> (list)

A list of fleet activity that has been suspended using [StopFleetActions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_StopFleetActions.html) . This includes fleet auto-scaling. This attribute is used with fleets where `ComputeType` is `EC2` .

(string)

InstanceRoleArn -> (string)

A unique identifier for an IAM role that manages access to your Amazon Web Services services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a roleâs ARN by using the [IAM dashboard](https://console.aws.amazon.com/iam/) in the Amazon Web Services Management Console. Learn more about using on-box credentials for your game servers at [Access external resources from a game server](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html) . This attribute is used with fleets where `ComputeType` is `EC2` .

CertificateConfiguration -> (structure)

Determines whether a TLS/SSL certificate is generated for a fleet. This feature must be enabled when creating the fleet. All instances in a fleet share the same certificate.

CertificateType -> (string)

Indicates whether a TLS/SSL certificate is generated for a fleet.

Valid values include:

- **GENERATED** - Generate a TLS/SSL certificate for this fleet.
- **DISABLED** - (default) Do not generate a TLS/SSL certificate for this fleet.

ComputeType -> (string)

The type of compute resource used to host your game servers. You can use your own compute resources with Amazon GameLift Anywhere or use Amazon EC2 instances with managed Amazon GameLift.

AnywhereConfiguration -> (structure)

A set of attributes that are specific to an Anywhere fleet.

Cost -> (string)

The cost to run your fleet per hour. Amazon GameLift uses the provided cost of your fleet to balance usage in queues. For more information about queues, see [Setting up queues](https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-intro.html) in the *Amazon GameLift Developer Guide* .

InstanceRoleCredentialsProvider -> (string)

Indicates that fleet instances maintain a shared credentials file for the IAM role defined in `InstanceRoleArn` . Shared credentials allow applications that are deployed with the game server executable to communicate with other Amazon Web Services resources. This property is used only when the game server is integrated with the server SDK version 5.x. For more information about using shared credentials, see [Communicate with other Amazon Web Services resources from your fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html) . This attribute is used with fleets where `ComputeType` is `EC2` .

LocationStates -> (list)

The fleetâs locations and life-cycle status of each location. For new fleets, the status of all locations is set to `NEW` . During fleet creation, Amazon GameLift updates each location status as instances are deployed there and prepared for game hosting. This list includes an entry for the fleetâs home Region. For fleets with no remote locations, only one entry, representing the home Region, is returned.

(structure)

A fleet location and its life-cycle state. A location state object might be used to describe a fleetâs remote location or home Region. Life-cycle state tracks the progress of launching the first instance in a new location and preparing it for game hosting, and then removing all instances and deleting the location from the fleet.

- **NEW** â A new fleet location has been defined and desired instances is set to 1.
- **DOWNLOADING/VALIDATING/BUILDING/ACTIVATING** â Amazon GameLift is setting up the new fleet location, creating new instances with the game build or Realtime script and starting server processes.
- **ACTIVE** â Hosts can now accept game sessions.
- **ERROR** â An error occurred when downloading, validating, building, or activating the fleet location.
- **DELETING** â Hosts are responding to a delete fleet location request.
- **TERMINATED** â The fleet location no longer exists.
- **NOT_FOUND** â The fleet location was not found. This could be because the custom location was removed or not created.

Location -> (string)

The fleet location, expressed as an Amazon Web Services Region code such as `us-west-2` .

Status -> (string)

The life-cycle status of a fleet location.