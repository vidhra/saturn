# create-fleetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# create-fleet

## Description

Creates an EC2 Fleet that contains the configuration information for On-Demand Instances and Spot Instances. Instances are launched immediately if there is available capacity.

A single EC2 Fleet can include multiple launch specifications that vary by instance type, AMI, Availability Zone, or subnet.

For more information, see [EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet.html) in the *Amazon EC2 User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateFleet)

## Synopsis

```
create-fleet
[--dry-run | --no-dry-run]
[--client-token <value>]
[--spot-options <value>]
[--on-demand-options <value>]
[--excess-capacity-termination-policy <value>]
--launch-template-configs <value>
--target-capacity-specification <value>
[--terminate-instances-with-expiration | --no-terminate-instances-with-expiration]
[--type <value>]
[--valid-from <value>]
[--valid-until <value>]
[--replace-unhealthy-instances | --no-replace-unhealthy-instances]
[--tag-specifications <value>]
[--context <value>]
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

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--client-token` (string)

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.

For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .

`--spot-options` (structure)

Describes the configuration of Spot Instances in an EC2 Fleet.

AllocationStrategy -> (string)

The strategy that determines how to allocate the target Spot Instance capacity across the Spot Instance pools specified by the EC2 Fleet launch configuration. For more information, see [Allocation strategies for Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.html) in the *Amazon EC2 User Guide* .

price-capacity-optimized (recommended)

EC2 Fleet identifies the pools with the highest capacity availability for the number of instances that are launching. This means that we will request Spot Instances from the pools that we believe have the lowest chance of interruption in the near term. EC2 Fleet then requests Spot Instances from the lowest priced of these pools.

capacity-optimized

EC2 Fleet identifies the pools with the highest capacity availability for the number of instances that are launching. This means that we will request Spot Instances from the pools that we believe have the lowest chance of interruption in the near term. To give certain instance types a higher chance of launching first, use `capacity-optimized-prioritized` . Set a priority for each instance type by using the `Priority` parameter for `LaunchTemplateOverrides` . You can assign the same priority to different `LaunchTemplateOverrides` . EC2 implements the priorities on a best-effort basis, but optimizes for capacity first. `capacity-optimized-prioritized` is supported only if your EC2 Fleet uses a launch template. Note that if the On-Demand `AllocationStrategy` is set to `prioritized` , the same priority is applied when fulfilling On-Demand capacity.

diversified

EC2 Fleet requests instances from all of the Spot Instance pools that you specify.

lowest-price (not recommended)

### Warning

We donât recommend the `lowest-price` allocation strategy because it has the highest risk of interruption for your Spot Instances.

EC2 Fleet requests instances from the lowest priced Spot Instance pool that has available capacity. If the lowest priced pool doesnât have available capacity, the Spot Instances come from the next lowest priced pool that has available capacity. If a pool runs out of capacity before fulfilling your desired capacity, EC2 Fleet will continue to fulfill your request by drawing from the next lowest priced pool. To ensure that your desired capacity is met, you might receive Spot Instances from several pools. Because this strategy only considers instance price and not capacity availability, it might lead to high interruption rates.

Default: `lowest-price`

MaintenanceStrategies -> (structure)

The strategies for managing your Spot Instances that are at an elevated risk of being interrupted.

CapacityRebalance -> (structure)

The strategy to use when Amazon EC2 emits a signal that your Spot Instance is at an elevated risk of being interrupted.

ReplacementStrategy -> (string)

The replacement strategy to use. Only available for fleets of type `maintain` .

`launch` - EC2 Fleet launches a replacement Spot Instance when a rebalance notification is emitted for an existing Spot Instance in the fleet. EC2 Fleet does not terminate the instances that receive a rebalance notification. You can terminate the old instances, or you can leave them running. You are charged for all instances while they are running.

`launch-before-terminate` - EC2 Fleet launches a replacement Spot Instance when a rebalance notification is emitted for an existing Spot Instance in the fleet, and then, after a delay that you specify (in `TerminationDelay` ), terminates the instances that received a rebalance notification.

TerminationDelay -> (integer)

The amount of time (in seconds) that Amazon EC2 waits before terminating the old Spot Instance after launching a new replacement Spot Instance.

Required when `ReplacementStrategy` is set to `launch-before-terminate` .

Not valid when `ReplacementStrategy` is set to `launch` .

Valid values: Minimum value of `120` seconds. Maximum value of `7200` seconds.

InstanceInterruptionBehavior -> (string)

The behavior when a Spot Instance is interrupted.

Default: `terminate`

InstancePoolsToUseCount -> (integer)

The number of Spot pools across which to allocate your target Spot capacity. Supported only when Spot `AllocationStrategy` is set to `lowest-price` . EC2 Fleet selects the cheapest Spot pools and evenly allocates your target Spot capacity across the number of Spot pools that you specify.

Note that EC2 Fleet attempts to draw Spot Instances from the number of pools that you specify on a best effort basis. If a pool runs out of Spot capacity before fulfilling your target capacity, EC2 Fleet will continue to fulfill your request by drawing from the next cheapest pool. To ensure that your target capacity is met, you might receive Spot Instances from more than the number of pools that you specified. Similarly, if most of the pools have no Spot capacity, you might receive your full target capacity from fewer than the number of pools that you specified.

SingleInstanceType -> (boolean)

Indicates that the fleet uses a single instance type to launch all Spot Instances in the fleet.

Supported only for fleets of type `instant` .

SingleAvailabilityZone -> (boolean)

Indicates that the fleet launches all Spot Instances into a single Availability Zone.

Supported only for fleets of type `instant` .

MinTargetCapacity -> (integer)

The minimum target capacity for Spot Instances in the fleet. If this minimum capacity isnât reached, no instances are launched.

Constraints: Maximum value of `1000` . Supported only for fleets of type `instant` .

At least one of the following must be specified: `SingleAvailabilityZone` | `SingleInstanceType`

MaxTotalPrice -> (string)

The maximum amount per hour for Spot Instances that youâre willing to pay. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.

### Warning

If you specify a maximum price, your Spot Instances will be interrupted more frequently than if you do not specify this parameter.

### Note

If your fleet includes T instances that are configured as `unlimited` , and if their average CPU usage exceeds the baseline utilization, you will incur a charge for surplus credits. The `MaxTotalPrice` does not account for surplus credits, and, if you use surplus credits, your final cost might be higher than what you specified for `MaxTotalPrice` . For more information, see [Surplus credits can incur charges](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html#unlimited-mode-surplus-credits) in the *Amazon EC2 User Guide* .

Shorthand Syntax:

```
AllocationStrategy=string,MaintenanceStrategies={CapacityRebalance={ReplacementStrategy=string,TerminationDelay=integer}},InstanceInterruptionBehavior=string,InstancePoolsToUseCount=integer,SingleInstanceType=boolean,SingleAvailabilityZone=boolean,MinTargetCapacity=integer,MaxTotalPrice=string
```

JSON Syntax:

```
{
  "AllocationStrategy": "lowest-price"|"diversified"|"capacity-optimized"|"capacity-optimized-prioritized"|"price-capacity-optimized",
  "MaintenanceStrategies": {
    "CapacityRebalance": {
      "ReplacementStrategy": "launch"|"launch-before-terminate",
      "TerminationDelay": integer
    }
  },
  "InstanceInterruptionBehavior": "hibernate"|"stop"|"terminate",
  "InstancePoolsToUseCount": integer,
  "SingleInstanceType": true|false,
  "SingleAvailabilityZone": true|false,
  "MinTargetCapacity": integer,
  "MaxTotalPrice": "string"
}
```

`--on-demand-options` (structure)

Describes the configuration of On-Demand Instances in an EC2 Fleet.

AllocationStrategy -> (string)

The strategy that determines the order of the launch template overrides to use in fulfilling On-Demand capacity.

`lowest-price` - EC2 Fleet uses price to determine the order, launching the lowest price first.

`prioritized` - EC2 Fleet uses the priority that you assigned to each launch template override, launching the highest priority first.

Default: `lowest-price`

CapacityReservationOptions -> (structure)

The strategy for using unused Capacity Reservations for fulfilling On-Demand capacity.

Supported only for fleets of type `instant` .

UsageStrategy -> (string)

Indicates whether to use unused Capacity Reservations for fulfilling On-Demand capacity.

If you specify `use-capacity-reservations-first` , the fleet uses unused Capacity Reservations to fulfill On-Demand capacity up to the target On-Demand capacity. If multiple instance pools have unused Capacity Reservations, the On-Demand allocation strategy (`lowest-price` or `prioritized` ) is applied. If the number of unused Capacity Reservations is less than the On-Demand target capacity, the remaining On-Demand target capacity is launched according to the On-Demand allocation strategy (`lowest-price` or `prioritized` ).

If you do not specify a value, the fleet fulfils the On-Demand capacity according to the chosen On-Demand allocation strategy.

SingleInstanceType -> (boolean)

Indicates that the fleet uses a single instance type to launch all On-Demand Instances in the fleet.

Supported only for fleets of type `instant` .

SingleAvailabilityZone -> (boolean)

Indicates that the fleet launches all On-Demand Instances into a single Availability Zone.

Supported only for fleets of type `instant` .

MinTargetCapacity -> (integer)

The minimum target capacity for On-Demand Instances in the fleet. If this minimum capacity isnât reached, no instances are launched.

Constraints: Maximum value of `1000` . Supported only for fleets of type `instant` .

At least one of the following must be specified: `SingleAvailabilityZone` | `SingleInstanceType`

MaxTotalPrice -> (string)

The maximum amount per hour for On-Demand Instances that youâre willing to pay.

### Note

If your fleet includes T instances that are configured as `unlimited` , and if their average CPU usage exceeds the baseline utilization, you will incur a charge for surplus credits. The `MaxTotalPrice` does not account for surplus credits, and, if you use surplus credits, your final cost might be higher than what you specified for `MaxTotalPrice` . For more information, see [Surplus credits can incur charges](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html#unlimited-mode-surplus-credits) in the *Amazon EC2 User Guide* .

Shorthand Syntax:

```
AllocationStrategy=string,CapacityReservationOptions={UsageStrategy=string},SingleInstanceType=boolean,SingleAvailabilityZone=boolean,MinTargetCapacity=integer,MaxTotalPrice=string
```

JSON Syntax:

```
{
  "AllocationStrategy": "lowest-price"|"prioritized",
  "CapacityReservationOptions": {
    "UsageStrategy": "use-capacity-reservations-first"
  },
  "SingleInstanceType": true|false,
  "SingleAvailabilityZone": true|false,
  "MinTargetCapacity": integer,
  "MaxTotalPrice": "string"
}
```

`--excess-capacity-termination-policy` (string)

Indicates whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2 Fleet.

Supported only for fleets of type `maintain` .

Possible values:

- `no-termination`
- `termination`

`--launch-template-configs` (list)

The configuration for the EC2 Fleet.

(structure)

Describes a launch template and overrides.

LaunchTemplateSpecification -> (structure)

The launch template to use. You must specify either the launch template ID or launch template name in the request.

LaunchTemplateId -> (string)

The ID of the launch template.

You must specify the `LaunchTemplateId` or the `LaunchTemplateName` , but not both.

LaunchTemplateName -> (string)

The name of the launch template.

You must specify the `LaunchTemplateName` or the `LaunchTemplateId` , but not both.

Version -> (string)

The launch template version number, `$Latest` , or `$Default` . You must specify a value, otherwise the request fails.

If the value is `$Latest` , Amazon EC2 uses the latest version of the launch template.

If the value is `$Default` , Amazon EC2 uses the default version of the launch template.

Overrides -> (list)

Any parameters that you specify override the same parameters in the launch template.

For fleets of type `request` and `maintain` , a maximum of 300 items is allowed across all launch templates.

(structure)

Describes overrides for a launch template.

InstanceType -> (string)

The instance type.

`mac1.metal` is not supported as a launch template override.

### Note

If you specify `InstanceType` , you canât specify `InstanceRequirements` .

MaxPrice -> (string)

The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.

### Warning

If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.

If you specify a maximum price, it must be more than USD $0.001. Specifying a value below USD $0.001 will result in an `InvalidParameterValue` error message.

SubnetId -> (string)

The IDs of the subnets in which to launch the instances. Separate multiple subnet IDs using commas (for example, `subnet-1234abcdeexample1, subnet-0987cdef6example2` ). A request of type `instant` can have only one subnet ID.

AvailabilityZone -> (string)

The Availability Zone in which to launch the instances.

WeightedCapacity -> (double)

The number of units provided by the specified instance type. These are the same units that you chose to set the target capacity in terms of instances, or a performance characteristic such as vCPUs, memory, or I/O.

If the target capacity divided by this value is not a whole number, Amazon EC2 rounds the number of instances to the next whole number. If this value is not specified, the default is 1.

### Note

When specifying weights, the price used in the `lowest-price` and `price-capacity-optimized` allocation strategies is per *unit* hour (where the instance price is divided by the specified weight). However, if all the specified weights are above the requested `TargetCapacity` , resulting in only 1 instance being launched, the price used is per *instance* hour.

Priority -> (double)

The priority for the launch template override. The highest priority is launched first.

If the On-Demand `AllocationStrategy` is set to `prioritized` , EC2 Fleet uses priority to determine which launch template override to use first in fulfilling On-Demand capacity.

If the Spot `AllocationStrategy` is set to `capacity-optimized-prioritized` , EC2 Fleet uses priority on a best-effort basis to determine which launch template override to use in fulfilling Spot capacity, but optimizes for capacity first.

Valid values are whole numbers starting at `0` . The lower the number, the higher the priority. If no number is set, the launch template override has the lowest priority. You can set the same priority for different launch template overrides.

Placement -> (structure)

The location where the instance launched, if applicable.

Affinity -> (string)

The affinity setting for the instance on the Dedicated Host.

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) or [ImportInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html) .

GroupName -> (string)

The name of the placement group that the instance is in. If you specify `GroupName` , you canât specify `GroupId` .

PartitionNumber -> (integer)

The number of the partition that the instance is in. Valid only if the placement group strategy is set to `partition` .

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) .

