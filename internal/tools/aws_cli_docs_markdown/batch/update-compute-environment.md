# update-compute-environmentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/update-compute-environment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/update-compute-environment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [batch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/index.html#cli-aws-batch) ]

# update-compute-environment

## Description

Updates an Batch compute environment.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/UpdateComputeEnvironment)

## Synopsis

```
update-compute-environment
--compute-environment <value>
[--state <value>]
[--unmanagedv-cpus <value>]
[--compute-resources <value>]
[--service-role <value>]
[--update-policy <value>]
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

`--compute-environment` (string)

The name or full Amazon Resource Name (ARN) of the compute environment to update.

`--state` (string)

The state of the compute environment. Compute environments in the `ENABLED` state can accept jobs from a queue and scale in or out automatically based on the workload demand of its associated queues.

If the state is `ENABLED` , then the Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically, based on the job queue demand.

If the state is `DISABLED` , then the Batch scheduler doesnât attempt to place jobs within the environment. Jobs in a `STARTING` or `RUNNING` state continue to progress normally. Managed compute environments in the `DISABLED` state donât scale out.

### Note

Compute environments in a `DISABLED` state may continue to incur billing charges. To prevent additional charges, turn off and then delete the compute environment. For more information, see [State](https://docs.aws.amazon.com/batch/latest/userguide/compute_environment_parameters.html#compute_environment_state) in the *Batch User Guide* .

When an instance is idle, the instance scales down to the `minvCpus` value. However, the instance size doesnât change. For example, consider a `c5.8xlarge` instance with a `minvCpus` value of `4` and a `desiredvCpus` value of `36` . This instance doesnât scale down to a `c5.large` instance.

Possible values:

- `ENABLED`
- `DISABLED`

`--unmanagedv-cpus` (integer)

The maximum number of vCPUs expected to be used for an unmanaged compute environment. Donât specify this parameter for a managed compute environment. This parameter is only used for fair-share scheduling to reserve vCPU capacity for new share identifiers. If this parameter isnât provided for a fair-share job queue, no vCPU capacity is reserved.

`--compute-resources` (structure)

Details of the compute resources managed by the compute environment. Required for a managed compute environment. For more information, see [Compute Environments](https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html) in the *Batch User Guide* .

minvCpus -> (integer)

The minimum number of vCPUs that an environment should maintain (even if the compute environment is `DISABLED` ).

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât specify it.

maxvCpus -> (integer)

The maximum number of Amazon EC2 vCPUs that an environment can reach.

### Note

With `BEST_FIT_PROGRESSIVE` ,``SPOT_CAPACITY_OPTIMIZED`` and `SPOT_PRICE_CAPACITY_OPTIMIZED` (recommended) strategies using On-Demand or Spot Instances, and the `BEST_FIT` strategy using Spot Instances, Batch might need to exceed `maxvCpus` to meet your capacity requirements. In this event, Batch never exceeds `maxvCpus` by more than a single instance.

desiredvCpus -> (integer)

The desired number of vCPUS in the compute environment. Batch modifies this value between the minimum and maximum values based on job queue demand.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât specify it.

### Note

Batch doesnât support changing the desired number of vCPUs of an existing compute environment. Donât specify this parameter for compute environments using Amazon EKS clusters.

### Note

When you update the `desiredvCpus` setting, the value must be between the `minvCpus` and `maxvCpus` values.

Additionally, the updated `desiredvCpus` value must be greater than or equal to the current `desiredvCpus` value. For more information, see [Troubleshooting Batch](https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#error-desired-vcpus-update) in the *Batch User Guide* .

subnets -> (list)

The VPC subnets where the compute resources are launched. Fargate compute resources can contain up to 16 subnets. For Fargate compute resources, providing an empty list will be handled as if this parameter wasnât specified and no change is made. For Amazon EC2 compute resources, providing an empty list removes the VPC subnets from the compute resource. For more information, see [VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) in the *Amazon VPC User Guide* .

When updating a compute environment, changing the VPC subnets requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *Batch User Guide* .

### Note

Batch on Amazon EC2 and Batch on Amazon EKS support Local Zones. For more information, see [Local Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-local-zones) in the *Amazon EC2 User Guide for Linux Instances* , [Amazon EKS and Amazon Web Services Local Zones](https://docs.aws.amazon.com/eks/latest/userguide/local-zones.html) in the *Amazon EKS User Guide* and [Amazon ECS clusters in Local Zones, Wavelength Zones, and Amazon Web Services Outposts](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-regions-zones.html#clusters-local-zones) in the *Amazon ECS Developer Guide* .

Batch on Fargate doesnât currently support Local Zones.

(string)

securityGroupIds -> (list)

The Amazon EC2 security groups that are associated with instances launched in the compute environment. This parameter is required for Fargate compute resources, where it can contain up to 5 security groups. For Fargate compute resources, providing an empty list is handled as if this parameter wasnât specified and no change is made. For Amazon EC2 compute resources, providing an empty list removes the security groups from the compute resource.

When updating a compute environment, changing the Amazon EC2 security groups requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *Batch User Guide* .

(string)

allocationStrategy -> (string)

The allocation strategy to use for the compute resource if thereâs not enough instances of the best fitting instance type that can be allocated. This might be because of availability of the instance type in the Region or [Amazon EC2 service limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) . For more information, see [Allocation strategies](https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html) in the *Batch User Guide* .

When updating a compute environment, changing the allocation strategy requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *Batch User Guide* . `BEST_FIT` isnât supported when updating a compute environment.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât specify it.

BEST_FIT_PROGRESSIVE

Batch selects additional instance types that are large enough to meet the requirements of the jobs in the queue. Its preference is for instance types with lower cost vCPUs. If additional instances of the previously selected instance types arenât available, Batch selects new instance types.

SPOT_CAPACITY_OPTIMIZED

Batch selects one or more instance types that are large enough to meet the requirements of the jobs in the queue. Its preference is for instance types that are less likely to be interrupted. This allocation strategy is only available for Spot Instance compute resources.

SPOT_PRICE_CAPACITY_OPTIMIZED

The price and capacity optimized allocation strategy looks at both price and capacity to select the Spot Instance pools that are the least likely to be interrupted and have the lowest possible price. This allocation strategy is only available for Spot Instance compute resources.

With `BEST_FIT_PROGRESSIVE` ,``SPOT_CAPACITY_OPTIMIZED`` and `SPOT_PRICE_CAPACITY_OPTIMIZED` (recommended) strategies using On-Demand or Spot Instances, and the `BEST_FIT` strategy using Spot Instances, Batch might need to exceed `maxvCpus` to meet your capacity requirements. In this event, Batch never exceeds `maxvCpus` by more than a single instance.

instanceTypes -> (list)

The instances types that can be launched. You can specify instance families to launch any instance type within those families (for example, `c5` or `p3` ), or you can specify specific sizes within a family (such as `c5.8xlarge` ). You can also choose `optimal` to select instance types (from the C4, M4, and R4 instance families) that match the demand of your job queues.

When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *Batch User Guide* .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât specify it.

### Note

When you create a compute environment, the instance types that you select for the compute environment must share the same architecture. For example, you canât mix x86 and ARM instances in the same compute environment.

### Note

Currently, `optimal` uses instance types from the C4, M4, and R4 instance families. In Regions that donât have instance types from those instance families, instance types from the C5, M5, and R5 instance families are used.

(string)

ec2KeyPair -> (string)

The Amazon EC2 key pair thatâs used for instances launched in the compute environment. You can use this key pair to log in to your instances with SSH. To remove the Amazon EC2 key pair, set this value to an empty string.

When updating a compute environment, changing the Amazon EC2 key pair requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *Batch User Guide* .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât specify it.

instanceRole -> (string)

The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment. Required for Amazon EC2 instances. You can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For example, `` *ecsInstanceRole* `` or [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/update-compute-environment.html#id1)arn:aws:iam::*<aws_account_id>* :instance-profile/*ecsInstanceRole* `` . For more information, see [Amazon ECS instance role](https://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html) in the *Batch User Guide* .

When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *Batch User Guide* .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât specify it.

tags -> (map)

Key-value pair tags to be applied to Amazon EC2 resources that are launched in the compute environment. For Batch, these take the form of `"String1": "String2"` , where `String1` is the tag key and `String2` is the tag value (for example, `{ "Name": "Batch Instance - C4OnDemand" }` ). This is helpful for recognizing your Batch instances in the Amazon EC2 console. These tags arenât seen when using the Batch `ListTagsForResource` API operation.

When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *Batch User Guide* .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât specify it.

key -> (string)

value -> (string)

placementGroup -> (string)

The Amazon EC2 placement group to associate with your compute resources. If you intend to submit multi-node parallel jobs to your compute environment, you should consider creating a cluster placement group and associate it with your compute resources. This keeps your multi-node parallel job on a logical grouping of instances within a single Availability Zone with high network flow potential. For more information, see [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in the *Amazon EC2 User Guide for Linux Instances* .

When updating a compute environment, changing the placement group requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *Batch User Guide* .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât specify it.

bidPercentage -> (integer)

The maximum percentage that a Spot Instance price can be when compared with the On-Demand price for that instance type before instances are launched. For example, if your maximum percentage is 20%, the Spot price must be less than 20% of the current On-Demand price for that Amazon EC2 instance. You always pay the lowest (market) price and never more than your maximum percentage. For most use cases, we recommend leaving this field empty.

When updating a compute environment, changing the bid percentage requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *Batch User Guide* .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât specify it.

launchTemplate -> (structure)

The updated launch template to use for your compute resources. You must specify either the launch template ID or launch template name in the request, but not both. For more information, see [Launch template support](https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html) in the *Batch User Guide* . To remove the custom launch template and use the default launch template, set `launchTemplateId` or `launchTemplateName` member of the launch template specification to an empty string. Removing the launch template from a compute environment will not remove the AMI specified in the launch template. In order to update the AMI specified in a launch template, the `updateToLatestImageVersion` parameter must be set to `true` .

When updating a compute environment, changing the launch template requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *Batch User Guide* .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât specify it.

launchTemplateId -> (string)

The ID of the launch template.

launchTemplateName -> (string)

The name of the launch template.

version -> (string)

The version number of the launch template, `$Default` , or `$Latest` .

If the value is `$Default` , the default version of the launch template is used. If the value is `$Latest` , the latest version of the launch template is used.

### Warning

If the AMI ID thatâs used in a compute environment is from the launch template, the AMI isnât changed when the compute environment is updated. Itâs only changed if the `updateToLatestImageVersion` parameter for the compute environment is set to `true` . During an infrastructure update, if either `$Default` or `$Latest` is specified, Batch re-evaluates the launch template version, and it might use a different version of the launch template. This is the case even if the launch template isnât specified in the update. When updating a compute environment, changing the launch template requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *Batch User Guide* .

Default: `$Default`

Latest: `$Latest`

overrides -> (list)

A launch template to use in place of the default launch template. You must specify either the launch template ID or launch template name in the request, but not both.

You can specify up to ten (10) launch template overrides that are associated to unique instance types or families for each compute environment.

### Note

To unset all override templates for a compute environment, you can pass an empty array to the [UpdateComputeEnvironment.overrides](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateComputeEnvironment.html) parameter, or not include the `overrides` parameter when submitting the `UpdateComputeEnvironment` API operation.

(structure)

An object that represents a launch template to use in place of the default launch template. You must specify either the launch template ID or launch template name in the request, but not both.

If security groups are specified using both the `securityGroupIds` parameter of `CreateComputeEnvironment` and the launch template, the values in the `securityGroupIds` parameter of `CreateComputeEnvironment` will be used.

You can define up to ten (10) overrides for each compute environment.

### Note

This object isnât applicable to jobs that are running on Fargate resources.

### Note

To unset all override templates for a compute environment, you can pass an empty array to the [UpdateComputeEnvironment.overrides](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateComputeEnvironment.html) parameter, or not include the `overrides` parameter when submitting the `UpdateComputeEnvironment` API operation.

launchTemplateId -> (string)

The ID of the launch template.

**Note:** If you specify the `launchTemplateId` you canât specify the `launchTemplateName` as well.

launchTemplateName -> (string)

The name of the launch template.

**Note:** If you specify the `launchTemplateName` you canât specify the `launchTemplateId` as well.

version -> (string)

The version number of the launch template, `$Default` , or `$Latest` .

If the value is `$Default` , the default version of the launch template is used. If the value is `$Latest` , the latest version of the launch template is used.

### Warning

If the AMI ID thatâs used in a compute environment is from the launch template, the AMI isnât changed when the compute environment is updated. Itâs only changed if the `updateToLatestImageVersion` parameter for the compute environment is set to `true` . During an infrastructure update, if either `$Default` or `$Latest` is specified, Batch re-evaluates the launch template version, and it might use a different version of the launch template. This is the case even if the launch template isnât specified in the update. When updating a compute environment, changing the launch template requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *Batch User Guide* .

Default: `$Default`

Latest: `$Latest`

targetInstanceTypes -> (list)

The instance type or family that this override launch template should be applied to.

This parameter is required when defining a launch template override.

Information included in this parameter must meet the following requirements:

- Must be a valid Amazon EC2 instance type or family.
- `optimal` isnât allowed.
- `targetInstanceTypes` can target only instance types and families that are included within the ` `ComputeResource.instanceTypes` [https://docs.aws.amazon.com/batch/latest/APIReference/API_ComputeResource.html#Batch-Type-ComputeResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_ComputeResource.html#Batch-Type-ComputeResource)-instanceTypes`__ set. `targetInstanceTypes` doesnât need to include all of the instances from the `instanceType` set, but at least a subset. For example, if `ComputeResource.instanceTypes` includes `[m5, g5]` , `targetInstanceTypes` can include `[m5.2xlarge]` and `[m5.large]` but not `[c5.large]` .
- `targetInstanceTypes` included within the same launch template override or across launch template overrides canât overlap for the same compute environment. For example, you canât define one launch template override to target an instance family and another define an instance type within this same family.

(string)

ec2Configuration -> (list)

Provides information used to select Amazon Machine Images (AMIs) for Amazon EC2 instances in the compute environment. If `Ec2Configuration` isnât specified, the default is `ECS_AL2` .

When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *Batch User Guide* . To remove the Amazon EC2 configuration and any custom AMI ID specified in `imageIdOverride` , set this value to an empty string.

One or two values can be provided.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât specify it.

(structure)

Provides information used to select Amazon Machine Images (AMIs) for instances in the compute environment. If `Ec2Configuration` isnât specified, the default is `ECS_AL2` ([Amazon Linux 2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#al2ami) ).

### Note

This object isnât applicable to jobs that are running on Fargate resources.

imageType -> (string)

The image type to match with the instance type to select an AMI. The supported values are different for `ECS` and `EKS` resources.

ECS

If the `imageIdOverride` parameter isnât specified, then a recent [Amazon ECS-optimized Amazon Linux 2 AMI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#al2ami) (`ECS_AL2` ) is used. If a new image type is specified in an update, but neither an `imageId` nor a `imageIdOverride` parameter is specified, then the latest Amazon ECS optimized AMI for that image type thatâs supported by Batch is used.

ECS_AL2

[Amazon Linux 2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#al2ami) : Default for all non-GPU instance families.

ECS_AL2_NVIDIA

[Amazon Linux 2 (GPU)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#gpuami) : Default for all GPU instance families (for example `P4` and `G4` ) and can be used for all non Amazon Web Services Graviton-based instance types.

ECS_AL2023

[Amazon Linux 2023](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html) : Batch supports Amazon Linux 2023.

### Note

Amazon Linux 2023 does not support `A1` instances.

ECS_AL1

[Amazon Linux](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#alami) . Amazon Linux has reached the end-of-life of standard support. For more information, see [Amazon Linux AMI](http://aws.amazon.com/amazon-linux-ami/) .

EKS

If the `imageIdOverride` parameter isnât specified, then a recent [Amazon EKS-optimized Amazon Linux AMI](https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html) (`EKS_AL2` ) is used. If a new image type is specified in an update, but neither an `imageId` nor a `imageIdOverride` parameter is specified, then the latest Amazon EKS optimized AMI for that image type that Batch supports is used.

EKS_AL2

[Amazon Linux 2](https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html) : Default for all non-GPU instance families.

EKS_AL2_NVIDIA

[Amazon Linux 2 (accelerated)](https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html) : Default for all GPU instance families (for example, `P4` and `G4` ) and can be used for all non Amazon Web Services Graviton-based instance types.

imageIdOverride -> (string)

The AMI ID used for instances launched in the compute environment that match the image type. This setting overrides the `imageId` set in the `computeResource` object.

### Note

The AMI that you choose for a compute environment must match the architecture of the instance types that you intend to use for that compute environment. For example, if your compute environment uses A1 instance types, the compute resource AMI that you choose must support ARM instances. Amazon ECS vends both x86 and ARM versions of the Amazon ECS-optimized Amazon Linux 2 AMI. For more information, see [Amazon ECS-optimized Amazon Linux 2 AMI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#ecs-optimized-ami-linux-variants.html) in the *Amazon Elastic Container Service Developer Guide* .

imageKubernetesVersion -> (string)

The Kubernetes version for the compute environment. If you donât specify a value, the latest version that Batch supports is used.

updateToLatestImageVersion -> (boolean)

Specifies whether the AMI ID is updated to the latest one thatâs supported by Batch when the compute environment has an infrastructure update. The default value is `false` .

### Note

An AMI ID can either be specified in the `imageId` or `imageIdOverride` parameters or be determined by the launch template thatâs specified in the `launchTemplate` parameter. If an AMI ID is specified any of these ways, this parameter is ignored. For more information about to update AMI IDs during an infrastructure update, see [Updating the AMI ID](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html#updating-compute-environments-ami) in the *Batch User Guide* .

When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *Batch User Guide* .

type -> (string)

The type of compute environment: `EC2` , `SPOT` , `FARGATE` , or `FARGATE_SPOT` . For more information, see [Compute environments](https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html) in the *Batch User Guide* .

If you choose `SPOT` , you must also specify an Amazon EC2 Spot Fleet role with the `spotIamFleetRole` parameter. For more information, see [Amazon EC2 spot fleet role](https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html) in the *Batch User Guide* .

When updating a compute environment, changing the type of a compute environment requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *Batch User Guide* .

imageId -> (string)

The Amazon Machine Image (AMI) ID used for instances launched in the compute environment. This parameter is overridden by the `imageIdOverride` member of the `Ec2Configuration` structure. To remove the custom AMI ID and use the default AMI ID, set this value to an empty string.

When updating a compute environment, changing the AMI ID requires an infrastructure update of the compute environment. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *Batch User Guide* .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât specify it.

### Note

The AMI that you choose for a compute environment must match the architecture of the instance types that you intend to use for that compute environment. For example, if your compute environment uses A1 instance types, the compute resource AMI that you choose must support ARM instances. Amazon ECS vends both x86 and ARM versions of the Amazon ECS-optimized Amazon Linux 2 AMI. For more information, see [Amazon ECS-optimized Amazon Linux 2 AMI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#ecs-optimized-ami-linux-variants.html) in the *Amazon Elastic Container Service Developer Guide* .

JSON Syntax:

```
{
  "minvCpus": integer,
  "maxvCpus": integer,
  "desiredvCpus": integer,
  "subnets": ["string", ...],
  "securityGroupIds": ["string", ...],
  "allocationStrategy": "BEST_FIT_PROGRESSIVE"|"SPOT_CAPACITY_OPTIMIZED"|"SPOT_PRICE_CAPACITY_OPTIMIZED",
  "instanceTypes": ["string", ...],
  "ec2KeyPair": "string",
  "instanceRole": "string",
  "tags": {"string": "string"
    ...},
  "placementGroup": "string",
  "bidPercentage": integer,
  "launchTemplate": {
    "launchTemplateId": "string",
    "launchTemplateName": "string",
    "version": "string",
    "overrides": [
      {
        "launchTemplateId": "string",
        "launchTemplateName": "string",
        "version": "string",
        "targetInstanceTypes": ["string", ...]
      }
      ...
    ]
  },
  "ec2Configuration": [
    {
      "imageType": "string",
      "imageIdOverride": "string",
      "imageKubernetesVersion": "string"
    }
    ...
  ],
  "updateToLatestImageVersion": true|false,
  "type": "EC2"|"SPOT"|"FARGATE"|"FARGATE_SPOT",
  "imageId": "string"
}
```

`--service-role` (string)

The full Amazon Resource Name (ARN) of the IAM role that allows Batch to make calls to other Amazon Web Services services on your behalf. For more information, see [Batch service IAM role](https://docs.aws.amazon.com/batch/latest/userguide/service_IAM_role.html) in the *Batch User Guide* .

### Warning

If the compute environment has a service-linked role, it canât be changed to use a regular IAM role. Likewise, if the compute environment has a regular IAM role, it canât be changed to use a service-linked role. To update the parameters for the compute environment that require an infrastructure update to change, the **AWSServiceRoleForBatch** service-linked role must be used. For more information, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *Batch User Guide* .

If your specified role has a path other than `/` , then you must either specify the full role ARN (recommended) or prefix the role name with the path.

### Note

Depending on how you created your Batch service role, its ARN might contain the `service-role` path prefix. When you only specify the name of the service role, Batch assumes that your ARN doesnât use the `service-role` path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.

`--update-policy` (structure)

Specifies the updated infrastructure update policy for the compute environment. For more information about infrastructure updates, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *Batch User Guide* .

terminateJobsOnUpdate -> (boolean)

Specifies whether jobs are automatically terminated when the computer environment infrastructure is updated. The default value is `false` .

jobExecutionTimeoutMinutes -> (long)

Specifies the job timeout (in minutes) when the compute environment infrastructure is updated. The default value is 30.

Shorthand Syntax:

```
terminateJobsOnUpdate=boolean,jobExecutionTimeoutMinutes=long
```

JSON Syntax:

```
{
  "terminateJobsOnUpdate": true|false,
  "jobExecutionTimeoutMinutes": long
}
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

**To update a compute environment**

This example disables the P2OnDemand compute environment so it can be deleted.

Command:

```
aws batch update-compute-environment --compute-environment P2OnDemand --state DISABLED
```

Output:

```
{
    "computeEnvironmentName": "P2OnDemand",
    "computeEnvironmentArn": "arn:aws:batch:us-east-1:012345678910:compute-environment/P2OnDemand"
}
```

## Output

computeEnvironmentName -> (string)

The name of the compute environment. It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).

computeEnvironmentArn -> (string)

The Amazon Resource Name (ARN) of the compute environment.