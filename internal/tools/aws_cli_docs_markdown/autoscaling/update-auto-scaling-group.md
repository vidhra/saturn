# update-auto-scaling-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [autoscaling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/index.html#cli-aws-autoscaling) ]

# update-auto-scaling-group

## Description

**We strongly recommend that all Auto Scaling groups use launch templates to ensure full functionality for Amazon EC2 Auto Scaling and Amazon EC2.**

Updates the configuration for the specified Auto Scaling group.

To update an Auto Scaling group, specify the name of the group and the property that you want to change. Any properties that you donât specify are not changed by this update request. The new settings take effect on any scaling activities after this call returns.

If you associate a new launch configuration or template with an Auto Scaling group, all new instances will get the updated configuration. Existing instances continue to run with the configuration that they were originally launched with. When you update a group to specify a mixed instances policy instead of a launch configuration or template, existing instances may be replaced to match the new purchasing options that you specified in the policy. For example, if the group currently has 100% On-Demand capacity and the policy specifies 50% Spot capacity, this means that half of your instances will be gradually terminated and relaunched as Spot Instances. When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating the old ones, so that updating your group does not compromise the performance or availability of your application.

Note the following about changing `DesiredCapacity` , `MaxSize` , or `MinSize` :

- If a scale-in activity occurs as a result of a new `DesiredCapacity` value that is lower than the current size of the group, the Auto Scaling group uses its termination policy to determine which instances to terminate.
- If you specify a new value for `MinSize` without specifying a value for `DesiredCapacity` , and the new `MinSize` is larger than the current size of the group, this sets the groupâs `DesiredCapacity` to the new `MinSize` value.
- If you specify a new value for `MaxSize` without specifying a value for `DesiredCapacity` , and the new `MaxSize` is smaller than the current size of the group, this sets the groupâs `DesiredCapacity` to the new `MaxSize` value.

To see which properties have been set, call the [DescribeAutoScalingGroups](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAutoScalingGroups.html) API. To view the scaling policies for an Auto Scaling group, call the [DescribePolicies](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribePolicies.html) API. If the group has scaling policies, you can update them by calling the [PutScalingPolicy](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutScalingPolicy.html) API.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/UpdateAutoScalingGroup)

## Synopsis