HostId -> (string)

The ID of the Dedicated Host on which the instance resides.

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) or [ImportInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html) .

Tenancy -> (string)

The tenancy of the instance. An instance with a tenancy of `dedicated` runs on single-tenant hardware.

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) . The `host` tenancy is not supported for [ImportInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html) or for T3 instances that are configured for the `unlimited` CPU credit option.

SpreadDomain -> (string)

Reserved for future use.

HostResourceGroupArn -> (string)

The ARN of the host resource group in which to launch the instances.

If you specify this parameter, either omit the **Tenancy** parameter or set it to `host` .

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) .

GroupId -> (string)

The ID of the placement group that the instance is in. If you specify `GroupId` , you canât specify `GroupName` .

AvailabilityZone -> (string)

The Availability Zone of the instance.

If not specified, an Availability Zone will be automatically chosen for you based on the load balancing criteria for the Region.

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) .

BlockDeviceMappings -> (list)

The block device mappings, which define the EBS volumes and instance store volumes to attach to the instance at launch.

Supported only for fleets of type `instant` .

For more information, see [Block device mappings for volumes on Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html) in the *Amazon EC2 User Guide* .

(structure)

Describes a block device mapping, which defines the EBS volumes and instance store volumes to attach to an instance at launch.

To override a block device mapping specified in the launch template:

- Specify the exact same `DeviceName` here as specified in the launch template.
- Only specify the parameters you want to change.
- Any parameters you donât specify here will keep their original launch template values.

To add a new block device mapping:

- Specify a `DeviceName` that doesnât exist in the launch template.
- Specify all desired parameters here.

DeviceName -> (string)

The device name (for example, `/dev/sdh` or `xvdh` ).

VirtualName -> (string)

The virtual device name (`ephemeralN` ). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for `ephemeral0` and `ephemeral1` . The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.

NVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect.

Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.

Ebs -> (structure)

Parameters used to automatically set up EBS volumes when the instance is launched.

Encrypted -> (boolean)

Indicates whether the encryption state of an EBS volume is changed while being restored from a backing snapshot. The effect of setting the encryption state to `true` depends on the volume origin (new or from a snapshot), starting encryption state, ownership, and whether encryption by default is enabled. For more information, see [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html) in the *Amazon EBS User Guide* .

In no case can you remove encryption from an encrypted volume.

Encrypted volumes can only be attached to instances that support Amazon EBS encryption. For more information, see [Supported instance types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption-requirements.html#ebs-encryption_supported_instances) .

This parameter is not returned by [DescribeImageAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImageAttribute) .

For [CreateImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage) and [RegisterImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RegisterImage) , whether you can include this parameter, and the allowed values differ depending on the type of block device mapping you are creating.

- If you are creating a block device mapping for a **new (empty) volume** , you can include this parameter, and specify either `true` for an encrypted volume, or `false` for an unencrypted volume. If you omit this parameter, it defaults to `false` (unencrypted).
- If you are creating a block device mapping from an **existing encrypted or unencrypted snapshot** , you must omit this parameter. If you include this parameter, the request will fail, regardless of the value that you specify.
- If you are creating a block device mapping from an **existing unencrypted volume** , you can include this parameter, but you must specify `false` . If you specify `true` , the request will fail. In this case, we recommend that you omit the parameter.
- If you are creating a block device mapping from an **existing encrypted volume** , you can include this parameter, and specify either `true` or `false` . However, if you specify `false` , the parameter is ignored and the block device mapping is always encrypted. In this case, we recommend that you omit the parameter.

DeleteOnTermination -> (boolean)

Indicates whether the EBS volume is deleted on instance termination. For more information, see [Preserve data when an instance is terminated](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/preserving-volumes-on-termination.html) in the *Amazon EC2 User Guide* .

Iops -> (integer)

The number of I/O operations per second (IOPS). For `gp3` , `io1` , and `io2` volumes, this represents the number of IOPS that are provisioned for the volume. For `gp2` volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.

The following are the supported values for each volume type:

- `gp3` : 3,000 - 16,000 IOPS
- `io1` : 100 - 64,000 IOPS
- `io2` : 100 - 256,000 IOPS

For `io2` volumes, you can achieve up to 256,000 IOPS on [instances built on the Nitro System](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances) . On other instances, you can achieve performance up to 32,000 IOPS.

This parameter is required for `io1` and `io2` volumes. The default for `gp3` volumes is 3,000 IOPS.

Throughput -> (integer)

The throughput that the volume supports, in MiB/s.

This parameter is valid only for `gp3` volumes.

Valid Range: Minimum value of 125. Maximum value of 1000.

KmsKeyId -> (string)

Identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed KMS key to use for EBS encryption.

This parameter is only supported on `BlockDeviceMapping` objects called by [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet.html) , [RequestSpotInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html) , and [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) .

SnapshotId -> (string)

The ID of the snapshot.

VolumeSize -> (integer)

The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size. If you specify a snapshot, the default is the snapshot size. You can specify a volume size that is equal to or larger than the snapshot size.

The following are the supported sizes for each volume type:

- `gp2` and `gp3` : 1 - 16,384 GiB
- `io1` : 4 - 16,384 GiB
- `io2` : 4 - 65,536 GiB
- `st1` and `sc1` : 125 - 16,384 GiB
- `standard` : 1 - 1024 GiB

VolumeType -> (string)

The volume type. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) in the *Amazon EBS User Guide* .

NoDevice -> (string)

To omit the device from the block device mapping, specify an empty string. When this property is specified, the device is removed from the block device mapping regardless of the assigned value.

InstanceRequirements -> (structure)

The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with those attributes.

### Note

If you specify `InstanceRequirements` , you canât specify `InstanceType` .

VCpuCount -> (structure)

The minimum and maximum number of vCPUs.

Min -> (integer)

The minimum number of vCPUs. To specify no minimum limit, specify `0` .

Max -> (integer)

The maximum number of vCPUs. To specify no maximum limit, omit this parameter.

MemoryMiB -> (structure)

The minimum and maximum amount of memory, in MiB.

Min -> (integer)

The minimum amount of memory, in MiB. To specify no minimum limit, specify `0` .

Max -> (integer)

The maximum amount of memory, in MiB. To specify no maximum limit, omit this parameter.

CpuManufacturers -> (list)

The CPU manufacturers to include.

- For instance types with Intel CPUs, specify `intel` .
- For instance types with AMD CPUs, specify `amd` .
- For instance types with Amazon Web Services CPUs, specify `amazon-web-services` .
- For instance types with Apple CPUs, specify `apple` .

### Note

Donât confuse the CPU manufacturer with the CPU architecture. Instances will be launched with a compatible CPU architecture based on the Amazon Machine Image (AMI) that you specify in your launch template.

Default: Any manufacturer

(string)

MemoryGiBPerVCpu -> (structure)

The minimum and maximum amount of memory per vCPU, in GiB.

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of memory per vCPU, in GiB. To specify no minimum limit, omit this parameter.

Max -> (double)

The maximum amount of memory per vCPU, in GiB. To specify no maximum limit, omit this parameter.

ExcludedInstanceTypes -> (list)

The instance types to exclude.

You can use strings with one or more wild cards, represented by an asterisk (`*` ), to exclude an instance family, type, size, or generation. The following are examples: `m5.8xlarge` , `c5*.*` , `m5a.*` , `r*` , `*3*` .

For example, if you specify `c5*` ,Amazon EC2 will exclude the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*` , Amazon EC2 will exclude all the M5a instance types, but not the M5n instance types.

### Note

If you specify `ExcludedInstanceTypes` , you canât specify `AllowedInstanceTypes` .

Default: No excluded instance types

(string)

InstanceGenerations -> (list)

Indicates whether current or previous generation instance types are included. The current generation instance types are recommended for use. Current generation instance types are typically the latest two to three generations in each instance family. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide* .

For current generation instance types, specify `current` .

For previous generation instance types, specify `previous` .

Default: Current and previous generation instance types

(string)

SpotMaxPricePercentageOverLowestPrice -> (integer)

[Price protection] The price protection threshold for Spot Instances, as a percentage higher than an identified Spot price. The identified Spot price is the Spot price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified Spot price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose Spot price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 interprets as a percentage.

If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib` , the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.

This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) and [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html) .

### Note

Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you donât specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999` .

Default: `100`

OnDemandMaxPricePercentageOverLowestPrice -> (integer)

[Price protection] The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 interprets as a percentage.

To indicate no price protection threshold, specify a high value, such as `999999` .

This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) and [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html) .

### Note

If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib` , the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.

Default: `20`

BareMetal -> (string)

Indicates whether bare metal instance types must be included, excluded, or required.

- To include bare metal instance types, specify `included` .
- To require only bare metal instance types, specify `required` .
- To exclude bare metal instance types, specify `excluded` .

Default: `excluded`

BurstablePerformance -> (string)

Indicates whether burstable performance T instance types are included, excluded, or required. For more information, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) .

- To include burstable performance instance types, specify `included` .
- To require only burstable performance instance types, specify `required` .
- To exclude burstable performance instance types, specify `excluded` .

Default: `excluded`

RequireHibernateSupport -> (boolean)

Indicates whether instance types must support hibernation for On-Demand Instances.

This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) .

Default: `false`

NetworkInterfaceCount -> (structure)

The minimum and maximum number of network interfaces.

Default: No minimum or maximum limits

Min -> (integer)

The minimum number of network interfaces. To specify no minimum limit, omit this parameter.

Max -> (integer)

The maximum number of network interfaces. To specify no maximum limit, omit this parameter.

LocalStorage -> (string)

Indicates whether instance types with instance store volumes are included, excluded, or required. For more information, [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) in the *Amazon EC2 User Guide* .

- To include instance types with instance store volumes, specify `included` .
- To require only instance types with instance store volumes, specify `required` .
- To exclude instance types with instance store volumes, specify `excluded` .

Default: `included`

LocalStorageTypes -> (list)

The type of local storage that is required.

- For instance types with hard disk drive (HDD) storage, specify `hdd` .
- For instance types with solid state drive (SSD) storage, specify `ssd` .

Default: `hdd` and `ssd`

(string)

TotalLocalStorageGB -> (structure)

The minimum and maximum amount of total local storage, in GB.

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of total local storage, in GB. To specify no minimum limit, omit this parameter.

Max -> (double)

The maximum amount of total local storage, in GB. To specify no maximum limit, omit this parameter.

BaselineEbsBandwidthMbps -> (structure)

The minimum and maximum baseline bandwidth to Amazon EBS, in Mbps. For more information, see [Amazon EBSâoptimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) in the *Amazon EC2 User Guide* .

Default: No minimum or maximum limits

Min -> (integer)

The minimum baseline bandwidth, in Mbps. To specify no minimum limit, omit this parameter.

Max -> (integer)

The maximum baseline bandwidth, in Mbps. To specify no maximum limit, omit this parameter.

AcceleratorTypes -> (list)

The accelerator types that must be on the instance type.

- For instance types with FPGA accelerators, specify `fpga` .
- For instance types with GPU accelerators, specify `gpu` .
- For instance types with Inference accelerators, specify `inference` .

Default: Any accelerator type

(string)

AcceleratorCount -> (structure)

The minimum and maximum number of accelerators (GPUs, FPGAs, or Amazon Web Services Inferentia chips) on an instance.

To exclude accelerator-enabled instance types, set `Max` to `0` .

Default: No minimum or maximum limits

Min -> (integer)

The minimum number of accelerators. To specify no minimum limit, omit this parameter.

Max -> (integer)

The maximum number of accelerators. To specify no maximum limit, omit this parameter. To exclude accelerator-enabled instance types, set `Max` to `0` .

AcceleratorManufacturers -> (list)

Indicates whether instance types must have accelerators by specific manufacturers.

- For instance types with Amazon Web Services devices, specify `amazon-web-services` .
- For instance types with AMD devices, specify `amd` .
- For instance types with Habana devices, specify `habana` .
- For instance types with NVIDIA devices, specify `nvidia` .
- For instance types with Xilinx devices, specify `xilinx` .

Default: Any manufacturer

(string)

AcceleratorNames -> (list)

The accelerators that must be on the instance type.

