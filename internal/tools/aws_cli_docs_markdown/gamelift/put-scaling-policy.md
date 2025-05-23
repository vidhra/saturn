# put-scaling-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/put-scaling-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/put-scaling-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# put-scaling-policy

## Description

Creates or updates a scaling policy for a fleet. Scaling policies are used to automatically scale a fleetâs hosting capacity to meet player demand. An active scaling policy instructs Amazon GameLift to track a fleet metric and automatically change the fleetâs capacity when a certain threshold is reached. There are two types of scaling policies: target-based and rule-based. Use a target-based policy to quickly and efficiently manage fleet scaling; this option is the most commonly used. Use rule-based policies when you need to exert fine-grained control over auto-scaling.

Fleets can have multiple scaling policies of each type in force at the same time; you can have one target-based policy, one or multiple rule-based scaling policies, or both. We recommend caution, however, because multiple auto-scaling policies can have unintended consequences.

Learn more about how to work with auto-scaling in [Set Up Fleet Automatic Scaling](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-autoscaling.html) .

**Target-based policy**

A target-based policy tracks a single metric: PercentAvailableGameSessions. This metric tells us how much of a fleetâs hosting capacity is ready to host game sessions but is not currently in use. This is the fleetâs buffer; it measures the additional player demand that the fleet could handle at current capacity. With a target-based policy, you set your ideal buffer size and leave it to Amazon GameLift to take whatever action is needed to maintain that target.

For example, you might choose to maintain a 10% buffer for a fleet that has the capacity to host 100 simultaneous game sessions. This policy tells Amazon GameLift to take action whenever the fleetâs available capacity falls below or rises above 10 game sessions. Amazon GameLift will start new instances or stop unused instances in order to return to the 10% buffer.

To create or update a target-based policy, specify a fleet ID and name, and set the policy type to âTargetBasedâ. Specify the metric to track (PercentAvailableGameSessions) and reference a `TargetConfiguration` object with your desired buffer value. Exclude all other parameters. On a successful request, the policy name is returned. The scaling policy is automatically in force as soon as itâs successfully created. If the fleetâs auto-scaling actions are temporarily suspended, the new policy will be in force once the fleet actions are restarted.

**Rule-based policy**

A rule-based policy tracks specified fleet metric, sets a threshold value, and specifies the type of action to initiate when triggered. With a rule-based policy, you can select from several available fleet metrics. Each policy specifies whether to scale up or scale down (and by how much), so you need one policy for each type of action.

For example, a policy may make the following statement: âIf the percentage of idle instances is greater than 20% for more than 15 minutes, then reduce the fleet capacity by 10%.â

A policyâs rule statement has the following structure:

If `[MetricName]` is `[ComparisonOperator]` `[Threshold]` for `[EvaluationPeriods]` minutes, then `[ScalingAdjustmentType]` to/by `[ScalingAdjustment]` .

To implement the example, the rule statement would look like this:

If `[PercentIdleInstances]` is `[GreaterThanThreshold]` `[20]` for `[15]` minutes, then `[PercentChangeInCapacity]` to/by `[10]` .

To create or update a scaling policy, specify a unique combination of name and fleet ID, and set the policy type to âRuleBasedâ. Specify the parameter values for a policy rule statement. On a successful request, the policy name is returned. Scaling policies are automatically in force as soon as theyâre successfully created. If the fleetâs auto-scaling actions are temporarily suspended, the new policy will be in force once the fleet actions are restarted.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/PutScalingPolicy)

## Synopsis

```
put-scaling-policy
--name <value>
--fleet-id <value>
[--scaling-adjustment <value>]
[--scaling-adjustment-type <value>]
[--threshold <value>]
[--comparison-operator <value>]
[--evaluation-periods <value>]
--metric-name <value>
[--policy-type <value>]
[--target-configuration <value>]
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

A descriptive label that is associated with a fleetâs scaling policy. Policy names do not need to be unique. A fleet can have only one scaling policy with the same name.

`--fleet-id` (string)

A unique identifier for the fleet to apply this policy to. You can use either the fleet ID or ARN value. The fleet cannot be in any of the following statuses: ERROR or DELETING.

`--scaling-adjustment` (integer)

Amount of adjustment to make, based on the scaling adjustment type.

`--scaling-adjustment-type` (string)

The type of adjustment to make to a fleetâs instance count:

- **ChangeInCapacity** â add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.
- **ExactCapacity** â set the instance count to the scaling adjustment value.
- **PercentChangeInCapacity** â increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down; for example, a value of â-10â scales the fleet down by 10%.

Possible values:

- `ChangeInCapacity`
- `ExactCapacity`
- `PercentChangeInCapacity`

`--threshold` (double)

Metric value used to trigger a scaling event.

`--comparison-operator` (string)

Comparison operator to use when measuring the metric against the threshold value.

Possible values:

- `GreaterThanOrEqualToThreshold`
- `GreaterThanThreshold`
- `LessThanThreshold`
- `LessThanOrEqualToThreshold`

`--evaluation-periods` (integer)

Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.

`--metric-name` (string)

Name of the Amazon GameLift-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see [Monitor Amazon GameLift with Amazon CloudWatch](https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html) .

- **ActivatingGameSessions** â Game sessions in the process of being created.
- **ActiveGameSessions** â Game sessions that are currently running.
- **ActiveInstances** â Fleet instances that are currently running at least one game session.
- **AvailableGameSessions** â Additional game sessions that fleet could host simultaneously, given current capacity.
- **AvailablePlayerSessions** â Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included.
- **CurrentPlayerSessions** â Player slots in active game sessions that are being used by a player or are reserved for a player.
- **IdleInstances** â Active instances that are currently hosting zero game sessions.
- **PercentAvailableGameSessions** â Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy.
- **PercentIdleInstances** â Percentage of the total number of active instances that are hosting zero game sessions.
- **QueueDepth** â Pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
- **WaitTime** â Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.

Possible values:

- `ActivatingGameSessions`
- `ActiveGameSessions`
- `ActiveInstances`
- `AvailableGameSessions`
- `AvailablePlayerSessions`
- `CurrentPlayerSessions`
- `IdleInstances`
- `PercentAvailableGameSessions`
- `PercentIdleInstances`
- `QueueDepth`
- `WaitTime`
- `ConcurrentActivatableGameSessions`

`--policy-type` (string)

The type of scaling policy to create. For a target-based policy, set the parameter *MetricName* to âPercentAvailableGameSessionsâ and specify a *TargetConfiguration* . For a rule-based policy set the following parameters: *MetricName* , *ComparisonOperator* , *Threshold* , *EvaluationPeriods* , *ScalingAdjustmentType* , and *ScalingAdjustment* .

Possible values:

- `RuleBased`
- `TargetBased`

`--target-configuration` (structure)

An object that contains settings for a target-based scaling policy.

TargetValue -> (double)

Desired value to use with a target-based scaling policy. The value must be relevant for whatever metric the scaling policy is using. For example, in a policy using the metric PercentAvailableGameSessions, the target value should be the preferred size of the fleetâs buffer (the percent of capacity that should be idle and ready for new game sessions).

Shorthand Syntax:

```
TargetValue=double
```

JSON Syntax:

```
{
  "TargetValue": double
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

Name -> (string)

A descriptive label that is associated with a fleetâs scaling policy. Policy names do not need to be unique.