```
update-auto-scaling-group
--auto-scaling-group-name <value>
[--launch-configuration-name <value>]
[--launch-template <value>]
[--mixed-instances-policy <value>]
[--min-size <value>]
[--max-size <value>]
[--desired-capacity <value>]
[--default-cooldown <value>]
[--availability-zones <value>]
[--health-check-type <value>]
[--health-check-grace-period <value>]
[--placement-group <value>]
[--vpc-zone-identifier <value>]
[--termination-policies <value>]
[--new-instances-protected-from-scale-in | --no-new-instances-protected-from-scale-in]
[--service-linked-role-arn <value>]
[--max-instance-lifetime <value>]
[--capacity-rebalance | --no-capacity-rebalance]
[--context <value>]
[--desired-capacity-type <value>]
[--default-instance-warmup <value>]
[--instance-maintenance-policy <value>]
[--availability-zone-distribution <value>]
[--availability-zone-impairment-policy <value>]
[--skip-zonal-shift-validation | --no-skip-zonal-shift-validation]
[--capacity-reservation-specification <value>]
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

`--auto-scaling-group-name` (string)

The name of the Auto Scaling group.

`--launch-configuration-name` (string)

The name of the launch configuration. If you specify `LaunchConfigurationName` in your update request, you canât specify `LaunchTemplate` or `MixedInstancesPolicy` .

`--launch-template` (structure)

The launch template and version to use to specify the updates. If you specify `LaunchTemplate` in your update request, you canât specify `LaunchConfigurationName` or `MixedInstancesPolicy` .

LaunchTemplateId -> (string)

The ID of the launch template. To get the template ID, use the Amazon EC2 [DescribeLaunchTemplates](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html) API operation. New launch templates can be created using the Amazon EC2 [CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) API.

Conditional: You must specify either a `LaunchTemplateId` or a `LaunchTemplateName` .

LaunchTemplateName -> (string)

The name of the launch template. To get the template name, use the Amazon EC2 [DescribeLaunchTemplates](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html) API operation. New launch templates can be created using the Amazon EC2 [CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) API.

Conditional: You must specify either a `LaunchTemplateId` or a `LaunchTemplateName` .

Version -> (string)

The version number, `$Latest` , or `$Default` . To get the version number, use the Amazon EC2 [DescribeLaunchTemplateVersions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplateVersions.html) API operation. New launch template versions can be created using the Amazon EC2 [CreateLaunchTemplateVersion](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplateVersion.html) API. If the value is `$Latest` , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is `$Default` , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is `$Default` .

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

`--mixed-instances-policy` (structure)

The mixed instances policy. For more information, see [Auto Scaling groups with multiple instance types and purchase options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html) in the *Amazon EC2 Auto Scaling User Guide* .

LaunchTemplate -> (structure)

One or more launch templates and the instance types (overrides) that are used to launch EC2 instances to fulfill On-Demand and Spot capacities.

LaunchTemplateSpecification -> (structure)

The launch template.

LaunchTemplateId -> (string)

The ID of the launch template. To get the template ID, use the Amazon EC2 [DescribeLaunchTemplates](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html) API operation. New launch templates can be created using the Amazon EC2 [CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) API.

Conditional: You must specify either a `LaunchTemplateId` or a `LaunchTemplateName` .

LaunchTemplateName -> (string)

The name of the launch template. To get the template name, use the Amazon EC2 [DescribeLaunchTemplates](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html) API operation. New launch templates can be created using the Amazon EC2 [CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) API.

Conditional: You must specify either a `LaunchTemplateId` or a `LaunchTemplateName` .

Version -> (string)

The version number, `$Latest` , or `$Default` . To get the version number, use the Amazon EC2 [DescribeLaunchTemplateVersions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplateVersions.html) API operation. New launch template versions can be created using the Amazon EC2 [CreateLaunchTemplateVersion](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplateVersion.html) API. If the value is `$Latest` , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is `$Default` , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is `$Default` .

Overrides -> (list)

Any properties that you specify override the same properties in the launch template.

(structure)

Use this structure to let Amazon EC2 Auto Scaling do the following when the Auto Scaling group has a mixed instances policy:

- Override the instance type that is specified in the launch template.
- Use multiple instance types.

Specify the instance types that you want, or define your instance requirements instead and let Amazon EC2 Auto Scaling provision the available instance types that meet your requirements. This can provide Amazon EC2 Auto Scaling with a larger selection of instance types to choose from when fulfilling Spot and On-Demand capacities. You can view which instance types are matched before you apply the instance requirements to your Auto Scaling group.

After you define your instance requirements, you donât have to keep updating these settings to get new EC2 instance types automatically. Amazon EC2 Auto Scaling uses the instance requirements of the Auto Scaling group to determine whether a new EC2 instance type can be used.

InstanceType -> (string)

The instance type, such as `m3.xlarge` . You must specify an instance type that is supported in your requested Region and Availability Zones. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide for Linux Instances* .

You can specify up to 40 instance types per Auto Scaling group.

WeightedCapacity -> (string)

If you provide a list of instance types to use, you can specify the number of capacity units provided by each instance type in terms of virtual CPUs, memory, storage, throughput, or other relative performance characteristic. When a Spot or On-Demand Instance is launched, the capacity units count toward the desired capacity. Amazon EC2 Auto Scaling launches instances until the desired capacity is totally fulfilled, even if this results in an overage. For example, if there are two units remaining to fulfill capacity, and Amazon EC2 Auto Scaling can only launch an instance with a `WeightedCapacity` of five units, the instance is launched, and the desired capacity is exceeded by three units. For more information, see [Configure an Auto Scaling group to use instance weights](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups-instance-weighting.html) in the *Amazon EC2 Auto Scaling User Guide* . Value must be in the range of 1â999.

If you specify a value for `WeightedCapacity` for one instance type, you must specify a value for `WeightedCapacity` for all of them.

### Warning

Every Auto Scaling group has three size parameters (`DesiredCapacity` , `MaxSize` , and `MinSize` ). Usually, you set these sizes based on a specific number of instances. However, if you configure a mixed instances policy that defines weights for the instance types, you must specify these sizes with the same units that you use for weighting instances.

LaunchTemplateSpecification -> (structure)

Provides a launch template for the specified instance type or set of instance requirements. For example, some instance types might require a launch template with a different AMI. If not provided, Amazon EC2 Auto Scaling uses the launch template thatâs specified in the `LaunchTemplate` definition. For more information, see [Specifying a different launch template for an instance type](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups-launch-template-overrides.html) in the *Amazon EC2 Auto Scaling User Guide* .

You can specify up to 20 launch templates per Auto Scaling group. The launch templates specified in the overrides and in the `LaunchTemplate` definition count towards this limit.

LaunchTemplateId -> (string)

The ID of the launch template. To get the template ID, use the Amazon EC2 [DescribeLaunchTemplates](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html) API operation. New launch templates can be created using the Amazon EC2 [CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) API.

Conditional: You must specify either a `LaunchTemplateId` or a `LaunchTemplateName` .

LaunchTemplateName -> (string)

The name of the launch template. To get the template name, use the Amazon EC2 [DescribeLaunchTemplates](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html) API operation. New launch templates can be created using the Amazon EC2 [CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) API.

Conditional: You must specify either a `LaunchTemplateId` or a `LaunchTemplateName` .

Version -> (string)

The version number, `$Latest` , or `$Default` . To get the version number, use the Amazon EC2 [DescribeLaunchTemplateVersions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplateVersions.html) API operation. New launch template versions can be created using the Amazon EC2 [CreateLaunchTemplateVersion](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplateVersion.html) API. If the value is `$Latest` , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is `$Default` , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is `$Default` .

InstanceRequirements -> (structure)

The instance requirements. Amazon EC2 Auto Scaling uses your specified requirements to identify instance types. Then, it uses your On-Demand and Spot allocation strategies to launch instances from these instance types.

You can specify up to four separate sets of instance requirements per Auto Scaling group. This is useful for provisioning instances from different Amazon Machine Images (AMIs) in the same Auto Scaling group. To do this, create the AMIs and create a new launch template for each AMI. Then, create a compatible set of instance requirements for each launch template.

### Note

If you specify `InstanceRequirements` , you canât specify `InstanceType` .

VCpuCount -> (structure)

The minimum and maximum number of vCPUs for an instance type.

Min -> (integer)

The minimum number of vCPUs.

Max -> (integer)

The maximum number of vCPUs.

MemoryMiB -> (structure)

The minimum and maximum instance memory size for an instance type, in MiB.

Min -> (integer)

The memory minimum in MiB.

Max -> (integer)

The memory maximum in MiB.

CpuManufacturers -> (list)

Lists which specific CPU manufacturers to include.

- For instance types with Intel CPUs, specify `intel` .
- For instance types with AMD CPUs, specify `amd` .
- For instance types with Amazon Web Services CPUs, specify `amazon-web-services` .

### Note

Donât confuse the CPU hardware manufacturer with the CPU hardware architecture. Instances will be launched with a compatible CPU architecture based on the Amazon Machine Image (AMI) that you specify in your launch template.

Default: Any manufacturer

(string)

MemoryGiBPerVCpu -> (structure)

The minimum and maximum amount of memory per vCPU for an instance type, in GiB.

Default: No minimum or maximum limits

Min -> (double)

The memory minimum in GiB.

Max -> (double)

The memory maximum in GiB.

ExcludedInstanceTypes -> (list)

The instance types to exclude. You can use strings with one or more wild cards, represented by an asterisk (`*` ), to exclude an instance family, type, size, or generation. The following are examples: `m5.8xlarge` , `c5*.*` , `m5a.*` , `r*` , `*3*` .

For example, if you specify `c5*` , you are excluding the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*` , Amazon EC2 Auto Scaling will exclude all the M5a instance types, but not the M5n instance types.