- For instance types with NVIDIA A10G GPUs, specify `a10g` .
- For instance types with NVIDIA A100 GPUs, specify `a100` .
- For instance types with NVIDIA H100 GPUs, specify `h100` .
- For instance types with Amazon Web Services Inferentia chips, specify `inferentia` .
- For instance types with NVIDIA GRID K520 GPUs, specify `k520` .
- For instance types with NVIDIA K80 GPUs, specify `k80` .
- For instance types with NVIDIA M60 GPUs, specify `m60` .
- For instance types with AMD Radeon Pro V520 GPUs, specify `radeon-pro-v520` .
- For instance types with NVIDIA T4 GPUs, specify `t4` .
- For instance types with NVIDIA T4G GPUs, specify `t4g` .
- For instance types with Xilinx VU9P FPGAs, specify `vu9p` .
- For instance types with NVIDIA V100 GPUs, specify `v100` .

Default: Any accelerator

(string)

AcceleratorTotalMemoryMiB -> (structure)

The minimum and maximum amount of total accelerator memory, in MiB.

Default: No minimum or maximum limits

Min -> (integer)

The minimum amount of accelerator memory, in MiB. To specify no minimum limit, omit this parameter.

Max -> (integer)

The maximum amount of accelerator memory, in MiB. To specify no maximum limit, omit this parameter.

NetworkBandwidthGbps -> (structure)

The minimum and maximum amount of baseline network bandwidth, in gigabits per second (Gbps). For more information, see [Amazon EC2 instance network bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html) in the *Amazon EC2 User Guide* .

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of network bandwidth, in Gbps. To specify no minimum limit, omit this parameter.

Max -> (double)

The maximum amount of network bandwidth, in Gbps. To specify no maximum limit, omit this parameter.

AllowedInstanceTypes -> (list)

The instance types to apply your specified attributes against. All other instance types are ignored, even if they match your specified attributes.

You can use strings with one or more wild cards, represented by an asterisk (`*` ), to allow an instance type, size, or generation. The following are examples: `m5.8xlarge` , `c5*.*` , `m5a.*` , `r*` , `*3*` .

For example, if you specify `c5*` ,Amazon EC2 will allow the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*` , Amazon EC2 will allow all the M5a instance types, but not the M5n instance types.

### Note

If you specify `AllowedInstanceTypes` , you canât specify `ExcludedInstanceTypes` .

Default: All instance types

(string)

MaxSpotPriceAsPercentageOfOptimalOnDemandPrice -> (integer)

[Price protection] The price protection threshold for Spot Instances, as a percentage of an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 interprets as a percentage.

If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib` , the price protection threshold is based on the per vCPU or per memory price instead of the per instance price.

