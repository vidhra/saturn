# put-auto-scaling-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/put-auto-scaling-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/put-auto-scaling-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/index.html#cli-aws-emr) ]

# put-auto-scaling-policy

## Description

Creates or updates an automatic scaling policy for a core instance group or task instance group in an Amazon EMR cluster. The automatic scaling policy defines how an instance group dynamically adds and terminates Amazon EC2 instances in response to the value of a CloudWatch metric.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/PutAutoScalingPolicy)

## Synopsis

```
put-auto-scaling-policy
--cluster-id <value>
--instance-group-id <value>
--auto-scaling-policy <value>
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

`--cluster-id` (string)

Specifies the ID of a cluster. The instance group to which the automatic scaling policy is applied is within this cluster.

`--instance-group-id` (string)

Specifies the ID of the instance group to which the automatic scaling policy is applied.

`--auto-scaling-policy` (structure)

Specifies the definition of the automatic scaling policy.

Constraints -> (structure)

The upper and lower Amazon EC2 instance limits for an automatic scaling policy. Automatic scaling activity will not cause an instance group to grow above or below these limits.

MinCapacity -> (integer)

The lower boundary of Amazon EC2 instances in an instance group below which scaling activities are not allowed to shrink. Scale-in activities will not terminate instances below this boundary.

MaxCapacity -> (integer)

The upper boundary of Amazon EC2 instances in an instance group beyond which scaling activities are not allowed to grow. Scale-out activities will not add instances beyond this boundary.

Rules -> (list)

The scale-in and scale-out rules that comprise the automatic scaling policy.

(structure)

A scale-in or scale-out rule that defines scaling activity, including the CloudWatch metric alarm that triggers activity, how Amazon EC2 instances are added or removed, and the periodicity of adjustments. The automatic scaling policy for an instance group can comprise one or more automatic scaling rules.

Name -> (string)

The name used to identify an automatic scaling rule. Rule names must be unique within a scaling policy.

Description -> (string)

A friendly, more verbose description of the automatic scaling rule.

Action -> (structure)

The conditions that trigger an automatic scaling activity.

Market -> (string)

Not available for instance groups. Instance groups use the market type specified for the group.

SimpleScalingPolicyConfiguration -> (structure)

The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.

AdjustmentType -> (string)

The way in which Amazon EC2 instances are added (if `ScalingAdjustment` is a positive number) or terminated (if `ScalingAdjustment` is a negative number) each time the scaling activity is triggered. `CHANGE_IN_CAPACITY` is the default. `CHANGE_IN_CAPACITY` indicates that the Amazon EC2 instance count increments or decrements by `ScalingAdjustment` , which should be expressed as an integer. `PERCENT_CHANGE_IN_CAPACITY` indicates the instance count increments or decrements by the percentage specified by `ScalingAdjustment` , which should be expressed as an integer. For example, 20 indicates an increase in 20% increments of cluster capacity. `EXACT_CAPACITY` indicates the scaling activity results in an instance group with the number of Amazon EC2 instances specified by `ScalingAdjustment` , which should be expressed as a positive integer.

ScalingAdjustment -> (integer)

The amount by which to scale in or scale out, based on the specified `AdjustmentType` . A positive value adds to the instance groupâs Amazon EC2 instance count while a negative number removes instances. If `AdjustmentType` is set to `EXACT_CAPACITY` , the number should only be a positive integer. If `AdjustmentType` is set to `PERCENT_CHANGE_IN_CAPACITY` , the value should express the percentage as an integer. For example, -20 indicates a decrease in 20% increments of cluster capacity.

CoolDown -> (integer)

The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start. The default value is 0.

Trigger -> (structure)

The CloudWatch alarm definition that determines when automatic scaling activity is triggered.

CloudWatchAlarmDefinition -> (structure)

The definition of a CloudWatch metric alarm. When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.

ComparisonOperator -> (string)

Determines how the metric specified by `MetricName` is compared to the value specified by `Threshold` .

EvaluationPeriods -> (integer)

The number of periods, in five-minute increments, during which the alarm condition must exist before the alarm triggers automatic scaling activity. The default value is `1` .

MetricName -> (string)

The name of the CloudWatch metric that is watched to determine an alarm condition.

Namespace -> (string)

The namespace for the CloudWatch metric. The default is `AWS/ElasticMapReduce` .

Period -> (integer)

The period, in seconds, over which the statistic is applied. CloudWatch metrics for Amazon EMR are emitted every five minutes (300 seconds), so if you specify a CloudWatch metric, specify `300` .

Statistic -> (string)

The statistic to apply to the metric associated with the alarm. The default is `AVERAGE` .

Threshold -> (double)

The value against which the specified statistic is compared.

Unit -> (string)

The unit of measure associated with the CloudWatch metric being watched. The value specified for `Unit` must correspond to the units specified in the CloudWatch metric.

Dimensions -> (list)

A CloudWatch metric dimension.

(structure)

A CloudWatch dimension, which is specified using a `Key` (known as a `Name` in CloudWatch), `Value` pair. By default, Amazon EMR uses one dimension whose `Key` is `JobFlowID` and `Value` is a variable representing the cluster ID, which is `${emr.clusterId}` . This enables the rule to bootstrap when the cluster ID becomes available.

Key -> (string)

The dimension name.

Value -> (string)

The dimension value.

JSON Syntax:

```
{
  "Constraints": {
    "MinCapacity": integer,
    "MaxCapacity": integer
  },
  "Rules": [
    {
      "Name": "string",
      "Description": "string",
      "Action": {
        "Market": "ON_DEMAND"|"SPOT",
        "SimpleScalingPolicyConfiguration": {
          "AdjustmentType": "CHANGE_IN_CAPACITY"|"PERCENT_CHANGE_IN_CAPACITY"|"EXACT_CAPACITY",
          "ScalingAdjustment": integer,
          "CoolDown": integer
        }
      },
      "Trigger": {
        "CloudWatchAlarmDefinition": {
          "ComparisonOperator": "GREATER_THAN_OR_EQUAL"|"GREATER_THAN"|"LESS_THAN"|"LESS_THAN_OR_EQUAL",
          "EvaluationPeriods": integer,
          "MetricName": "string",
          "Namespace": "string",
          "Period": integer,
          "Statistic": "SAMPLE_COUNT"|"AVERAGE"|"SUM"|"MINIMUM"|"MAXIMUM",
          "Threshold": double,
          "Unit": "NONE"|"SECONDS"|"MICRO_SECONDS"|"MILLI_SECONDS"|"BYTES"|"KILO_BYTES"|"MEGA_BYTES"|"GIGA_BYTES"|"TERA_BYTES"|"BITS"|"KILO_BITS"|"MEGA_BITS"|"GIGA_BITS"|"TERA_BITS"|"PERCENT"|"COUNT"|"BYTES_PER_SECOND"|"KILO_BYTES_PER_SECOND"|"MEGA_BYTES_PER_SECOND"|"GIGA_BYTES_PER_SECOND"|"TERA_BYTES_PER_SECOND"|"BITS_PER_SECOND"|"KILO_BITS_PER_SECOND"|"MEGA_BITS_PER_SECOND"|"GIGA_BITS_PER_SECOND"|"TERA_BITS_PER_SECOND"|"COUNT_PER_SECOND",
          "Dimensions": [
            {
              "Key": "string",
              "Value": "string"
            }
            ...
          ]
        }
      }
    }
    ...
  ]
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

ClusterId -> (string)

Specifies the ID of a cluster. The instance group to which the automatic scaling policy is applied is within this cluster.

InstanceGroupId -> (string)

Specifies the ID of the instance group to which the scaling policy is applied.

AutoScalingPolicy -> (structure)

The automatic scaling policy definition.

Status -> (structure)

The status of an automatic scaling policy.

State -> (string)

Indicates the status of the automatic scaling policy.

StateChangeReason -> (structure)

The reason for a change in status.

Code -> (string)

The code indicating the reason for the change in status.``USER_REQUEST`` indicates that the scaling policy status was changed by a user. `PROVISION_FAILURE` indicates that the status change was because the policy failed to provision. `CLEANUP_FAILURE` indicates an error.

Message -> (string)

A friendly, more verbose message that accompanies an automatic scaling policy state change.

Constraints -> (structure)

The upper and lower Amazon EC2 instance limits for an automatic scaling policy. Automatic scaling activity will not cause an instance group to grow above or below these limits.

MinCapacity -> (integer)

The lower boundary of Amazon EC2 instances in an instance group below which scaling activities are not allowed to shrink. Scale-in activities will not terminate instances below this boundary.

MaxCapacity -> (integer)

The upper boundary of Amazon EC2 instances in an instance group beyond which scaling activities are not allowed to grow. Scale-out activities will not add instances beyond this boundary.

Rules -> (list)

The scale-in and scale-out rules that comprise the automatic scaling policy.

(structure)

A scale-in or scale-out rule that defines scaling activity, including the CloudWatch metric alarm that triggers activity, how Amazon EC2 instances are added or removed, and the periodicity of adjustments. The automatic scaling policy for an instance group can comprise one or more automatic scaling rules.

Name -> (string)

The name used to identify an automatic scaling rule. Rule names must be unique within a scaling policy.

Description -> (string)

A friendly, more verbose description of the automatic scaling rule.

Action -> (structure)

The conditions that trigger an automatic scaling activity.

Market -> (string)

Not available for instance groups. Instance groups use the market type specified for the group.

SimpleScalingPolicyConfiguration -> (structure)

The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.

AdjustmentType -> (string)

The way in which Amazon EC2 instances are added (if `ScalingAdjustment` is a positive number) or terminated (if `ScalingAdjustment` is a negative number) each time the scaling activity is triggered. `CHANGE_IN_CAPACITY` is the default. `CHANGE_IN_CAPACITY` indicates that the Amazon EC2 instance count increments or decrements by `ScalingAdjustment` , which should be expressed as an integer. `PERCENT_CHANGE_IN_CAPACITY` indicates the instance count increments or decrements by the percentage specified by `ScalingAdjustment` , which should be expressed as an integer. For example, 20 indicates an increase in 20% increments of cluster capacity. `EXACT_CAPACITY` indicates the scaling activity results in an instance group with the number of Amazon EC2 instances specified by `ScalingAdjustment` , which should be expressed as a positive integer.

ScalingAdjustment -> (integer)

The amount by which to scale in or scale out, based on the specified `AdjustmentType` . A positive value adds to the instance groupâs Amazon EC2 instance count while a negative number removes instances. If `AdjustmentType` is set to `EXACT_CAPACITY` , the number should only be a positive integer. If `AdjustmentType` is set to `PERCENT_CHANGE_IN_CAPACITY` , the value should express the percentage as an integer. For example, -20 indicates a decrease in 20% increments of cluster capacity.

CoolDown -> (integer)

The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start. The default value is 0.

Trigger -> (structure)

The CloudWatch alarm definition that determines when automatic scaling activity is triggered.

CloudWatchAlarmDefinition -> (structure)

The definition of a CloudWatch metric alarm. When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.

ComparisonOperator -> (string)

Determines how the metric specified by `MetricName` is compared to the value specified by `Threshold` .

EvaluationPeriods -> (integer)

The number of periods, in five-minute increments, during which the alarm condition must exist before the alarm triggers automatic scaling activity. The default value is `1` .

MetricName -> (string)

The name of the CloudWatch metric that is watched to determine an alarm condition.

Namespace -> (string)

The namespace for the CloudWatch metric. The default is `AWS/ElasticMapReduce` .

Period -> (integer)

The period, in seconds, over which the statistic is applied. CloudWatch metrics for Amazon EMR are emitted every five minutes (300 seconds), so if you specify a CloudWatch metric, specify `300` .

Statistic -> (string)

The statistic to apply to the metric associated with the alarm. The default is `AVERAGE` .

Threshold -> (double)

The value against which the specified statistic is compared.

Unit -> (string)

The unit of measure associated with the CloudWatch metric being watched. The value specified for `Unit` must correspond to the units specified in the CloudWatch metric.

Dimensions -> (list)

A CloudWatch metric dimension.

(structure)

A CloudWatch dimension, which is specified using a `Key` (known as a `Name` in CloudWatch), `Value` pair. By default, Amazon EMR uses one dimension whose `Key` is `JobFlowID` and `Value` is a variable representing the cluster ID, which is `${emr.clusterId}` . This enables the rule to bootstrap when the cluster ID becomes available.

Key -> (string)

The dimension name.

Value -> (string)

The dimension value.

ClusterArn -> (string)

The Amazon Resource Name (ARN) of the cluster.