### Note

If you specify `ExcludedInstanceTypes` , you canât specify `AllowedInstanceTypes` .

Default: No excluded instance types

(string)

InstanceGenerations -> (list)

Indicates whether current or previous generation instance types are included.

- For current generation instance types, specify `current` . The current generation includes EC2 instance types currently recommended for use. This typically includes the latest two to three generations in each instance family. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide for Linux Instances* .
- For previous generation instance types, specify `previous` .

Default: Any current or previous generation

(string)

SpotMaxPricePercentageOverLowestPrice -> (integer)

[Price protection] The price protection threshold for Spot Instances, as a percentage higher than an identified Spot price. The identified Spot price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from either the lowest priced current generation instance types or, failing that, the lowest priced previous generation instance types that match your attributes. When Amazon EC2 Auto Scaling selects instance types with your attributes, we will exclude instance types whose price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 Auto Scaling interprets as a percentage.

If you set `DesiredCapacityType` to `vcpu` or `memory-mib` , the price protection threshold is based on the per-vCPU or per-memory price instead of the per instance price.

### Note

Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you donât specify either, Amazon EC2 Auto Scaling will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999` .

MaxSpotPriceAsPercentageOfOptimalOnDemandPrice -> (integer)

[Price protection] The price protection threshold for Spot Instances, as a percentage of an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from either the lowest priced current generation instance types or, failing that, the lowest priced previous generation instance types that match your attributes. When Amazon EC2 Auto Scaling selects instance types with your attributes, we will exclude instance types whose price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 Auto Scaling interprets as a percentage.

If you set `DesiredCapacityType` to `vcpu` or `memory-mib` , the price protection threshold is based on the per-vCPU or per-memory price instead of the per instance price.

### Note

Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you donât specify either, Amazon EC2 Auto Scaling will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999` .

OnDemandMaxPricePercentageOverLowestPrice -> (integer)

[Price protection] The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from either the lowest priced current generation instance types or, failing that, the lowest priced previous generation instance types that match your attributes. When Amazon EC2 Auto Scaling selects instance types with your attributes, we will exclude instance types whose price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 Auto Scaling interprets as a percentage.

To turn off price protection, specify a high value, such as `999999` .

If you set `DesiredCapacityType` to `vcpu` or `memory-mib` , the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per instance price.

Default: `20`

BareMetal -> (string)

Indicates whether bare metal instance types are included, excluded, or required.

Default: `excluded`

BurstablePerformance -> (string)

Indicates whether burstable performance instance types are included, excluded, or required. For more information, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) in the *Amazon EC2 User Guide for Linux Instances* .

Default: `excluded`

RequireHibernateSupport -> (boolean)

Indicates whether instance types must provide On-Demand Instance hibernation support.

Default: `false`

NetworkInterfaceCount -> (structure)

The minimum and maximum number of network interfaces for an instance type.

Default: No minimum or maximum limits

Min -> (integer)

The minimum number of network interfaces.

Max -> (integer)

The maximum number of network interfaces.

LocalStorage -> (string)

Indicates whether instance types with instance store volumes are included, excluded, or required. For more information, see [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) in the *Amazon EC2 User Guide for Linux Instances* .

Default: `included`

LocalStorageTypes -> (list)

Indicates the type of local storage that is required.