### Note

Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you donât specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999` .

BaselinePerformanceFactors -> (structure)

The baseline performance to consider, using an instance family as a baseline reference. The instance family establishes the lowest acceptable level of performance. Amazon EC2 uses this baseline to guide instance type selection, but there is no guarantee that the selected instance types will always exceed the baseline for every application. Currently, this parameter only supports CPU performance as a baseline performance factor. For more information, see [Performance protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html#ec2fleet-abis-performance-protection) in the *Amazon EC2 User Guide* .

Cpu -> (structure)

The CPU performance to consider, using an instance family as the baseline reference.

References -> (list)

Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture differences.

### Note

Currently, only one instance family can be specified in the list.

(structure)

Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture.

### Note

Currently, only one instance family can be specified in the list.

InstanceFamily -> (string)

The instance family to use as a baseline reference.

### Note

Ensure that you specify the correct value for the instance family. The instance family is everything before the period (`.` ) in the instance type name. For example, in the instance type `c6i.large` , the instance family is `c6i` , not `c6` . For more information, see [Amazon EC2 instance type naming conventions](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html) in *Amazon EC2 Instance Types* .

The following instance families are *not supported* for performance protection:

- `c1`
- `g3` | `g3s`
- `hpc7g`
- `m1` | `m2`
- `mac1` | `mac2` | `mac2-m1ultra` | `mac2-m2` | `mac2-m2pro`
- `p3dn` | `p4d` | `p5`
- `t1`
- `u-12tb1` | `u-18tb1` | `u-24tb1` | `u-3tb1` | `u-6tb1` | `u-9tb1` | `u7i-12tb` | `u7in-16tb` | `u7in-24tb` | `u7in-32tb`

If you enable performance protection by specifying a supported instance family, the returned instance types will exclude the above unsupported instance families.

If you specify an unsupported instance family as a value for baseline performance, the API returns an empty response for [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements) and an exception for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) , [RequestSpotFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet) , [ModifyFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyFleet) , and [ModifySpotFleetRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySpotFleetRequest) .

ImageId -> (string)

The ID of the AMI in the format `ami-17characters00000` .

Alternatively, you can specify a Systems Manager parameter, using one of the following formats. The Systems Manager parameter will resolve to an AMI ID on launch.

To reference a public parameter:

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id1)resolve:ssm:*public-parameter* ``

To reference a parameter stored in the same account:

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id3)resolve:ssm:*parameter-name* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id5)resolve:ssm:*parameter-name:version-number* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id7)resolve:ssm:*parameter-name:label* ``

To reference a parameter shared from another Amazon Web Services account:

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id9)resolve:ssm:*parameter-ARN* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id11)resolve:ssm:*parameter-ARN:version-number* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id13)resolve:ssm:*parameter-ARN:label* ``

For more information, see [Use a Systems Manager parameter instead of an AMI ID](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#use-an-ssm-parameter-instead-of-an-ami-id) in the *Amazon EC2 User Guide* .

### Note

This parameter is only available for fleets of type `instant` . For fleets of type `maintain` and `request` , you must specify the AMI ID in the launch template.

JSON Syntax:

```
[
  {
    "LaunchTemplateSpecification": {
      "LaunchTemplateId": "string",
      "LaunchTemplateName": "string",
      "Version": "string"
    },
    "Overrides": [
      {
        "InstanceType": "a1.medium"|"a1.large"|"a1.xlarge"|"a1.2xlarge"|"a1.4xlarge"|"a1.metal"|"c1.medium"|"c1.xlarge"|"c3.large"|"c3.xlarge"|"c3.2xlarge"|"c3.4xlarge"|"c3.8xlarge"|"c4.large"|"c4.xlarge"|"c4.2xlarge"|"c4.4xlarge"|"c4.8xlarge"|"c5.large"|"c5.xlarge"|"c5.2xlarge"|"c5.4xlarge"|"c5.9xlarge"|"c5.12xlarge"|"c5.18xlarge"|"c5.24xlarge"|"c5.metal"|"c5a.large"|"c5a.xlarge"|"c5a.2xlarge"|"c5a.4xlarge"|"c5a.8xlarge"|"c5a.12xlarge"|"c5a.16xlarge"|"c5a.24xlarge"|"c5ad.large"|"c5ad.xlarge"|"c5ad.2xlarge"|"c5ad.4xlarge"|"c5ad.8xlarge"|"c5ad.12xlarge"|"c5ad.16xlarge"|"c5ad.24xlarge"|"c5d.large"|"c5d.xlarge"|"c5d.2xlarge"|"c5d.4xlarge"|"c5d.9xlarge"|"c5d.12xlarge"|"c5d.18xlarge"|"c5d.24xlarge"|"c5d.metal"|"c5n.large"|"c5n.xlarge"|"c5n.2xlarge"|"c5n.4xlarge"|"c5n.9xlarge"|"c5n.18xlarge"|"c5n.metal"|"c6g.medium"|"c6g.large"|"c6g.xlarge"|"c6g.2xlarge"|"c6g.4xlarge"|"c6g.8xlarge"|"c6g.12xlarge"|"c6g.16xlarge"|"c6g.metal"|"c6gd.medium"|"c6gd.large"|"c6gd.xlarge"|"c6gd.2xlarge"|"c6gd.4xlarge"|"c6gd.8xlarge"|"c6gd.12xlarge"|"c6gd.16xlarge"|"c6gd.metal"|"c6gn.medium"|"c6gn.large"|"c6gn.xlarge"|"c6gn.2xlarge"|"c6gn.4xlarge"|"c6gn.8xlarge"|"c6gn.12xlarge"|"c6gn.16xlarge"|"c6i.large"|"c6i.xlarge"|"c6i.2xlarge"|"c6i.4xlarge"|"c6i.8xlarge"|"c6i.12xlarge"|"c6i.16xlarge"|"c6i.24xlarge"|"c6i.32xlarge"|"c6i.metal"|"cc1.4xlarge"|"cc2.8xlarge"|"cg1.4xlarge"|"cr1.8xlarge"|"d2.xlarge"|"d2.2xlarge"|"d2.4xlarge"|"d2.8xlarge"|"d3.xlarge"|"d3.2xlarge"|"d3.4xlarge"|"d3.8xlarge"|"d3en.xlarge"|"d3en.2xlarge"|"d3en.4xlarge"|"d3en.6xlarge"|"d3en.8xlarge"|"d3en.12xlarge"|"dl1.24xlarge"|"f1.2xlarge"|"f1.4xlarge"|"f1.16xlarge"|"g2.2xlarge"|"g2.8xlarge"|"g3.4xlarge"|"g3.8xlarge"|"g3.16xlarge"|"g3s.xlarge"|"g4ad.xlarge"|"g4ad.2xlarge"|"g4ad.4xlarge"|"g4ad.8xlarge"|"g4ad.16xlarge"|"g4dn.xlarge"|"g4dn.2xlarge"|"g4dn.4xlarge"|"g4dn.8xlarge"|"g4dn.12xlarge"|"g4dn.16xlarge"|"g4dn.metal"|"g5.xlarge"|"g5.2xlarge"|"g5.4xlarge"|"g5.8xlarge"|"g5.12xlarge"|"g5.16xlarge"|"g5.24xlarge"|"g5.48xlarge"|"g5g.xlarge"|"g5g.2xlarge"|"g5g.4xlarge"|"g5g.8xlarge"|"g5g.16xlarge"|"g5g.metal"|"hi1.4xlarge"|"hpc6a.48xlarge"|"hs1.8xlarge"|"h1.2xlarge"|"h1.4xlarge"|"h1.8xlarge"|"h1.16xlarge"|"i2.xlarge"|"i2.2xlarge"|"i2.4xlarge"|"i2.8xlarge"|"i3.large"|"i3.xlarge"|"i3.2xlarge"|"i3.4xlarge"|"i3.8xlarge"|"i3.16xlarge"|"i3.metal"|"i3en.large"|"i3en.xlarge"|"i3en.2xlarge"|"i3en.3xlarge"|"i3en.6xlarge"|"i3en.12xlarge"|"i3en.24xlarge"|"i3en.metal"|"im4gn.large"|"im4gn.xlarge"|"im4gn.2xlarge"|"im4gn.4xlarge"|"im4gn.8xlarge"|"im4gn.16xlarge"|"inf1.xlarge"|"inf1.2xlarge"|"inf1.6xlarge"|"inf1.24xlarge"|"is4gen.medium"|"is4gen.large"|"is4gen.xlarge"|"is4gen.2xlarge"|"is4gen.4xlarge"|"is4gen.8xlarge"|"m1.small"|"m1.medium"|"m1.large"|"m1.xlarge"|"m2.xlarge"|"m2.2xlarge"|"m2.4xlarge"|"m3.medium"|"m3.large"|"m3.xlarge"|"m3.2xlarge"|"m4.large"|"m4.xlarge"|"m4.2xlarge"|"m4.4xlarge"|"m4.10xlarge"|"m4.16xlarge"|"m5.large"|"m5.xlarge"|"m5.2xlarge"|"m5.4xlarge"|"m5.8xlarge"|"m5.12xlarge"|"m5.16xlarge"|"m5.24xlarge"|"m5.metal"|"m5a.large"|"m5a.xlarge"|"m5a.2xlarge"|"m5a.4xlarge"|"m5a.8xlarge"|"m5a.12xlarge"|"m5a.16xlarge"|"m5a.24xlarge"|"m5ad.large"|"m5ad.xlarge"|"m5ad.2xlarge"|"m5ad.4xlarge"|"m5ad.8xlarge"|"m5ad.12xlarge"|"m5ad.16xlarge"|"m5ad.24xlarge"|"m5d.large"|"m5d.xlarge"|"m5d.2xlarge"|"m5d.4xlarge"|"m5d.8xlarge"|"m5d.12xlarge"|"m5d.16xlarge"|"m5d.24xlarge"|"m5d.metal"|"m5dn.large"|"m5dn.xlarge"|"m5dn.2xlarge"|"m5dn.4xlarge"|"m5dn.8xlarge"|"m5dn.12xlarge"|"m5dn.16xlarge"|"m5dn.24xlarge"|"m5dn.metal"|"m5n.large"|"m5n.xlarge"|"m5n.2xlarge"|"m5n.4xlarge"|"m5n.8xlarge"|"m5n.12xlarge"|"m5n.16xlarge"|"m5n.24xlarge"|"m5n.metal"|"m5zn.large"|"m5zn.xlarge"|"m5zn.2xlarge"|"m5zn.3xlarge"|"m5zn.6xlarge"|"m5zn.12xlarge"|"m5zn.metal"|"m6a.large"|"m6a.xlarge"|"m6a.2xlarge"|"m6a.4xlarge"|"m6a.8xlarge"|"m6a.12xlarge"|"m6a.16xlarge"|"m6a.24xlarge"|"m6a.32xlarge"|"m6a.48xlarge"|"m6g.metal"|"m6g.medium"|"m6g.large"|"m6g.xlarge"|"m6g.2xlarge"|"m6g.4xlarge"|"m6g.8xlarge"|"m6g.12xlarge"|"m6g.16xlarge"|"m6gd.metal"|"m6gd.medium"|"m6gd.large"|"m6gd.xlarge"|"m6gd.2xlarge"|"m6gd.4xlarge"|"m6gd.8xlarge"|"m6gd.12xlarge"|"m6gd.16xlarge"|"m6i.large"|"m6i.xlarge"|"m6i.2xlarge"|"m6i.4xlarge"|"m6i.8xlarge"|"m6i.12xlarge"|"m6i.16xlarge"|"m6i.24xlarge"|"m6i.32xlarge"|"m6i.metal"|"mac1.metal"|"p2.xlarge"|"p2.8xlarge"|"p2.16xlarge"|"p3.2xlarge"|"p3.8xlarge"|"p3.16xlarge"|"p3dn.24xlarge"|"p4d.24xlarge"|"r3.large"|"r3.xlarge"|"r3.2xlarge"|"r3.4xlarge"|"r3.8xlarge"|"r4.large"|"r4.xlarge"|"r4.2xlarge"|"r4.4xlarge"|"r4.8xlarge"|"r4.16xlarge"|"r5.large"|"r5.xlarge"|"r5.2xlarge"|"r5.4xlarge"|"r5.8xlarge"|"r5.12xlarge"|"r5.16xlarge"|"r5.24xlarge"|"r5.metal"|"r5a.large"|"r5a.xlarge"|"r5a.2xlarge"|"r5a.4xlarge"|"r5a.8xlarge"|"r5a.12xlarge"|"r5a.16xlarge"|"r5a.24xlarge"|"r5ad.large"|"r5ad.xlarge"|"r5ad.2xlarge"|"r5ad.4xlarge"|"r5ad.8xlarge"|"r5ad.12xlarge"|"r5ad.16xlarge"|"r5ad.24xlarge"|"r5b.large"|"r5b.xlarge"|"r5b.2xlarge"|"r5b.4xlarge"|"r5b.8xlarge"|"r5b.12xlarge"|"r5b.16xlarge"|"r5b.24xlarge"|"r5b.metal"|"r5d.large"|"r5d.xlarge"|"r5d.2xlarge"|"r5d.4xlarge"|"r5d.8xlarge"|"r5d.12xlarge"|"r5d.16xlarge"|"r5d.24xlarge"|"r5d.metal"|"r5dn.large"|"r5dn.xlarge"|"r5dn.2xlarge"|"r5dn.4xlarge"|"r5dn.8xlarge"|"r5dn.12xlarge"|"r5dn.16xlarge"|"r5dn.24xlarge"|"r5dn.metal"|"r5n.large"|"r5n.xlarge"|"r5n.2xlarge"|"r5n.4xlarge"|"r5n.8xlarge"|"r5n.12xlarge"|"r5n.16xlarge"|"r5n.24xlarge"|"r5n.metal"|"r6g.medium"|"r6g.large"|"r6g.xlarge"|"r6g.2xlarge"|"r6g.4xlarge"|"r6g.8xlarge"|"r6g.12xlarge"|"r6g.16xlarge"|"r6g.metal"|"r6gd.medium"|"r6gd.large"|"r6gd.xlarge"|"r6gd.2xlarge"|"r6gd.4xlarge"|"r6gd.8xlarge"|"r6gd.12xlarge"|"r6gd.16xlarge"|"r6gd.metal"|"r6i.large"|"r6i.xlarge"|"r6i.2xlarge"|"r6i.4xlarge"|"r6i.8xlarge"|"r6i.12xlarge"|"r6i.16xlarge"|"r6i.24xlarge"|"r6i.32xlarge"|"r6i.metal"|"t1.micro"|"t2.nano"|"t2.micro"|"t2.small"|"t2.medium"|"t2.large"|"t2.xlarge"|"t2.2xlarge"|"t3.nano"|"t3.micro"|"t3.small"|"t3.medium"|"t3.large"|"t3.xlarge"|"t3.2xlarge"|"t3a.nano"|"t3a.micro"|"t3a.small"|"t3a.medium"|"t3a.large"|"t3a.xlarge"|"t3a.2xlarge"|"t4g.nano"|"t4g.micro"|"t4g.small"|"t4g.medium"|"t4g.large"|"t4g.xlarge"|"t4g.2xlarge"|"u-6tb1.56xlarge"|"u-6tb1.112xlarge"|"u-9tb1.112xlarge"|"u-12tb1.112xlarge"|"u-6tb1.metal"|"u-9tb1.metal"|"u-12tb1.metal"|"u-18tb1.metal"|"u-24tb1.metal"|"vt1.3xlarge"|"vt1.6xlarge"|"vt1.24xlarge"|"x1.16xlarge"|"x1.32xlarge"|"x1e.xlarge"|"x1e.2xlarge"|"x1e.4xlarge"|"x1e.8xlarge"|"x1e.16xlarge"|"x1e.32xlarge"|"x2iezn.2xlarge"|"x2iezn.4xlarge"|"x2iezn.6xlarge"|"x2iezn.8xlarge"|"x2iezn.12xlarge"|"x2iezn.metal"|"x2gd.medium"|"x2gd.large"|"x2gd.xlarge"|"x2gd.2xlarge"|"x2gd.4xlarge"|"x2gd.8xlarge"|"x2gd.12xlarge"|"x2gd.16xlarge"|"x2gd.metal"|"z1d.large"|"z1d.xlarge"|"z1d.2xlarge"|"z1d.3xlarge"|"z1d.6xlarge"|"z1d.12xlarge"|"z1d.metal"|"x2idn.16xlarge"|"x2idn.24xlarge"|"x2idn.32xlarge"|"x2iedn.xlarge"|"x2iedn.2xlarge"|"x2iedn.4xlarge"|"x2iedn.8xlarge"|"x2iedn.16xlarge"|"x2iedn.24xlarge"|"x2iedn.32xlarge"|"c6a.large"|"c6a.xlarge"|"c6a.2xlarge"|"c6a.4xlarge"|"c6a.8xlarge"|"c6a.12xlarge"|"c6a.16xlarge"|"c6a.24xlarge"|"c6a.32xlarge"|"c6a.48xlarge"|"c6a.metal"|"m6a.metal"|"i4i.large"|"i4i.xlarge"|"i4i.2xlarge"|"i4i.4xlarge"|"i4i.8xlarge"|"i4i.16xlarge"|"i4i.32xlarge"|"i4i.metal"|"x2idn.metal"|"x2iedn.metal"|"c7g.medium"|"c7g.large"|"c7g.xlarge"|"c7g.2xlarge"|"c7g.4xlarge"|"c7g.8xlarge"|"c7g.12xlarge"|"c7g.16xlarge"|"mac2.metal"|"c6id.large"|"c6id.xlarge"|"c6id.2xlarge"|"c6id.4xlarge"|"c6id.8xlarge"|"c6id.12xlarge"|"c6id.16xlarge"|"c6id.24xlarge"|"c6id.32xlarge"|"c6id.metal"|"m6id.large"|"m6id.xlarge"|"m6id.2xlarge"|"m6id.4xlarge"|"m6id.8xlarge"|"m6id.12xlarge"|"m6id.16xlarge"|"m6id.24xlarge"|"m6id.32xlarge"|"m6id.metal"|"r6id.large"|"r6id.xlarge"|"r6id.2xlarge"|"r6id.4xlarge"|"r6id.8xlarge"|"r6id.12xlarge"|"r6id.16xlarge"|"r6id.24xlarge"|"r6id.32xlarge"|"r6id.metal"|"r6a.large"|"r6a.xlarge"|"r6a.2xlarge"|"r6a.4xlarge"|"r6a.8xlarge"|"r6a.12xlarge"|"r6a.16xlarge"|"r6a.24xlarge"|"r6a.32xlarge"|"r6a.48xlarge"|"r6a.metal"|"p4de.24xlarge"|"u-3tb1.56xlarge"|"u-18tb1.112xlarge"|"u-24tb1.112xlarge"|"trn1.2xlarge"|"trn1.32xlarge"|"hpc6id.32xlarge"|"c6in.large"|"c6in.xlarge"|"c6in.2xlarge"|"c6in.4xlarge"|"c6in.8xlarge"|"c6in.12xlarge"|"c6in.16xlarge"|"c6in.24xlarge"|"c6in.32xlarge"|"m6in.large"|"m6in.xlarge"|"m6in.2xlarge"|"m6in.4xlarge"|"m6in.8xlarge"|"m6in.12xlarge"|"m6in.16xlarge"|"m6in.24xlarge"|"m6in.32xlarge"|"m6idn.large"|"m6idn.xlarge"|"m6idn.2xlarge"|"m6idn.4xlarge"|"m6idn.8xlarge"|"m6idn.12xlarge"|"m6idn.16xlarge"|"m6idn.24xlarge"|"m6idn.32xlarge"|"r6in.large"|"r6in.xlarge"|"r6in.2xlarge"|"r6in.4xlarge"|"r6in.8xlarge"|"r6in.12xlarge"|"r6in.16xlarge"|"r6in.24xlarge"|"r6in.32xlarge"|"r6idn.large"|"r6idn.xlarge"|"r6idn.2xlarge"|"r6idn.4xlarge"|"r6idn.8xlarge"|"r6idn.12xlarge"|"r6idn.16xlarge"|"r6idn.24xlarge"|"r6idn.32xlarge"|"c7g.metal"|"m7g.medium"|"m7g.large"|"m7g.xlarge"|"m7g.2xlarge"|"m7g.4xlarge"|"m7g.8xlarge"|"m7g.12xlarge"|"m7g.16xlarge"|"m7g.metal"|"r7g.medium"|"r7g.large"|"r7g.xlarge"|"r7g.2xlarge"|"r7g.4xlarge"|"r7g.8xlarge"|"r7g.12xlarge"|"r7g.16xlarge"|"r7g.metal"|"c6in.metal"|"m6in.metal"|"m6idn.metal"|"r6in.metal"|"r6idn.metal"|"inf2.xlarge"|"inf2.8xlarge"|"inf2.24xlarge"|"inf2.48xlarge"|"trn1n.32xlarge"|"i4g.large"|"i4g.xlarge"|"i4g.2xlarge"|"i4g.4xlarge"|"i4g.8xlarge"|"i4g.16xlarge"|"hpc7g.4xlarge"|"hpc7g.8xlarge"|"hpc7g.16xlarge"|"c7gn.medium"|"c7gn.large"|"c7gn.xlarge"|"c7gn.2xlarge"|"c7gn.4xlarge"|"c7gn.8xlarge"|"c7gn.12xlarge"|"c7gn.16xlarge"|"p5.48xlarge"|"m7i.large"|"m7i.xlarge"|"m7i.2xlarge"|"m7i.4xlarge"|"m7i.8xlarge"|"m7i.12xlarge"|"m7i.16xlarge"|"m7i.24xlarge"|"m7i.48xlarge"|"m7i-flex.large"|"m7i-flex.xlarge"|"m7i-flex.2xlarge"|"m7i-flex.4xlarge"|"m7i-flex.8xlarge"|"m7a.medium"|"m7a.large"|"m7a.xlarge"|"m7a.2xlarge"|"m7a.4xlarge"|"m7a.8xlarge"|"m7a.12xlarge"|"m7a.16xlarge"|"m7a.24xlarge"|"m7a.32xlarge"|"m7a.48xlarge"|"m7a.metal-48xl"|"hpc7a.12xlarge"|"hpc7a.24xlarge"|"hpc7a.48xlarge"|"hpc7a.96xlarge"|"c7gd.medium"|"c7gd.large"|"c7gd.xlarge"|"c7gd.2xlarge"|"c7gd.4xlarge"|"c7gd.8xlarge"|"c7gd.12xlarge"|"c7gd.16xlarge"|"m7gd.medium"|"m7gd.large"|"m7gd.xlarge"|"m7gd.2xlarge"|"m7gd.4xlarge"|"m7gd.8xlarge"|"m7gd.12xlarge"|"m7gd.16xlarge"|"r7gd.medium"|"r7gd.large"|"r7gd.xlarge"|"r7gd.2xlarge"|"r7gd.4xlarge"|"r7gd.8xlarge"|"r7gd.12xlarge"|"r7gd.16xlarge"|"r7a.medium"|"r7a.large"|"r7a.xlarge"|"r7a.2xlarge"|"r7a.4xlarge"|"r7a.8xlarge"|"r7a.12xlarge"|"r7a.16xlarge"|"r7a.24xlarge"|"r7a.32xlarge"|"r7a.48xlarge"|"c7i.large"|"c7i.xlarge"|"c7i.2xlarge"|"c7i.4xlarge"|"c7i.8xlarge"|"c7i.12xlarge"|"c7i.16xlarge"|"c7i.24xlarge"|"c7i.48xlarge"|"mac2-m2pro.metal"|"r7iz.large"|"r7iz.xlarge"|"r7iz.2xlarge"|"r7iz.4xlarge"|"r7iz.8xlarge"|"r7iz.12xlarge"|"r7iz.16xlarge"|"r7iz.32xlarge"|"c7a.medium"|"c7a.large"|"c7a.xlarge"|"c7a.2xlarge"|"c7a.4xlarge"|"c7a.8xlarge"|"c7a.12xlarge"|"c7a.16xlarge"|"c7a.24xlarge"|"c7a.32xlarge"|"c7a.48xlarge"|"c7a.metal-48xl"|"r7a.metal-48xl"|"r7i.large"|"r7i.xlarge"|"r7i.2xlarge"|"r7i.4xlarge"|"r7i.8xlarge"|"r7i.12xlarge"|"r7i.16xlarge"|"r7i.24xlarge"|"r7i.48xlarge"|"dl2q.24xlarge"|"mac2-m2.metal"|"i4i.12xlarge"|"i4i.24xlarge"|"c7i.metal-24xl"|"c7i.metal-48xl"|"m7i.metal-24xl"|"m7i.metal-48xl"|"r7i.metal-24xl"|"r7i.metal-48xl"|"r7iz.metal-16xl"|"r7iz.metal-32xl"|"c7gd.metal"|"m7gd.metal"|"r7gd.metal"|"g6.xlarge"|"g6.2xlarge"|"g6.4xlarge"|"g6.8xlarge"|"g6.12xlarge"|"g6.16xlarge"|"g6.24xlarge"|"g6.48xlarge"|"gr6.4xlarge"|"gr6.8xlarge"|"c7i-flex.large"|"c7i-flex.xlarge"|"c7i-flex.2xlarge"|"c7i-flex.4xlarge"|"c7i-flex.8xlarge"|"u7i-12tb.224xlarge"|"u7in-16tb.224xlarge"|"u7in-24tb.224xlarge"|"u7in-32tb.224xlarge"|"u7ib-12tb.224xlarge"|"c7gn.metal"|"r8g.medium"|"r8g.large"|"r8g.xlarge"|"r8g.2xlarge"|"r8g.4xlarge"|"r8g.8xlarge"|"r8g.12xlarge"|"r8g.16xlarge"|"r8g.24xlarge"|"r8g.48xlarge"|"r8g.metal-24xl"|"r8g.metal-48xl"|"mac2-m1ultra.metal"|"g6e.xlarge"|"g6e.2xlarge"|"g6e.4xlarge"|"g6e.8xlarge"|"g6e.12xlarge"|"g6e.16xlarge"|"g6e.24xlarge"|"g6e.48xlarge"|"c8g.medium"|"c8g.large"|"c8g.xlarge"|"c8g.2xlarge"|"c8g.4xlarge"|"c8g.8xlarge"|"c8g.12xlarge"|"c8g.16xlarge"|"c8g.24xlarge"|"c8g.48xlarge"|"c8g.metal-24xl"|"c8g.metal-48xl"|"m8g.medium"|"m8g.large"|"m8g.xlarge"|"m8g.2xlarge"|"m8g.4xlarge"|"m8g.8xlarge"|"m8g.12xlarge"|"m8g.16xlarge"|"m8g.24xlarge"|"m8g.48xlarge"|"m8g.metal-24xl"|"m8g.metal-48xl"|"x8g.medium"|"x8g.large"|"x8g.xlarge"|"x8g.2xlarge"|"x8g.4xlarge"|"x8g.8xlarge"|"x8g.12xlarge"|"x8g.16xlarge"|"x8g.24xlarge"|"x8g.48xlarge"|"x8g.metal-24xl"|"x8g.metal-48xl"|"i7ie.large"|"i7ie.xlarge"|"i7ie.2xlarge"|"i7ie.3xlarge"|"i7ie.6xlarge"|"i7ie.12xlarge"|"i7ie.18xlarge"|"i7ie.24xlarge"|"i7ie.48xlarge"|"i8g.large"|"i8g.xlarge"|"i8g.2xlarge"|"i8g.4xlarge"|"i8g.8xlarge"|"i8g.12xlarge"|"i8g.16xlarge"|"i8g.24xlarge"|"i8g.metal-24xl"|"u7i-6tb.112xlarge"|"u7i-8tb.112xlarge"|"u7inh-32tb.480xlarge"|"p5e.48xlarge"|"p5en.48xlarge"|"f2.12xlarge"|"f2.48xlarge"|"trn2.48xlarge",
        "MaxPrice": "string",
        "SubnetId": "string",
        "AvailabilityZone": "string",
        "WeightedCapacity": double,
        "Priority": double,
        "Placement": {
          "Affinity": "string",
          "GroupName": "string",
          "PartitionNumber": integer,
          "HostId": "string",
          "Tenancy": "default"|"dedicated"|"host",
          "SpreadDomain": "string",
          "HostResourceGroupArn": "string",
          "GroupId": "string",
          "AvailabilityZone": "string"
        },
        "BlockDeviceMappings": [
          {
            "DeviceName": "string",
            "VirtualName": "string",
            "Ebs": {
              "Encrypted": true|false,
              "DeleteOnTermination": true|false,
              "Iops": integer,
              "Throughput": integer,
              "KmsKeyId": "string",
              "SnapshotId": "string",
              "VolumeSize": integer,
              "VolumeType": "standard"|"io1"|"io2"|"gp2"|"sc1"|"st1"|"gp3"
            },
            "NoDevice": "string"
          }
          ...
        ],
        "InstanceRequirements": {
          "VCpuCount": {
            "Min": integer,
            "Max": integer
          },
          "MemoryMiB": {
            "Min": integer,
            "Max": integer
          },
          "CpuManufacturers": ["intel"|"amd"|"amazon-web-services"|"apple", ...],
          "MemoryGiBPerVCpu": {
            "Min": double,
            "Max": double
          },
          "ExcludedInstanceTypes": ["string", ...],
          "InstanceGenerations": ["current"|"previous", ...],
          "SpotMaxPricePercentageOverLowestPrice": integer,
          "OnDemandMaxPricePercentageOverLowestPrice": integer,
          "BareMetal": "included"|"required"|"excluded",
          "BurstablePerformance": "included"|"required"|"excluded",
          "RequireHibernateSupport": true|false,
          "NetworkInterfaceCount": {
            "Min": integer,
            "Max": integer
          },
          "LocalStorage": "included"|"required"|"excluded",
          "LocalStorageTypes": ["hdd"|"ssd", ...],
          "TotalLocalStorageGB": {
            "Min": double,
            "Max": double
          },
          "BaselineEbsBandwidthMbps": {
            "Min": integer,
            "Max": integer
          },
          "AcceleratorTypes": ["gpu"|"fpga"|"inference", ...],
          "AcceleratorCount": {
            "Min": integer,
            "Max": integer
          },
          "AcceleratorManufacturers": ["amazon-web-services"|"amd"|"nvidia"|"xilinx"|"habana", ...],
          "AcceleratorNames": ["a100"|"inferentia"|"k520"|"k80"|"m60"|"radeon-pro-v520"|"t4"|"vu9p"|"v100"|"a10g"|"h100"|"t4g", ...],
          "AcceleratorTotalMemoryMiB": {
            "Min": integer,
            "Max": integer
          },
          "NetworkBandwidthGbps": {
            "Min": double,
            "Max": double
          },
          "AllowedInstanceTypes": ["string", ...],
          "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice": integer,
          "BaselinePerformanceFactors": {
            "Cpu": {
              "References": [
                {
                  "InstanceFamily": "string"
                }
                ...
              ]
            }
          }
        },
        "ImageId": "string"
      }
      ...
    ]
  }
  ...
]
```

`--target-capacity-specification` (structure)

The number of units to request.

TotalTargetCapacity -> (integer)

The number of units to request, filled using the default target capacity type.

OnDemandTargetCapacity -> (integer)

The number of On-Demand units to request.

SpotTargetCapacity -> (integer)

The number of Spot units to request.

DefaultTargetCapacityType -> (string)

The default target capacity type.

TargetCapacityUnitType -> (string)

The unit for the target capacity. You can specify this parameter only when using attributed-based instance type selection.

Default: `units` (the number of instances)

Shorthand Syntax:

```
TotalTargetCapacity=integer,OnDemandTargetCapacity=integer,SpotTargetCapacity=integer,DefaultTargetCapacityType=string,TargetCapacityUnitType=string
```

JSON Syntax:

```
{
  "TotalTargetCapacity": integer,
  "OnDemandTargetCapacity": integer,
  "SpotTargetCapacity": integer,
  "DefaultTargetCapacityType": "spot"|"on-demand"|"capacity-block",
  "TargetCapacityUnitType": "vcpu"|"memory-mib"|"units"
}
```

`--terminate-instances-with-expiration` | `--no-terminate-instances-with-expiration` (boolean)

Indicates whether running instances should be terminated when the EC2 Fleet expires.

`--type` (string)

The fleet type. The default value is `maintain` .

- `maintain` - The EC2 Fleet places an asynchronous request for your desired capacity, and continues to maintain your desired Spot capacity by replenishing interrupted Spot Instances.
- `request` - The EC2 Fleet places an asynchronous one-time request for your desired capacity, but does submit Spot requests in alternative capacity pools if Spot capacity is unavailable, and does not maintain Spot capacity if Spot Instances are interrupted.
- `instant` - The EC2 Fleet places a synchronous one-time request for your desired capacity, and returns errors for any instances that could not be launched.

For more information, see [EC2 Fleet request types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-request-type.html) in the *Amazon EC2 User Guide* .

Possible values:

- `request`
- `maintain`
- `instant`

`--valid-from` (timestamp)

The start date and time of the request, in UTC format (for example, *YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z). The default is to start fulfilling the request immediately.

`--valid-until` (timestamp)

The end date and time of the request, in UTC format (for example, *YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z). At this point, no new EC2 Fleet requests are placed or able to fulfill the request. If no value is specified, the request remains until you cancel it.

`--replace-unhealthy-instances` | `--no-replace-unhealthy-instances` (boolean)

Indicates whether EC2 Fleet should replace unhealthy Spot Instances. Supported only for fleets of type `maintain` . For more information, see [EC2 Fleet health checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html#ec2-fleet-health-checks) in the *Amazon EC2 User Guide* .

`--tag-specifications` (list)

The key-value pair for tagging the EC2 Fleet request on creation. For more information, see [Tag your resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-resources) .

If the fleet type is `instant` , specify a resource type of `fleet` to tag the fleet or `instance` to tag the instances at launch.

If the fleet type is `maintain` or `request` , specify a resource type of `fleet` to tag the fleet. You cannot specify a resource type of `instance` . To tag instances at launch, specify the tags in a [launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#create-launch-template) .

(structure)

The tags to apply to a resource when the resource is being created. When you specify a tag, you must specify the resource type to tag, otherwise the request will fail.

### Note

The `Valid Values` lists all the resource types that can be tagged. However, the action youâre using might not support tagging all of these resource types. If you try to tag a resource type that is unsupported for the action youâre using, youâll get an error.

ResourceType -> (string)

The type of resource to tag on creation.

Tags -> (list)

The tags to apply to the resource.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

Shorthand Syntax:

```
ResourceType=string,Tags=[{Key=string,Value=string},{Key=string,Value=string}] ...
```

JSON Syntax:

```
[
  {
    "ResourceType": "capacity-reservation"|"client-vpn-endpoint"|"customer-gateway"|"carrier-gateway"|"coip-pool"|"declarative-policies-report"|"dedicated-host"|"dhcp-options"|"egress-only-internet-gateway"|"elastic-ip"|"elastic-gpu"|"export-image-task"|"export-instance-task"|"fleet"|"fpga-image"|"host-reservation"|"image"|"import-image-task"|"import-snapshot-task"|"instance"|"instance-event-window"|"internet-gateway"|"ipam"|"ipam-pool"|"ipam-scope"|"ipv4pool-ec2"|"ipv6pool-ec2"|"key-pair"|"launch-template"|"local-gateway"|"local-gateway-route-table"|"local-gateway-virtual-interface"|"local-gateway-virtual-interface-group"|"local-gateway-route-table-vpc-association"|"local-gateway-route-table-virtual-interface-group-association"|"natgateway"|"network-acl"|"network-interface"|"network-insights-analysis"|"network-insights-path"|"network-insights-access-scope"|"network-insights-access-scope-analysis"|"outpost-lag"|"placement-group"|"prefix-list"|"replace-root-volume-task"|"reserved-instances"|"route-table"|"security-group"|"security-group-rule"|"service-link-virtual-interface"|"snapshot"|"spot-fleet-request"|"spot-instances-request"|"subnet"|"subnet-cidr-reservation"|"traffic-mirror-filter"|"traffic-mirror-session"|"traffic-mirror-target"|"transit-gateway"|"transit-gateway-attachment"|"transit-gateway-connect-peer"|"transit-gateway-multicast-domain"|"transit-gateway-policy-table"|"transit-gateway-route-table"|"transit-gateway-route-table-announcement"|"volume"|"vpc"|"vpc-endpoint"|"vpc-endpoint-connection"|"vpc-endpoint-service"|"vpc-endpoint-service-permission"|"vpc-peering-connection"|"vpn-connection"|"vpn-gateway"|"vpc-flow-log"|"capacity-reservation-fleet"|"traffic-mirror-filter-rule"|"vpc-endpoint-connection-device-type"|"verified-access-instance"|"verified-access-group"|"verified-access-endpoint"|"verified-access-policy"|"verified-access-trust-provider"|"vpn-connection-device-type"|"vpc-block-public-access-exclusion"|"route-server"|"route-server-endpoint"|"route-server-peer"|"ipam-resource-discovery"|"ipam-resource-discovery-association"|"instance-connect-endpoint"|"verified-access-endpoint-target"|"ipam-external-resource-verification-token"|"mac-modification-task",
    "Tags": [
      {
        "Key": "string",
        "Value": "string"
      }
      ...
    ]
  }
  ...
]
```

`--context` (string)

Reserved.

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

**Example 1: To create an EC2 Fleet that launches Spot Instances as the default purchasing model**

The following `create-fleet` example creates an EC2 Fleet using the minimum parameters required to launch a fleet: a launch template, target capacity, and default purchasing model. The launch template is identified by its launch template ID and version number. The target capacity for the fleet is 2 instances, and the default purchasing model is `spot`, which results in the fleet launching 2 Spot Instances.

When you create an EC2 Fleet, use a JSON file to specify information about the instances to launch.

```
aws ec2 create-fleet \
    --cli-input-json file://file_name.json
