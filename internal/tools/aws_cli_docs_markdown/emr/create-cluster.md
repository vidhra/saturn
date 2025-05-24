# create-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/create-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/create-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/index.html#cli-aws-emr) ]

# create-cluster

## Description

Creates an Amazon EMR cluster with the specified configurations.

## Synopsis

```
create-cluster
--release-label <value>   | --ami-version <value>
--instance-fleets <value> | --instance-groups <value> | --instance-type <value> --instance-count <value>
[--os-release-label <value>]
[--auto-terminate | --no-auto-terminate]
[--use-default-roles]
[--service-role <value>]
[--configurations <value>]
[--name <value>]
[--log-uri <value>]
[--log-encryption-kms-key-id <value>]
[--additional-info <value>]
[--ec2-attributes <value>]
[--termination-protected | --no-termination-protected]
[--unhealthy-node-replacement | --no-unhealthy-node-replacement]
[--scale-down-behavior <value>]
[--visible-to-all-users | --no-visible-to-all-users]
[--enable-debugging | --no-enable-debugging]
[--tags <value>]
[--applications <value>]
[--emrfs <value>]
[--bootstrap-actions <value>]
[--steps <value>]
[--restore-from-hbase-backup <value>]
[--security-configuration <value>]
[--custom-ami-id <value>]
[--ebs-root-volume-size <value>]
[--ebs-root-volume-iops <value>]
[--ebs-root-volume-throughput <value>]
[--repo-upgrade-on-boot <value>]
[--kerberos-attributes <value>]
[--managed-scaling-policy <value>]
[--placement-group-configs <value>]
[--auto-termination-policy <value>]
```

## Options

`--release-label` (string)

Specifies the Amazon EMR release version, which determines the versions of application software that are installed on the cluster. For example, `--release-label emr-5.15.0` installs the application versions and features available in that version. For details about application versions and features available in each release, see the Amazon EMR Release Guide:

[https://docs.aws.amazon.com/emr/latest/ReleaseGuide](https://docs.aws.amazon.com/emr/latest/ReleaseGuide)

Use `--release-label` only for Amazon EMR release version 4.0 and later. Use `--ami-version` for earlier versions. You cannot specify both a release label and AMI version.

`--os-release-label` (string)

Specifies a particular Amazon Linux release for all nodes in a cluster launch request. If a release is not specified, EMR uses the latest validated Amazon Linux release for cluster launch.

`--ami-version` (string)

Applies only to Amazon EMR release versions earlier than 4.0. Use `--release-label` for 4.0 and later. Specifies the version of Amazon Linux Amazon Machine Image (AMI) to use when launching Amazon EC2 instances in the cluster. For example, `--ami-version 3.1.0` .

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

`--instance-type` (string)

Shortcut parameter as an alternative to `--instance-groups` . Specifies the type of Amazon EC2 instance to use in a cluster. If used without the `--instance-count` parameter, the cluster consists of a single master node running on the EC2 instance type specified. When used together with `--instance-count` , one instance is used for the master node, and the remainder are used for the core node type.

`--instance-count` (string)

Shortcut parameter as an alternative to `--instance-groups` when used together with `--instance-type` . Specifies the number of Amazon EC2 instances to create for a cluster. One instance is used for the master node, and the remainder are used for the core node type.

`--auto-terminate` | `--no-auto-terminate` (boolean)

Specifies whether the cluster should terminate after completing all the steps. Auto termination is off by default.

`--instance-fleets` (list)

Applies only to Amazon EMR release version 5.0 and later. Specifies the number and type of Amazon EC2 instances to create for each node type in a cluster, using instance fleets. You can specify either `--instance-fleets` or `--instance-groups` but not both. For more information and examples, see the following topic in the Amazon EMR Management Guide:

[https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-fleet.html](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-fleet.html)

You can specify arguments individually using multiple `InstanceFleetType` argument blocks, one for the `MASTER` instance fleet, one for a `CORE` instance fleet, and an optional `TASK` instance fleet.

The following arguments can be specified for each instance fleet. Optional arguments are shown in [square brackets].

- `[Name]` - An optional friendly name for the instance fleet.
- `InstanceFleetType` - `MASTER` , `CORE` , or `TASK` .
- `TargetOnDemandCapacity` - The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand Instances to provision. The `WeightedCapacity` specified for an instance type within `InstanceTypeConfigs` counts toward this total when an instance type with the On-Demand purchasing option launches.
- `TargetSpotCapacity` - The target capacity of Spot units for the instance fleet, which determines how many Spot Instances to provision. The `WeightedCapacity` specified for an instance type within `InstanceTypeConfigs` counts toward this total when an instance type with the Spot purchasing option launches.
- `[LaunchSpecifications]` - When `TargetSpotCapacity` is specified, specifies the block duration and timeout action for Spot Instances.
- `InstanceTypeConfigs` - Specify up to five EC2 instance types to use in the instance fleet, including details such as Spot price and Amazon EBS configuration. When you use an On-Demand or Spot Instance allocation strategy, you can specify up to 30 instance types per instance fleet.

(structure)

Name -> (string)

Friendly name given to the instance fleet.

InstanceFleetType -> (string)

The type of the instance fleet in the cluster.

TargetOnDemandCapacity -> (integer)

Target on-demand capacity for the instance fleet.

TargetSpotCapacity -> (integer)

Target spot capacity for the instance fleet.

InstanceTypeConfigs -> (list)

(structure)

InstanceType -> (string)

The Amazon EC2 instance type for the instance fleet.

WeightedCapacity -> (integer)

The weight assigned to an instance type, which will impact the overall fulfillment of the capacity.

BidPrice -> (string)

Bid price for each Amazon EC2 instance in the instance fleet when launching nodes as Spot Instances, expressed in USD.

BidPriceAsPercentageOfOnDemandPrice -> (double)

Bid price as percentage of on-demand price.

CustomAmiId -> (string)

The AMI ID of a custom AMI to use when Amazon EMR provisions EC2 instances.

Priority -> (double)

The priority at which Amazon EMR launches the EC2 instances with this instance type. Priority starts at 0, which is the highest priority. Amazon EMR considers the highest priority first.

EbsConfiguration -> (structure)

EBS configuration that is associated with the instance group.

EbsOptimized -> (boolean)

Boolean flag used to tag EBS-optimized instances.

EbsBlockDeviceConfigs -> (list)

(structure)

VolumeSpecification -> (structure)

The EBS volume specification that is created and attached to each instance in the instance group.

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

LaunchSpecifications -> (structure)

OnDemandSpecification -> (structure)

AllocationStrategy -> (string)

The strategy to use to launch On-Demand instance fleets.

CapacityReservationOptions -> (structure)

UsageStrategy -> (string)

The strategy of whether to use available capacity reservations to fulfill On-Demand capacity.

CapacityReservationPreference -> (string)

The preference of the capacity reservation of the instance.

CapacityReservationResourceGroupArn -> (string)

The ARN of the capacity reservation resource group in which to run the instance.

SpotSpecification -> (structure)

TimeoutDurationMinutes -> (integer)

The time, in minutes, after which the action specified in TimeoutAction field will be performed if requested resources are unavailable.

TimeoutAction -> (string)

The action that is performed after TimeoutDurationMinutes.

BlockDurationMinutes -> (integer)

Block duration in minutes.

AllocationStrategy -> (string)

The strategy to use to launch Spot instance fleets.

ResizeSpecifications -> (structure)

SpotResizeSpecification -> (structure)

TimeoutDurationMinutes -> (integer)

The time, in minutes, after which the resize will be stopped if requested resources are unavailable.

AllocationStrategy -> (string)

The strategy to use to launch Spot instance fleets.

OnDemandResizeSpecification -> (structure)

TimeoutDurationMinutes -> (integer)

The time, in minutes, after which the resize will be stopped if requested resources are unavailable.

AllocationStrategy -> (string)

The strategy to use to launch On-Demand instance fleets.

CapacityReservationOptions -> (structure)

UsageStrategy -> (string)

The strategy of whether to use available capacity reservations to fulfill On-Demand capacity.

CapacityReservationPreference -> (string)

The preference of the capacity reservation of the instance.

CapacityReservationResourceGroupArn -> (string)

The ARN of the capacity reservation resource group in which to run the instance.

Context -> (string)

Reserved.

JSON Syntax:

```
[
  {
    "Name": "string",
    "InstanceFleetType": "MASTER"|"CORE"|"TASK",
    "TargetOnDemandCapacity": integer,
    "TargetSpotCapacity": integer,
    "InstanceTypeConfigs": [
      {
        "InstanceType": "string",
        "WeightedCapacity": integer,
        "BidPrice": "string",
        "BidPriceAsPercentageOfOnDemandPrice": double,
        "CustomAmiId": "string",
        "Priority": double,
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
    ],
    "LaunchSpecifications": {
      "OnDemandSpecification": {
        "AllocationStrategy": "lowest-price"|"prioritized",
        "CapacityReservationOptions": {
          "UsageStrategy": "use-capacity-reservations-first",
          "CapacityReservationPreference": "open"|"none",
          "CapacityReservationResourceGroupArn": "string"
        }
      },
      "SpotSpecification": {
        "TimeoutDurationMinutes": integer,
        "TimeoutAction": "TERMINATE_CLUSTER"|"SWITCH_TO_ONDEMAND",
        "BlockDurationMinutes": integer,
        "AllocationStrategy": "capacity-optimized"|"price-capacity-optimized"|"lowest-price"|"diversified"|"capacity-optimized-prioritized"
      }
    },
    "ResizeSpecifications": {
      "SpotResizeSpecification": {
        "TimeoutDurationMinutes": integer,
        "AllocationStrategy": "capacity-optimized"|"price-capacity-optimized"|"lowest-price"|"diversified"|"capacity-optimized-prioritized"
      },
      "OnDemandResizeSpecification": {
        "TimeoutDurationMinutes": integer,
        "AllocationStrategy": "lowest-price"|"prioritized",
        "CapacityReservationOptions": {
          "UsageStrategy": "use-capacity-reservations-first",
          "CapacityReservationPreference": "open"|"none",
          "CapacityReservationResourceGroupArn": "string"
        }
      }
    },
    "Context": "string"
  }
  ...
]
```

`--name` (string)

The name of the cluster. If not provided, the default is âDevelopment Clusterâ.

`--log-uri` (string)

Specifies the location in Amazon S3 to which log files are periodically written. If a value is not provided, logs files are not written to Amazon S3 from the master node and are lost if the master node terminates.

`--log-encryption-kms-key-id` (string)

Specifies the KMS Id utilized for log encryption. If a value is not provided, log files will be encrypted by default encryption method AES-256. This attribute is only available with EMR version 5.30.0 and later, excluding EMR 6.0.0.

`--service-role` (string)

Specifies an IAM service role, which Amazon EMR requires to call other AWS services on your behalf during cluster operation. This parameter is usually specified when a customized service role is used. To specify the default service role, as well as the default instance profile, use the `--use-default-roles` parameter. If the role and instance profile do not already exist, use the `aws emr create-default-roles` command to create them.

`--auto-scaling-role` (string)

Specify `--auto-scaling-role EMR_AutoScaling_DefaultRole` if an automatic scaling policy is specified for an instance group using the `--instance-groups` parameter. This default IAM role allows the automatic scaling feature to launch and terminate Amazon EC2 instances during scaling operations.

`--use-default-roles` (boolean)

Specifies that the cluster should use the default service role (EMR_DefaultRole) and instance profile (EMR_EC2_DefaultRole) for permissions to access other AWS services.

Make sure that the role and instance profile exist first. To create them, use the `create-default-roles` command.

`--configurations` (string)

Specifies a JSON file that contains configuration classifications, which you can use to customize applications that Amazon EMR installs when cluster instances launch. Applies only to Amazon EMR 4.0 and later. The file referenced can either be stored locally (for example, `--configurations file://configurations.json` ) or stored in Amazon S3 (for example, `--configurations https://s3.amazonaws.com/myBucket/configurations.json` ). Each classification usually corresponds to the xml configuration file for an application, such as `yarn-site` for YARN. For a list of available configuration classifications and example JSON, see the following topic in the Amazon EMR Release Guide:

[https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html)

`--ec2-attributes` (structure)

Configures cluster and Amazon EC2 instance configurations. Accepts the following arguments:

- `KeyName` - Specifies the name of the AWS EC2 key pair that will be used for SSH connections to the master node and other instances on the cluster.
- `AvailabilityZone` - Applies to clusters that use the uniform instance group configuration. Specifies the availability zone in which to launch the cluster. For example, `us-west-1b` . `AvailabilityZone` is used for uniform instance groups, while `AvailabilityZones` (plural) is used for instance fleets.
- `AvailabilityZones` - Applies to clusters that use the instance fleet configuration. When multiple Availability Zones are specified, Amazon EMR evaluates them and launches instances in the optimal Availability Zone. `AvailabilityZone` is used for uniform instance groups, while `AvailabilityZones` (plural) is used for instance fleets.
- `SubnetId` - Applies to clusters that use the uniform instance group configuration. Specify the VPC subnet in which to create the cluster. `SubnetId` is used for uniform instance groups, while `SubnetIds` (plural) is used for instance fleets.
- `SubnetIds` - Applies to clusters that use the instance fleet configuration. When multiple EC2 subnet IDs are specified, Amazon EMR evaluates them and launches instances in the optimal subnet. `SubnetId` is used for uniform instance groups, while `SubnetIds` (plural) is used for instance fleets.
- `InstanceProfile` - An IAM role that allows EC2 instances to access other AWS services, such as Amazon S3, that are required for operations.
- `EmrManagedMasterSecurityGroup` - The security group ID of the Amazon EC2 security group for the master node.
- `EmrManagedSlaveSecurityGroup` - The security group ID of the Amazon EC2 security group for the slave nodes.
- `ServiceAccessSecurityGroup` - The security group ID of the Amazon EC2 security group for Amazon EMR access to clusters in VPC private subnets.
- `AdditionalMasterSecurityGroups` - A list of additional Amazon EC2 security group IDs for the master node.
- `AdditionalSlaveSecurityGroups` - A list of additional Amazon EC2 security group IDs for the slave nodes.

KeyName -> (string)

The name of the Amazon EC2 key pair that can be used to ssh to the master node as the user âhadoopâ.

SubnetId -> (string)

To launch the cluster in Amazon Virtual Private Cloud (Amazon VPC), set this parameter to the identifier of the Amazon VPC subnet where you want the cluster to launch. If you do not specify this value, the cluster is launched in the normal Amazon Web Services cloud, outside of an Amazon VPC.

SubnetIds -> (list)

List of SubnetIds.

(string)

AvailabilityZone -> (string)

The Availability Zone the cluster will run in.

AvailabilityZones -> (list)

List of AvailabilityZones.

(string)

InstanceProfile -> (string)

An IAM role for the cluster. The EC2 instances of the cluster assume this role. The default role is EMR_EC2_DefaultRole. In order to use the default role, you must have already created it using the `create-default-roles` command.

EmrManagedMasterSecurityGroup -> (string)

The identifier of the Amazon EC2 security group for the master node.

EmrManagedSlaveSecurityGroup -> (string)

The identifier of the Amazon EC2 security group for the slave nodes.

ServiceAccessSecurityGroup -> (string)

The identifier of the Amazon EC2 security group for Amazon EMR to access clusters in VPC private subnets.

AdditionalMasterSecurityGroups -> (list)

A list of additional Amazon EC2 security group IDs for the master node

(string)

AdditionalSlaveSecurityGroups -> (list)

A list of additional Amazon EC2 security group IDs for the slave nodes.

(string)

Shorthand Syntax:

```
KeyName=string,SubnetId=string,SubnetIds=string,string,AvailabilityZone=string,AvailabilityZones=string,string,InstanceProfile=string,EmrManagedMasterSecurityGroup=string,EmrManagedSlaveSecurityGroup=string,ServiceAccessSecurityGroup=string,AdditionalMasterSecurityGroups=string,string,AdditionalSlaveSecurityGroups=string,string
```

JSON Syntax:

```
{
  "KeyName": "string",
  "SubnetId": "string",
  "SubnetIds": ["string", ...],
  "AvailabilityZone": "string",
  "AvailabilityZones": ["string", ...],
  "InstanceProfile": "string",
  "EmrManagedMasterSecurityGroup": "string",
  "EmrManagedSlaveSecurityGroup": "string",
  "ServiceAccessSecurityGroup": "string",
  "AdditionalMasterSecurityGroups": ["string", ...],
  "AdditionalSlaveSecurityGroups": ["string", ...]
}
```

`--termination-protected` | `--no-termination-protected` (boolean)

Specifies whether to lock the cluster to prevent the Amazon EC2 instances from being terminated by API call, user intervention, or an error.

`--unhealthy-node-replacement` | `--no-unhealthy-node-replacement` (boolean)

Unhealthy node replacement for an Amazon EMR cluster.

`--scale-down-behavior` (string)

Specifies the way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an instance group is resized.

Accepted values:

- `TERMINATE_AT_TASK_COMPLETION` - Specifies that Amazon EMR blacklists and drains tasks from nodes before terminating the instance.
- `TERMINATE_AT_INSTANCE_HOUR` - Specifies that Amazon EMR terminate EC2 instances at the instance-hour boundary, regardless of when the request to terminate was submitted.

`--visible-to-all-users` | `--no-visible-to-all-users` (boolean)

Specifies whether the cluster is visible to all IAM users of the AWS account associated with the cluster. If a user has the proper policy permissions set, they can also manage the cluster.

Visibility is on by default. The `--no-visible-to-all-users` option is no longer supported. To restrict cluster visibility, use an IAM policy.

`--enable-debugging` | `--no-enable-debugging` (boolean)

Specifies that the debugging tool is enabled for the cluster, which allows you to browse log files using the Amazon EMR console. Turning debugging on requires that you specify `--log-uri` because log files must be stored in Amazon S3 so that Amazon EMR can index them for viewing in the console. Effective January 23, 2023, Amazon EMR will discontinue the debugging tool for all versions.

`--tags` (list)

A list of tags to associate with a cluster, which apply to each Amazon EC2 instance in the cluster. Tags are key-value pairs that consist of a required key string with a maximum of 128 characters, and an optional value string with a maximum of 256 characters.

You can specify tags in `key=value` format or you can add a tag without a value using only the key name, for example `key` . Use a space to separate multiple tags.

(string)

Syntax:

```
"string" "string" ...
```

`--bootstrap-actions` (list)

Specifies a list of bootstrap actions to run on each EC2 instance when a cluster is created. Bootstrap actions run on each instance immediately after Amazon EMR provisions the EC2 instance and before Amazon EMR installs specified applications.

You can specify a bootstrap action as an inline JSON structure enclosed in single quotation marks, or you can use a shorthand syntax, specifying multiple bootstrap actions, each separated by a space. When using the shorthand syntax, each bootstrap action takes the following parameters, separated by commas with no trailing space. Optional parameters are shown in [square brackets].

- `Path` - The path and file name of the script to run, which must be accessible to each instance in the cluster. For example, `Path=s3://mybucket/myscript.sh` .
- `[Name]` - A friendly name to help you identify the bootstrap action. For example, `Name=BootstrapAction1`
- `[Args]` - A comma-separated list of arguments to pass to the bootstrap action script. Arguments can be either a list of values (`Args=arg1,arg2,arg3` ) or a list of key-value pairs, as well as optional values, enclosed in square brackets (`Args=[arg1,arg2=arg2value,arg3])` .

(structure)

Name -> (string)

Path -> (string)

Location of the script to run during a bootstrap action. Can be either a location in Amazon S3 or on a local file system.

Args -> (list)

A list of command line arguments to pass to the bootstrap action script

(string)

Shorthand Syntax:

```
Name=string,Path=string,Args=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Path": "string",
    "Args": ["string", ...]
  }
  ...
]
```

`--applications` (list)

Specifies the applications to install on the cluster. Available applications and their respective versions vary by Amazon EMR release. For more information, see the Amazon EMR Release Guide:

[https://docs.aws.amazon.com/emr/latest/ReleaseGuide/](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/)

When using versions of Amazon EMR earlier than 4.0, some applications take optional arguments for configuration. Arguments should either be a comma-separated list of values (`Args=arg1,arg2,arg3` ) or a bracket-enclosed list of values and key-value pairs (`Args=[arg1,arg2=arg3,arg4]` ).

(structure)

Name -> (string)

Application name.

Args -> (list)

A list of arguments to pass to the application.

(string)

Shorthand Syntax:

```
Name=string,Args=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "MapR"|"HUE"|"HIVE"|"PIG"|"HBASE"|"IMPALA"|"GANGLIA"|"HADOOP"|"SPARK",
    "Args": ["string", ...]
  }
  ...
]
```

`--emrfs` (structure)

Specifies EMRFS configuration options, such as consistent view and Amazon S3 encryption parameters.

When you use Amazon EMR release version 4.8.0 or later, we recommend that you use the `--configurations` option together with the `emrfs-site` configuration classification to configure EMRFS, and use security configurations to configure encryption for EMRFS data in Amazon S3 instead. For more information, see the following topic in the Amazon EMR Management Guide:

[https://docs.aws.amazon.com/emr/latest/ManagementGuide/emrfs-configure-consistent-view.html](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emrfs-configure-consistent-view.html)

Consistent -> (boolean)

Enable EMRFS consistent view.

SSE -> (boolean)

Enable Amazon S3 server-side encryption on files written to S3 by EMRFS.

RetryCount -> (integer)

The maximum number of times to retry upon S3 inconsistency.

RetryPeriod -> (integer)

The amount of time (in seconds) until the first retry. Subsequent retries use an exponential back-off.

Args -> (list)

A list of arguments to pass for additional EMRFS configuration.

(string)

Encryption -> (string)

EMRFS encryption type.

ProviderType -> (string)

EMRFS client-side encryption provider type.

KMSKeyId -> (string)

AWS KMSâs customer master key identifier

CustomProviderLocation -> (string)

Custom encryption provider JAR location.

CustomProviderClass -> (string)

Custom encryption provider full class name.

Shorthand Syntax:

```
Consistent=boolean,SSE=boolean,RetryCount=integer,RetryPeriod=integer,Args=string,string,Encryption=string,ProviderType=string,KMSKeyId=string,CustomProviderLocation=string,CustomProviderClass=string
```

JSON Syntax:

```
{
  "Consistent": true|false,
  "SSE": true|false,
  "RetryCount": integer,
  "RetryPeriod": integer,
  "Args": ["string", ...],
  "Encryption": "SERVERSIDE"|"CLIENTSIDE",
  "ProviderType": "KMS"|"CUSTOM",
  "KMSKeyId": "string",
  "CustomProviderLocation": "string",
  "CustomProviderClass": "string"
}
```

`--steps` (list)

Specifies a list of steps to be executed by the cluster. Steps run only on the master node after applications are installed and are used to submit work to a cluster. A step can be specified using the shorthand syntax, by referencing a JSON file or by specifying an inline JSON structure. `Args` supplied with steps should be a comma-separated list of values (`Args=arg1,arg2,arg3` ) or a bracket-enclosed list of values and key-value pairs (`Args=[arg1,arg2=value,arg4` ).

(structure)

Type -> (string)

The type of a step to be added to the cluster.

Name -> (string)

The name of the step.

ActionOnFailure -> (string)

The action to take if the cluster step fails.

Jar -> (string)

A path to a JAR file run during the step.

Args -> (list)

A list of command line arguments to pass to the step.

(string)

MainClass -> (string)

The name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.

Properties -> (string)

A list of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.

Shorthand Syntax:

```
Type=string,Name=string,ActionOnFailure=string,Jar=string,Args=string,string,MainClass=string,Properties=string ...
```

JSON Syntax:

```
[
  {
    "Type": "CUSTOM_JAR"|"STREAMING"|"HIVE"|"PIG"|"IMPALA",
    "Name": "string",
    "ActionOnFailure": "TERMINATE_CLUSTER"|"CANCEL_AND_WAIT"|"CONTINUE",
    "Jar": "string",
    "Args": ["string", ...],
    "MainClass": "string",
    "Properties": "string"
  }
  ...
]
```

`--additional-info` (string)

Specifies additional information during cluster creation. To set development mode when starting your EMR cluster, set this parameter to `{"clusterType":"development"}` .

`--restore-from-hbase-backup` (structure)

Applies only when using Amazon EMR release versions earlier than 4.0. Launches a new HBase cluster and populates it with data from a previous backup of an HBase cluster. HBase must be installed using the `--applications` option.

Dir -> (string)

The Amazon S3 location of the Hbase backup. Example: `s3://mybucket/mybackup` , where `mybucket` is the specified Amazon S3 bucket and mybackup is the specified backup location. The path argument must begin with s3://, which refers to an Amazon S3 bucket.

BackupVersion -> (string)

The backup version to restore from. If not specified, the latest backup in the specified location is used.

Shorthand Syntax:

```
Dir=string,BackupVersion=string
```

JSON Syntax:

```
{
  "Dir": "string",
  "BackupVersion": "string"
}
```

`--security-configuration` (string)

Specifies the name of a security configuration to use for the cluster. A security configuration defines data encryption settings and other security options. For more information, see the following topic in the Amazon EMR Management Guide:

[https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-encryption-enable-security-configuration.html](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-encryption-enable-security-configuration.html)

Use `list-security-configurations` to get a list of available security configurations in the active account.

`--custom-ami-id` (string)

Applies only to Amazon EMR release version 5.7.0 and later. Specifies the AMI ID of a custom AMI to use when Amazon EMR provisions EC2 instances. A custom AMI can be used to encrypt the Amazon EBS root volume. It can also be used instead of bootstrap actions to customize cluster node configurations. For more information, see the following topic in the Amazon EMR Management Guide:

[https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-custom-ami.html](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-custom-ami.html)

`--ebs-root-volume-size` (string)

This option is available only with Amazon EMR version 4.x and later. Specifies the size, in GiB, of the EBS root device volume of the Amazon Linux AMI that is used for each EC2 instance in the cluster.

`--ebs-root-volume-iops` (string)

This option is available only with Amazon EMR version 6.15.0 and later. Specifies the IOPS, of the EBS root device volume of the Amazon Linux AMI that is used for each EC2 instance in the cluster.

`--ebs-root-volume-throughput` (string)

This option is available only with Amazon EMR version 6.15.0 and later. Specifies the throughput, in MiB/s, of the EBS root device volume of the Amazon Linux AMI that is used for each EC2 instance in the cluster.

`--repo-upgrade-on-boot` (string)

Applies only when a `--custom-ami-id` is specified. On first boot, by default, Amazon Linux AMIs connect to package repositories to install security updates before other services start. You can set this parameter using `--rep-upgrade-on-boot NONE` to disable these updates. CAUTION: This creates additional security risks.

`--kerberos-attributes` (structure)

Specifies required cluster attributes for Kerberos when Kerberos authentication is enabled in the specified `--security-configuration` . Takes the following arguments:

- `Realm` - Specifies the name of the Kerberos realm to which all nodes in a cluster belong. For example, `Realm=EC2.INTERNAL` .
- `KdcAdminPassword` - Specifies the password used within the cluster for the kadmin service, which maintains Kerberos principals, password policies, and keytabs for the cluster.
- `CrossRealmTrustPrincipalPassword` - Required when establishing a cross-realm trust with a KDC in a different realm. This is the cross-realm principal password, which must be identical across realms.
- `ADDomainJoinUser` - Required when establishing trust with an Active Directory domain. This is the User logon name of an AD account with sufficient privileges to join resources to the domain.
- `ADDomainJoinPassword` - The AD password for `ADDomainJoinUser` .

Realm -> (string)

The name of Kerberos realm.

KdcAdminPassword -> (string)

The password of Kerberos administrator.

CrossRealmTrustPrincipalPassword -> (string)

The password to establish cross-realm trusts.

ADDomainJoinUser -> (string)

The name of the user with privileges to join instances to Active Directory.

ADDomainJoinPassword -> (string)

The password of the user with privileges to join instances to Active Directory.

Shorthand Syntax:

```
Realm=string,KdcAdminPassword=string,CrossRealmTrustPrincipalPassword=string,ADDomainJoinUser=string,ADDomainJoinPassword=string
```

JSON Syntax:

```
{
  "Realm": "string",
  "KdcAdminPassword": "string",
  "CrossRealmTrustPrincipalPassword": "string",
  "ADDomainJoinUser": "string",
  "ADDomainJoinPassword": "string"
}
```

`--step-concurrency-level` (integer)
This command specifies the step concurrency level of the cluster.Default is 1 which is non-concurrent.

`--managed-scaling-policy` (structure)

Managed scaling policy for an Amazon EMR cluster. The policy specifies the limits for resources that can be added or terminated from a cluster. You can specify the ComputeLimits which include the MaximumCapacityUnits, MaximumCoreCapacityUnits, MinimumCapacityUnits, MaximumOnDemandCapacityUnits and UnitType. For an InstanceFleet cluster, the UnitType must be InstanceFleetUnits. For InstanceGroup clusters, the UnitType can be either VCPU or Instances.

ComputeLimits -> (structure)

The EC2 unit limits for a managed scaling policy. The managed scaling activity of a cluster is not allowed to go above or below these limits. The limits apply to CORE and TASK groups and exclude the capacity of the MASTER group.

MinimumCapacityUnits -> (integer)

The lower boundary of EC2 units. It is measured through VCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary.

MaximumCapacityUnits -> (integer)

The upper boundary of EC2 units. It is measured through VCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary.

MaximumOnDemandCapacityUnits -> (integer)

The upper boundary of on-demand EC2 units. It is measured through VCPU cores or instances for instance groups and measured through units for instance fleets. The on-demand units are not allowed to scale beyond this boundary. This value must be lower than MaximumCapacityUnits.

UnitType -> (string)

The unit type used for specifying a managed scaling policy.

MaximumCoreCapacityUnits -> (integer)

The upper boundary of EC2 units for core node type in a cluster. It is measured through VCPU cores or instances for instance groups and measured through units for instance fleets. The core units are not allowed to scale beyond this boundary. The parameter is used to split capacity allocation between core and task nodes.

ScalingStrategy -> (string)

Determines whether a custom scaling utilization performance index can be set. Possible values include ADVANCED or DEFAULT.

UtilizationPerformanceIndex -> (integer)

An integer value that represents an advanced scaling strategy. Setting a higher value optimizes for performance. Setting a lower value optimizes for resource conservation. Setting the value to 50 balances performance and resource conservation. Possible values are 1, 25, 50, 75, and 100.

Shorthand Syntax:

```
ComputeLimits={MinimumCapacityUnits=integer,MaximumCapacityUnits=integer,MaximumOnDemandCapacityUnits=integer,UnitType=string,MaximumCoreCapacityUnits=integer},ScalingStrategy=string,UtilizationPerformanceIndex=integer
```

JSON Syntax:

```
{
  "ComputeLimits": {
    "MinimumCapacityUnits": integer,
    "MaximumCapacityUnits": integer,
    "MaximumOnDemandCapacityUnits": integer,
    "UnitType": "VCPU"|"Instances"|"InstanceFleetUnits",
    "MaximumCoreCapacityUnits": integer
  },
  "ScalingStrategy": "DEFAULT"|"ADVANCED",
  "UtilizationPerformanceIndex": integer
}
```

`--placement-group-configs` (list)

Placement group configuration for an Amazon EMR cluster. The configuration specifies the EC2 placement group strategy associated with each EMR Instance Role.

Currently, we support placement group only for `MASTER` role with `SPREAD` strategy by default. You can opt-in by passing `--placement-group-configs InstanceRole=MASTER` during cluster creation.

(structure)

InstanceRole -> (string)

Role of the instance in the cluster.

PlacementStrategy -> (string)

EC2 Placement Group strategy associated with instance role.

Shorthand Syntax:

```
InstanceRole=string,PlacementStrategy=string ...
```

JSON Syntax:

```
[
  {
    "InstanceRole": "MASTER"|"CORE"|"TASK",
    "PlacementStrategy": "SPREAD"|"PARTITION"|"CLUSTER"|"NONE"
  }
  ...
]
```

`--auto-termination-policy` (structure)

Auto termination policy for an Amazon EMR cluster. The configuration specifies the termination idle timeoutthreshold for an cluster.

IdleTimeout -> (long)

Specifies the amount of idle time in seconds after which the cluster automatically terminates. You can specify a minimum of 60 seconds and a maximum of 604800 seconds (seven days).

Shorthand Syntax:

```
IdleTimeout=long
```

JSON Syntax:

```
{
  "IdleTimeout": long
}
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

## Examples

Most of the following examples assume that you specified your Amazon EMR service role and Amazon EC2 instance profile. If you have not done this, you must specify each required IAM role or use the `--use-default-roles` parameter when creating your cluster. For more information about specifying IAM roles, see [Configure IAM Roles for Amazon EMR Permissions to AWS Services](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-roles.html) in the *Amazon EMR Management Guide*.

**Example 1: To create a cluster**

The following `create-cluster` example creates a simple EMR cluster.

```
aws emr create-cluster \
    --release-label emr-5.14.0 \
    --instance-type m4.large \
    --instance-count 2
```

This command produces no output.

**Example 2: To create an Amazon EMR cluster with default ServiceRole and InstanceProfile roles**

The following `create-cluster` example creates an Amazon EMR cluster that uses the `--instance-groups` configuration.

```
aws emr create-cluster \
    --release-label emr-5.14.0 \
    --service-role EMR_DefaultRole \
    --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large
```

**Example 3: To create an Amazon EMR cluster that uses an instance fleet**

The following `create-cluster` example creates an Amazon EMR cluster that uses the `--instance-fleets` configuration, specifying two instance types for each fleet and two EC2 Subnets.

```
aws emr create-cluster \
    --release-label emr-5.14.0 \
    --service-role EMR_DefaultRole \
    --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole,SubnetIds=['subnet-ab12345c','subnet-de67890f'] \
    --instance-fleets InstanceFleetType=MASTER,TargetOnDemandCapacity=1,InstanceTypeConfigs=['{InstanceType=m4.large}'] InstanceFleetType=CORE,TargetSpotCapacity=11,InstanceTypeConfigs=['{InstanceType=m4.large,BidPrice=0.5,WeightedCapacity=3}','{InstanceType=m4.2xlarge,BidPrice=0.9,WeightedCapacity=5}'],LaunchSpecifications={SpotSpecification='{TimeoutDurationMinutes=120,TimeoutAction=SWITCH_TO_ON_DEMAND}'}
```

**Example 4: To create a cluster with default roles**

The following `create-cluster` example uses the `--use-default-roles` parameter to specify the default service role and instance profile.

```
aws emr create-cluster \
    --release-label emr-5.9.0 \
    --use-default-roles \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large \
    --auto-terminate
```

**Example 5: To create a cluster and specify the applications to install**

The following `create-cluster` example uses the `--applications` parameter to specify the applications that Amazon EMR installs. This example installs Hadoop, Hive and Pig.

```
aws emr create-cluster \
    --applications Name=Hadoop Name=Hive Name=Pig \
    --release-label emr-5.9.0 \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large \
    --auto-terminate
```

**Example 6: To create a cluster that includes Spark**

The following example installs Spark.

```
aws emr create-cluster \
    --release-label emr-5.9.0 \
    --applications Name=Spark \
    --ec2-attributes KeyName=myKey \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large \
    --auto-terminate
```

**Example 7: To specify a custom AMI to use for cluster instances**

The following `create-cluster` example creates a cluster instance based on the Amazon Linux AMI with ID `ami-a518e6df`.

```
aws emr create-cluster \
    --name "Cluster with My Custom AMI" \
    --custom-ami-id ami-a518e6df \
    --ebs-root-volume-size 20 \
    --release-label emr-5.9.0 \
    --use-default-roles \
    --instance-count 2 \
    --instance-type m4.large
```

**Example 8: To customize application configurations**

The following examples use the `--configurations` parameter to specify a JSON configuration file that contains application customizations for Hadoop. For more information, see [Configuring Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html) in the *Amazon EMR Release Guide*.

Contents of `configurations.json`:

```
[
    {
       "Classification": "mapred-site",
       "Properties": {
           "mapred.tasktracker.map.tasks.maximum": 2
       }
    },
    {
        "Classification": "hadoop-env",
        "Properties": {},
        "Configurations": [
            {
                "Classification": "export",
                "Properties": {
                    "HADOOP_DATANODE_HEAPSIZE": 2048,
                    "HADOOP_NAMENODE_OPTS": "-XX:GCTimeRatio=19"
                }
            }
        ]
    }
]
```

The following example references `configurations.json` as a local file.

```
aws emr create-cluster \
    --configurations file://configurations.json \
    --release-label emr-5.9.0 \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large \
    --auto-terminate
```

The following example references `configurations.json` as a file in Amazon S3.

```
aws emr create-cluster \
    --configurations https://s3.amazonaws.com/amzn-s3-demo-bucket/configurations.json \
    --release-label emr-5.9.0 \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large \
    --auto-terminate
```

**Example 9: To create a cluster with master, core, and task instance groups**

The following `create-cluster` example uses `--instance-groups` to specify the type and number of EC2 instances to use for master, core, and task instance groups.

```
aws emr create-cluster \
    --release-label emr-5.9.0 \
    --instance-groups Name=Master,InstanceGroupType=MASTER,InstanceType=m4.large,InstanceCount=1 Name=Core,InstanceGroupType=CORE,InstanceType=m4.large,InstanceCount=2 Name=Task,InstanceGroupType=TASK,InstanceType=m4.large,InstanceCount=2
```

**Example 10: To specify that a cluster should terminate after completing all steps**

The following `create-cluster` example uses `--auto-terminate` to specify that the cluster should shut down automatically after completing all steps.

```
aws emr create-cluster \
    --release-label emr-5.9.0 \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large  InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large \
    --auto-terminate
```

**Example 11: To specify cluster configuration details such as the Amazon EC2 key pair, network configuration, and security groups**

The following `create-cluster` example creates a cluster with the Amazon EC2 key pair named `myKey` and a customized instance profile named `myProfile`. Key pairs are used to authorize SSH connections to cluster nodes, most often the master node. For more information, see [Use an Amazon EC2 Key Pair for SSH Credentials](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-access-ssh.html) in the *Amazon EMR Management Guide*.

```
aws emr create-cluster \
    --ec2-attributes KeyName=myKey,InstanceProfile=myProfile \
    --release-label emr-5.9.0 \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large \
    --auto-terminate
```

The following example creates a cluster in an Amazon VPC subnet.

```
aws emr create-cluster \
    --ec2-attributes SubnetId=subnet-xxxxx \
    --release-label emr-5.9.0 \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large \
    --auto-terminate
```

The following example creates a cluster in the `us-east-1b` availability zone.

```
aws emr create-cluster \
    --ec2-attributes AvailabilityZone=us-east-1b \
    --release-label emr-5.9.0 \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large
```

The following example creates a cluster and specifies only the Amazon EMR-managed security groups.

```
aws emr create-cluster \
    --release-label emr-5.9.0 \
    --service-role myServiceRole \
    --ec2-attributes InstanceProfile=myRole,EmrManagedMasterSecurityGroup=sg-master1,EmrManagedSlaveSecurityGroup=sg-slave1 \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large
```

The following example creates a cluster and specifies only additional Amazon EC2 security groups.

```
aws emr create-cluster \
    --release-label emr-5.9.0 \
    --service-role myServiceRole \
    --ec2-attributes InstanceProfile=myRole,AdditionalMasterSecurityGroups=[sg-addMaster1,sg-addMaster2,sg-addMaster3,sg-addMaster4],AdditionalSlaveSecurityGroups=[sg-addSlave1,sg-addSlave2,sg-addSlave3,sg-addSlave4] \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large
```

The following example creates a cluster and specifies the EMR-Managed security groups, as well as additional security groups.

```
aws emr create-cluster \
    --release-label emr-5.9.0 \
    --service-role myServiceRole \
    --ec2-attributes InstanceProfile=myRole,EmrManagedMasterSecurityGroup=sg-master1,EmrManagedSlaveSecurityGroup=sg-slave1,AdditionalMasterSecurityGroups=[sg-addMaster1,sg-addMaster2,sg-addMaster3,sg-addMaster4],AdditionalSlaveSecurityGroups=[sg-addSlave1,sg-addSlave2,sg-addSlave3,sg-addSlave4] \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large
```

The following example creates a cluster in a VPC private subnet and use a specific Amazon EC2 security group to enable Amazon EMR service access, which is required for clusters in private subnets.

```
aws emr create-cluster \
    --release-label emr-5.9.0 \
    --service-role myServiceRole \
    --ec2-attributes InstanceProfile=myRole,ServiceAccessSecurityGroup=sg-service-access,EmrManagedMasterSecurityGroup=sg-master,EmrManagedSlaveSecurityGroup=sg-slave \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large
```

The following example specifies security group configuration parameters using a JSON file named `ec2_attributes.json` that is stored locally.
NOTE: JSON arguments must include options and values as their own items in the list.

```
aws emr create-cluster \
    --release-label emr-5.9.0 \
    --service-role myServiceRole \
    --ec2-attributes file://ec2_attributes.json  \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large
```

Contents of `ec2_attributes.json`:

```
[
    {
        "SubnetId": "subnet-xxxxx",
        "KeyName": "myKey",
        "InstanceProfile":"myRole",
        "EmrManagedMasterSecurityGroup": "sg-master1",
        "EmrManagedSlaveSecurityGroup": "sg-slave1",
        "ServiceAccessSecurityGroup": "sg-service-access",
        "AdditionalMasterSecurityGroups": ["sg-addMaster1","sg-addMaster2","sg-addMaster3","sg-addMaster4"],
        "AdditionalSlaveSecurityGroups": ["sg-addSlave1","sg-addSlave2","sg-addSlave3","sg-addSlave4"]
    }
]
```

**Example 12: To enable debugging and specify a log URI**

The following `create-cluster` example uses the `--enable-debugging` parameter, which allows you to view log files more easily using the debugging tool in the Amazon EMR console. The `--log-uri` parameter is required with `--enable-debugging`.

```
aws emr create-cluster \
    --enable-debugging \
    --log-uri s3://amzn-s3-demo-bucket/myLog \
    --release-label emr-5.9.0 \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large \
    --auto-terminate
```

**Example 13: To add tags when creating a cluster**

Tags are key-value pairs that help you identify and manage clusters. The following `create-cluster` example uses the `--tags` parameter to create three tags for a cluster, one with the key name `name` and the value `Shirley Rodriguez`, a second with the key name `age` and the value `29`, and a third tag with the key name `department` and the value `Analytics`.

```
aws emr create-cluster \
    --tags name="Shirley Rodriguez" age=29 department="Analytics" \
    --release-label emr-5.32.0 \
    --instance-type m5.xlarge \
    --instance-count 3 \
    --use-default-roles
```

The following example lists the tags applied to a cluster.

```
aws emr describe-cluster \
    --cluster-id j-XXXXXXYY \
    --query Cluster.Tags
```

**Example 14: To use a security configuration that enables encryption and other security features**

The following `create-cluster` example uses the `--security-configuration` parameter to specify a security configuration for an EMR cluster. You can use security configurations with Amazon EMR version 4.8.0 or later.

```
aws emr create-cluster \
    --instance-type m4.large \
    --release-label emr-5.9.0 \
    --security-configuration mySecurityConfiguration
```

**Example 15: To create a cluster with additional EBS storage volumes configured for the instance groups**

When specifying additional EBS volumes, the following arguments are required: `VolumeType`, `SizeInGB` if `EbsBlockDeviceConfigs` is specified.

The following `create-cluster` example creates a cluster with multiple EBS volumes attached to EC2 instances in the core instance group.

```
aws emr create-cluster \
    --release-label emr-5.9.0  \
    --use-default-roles \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=d2.xlarge 'InstanceGroupType=CORE,InstanceCount=2,InstanceType=d2.xlarge,EbsConfiguration={EbsOptimized=true,EbsBlockDeviceConfigs=[{VolumeSpecification={VolumeType=gp2,SizeInGB=100}},{VolumeSpecification={VolumeType=io1,SizeInGB=100,Iops=100},VolumesPerInstance=4}]}' \
    --auto-terminate
```

The following example creates a cluster with multiple EBS volumes attached to EC2 instances in the master instance group.

```
aws emr create-cluster \
    --release-label emr-5.9.0 \
    --use-default-roles \
    --instance-groups 'InstanceGroupType=MASTER, InstanceCount=1, InstanceType=d2.xlarge, EbsConfiguration={EbsOptimized=true, EbsBlockDeviceConfigs=[{VolumeSpecification={VolumeType=io1, SizeInGB=100, Iops=100}},{VolumeSpecification={VolumeType=standard,SizeInGB=50},VolumesPerInstance=3}]}' InstanceGroupType=CORE,InstanceCount=2,InstanceType=d2.xlarge \
    --auto-terminate
```

**Example 16: To create a cluster with an automatic scaling policy**

You can attach automatic scaling policies to core and task instance groups using Amazon EMR version 4.0 and later. The automatic scaling policy dynamically adds and removes EC2 instances in response to an Amazon CloudWatch metric. For more information, see Using Automatic Scaling in Amazon EMR <[https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html)>`_ in the *Amazon EMR Management Guide*.

When attaching an automatic scaling policy, you must also specify the default role for automatic scaling using `--auto-scaling-role EMR_AutoScaling_DefaultRole`.

The following `create-cluster` example specifies the automatic scaling policy for the `CORE` instance group using the `AutoScalingPolicy` argument with an embedded JSON structure, which specifies the scaling policy configuration. Instance groups with an embedded JSON structure must have the entire collection of arguments enclosed in single quotes. Using single quotes is optional for instance groups without an embedded JSON structure.

```
aws emr create-cluster
    --release-label emr-5.9.0 \
    --use-default-roles --auto-scaling-role EMR_AutoScaling_DefaultRole \
    --instance-groups InstanceGroupType=MASTER,InstanceType=d2.xlarge,InstanceCount=1 'InstanceGroupType=CORE,InstanceType=d2.xlarge,InstanceCount=2,AutoScalingPolicy={Constraints={MinCapacity=1,MaxCapacity=5},Rules=[{Name=TestRule,Description=TestDescription,Action={Market=ON_DEMAND,SimpleScalingPolicyConfiguration={AdjustmentType=EXACT_CAPACITY,ScalingAdjustment=2}},Trigger={CloudWatchAlarmDefinition={ComparisonOperator=GREATER_THAN,EvaluationPeriods=5,MetricName=TestMetric,Namespace=EMR,Period=3,Statistic=MAXIMUM,Threshold=4.5,Unit=NONE,Dimensions=[{Key=TestKey,Value=TestValue}]}}}]}'
```

The following example uses a JSON file, `instancegroupconfig.json`, to specify the configuration of all instance groups in a cluster. The JSON file specifies the automatic scaling policy configuration for the core instance group.

```
aws emr create-cluster \
    --release-label emr-5.9.0 \
    --service-role EMR_DefaultRole \
    --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole \
    --instance-groups file://myfolder/instancegroupconfig.json \
    --auto-scaling-role EMR_AutoScaling_DefaultRole
```

Contents of `instancegroupconfig.json`:

```
[
    {
        "InstanceCount": 1,
        "Name": "MyMasterIG",
        "InstanceGroupType": "MASTER",
        "InstanceType": "m4.large"
    },
    {
        "InstanceCount": 2,
        "Name": "MyCoreIG",
        "InstanceGroupType": "CORE",
        "InstanceType": "m4.large",
        "AutoScalingPolicy": {
            "Constraints": {
                "MinCapacity": 2,
                "MaxCapacity": 10
            },
            "Rules": [
                {
                    "Name": "Default-scale-out",
                    "Description": "Replicates the default scale-out rule in the console for YARN memory.",
                    "Action": {
                        "SimpleScalingPolicyConfiguration": {
                            "AdjustmentType": "CHANGE_IN_CAPACITY",
                            "ScalingAdjustment": 1,
                            "CoolDown": 300
                        }
                    },
                    "Trigger": {
                        "CloudWatchAlarmDefinition": {
                            "ComparisonOperator": "LESS_THAN",
                            "EvaluationPeriods": 1,
                            "MetricName": "YARNMemoryAvailablePercentage",
                            "Namespace": "AWS/ElasticMapReduce",
                            "Period": 300,
                            "Threshold": 15,
                            "Statistic": "AVERAGE",
                            "Unit": "PERCENT",
                            "Dimensions": [
                                {
                                    "Key": "JobFlowId",
                                    "Value": "${emr.clusterId}"
                                }
                            ]
                        }
                    }
                }
            ]
        }
    }
]
```

**Example 17: Add custom JAR steps when creating a cluster**

The following `create-cluster` example adds steps by specifying a JAR file stored in Amazon S3. Steps submit work to a cluster. The main function defined in the JAR file executes after EC2 instances are provisioned, any bootstrap actions have executed, and applications are installed. The steps are specified using `Type=CUSTOM_JAR`.

Custom JAR steps require the `Jar=` parameter, which specifies the path and file name of the JAR. Optional parameters are `Type`, `Name`, `ActionOnFailure`, `Args`, and `MainClass`. If main class is not specified, the JAR file should specify `Main-Class` in its manifest file.

```
aws emr create-cluster \
    --steps Type=CUSTOM_JAR,Name=CustomJAR,ActionOnFailure=CONTINUE,Jar=s3://amzn-s3-demo-bucket/mytest.jar,Args=arg1,arg2,arg3 Type=CUSTOM_JAR,Name=CustomJAR,ActionOnFailure=CONTINUE,Jar=s3://amzn-s3-demo-bucket/mytest.jar,MainClass=mymainclass,Args=arg1,arg2,arg3  \
    --release-label emr-5.3.1 \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large \
    --auto-terminate
```

**Example 18: To add streaming steps when creating a cluster**

The following `create-cluster` examples add a streaming step to a cluster that terminates after all steps run. Streaming steps require parameters `Type` and `Args`. Streaming steps optional parameters are `Name` and `ActionOnFailure`.

The following example specifies the step inline.

```
aws emr create-cluster \
    --steps Type=STREAMING,Name='Streaming Program',ActionOnFailure=CONTINUE,Args=[-files,s3://elasticmapreduce/samples/wordcount/wordSplitter.py,-mapper,wordSplitter.py,-reducer,aggregate,-input,s3://elasticmapreduce/samples/wordcount/input,-output,s3://amzn-s3-demo-bucket/wordcount/output] \
    --release-label emr-5.3.1 \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large \
    --auto-terminate
```

The following example uses a locally stored JSON configuration file named `multiplefiles.json`. The JSON configuration specifies multiple files. To specify multiple files within a step, you must use a JSON configuration file to specify the step. JSON arguments must include options and values as their own items in the list.

```
aws emr create-cluster \
    --steps file://./multiplefiles.json \
    --release-label emr-5.9.0  \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large \
    --auto-terminate
```

Contents of `multiplefiles.json`:

```
[
    {
        "Name": "JSON Streaming Step",
        "Args": [
            "-files",
            "s3://elasticmapreduce/samples/wordcount/wordSplitter.py",
            "-mapper",
            "wordSplitter.py",
            "-reducer",
            "aggregate",
            "-input",
            "s3://elasticmapreduce/samples/wordcount/input",
            "-output",
            "s3://amzn-s3-demo-bucket/wordcount/output"
        ],
        "ActionOnFailure": "CONTINUE",
        "Type": "STREAMING"
    }
]
```

**Example 19: To add Hive steps when creating a cluster**

The following example add Hive steps when creating a cluster. Hive steps require parameters `Type` and `Args`. Hive steps optional parameters are `Name` and `ActionOnFailure`.

```
aws emr create-cluster \
    --steps Type=HIVE,Name='Hive program',ActionOnFailure=CONTINUE,ActionOnFailure=TERMINATE_CLUSTER,Args=[-f,s3://elasticmapreduce/samples/hive-ads/libs/model-build.q,-d,INPUT=s3://elasticmapreduce/samples/hive-ads/tables,-d,OUTPUT=s3://amzn-s3-demo-bucket/hive-ads/output/2014-04-18/11-07-32,-d,LIBS=s3://elasticmapreduce/samples/hive-ads/libs] \
    --applications Name=Hive \
    --release-label emr-5.3.1 \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large
```

**Example 20: To add Pig steps when creating a cluster**

The following example adds Pig steps when creating a cluster. Pig steps required parameters are `Type` and `Args`. Pig steps optional parameters are `Name` and `ActionOnFailure`.

```
aws emr create-cluster \
    --steps Type=PIG,Name='Pig program',ActionOnFailure=CONTINUE,Args=[-f,s3://elasticmapreduce/samples/pig-apache/do-reports2.pig,-p,INPUT=s3://elasticmapreduce/samples/pig-apache/input,-p,OUTPUT=s3://amzn-s3-demo-bucket/pig-apache/output] \
    --applications Name=Pig \
    --release-label emr-5.3.1 \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large
```

**Example 21: To add bootstrap actions**

The following `create-cluster` example runs two bootstrap actions defined as scripts that are stored in Amazon S3.

```
aws emr create-cluster \
    --bootstrap-actions Path=s3://amzn-s3-demo-bucket/myscript1,Name=BootstrapAction1,Args=[arg1,arg2] Path=s3://amzn-s3-demo-bucket/myscript2,Name=BootstrapAction2,Args=[arg1,arg2] \
    --release-label emr-5.3.1 \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large \
    --auto-terminate
```

**Example 22: To enable EMRFS consistent view and customize the RetryCount and RetryPeriod settings**

The following `create-cluster` example specifies the retry count and retry period for EMRFS consistent view. The `Consistent=true` argument is required.

```
aws emr create-cluster \
    --instance-type m4.large \
    --release-label emr-5.9.0 \
    --emrfs Consistent=true,RetryCount=6,RetryPeriod=30
```

The following example specifies the same EMRFS configuration as the previous example, using a locally stored JSON configuration file named `emrfsconfig.json`.

```
aws emr create-cluster \
    --instance-type m4.large \
    --release-label emr-5.9.0 \
    --emrfs file://emrfsconfig.json
```

Contents of `emrfsconfig.json`:

```
{
    "Consistent": true,
    "RetryCount": 6,
    "RetryPeriod": 30
}
```

**Example 23: To create a cluster with Kerberos configured**

The following `create-cluster` examples create a cluster using a security configuration with Kerberos enabled, and establishes Kerberos parameters for the cluster using `--kerberos-attributes`.

The following command specifies Kerberos attributes for the cluster inline.

```
aws emr create-cluster \
    --instance-type m3.xlarge \
    --release-label emr-5.10.0 \
    --service-role EMR_DefaultRole \
    --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole \
    --security-configuration mySecurityConfiguration \
    --kerberos-attributes Realm=EC2.INTERNAL,KdcAdminPassword=123,CrossRealmTrustPrincipalPassword=123
```

The following command specifies the same attributes, but references a locally stored JSON file named `kerberos_attributes.json`. In this example, the file is saved in the same directory where you run the command. You can also reference a configuration file saved in Amazon S3.

```
aws emr create-cluster \
    --instance-type m3.xlarge \
    --release-label emr-5.10.0 \
    --service-role EMR_DefaultRole \
    --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole \
    --security-configuration mySecurityConfiguration \
    --kerberos-attributes file://kerberos_attributes.json
```

Contents of `kerberos_attributes.json`:

```
{
    "Realm": "EC2.INTERNAL",
    "KdcAdminPassword": "123",
    "CrossRealmTrustPrincipalPassword": "123",
}
```

The following `create-cluster` example creates an Amazon EMR cluster that uses the `--instance-groups` configuration and has a managed scaling policy.

```
aws emr create-cluster \
    --release-label emr-5.30.0 \
    --service-role EMR_DefaultRole \
    --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large
    --managed-scaling-policy ComputeLimits='{MinimumCapacityUnits=2,MaximumCapacityUnits=4,UnitType=Instances}'
```

The following `create-cluster` example creates an Amazon EMR cluster that uses the ââlog-encryption-kms-key-idâ to define KMS key ID utilized for Log encryption.

```
aws emr create-cluster \
    --release-label emr-5.30.0 \
    --log-uri s3://amzn-s3-demo-bucket/myLog \
    --log-encryption-kms-key-id arn:aws:kms:us-east-1:110302272565:key/dd559181-283e-45d7-99d1-66da348c4d33 \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large
```

The following `create-cluster` example creates an Amazon EMR cluster that uses the ââplacement-group-configsâ configuration to place master nodes in a high-availability (HA) cluster within an EC2 placement group using `SPREAD` placement strategy.

```
aws emr create-cluster \
    --release-label emr-5.30.0 \
    --service-role EMR_DefaultRole \
    --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=3,InstanceType=m4.largeInstanceGroupType=CORE,InstanceCount=1,InstanceType=m4.large \
    --placement-group-configs InstanceRole=MASTER
```

The following `create-cluster` example creates an Amazon EMR cluster that uses the ââauto-termination-policyâ configuration to place an automatic idle termination threshold for the cluster.

```
aws emr create-cluster \
    --release-label emr-5.34.0 \
    --service-role EMR_DefaultRole \
    --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=1,InstanceType=m4.large \
    --auto-termination-policy IdleTimeout=100
```

The following `create-cluster` example creates an Amazon EMR cluster that uses the ââos-release-labelâ to define an Amazon Linux release for cluster launch

```
aws emr create-cluster \
    --release-label emr-6.6.0 \
    --os-release-label 2.0.20220406.1 \
    --service-role EMR_DefaultRole \
    --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=1,InstanceType=m4.large
```

**Example 24: To specify an EBS root volume attributes: size, iops and throughput for cluster instances created with EMR releases 6.15.0 and later**

The following `create-cluster` example creates an Amazon EMR cluster that uses root volume attributes to configure root volumes specifications for the EC2 instances.

```
aws emr create-cluster \
    --name "Cluster with My Custom AMI" \
    --custom-ami-id ami-a518e6df \
    --ebs-root-volume-size 20 \
    --ebs-root-volume-iops 3000 \
    --ebs-root-volume-throughput 125 \
    --release-label emr-6.15.0 \
    --use-default-roles \
    --instance-count 2 \
    --instance-type m4.large
```