- For instance types with hard disk drive (HDD) storage, specify `hdd` .
- For instance types with solid state drive (SSD) storage, specify `ssd` .

Default: Any local storage type

(string)

TotalLocalStorageGB -> (structure)

The minimum and maximum total local storage size for an instance type, in GB.

Default: No minimum or maximum limits

Min -> (double)

The storage minimum in GB.

Max -> (double)

The storage maximum in GB.

BaselineEbsBandwidthMbps -> (structure)

The minimum and maximum baseline bandwidth performance for an instance type, in Mbps. For more information, see [Amazon EBSâoptimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) in the *Amazon EC2 User Guide for Linux Instances* .

Default: No minimum or maximum limits

Min -> (integer)

The minimum value in Mbps.

Max -> (integer)

The maximum value in Mbps.

AcceleratorTypes -> (list)

Lists the accelerator types that must be on an instance type.

- For instance types with GPU accelerators, specify `gpu` .
- For instance types with FPGA accelerators, specify `fpga` .
- For instance types with inference accelerators, specify `inference` .

Default: Any accelerator type

(string)

AcceleratorCount -> (structure)

The minimum and maximum number of accelerators (GPUs, FPGAs, or Amazon Web Services Inferentia chips) for an instance type.

To exclude accelerator-enabled instance types, set `Max` to `0` .

Default: No minimum or maximum limits

Min -> (integer)

The minimum value.

Max -> (integer)

The maximum value.

AcceleratorManufacturers -> (list)

Indicates whether instance types must have accelerators by specific manufacturers.

- For instance types with NVIDIA devices, specify `nvidia` .
- For instance types with AMD devices, specify `amd` .
- For instance types with Amazon Web Services devices, specify `amazon-web-services` .
- For instance types with Xilinx devices, specify `xilinx` .

Default: Any manufacturer

(string)

AcceleratorNames -> (list)

Lists the accelerators that must be on an instance type.

- For instance types with NVIDIA A100 GPUs, specify `a100` .
- For instance types with NVIDIA V100 GPUs, specify `v100` .
- For instance types with NVIDIA K80 GPUs, specify `k80` .
- For instance types with NVIDIA T4 GPUs, specify `t4` .
- For instance types with NVIDIA M60 GPUs, specify `m60` .
- For instance types with AMD Radeon Pro V520 GPUs, specify `radeon-pro-v520` .
- For instance types with Xilinx VU9P FPGAs, specify `vu9p` .

Default: Any accelerator

(string)

AcceleratorTotalMemoryMiB -> (structure)

The minimum and maximum total memory size for the accelerators on an instance type, in MiB.

Default: No minimum or maximum limits

Min -> (integer)

The memory minimum in MiB.

Max -> (integer)

The memory maximum in MiB.

NetworkBandwidthGbps -> (structure)

The minimum and maximum amount of network bandwidth, in gigabits per second (Gbps).

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of network bandwidth, in gigabits per second (Gbps).

Max -> (double)

The maximum amount of network bandwidth, in gigabits per second (Gbps).

AllowedInstanceTypes -> (list)

The instance types to apply your specified attributes against. All other instance types are ignored, even if they match your specified attributes.

You can use strings with one or more wild cards, represented by an asterisk (`*` ), to allow an instance type, size, or generation. The following are examples: `m5.8xlarge` , `c5*.*` , `m5a.*` , `r*` , `*3*` .