```

Contents of file_name.json:

```
{
    "LaunchTemplateConfigs": [
    {
        "LaunchTemplateSpecification": {
        "LaunchTemplateId": "lt-0e8c754449b27161c",
        "Version": "1"
        }
    }
    ],
    "TargetCapacitySpecification": {
        "TotalTargetCapacity": 2,
        "DefaultTargetCapacityType": "spot"
    }
}
```

Output:

```
{
    "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE"
}
```

**Example 2: To create an EC2 Fleet that launches On-Demand Instances as the default purchasing model**

The following `create-fleet` example creates an EC2 Fleet using the minimum parameters required to launch a fleet: a launch template, target capacity, and default purchasing model. The launch template is identified by its launch template ID and version number. The target capacity for the fleet is 2 instances, and the default purchasing model is `on-demand`, which results in the fleet launching 2 On-Demand Instances.

When you create an EC2 Fleet, use a JSON file to specify information about the instances to launch.

```
aws ec2 create-fleet \
    --cli-input-json file://file_name.json
```

Contents of file_name.json:

```
{
    "LaunchTemplateConfigs": [
    {
        "LaunchTemplateSpecification": {
        "LaunchTemplateId": "lt-0e8c754449b27161c",
        "Version": "1"
        }
    }
    ],
    "TargetCapacitySpecification": {
    "TotalTargetCapacity": 2,
    "DefaultTargetCapacityType": "on-demand"
    }
}
```

Output:

```
{
    "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE"
}
```

**Example 3: To create an EC2 Fleet that launches On-Demand Instances as the primary capacity**

The following `create-fleet` example creates an EC2 Fleet that specifies the total target capacity of 2 instances for the fleet, and a target capacity of 1 On-Demand Instance. The default purchasing model is `spot`. The fleet launches 1 On-Demand Instance as specified, but needs to launch one more instance to fulfil the total target capacity. The purchasing model for the difference is calculated as `TotalTargetCapacity` - `OnDemandTargetCapacity` = `DefaultTargetCapacityType`, which results in the fleet launching 1 Spot Instance.

When you create an EC2 Fleet, use a JSON file to specify information about the instances to launch.

```
aws ec2 create-fleet \
    --cli-input-json file://file_name.json
