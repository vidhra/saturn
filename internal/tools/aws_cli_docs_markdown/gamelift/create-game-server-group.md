# create-game-server-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-game-server-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-game-server-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# create-game-server-group

## Description

**This operation is used with the Amazon GameLift FleetIQ solution and game server groups.**

Creates a Amazon GameLift FleetIQ game server group for managing game hosting on a collection of Amazon Elastic Compute Cloud instances for game hosting. This operation creates the game server group, creates an Auto Scaling group in your Amazon Web Services account, and establishes a link between the two groups. You can view the status of your game server groups in the Amazon GameLift console. Game server group metrics and events are emitted to Amazon CloudWatch.

Before creating a new game server group, you must have the following:

- An Amazon Elastic Compute Cloud launch template that specifies how to launch Amazon Elastic Compute Cloud instances with your game server build. For more information, see [Launching an Instance from a Launch Template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) in the *Amazon Elastic Compute Cloud User Guide* .
- An IAM role that extends limited access to your Amazon Web Services account to allow Amazon GameLift FleetIQ to create and interact with the Auto Scaling group. For more information, see [Create IAM roles for cross-service interaction](https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-iam-permissions-roles.html) in the *Amazon GameLift FleetIQ Developer Guide* .

To create a new game server group, specify a unique group name, IAM role and Amazon Elastic Compute Cloud launch template, and provide a list of instance types that can be used in the group. You must also set initial maximum and minimum limits on the groupâs instance count. You can optionally set an Auto Scaling policy with target tracking based on a Amazon GameLift FleetIQ metric.

Once the game server group and corresponding Auto Scaling group are created, you have full access to change the Auto Scaling groupâs configuration as needed. Several properties that are set when creating a game server group, including maximum/minimum size and auto-scaling policy settings, must be updated directly in the Auto Scaling group. Keep in mind that some Auto Scaling group properties are periodically updated by Amazon GameLift FleetIQ as part of its balancing activities to optimize for availability and cost.

**Learn more**

[Amazon GameLift FleetIQ Guide](https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/CreateGameServerGroup)

## Synopsis