For example, if you specify `c5*` , Amazon EC2 Auto Scaling will allow the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*` , Amazon EC2 Auto Scaling will allow all the M5a instance types, but not the M5n instance types.

### Note

If you specify `AllowedInstanceTypes` , you canât specify `ExcludedInstanceTypes` .

Default: All instance types

(string)

BaselinePerformanceFactors -> (structure)

The baseline performance factors for the instance requirements.

Cpu -> (structure)

The CPU performance to consider, using an instance family as the baseline reference.

References -> (list)

Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture differences.

### Note

Currently only one instance family can be specified in the list.

(structure)

Specify an instance family to use as the baseline reference for CPU performance. All instance types that All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture differences.

### Note

Currently only one instance family can be specified in the list.

InstanceFamily -> (string)

The instance family to use as a baseline reference.

### Note

Make sure that you specify the correct value for the instance family. The instance family is everything before the period (.) in the instance type name. For example, in the instance `c6i.large` , the instance family is `c6i` , not `c6` . For more information, see [Amazon EC2 instance type naming conventions](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html) in *Amazon EC2 Instance Types* .

The following instance types are *not supported* for performance protection.

- `c1`
- `g3| g3s`
- `hpc7g`
- `m1| m2`
- `mac1 | mac2 | mac2-m1ultra | mac2-m2 | mac2-m2pro`
- `p3dn | p4d | p5`
- `t1`
- `u-12tb1 | u-18tb1 | u-24tb1 | u-3tb1 | u-6tb1 | u-9tb1 | u7i-12tb | u7in-16tb | u7in-24tb | u7in-32tb`

If you performance protection by specifying a supported instance family, the returned instance types will exclude the preceding unsupported instance families.

If you specify an unsupported instance family as a value for baseline performance, the API returns an empty response.

InstancesDistribution -> (structure)

The instances distribution.

OnDemandAllocationStrategy -> (string)

The allocation strategy to apply to your On-Demand Instances when they are launched. Possible instance types are determined by the launch template overrides that you specify.

The following lists the valid values:

lowest-price

Uses price to determine which instance types are the highest priority, launching the lowest priced instance types within an Availability Zone first. This is the default value for Auto Scaling groups that specify [InstanceRequirements](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html) .

prioritized

You set the order of instance types for the launch template overrides from highest to lowest priority (from first to last in the list). Amazon EC2 Auto Scaling launches your highest priority instance types first. If all your On-Demand capacity cannot be fulfilled using your highest priority instance type, then Amazon EC2 Auto Scaling launches the remaining capacity using the second priority instance type, and so on. This is the default value for Auto Scaling groups that donât specify [InstanceRequirements](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html) and cannot be used for groups that do.

OnDemandBaseCapacity -> (integer)

The minimum amount of the Auto Scaling groupâs capacity that must be fulfilled by On-Demand Instances. This base portion is launched first as your group scales.

This number has the same unit of measurement as the groupâs desired capacity. If you change the default unit of measurement (number of instances) by specifying weighted capacity values in your launch template overrides list, or by changing the default desired capacity type setting of the group, you must specify this number using the same unit of measurement.

Default: 0

OnDemandPercentageAboveBaseCapacity -> (integer)

Controls the percentages of On-Demand Instances and Spot Instances for your additional capacity beyond `OnDemandBaseCapacity` . Expressed as a number (for example, 20 specifies 20% On-Demand Instances, 80% Spot Instances). If set to 100, only On-Demand Instances are used.

Default: 100

SpotAllocationStrategy -> (string)

The allocation strategy to apply to your Spot Instances when they are launched. Possible instance types are determined by the launch template overrides that you specify.

The following lists the valid values:

capacity-optimized

Requests Spot Instances using pools that are optimally chosen based on the available Spot capacity. This strategy has the lowest risk of interruption. To give certain instance types a higher chance of launching first, use `capacity-optimized-prioritized` .

capacity-optimized-prioritized

You set the order of instance types for the launch template overrides from highest to lowest priority (from first to last in the list). Amazon EC2 Auto Scaling honors the instance type priorities on a best effort basis but optimizes for capacity first. Note that if the On-Demand allocation strategy is set to `prioritized` , the same priority is applied when fulfilling On-Demand capacity. This is not a valid value for Auto Scaling groups that specify [InstanceRequirements](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html) .

lowest-price

Requests Spot Instances using the lowest priced pools within an Availability Zone, across the number of Spot pools that you specify for the `SpotInstancePools` property. To ensure that your desired capacity is met, you might receive Spot Instances from several pools. This is the default value, but it might lead to high interruption rates because this strategy only considers instance price and not available capacity.

price-capacity-optimized (recommended)

The price and capacity optimized allocation strategy looks at both price and capacity to select the Spot Instance pools that are the least likely to be interrupted and have the lowest possible price.

SpotInstancePools -> (integer)

The number of Spot Instance pools across which to allocate your Spot Instances. The Spot pools are determined from the different instance types in the overrides. Valid only when the `SpotAllocationStrategy` is `lowest-price` . Value must be in the range of 1â20.

Default: 2

SpotMaxPrice -> (string)

The maximum price per unit hour that you are willing to pay for a Spot Instance. If your maximum price is lower than the Spot price for the instance types that you selected, your Spot Instances are not launched. We do not recommend specifying a maximum price because it can lead to increased interruptions. When Spot Instances launch, you pay the current Spot price. To remove a maximum price that you previously set, include the property but specify an empty string (ââ) for the value.

### Warning

If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify one.

Valid Range: Minimum value of 0.001

JSON Syntax:

```
{
  "LaunchTemplate": {
    "LaunchTemplateSpecification": {
      "LaunchTemplateId": "string",
      "LaunchTemplateName": "string",
      "Version": "string"
    },
    "Overrides": [
      {
        "InstanceType": "string",
        "WeightedCapacity": "string",
        "LaunchTemplateSpecification": {
          "LaunchTemplateId": "string",
          "LaunchTemplateName": "string",
          "Version": "string"
        },
        "InstanceRequirements": {
          "VCpuCount": {
            "Min": integer,
            "Max": integer
          },
          "MemoryMiB": {
            "Min": integer,
            "Max": integer
          },
          "CpuManufacturers": ["intel"|"amd"|"amazon-web-services", ...],
          "MemoryGiBPerVCpu": {
            "Min": double,
            "Max": double
          },
          "ExcludedInstanceTypes": ["string", ...],
          "InstanceGenerations": ["current"|"previous", ...],
          "SpotMaxPricePercentageOverLowestPrice": integer,
          "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice": integer,
          "OnDemandMaxPricePercentageOverLowestPrice": integer,
          "BareMetal": "included"|"excluded"|"required",
          "BurstablePerformance": "included"|"excluded"|"required",
          "RequireHibernateSupport": true|false,
          "NetworkInterfaceCount": {
            "Min": integer,
            "Max": integer
          },
          "LocalStorage": "included"|"excluded"|"required",
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
          "AcceleratorManufacturers": ["nvidia"|"amd"|"amazon-web-services"|"xilinx", ...],
          "AcceleratorNames": ["a100"|"v100"|"k80"|"t4"|"m60"|"radeon-pro-v520"|"vu9p", ...],
          "AcceleratorTotalMemoryMiB": {
            "Min": integer,
            "Max": integer
          },
          "NetworkBandwidthGbps": {
            "Min": double,
            "Max": double
          },
          "AllowedInstanceTypes": ["string", ...],
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
        }
      }
      ...
    ]
  },
  "InstancesDistribution": {
    "OnDemandAllocationStrategy": "string",
    "OnDemandBaseCapacity": integer,
    "OnDemandPercentageAboveBaseCapacity": integer,
    "SpotAllocationStrategy": "string",
    "SpotInstancePools": integer,
    "SpotMaxPrice": "string"
  }
}
```

`--min-size` (integer)

The minimum size of the Auto Scaling group.

`--max-size` (integer)

The maximum size of the Auto Scaling group.

### Note

With a mixed instances policy that uses instance weighting, Amazon EC2 Auto Scaling may need to go above `MaxSize` to meet your capacity requirements. In this event, Amazon EC2 Auto Scaling will never go above `MaxSize` by more than your largest instance weight (weights that define how many units each instance contributes to the desired capacity of the group).

`--desired-capacity` (integer)

The desired capacity is the initial capacity of the Auto Scaling group after this operation completes and the capacity it attempts to maintain. This number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group.

`--default-cooldown` (integer)

*Only needed if you use simple scaling policies.*

The amount of time, in seconds, between one scaling activity ending and another one starting due to simple scaling policies. For more information, see [Scaling cooldowns for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html) in the *Amazon EC2 Auto Scaling User Guide* .

`--availability-zones` (list)

One or more Availability Zones for the group.

(string)

Syntax:

```
"string" "string" ...
```

`--health-check-type` (string)

A comma-separated value string of one or more health check types.

The valid values are `EC2` , `EBS` , `ELB` , and `VPC_LATTICE` . `EC2` is the default health check and cannot be disabled. For more information, see [Health checks for instances in an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html) in the *Amazon EC2 Auto Scaling User Guide* .

Only specify `EC2` if you must clear a value that was previously set.

`--health-check-grace-period` (integer)

The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service and marking it unhealthy due to a failed health check. This is useful if your instances do not immediately pass their health checks after they enter the `InService` state. For more information, see [Set the health check grace period for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-check-grace-period.html) in the *Amazon EC2 Auto Scaling User Guide* .

`--placement-group` (string)

The name of an existing placement group into which to launch your instances. To remove the placement group setting, pass an empty string for `placement-group` . For more information about placement groups, see [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in the *Amazon EC2 User Guide for Linux Instances* .

### Note

A *cluster* placement group is a logical grouping of instances within a single Availability Zone. You cannot specify multiple Availability Zones and a cluster placement group.

`--vpc-zone-identifier` (string)

A comma-separated list of subnet IDs for a virtual private cloud (VPC). If you specify `VPCZoneIdentifier` with `AvailabilityZones` , the subnets that you specify must reside in those Availability Zones.

`--termination-policies` (list)

A policy or a list of policies that are used to select the instances to terminate. The policies are executed in the order that you list them. For more information, see [Configure termination policies for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-termination-policies.html) in the *Amazon EC2 Auto Scaling User Guide* .

Valid values: `Default` | `AllocationStrategy` | `ClosestToNextInstanceHour` | `NewestInstance` | `OldestInstance` | `OldestLaunchConfiguration` | `OldestLaunchTemplate` | `arn:aws:lambda:region:account-id:function:my-function:my-alias`

(string)

Syntax:

```
"string" "string" ...
```

`--new-instances-protected-from-scale-in` | `--no-new-instances-protected-from-scale-in` (boolean)

Indicates whether newly launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in. For more information about preventing instances from terminating on scale in, see [Use instance scale-in protection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html) in the *Amazon EC2 Auto Scaling User Guide* .

`--service-linked-role-arn` (string)

The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other Amazon Web Services on your behalf. For more information, see [Service-linked roles](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-service-linked-role.html) in the *Amazon EC2 Auto Scaling User Guide* .

`--max-instance-lifetime` (integer)

The maximum amount of time, in seconds, that an instance can be in service. The default is null. If specified, the value must be either 0 or a number equal to or greater than 86,400 seconds (1 day). To clear a previously set value, specify a new value of 0. For more information, see [Replacing Auto Scaling instances based on maximum instance lifetime](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-max-instance-lifetime.html) in the *Amazon EC2 Auto Scaling User Guide* .

`--capacity-rebalance` | `--no-capacity-rebalance` (boolean)

Enables or disables Capacity Rebalancing. If Capacity Rebalancing is disabled, proactive replacement of at-risk Spot Instances does not occur. For more information, see [Capacity Rebalancing in Auto Scaling to replace at-risk Spot Instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.html) in the *Amazon EC2 Auto Scaling User Guide* .

### Note

To suspend rebalancing across Availability Zones, use the [SuspendProcesses](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_SuspendedProcess.html) API.

`--context` (string)

Reserved.

`--desired-capacity-type` (string)

The unit of measurement for the value specified for desired capacity. Amazon EC2 Auto Scaling supports `DesiredCapacityType` for attribute-based instance type selection only. For more information, see [Create a mixed instances group using attribute-based instance type selection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-mixed-instances-group-attribute-based-instance-type-selection.html) in the *Amazon EC2 Auto Scaling User Guide* .

By default, Amazon EC2 Auto Scaling specifies `units` , which translates into number of instances.

Valid values: `units` | `vcpu` | `memory-mib`

`--default-instance-warmup` (integer)

The amount of time, in seconds, until a new instance is considered to have finished initializing and resource consumption to become stable after it enters the `InService` state.

During an instance refresh, Amazon EC2 Auto Scaling waits for the warm-up period after it replaces an instance before it moves on to replacing the next instance. Amazon EC2 Auto Scaling also waits for the warm-up period before aggregating the metrics for new instances with existing instances in the Amazon CloudWatch metrics that are used for scaling, resulting in more reliable usage data. For more information, see [Set the default instance warmup for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-default-instance-warmup.html) in the *Amazon EC2 Auto Scaling User Guide* .

### Warning

To manage various warm-up settings at the group level, we recommend that you set the default instance warmup, *even if it is set to 0 seconds* . To remove a value that you previously set, include the property but specify `-1` for the value. However, we strongly recommend keeping the default instance warmup enabled by specifying a value of `0` or other nominal value.

`--instance-maintenance-policy` (structure)

An instance maintenance policy. For more information, see [Set instance maintenance policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-maintenance-policy.html) in the *Amazon EC2 Auto Scaling User Guide* .

MinHealthyPercentage -> (integer)

Specifies the lower threshold as a percentage of the desired capacity of the Auto Scaling group. It represents the minimum percentage of the group to keep in service, healthy, and ready to use to support your workload when replacing instances. Value range is 0 to 100. To clear a previously set value, specify a value of `-1` .

MaxHealthyPercentage -> (integer)

Specifies the upper threshold as a percentage of the desired capacity of the Auto Scaling group. It represents the maximum percentage of the group that can be in service and healthy, or pending, to support your workload when replacing instances. Value range is 100 to 200. To clear a previously set value, specify a value of `-1` .

Both `MinHealthyPercentage` and `MaxHealthyPercentage` must be specified, and the difference between them cannot be greater than 100. A large range increases the number of instances that can be replaced at the same time.

Shorthand Syntax:

```
MinHealthyPercentage=integer,MaxHealthyPercentage=integer
```

JSON Syntax:

```
{
  "MinHealthyPercentage": integer,
  "MaxHealthyPercentage": integer
}
```

`--availability-zone-distribution` (structure)

The instance capacity distribution across Availability Zones.

CapacityDistributionStrategy -> (string)

If launches fail in an Availability Zone, the following strategies are available. The default is `balanced-best-effort` .

- `balanced-only` - If launches fail in an Availability Zone, Auto Scaling will continue to attempt to launch in the unhealthy zone to preserve a balanced distribution.
- `balanced-best-effort` - If launches fail in an Availability Zone, Auto Scaling will attempt to launch in another healthy Availability Zone instead.

Shorthand Syntax:

```
CapacityDistributionStrategy=string
```

JSON Syntax:

```
{
  "CapacityDistributionStrategy": "balanced-only"|"balanced-best-effort"
}
```

`--availability-zone-impairment-policy` (structure)

The policy for Availability Zone impairment.

ZonalShiftEnabled -> (boolean)

If `true` , enable zonal shift for your Auto Scaling group.

ImpairedZoneHealthCheckBehavior -> (string)

Specifies the health check behavior for the impaired Availability Zone in an active zonal shift. If you select `Replace unhealthy` , instances that appear unhealthy will be replaced in all Availability Zones. If you select `Ignore unhealthy` , instances will not be replaced in the Availability Zone with the active zonal shift. For more information, see [Auto Scaling group zonal shift](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-zonal-shift.html) in the *Amazon EC2 Auto Scaling User Guide* .

Shorthand Syntax:

```
ZonalShiftEnabled=boolean,ImpairedZoneHealthCheckBehavior=string
```

JSON Syntax:

```
{
  "ZonalShiftEnabled": true|false,
  "ImpairedZoneHealthCheckBehavior": "ReplaceUnhealthy"|"IgnoreUnhealthy"
}
```

`--skip-zonal-shift-validation` | `--no-skip-zonal-shift-validation` (boolean)

If you enable zonal shift with cross-zone disabled load balancers, capacity could become imbalanced across Availability Zones. To skip the validation, specify `true` . For more information, see [Auto Scaling group zonal shift](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-zonal-shift.html) in the *Amazon EC2 Auto Scaling User Guide* .

`--capacity-reservation-specification` (structure)

The capacity reservation specification for the Auto Scaling group.

CapacityReservationPreference -> (string)

The capacity reservation preference. The following options are available:

- `capacity-reservations-only` - Auto Scaling will only launch instances into a Capacity Reservation or Capacity Reservation resource group. If capacity isnât available, instances will fail to launch.
- `capacity-reservations-first` - Auto Scaling will try to launch instances into a Capacity Reservation or Capacity Reservation resource group first. If capacity isnât available, instances will run in On-Demand capacity.
- `none` - Auto Scaling will not launch instances into a Capacity Reservation. Instances will run in On-Demand capacity.
- `default` - Auto Scaling uses the Capacity Reservation preference from your launch template or an open Capacity Reservation.

CapacityReservationTarget -> (structure)

Describes a target Capacity Reservation or Capacity Reservation resource group.

CapacityReservationIds -> (list)

The Capacity Reservation IDs to launch instances into.

(string)

CapacityReservationResourceGroupArns -> (list)

The resource group ARNs of the Capacity Reservation to launch instances into.

(string)

Shorthand Syntax:

```
CapacityReservationPreference=string,CapacityReservationTarget={CapacityReservationIds=[string,string],CapacityReservationResourceGroupArns=[string,string]}
```

JSON Syntax:

```
{
  "CapacityReservationPreference": "capacity-reservations-only"|"capacity-reservations-first"|"none"|"default",
  "CapacityReservationTarget": {
    "CapacityReservationIds": ["string", ...],
    "CapacityReservationResourceGroupArns": ["string", ...]
  }
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To update the size limits of an Auto Scaling group**

This example updates the specified Auto Scaling group with a minimum size of 2 and a maximum size of 10.

```
aws autoscaling update-auto-scaling-group \
    --auto-scaling-group-name my-asg \
    --min-size 2 \
    --max-size 10
```

This command produces no output.

For more information, see [Setting capacity limits for your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-capacity-limits.html) in the *Amazon EC2 Auto Scaling User Guide*.

**Example 2: To add Elastic Load Balancing health checks and specify which Availability Zones and subnets to use**

This example updates the specified Auto Scaling group to add Elastic Load Balancing health checks. This command also updates the value of `--vpc-zone-identifier` with a list of subnet IDs in multiple Availability Zones.

```
aws autoscaling update-auto-scaling-group \
    --auto-scaling-group-name my-asg \
    --health-check-type ELB \
    --health-check-grace-period 600 \
    --vpc-zone-identifier "subnet-5ea0c127,subnet-6194ea3b,subnet-c934b782"
```

This command produces no output.

For more information, see [Elastic Load Balancing and Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html) in the *Amazon EC2 Auto Scaling User Guide*.

**Example 3: To update the placement group and termination policy**

This example updates the placement group and termination policy to use.

```
aws autoscaling update-auto-scaling-group \
    --auto-scaling-group-name my-asg \
    --placement-group my-placement-group \
    --termination-policies "OldestInstance"
```

This command produces no output.

For more information, see [Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html) in the *Amazon EC2 Auto Scaling User Guide*.

**Example 4: To use the latest version of the launch template**

This example updates the specified Auto Scaling group to use the latest version of the specified launch template.

```
aws autoscaling update-auto-scaling-group \
    --auto-scaling-group-name my-asg \
    --launch-template LaunchTemplateId=lt-1234567890abcde12,Version='$Latest'
```

This command produces no output.

For more information, see [Launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/LaunchTemplates.html) in the *Amazon EC2 Auto Scaling User Guide*.

**Example 5: To use a specific version of the launch template**

This example updates the specified Auto Scaling group to use a specific version of a launch template instead of the latest or default version.

```
aws autoscaling update-auto-scaling-group \
    --auto-scaling-group-name my-asg \
    --launch-template LaunchTemplateName=my-template-for-auto-scaling,Version='2'
```

This command produces no output.

For more information, see [Launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/LaunchTemplates.html) in the *Amazon EC2 Auto Scaling User Guide*.

**Example 6: To define a mixed instances policy and enable capacity rebalancing**

This example updates the specified Auto Scaling group to use a mixed instances policy and enables capacity rebalancing. This structure lets you specify groups with Spot and On-Demand capacities and use different launch templates for different architectures.

```
aws autoscaling update-auto-scaling-group \
    --cli-input-json file://~/config.json
```

Contents of `config.json`:

```
{
    "AutoScalingGroupName": "my-asg",
    "CapacityRebalance": true,
    "MixedInstancesPolicy": {
        "LaunchTemplate": {
            "LaunchTemplateSpecification": {
                "LaunchTemplateName": "my-launch-template-for-x86",
                "Version": "$Latest"
            },
            "Overrides": [
                {
                    "InstanceType": "c6g.large",
                    "LaunchTemplateSpecification": {
                        "LaunchTemplateName": "my-launch-template-for-arm",
                        "Version": "$Latest"
                    }
                },
                {
                    "InstanceType": "c5.large"
                },
                {
                    "InstanceType": "c5a.large"
                }
            ]
        },
        "InstancesDistribution": {
            "OnDemandPercentageAboveBaseCapacity": 50,
            "SpotAllocationStrategy": "capacity-optimized"
        }
    }
}
```

This command produces no output.

For more information, see [Auto Scaling groups with multiple instance types and purchase options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Output

None