```

Contents of file_name.json:

```
{
    "LaunchTemplateConfigs": [
    {
        "LaunchTemplateSpecification": {
        "LaunchTemplateId": "lt-0e8c754449b27161c",
        "Version": "1"
        }
    }
    ],
    "TargetCapacitySpecification": {
        "TotalTargetCapacity": 2,
        "OnDemandTargetCapacity":1,
        "DefaultTargetCapacityType": "spot"
    }
}
```

Output:

```
{
    "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE"
}
```

**Example 4: To create an EC2 Fleet that launches Spot Instances using the lowest-price allocation strategy**

If the allocation strategy for Spot Instances is not specified, the default allocation strategy, which is `lowest-price`, is used. The following `create-fleet` example creates an EC2 Fleet using the `lowest-price` allocation strategy. The three launch specifications, which override the launch template, have different instance types but the same weighted capacity and subnet. The total target capacity is 2 instances and the default purchasing model is `spot`. The EC2 Fleet launches 2 Spot Instances using the instance type of the launch specification with the lowest price.

When you create an EC2 Fleet, use a JSON file to specify information about the instances to launch.

```
aws ec2 create-fleet \
    --cli-input-json file://file_name.jsonContents of file_name.json::

{
    "LaunchTemplateConfigs": [
    {
        "LaunchTemplateSpecification": {
        "LaunchTemplateId": "lt-0e8c754449b27161c",
        "Version": "1"
        },
        "Overrides": [
            {
                "InstanceType": "c4.large",
                "WeightedCapacity": 1,
                "SubnetId": "subnet-a4f6c5d3"
            },
            {
                "InstanceType": "c3.large",
                "WeightedCapacity": 1,
                "SubnetId": "subnet-a4f6c5d3"
            },
            {
                "InstanceType": "c5.large",
                "WeightedCapacity": 1,
                "SubnetId": "subnet-a4f6c5d3"
            }
        ]
    }
    ],
    "TargetCapacitySpecification": {
        "TotalTargetCapacity": 2,
        "DefaultTargetCapacityType": "spot"
    }
}
```

Output:

```
{
    "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE"
}
```

## Output

FleetId -> (string)

The ID of the EC2 Fleet.

Errors -> (list)

Information about the instances that could not be launched by the fleet. Supported only for fleets of type `instant` .

(structure)

Describes the instances that could not be launched by the fleet.

LaunchTemplateAndOverrides -> (structure)

The launch templates and overrides that were used for launching the instances. The values that you specify in the Overrides replace the values in the launch template.

LaunchTemplateSpecification -> (structure)

The launch template.

LaunchTemplateId -> (string)

The ID of the launch template.

You must specify the `LaunchTemplateId` or the `LaunchTemplateName` , but not both.

LaunchTemplateName -> (string)

The name of the launch template.

You must specify the `LaunchTemplateName` or the `LaunchTemplateId` , but not both.

Version -> (string)

The launch template version number, `$Latest` , or `$Default` . You must specify a value, otherwise the request fails.

If the value is `$Latest` , Amazon EC2 uses the latest version of the launch template.

If the value is `$Default` , Amazon EC2 uses the default version of the launch template.

Overrides -> (structure)

Any parameters that you specify override the same parameters in the launch template.

InstanceType -> (string)

The instance type.

`mac1.metal` is not supported as a launch template override.

### Note

If you specify `InstanceType` , you canât specify `InstanceRequirements` .

MaxPrice -> (string)

The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.

### Warning

If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.

If you specify a maximum price, it must be more than USD $0.001. Specifying a value below USD $0.001 will result in an `InvalidParameterValue` error message.

SubnetId -> (string)

The ID of the subnet in which to launch the instances.

AvailabilityZone -> (string)

The Availability Zone in which to launch the instances.

WeightedCapacity -> (double)

The number of units provided by the specified instance type. These are the same units that you chose to set the target capacity in terms of instances, or a performance characteristic such as vCPUs, memory, or I/O.

If the target capacity divided by this value is not a whole number, Amazon EC2 rounds the number of instances to the next whole number. If this value is not specified, the default is 1.

### Note

When specifying weights, the price used in the `lowest-price` and `price-capacity-optimized` allocation strategies is per *unit* hour (where the instance price is divided by the specified weight). However, if all the specified weights are above the requested `TargetCapacity` , resulting in only 1 instance being launched, the price used is per *instance* hour.

Priority -> (double)

The priority for the launch template override. The highest priority is launched first.

If the On-Demand `AllocationStrategy` is set to `prioritized` , EC2 Fleet uses priority to determine which launch template override to use first in fulfilling On-Demand capacity.

If the Spot `AllocationStrategy` is set to `capacity-optimized-prioritized` , EC2 Fleet uses priority on a best-effort basis to determine which launch template override to use in fulfilling Spot capacity, but optimizes for capacity first.

Valid values are whole numbers starting at `0` . The lower the number, the higher the priority. If no number is set, the override has the lowest priority. You can set the same priority for different launch template overrides.

Placement -> (structure)

The location where the instance launched, if applicable.

GroupName -> (string)

The name of the placement group that the instance is in.

InstanceRequirements -> (structure)

The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with those attributes.

### Note

If you specify `InstanceRequirements` , you canât specify `InstanceType` .

VCpuCount -> (structure)

The minimum and maximum number of vCPUs.

Min -> (integer)

The minimum number of vCPUs. If the value is `0` , there is no minimum limit.

Max -> (integer)

The maximum number of vCPUs. If this parameter is not specified, there is no maximum limit.

MemoryMiB -> (structure)

The minimum and maximum amount of memory, in MiB.

Min -> (integer)

The minimum amount of memory, in MiB. If this parameter is not specified, there is no minimum limit.

Max -> (integer)

The maximum amount of memory, in MiB. If this parameter is not specified, there is no maximum limit.

CpuManufacturers -> (list)

The CPU manufacturers to include.

- For instance types with Intel CPUs, specify `intel` .
- For instance types with AMD CPUs, specify `amd` .
- For instance types with Amazon Web Services CPUs, specify `amazon-web-services` .
- For instance types with Apple CPUs, specify `apple` .

### Note

Donât confuse the CPU manufacturer with the CPU architecture. Instances will be launched with a compatible CPU architecture based on the Amazon Machine Image (AMI) that you specify in your launch template.

Default: Any manufacturer

(string)

MemoryGiBPerVCpu -> (structure)

The minimum and maximum amount of memory per vCPU, in GiB.

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of memory per vCPU, in GiB. If this parameter is not specified, there is no minimum limit.

Max -> (double)

The maximum amount of memory per vCPU, in GiB. If this parameter is not specified, there is no maximum limit.

ExcludedInstanceTypes -> (list)

The instance types to exclude.

You can use strings with one or more wild cards, represented by an asterisk (`*` ), to exclude an instance type, size, or generation. The following are examples: `m5.8xlarge` , `c5*.*` , `m5a.*` , `r*` , `*3*` .

For example, if you specify `c5*` ,Amazon EC2 will exclude the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*` , Amazon EC2 will exclude all the M5a instance types, but not the M5n instance types.

### Note

If you specify `ExcludedInstanceTypes` , you canât specify `AllowedInstanceTypes` .

Default: No excluded instance types

(string)

InstanceGenerations -> (list)

Indicates whether current or previous generation instance types are included. The current generation instance types are recommended for use. Current generation instance types are typically the latest two to three generations in each instance family. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide* .

For current generation instance types, specify `current` .

For previous generation instance types, specify `previous` .

Default: Current and previous generation instance types

(string)

SpotMaxPricePercentageOverLowestPrice -> (integer)

[Price protection] The price protection threshold for Spot Instances, as a percentage higher than an identified Spot price. The identified Spot price is the Spot price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified Spot price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose Spot price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 interprets as a percentage.

If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib` , the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.

This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) and [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html) .

### Note

Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you donât specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999` .

Default: `100`

OnDemandMaxPricePercentageOverLowestPrice -> (integer)

[Price protection] The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 interprets as a percentage.

To turn off price protection, specify a high value, such as `999999` .

This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) and [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html) .

### Note