```
create-game-server-group
--game-server-group-name <value>
--role-arn <value>
--min-size <value>
--max-size <value>
--launch-template <value>
--instance-definitions <value>
[--auto-scaling-policy <value>]
[--balancing-strategy <value>]
[--game-server-protection-policy <value>]
[--vpc-subnets <value>]
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

`--game-server-group-name` (string)

An identifier for the new game server group. This value is used to generate unique ARN identifiers for the Amazon EC2 Auto Scaling group and the Amazon GameLift FleetIQ game server group. The name must be unique per Region per Amazon Web Services account.

`--role-arn` (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) for an IAM role that allows Amazon GameLift to access your Amazon EC2 Auto Scaling groups.

`--min-size` (integer)

The minimum number of instances allowed in the Amazon EC2 Auto Scaling group. During automatic scaling events, Amazon GameLift FleetIQ and Amazon EC2 do not scale down the group below this minimum. In production, this value should be set to at least 1. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the Amazon Web Services console or APIs.

`--max-size` (integer)

The maximum number of instances allowed in the Amazon EC2 Auto Scaling group. During automatic scaling events, Amazon GameLift FleetIQ and EC2 do not scale up the group above this maximum. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the Amazon Web Services console or APIs.

`--launch-template` (structure)

The Amazon EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group. You can specify the template using either the template name or ID. For help with creating a launch template, see [Creating a Launch Template for an Auto Scaling Group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html) in the *Amazon Elastic Compute Cloud Auto Scaling User Guide* . After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the Amazon Web Services console or APIs.

### Note

If you specify network interfaces in your launch template, you must explicitly set the property `AssociatePublicIpAddress` to âtrueâ. If no network interface is specified in the launch template, Amazon GameLift FleetIQ uses your accountâs default VPC.

LaunchTemplateId -> (string)

A unique identifier for an existing Amazon EC2 launch template.

LaunchTemplateName -> (string)

A readable identifier for an existing Amazon EC2 launch template.

Version -> (string)

The version of the Amazon EC2 launch template to use. If no version is specified, the default version will be used. With Amazon EC2, you can specify a default version for a launch template. If none is set, the default is the first version created.

Shorthand Syntax:

```
LaunchTemplateId=string,LaunchTemplateName=string,Version=string
```

JSON Syntax:

```
{
  "LaunchTemplateId": "string",
  "LaunchTemplateName": "string",
  "Version": "string"
}
```

`--instance-definitions` (list)

The Amazon EC2 instance types and sizes to use in the Auto Scaling group. The instance definitions must specify at least two different instance types that are supported by Amazon GameLift FleetIQ. For more information on instance types, see [EC2 Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon Elastic Compute Cloud User Guide* . You can optionally specify capacity weighting for each instance type. If no weight value is specified for an instance type, it is set to the default value â1â. For more information about capacity weighting, see [Instance Weighting for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-weighting.html) in the Amazon EC2 Auto Scaling User Guide.

(structure)

**This data type is used with the Amazon GameLift FleetIQ and game server groups.**

An allowed instance type for a game server group. All game server groups must have at least two instance types defined for it. Amazon GameLift FleetIQ periodically evaluates each defined instance type for viability. It then updates the Auto Scaling group with the list of viable instance types.

InstanceType -> (string)

An Amazon EC2 instance type designation.

WeightedCapacity -> (string)

Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group. Instance weights are used by Amazon GameLift FleetIQ to calculate the instance typeâs cost per unit hour and better identify the most cost-effective options. For detailed information on weighting instance capacity, see [Instance Weighting](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-weighting.html) in the *Amazon Elastic Compute Cloud Auto Scaling User Guide* . Default value is â1â.

Shorthand Syntax:

```
InstanceType=string,WeightedCapacity=string ...
```

JSON Syntax:

```
[
  {
    "InstanceType": "c4.large"|"c4.xlarge"|"c4.2xlarge"|"c4.4xlarge"|"c4.8xlarge"|"c5.large"|"c5.xlarge"|"c5.2xlarge"|"c5.4xlarge"|"c5.9xlarge"|"c5.12xlarge"|"c5.18xlarge"|"c5.24xlarge"|"c5a.large"|"c5a.xlarge"|"c5a.2xlarge"|"c5a.4xlarge"|"c5a.8xlarge"|"c5a.12xlarge"|"c5a.16xlarge"|"c5a.24xlarge"|"c6g.medium"|"c6g.large"|"c6g.xlarge"|"c6g.2xlarge"|"c6g.4xlarge"|"c6g.8xlarge"|"c6g.12xlarge"|"c6g.16xlarge"|"r4.large"|"r4.xlarge"|"r4.2xlarge"|"r4.4xlarge"|"r4.8xlarge"|"r4.16xlarge"|"r5.large"|"r5.xlarge"|"r5.2xlarge"|"r5.4xlarge"|"r5.8xlarge"|"r5.12xlarge"|"r5.16xlarge"|"r5.24xlarge"|"r5a.large"|"r5a.xlarge"|"r5a.2xlarge"|"r5a.4xlarge"|"r5a.8xlarge"|"r5a.12xlarge"|"r5a.16xlarge"|"r5a.24xlarge"|"r6g.medium"|"r6g.large"|"r6g.xlarge"|"r6g.2xlarge"|"r6g.4xlarge"|"r6g.8xlarge"|"r6g.12xlarge"|"r6g.16xlarge"|"m4.large"|"m4.xlarge"|"m4.2xlarge"|"m4.4xlarge"|"m4.10xlarge"|"m5.large"|"m5.xlarge"|"m5.2xlarge"|"m5.4xlarge"|"m5.8xlarge"|"m5.12xlarge"|"m5.16xlarge"|"m5.24xlarge"|"m5a.large"|"m5a.xlarge"|"m5a.2xlarge"|"m5a.4xlarge"|"m5a.8xlarge"|"m5a.12xlarge"|"m5a.16xlarge"|"m5a.24xlarge"|"m6g.medium"|"m6g.large"|"m6g.xlarge"|"m6g.2xlarge"|"m6g.4xlarge"|"m6g.8xlarge"|"m6g.12xlarge"|"m6g.16xlarge",
    "WeightedCapacity": "string"
  }
  ...
]
```

`--auto-scaling-policy` (structure)

Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting. The scaling policy uses the metric `"PercentUtilizedGameServers"` to maintain a buffer of idle game servers that can immediately accommodate new games and players. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the Amazon Web Services console or APIs.

EstimatedInstanceWarmup -> (integer)

Length of time, in seconds, it takes for a new instance to start new game server processes and register with Amazon GameLift FleetIQ. Specifying a warm-up time can be useful, particularly with game servers that take a long time to start up, because it avoids prematurely starting new instances.

TargetTrackingConfiguration -> (structure)

Settings for a target-based scaling policy applied to Auto Scaling group. These settings are used to create a target-based policy that tracks the Amazon GameLift FleetIQ metric `"PercentUtilizedGameServers"` and specifies a target value for the metric. As player usage changes, the policy triggers to adjust the game server group capacity so that the metric returns to the target value.

TargetValue -> (double)

Desired value to use with a game server group target-based scaling policy.

Shorthand Syntax:

```
EstimatedInstanceWarmup=integer,TargetTrackingConfiguration={TargetValue=double}
```

JSON Syntax:

```
{
  "EstimatedInstanceWarmup": integer,
  "TargetTrackingConfiguration": {
    "TargetValue": double
  }
}
```

`--balancing-strategy` (string)

Indicates how Amazon GameLift FleetIQ balances the use of Spot Instances and On-Demand Instances in the game server group. Method options include the following:

- `SPOT_ONLY` - Only Spot Instances are used in the game server group. If Spot Instances are unavailable or not viable for game hosting, the game server group provides no hosting capacity until Spot Instances can again be used. Until then, no new instances are started, and the existing nonviable Spot Instances are terminated (after current gameplay ends) and are not replaced.
- `SPOT_PREFERRED` - (default value) Spot Instances are used whenever available in the game server group. If Spot Instances are unavailable, the game server group continues to provide hosting capacity by falling back to On-Demand Instances. Existing nonviable Spot Instances are terminated (after current gameplay ends) and are replaced with new On-Demand Instances.
- `ON_DEMAND_ONLY` - Only On-Demand Instances are used in the game server group. No Spot Instances are used, even when available, while this balancing strategy is in force.

Possible values:

- `SPOT_ONLY`
- `SPOT_PREFERRED`
- `ON_DEMAND_ONLY`

`--game-server-protection-policy` (string)

A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running might be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see ). An exception to this is with Spot Instances, which can be terminated by Amazon Web Services regardless of protection status. This property is set to `NO_PROTECTION` by default.

Possible values:

- `NO_PROTECTION`
- `FULL_PROTECTION`

`--vpc-subnets` (list)

A list of virtual private cloud (VPC) subnets to use with instances in the game server group. By default, all Amazon GameLift FleetIQ-supported Availability Zones are used. You can use this parameter to specify VPCs that youâve set up. This property cannot be updated after the game server group is created, and the corresponding Auto Scaling group will always use the property value that is set with this request, even if the Auto Scaling group is updated directly.

(string)

Syntax:

```
"string" "string" ...
```

`--tags` (list)

A list of labels to assign to the new game server group resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management, and cost allocation. For more information, see [Tagging Amazon Web Services Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference* .

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

GameServerGroup -> (structure)

The newly created game server group object, including the new ARN value for the Amazon GameLift FleetIQ game server group and the objectâs status. The Amazon EC2 Auto Scaling group ARN is initially null, since the group has not yet been created. This value is added once the game server group status reaches `ACTIVE` .

GameServerGroupName -> (string)

A developer-defined identifier for the game server group. The name is unique for each Region in each Amazon Web Services account.

GameServerGroupArn -> (string)

A generated unique ID for the game server group.

RoleArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) for an IAM role that allows Amazon GameLift to access your Amazon EC2 Auto Scaling groups.

InstanceDefinitions -> (list)

The set of Amazon EC2 instance types that Amazon GameLift FleetIQ can use when balancing and automatically scaling instances in the corresponding Auto Scaling group.

(structure)

**This data type is used with the Amazon GameLift FleetIQ and game server groups.**

An allowed instance type for a game server group. All game server groups must have at least two instance types defined for it. Amazon GameLift FleetIQ periodically evaluates each defined instance type for viability. It then updates the Auto Scaling group with the list of viable instance types.

InstanceType -> (string)

An Amazon EC2 instance type designation.

WeightedCapacity -> (string)

Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group. Instance weights are used by Amazon GameLift FleetIQ to calculate the instance typeâs cost per unit hour and better identify the most cost-effective options. For detailed information on weighting instance capacity, see [Instance Weighting](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-weighting.html) in the *Amazon Elastic Compute Cloud Auto Scaling User Guide* . Default value is â1â.

BalancingStrategy -> (string)

Indicates how Amazon GameLift FleetIQ balances the use of Spot Instances and On-Demand Instances in the game server group. Method options include the following:

- `SPOT_ONLY` - Only Spot Instances are used in the game server group. If Spot Instances are unavailable or not viable for game hosting, the game server group provides no hosting capacity until Spot Instances can again be used. Until then, no new instances are started, and the existing nonviable Spot Instances are terminated (after current gameplay ends) and are not replaced.
- `SPOT_PREFERRED` - (default value) Spot Instances are used whenever available in the game server group. If Spot Instances are unavailable, the game server group continues to provide hosting capacity by falling back to On-Demand Instances. Existing nonviable Spot Instances are terminated (after current gameplay ends) and are replaced with new On-Demand Instances.
- `ON_DEMAND_ONLY` - Only On-Demand Instances are used in the game server group. No Spot Instances are used, even when available, while this balancing strategy is in force.

GameServerProtectionPolicy -> (string)

A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running might be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see ). An exception to this is with Spot Instances, which can be terminated by Amazon Web Services regardless of protection status.

AutoScalingGroupArn -> (string)

A generated unique ID for the Amazon EC2 Auto Scaling group that is associated with this game server group.

Status -> (string)

The current status of the game server group. Possible statuses include:

- `NEW` - Amazon GameLift FleetIQ has validated the `CreateGameServerGroup()` request.
- `ACTIVATING` - Amazon GameLift FleetIQ is setting up a game server group, which includes creating an Auto Scaling group in your Amazon Web Services account.
- `ACTIVE` - The game server group has been successfully created.
- `DELETE_SCHEDULED` - A request to delete the game server group has been received.
- `DELETING` - Amazon GameLift FleetIQ has received a valid `DeleteGameServerGroup()` request and is processing it. Amazon GameLift FleetIQ must first complete and release hosts before it deletes the Auto Scaling group and the game server group.
- `DELETED` - The game server group has been successfully deleted.
- `ERROR` - The asynchronous processes of activating or deleting a game server group has failed, resulting in an error state.

StatusReason -> (string)

Additional information about the current game server group status. This information might provide additional insight on groups that are in `ERROR` status.

SuspendedActions -> (list)

A list of activities that are currently suspended for this game server group. If this property is empty, all activities are occurring.

(string)

CreationTime -> (timestamp)

A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ).

LastUpdatedTime -> (timestamp)

A timestamp that indicates when this game server group was last updated.