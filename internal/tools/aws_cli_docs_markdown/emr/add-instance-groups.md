# add-instance-groupsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/add-instance-groups.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/add-instance-groups.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/index.html#cli-aws-emr) ]

# add-instance-groups

## Description

Adds an instance group to a running cluster.

## Synopsis

```
add-instance-groups
--cluster-id <value>
--instance-groups <value> [<value>...]
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

A unique string that identifies a cluster. The `create-cluster` command returns this identifier. You can use the `list-clusters` command to get cluster IDs.

`--instance-groups` (list)

Specifies the number and type of Amazon EC2 instances to create for each node type in a cluster, using uniform instance groups. You can specify either `--instance-groups` or `--instance-fleets` but not both. For more information, see the following topic in the EMR Management Guide:

[https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html)

You can specify arguments individually using multiple `InstanceGroupType` argument blocks, one for the `MASTER` instance group, one for a `CORE` instance group, and optional, multiple `TASK` instance groups.

If you specify inline JSON structures, enclose the entire `InstanceGroupType` argument block in single quotation marks.

Each `InstanceGroupType` block takes the following inline arguments. Optional arguments are shown in [square brackets].

- `[Name]` - An optional friendly name for the instance group.
- `InstanceGroupType` - `MASTER` , `CORE` , or `TASK` .
- `InstanceType` - The type of EC2 instance, for example `m4.large` , to use for all nodes in the instance group.
- `InstanceCount` - The number of EC2 instances to provision in the instance group.
- `[BidPrice]` - If specified, indicates that the instance group uses Spot Instances. This is the maximum price you are willing to pay for Spot Instances. Specify OnDemandPrice to set the amount equal to the On-Demand price, or specify an amount in USD.
- `[EbsConfiguration]` - Specifies additional Amazon EBS storage volumes attached to EC2 instances using an inline JSON structure.
- `[AutoScalingPolicy]` - Specifies an automatic scaling policy for the instance group using an inline JSON structure.

(structure)

Name -> (string)

Friendly name given to the instance group.

InstanceGroupType -> (string)

The type of the instance group in the cluster.

BidPrice -> (string)

Bid price for each Amazon EC2 instance in the instance group when launching nodes as Spot Instances, expressed in USD.

InstanceType -> (string)

The Amazon EC2 instance type for all instances in the instance group.

InstanceCount -> (integer)

Target number of Amazon EC2 instances for the instance group

CustomAmiId -> (string)

The AMI ID of a custom AMI to use when Amazon EMR provisions EC2 instances.

EbsConfiguration -> (structure)

EBS configuration that will be associated with the instance group.

EbsOptimized -> (boolean)

Boolean flag used to tag EBS-optimized instances.

EbsBlockDeviceConfigs -> (list)

(structure)

VolumeSpecification -> (structure)

The EBS volume specification that will be created and attached to every instance in this instance group.

VolumeType -> (string)

The EBS volume type that is attached to all the instances in the instance group. Valid types are: gp2, io1, and standard.

SizeInGB -> (integer)

The EBS volume size, in GB, that is attached to all the instances in the instance group.

Iops -> (integer)

The IOPS of the EBS volume that is attached to all the instances in the instance group.

Throughput -> (integer)

The throughput of the EBS volume that is attached to all the instances in the instance group.

VolumesPerInstance -> (integer)

The number of EBS volumes that will be created and attached to each instance in the instance group.

AutoScalingPolicy -> (structure)

Auto Scaling policy that will be associated with the instance group.

Constraints -> (structure)

The Constraints that will be associated to an Auto Scaling policy.

MinCapacity -> (integer)

The minimum value for the instances to scale in to in response to scaling activities.

MaxCapacity -> (integer)

The maximum value for the instances to scale out to in response to scaling activities

Rules -> (list)

The Rules associated to an Auto Scaling policy.

(structure)

Name -> (string)

Name of the Auto Scaling rule.

Description -> (string)

Description of the Auto Scaling rule.

Action -> (structure)

The Action associated to an Auto Scaling rule.

Market -> (string)

Market type of the Amazon EC2 instances used to create a cluster node by Auto Scaling action.

SimpleScalingPolicyConfiguration -> (structure)

The Simple scaling configuration that will be associatedto Auto Scaling action.

AdjustmentType -> (string)

Specifies how the ScalingAdjustment parameter is interpreted.

ScalingAdjustment -> (integer)

The amount by which to scale, based on the specified adjustment type.

CoolDown -> (integer)

The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.

Trigger -> (structure)

The Trigger associated to an Auto Scaling rule.

CloudWatchAlarmDefinition -> (structure)

The Alarm to be registered with CloudWatch, to trigger scaling activities.

ComparisonOperator -> (string)

The arithmetic operation to use when comparing the specified Statistic and Threshold.

EvaluationPeriods -> (integer)

The number of periods over which data is compared to the specified threshold.

MetricName -> (string)

The name for the alarmâs associated metric.

Namespace -> (string)

The namespace for the alarmâs associated metric.

Period -> (integer)

The period in seconds over which the specified statistic is applied.

Statistic -> (string)

The statistic to apply to the alarmâs associated metric.

Threshold -> (double)

The value against which the specified statistic is compared.

Unit -> (string)

The statisticâs unit of measure.

Dimensions -> (list)

The dimensions for the alarmâs associated metric.

(structure)

Key -> (string)

Dimension Key.

Value -> (string)

Dimension Value.

Configurations -> (list)

Instance group application configurations.

(structure)

Classification -> (string)

Application configuration classification name

Properties -> (map)

Application configuration properties

key -> (string)

Configuration key

value -> (string)

Configuration value

Configurations -> (list)

Instance group application configurations.

(structure)

Classification -> (string)

Application configuration classification name

Properties -> (map)

Application configuration properties

key -> (string)

Configuration key

value -> (string)

Configuration value

JSON Syntax:

```
[
  {
    "Name": "string",
    "InstanceGroupType": "MASTER"|"CORE"|"TASK",
    "BidPrice": "string",
    "InstanceType": "string",
    "InstanceCount": integer,
    "CustomAmiId": "string",
    "EbsConfiguration": {
      "EbsOptimized": true|false,
      "EbsBlockDeviceConfigs": [
        {
          "VolumeSpecification": {
            "VolumeType": "string",
            "SizeInGB": integer,
            "Iops": integer,
            "Throughput": integer
          },
          "VolumesPerInstance": integer
        }
        ...
      ]
    },
    "AutoScalingPolicy": {
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
              "ComparisonOperator": "string",
              "EvaluationPeriods": integer,
              "MetricName": "string",
              "Namespace": "string",
              "Period": integer,
              "Statistic": "string",
              "Threshold": double,
              "Unit": "string",
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
    },
    "Configurations": [
      {
        "Classification": "string",
        "Properties": {"string": "string"
          ...},
        "Configurations": [
          {
            "Classification": "string",
            "Properties": {"string": "string"
              ...}
          }
          ...
        ]
      }
      ...
    ]
  }
  ...
]
```

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