If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib` , the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.

Default: `20`

BareMetal -> (string)

Indicates whether bare metal instance types must be included, excluded, or required.

- To include bare metal instance types, specify `included` .
- To require only bare metal instance types, specify `required` .
- To exclude bare metal instance types, specify `excluded` .

Default: `excluded`

BurstablePerformance -> (string)

Indicates whether burstable performance T instance types are included, excluded, or required. For more information, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) .

- To include burstable performance instance types, specify `included` .
- To require only burstable performance instance types, specify `required` .
- To exclude burstable performance instance types, specify `excluded` .

Default: `excluded`

RequireHibernateSupport -> (boolean)

Indicates whether instance types must support hibernation for On-Demand Instances.

This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) .

Default: `false`

NetworkInterfaceCount -> (structure)

The minimum and maximum number of network interfaces.

Default: No minimum or maximum limits

Min -> (integer)

The minimum number of network interfaces. If this parameter is not specified, there is no minimum limit.

Max -> (integer)

The maximum number of network interfaces. If this parameter is not specified, there is no maximum limit.

LocalStorage -> (string)

Indicates whether instance types with instance store volumes are included, excluded, or required. For more information, [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) in the *Amazon EC2 User Guide* .

- To include instance types with instance store volumes, specify `included` .
- To require only instance types with instance store volumes, specify `required` .
- To exclude instance types with instance store volumes, specify `excluded` .

Default: `included`

LocalStorageTypes -> (list)

The type of local storage that is required.

- For instance types with hard disk drive (HDD) storage, specify `hdd` .
- For instance types with solid state drive (SSD) storage, specify `ssd` .

Default: `hdd` and `ssd`

(string)

TotalLocalStorageGB -> (structure)

The minimum and maximum amount of total local storage, in GB.

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of total local storage, in GB. If this parameter is not specified, there is no minimum limit.

Max -> (double)

The maximum amount of total local storage, in GB. If this parameter is not specified, there is no maximum limit.

BaselineEbsBandwidthMbps -> (structure)

The minimum and maximum baseline bandwidth to Amazon EBS, in Mbps. For more information, see [Amazon EBSâoptimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) in the *Amazon EC2 User Guide* .

Default: No minimum or maximum limits

Min -> (integer)

The minimum baseline bandwidth, in Mbps. If this parameter is not specified, there is no minimum limit.

Max -> (integer)

The maximum baseline bandwidth, in Mbps. If this parameter is not specified, there is no maximum limit.

AcceleratorTypes -> (list)

The accelerator types that must be on the instance type.

- For instance types with FPGA accelerators, specify `fpga` .
- For instance types with GPU accelerators, specify `gpu` .
- For instance types with Inference accelerators, specify `inference` .

Default: Any accelerator type

(string)

AcceleratorCount -> (structure)

The minimum and maximum number of accelerators (GPUs, FPGAs, or Amazon Web Services Inferentia chips) on an instance.

To exclude accelerator-enabled instance types, set `Max` to `0` .

Default: No minimum or maximum limits

Min -> (integer)

The minimum number of accelerators. If this parameter is not specified, there is no minimum limit.

Max -> (integer)

The maximum number of accelerators. If this parameter is not specified, there is no maximum limit.

AcceleratorManufacturers -> (list)

Indicates whether instance types must have accelerators by specific manufacturers.

- For instance types with Amazon Web Services devices, specify `amazon-web-services` .
- For instance types with AMD devices, specify `amd` .
- For instance types with Habana devices, specify `habana` .
- For instance types with NVIDIA devices, specify `nvidia` .
- For instance types with Xilinx devices, specify `xilinx` .

Default: Any manufacturer

(string)

AcceleratorNames -> (list)

The accelerators that must be on the instance type.

- For instance types with NVIDIA A10G GPUs, specify `a10g` .
- For instance types with NVIDIA A100 GPUs, specify `a100` .
- For instance types with NVIDIA H100 GPUs, specify `h100` .
- For instance types with Amazon Web Services Inferentia chips, specify `inferentia` .
- For instance types with NVIDIA GRID K520 GPUs, specify `k520` .
- For instance types with NVIDIA K80 GPUs, specify `k80` .
- For instance types with NVIDIA M60 GPUs, specify `m60` .
- For instance types with AMD Radeon Pro V520 GPUs, specify `radeon-pro-v520` .
- For instance types with NVIDIA T4 GPUs, specify `t4` .
- For instance types with NVIDIA T4G GPUs, specify `t4g` .
- For instance types with Xilinx VU9P FPGAs, specify `vu9p` .
- For instance types with NVIDIA V100 GPUs, specify `v100` .

Default: Any accelerator

(string)

AcceleratorTotalMemoryMiB -> (structure)

The minimum and maximum amount of total accelerator memory, in MiB.

Default: No minimum or maximum limits

Min -> (integer)

The minimum amount of accelerator memory, in MiB. If this parameter is not specified, there is no minimum limit.

Max -> (integer)

The maximum amount of accelerator memory, in MiB. If this parameter is not specified, there is no maximum limit.

NetworkBandwidthGbps -> (structure)

The minimum and maximum amount of network bandwidth, in gigabits per second (Gbps).

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of network bandwidth, in Gbps. If this parameter is not specified, there is no minimum limit.

Max -> (double)

The maximum amount of network bandwidth, in Gbps. If this parameter is not specified, there is no maximum limit.

AllowedInstanceTypes -> (list)

The instance types to apply your specified attributes against. All other instance types are ignored, even if they match your specified attributes.

You can use strings with one or more wild cards, represented by an asterisk (`*` ), to allow an instance type, size, or generation. The following are examples: `m5.8xlarge` , `c5*.*` , `m5a.*` , `r*` , `*3*` .

For example, if you specify `c5*` ,Amazon EC2 will allow the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*` , Amazon EC2 will allow all the M5a instance types, but not the M5n instance types.

### Note

If you specify `AllowedInstanceTypes` , you canât specify `ExcludedInstanceTypes` .

Default: All instance types

(string)

MaxSpotPriceAsPercentageOfOptimalOnDemandPrice -> (integer)

[Price protection] The price protection threshold for Spot Instances, as a percentage of an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 interprets as a percentage.

If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib` , the price protection threshold is based on the per vCPU or per memory price instead of the per instance price.

### Note

Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you donât specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999` .

BaselinePerformanceFactors -> (structure)

The baseline performance to consider, using an instance family as a baseline reference. The instance family establishes the lowest acceptable level of performance. Amazon EC2 uses this baseline to guide instance type selection, but there is no guarantee that the selected instance types will always exceed the baseline for every application. Currently, this parameter only supports CPU performance as a baseline performance factor. For more information, see [Performance protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html#ec2fleet-abis-performance-protection) in the *Amazon EC2 User Guide* .

Cpu -> (structure)

The CPU performance to consider, using an instance family as the baseline reference.

References -> (list)

Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture differences.

### Note

Currently, only one instance family can be specified in the list.

(structure)

Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture.

### Note

Currently, only one instance family can be specified in the list.

InstanceFamily -> (string)

The instance family to use as a baseline reference.

### Note

Ensure that you specify the correct value for the instance family. The instance family is everything before the period (`.` ) in the instance type name. For example, in the instance type `c6i.large` , the instance family is `c6i` , not `c6` . For more information, see [Amazon EC2 instance type naming conventions](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html) in *Amazon EC2 Instance Types* .

The following instance families are *not supported* for performance protection:

- `c1`
- `g3` | `g3s`
- `hpc7g`
- `m1` | `m2`
- `mac1` | `mac2` | `mac2-m1ultra` | `mac2-m2` | `mac2-m2pro`
- `p3dn` | `p4d` | `p5`
- `t1`
- `u-12tb1` | `u-18tb1` | `u-24tb1` | `u-3tb1` | `u-6tb1` | `u-9tb1` | `u7i-12tb` | `u7in-16tb` | `u7in-24tb` | `u7in-32tb`

If you enable performance protection by specifying a supported instance family, the returned instance types will exclude the above unsupported instance families.

If you specify an unsupported instance family as a value for baseline performance, the API returns an empty response for [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements) and an exception for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) , [RequestSpotFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet) , [ModifyFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyFleet) , and [ModifySpotFleetRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySpotFleetRequest) .

ImageId -> (string)

The ID of the AMI in the format `ami-17characters00000` .

Alternatively, you can specify a Systems Manager parameter, using one of the following formats. The Systems Manager parameter will resolve to an AMI ID on launch.

To reference a public parameter:

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id15)resolve:ssm:*public-parameter* ``

To reference a parameter stored in the same account:

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id17)resolve:ssm:*parameter-name* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id19)resolve:ssm:*parameter-name:version-number* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id21)resolve:ssm:*parameter-name:label* ``

To reference a parameter shared from another Amazon Web Services account:

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id23)resolve:ssm:*parameter-ARN* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id25)resolve:ssm:*parameter-ARN:version-number* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id27)resolve:ssm:*parameter-ARN:label* ``

For more information, see [Use a Systems Manager parameter instead of an AMI ID](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#use-an-ssm-parameter-instead-of-an-ami-id) in the *Amazon EC2 User Guide* .

### Note

This parameter is only available for fleets of type `instant` . For fleets of type `maintain` and `request` , you must specify the AMI ID in the launch template.

BlockDeviceMappings -> (list)

The block device mappings, which define the EBS volumes and instance store volumes to attach to the instance at launch.

Supported only for fleets of type `instant` .

For more information, see [Block device mappings for volumes on Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html) in the *Amazon EC2 User Guide* .

(structure)

Describes a block device mapping, which defines the EBS volumes and instance store volumes to attach to an instance at launch.

DeviceName -> (string)

The device name (for example, `/dev/sdh` or `xvdh` ).

VirtualName -> (string)

The virtual device name.

Ebs -> (structure)

Parameters used to automatically set up EBS volumes when the instance is launched.

Encrypted -> (boolean)

Indicates whether the volume is encrypted.

DeleteOnTermination -> (boolean)

Indicates whether the volume is deleted on instance termination.

Iops -> (integer)

The number of I/O operations per second (IOPS). For `gp3` , `io1` , and `io2` volumes, this represents the number of IOPS that are provisioned for the volume. For `gp2` volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.

Throughput -> (integer)

The throughput that the volume supports, in MiB/s.

KmsKeyId -> (string)

Identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed KMS key to use for EBS encryption.

SnapshotId -> (string)

The ID of the snapshot.

VolumeSize -> (integer)

The size of the volume, in GiBs.

VolumeType -> (string)

The volume type. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) in the *Amazon EBS User Guide* .

NoDevice -> (string)

Suppresses the specified device included in the block device mapping.

Lifecycle -> (string)

Indicates if the instance that could not be launched was a Spot Instance or On-Demand Instance.

ErrorCode -> (string)

The error code that indicates why the instance could not be launched. For more information about error codes, see [Error codes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html) .

ErrorMessage -> (string)

The error message that describes why the instance could not be launched. For more information about error messages, see [Error codes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html) .

Instances -> (list)

Information about the instances that were launched by the fleet. Supported only for fleets of type `instant` .

(structure)

Describes the instances that were launched by the fleet.

LaunchTemplateAndOverrides -> (structure)

The launch templates and overrides that were used for launching the instances. The values that you specify in the Overrides replace the values in the launch template.

LaunchTemplateSpecification -> (structure)

The launch template.

LaunchTemplateId -> (string)

The ID of the launch template.

You must specify the `LaunchTemplateId` or the `LaunchTemplateName` , but not both.

LaunchTemplateName -> (string)

The name of the launch template.

You must specify the `LaunchTemplateName` or the `LaunchTemplateId` , but not both.

Version -> (string)

The launch template version number, `$Latest` , or `$Default` . You must specify a value, otherwise the request fails.

If the value is `$Latest` , Amazon EC2 uses the latest version of the launch template.

If the value is `$Default` , Amazon EC2 uses the default version of the launch template.

Overrides -> (structure)

Any parameters that you specify override the same parameters in the launch template.

InstanceType -> (string)

The instance type.

`mac1.metal` is not supported as a launch template override.

### Note

If you specify `InstanceType` , you canât specify `InstanceRequirements` .

MaxPrice -> (string)

The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.

### Warning

If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.

If you specify a maximum price, it must be more than USD $0.001. Specifying a value below USD $0.001 will result in an `InvalidParameterValue` error message.

SubnetId -> (string)

The ID of the subnet in which to launch the instances.

AvailabilityZone -> (string)

The Availability Zone in which to launch the instances.

WeightedCapacity -> (double)

The number of units provided by the specified instance type. These are the same units that you chose to set the target capacity in terms of instances, or a performance characteristic such as vCPUs, memory, or I/O.

If the target capacity divided by this value is not a whole number, Amazon EC2 rounds the number of instances to the next whole number. If this value is not specified, the default is 1.

### Note

When specifying weights, the price used in the `lowest-price` and `price-capacity-optimized` allocation strategies is per *unit* hour (where the instance price is divided by the specified weight). However, if all the specified weights are above the requested `TargetCapacity` , resulting in only 1 instance being launched, the price used is per *instance* hour.

Priority -> (double)

The priority for the launch template override. The highest priority is launched first.

If the On-Demand `AllocationStrategy` is set to `prioritized` , EC2 Fleet uses priority to determine which launch template override to use first in fulfilling On-Demand capacity.

If the Spot `AllocationStrategy` is set to `capacity-optimized-prioritized` , EC2 Fleet uses priority on a best-effort basis to determine which launch template override to use in fulfilling Spot capacity, but optimizes for capacity first.

Valid values are whole numbers starting at `0` . The lower the number, the higher the priority. If no number is set, the override has the lowest priority. You can set the same priority for different launch template overrides.

Placement -> (structure)

The location where the instance launched, if applicable.

GroupName -> (string)

The name of the placement group that the instance is in.

InstanceRequirements -> (structure)

The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with those attributes.

### Note

If you specify `InstanceRequirements` , you canât specify `InstanceType` .

VCpuCount -> (structure)

The minimum and maximum number of vCPUs.

Min -> (integer)

The minimum number of vCPUs. If the value is `0` , there is no minimum limit.

Max -> (integer)

The maximum number of vCPUs. If this parameter is not specified, there is no maximum limit.

MemoryMiB -> (structure)

The minimum and maximum amount of memory, in MiB.

Min -> (integer)

The minimum amount of memory, in MiB. If this parameter is not specified, there is no minimum limit.

Max -> (integer)

The maximum amount of memory, in MiB. If this parameter is not specified, there is no maximum limit.

CpuManufacturers -> (list)

The CPU manufacturers to include.

- For instance types with Intel CPUs, specify `intel` .
- For instance types with AMD CPUs, specify `amd` .
- For instance types with Amazon Web Services CPUs, specify `amazon-web-services` .
- For instance types with Apple CPUs, specify `apple` .

### Note

Donât confuse the CPU manufacturer with the CPU architecture. Instances will be launched with a compatible CPU architecture based on the Amazon Machine Image (AMI) that you specify in your launch template.

Default: Any manufacturer

(string)

MemoryGiBPerVCpu -> (structure)

The minimum and maximum amount of memory per vCPU, in GiB.

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of memory per vCPU, in GiB. If this parameter is not specified, there is no minimum limit.

Max -> (double)

The maximum amount of memory per vCPU, in GiB. If this parameter is not specified, there is no maximum limit.

ExcludedInstanceTypes -> (list)

The instance types to exclude.

You can use strings with one or more wild cards, represented by an asterisk (`*` ), to exclude an instance type, size, or generation. The following are examples: `m5.8xlarge` , `c5*.*` , `m5a.*` , `r*` , `*3*` .

For example, if you specify `c5*` ,Amazon EC2 will exclude the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*` , Amazon EC2 will exclude all the M5a instance types, but not the M5n instance types.

### Note

If you specify `ExcludedInstanceTypes` , you canât specify `AllowedInstanceTypes` .

Default: No excluded instance types

(string)

InstanceGenerations -> (list)

Indicates whether current or previous generation instance types are included. The current generation instance types are recommended for use. Current generation instance types are typically the latest two to three generations in each instance family. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide* .

For current generation instance types, specify `current` .

For previous generation instance types, specify `previous` .

Default: Current and previous generation instance types

(string)

SpotMaxPricePercentageOverLowestPrice -> (integer)

[Price protection] The price protection threshold for Spot Instances, as a percentage higher than an identified Spot price. The identified Spot price is the Spot price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified Spot price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose Spot price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 interprets as a percentage.

If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib` , the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.

This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) and [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html) .

### Note

Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you donât specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999` .

Default: `100`

OnDemandMaxPricePercentageOverLowestPrice -> (integer)

[Price protection] The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 interprets as a percentage.

To turn off price protection, specify a high value, such as `999999` .

This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) and [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html) .

### Note

If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib` , the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.

Default: `20`

BareMetal -> (string)

Indicates whether bare metal instance types must be included, excluded, or required.

- To include bare metal instance types, specify `included` .
- To require only bare metal instance types, specify `required` .
- To exclude bare metal instance types, specify `excluded` .

Default: `excluded`

BurstablePerformance -> (string)

Indicates whether burstable performance T instance types are included, excluded, or required. For more information, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) .

- To include burstable performance instance types, specify `included` .
- To require only burstable performance instance types, specify `required` .
- To exclude burstable performance instance types, specify `excluded` .

Default: `excluded`

RequireHibernateSupport -> (boolean)

Indicates whether instance types must support hibernation for On-Demand Instances.

This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) .

Default: `false`

NetworkInterfaceCount -> (structure)

The minimum and maximum number of network interfaces.

Default: No minimum or maximum limits

Min -> (integer)

The minimum number of network interfaces. If this parameter is not specified, there is no minimum limit.

Max -> (integer)

The maximum number of network interfaces. If this parameter is not specified, there is no maximum limit.

LocalStorage -> (string)

Indicates whether instance types with instance store volumes are included, excluded, or required. For more information, [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) in the *Amazon EC2 User Guide* .

- To include instance types with instance store volumes, specify `included` .
- To require only instance types with instance store volumes, specify `required` .
- To exclude instance types with instance store volumes, specify `excluded` .

Default: `included`

LocalStorageTypes -> (list)

The type of local storage that is required.

- For instance types with hard disk drive (HDD) storage, specify `hdd` .
- For instance types with solid state drive (SSD) storage, specify `ssd` .

Default: `hdd` and `ssd`

(string)

TotalLocalStorageGB -> (structure)

The minimum and maximum amount of total local storage, in GB.

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of total local storage, in GB. If this parameter is not specified, there is no minimum limit.

Max -> (double)

The maximum amount of total local storage, in GB. If this parameter is not specified, there is no maximum limit.

BaselineEbsBandwidthMbps -> (structure)

The minimum and maximum baseline bandwidth to Amazon EBS, in Mbps. For more information, see [Amazon EBSâoptimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) in the *Amazon EC2 User Guide* .

Default: No minimum or maximum limits

Min -> (integer)

The minimum baseline bandwidth, in Mbps. If this parameter is not specified, there is no minimum limit.

Max -> (integer)

The maximum baseline bandwidth, in Mbps. If this parameter is not specified, there is no maximum limit.

AcceleratorTypes -> (list)

The accelerator types that must be on the instance type.

- For instance types with FPGA accelerators, specify `fpga` .
- For instance types with GPU accelerators, specify `gpu` .
- For instance types with Inference accelerators, specify `inference` .

Default: Any accelerator type

(string)

AcceleratorCount -> (structure)

The minimum and maximum number of accelerators (GPUs, FPGAs, or Amazon Web Services Inferentia chips) on an instance.

To exclude accelerator-enabled instance types, set `Max` to `0` .

Default: No minimum or maximum limits

Min -> (integer)

The minimum number of accelerators. If this parameter is not specified, there is no minimum limit.

Max -> (integer)

The maximum number of accelerators. If this parameter is not specified, there is no maximum limit.

AcceleratorManufacturers -> (list)

Indicates whether instance types must have accelerators by specific manufacturers.

- For instance types with Amazon Web Services devices, specify `amazon-web-services` .
- For instance types with AMD devices, specify `amd` .
- For instance types with Habana devices, specify `habana` .
- For instance types with NVIDIA devices, specify `nvidia` .
- For instance types with Xilinx devices, specify `xilinx` .

Default: Any manufacturer

(string)

AcceleratorNames -> (list)

The accelerators that must be on the instance type.

- For instance types with NVIDIA A10G GPUs, specify `a10g` .
- For instance types with NVIDIA A100 GPUs, specify `a100` .
- For instance types with NVIDIA H100 GPUs, specify `h100` .
- For instance types with Amazon Web Services Inferentia chips, specify `inferentia` .
- For instance types with NVIDIA GRID K520 GPUs, specify `k520` .
- For instance types with NVIDIA K80 GPUs, specify `k80` .
- For instance types with NVIDIA M60 GPUs, specify `m60` .
- For instance types with AMD Radeon Pro V520 GPUs, specify `radeon-pro-v520` .
- For instance types with NVIDIA T4 GPUs, specify `t4` .
- For instance types with NVIDIA T4G GPUs, specify `t4g` .
- For instance types with Xilinx VU9P FPGAs, specify `vu9p` .
- For instance types with NVIDIA V100 GPUs, specify `v100` .

Default: Any accelerator

(string)

AcceleratorTotalMemoryMiB -> (structure)

The minimum and maximum amount of total accelerator memory, in MiB.

Default: No minimum or maximum limits

Min -> (integer)

The minimum amount of accelerator memory, in MiB. If this parameter is not specified, there is no minimum limit.

Max -> (integer)

The maximum amount of accelerator memory, in MiB. If this parameter is not specified, there is no maximum limit.

NetworkBandwidthGbps -> (structure)

The minimum and maximum amount of network bandwidth, in gigabits per second (Gbps).

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of network bandwidth, in Gbps. If this parameter is not specified, there is no minimum limit.

Max -> (double)

The maximum amount of network bandwidth, in Gbps. If this parameter is not specified, there is no maximum limit.

AllowedInstanceTypes -> (list)

The instance types to apply your specified attributes against. All other instance types are ignored, even if they match your specified attributes.

You can use strings with one or more wild cards, represented by an asterisk (`*` ), to allow an instance type, size, or generation. The following are examples: `m5.8xlarge` , `c5*.*` , `m5a.*` , `r*` , `*3*` .

For example, if you specify `c5*` ,Amazon EC2 will allow the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*` , Amazon EC2 will allow all the M5a instance types, but not the M5n instance types.

### Note

If you specify `AllowedInstanceTypes` , you canât specify `ExcludedInstanceTypes` .

Default: All instance types

(string)

MaxSpotPriceAsPercentageOfOptimalOnDemandPrice -> (integer)

[Price protection] The price protection threshold for Spot Instances, as a percentage of an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 interprets as a percentage.

If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib` , the price protection threshold is based on the per vCPU or per memory price instead of the per instance price.

### Note

Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you donât specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999` .

BaselinePerformanceFactors -> (structure)

The baseline performance to consider, using an instance family as a baseline reference. The instance family establishes the lowest acceptable level of performance. Amazon EC2 uses this baseline to guide instance type selection, but there is no guarantee that the selected instance types will always exceed the baseline for every application. Currently, this parameter only supports CPU performance as a baseline performance factor. For more information, see [Performance protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html#ec2fleet-abis-performance-protection) in the *Amazon EC2 User Guide* .

Cpu -> (structure)

The CPU performance to consider, using an instance family as the baseline reference.

References -> (list)

Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture differences.

### Note

Currently, only one instance family can be specified in the list.

(structure)

Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture.

### Note

Currently, only one instance family can be specified in the list.

InstanceFamily -> (string)

The instance family to use as a baseline reference.

### Note

Ensure that you specify the correct value for the instance family. The instance family is everything before the period (`.` ) in the instance type name. For example, in the instance type `c6i.large` , the instance family is `c6i` , not `c6` . For more information, see [Amazon EC2 instance type naming conventions](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html) in *Amazon EC2 Instance Types* .

The following instance families are *not supported* for performance protection:

- `c1`
- `g3` | `g3s`
- `hpc7g`
- `m1` | `m2`
- `mac1` | `mac2` | `mac2-m1ultra` | `mac2-m2` | `mac2-m2pro`
- `p3dn` | `p4d` | `p5`
- `t1`
- `u-12tb1` | `u-18tb1` | `u-24tb1` | `u-3tb1` | `u-6tb1` | `u-9tb1` | `u7i-12tb` | `u7in-16tb` | `u7in-24tb` | `u7in-32tb`

If you enable performance protection by specifying a supported instance family, the returned instance types will exclude the above unsupported instance families.

If you specify an unsupported instance family as a value for baseline performance, the API returns an empty response for [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements) and an exception for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) , [RequestSpotFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet) , [ModifyFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyFleet) , and [ModifySpotFleetRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySpotFleetRequest) .

ImageId -> (string)

The ID of the AMI in the format `ami-17characters00000` .

Alternatively, you can specify a Systems Manager parameter, using one of the following formats. The Systems Manager parameter will resolve to an AMI ID on launch.

To reference a public parameter:

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id29)resolve:ssm:*public-parameter* ``

To reference a parameter stored in the same account:

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id31)resolve:ssm:*parameter-name* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id33)resolve:ssm:*parameter-name:version-number* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id35)resolve:ssm:*parameter-name:label* ``

To reference a parameter shared from another Amazon Web Services account:

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id37)resolve:ssm:*parameter-ARN* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id39)resolve:ssm:*parameter-ARN:version-number* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html#id41)resolve:ssm:*parameter-ARN:label* ``

For more information, see [Use a Systems Manager parameter instead of an AMI ID](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#use-an-ssm-parameter-instead-of-an-ami-id) in the *Amazon EC2 User Guide* .

### Note

This parameter is only available for fleets of type `instant` . For fleets of type `maintain` and `request` , you must specify the AMI ID in the launch template.

BlockDeviceMappings -> (list)

The block device mappings, which define the EBS volumes and instance store volumes to attach to the instance at launch.

Supported only for fleets of type `instant` .

For more information, see [Block device mappings for volumes on Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html) in the *Amazon EC2 User Guide* .

(structure)

Describes a block device mapping, which defines the EBS volumes and instance store volumes to attach to an instance at launch.

DeviceName -> (string)

The device name (for example, `/dev/sdh` or `xvdh` ).

VirtualName -> (string)

The virtual device name.

Ebs -> (structure)

Parameters used to automatically set up EBS volumes when the instance is launched.

Encrypted -> (boolean)

Indicates whether the volume is encrypted.

DeleteOnTermination -> (boolean)

Indicates whether the volume is deleted on instance termination.

Iops -> (integer)

The number of I/O operations per second (IOPS). For `gp3` , `io1` , and `io2` volumes, this represents the number of IOPS that are provisioned for the volume. For `gp2` volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.

Throughput -> (integer)

The throughput that the volume supports, in MiB/s.

KmsKeyId -> (string)

Identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed KMS key to use for EBS encryption.

SnapshotId -> (string)

The ID of the snapshot.

VolumeSize -> (integer)

The size of the volume, in GiBs.

VolumeType -> (string)

The volume type. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) in the *Amazon EBS User Guide* .

NoDevice -> (string)

Suppresses the specified device included in the block device mapping.

Lifecycle -> (string)

Indicates if the instance that was launched is a Spot Instance or On-Demand Instance.

InstanceIds -> (list)

The IDs of the instances.

(string)

InstanceType -> (string)

The instance type.

Platform -> (string)

The value is `windows` for Windows instances in an EC2 Fleet. Otherwise, the value is blank.