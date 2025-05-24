# register-job-definitionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/register-job-definition.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/register-job-definition.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [batch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/index.html#cli-aws-batch) ]

# register-job-definition

## Description

Registers an Batch job definition.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/RegisterJobDefinition)

## Synopsis

```
register-job-definition
--job-definition-name <value>
--type <value>
[--parameters <value>]
[--scheduling-priority <value>]
[--container-properties <value>]
[--node-properties <value>]
[--retry-strategy <value>]
[--propagate-tags | --no-propagate-tags]
[--timeout <value>]
[--tags <value>]
[--platform-capabilities <value>]
[--eks-properties <value>]
[--ecs-properties <value>]
[--consumable-resource-properties <value>]
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

`--job-definition-name` (string)

The name of the job definition to register. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).

`--type` (string)

The type of job definition. For more information about multi-node parallel jobs, see [Creating a multi-node parallel job definition](https://docs.aws.amazon.com/batch/latest/userguide/multi-node-job-def.html) in the *Batch User Guide* .

- If the value is `container` , then one of the following is required: `containerProperties` , `ecsProperties` , or `eksProperties` .
- If the value is `multinode` , then `nodeProperties` is required.

### Note

If the job is run on Fargate resources, then `multinode` isnât supported.

Possible values:

- `container`
- `multinode`

`--parameters` (map)

Default parameter substitution placeholders to set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a `SubmitJob` request override any corresponding parameter defaults from the job definition.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--scheduling-priority` (integer)

The scheduling priority for jobs that are submitted with this job definition. This only affects jobs in job queues with a fair-share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.

The minimum supported value is 0 and the maximum supported value is 9999.

`--container-properties` (structure)

An object with properties specific to Amazon ECS-based single-node container-based jobs. If the job definitionâs `type` parameter is `container` , then you must specify either `containerProperties` or `nodeProperties` . This must not be specified for Amazon EKS-based job definitions.

### Note

If the job runs on Fargate resources, then you must not specify `nodeProperties` ; use only `containerProperties` .

image -> (string)

Required. The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `` *repository-url* /*image* :*tag* `` . It can be 255 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), underscores (_), colons (:), periods (.), forward slashes (/), and number signs (#). This parameter maps to `Image` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `IMAGE` parameter of [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

Docker image architecture must match the processor architecture of the compute resources that theyâre scheduled on. For example, ARM-based Docker images can only run on ARM-based compute resources.

- Images in Amazon ECR Public repositories use the full `registry/repository[:tag]` or `registry/repository[@digest]` naming conventions. For example, [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/register-job-definition.html#id1)public.ecr.aws/*registry_alias* /*my-web-app* :*latest* `` .
- Images in Amazon ECR repositories use the full registry and repository URI (for example, `123456789012.dkr.ecr.<region-name>.amazonaws.com/<repository-name>` ).
- Images in official repositories on Docker Hub use a single name (for example, `ubuntu` or `mongo` ).
- Images in other repositories on Docker Hub are qualified with an organization name (for example, `amazon/amazon-ecs-agent` ).
- Images in other online repositories are qualified further by a domain name (for example, `quay.io/assemblyline/ubuntu` ).

vcpus -> (integer)

This parameter is deprecated, use `resourceRequirements` to specify the vCPU requirements for the job definition. Itâs not supported for jobs running on Fargate resources. For jobs running on Amazon EC2 resources, it specifies the number of vCPUs reserved for the job.

Each vCPU is equivalent to 1,024 CPU shares. This parameter maps to `CpuShares` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--cpu-shares` option to [docker run](https://docs.docker.com/engine/reference/run/) . The number of vCPUs must be specified but can be specified in several places. You must specify it at least once for each node.

memory -> (integer)

This parameter is deprecated, use `resourceRequirements` to specify the memory requirements for the job definition. Itâs not supported for jobs running on Fargate resources. For jobs that run on Amazon EC2 resources, it specifies the memory hard limit (in MiB) for a container. If your container attempts to exceed the specified number, itâs terminated. You must specify at least 4 MiB of memory for a job using this parameter. The memory hard limit can be specified in several places. It must be specified for each node at least once.

command -> (list)

The command thatâs passed to the container. This parameter maps to `Cmd` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `COMMAND` parameter to [docker run](https://docs.docker.com/engine/reference/run/) . For more information, see [https://docs.docker.com/engine/reference/builder/#cmd](https://docs.docker.com/engine/reference/builder/#cmd) .

(string)

jobRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that the container can assume for Amazon Web Services permissions. For more information, see [IAM roles for tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide* .

executionRoleArn -> (string)

The Amazon Resource Name (ARN) of the execution role that Batch can assume. For jobs that run on Fargate resources, you must provide an execution role. For more information, see [Batch execution IAM role](https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html) in the *Batch User Guide* .

volumes -> (list)

A list of data volumes used in a job.

(structure)

A data volume thatâs used in a jobâs container properties.

host -> (structure)

The contents of the `host` parameter determine whether your data volume persists on the host container instance and where itâs stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data isnât guaranteed to persist after the containers that are associated with it stop running.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources and shouldnât be provided.

sourcePath -> (string)

The path on the host container instance thatâs presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If this parameter contains a file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the source path location doesnât exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.

### Note

This parameter isnât applicable to jobs that run on Fargate resources. Donât provide this for these jobs.

name -> (string)

The name of the volume. It can be up to 255 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_). This name is referenced in the `sourceVolume` parameter of container definition `mountPoints` .

efsVolumeConfiguration -> (structure)

This parameter is specified when youâre using an Amazon Elastic File System file system for job storage. Jobs that are running on Fargate resources must specify a `platformVersion` of at least `1.4.0` .

fileSystemId -> (string)

The Amazon EFS file system ID to use.

rootDirectory -> (string)

The directory within the Amazon EFS file system to mount as the root directory inside the host. If this parameter is omitted, the root of the Amazon EFS volume is used instead. Specifying `/` has the same effect as omitting this parameter. The maximum length is 4,096 characters.

### Warning

If an EFS access point is specified in the `authorizationConfig` , the root directory parameter must either be omitted or set to `/` , which enforces the path set on the Amazon EFS access point.

transitEncryption -> (string)

Determines whether to enable encryption for Amazon EFS data in transit between the Amazon ECS host and the Amazon EFS server. Transit encryption must be enabled if Amazon EFS IAM authorization is used. If this parameter is omitted, the default value of `DISABLED` is used. For more information, see [Encrypting data in transit](https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html) in the *Amazon Elastic File System User Guide* .

transitEncryptionPort -> (integer)

The port to use when sending encrypted data between the Amazon ECS host and the Amazon EFS server. If you donât specify a transit encryption port, it uses the port selection strategy that the Amazon EFS mount helper uses. The value must be between 0 and 65,535. For more information, see [EFS mount helper](https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html) in the *Amazon Elastic File System User Guide* .

authorizationConfig -> (structure)

The authorization configuration details for the Amazon EFS file system.

accessPointId -> (string)

The Amazon EFS access point ID to use. If an access point is specified, the root directory value specified in the `EFSVolumeConfiguration` must either be omitted or set to `/` which enforces the path set on the EFS access point. If an access point is used, transit encryption must be enabled in the `EFSVolumeConfiguration` . For more information, see [Working with Amazon EFS access points](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html) in the *Amazon Elastic File System User Guide* .

iam -> (string)

Whether or not to use the Batch job IAM role defined in a job definition when mounting the Amazon EFS file system. If enabled, transit encryption must be enabled in the `EFSVolumeConfiguration` . If this parameter is omitted, the default value of `DISABLED` is used. For more information, see [Using Amazon EFS access points](https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html#efs-volume-accesspoints) in the *Batch User Guide* . EFS IAM authorization requires that `TransitEncryption` be `ENABLED` and that a `JobRoleArn` is specified.

environment -> (list)

The environment variables to pass to a container. This parameter maps to `Env` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--env` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Warning

We donât recommend using plaintext environment variables for sensitive information, such as credential data.

### Note

Environment variables cannot start with â`AWS_BATCH` â. This naming convention is reserved for variables that Batch sets.

(structure)

A key-value pair object.

name -> (string)

The name of the key-value pair. For environment variables, this is the name of the environment variable.

value -> (string)

The value of the key-value pair. For environment variables, this is the value of the environment variable.

mountPoints -> (list)

The mount points for data volumes in your container. This parameter maps to `Volumes` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--volume` option to [docker run](https://docs.docker.com/engine/reference/run/) .

(structure)

Details for a Docker volume mount point thatâs used in a jobâs container properties. This parameter maps to `Volumes` in the [Create a container](https://docs.docker.com/engine/api/v1.43/#tag/Container/operation/ContainerCreate) section of the *Docker Remote API* and the `--volume` option to docker run.

containerPath -> (string)

The path on the container where the host volume is mounted.

readOnly -> (boolean)

If this value is `true` , the container has read-only access to the volume. Otherwise, the container can write to the volume. The default value is `false` .

sourceVolume -> (string)

The name of the volume to mount.

readonlyRootFilesystem -> (boolean)

When this parameter is true, the container is given read-only access to its root file system. This parameter maps to `ReadonlyRootfs` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--read-only` option to `docker run` .

privileged -> (boolean)

When this parameter is true, the container is given elevated permissions on the host container instance (similar to the `root` user). This parameter maps to `Privileged` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--privileged` option to [docker run](https://docs.docker.com/engine/reference/run/) . The default value is false.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources and shouldnât be provided, or specified as false.

ulimits -> (list)

A list of `ulimits` to set in the container. This parameter maps to `Ulimits` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--ulimit` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources and shouldnât be provided.

(structure)

The `ulimit` settings to pass to the container. For more information, see [Ulimit](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Ulimit.html) .

### Note

This object isnât applicable to jobs that are running on Fargate resources.

hardLimit -> (integer)

The hard limit for the `ulimit` type.

name -> (string)

The `type` of the `ulimit` . Valid values are: `core` | `cpu` | `data` | `fsize` | `locks` | `memlock` | `msgqueue` | `nice` | `nofile` | `nproc` | `rss` | `rtprio` | `rttime` | `sigpending` | `stack` .

softLimit -> (integer)

The soft limit for the `ulimit` type.

user -> (string)

The user name to use inside the container. This parameter maps to `User` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--user` option to [docker run](https://docs.docker.com/engine/reference/run/) .

instanceType -> (string)

The instance type to use for a multi-node parallel job. All node groups in a multi-node parallel job must use the same instance type.

### Note

This parameter isnât applicable to single-node container jobs or jobs that run on Fargate resources, and shouldnât be provided.

resourceRequirements -> (list)

The type and amount of resources to assign to a container. The supported resources include `GPU` , `MEMORY` , and `VCPU` .

(structure)

The type and amount of a resource to assign to a container. The supported resources include `GPU` , `MEMORY` , and `VCPU` .

value -> (string)

The quantity of the specified resource to reserve for the container. The values vary based on the `type` specified.

type=âGPUâ

The number of physical GPUs to reserve for the container. Make sure that the number of GPUs reserved for all containers in a job doesnât exceed the number of available GPUs on the compute resource that the job is launched on.

### Note

GPUs arenât available for jobs that are running on Fargate resources.

type=âMEMORYâ

The memory hard limit (in MiB) present to the container. This parameter is supported for jobs that are running on Amazon EC2 resources. If your container attempts to exceed the memory specified, the container is terminated. This parameter maps to `Memory` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--memory` option to [docker run](https://docs.docker.com/engine/reference/run/) . You must specify at least 4 MiB of memory for a job. This is required but can be specified in several places for multi-node parallel (MNP) jobs. It must be specified for each node at least once. This parameter maps to `Memory` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--memory` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

If youâre trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see [Memory management](https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html) in the *Batch User Guide* .

For jobs that are running on Fargate resources, then `value` is the hard limit (in MiB), and must match one of the supported values and the `VCPU` values must be one of the values supported for that memory value.

value = 512

`VCPU` = 0.25

value = 1024

`VCPU` = 0.25 or 0.5

value = 2048

`VCPU` = 0.25, 0.5, or 1

value = 3072

`VCPU` = 0.5, or 1

value = 4096

`VCPU` = 0.5, 1, or 2

value = 5120, 6144, or 7168

`VCPU` = 1 or 2

value = 8192

`VCPU` = 1, 2, or 4

value = 9216, 10240, 11264, 12288, 13312, 14336, or 15360

`VCPU` = 2 or 4

value = 16384

`VCPU` = 2, 4, or 8

value = 17408, 18432, 19456, 21504, 22528, 23552, 25600, 26624, 27648, 29696, or 30720

`VCPU` = 4

value = 20480, 24576, or 28672

`VCPU` = 4 or 8

value = 36864, 45056, 53248, or 61440

`VCPU` = 8

value = 32768, 40960, 49152, or 57344

`VCPU` = 8 or 16

value = 65536, 73728, 81920, 90112, 98304, 106496, 114688, or 122880

`VCPU` = 16

type=âVCPUâ

The number of vCPUs reserved for the container. This parameter maps to `CpuShares` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--cpu-shares` option to [docker run](https://docs.docker.com/engine/reference/run/) . Each vCPU is equivalent to 1,024 CPU shares. For Amazon EC2 resources, you must specify at least one vCPU. This is required but can be specified in several places; it must be specified for each node at least once.

The default for the Fargate On-Demand vCPU resource count quota is 6 vCPUs. For more information about Fargate quotas, see [Fargate quotas](https://docs.aws.amazon.com/general/latest/gr/ecs-service.html#service-quotas-fargate) in the *Amazon Web Services General Reference* .

For jobs that are running on Fargate resources, then `value` must match one of the supported values and the `MEMORY` values must be one of the values supported for that `VCPU` value. The supported values are 0.25, 0.5, 1, 2, 4, 8, and 16

value = 0.25

`MEMORY` = 512, 1024, or 2048

value = 0.5

`MEMORY` = 1024, 2048, 3072, or 4096

value = 1

`MEMORY` = 2048, 3072, 4096, 5120, 6144, 7168, or 8192

value = 2

`MEMORY` = 4096, 5120, 6144, 7168, 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, or 16384

value = 4

`MEMORY` = 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, 16384, 17408, 18432, 19456, 20480, 21504, 22528, 23552, 24576, 25600, 26624, 27648, 28672, 29696, or 30720

value = 8

`MEMORY` = 16384, 20480, 24576, 28672, 32768, 36864, 40960, 45056, 49152, 53248, 57344, or 61440

value = 16

`MEMORY` = 32768, 40960, 49152, 57344, 65536, 73728, 81920, 90112, 98304, 106496, 114688, or 122880

type -> (string)

The type of resource to assign to a container. The supported resources include `GPU` , `MEMORY` , and `VCPU` .

linuxParameters -> (structure)

Linux-specific modifications that are applied to the container, such as details for device mappings.

devices -> (list)

Any of the host devices to expose to the container. This parameter maps to `Devices` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--device` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide it for these jobs.

(structure)

An object that represents a container instance host device.

### Note

This object isnât applicable to jobs that are running on Fargate resources and shouldnât be provided.

hostPath -> (string)

The path for the device on the host container instance.

containerPath -> (string)

The path inside the container thatâs used to expose the host device. By default, the `hostPath` value is used.

permissions -> (list)

The explicit permissions to provide to the container for the device. By default, the container has permissions for `read` , `write` , and `mknod` for the device.

(string)

initProcessEnabled -> (boolean)

If true, run an `init` process inside the container that forwards signals and reaps processes. This parameter maps to the `--init` option to [docker run](https://docs.docker.com/engine/reference/run/) . This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`

sharedMemorySize -> (integer)

The value for the size (in MiB) of the `/dev/shm` volume. This parameter maps to the `--shm-size` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide it for these jobs.

tmpfs -> (list)

The container path, mount options, and size (in MiB) of the `tmpfs` mount. This parameter maps to the `--tmpfs` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide this parameter for this resource type.

(structure)

The container path, mount options, and size of the `tmpfs` mount.

### Note

This object isnât applicable to jobs that are running on Fargate resources.

containerPath -> (string)

The absolute file path in the container where the `tmpfs` volume is mounted.

size -> (integer)

The size (in MiB) of the `tmpfs` volume.

mountOptions -> (list)

The list of `tmpfs` volume mount options.

Valid values: â`defaults` â | â`ro` â | â`rw` â | â`suid` â | â`nosuid` â | â`dev` â | â`nodev` â | â`exec` â | â`noexec` â | â`sync` â | â`async` â | â`dirsync` â | â`remount` â | â`mand` â | â`nomand` â | â`atime` â | â`noatime` â | â`diratime` â | â`nodiratime` â | â`bind` â | â`rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime` â | â`norelatime` â | â`strictatime` â | â`nostrictatime` â | â`mode` â | â`uid` â | â`gid` â | â`nr_inodes` â | â`nr_blocks` â | â`mpol` â

(string)

maxSwap -> (integer)

The total amount of swap memory (in MiB) a container can use. This parameter is translated to the `--memory-swap` option to [docker run](https://docs.docker.com/engine/reference/run/) where the value is the sum of the container memory plus the `maxSwap` value. For more information, see ` `--memory-swap` details <[https://docs.docker.com/config/containers/resource_constraints/#âmemory-swap-details](https://docs.docker.com/config/containers/resource_constraints/#--memory-swap-details)>`__ in the Docker documentation.

If a `maxSwap` value of `0` is specified, the container doesnât use swap. Accepted values are `0` or any positive integer. If the `maxSwap` parameter is omitted, the container doesnât use the swap configuration for the container instance on which it runs. A `maxSwap` value must be set for the `swappiness` parameter to be used.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide it for these jobs.

swappiness -> (integer)

You can use this parameter to tune a containerâs memory swappiness behavior. A `swappiness` value of `0` causes swapping to not occur unless absolutely necessary. A `swappiness` value of `100` causes pages to be swapped aggressively. Valid values are whole numbers between `0` and `100` . If the `swappiness` parameter isnât specified, a default value of `60` is used. If a value isnât specified for `maxSwap` , then this parameter is ignored. If `maxSwap` is set to 0, the container doesnât use swap. This parameter maps to the `--memory-swappiness` option to [docker run](https://docs.docker.com/engine/reference/run/) .

Consider the following when you use a per-container swap configuration.

- Swap space must be enabled and allocated on the container instance for the containers to use.

### Note

By default, the Amazon ECS optimized AMIs donât have swap enabled. You must enable swap on the instance to use this feature. For more information, see [Instance store swap volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-swap-volumes.html) in the *Amazon EC2 User Guide for Linux Instances* or [How do I allocate memory to work as swap space in an Amazon EC2 instance by using a swap file?](http://aws.amazon.com/premiumsupport/knowledge-center/ec2-memory-swap-file/)

- The swap space parameters are only supported for job definitions using EC2 resources.
- If the `maxSwap` and `swappiness` parameters are omitted from a job definition, each container has a default `swappiness` value of 60. Moreover, the total swap usage is limited to two times the memory reservation of the container.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide it for these jobs.

logConfiguration -> (structure)

The log configuration specification for the container.

This parameter maps to `LogConfig` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--log-driver` option to [docker run](https://docs.docker.com/engine/reference/run/) . By default, containers use the same logging driver that the Docker daemon uses. However the container might use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see [Configure logging drivers](https://docs.docker.com/engine/admin/logging/overview/) in the Docker documentation.

### Note

Batch currently supports a subset of the logging drivers available to the Docker daemon (shown in the [LogConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html) data type).

This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`

### Note

The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the `ECS_AVAILABLE_LOGGING_DRIVERS` environment variable before containers placed on that instance can use these log configuration options. For more information, see [Amazon ECS container agent configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html) in the *Amazon Elastic Container Service Developer Guide* .

logDriver -> (string)

The log driver to use for the container. The valid values that are listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default.

The supported log drivers are `awslogs` , `fluentd` , `gelf` , `json-file` , `journald` , `logentries` , `syslog` , and `splunk` .

### Note

Jobs that are running on Fargate resources are restricted to the `awslogs` and `splunk` log drivers.

awsfirelens

Specifies the firelens logging driver. For more information on configuring Firelens, see [Send Amazon ECS logs to an Amazon Web Services service or Amazon Web Services Partner](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) in the *Amazon Elastic Container Service Developer Guide* .

awslogs

Specifies the Amazon CloudWatch Logs logging driver. For more information, see [Using the awslogs log driver](https://docs.aws.amazon.com/batch/latest/userguide/using_awslogs.html) in the *Batch User Guide* and [Amazon CloudWatch Logs logging driver](https://docs.docker.com/config/containers/logging/awslogs/) in the Docker documentation.

fluentd

Specifies the Fluentd logging driver. For more information including usage and options, see [Fluentd logging driver](https://docs.docker.com/config/containers/logging/fluentd/) in the *Docker documentation* .

gelf

Specifies the Graylog Extended Format (GELF) logging driver. For more information including usage and options, see [Graylog Extended Format logging driver](https://docs.docker.com/config/containers/logging/gelf/) in the *Docker documentation* .

journald

Specifies the journald logging driver. For more information including usage and options, see [Journald logging driver](https://docs.docker.com/config/containers/logging/journald/) in the *Docker documentation* .

json-file

Specifies the JSON file logging driver. For more information including usage and options, see [JSON File logging driver](https://docs.docker.com/config/containers/logging/json-file/) in the *Docker documentation* .

splunk

Specifies the Splunk logging driver. For more information including usage and options, see [Splunk logging driver](https://docs.docker.com/config/containers/logging/splunk/) in the *Docker documentation* .

syslog

Specifies the syslog logging driver. For more information including usage and options, see [Syslog logging driver](https://docs.docker.com/config/containers/logging/syslog/) in the *Docker documentation* .

### Note

If you have a custom driver thatâs not listed earlier that you want to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project thatâs [available on GitHub](https://github.com/aws/amazon-ecs-agent) and customize it to work with that driver. We encourage you to submit pull requests for changes that you want to have included. However, Amazon Web Services doesnât currently support running modified copies of this software.

This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`

options -> (map)

The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`

key -> (string)

value -> (string)

secretOptions -> (list)

The secrets to pass to the log configuration. For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the *Batch User Guide* .

(structure)

An object that represents the secret to expose to your container. Secrets can be exposed to a container in the following ways:

- To inject sensitive data into your containers as environment variables, use the `secrets` container definition parameter.
- To reference sensitive information in the log configuration of a container, use the `secretOptions` container definition parameter.

For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the *Batch User Guide* .

name -> (string)

The name of the secret.

valueFrom -> (string)

The secret to expose to the container. The supported values are either the full Amazon Resource Name (ARN) of the Secrets Manager secret or the full ARN of the parameter in the Amazon Web Services Systems Manager Parameter Store.

### Note

If the Amazon Web Services Systems Manager Parameter Store parameter exists in the same Region as the job youâre launching, then you can use either the full Amazon Resource Name (ARN) or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.

secrets -> (list)

The secrets for the container. For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the *Batch User Guide* .

(structure)

An object that represents the secret to expose to your container. Secrets can be exposed to a container in the following ways:

- To inject sensitive data into your containers as environment variables, use the `secrets` container definition parameter.
- To reference sensitive information in the log configuration of a container, use the `secretOptions` container definition parameter.

For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the *Batch User Guide* .

name -> (string)

The name of the secret.

valueFrom -> (string)

The secret to expose to the container. The supported values are either the full Amazon Resource Name (ARN) of the Secrets Manager secret or the full ARN of the parameter in the Amazon Web Services Systems Manager Parameter Store.

### Note

If the Amazon Web Services Systems Manager Parameter Store parameter exists in the same Region as the job youâre launching, then you can use either the full Amazon Resource Name (ARN) or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.

networkConfiguration -> (structure)

The network configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.

assignPublicIp -> (string)

Indicates whether the job has a public IP address. For a job thatâs running on Fargate resources in a private subnet to send outbound traffic to the internet (for example, to pull container images), the private subnet requires a NAT gateway be attached to route requests to the internet. For more information, see [Amazon ECS task networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide* . The default value is â`DISABLED` â.

fargatePlatformConfiguration -> (structure)

The platform configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.

platformVersion -> (string)

The Fargate platform version where the jobs are running. A platform version is specified only for jobs that are running on Fargate resources. If one isnât specified, the `LATEST` platform version is used by default. This uses a recent, approved version of the Fargate platform for compute resources. For more information, see [Fargate platform versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide* .

enableExecuteCommand -> (boolean)

Determines whether execute command functionality is turned on for this task. If `true` , execute command functionality is turned on all the containers in the task.

ephemeralStorage -> (structure)

The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on Fargate.

sizeInGiB -> (integer)

The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is `21` GiB and the maximum supported value is `200` GiB.

runtimePlatform -> (structure)

An object that represents the compute environment architecture for Batch jobs on Fargate.

operatingSystemFamily -> (string)

The operating system for the compute environment. Valid values are: `LINUX` (default), `WINDOWS_SERVER_2019_CORE` , `WINDOWS_SERVER_2019_FULL` , `WINDOWS_SERVER_2022_CORE` , and `WINDOWS_SERVER_2022_FULL` .

### Note

The following parameters canât be set for Windows containers: `linuxParameters` , `privileged` , `user` , `ulimits` , `readonlyRootFilesystem` , and `efsVolumeConfiguration` .

### Note

The Batch Scheduler checks the compute environments that are attached to the job queue before registering a task definition with Fargate. In this scenario, the job queue is where the job is submitted. If the job requires a Windows container and the first compute environment is `LINUX` , the compute environment is skipped and the next compute environment is checked until a Windows-based compute environment is found.

### Note

Fargate Spot is not supported for `ARM64` and Windows-based containers on Fargate. A job queue will be blocked if a Fargate `ARM64` or Windows job is submitted to a job queue with only Fargate Spot compute environments. However, you can attach both `FARGATE` and `FARGATE_SPOT` compute environments to the same job queue.

cpuArchitecture -> (string)

The vCPU architecture. The default value is `X86_64` . Valid values are `X86_64` and `ARM64` .

### Note

This parameter must be set to `X86_64` for Windows containers.

### Note

Fargate Spot is not supported for `ARM64` and Windows-based containers on Fargate. A job queue will be blocked if a Fargate `ARM64` or Windows job is submitted to a job queue with only Fargate Spot compute environments. However, you can attach both `FARGATE` and `FARGATE_SPOT` compute environments to the same job queue.

repositoryCredentials -> (structure)

The private repository authentication credentials to use.

credentialsParameter -> (string)

The Amazon Resource Name (ARN) of the secret containing the private repository credentials.

JSON Syntax:

```
{
  "image": "string",
  "vcpus": integer,
  "memory": integer,
  "command": ["string", ...],
  "jobRoleArn": "string",
  "executionRoleArn": "string",
  "volumes": [
    {
      "host": {
        "sourcePath": "string"
      },
      "name": "string",
      "efsVolumeConfiguration": {
        "fileSystemId": "string",
        "rootDirectory": "string",
        "transitEncryption": "ENABLED"|"DISABLED",
        "transitEncryptionPort": integer,
        "authorizationConfig": {
          "accessPointId": "string",
          "iam": "ENABLED"|"DISABLED"
        }
      }
    }
    ...
  ],
  "environment": [
    {
      "name": "string",
      "value": "string"
    }
    ...
  ],
  "mountPoints": [
    {
      "containerPath": "string",
      "readOnly": true|false,
      "sourceVolume": "string"
    }
    ...
  ],
  "readonlyRootFilesystem": true|false,
  "privileged": true|false,
  "ulimits": [
    {
      "hardLimit": integer,
      "name": "string",
      "softLimit": integer
    }
    ...
  ],
  "user": "string",
  "instanceType": "string",
  "resourceRequirements": [
    {
      "value": "string",
      "type": "GPU"|"VCPU"|"MEMORY"
    }
    ...
  ],
  "linuxParameters": {
    "devices": [
      {
        "hostPath": "string",
        "containerPath": "string",
        "permissions": ["READ"|"WRITE"|"MKNOD", ...]
      }
      ...
    ],
    "initProcessEnabled": true|false,
    "sharedMemorySize": integer,
    "tmpfs": [
      {
        "containerPath": "string",
        "size": integer,
        "mountOptions": ["string", ...]
      }
      ...
    ],
    "maxSwap": integer,
    "swappiness": integer
  },
  "logConfiguration": {
    "logDriver": "json-file"|"syslog"|"journald"|"gelf"|"fluentd"|"awslogs"|"splunk"|"awsfirelens",
    "options": {"string": "string"
      ...},
    "secretOptions": [
      {
        "name": "string",
        "valueFrom": "string"
      }
      ...
    ]
  },
  "secrets": [
    {
      "name": "string",
      "valueFrom": "string"
    }
    ...
  ],
  "networkConfiguration": {
    "assignPublicIp": "ENABLED"|"DISABLED"
  },
  "fargatePlatformConfiguration": {
    "platformVersion": "string"
  },
  "enableExecuteCommand": true|false,
  "ephemeralStorage": {
    "sizeInGiB": integer
  },
  "runtimePlatform": {
    "operatingSystemFamily": "string",
    "cpuArchitecture": "string"
  },
  "repositoryCredentials": {
    "credentialsParameter": "string"
  }
}
```

`--node-properties` (structure)

An object with properties specific to multi-node parallel jobs. If you specify node properties for a job, it becomes a multi-node parallel job. For more information, see [Multi-node Parallel Jobs](https://docs.aws.amazon.com/batch/latest/userguide/multi-node-parallel-jobs.html) in the *Batch User Guide* .

### Note

If the job runs on Fargate resources, then you must not specify `nodeProperties` ; use `containerProperties` instead.

### Note

If the job runs on Amazon EKS resources, then you must not specify `nodeProperties` .

numNodes -> (integer)

The number of nodes that are associated with a multi-node parallel job.

mainNode -> (integer)

Specifies the node index for the main node of a multi-node parallel job. This node index value must be fewer than the number of nodes.

nodeRangeProperties -> (list)

A list of node ranges and their properties that are associated with a multi-node parallel job.

(structure)

This is an object that represents the properties of the node range for a multi-node parallel job.

targetNodes -> (string)

The range of nodes, using node index values. A range of `0:3` indicates nodes with index values of `0` through `3` . If the starting range value is omitted (`:n` ), then `0` is used to start the range. If the ending range value is omitted (`n:` ), then the highest possible node index is used to end the range. Your accumulative node ranges must account for all nodes (`0:n` ). You can nest node ranges (for example, `0:10` and `4:5` ). In this case, the `4:5` range properties override the `0:10` properties.

container -> (structure)

The container details for the node range.

image -> (string)

Required. The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `` *repository-url* /*image* :*tag* `` . It can be 255 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), underscores (_), colons (:), periods (.), forward slashes (/), and number signs (#). This parameter maps to `Image` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `IMAGE` parameter of [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

Docker image architecture must match the processor architecture of the compute resources that theyâre scheduled on. For example, ARM-based Docker images can only run on ARM-based compute resources.

- Images in Amazon ECR Public repositories use the full `registry/repository[:tag]` or `registry/repository[@digest]` naming conventions. For example, [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/register-job-definition.html#id3)public.ecr.aws/*registry_alias* /*my-web-app* :*latest* `` .
- Images in Amazon ECR repositories use the full registry and repository URI (for example, `123456789012.dkr.ecr.<region-name>.amazonaws.com/<repository-name>` ).
- Images in official repositories on Docker Hub use a single name (for example, `ubuntu` or `mongo` ).
- Images in other repositories on Docker Hub are qualified with an organization name (for example, `amazon/amazon-ecs-agent` ).
- Images in other online repositories are qualified further by a domain name (for example, `quay.io/assemblyline/ubuntu` ).

vcpus -> (integer)

This parameter is deprecated, use `resourceRequirements` to specify the vCPU requirements for the job definition. Itâs not supported for jobs running on Fargate resources. For jobs running on Amazon EC2 resources, it specifies the number of vCPUs reserved for the job.

Each vCPU is equivalent to 1,024 CPU shares. This parameter maps to `CpuShares` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--cpu-shares` option to [docker run](https://docs.docker.com/engine/reference/run/) . The number of vCPUs must be specified but can be specified in several places. You must specify it at least once for each node.

memory -> (integer)

This parameter is deprecated, use `resourceRequirements` to specify the memory requirements for the job definition. Itâs not supported for jobs running on Fargate resources. For jobs that run on Amazon EC2 resources, it specifies the memory hard limit (in MiB) for a container. If your container attempts to exceed the specified number, itâs terminated. You must specify at least 4 MiB of memory for a job using this parameter. The memory hard limit can be specified in several places. It must be specified for each node at least once.

command -> (list)

The command thatâs passed to the container. This parameter maps to `Cmd` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `COMMAND` parameter to [docker run](https://docs.docker.com/engine/reference/run/) . For more information, see [https://docs.docker.com/engine/reference/builder/#cmd](https://docs.docker.com/engine/reference/builder/#cmd) .

(string)

jobRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that the container can assume for Amazon Web Services permissions. For more information, see [IAM roles for tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide* .

executionRoleArn -> (string)

The Amazon Resource Name (ARN) of the execution role that Batch can assume. For jobs that run on Fargate resources, you must provide an execution role. For more information, see [Batch execution IAM role](https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html) in the *Batch User Guide* .

volumes -> (list)

A list of data volumes used in a job.

(structure)

A data volume thatâs used in a jobâs container properties.

host -> (structure)

The contents of the `host` parameter determine whether your data volume persists on the host container instance and where itâs stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data isnât guaranteed to persist after the containers that are associated with it stop running.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources and shouldnât be provided.

sourcePath -> (string)

The path on the host container instance thatâs presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If this parameter contains a file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the source path location doesnât exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.

### Note

This parameter isnât applicable to jobs that run on Fargate resources. Donât provide this for these jobs.

name -> (string)

The name of the volume. It can be up to 255 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_). This name is referenced in the `sourceVolume` parameter of container definition `mountPoints` .

efsVolumeConfiguration -> (structure)

This parameter is specified when youâre using an Amazon Elastic File System file system for job storage. Jobs that are running on Fargate resources must specify a `platformVersion` of at least `1.4.0` .

fileSystemId -> (string)

The Amazon EFS file system ID to use.

rootDirectory -> (string)

The directory within the Amazon EFS file system to mount as the root directory inside the host. If this parameter is omitted, the root of the Amazon EFS volume is used instead. Specifying `/` has the same effect as omitting this parameter. The maximum length is 4,096 characters.

### Warning

If an EFS access point is specified in the `authorizationConfig` , the root directory parameter must either be omitted or set to `/` , which enforces the path set on the Amazon EFS access point.

transitEncryption -> (string)

Determines whether to enable encryption for Amazon EFS data in transit between the Amazon ECS host and the Amazon EFS server. Transit encryption must be enabled if Amazon EFS IAM authorization is used. If this parameter is omitted, the default value of `DISABLED` is used. For more information, see [Encrypting data in transit](https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html) in the *Amazon Elastic File System User Guide* .

transitEncryptionPort -> (integer)

The port to use when sending encrypted data between the Amazon ECS host and the Amazon EFS server. If you donât specify a transit encryption port, it uses the port selection strategy that the Amazon EFS mount helper uses. The value must be between 0 and 65,535. For more information, see [EFS mount helper](https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html) in the *Amazon Elastic File System User Guide* .

authorizationConfig -> (structure)

The authorization configuration details for the Amazon EFS file system.

accessPointId -> (string)

The Amazon EFS access point ID to use. If an access point is specified, the root directory value specified in the `EFSVolumeConfiguration` must either be omitted or set to `/` which enforces the path set on the EFS access point. If an access point is used, transit encryption must be enabled in the `EFSVolumeConfiguration` . For more information, see [Working with Amazon EFS access points](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html) in the *Amazon Elastic File System User Guide* .

iam -> (string)

Whether or not to use the Batch job IAM role defined in a job definition when mounting the Amazon EFS file system. If enabled, transit encryption must be enabled in the `EFSVolumeConfiguration` . If this parameter is omitted, the default value of `DISABLED` is used. For more information, see [Using Amazon EFS access points](https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html#efs-volume-accesspoints) in the *Batch User Guide* . EFS IAM authorization requires that `TransitEncryption` be `ENABLED` and that a `JobRoleArn` is specified.

environment -> (list)

The environment variables to pass to a container. This parameter maps to `Env` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--env` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Warning

We donât recommend using plaintext environment variables for sensitive information, such as credential data.

### Note

Environment variables cannot start with â`AWS_BATCH` â. This naming convention is reserved for variables that Batch sets.

(structure)

A key-value pair object.

name -> (string)

The name of the key-value pair. For environment variables, this is the name of the environment variable.

value -> (string)

The value of the key-value pair. For environment variables, this is the value of the environment variable.

mountPoints -> (list)

The mount points for data volumes in your container. This parameter maps to `Volumes` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--volume` option to [docker run](https://docs.docker.com/engine/reference/run/) .

(structure)

Details for a Docker volume mount point thatâs used in a jobâs container properties. This parameter maps to `Volumes` in the [Create a container](https://docs.docker.com/engine/api/v1.43/#tag/Container/operation/ContainerCreate) section of the *Docker Remote API* and the `--volume` option to docker run.

containerPath -> (string)

The path on the container where the host volume is mounted.

readOnly -> (boolean)

If this value is `true` , the container has read-only access to the volume. Otherwise, the container can write to the volume. The default value is `false` .

sourceVolume -> (string)

The name of the volume to mount.

readonlyRootFilesystem -> (boolean)

When this parameter is true, the container is given read-only access to its root file system. This parameter maps to `ReadonlyRootfs` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--read-only` option to `docker run` .

privileged -> (boolean)

When this parameter is true, the container is given elevated permissions on the host container instance (similar to the `root` user). This parameter maps to `Privileged` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--privileged` option to [docker run](https://docs.docker.com/engine/reference/run/) . The default value is false.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources and shouldnât be provided, or specified as false.

ulimits -> (list)

A list of `ulimits` to set in the container. This parameter maps to `Ulimits` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--ulimit` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources and shouldnât be provided.

(structure)

The `ulimit` settings to pass to the container. For more information, see [Ulimit](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Ulimit.html) .

### Note

This object isnât applicable to jobs that are running on Fargate resources.

hardLimit -> (integer)

The hard limit for the `ulimit` type.

name -> (string)

The `type` of the `ulimit` . Valid values are: `core` | `cpu` | `data` | `fsize` | `locks` | `memlock` | `msgqueue` | `nice` | `nofile` | `nproc` | `rss` | `rtprio` | `rttime` | `sigpending` | `stack` .

softLimit -> (integer)

The soft limit for the `ulimit` type.

user -> (string)

The user name to use inside the container. This parameter maps to `User` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--user` option to [docker run](https://docs.docker.com/engine/reference/run/) .

instanceType -> (string)

The instance type to use for a multi-node parallel job. All node groups in a multi-node parallel job must use the same instance type.

### Note

This parameter isnât applicable to single-node container jobs or jobs that run on Fargate resources, and shouldnât be provided.

resourceRequirements -> (list)

The type and amount of resources to assign to a container. The supported resources include `GPU` , `MEMORY` , and `VCPU` .

(structure)

The type and amount of a resource to assign to a container. The supported resources include `GPU` , `MEMORY` , and `VCPU` .

value -> (string)

The quantity of the specified resource to reserve for the container. The values vary based on the `type` specified.

type=âGPUâ

The number of physical GPUs to reserve for the container. Make sure that the number of GPUs reserved for all containers in a job doesnât exceed the number of available GPUs on the compute resource that the job is launched on.

### Note

GPUs arenât available for jobs that are running on Fargate resources.

type=âMEMORYâ

The memory hard limit (in MiB) present to the container. This parameter is supported for jobs that are running on Amazon EC2 resources. If your container attempts to exceed the memory specified, the container is terminated. This parameter maps to `Memory` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--memory` option to [docker run](https://docs.docker.com/engine/reference/run/) . You must specify at least 4 MiB of memory for a job. This is required but can be specified in several places for multi-node parallel (MNP) jobs. It must be specified for each node at least once. This parameter maps to `Memory` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--memory` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

If youâre trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see [Memory management](https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html) in the *Batch User Guide* .

For jobs that are running on Fargate resources, then `value` is the hard limit (in MiB), and must match one of the supported values and the `VCPU` values must be one of the values supported for that memory value.

value = 512

`VCPU` = 0.25

value = 1024

`VCPU` = 0.25 or 0.5

value = 2048

`VCPU` = 0.25, 0.5, or 1

value = 3072

`VCPU` = 0.5, or 1

value = 4096

`VCPU` = 0.5, 1, or 2

value = 5120, 6144, or 7168

`VCPU` = 1 or 2

value = 8192

`VCPU` = 1, 2, or 4

value = 9216, 10240, 11264, 12288, 13312, 14336, or 15360

`VCPU` = 2 or 4

value = 16384

`VCPU` = 2, 4, or 8

value = 17408, 18432, 19456, 21504, 22528, 23552, 25600, 26624, 27648, 29696, or 30720

`VCPU` = 4

value = 20480, 24576, or 28672

`VCPU` = 4 or 8

value = 36864, 45056, 53248, or 61440

`VCPU` = 8

value = 32768, 40960, 49152, or 57344

`VCPU` = 8 or 16

value = 65536, 73728, 81920, 90112, 98304, 106496, 114688, or 122880

`VCPU` = 16

type=âVCPUâ

The number of vCPUs reserved for the container. This parameter maps to `CpuShares` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--cpu-shares` option to [docker run](https://docs.docker.com/engine/reference/run/) . Each vCPU is equivalent to 1,024 CPU shares. For Amazon EC2 resources, you must specify at least one vCPU. This is required but can be specified in several places; it must be specified for each node at least once.

The default for the Fargate On-Demand vCPU resource count quota is 6 vCPUs. For more information about Fargate quotas, see [Fargate quotas](https://docs.aws.amazon.com/general/latest/gr/ecs-service.html#service-quotas-fargate) in the *Amazon Web Services General Reference* .

For jobs that are running on Fargate resources, then `value` must match one of the supported values and the `MEMORY` values must be one of the values supported for that `VCPU` value. The supported values are 0.25, 0.5, 1, 2, 4, 8, and 16

value = 0.25

`MEMORY` = 512, 1024, or 2048

value = 0.5

`MEMORY` = 1024, 2048, 3072, or 4096

value = 1

`MEMORY` = 2048, 3072, 4096, 5120, 6144, 7168, or 8192

value = 2

`MEMORY` = 4096, 5120, 6144, 7168, 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, or 16384

value = 4

`MEMORY` = 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, 16384, 17408, 18432, 19456, 20480, 21504, 22528, 23552, 24576, 25600, 26624, 27648, 28672, 29696, or 30720

value = 8

`MEMORY` = 16384, 20480, 24576, 28672, 32768, 36864, 40960, 45056, 49152, 53248, 57344, or 61440

value = 16

`MEMORY` = 32768, 40960, 49152, 57344, 65536, 73728, 81920, 90112, 98304, 106496, 114688, or 122880

type -> (string)

The type of resource to assign to a container. The supported resources include `GPU` , `MEMORY` , and `VCPU` .

linuxParameters -> (structure)

Linux-specific modifications that are applied to the container, such as details for device mappings.

devices -> (list)

Any of the host devices to expose to the container. This parameter maps to `Devices` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--device` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide it for these jobs.

(structure)

An object that represents a container instance host device.

### Note

This object isnât applicable to jobs that are running on Fargate resources and shouldnât be provided.

hostPath -> (string)

The path for the device on the host container instance.

containerPath -> (string)

The path inside the container thatâs used to expose the host device. By default, the `hostPath` value is used.

permissions -> (list)

The explicit permissions to provide to the container for the device. By default, the container has permissions for `read` , `write` , and `mknod` for the device.

(string)

initProcessEnabled -> (boolean)

If true, run an `init` process inside the container that forwards signals and reaps processes. This parameter maps to the `--init` option to [docker run](https://docs.docker.com/engine/reference/run/) . This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`

sharedMemorySize -> (integer)

The value for the size (in MiB) of the `/dev/shm` volume. This parameter maps to the `--shm-size` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide it for these jobs.

tmpfs -> (list)

The container path, mount options, and size (in MiB) of the `tmpfs` mount. This parameter maps to the `--tmpfs` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide this parameter for this resource type.

(structure)

The container path, mount options, and size of the `tmpfs` mount.

### Note

This object isnât applicable to jobs that are running on Fargate resources.

containerPath -> (string)

The absolute file path in the container where the `tmpfs` volume is mounted.

size -> (integer)

The size (in MiB) of the `tmpfs` volume.

mountOptions -> (list)

The list of `tmpfs` volume mount options.

Valid values: â`defaults` â | â`ro` â | â`rw` â | â`suid` â | â`nosuid` â | â`dev` â | â`nodev` â | â`exec` â | â`noexec` â | â`sync` â | â`async` â | â`dirsync` â | â`remount` â | â`mand` â | â`nomand` â | â`atime` â | â`noatime` â | â`diratime` â | â`nodiratime` â | â`bind` â | â`rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime` â | â`norelatime` â | â`strictatime` â | â`nostrictatime` â | â`mode` â | â`uid` â | â`gid` â | â`nr_inodes` â | â`nr_blocks` â | â`mpol` â

(string)

maxSwap -> (integer)

The total amount of swap memory (in MiB) a container can use. This parameter is translated to the `--memory-swap` option to [docker run](https://docs.docker.com/engine/reference/run/) where the value is the sum of the container memory plus the `maxSwap` value. For more information, see ` `--memory-swap` details <[https://docs.docker.com/config/containers/resource_constraints/#âmemory-swap-details](https://docs.docker.com/config/containers/resource_constraints/#--memory-swap-details)>`__ in the Docker documentation.

If a `maxSwap` value of `0` is specified, the container doesnât use swap. Accepted values are `0` or any positive integer. If the `maxSwap` parameter is omitted, the container doesnât use the swap configuration for the container instance on which it runs. A `maxSwap` value must be set for the `swappiness` parameter to be used.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide it for these jobs.

swappiness -> (integer)

You can use this parameter to tune a containerâs memory swappiness behavior. A `swappiness` value of `0` causes swapping to not occur unless absolutely necessary. A `swappiness` value of `100` causes pages to be swapped aggressively. Valid values are whole numbers between `0` and `100` . If the `swappiness` parameter isnât specified, a default value of `60` is used. If a value isnât specified for `maxSwap` , then this parameter is ignored. If `maxSwap` is set to 0, the container doesnât use swap. This parameter maps to the `--memory-swappiness` option to [docker run](https://docs.docker.com/engine/reference/run/) .

Consider the following when you use a per-container swap configuration.

- Swap space must be enabled and allocated on the container instance for the containers to use.

### Note

By default, the Amazon ECS optimized AMIs donât have swap enabled. You must enable swap on the instance to use this feature. For more information, see [Instance store swap volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-swap-volumes.html) in the *Amazon EC2 User Guide for Linux Instances* or [How do I allocate memory to work as swap space in an Amazon EC2 instance by using a swap file?](http://aws.amazon.com/premiumsupport/knowledge-center/ec2-memory-swap-file/)

- The swap space parameters are only supported for job definitions using EC2 resources.
- If the `maxSwap` and `swappiness` parameters are omitted from a job definition, each container has a default `swappiness` value of 60. Moreover, the total swap usage is limited to two times the memory reservation of the container.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide it for these jobs.

logConfiguration -> (structure)

The log configuration specification for the container.

This parameter maps to `LogConfig` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--log-driver` option to [docker run](https://docs.docker.com/engine/reference/run/) . By default, containers use the same logging driver that the Docker daemon uses. However the container might use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see [Configure logging drivers](https://docs.docker.com/engine/admin/logging/overview/) in the Docker documentation.

### Note

Batch currently supports a subset of the logging drivers available to the Docker daemon (shown in the [LogConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html) data type).

This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`

### Note

The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the `ECS_AVAILABLE_LOGGING_DRIVERS` environment variable before containers placed on that instance can use these log configuration options. For more information, see [Amazon ECS container agent configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html) in the *Amazon Elastic Container Service Developer Guide* .

logDriver -> (string)

The log driver to use for the container. The valid values that are listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default.

The supported log drivers are `awslogs` , `fluentd` , `gelf` , `json-file` , `journald` , `logentries` , `syslog` , and `splunk` .

### Note

Jobs that are running on Fargate resources are restricted to the `awslogs` and `splunk` log drivers.

awsfirelens

Specifies the firelens logging driver. For more information on configuring Firelens, see [Send Amazon ECS logs to an Amazon Web Services service or Amazon Web Services Partner](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) in the *Amazon Elastic Container Service Developer Guide* .

awslogs

Specifies the Amazon CloudWatch Logs logging driver. For more information, see [Using the awslogs log driver](https://docs.aws.amazon.com/batch/latest/userguide/using_awslogs.html) in the *Batch User Guide* and [Amazon CloudWatch Logs logging driver](https://docs.docker.com/config/containers/logging/awslogs/) in the Docker documentation.

fluentd

Specifies the Fluentd logging driver. For more information including usage and options, see [Fluentd logging driver](https://docs.docker.com/config/containers/logging/fluentd/) in the *Docker documentation* .

gelf

Specifies the Graylog Extended Format (GELF) logging driver. For more information including usage and options, see [Graylog Extended Format logging driver](https://docs.docker.com/config/containers/logging/gelf/) in the *Docker documentation* .

journald

Specifies the journald logging driver. For more information including usage and options, see [Journald logging driver](https://docs.docker.com/config/containers/logging/journald/) in the *Docker documentation* .

json-file

Specifies the JSON file logging driver. For more information including usage and options, see [JSON File logging driver](https://docs.docker.com/config/containers/logging/json-file/) in the *Docker documentation* .

splunk

Specifies the Splunk logging driver. For more information including usage and options, see [Splunk logging driver](https://docs.docker.com/config/containers/logging/splunk/) in the *Docker documentation* .

syslog

Specifies the syslog logging driver. For more information including usage and options, see [Syslog logging driver](https://docs.docker.com/config/containers/logging/syslog/) in the *Docker documentation* .

### Note

If you have a custom driver thatâs not listed earlier that you want to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project thatâs [available on GitHub](https://github.com/aws/amazon-ecs-agent) and customize it to work with that driver. We encourage you to submit pull requests for changes that you want to have included. However, Amazon Web Services doesnât currently support running modified copies of this software.

This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`

options -> (map)

The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`

key -> (string)

value -> (string)

secretOptions -> (list)

The secrets to pass to the log configuration. For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the *Batch User Guide* .

(structure)

An object that represents the secret to expose to your container. Secrets can be exposed to a container in the following ways:

- To inject sensitive data into your containers as environment variables, use the `secrets` container definition parameter.
- To reference sensitive information in the log configuration of a container, use the `secretOptions` container definition parameter.

For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the *Batch User Guide* .

name -> (string)

The name of the secret.

valueFrom -> (string)

The secret to expose to the container. The supported values are either the full Amazon Resource Name (ARN) of the Secrets Manager secret or the full ARN of the parameter in the Amazon Web Services Systems Manager Parameter Store.

### Note

If the Amazon Web Services Systems Manager Parameter Store parameter exists in the same Region as the job youâre launching, then you can use either the full Amazon Resource Name (ARN) or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.

secrets -> (list)

The secrets for the container. For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the *Batch User Guide* .

(structure)

An object that represents the secret to expose to your container. Secrets can be exposed to a container in the following ways:

- To inject sensitive data into your containers as environment variables, use the `secrets` container definition parameter.
- To reference sensitive information in the log configuration of a container, use the `secretOptions` container definition parameter.

For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the *Batch User Guide* .

name -> (string)

The name of the secret.

valueFrom -> (string)

The secret to expose to the container. The supported values are either the full Amazon Resource Name (ARN) of the Secrets Manager secret or the full ARN of the parameter in the Amazon Web Services Systems Manager Parameter Store.

### Note

If the Amazon Web Services Systems Manager Parameter Store parameter exists in the same Region as the job youâre launching, then you can use either the full Amazon Resource Name (ARN) or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.

networkConfiguration -> (structure)

The network configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.

assignPublicIp -> (string)

Indicates whether the job has a public IP address. For a job thatâs running on Fargate resources in a private subnet to send outbound traffic to the internet (for example, to pull container images), the private subnet requires a NAT gateway be attached to route requests to the internet. For more information, see [Amazon ECS task networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide* . The default value is â`DISABLED` â.

fargatePlatformConfiguration -> (structure)

The platform configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.

platformVersion -> (string)

The Fargate platform version where the jobs are running. A platform version is specified only for jobs that are running on Fargate resources. If one isnât specified, the `LATEST` platform version is used by default. This uses a recent, approved version of the Fargate platform for compute resources. For more information, see [Fargate platform versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide* .

enableExecuteCommand -> (boolean)

Determines whether execute command functionality is turned on for this task. If `true` , execute command functionality is turned on all the containers in the task.

ephemeralStorage -> (structure)

The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on Fargate.

sizeInGiB -> (integer)

The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is `21` GiB and the maximum supported value is `200` GiB.

runtimePlatform -> (structure)

An object that represents the compute environment architecture for Batch jobs on Fargate.

operatingSystemFamily -> (string)

The operating system for the compute environment. Valid values are: `LINUX` (default), `WINDOWS_SERVER_2019_CORE` , `WINDOWS_SERVER_2019_FULL` , `WINDOWS_SERVER_2022_CORE` , and `WINDOWS_SERVER_2022_FULL` .

### Note

The following parameters canât be set for Windows containers: `linuxParameters` , `privileged` , `user` , `ulimits` , `readonlyRootFilesystem` , and `efsVolumeConfiguration` .

### Note

The Batch Scheduler checks the compute environments that are attached to the job queue before registering a task definition with Fargate. In this scenario, the job queue is where the job is submitted. If the job requires a Windows container and the first compute environment is `LINUX` , the compute environment is skipped and the next compute environment is checked until a Windows-based compute environment is found.

### Note

Fargate Spot is not supported for `ARM64` and Windows-based containers on Fargate. A job queue will be blocked if a Fargate `ARM64` or Windows job is submitted to a job queue with only Fargate Spot compute environments. However, you can attach both `FARGATE` and `FARGATE_SPOT` compute environments to the same job queue.

cpuArchitecture -> (string)

The vCPU architecture. The default value is `X86_64` . Valid values are `X86_64` and `ARM64` .

### Note

This parameter must be set to `X86_64` for Windows containers.

### Note

Fargate Spot is not supported for `ARM64` and Windows-based containers on Fargate. A job queue will be blocked if a Fargate `ARM64` or Windows job is submitted to a job queue with only Fargate Spot compute environments. However, you can attach both `FARGATE` and `FARGATE_SPOT` compute environments to the same job queue.

repositoryCredentials -> (structure)

The private repository authentication credentials to use.

credentialsParameter -> (string)

The Amazon Resource Name (ARN) of the secret containing the private repository credentials.

instanceTypes -> (list)

The instance types of the underlying host infrastructure of a multi-node parallel job.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources.

In addition, this list object is currently limited to one element.

(string)

ecsProperties -> (structure)

This is an object that represents the properties of the node range for a multi-node parallel job.

taskProperties -> (list)

An object that contains the properties for the Amazon ECS task definition of a job.

### Note

This object is currently limited to one task element. However, the task element can run up to 10 containers.

(structure)

The properties for a task definition that describes the container and volume definitions of an Amazon ECS task. You can specify which Docker images to use, the required resources, and other configurations related to launching the task definition through an Amazon ECS service or task.

containers -> (list)

This object is a list of containers.

(structure)

Container properties are used for Amazon ECS-based job definitions. These properties to describe the container thatâs launched as part of a job.

command -> (list)

The command thatâs passed to the container. This parameter maps to `Cmd` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `COMMAND` parameter to [docker run](https://docs.docker.com/engine/reference/run/) . For more information, see [Dockerfile reference: CMD](https://docs.docker.com/engine/reference/builder/#cmd) .

(string)

dependsOn -> (list)

A list of containers that this container depends on.

(structure)

A list of containers that this task depends on.

containerName -> (string)

A unique identifier for the container.

condition -> (string)

The dependency condition of the container. The following are the available conditions and their behavior:

- `START` - This condition emulates the behavior of links and volumes today. It validates that a dependent container is started before permitting other containers to start.
- `COMPLETE` - This condition validates that a dependent container runs to completion (exits) before permitting other containers to start. This can be useful for nonessential containers that run a script and then exit. This condition canât be set on an essential container.
- `SUCCESS` - This condition is the same as `COMPLETE` , but it also requires that the container exits with a zero status. This condition canât be set on an essential container.

environment -> (list)

The environment variables to pass to a container. This parameter maps to Env in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--env` parameter to [docker run](https://docs.docker.com/engine/reference/run/) .

### Warning

We donât recommend using plaintext environment variables for sensitive information, such as credential data.

### Note

Environment variables cannot start with `AWS_BATCH` . This naming convention is reserved for variables that Batch sets.

(structure)

A key-value pair object.

name -> (string)

The name of the key-value pair. For environment variables, this is the name of the environment variable.

value -> (string)

The value of the key-value pair. For environment variables, this is the value of the environment variable.

essential -> (boolean)

If the essential parameter of a container is marked as `true` , and that container fails or stops for any reason, all other containers that are part of the task are stopped. If the `essential` parameter of a container is marked as false, its failure doesnât affect the rest of the containers in a task. If this parameter is omitted, a container is assumed to be essential.

All jobs must have at least one essential container. If you have an application thatâs composed of multiple containers, group containers that are used for a common purpose into components, and separate the different components into multiple task definitions. For more information, see [Application Architecture](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/application_architecture.html) in the *Amazon Elastic Container Service Developer Guide* .

firelensConfiguration -> (structure)

The FireLens configuration for the container. This is used to specify and configure a log router for container logs. For more information, see [Custom log](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) routing in the *Amazon Elastic Container Service Developer Guide* .

type -> (string)

The log router to use. The valid values are `fluentd` or `fluentbit` .

options -> (map)

The options to use when configuring the log router. This field is optional and can be used to specify a custom configuration file or to add additional metadata, such as the task, task definition, cluster, and container instance details to the log event. If specified, the syntax to use is `"options":{"enable-ecs-log-metadata":"true|false","config-file-type:"s3|file","config-file-value":"arn:aws:s3:::mybucket/fluent.conf|filepath"}` . For more information, see [Creating a task definition that uses a FireLens configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html#firelens-taskdef) in the *Amazon Elastic Container Service Developer Guide* .

key -> (string)

value -> (string)

image -> (string)

The image used to start a container. This string is passed directly to the Docker daemon. By default, images in the Docker Hub registry are available. Other repositories are specified with either `repository-url/image:tag` or `repository-url/image@digest` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to `Image` in the [Create a container](https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.35/) and the `IMAGE` parameter of the ` *docker run* [https://docs.docker.com/engine/reference/run/#security](https://docs.docker.com/engine/reference/run/#security)-configuration`__ .

linuxParameters -> (structure)

Linux-specific modifications that are applied to the container, such as Linux kernel capabilities. For more information, see [KernelCapabilities](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_KernelCapabilities.html) .

devices -> (list)

Any of the host devices to expose to the container. This parameter maps to `Devices` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--device` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide it for these jobs.

(structure)

An object that represents a container instance host device.

### Note

This object isnât applicable to jobs that are running on Fargate resources and shouldnât be provided.

hostPath -> (string)

The path for the device on the host container instance.

containerPath -> (string)

The path inside the container thatâs used to expose the host device. By default, the `hostPath` value is used.

permissions -> (list)

The explicit permissions to provide to the container for the device. By default, the container has permissions for `read` , `write` , and `mknod` for the device.

(string)

initProcessEnabled -> (boolean)

If true, run an `init` process inside the container that forwards signals and reaps processes. This parameter maps to the `--init` option to [docker run](https://docs.docker.com/engine/reference/run/) . This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`

sharedMemorySize -> (integer)

The value for the size (in MiB) of the `/dev/shm` volume. This parameter maps to the `--shm-size` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide it for these jobs.

tmpfs -> (list)

The container path, mount options, and size (in MiB) of the `tmpfs` mount. This parameter maps to the `--tmpfs` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide this parameter for this resource type.

(structure)

The container path, mount options, and size of the `tmpfs` mount.

### Note

This object isnât applicable to jobs that are running on Fargate resources.

containerPath -> (string)

The absolute file path in the container where the `tmpfs` volume is mounted.

size -> (integer)

The size (in MiB) of the `tmpfs` volume.

mountOptions -> (list)

The list of `tmpfs` volume mount options.

Valid values: â`defaults` â | â`ro` â | â`rw` â | â`suid` â | â`nosuid` â | â`dev` â | â`nodev` â | â`exec` â | â`noexec` â | â`sync` â | â`async` â | â`dirsync` â | â`remount` â | â`mand` â | â`nomand` â | â`atime` â | â`noatime` â | â`diratime` â | â`nodiratime` â | â`bind` â | â`rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime` â | â`norelatime` â | â`strictatime` â | â`nostrictatime` â | â`mode` â | â`uid` â | â`gid` â | â`nr_inodes` â | â`nr_blocks` â | â`mpol` â

(string)

maxSwap -> (integer)

The total amount of swap memory (in MiB) a container can use. This parameter is translated to the `--memory-swap` option to [docker run](https://docs.docker.com/engine/reference/run/) where the value is the sum of the container memory plus the `maxSwap` value. For more information, see ` `--memory-swap` details <[https://docs.docker.com/config/containers/resource_constraints/#âmemory-swap-details](https://docs.docker.com/config/containers/resource_constraints/#--memory-swap-details)>`__ in the Docker documentation.

If a `maxSwap` value of `0` is specified, the container doesnât use swap. Accepted values are `0` or any positive integer. If the `maxSwap` parameter is omitted, the container doesnât use the swap configuration for the container instance on which it runs. A `maxSwap` value must be set for the `swappiness` parameter to be used.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide it for these jobs.

swappiness -> (integer)

You can use this parameter to tune a containerâs memory swappiness behavior. A `swappiness` value of `0` causes swapping to not occur unless absolutely necessary. A `swappiness` value of `100` causes pages to be swapped aggressively. Valid values are whole numbers between `0` and `100` . If the `swappiness` parameter isnât specified, a default value of `60` is used. If a value isnât specified for `maxSwap` , then this parameter is ignored. If `maxSwap` is set to 0, the container doesnât use swap. This parameter maps to the `--memory-swappiness` option to [docker run](https://docs.docker.com/engine/reference/run/) .

Consider the following when you use a per-container swap configuration.

- Swap space must be enabled and allocated on the container instance for the containers to use.

### Note

By default, the Amazon ECS optimized AMIs donât have swap enabled. You must enable swap on the instance to use this feature. For more information, see [Instance store swap volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-swap-volumes.html) in the *Amazon EC2 User Guide for Linux Instances* or [How do I allocate memory to work as swap space in an Amazon EC2 instance by using a swap file?](http://aws.amazon.com/premiumsupport/knowledge-center/ec2-memory-swap-file/)

- The swap space parameters are only supported for job definitions using EC2 resources.
- If the `maxSwap` and `swappiness` parameters are omitted from a job definition, each container has a default `swappiness` value of 60. Moreover, the total swap usage is limited to two times the memory reservation of the container.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide it for these jobs.

logConfiguration -> (structure)

The log configuration specification for the container.

This parameter maps to `LogConfig` in the [Create a container](https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.35/) and the `--log-driver` option to [docker run](https://docs.docker.com/engine/reference/run/#security-configuration) .

By default, containers use the same logging driver that the Docker daemon uses. However the container can use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information about the options for different supported log drivers, see [Configure logging drivers](https://docs.docker.com/engine/admin/logging/overview/) in the *Docker documentation* .

### Note

Amazon ECS currently supports a subset of the logging drivers available to the Docker daemon (shown in the `LogConfiguration` data type). Additional log drivers may be available in future releases of the Amazon ECS container agent.

This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version `--format '{{.Server.APIVersion}}'`

### Note

The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the `ECS_AVAILABLE_LOGGING_DRIVERS` environment variable before containers placed on that instance can use these log configuration options. For more information, see [Amazon ECS container agent configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html) in the *Amazon Elastic Container Service Developer Guide* .

logDriver -> (string)

The log driver to use for the container. The valid values that are listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default.

The supported log drivers are `awslogs` , `fluentd` , `gelf` , `json-file` , `journald` , `logentries` , `syslog` , and `splunk` .

### Note

Jobs that are running on Fargate resources are restricted to the `awslogs` and `splunk` log drivers.

awsfirelens

Specifies the firelens logging driver. For more information on configuring Firelens, see [Send Amazon ECS logs to an Amazon Web Services service or Amazon Web Services Partner](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) in the *Amazon Elastic Container Service Developer Guide* .

awslogs

Specifies the Amazon CloudWatch Logs logging driver. For more information, see [Using the awslogs log driver](https://docs.aws.amazon.com/batch/latest/userguide/using_awslogs.html) in the *Batch User Guide* and [Amazon CloudWatch Logs logging driver](https://docs.docker.com/config/containers/logging/awslogs/) in the Docker documentation.

fluentd

Specifies the Fluentd logging driver. For more information including usage and options, see [Fluentd logging driver](https://docs.docker.com/config/containers/logging/fluentd/) in the *Docker documentation* .

gelf

Specifies the Graylog Extended Format (GELF) logging driver. For more information including usage and options, see [Graylog Extended Format logging driver](https://docs.docker.com/config/containers/logging/gelf/) in the *Docker documentation* .

journald

Specifies the journald logging driver. For more information including usage and options, see [Journald logging driver](https://docs.docker.com/config/containers/logging/journald/) in the *Docker documentation* .

json-file

Specifies the JSON file logging driver. For more information including usage and options, see [JSON File logging driver](https://docs.docker.com/config/containers/logging/json-file/) in the *Docker documentation* .

splunk

Specifies the Splunk logging driver. For more information including usage and options, see [Splunk logging driver](https://docs.docker.com/config/containers/logging/splunk/) in the *Docker documentation* .

syslog

Specifies the syslog logging driver. For more information including usage and options, see [Syslog logging driver](https://docs.docker.com/config/containers/logging/syslog/) in the *Docker documentation* .

### Note

If you have a custom driver thatâs not listed earlier that you want to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project thatâs [available on GitHub](https://github.com/aws/amazon-ecs-agent) and customize it to work with that driver. We encourage you to submit pull requests for changes that you want to have included. However, Amazon Web Services doesnât currently support running modified copies of this software.

This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`

options -> (map)

The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`

key -> (string)

value -> (string)

secretOptions -> (list)

The secrets to pass to the log configuration. For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the *Batch User Guide* .

(structure)

An object that represents the secret to expose to your container. Secrets can be exposed to a container in the following ways:

- To inject sensitive data into your containers as environment variables, use the `secrets` container definition parameter.
- To reference sensitive information in the log configuration of a container, use the `secretOptions` container definition parameter.

For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the *Batch User Guide* .

name -> (string)

The name of the secret.

valueFrom -> (string)

The secret to expose to the container. The supported values are either the full Amazon Resource Name (ARN) of the Secrets Manager secret or the full ARN of the parameter in the Amazon Web Services Systems Manager Parameter Store.

### Note

If the Amazon Web Services Systems Manager Parameter Store parameter exists in the same Region as the job youâre launching, then you can use either the full Amazon Resource Name (ARN) or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.

mountPoints -> (list)

The mount points for data volumes in your container.

This parameter maps to `Volumes` in the [Create a container](https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.35/) and the [âvolume option to `docker run](https://docs.docker.com/engine/reference/run/#security-configuration) .

Windows containers can mount whole directories on the same drive as `$env:ProgramData` . Windows containers canât mount directories on a different drive, and mount point canât be across drives.

(structure)

Details for a Docker volume mount point thatâs used in a jobâs container properties. This parameter maps to `Volumes` in the [Create a container](https://docs.docker.com/engine/api/v1.43/#tag/Container/operation/ContainerCreate) section of the *Docker Remote API* and the `--volume` option to docker run.

containerPath -> (string)

The path on the container where the host volume is mounted.

readOnly -> (boolean)

If this value is `true` , the container has read-only access to the volume. Otherwise, the container can write to the volume. The default value is `false` .

sourceVolume -> (string)

The name of the volume to mount.

name -> (string)

The name of a container. The name can be used as a unique identifier to target your `dependsOn` and `Overrides` objects.

privileged -> (boolean)

When this parameter is `true` , the container is given elevated privileges on the host container instance (similar to the `root` user). This parameter maps to `Privileged` in the [Create a container](https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.35/) and the `--privileged` option to [docker run](https://docs.docker.com/engine/reference/run/#security-configuration) .

### Note

This parameter is not supported for Windows containers or tasks run on Fargate.

readonlyRootFilesystem -> (boolean)

When this parameter is true, the container is given read-only access to its root file system. This parameter maps to `ReadonlyRootfs` in the [Create a container](https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.35/) and the `--read-only` option to [docker run](https://docs.docker.com/engine/reference/run/#security-configuration) .

### Note

This parameter is not supported for Windows containers.

repositoryCredentials -> (structure)

The private repository authentication credentials to use.

credentialsParameter -> (string)

The Amazon Resource Name (ARN) of the secret containing the private repository credentials.

resourceRequirements -> (list)

The type and amount of a resource to assign to a container. The only supported resource is a GPU.

(structure)

The type and amount of a resource to assign to a container. The supported resources include `GPU` , `MEMORY` , and `VCPU` .

value -> (string)

The quantity of the specified resource to reserve for the container. The values vary based on the `type` specified.

type=âGPUâ

The number of physical GPUs to reserve for the container. Make sure that the number of GPUs reserved for all containers in a job doesnât exceed the number of available GPUs on the compute resource that the job is launched on.

### Note

GPUs arenât available for jobs that are running on Fargate resources.

type=âMEMORYâ

The memory hard limit (in MiB) present to the container. This parameter is supported for jobs that are running on Amazon EC2 resources. If your container attempts to exceed the memory specified, the container is terminated. This parameter maps to `Memory` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--memory` option to [docker run](https://docs.docker.com/engine/reference/run/) . You must specify at least 4 MiB of memory for a job. This is required but can be specified in several places for multi-node parallel (MNP) jobs. It must be specified for each node at least once. This parameter maps to `Memory` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--memory` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

If youâre trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see [Memory management](https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html) in the *Batch User Guide* .

For jobs that are running on Fargate resources, then `value` is the hard limit (in MiB), and must match one of the supported values and the `VCPU` values must be one of the values supported for that memory value.

value = 512

`VCPU` = 0.25

value = 1024

`VCPU` = 0.25 or 0.5

value = 2048

`VCPU` = 0.25, 0.5, or 1

value = 3072

`VCPU` = 0.5, or 1

value = 4096

`VCPU` = 0.5, 1, or 2

value = 5120, 6144, or 7168

`VCPU` = 1 or 2

value = 8192

`VCPU` = 1, 2, or 4

value = 9216, 10240, 11264, 12288, 13312, 14336, or 15360

`VCPU` = 2 or 4

value = 16384

`VCPU` = 2, 4, or 8

value = 17408, 18432, 19456, 21504, 22528, 23552, 25600, 26624, 27648, 29696, or 30720

`VCPU` = 4

value = 20480, 24576, or 28672

`VCPU` = 4 or 8

value = 36864, 45056, 53248, or 61440

`VCPU` = 8

value = 32768, 40960, 49152, or 57344

`VCPU` = 8 or 16

value = 65536, 73728, 81920, 90112, 98304, 106496, 114688, or 122880

`VCPU` = 16

type=âVCPUâ

The number of vCPUs reserved for the container. This parameter maps to `CpuShares` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--cpu-shares` option to [docker run](https://docs.docker.com/engine/reference/run/) . Each vCPU is equivalent to 1,024 CPU shares. For Amazon EC2 resources, you must specify at least one vCPU. This is required but can be specified in several places; it must be specified for each node at least once.

The default for the Fargate On-Demand vCPU resource count quota is 6 vCPUs. For more information about Fargate quotas, see [Fargate quotas](https://docs.aws.amazon.com/general/latest/gr/ecs-service.html#service-quotas-fargate) in the *Amazon Web Services General Reference* .

For jobs that are running on Fargate resources, then `value` must match one of the supported values and the `MEMORY` values must be one of the values supported for that `VCPU` value. The supported values are 0.25, 0.5, 1, 2, 4, 8, and 16

value = 0.25

`MEMORY` = 512, 1024, or 2048

value = 0.5

`MEMORY` = 1024, 2048, 3072, or 4096

value = 1

`MEMORY` = 2048, 3072, 4096, 5120, 6144, 7168, or 8192

value = 2

`MEMORY` = 4096, 5120, 6144, 7168, 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, or 16384

value = 4

`MEMORY` = 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, 16384, 17408, 18432, 19456, 20480, 21504, 22528, 23552, 24576, 25600, 26624, 27648, 28672, 29696, or 30720

value = 8

`MEMORY` = 16384, 20480, 24576, 28672, 32768, 36864, 40960, 45056, 49152, 53248, 57344, or 61440

value = 16

`MEMORY` = 32768, 40960, 49152, 57344, 65536, 73728, 81920, 90112, 98304, 106496, 114688, or 122880

type -> (string)

The type of resource to assign to a container. The supported resources include `GPU` , `MEMORY` , and `VCPU` .

secrets -> (list)

The secrets to pass to the container. For more information, see [Specifying Sensitive Data](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html) in the Amazon Elastic Container Service Developer Guide.

(structure)

An object that represents the secret to expose to your container. Secrets can be exposed to a container in the following ways:

- To inject sensitive data into your containers as environment variables, use the `secrets` container definition parameter.
- To reference sensitive information in the log configuration of a container, use the `secretOptions` container definition parameter.

For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the *Batch User Guide* .

name -> (string)

The name of the secret.

valueFrom -> (string)

The secret to expose to the container. The supported values are either the full Amazon Resource Name (ARN) of the Secrets Manager secret or the full ARN of the parameter in the Amazon Web Services Systems Manager Parameter Store.

### Note

If the Amazon Web Services Systems Manager Parameter Store parameter exists in the same Region as the job youâre launching, then you can use either the full Amazon Resource Name (ARN) or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.

ulimits -> (list)

A list of `ulimits` to set in the container. If a `ulimit` value is specified in a task definition, it overrides the default values set by Docker. This parameter maps to `Ulimits` in the [Create a container](https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.35/) and the `--ulimit` option to [docker run](https://docs.docker.com/engine/reference/run/#security-configuration) .

Amazon ECS tasks hosted on Fargate use the default resource limit values set by the operating system with the exception of the nofile resource limit parameter which Fargate overrides. The `nofile` resource limit sets a restriction on the number of open files that a container can use. The default `nofile` soft limit is `1024` and the default hard limit is `65535` .

This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version `--format '{{.Server.APIVersion}}'`

### Note

This parameter is not supported for Windows containers.

(structure)

The `ulimit` settings to pass to the container. For more information, see [Ulimit](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Ulimit.html) .

### Note

This object isnât applicable to jobs that are running on Fargate resources.

hardLimit -> (integer)

The hard limit for the `ulimit` type.

name -> (string)

The `type` of the `ulimit` . Valid values are: `core` | `cpu` | `data` | `fsize` | `locks` | `memlock` | `msgqueue` | `nice` | `nofile` | `nproc` | `rss` | `rtprio` | `rttime` | `sigpending` | `stack` .

softLimit -> (integer)

The soft limit for the `ulimit` type.

user -> (string)

The user to use inside the container. This parameter maps to User in the Create a container section of the Docker Remote API and the âuser option to docker run.

### Note

When running tasks using the `host` network mode, donât run containers using the `root user (UID 0)` . We recommend using a non-root user for better security.

You can specify the `user` using the following formats. If specifying a UID or GID, you must specify it as a positive integer.

- `user`
- `user:group`
- `uid`
- `uid:gid`
- `user:gi`
- `uid:group`

### Note

This parameter is not supported for Windows containers.

ephemeralStorage -> (structure)

The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on Fargate.

sizeInGiB -> (integer)

The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is `21` GiB and the maximum supported value is `200` GiB.

executionRoleArn -> (string)

The Amazon Resource Name (ARN) of the execution role that Batch can assume. For jobs that run on Fargate resources, you must provide an execution role. For more information, see [Batch execution IAM role](https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html) in the *Batch User Guide* .

platformVersion -> (string)

The Fargate platform version where the jobs are running. A platform version is specified only for jobs that are running on Fargate resources. If one isnât specified, the `LATEST` platform version is used by default. This uses a recent, approved version of the Fargate platform for compute resources. For more information, see [Fargate platform versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide* .

ipcMode -> (string)

The IPC resource namespace to use for the containers in the task. The valid values are `host` , `task` , or `none` .

If `host` is specified, all containers within the tasks that specified the `host` IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance.

If `task` is specified, all containers within the specified `task` share the same IPC resources.

If `none` is specified, the IPC resources within the containers of a task are private, and are not shared with other containers in a task or on the container instance.

If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance. For more information, see [IPC settings](https://docs.docker.com/engine/reference/run/#ipc-settings---ipc) in the Docker run reference.

taskRoleArn -> (string)

The Amazon Resource Name (ARN) thatâs associated with the Amazon ECS task.

### Note

This is object is comparable to [ContainerProperties:jobRoleArn](https://docs.aws.amazon.com/batch/latest/APIReference/API_ContainerProperties.html) .

pidMode -> (string)

The process namespace to use for the containers in the task. The valid values are `host` or `task` . For example, monitoring sidecars might need `pidMode` to access information about other containers running in the same task.

If `host` is specified, all containers within the tasks that specified the `host` PID mode on the same container instance share the process namespace with the host Amazon EC2 instance.

If `task` is specified, all containers within the specified task share the same process namespace.

If no value is specified, the default is a private namespace for each container. For more information, see [PID settings](https://docs.docker.com/engine/reference/run/#pid-settings---pid) in the Docker run reference.

networkConfiguration -> (structure)

The network configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.

assignPublicIp -> (string)

Indicates whether the job has a public IP address. For a job thatâs running on Fargate resources in a private subnet to send outbound traffic to the internet (for example, to pull container images), the private subnet requires a NAT gateway be attached to route requests to the internet. For more information, see [Amazon ECS task networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide* . The default value is â`DISABLED` â.

runtimePlatform -> (structure)

An object that represents the compute environment architecture for Batch jobs on Fargate.

operatingSystemFamily -> (string)

The operating system for the compute environment. Valid values are: `LINUX` (default), `WINDOWS_SERVER_2019_CORE` , `WINDOWS_SERVER_2019_FULL` , `WINDOWS_SERVER_2022_CORE` , and `WINDOWS_SERVER_2022_FULL` .

### Note

The following parameters canât be set for Windows containers: `linuxParameters` , `privileged` , `user` , `ulimits` , `readonlyRootFilesystem` , and `efsVolumeConfiguration` .

### Note

The Batch Scheduler checks the compute environments that are attached to the job queue before registering a task definition with Fargate. In this scenario, the job queue is where the job is submitted. If the job requires a Windows container and the first compute environment is `LINUX` , the compute environment is skipped and the next compute environment is checked until a Windows-based compute environment is found.

### Note

Fargate Spot is not supported for `ARM64` and Windows-based containers on Fargate. A job queue will be blocked if a Fargate `ARM64` or Windows job is submitted to a job queue with only Fargate Spot compute environments. However, you can attach both `FARGATE` and `FARGATE_SPOT` compute environments to the same job queue.

cpuArchitecture -> (string)

The vCPU architecture. The default value is `X86_64` . Valid values are `X86_64` and `ARM64` .

### Note

This parameter must be set to `X86_64` for Windows containers.

### Note

Fargate Spot is not supported for `ARM64` and Windows-based containers on Fargate. A job queue will be blocked if a Fargate `ARM64` or Windows job is submitted to a job queue with only Fargate Spot compute environments. However, you can attach both `FARGATE` and `FARGATE_SPOT` compute environments to the same job queue.

volumes -> (list)

A list of volumes that are associated with the job.

(structure)

A data volume thatâs used in a jobâs container properties.

host -> (structure)

The contents of the `host` parameter determine whether your data volume persists on the host container instance and where itâs stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data isnât guaranteed to persist after the containers that are associated with it stop running.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources and shouldnât be provided.

sourcePath -> (string)

The path on the host container instance thatâs presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If this parameter contains a file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the source path location doesnât exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.

### Note

This parameter isnât applicable to jobs that run on Fargate resources. Donât provide this for these jobs.

name -> (string)

The name of the volume. It can be up to 255 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_). This name is referenced in the `sourceVolume` parameter of container definition `mountPoints` .

efsVolumeConfiguration -> (structure)

This parameter is specified when youâre using an Amazon Elastic File System file system for job storage. Jobs that are running on Fargate resources must specify a `platformVersion` of at least `1.4.0` .

fileSystemId -> (string)

The Amazon EFS file system ID to use.

rootDirectory -> (string)

The directory within the Amazon EFS file system to mount as the root directory inside the host. If this parameter is omitted, the root of the Amazon EFS volume is used instead. Specifying `/` has the same effect as omitting this parameter. The maximum length is 4,096 characters.

### Warning

If an EFS access point is specified in the `authorizationConfig` , the root directory parameter must either be omitted or set to `/` , which enforces the path set on the Amazon EFS access point.

transitEncryption -> (string)

Determines whether to enable encryption for Amazon EFS data in transit between the Amazon ECS host and the Amazon EFS server. Transit encryption must be enabled if Amazon EFS IAM authorization is used. If this parameter is omitted, the default value of `DISABLED` is used. For more information, see [Encrypting data in transit](https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html) in the *Amazon Elastic File System User Guide* .

transitEncryptionPort -> (integer)

The port to use when sending encrypted data between the Amazon ECS host and the Amazon EFS server. If you donât specify a transit encryption port, it uses the port selection strategy that the Amazon EFS mount helper uses. The value must be between 0 and 65,535. For more information, see [EFS mount helper](https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html) in the *Amazon Elastic File System User Guide* .

authorizationConfig -> (structure)

The authorization configuration details for the Amazon EFS file system.

accessPointId -> (string)

The Amazon EFS access point ID to use. If an access point is specified, the root directory value specified in the `EFSVolumeConfiguration` must either be omitted or set to `/` which enforces the path set on the EFS access point. If an access point is used, transit encryption must be enabled in the `EFSVolumeConfiguration` . For more information, see [Working with Amazon EFS access points](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html) in the *Amazon Elastic File System User Guide* .

iam -> (string)

Whether or not to use the Batch job IAM role defined in a job definition when mounting the Amazon EFS file system. If enabled, transit encryption must be enabled in the `EFSVolumeConfiguration` . If this parameter is omitted, the default value of `DISABLED` is used. For more information, see [Using Amazon EFS access points](https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html#efs-volume-accesspoints) in the *Batch User Guide* . EFS IAM authorization requires that `TransitEncryption` be `ENABLED` and that a `JobRoleArn` is specified.

enableExecuteCommand -> (boolean)

Determines whether execute command functionality is turned on for this task. If `true` , execute command functionality is turned on all the containers in the task.

eksProperties -> (structure)

This is an object that represents the properties of the node range for a multi-node parallel job.

podProperties -> (structure)

The properties for the Kubernetes pod resources of a job.

serviceAccountName -> (string)

The name of the service account thatâs used to run the pod. For more information, see [Kubernetes service accounts](https://docs.aws.amazon.com/eks/latest/userguide/service-accounts.html) and [Configure a Kubernetes service account to assume an IAM role](https://docs.aws.amazon.com/eks/latest/userguide/associate-service-account-role.html) in the *Amazon EKS User Guide* and [Configure service accounts for pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) in the *Kubernetes documentation* .

hostNetwork -> (boolean)

Indicates if the pod uses the hostsâ network IP address. The default value is `true` . Setting this to `false` enables the Kubernetes pod networking model. Most Batch workloads are egress-only and donât require the overhead of IP allocation for each pod for incoming connections. For more information, see [Host namespaces](https://kubernetes.io/docs/concepts/security/pod-security-policy/#host-namespaces) and [Pod networking](https://kubernetes.io/docs/concepts/workloads/pods/#pod-networking) in the *Kubernetes documentation* .

dnsPolicy -> (string)

The DNS policy for the pod. The default value is `ClusterFirst` . If the `hostNetwork` parameter is not specified, the default is `ClusterFirstWithHostNet` . `ClusterFirst` indicates that any DNS query that does not match the configured cluster domain suffix is forwarded to the upstream nameserver inherited from the node. For more information, see [Podâs DNS policy](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pod-s-dns-policy) in the *Kubernetes documentation* .

Valid values: `Default` | `ClusterFirst` | `ClusterFirstWithHostNet`

imagePullSecrets -> (list)

References a Kubernetes secret resource. It holds a list of secrets. These secrets help to gain access to pull an images from a private registry.

`ImagePullSecret$name` is required when this object is used.

(structure)

References a Kubernetes secret resource. This name of the secret must start and end with an alphanumeric character, is required to be lowercase, can include periods (.) and hyphens (-), and canât contain more than 253 characters.

name -> (string)

Provides a unique identifier for the `ImagePullSecret` . This object is required when `EksPodProperties$imagePullSecrets` is used.

containers -> (list)

The properties of the container thatâs used on the Amazon EKS pod.

### Note

This object is limited to 10 elements.

(structure)

EKS container properties are used in job definitions for Amazon EKS based job definitions to describe the properties for a container node in the pod thatâs launched as part of a job. This canât be specified for Amazon ECS based job definitions.

name -> (string)

The name of the container. If the name isnât specified, the default name â`Default` â is used. Each container in a pod must have a unique name.

image -> (string)

The Docker image used to start the container.

imagePullPolicy -> (string)

The image pull policy for the container. Supported values are `Always` , `IfNotPresent` , and `Never` . This parameter defaults to `IfNotPresent` . However, if the `:latest` tag is specified, it defaults to `Always` . For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images) in the *Kubernetes documentation* .

command -> (list)

The entrypoint for the container. This isnât run within a shell. If this isnât specified, the `ENTRYPOINT` of the container image is used. Environment variable references are expanded using the containerâs environment.

If the referenced environment variable doesnât exist, the reference in the command isnât changed. For example, if the reference is to â`$(NAME1)` â and the `NAME1` environment variable doesnât exist, the command string will remain â`$(NAME1)` .â `$$` is replaced with `$` and the resulting string isnât expanded. For example, `$$(VAR_NAME)` will be passed as `$(VAR_NAME)` whether or not the `VAR_NAME` environment variable exists. The entrypoint canât be updated. For more information, see [ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint) in the *Dockerfile reference* and [Define a command and arguments for a container](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/) and [Entrypoint](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#entrypoint) in the *Kubernetes documentation* .

(string)

args -> (list)

An array of arguments to the entrypoint. If this isnât specified, the `CMD` of the container image is used. This corresponds to the `args` member in the [Entrypoint](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#entrypoint) portion of the [Pod](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/) in Kubernetes. Environment variable references are expanded using the containerâs environment.

If the referenced environment variable doesnât exist, the reference in the command isnât changed. For example, if the reference is to â`$(NAME1)` â and the `NAME1` environment variable doesnât exist, the command string will remain â`$(NAME1)` .â `$$` is replaced with `$` , and the resulting string isnât expanded. For example, `$$(VAR_NAME)` is passed as `$(VAR_NAME)` whether or not the `VAR_NAME` environment variable exists. For more information, see [Dockerfile reference: CMD](https://docs.docker.com/engine/reference/builder/#cmd) and [Define a command and arguments for a pod](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/) in the *Kubernetes documentation* .

(string)

env -> (list)

The environment variables to pass to a container.

### Note

Environment variables cannot start with â`AWS_BATCH` â. This naming convention is reserved for variables that Batch sets.

(structure)

An environment variable.

name -> (string)

The name of the environment variable.

value -> (string)

The value of the environment variable.

resources -> (structure)

The type and amount of resources to assign to a container. The supported resources include `memory` , `cpu` , and `nvidia.com/gpu` . For more information, see [Resource management for pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) in the *Kubernetes documentation* .

limits -> (map)

The type and quantity of the resources to reserve for the container. The values vary based on the `name` thatâs specified. Resources can be requested using either the `limits` or the `requests` objects.

memory

The memory hard limit (in MiB) for the container, using whole integers, with a âMiâ suffix. If your container attempts to exceed the memory specified, the container is terminated. You must specify at least 4 MiB of memory for a job. `memory` can be specified in `limits` , `requests` , or both. If `memory` is specified in both places, then the value thatâs specified in `limits` must be equal to the value thatâs specified in `requests` .

### Note

To maximize your resource utilization, provide your jobs with as much memory as possible for the specific instance type that you are using. To learn how, see [Memory management](https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html) in the *Batch User Guide* .

cpu

The number of CPUs thatâs reserved for the container. Values must be an even multiple of `0.25` . `cpu` can be specified in `limits` , `requests` , or both. If `cpu` is specified in both places, then the value thatâs specified in `limits` must be at least as large as the value thatâs specified in `requests` .

nvidia.com/gpu

The number of GPUs thatâs reserved for the container. Values must be a whole integer. `memory` can be specified in `limits` , `requests` , or both. If `memory` is specified in both places, then the value thatâs specified in `limits` must be equal to the value thatâs specified in `requests` .

key -> (string)

value -> (string)

requests -> (map)

The type and quantity of the resources to request for the container. The values vary based on the `name` thatâs specified. Resources can be requested by using either the `limits` or the `requests` objects.

memory

The memory hard limit (in MiB) for the container, using whole integers, with a âMiâ suffix. If your container attempts to exceed the memory specified, the container is terminated. You must specify at least 4 MiB of memory for a job. `memory` can be specified in `limits` , `requests` , or both. If `memory` is specified in both, then the value thatâs specified in `limits` must be equal to the value thatâs specified in `requests` .

### Note

If youâre trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see [Memory management](https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html) in the *Batch User Guide* .

cpu

The number of CPUs that are reserved for the container. Values must be an even multiple of `0.25` . `cpu` can be specified in `limits` , `requests` , or both. If `cpu` is specified in both, then the value thatâs specified in `limits` must be at least as large as the value thatâs specified in `requests` .

nvidia.com/gpu

The number of GPUs that are reserved for the container. Values must be a whole integer. `nvidia.com/gpu` can be specified in `limits` , `requests` , or both. If `nvidia.com/gpu` is specified in both, then the value thatâs specified in `limits` must be equal to the value thatâs specified in `requests` .

key -> (string)

value -> (string)

volumeMounts -> (list)

The volume mounts for the container. Batch supports `emptyDir` , `hostPath` , and `secret` volume types. For more information about volumes and volume mounts in Kubernetes, see [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/) in the *Kubernetes documentation* .

(structure)

The volume mounts for a container for an Amazon EKS job. For more information about volumes and volume mounts in Kubernetes, see [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/) in the *Kubernetes documentation* .

name -> (string)

The name the volume mount. This must match the name of one of the volumes in the pod.

mountPath -> (string)

The path on the container where the volume is mounted.

subPath -> (string)

A sub-path inside the referenced volume instead of its root.

readOnly -> (boolean)

If this value is `true` , the container has read-only access to the volume. Otherwise, the container can write to the volume. The default value is `false` .

securityContext -> (structure)

The security context for a job. For more information, see [Configure a security context for a pod or container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) in the *Kubernetes documentation* .

runAsUser -> (long)

When this parameter is specified, the container is run as the specified user ID (`uid` ). If this parameter isnât specified, the default is the user thatâs specified in the image metadata. This parameter maps to `RunAsUser` and `MustRanAs` policy in the [Users and groups pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups) in the *Kubernetes documentation* .

runAsGroup -> (long)

When this parameter is specified, the container is run as the specified group ID (`gid` ). If this parameter isnât specified, the default is the group thatâs specified in the image metadata. This parameter maps to `RunAsGroup` and `MustRunAs` policy in the [Users and groups pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups) in the *Kubernetes documentation* .

privileged -> (boolean)

When this parameter is `true` , the container is given elevated permissions on the host container instance. The level of permissions are similar to the `root` user permissions. The default value is `false` . This parameter maps to `privileged` policy in the [Privileged pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#privileged) in the *Kubernetes documentation* .

allowPrivilegeEscalation -> (boolean)

Whether or not a container or a Kubernetes pod is allowed to gain more privileges than its parent process. The default value is `false` .

readOnlyRootFilesystem -> (boolean)

When this parameter is `true` , the container is given read-only access to its root file system. The default value is `false` . This parameter maps to `ReadOnlyRootFilesystem` policy in the [Volumes and file systems pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#volumes-and-file-systems) in the *Kubernetes documentation* .

runAsNonRoot -> (boolean)

When this parameter is specified, the container is run as a user with a `uid` other than 0. If this parameter isnât specified, so such rule is enforced. This parameter maps to `RunAsUser` and `MustRunAsNonRoot` policy in the [Users and groups pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups) in the *Kubernetes documentation* .

initContainers -> (list)

These containers run before application containers, always runs to completion, and must complete successfully before the next container starts. These containers are registered with the Amazon EKS Connector agent and persists the registration information in the Kubernetes backend data store. For more information, see [Init Containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) in the *Kubernetes documentation* .

### Note

This object is limited to 10 elements.

(structure)

EKS container properties are used in job definitions for Amazon EKS based job definitions to describe the properties for a container node in the pod thatâs launched as part of a job. This canât be specified for Amazon ECS based job definitions.

name -> (string)

The name of the container. If the name isnât specified, the default name â`Default` â is used. Each container in a pod must have a unique name.

image -> (string)

The Docker image used to start the container.

imagePullPolicy -> (string)

The image pull policy for the container. Supported values are `Always` , `IfNotPresent` , and `Never` . This parameter defaults to `IfNotPresent` . However, if the `:latest` tag is specified, it defaults to `Always` . For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images) in the *Kubernetes documentation* .

command -> (list)

The entrypoint for the container. This isnât run within a shell. If this isnât specified, the `ENTRYPOINT` of the container image is used. Environment variable references are expanded using the containerâs environment.

If the referenced environment variable doesnât exist, the reference in the command isnât changed. For example, if the reference is to â`$(NAME1)` â and the `NAME1` environment variable doesnât exist, the command string will remain â`$(NAME1)` .â `$$` is replaced with `$` and the resulting string isnât expanded. For example, `$$(VAR_NAME)` will be passed as `$(VAR_NAME)` whether or not the `VAR_NAME` environment variable exists. The entrypoint canât be updated. For more information, see [ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint) in the *Dockerfile reference* and [Define a command and arguments for a container](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/) and [Entrypoint](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#entrypoint) in the *Kubernetes documentation* .

(string)

args -> (list)

An array of arguments to the entrypoint. If this isnât specified, the `CMD` of the container image is used. This corresponds to the `args` member in the [Entrypoint](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#entrypoint) portion of the [Pod](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/) in Kubernetes. Environment variable references are expanded using the containerâs environment.

If the referenced environment variable doesnât exist, the reference in the command isnât changed. For example, if the reference is to â`$(NAME1)` â and the `NAME1` environment variable doesnât exist, the command string will remain â`$(NAME1)` .â `$$` is replaced with `$` , and the resulting string isnât expanded. For example, `$$(VAR_NAME)` is passed as `$(VAR_NAME)` whether or not the `VAR_NAME` environment variable exists. For more information, see [Dockerfile reference: CMD](https://docs.docker.com/engine/reference/builder/#cmd) and [Define a command and arguments for a pod](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/) in the *Kubernetes documentation* .

(string)

env -> (list)

The environment variables to pass to a container.

### Note

Environment variables cannot start with â`AWS_BATCH` â. This naming convention is reserved for variables that Batch sets.

(structure)

An environment variable.

name -> (string)

The name of the environment variable.

value -> (string)

The value of the environment variable.

resources -> (structure)

The type and amount of resources to assign to a container. The supported resources include `memory` , `cpu` , and `nvidia.com/gpu` . For more information, see [Resource management for pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) in the *Kubernetes documentation* .

limits -> (map)

The type and quantity of the resources to reserve for the container. The values vary based on the `name` thatâs specified. Resources can be requested using either the `limits` or the `requests` objects.

memory

The memory hard limit (in MiB) for the container, using whole integers, with a âMiâ suffix. If your container attempts to exceed the memory specified, the container is terminated. You must specify at least 4 MiB of memory for a job. `memory` can be specified in `limits` , `requests` , or both. If `memory` is specified in both places, then the value thatâs specified in `limits` must be equal to the value thatâs specified in `requests` .

### Note

To maximize your resource utilization, provide your jobs with as much memory as possible for the specific instance type that you are using. To learn how, see [Memory management](https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html) in the *Batch User Guide* .

cpu

The number of CPUs thatâs reserved for the container. Values must be an even multiple of `0.25` . `cpu` can be specified in `limits` , `requests` , or both. If `cpu` is specified in both places, then the value thatâs specified in `limits` must be at least as large as the value thatâs specified in `requests` .

nvidia.com/gpu

The number of GPUs thatâs reserved for the container. Values must be a whole integer. `memory` can be specified in `limits` , `requests` , or both. If `memory` is specified in both places, then the value thatâs specified in `limits` must be equal to the value thatâs specified in `requests` .

key -> (string)

value -> (string)

requests -> (map)

The type and quantity of the resources to request for the container. The values vary based on the `name` thatâs specified. Resources can be requested by using either the `limits` or the `requests` objects.

memory

The memory hard limit (in MiB) for the container, using whole integers, with a âMiâ suffix. If your container attempts to exceed the memory specified, the container is terminated. You must specify at least 4 MiB of memory for a job. `memory` can be specified in `limits` , `requests` , or both. If `memory` is specified in both, then the value thatâs specified in `limits` must be equal to the value thatâs specified in `requests` .

### Note

If youâre trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see [Memory management](https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html) in the *Batch User Guide* .

cpu

The number of CPUs that are reserved for the container. Values must be an even multiple of `0.25` . `cpu` can be specified in `limits` , `requests` , or both. If `cpu` is specified in both, then the value thatâs specified in `limits` must be at least as large as the value thatâs specified in `requests` .

nvidia.com/gpu

The number of GPUs that are reserved for the container. Values must be a whole integer. `nvidia.com/gpu` can be specified in `limits` , `requests` , or both. If `nvidia.com/gpu` is specified in both, then the value thatâs specified in `limits` must be equal to the value thatâs specified in `requests` .

key -> (string)

value -> (string)

volumeMounts -> (list)

The volume mounts for the container. Batch supports `emptyDir` , `hostPath` , and `secret` volume types. For more information about volumes and volume mounts in Kubernetes, see [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/) in the *Kubernetes documentation* .

(structure)

The volume mounts for a container for an Amazon EKS job. For more information about volumes and volume mounts in Kubernetes, see [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/) in the *Kubernetes documentation* .

name -> (string)

The name the volume mount. This must match the name of one of the volumes in the pod.

mountPath -> (string)

The path on the container where the volume is mounted.

subPath -> (string)

A sub-path inside the referenced volume instead of its root.

readOnly -> (boolean)

If this value is `true` , the container has read-only access to the volume. Otherwise, the container can write to the volume. The default value is `false` .

securityContext -> (structure)

The security context for a job. For more information, see [Configure a security context for a pod or container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) in the *Kubernetes documentation* .

runAsUser -> (long)

When this parameter is specified, the container is run as the specified user ID (`uid` ). If this parameter isnât specified, the default is the user thatâs specified in the image metadata. This parameter maps to `RunAsUser` and `MustRanAs` policy in the [Users and groups pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups) in the *Kubernetes documentation* .

runAsGroup -> (long)

When this parameter is specified, the container is run as the specified group ID (`gid` ). If this parameter isnât specified, the default is the group thatâs specified in the image metadata. This parameter maps to `RunAsGroup` and `MustRunAs` policy in the [Users and groups pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups) in the *Kubernetes documentation* .

privileged -> (boolean)

When this parameter is `true` , the container is given elevated permissions on the host container instance. The level of permissions are similar to the `root` user permissions. The default value is `false` . This parameter maps to `privileged` policy in the [Privileged pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#privileged) in the *Kubernetes documentation* .

allowPrivilegeEscalation -> (boolean)

Whether or not a container or a Kubernetes pod is allowed to gain more privileges than its parent process. The default value is `false` .

readOnlyRootFilesystem -> (boolean)

When this parameter is `true` , the container is given read-only access to its root file system. The default value is `false` . This parameter maps to `ReadOnlyRootFilesystem` policy in the [Volumes and file systems pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#volumes-and-file-systems) in the *Kubernetes documentation* .

runAsNonRoot -> (boolean)

When this parameter is specified, the container is run as a user with a `uid` other than 0. If this parameter isnât specified, so such rule is enforced. This parameter maps to `RunAsUser` and `MustRunAsNonRoot` policy in the [Users and groups pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups) in the *Kubernetes documentation* .

volumes -> (list)

Specifies the volumes for a job definition that uses Amazon EKS resources.

(structure)

Specifies an Amazon EKS volume for a job definition.

name -> (string)

The name of the volume. The name must be allowed as a DNS subdomain name. For more information, see [DNS subdomain names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names) in the *Kubernetes documentation* .

hostPath -> (structure)

Specifies the configuration of a Kubernetes `hostPath` volume. For more information, see [hostPath](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath) in the *Kubernetes documentation* .

path -> (string)

The path of the file or directory on the host to mount into containers on the pod.

emptyDir -> (structure)

Specifies the configuration of a Kubernetes `emptyDir` volume. For more information, see [emptyDir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) in the *Kubernetes documentation* .

medium -> (string)

The medium to store the volume. The default value is an empty string, which uses the storage of the node.

ââ

**(Default)** Use the disk storage of the node.

âMemoryâ

Use the `tmpfs` volume thatâs backed by the RAM of the node. Contents of the volume are lost when the node reboots, and any storage on the volume counts against the containerâs memory limit.

sizeLimit -> (string)

The maximum size of the volume. By default, thereâs no maximum size defined.

secret -> (structure)

Specifies the configuration of a Kubernetes `secret` volume. For more information, see [secret](https://kubernetes.io/docs/concepts/storage/volumes/#secret) in the *Kubernetes documentation* .

secretName -> (string)

The name of the secret. The name must be allowed as a DNS subdomain name. For more information, see [DNS subdomain names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names) in the *Kubernetes documentation* .

optional -> (boolean)

Specifies whether the secret or the secretâs keys must be defined.

persistentVolumeClaim -> (structure)

Specifies the configuration of a Kubernetes `persistentVolumeClaim` bounded to a `persistentVolume` . For more information, see [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) in the *Kubernetes documentation* .

claimName -> (string)

The name of the `persistentVolumeClaim` bounded to a `persistentVolume` . For more information, see [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) in the *Kubernetes documentation* .

readOnly -> (boolean)

An optional boolean value indicating if the mount is read only. Default is false. For more information, see [Read Only Mounts](https://kubernetes.io/docs/concepts/storage/volumes/#read-only-mounts) in the *Kubernetes documentation* .

metadata -> (structure)

Metadata about the Kubernetes pod. For more information, see [Understanding Kubernetes Objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) in the *Kubernetes documentation* .

labels -> (map)

Key-value pairs used to identify, sort, and organize cube resources. Can contain up to 63 uppercase letters, lowercase letters, numbers, hyphens (-), and underscores (_). Labels can be added or modified at any time. Each resource can have multiple labels, but each key must be unique for a given object.

key -> (string)

value -> (string)

annotations -> (map)

Key-value pairs used to attach arbitrary, non-identifying metadata to Kubernetes objects. Valid annotation keys have two segments: an optional prefix and a name, separated by a slash (/).

- The prefix is optional and must be 253 characters or less. If specified, the prefix must be a DNS subdomainâ a series of DNS labels separated by dots (.), and it must end with a slash (/).
- The name segment is required and must be 63 characters or less. It can include alphanumeric characters ([a-z0-9A-Z]), dashes (-), underscores (_), and dots (.), but must begin and end with an alphanumeric character.

### Note

Annotation values must be 255 characters or less.

Annotations can be added or modified at any time. Each resource can have multiple annotations.

key -> (string)

value -> (string)

namespace -> (string)

The namespace of the Amazon EKS cluster. In Kubernetes, namespaces provide a mechanism for isolating groups of resources within a single cluster. Names of resources need to be unique within a namespace, but not across namespaces. Batch places Batch Job pods in this namespace. If this field is provided, the value canât be empty or null. It must meet the following requirements:

- 1-63 characters long
- Canât be set to default
- Canât start with `kube`
- Must match the following regular expression: `^[a-z0-9]([-a-z0-9]*[a-z0-9])?$`

For more information, see [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) in the *Kubernetes documentation* . This namespace can be different from the `kubernetesNamespace` set in the compute environmentâs `EksConfiguration` , but must have identical role-based access control (RBAC) roles as the compute environmentâs `kubernetesNamespace` . For multi-node parallel jobs, the same value must be provided across all the node ranges.

shareProcessNamespace -> (boolean)

Indicates if the processes in a container are shared, or visible, to other containers in the same pod. For more information, see [Share Process Namespace between Containers in a Pod](https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/) .

consumableResourceProperties -> (structure)

Contains a list of consumable resources required by a job.

consumableResourceList -> (list)

The list of consumable resources required by a job.

(structure)

Information about a consumable resource required to run a job.

consumableResource -> (string)

The name or ARN of the consumable resource.

quantity -> (long)

The quantity of the consumable resource that is needed.

JSON Syntax:

```
{
  "numNodes": integer,
  "mainNode": integer,
  "nodeRangeProperties": [
    {
      "targetNodes": "string",
      "container": {
        "image": "string",
        "vcpus": integer,
        "memory": integer,
        "command": ["string", ...],
        "jobRoleArn": "string",
        "executionRoleArn": "string",
        "volumes": [
          {
            "host": {
              "sourcePath": "string"
            },
            "name": "string",
            "efsVolumeConfiguration": {
              "fileSystemId": "string",
              "rootDirectory": "string",
              "transitEncryption": "ENABLED"|"DISABLED",
              "transitEncryptionPort": integer,
              "authorizationConfig": {
                "accessPointId": "string",
                "iam": "ENABLED"|"DISABLED"
              }
            }
          }
          ...
        ],
        "environment": [
          {
            "name": "string",
            "value": "string"
          }
          ...
        ],
        "mountPoints": [
          {
            "containerPath": "string",
            "readOnly": true|false,
            "sourceVolume": "string"
          }
          ...
        ],
        "readonlyRootFilesystem": true|false,
        "privileged": true|false,
        "ulimits": [
          {
            "hardLimit": integer,
            "name": "string",
            "softLimit": integer
          }
          ...
        ],
        "user": "string",
        "instanceType": "string",
        "resourceRequirements": [
          {
            "value": "string",
            "type": "GPU"|"VCPU"|"MEMORY"
          }
          ...
        ],
        "linuxParameters": {
          "devices": [
            {
              "hostPath": "string",
              "containerPath": "string",
              "permissions": ["READ"|"WRITE"|"MKNOD", ...]
            }
            ...
          ],
          "initProcessEnabled": true|false,
          "sharedMemorySize": integer,
          "tmpfs": [
            {
              "containerPath": "string",
              "size": integer,
              "mountOptions": ["string", ...]
            }
            ...
          ],
          "maxSwap": integer,
          "swappiness": integer
        },
        "logConfiguration": {
          "logDriver": "json-file"|"syslog"|"journald"|"gelf"|"fluentd"|"awslogs"|"splunk"|"awsfirelens",
          "options": {"string": "string"
            ...},
          "secretOptions": [
            {
              "name": "string",
              "valueFrom": "string"
            }
            ...
          ]
        },
        "secrets": [
          {
            "name": "string",
            "valueFrom": "string"
          }
          ...
        ],
        "networkConfiguration": {
          "assignPublicIp": "ENABLED"|"DISABLED"
        },
        "fargatePlatformConfiguration": {
          "platformVersion": "string"
        },
        "enableExecuteCommand": true|false,
        "ephemeralStorage": {
          "sizeInGiB": integer
        },
        "runtimePlatform": {
          "operatingSystemFamily": "string",
          "cpuArchitecture": "string"
        },
        "repositoryCredentials": {
          "credentialsParameter": "string"
        }
      },
      "instanceTypes": ["string", ...],
      "ecsProperties": {
        "taskProperties": [
          {
            "containers": [
              {
                "command": ["string", ...],
                "dependsOn": [
                  {
                    "containerName": "string",
                    "condition": "string"
                  }
                  ...
                ],
                "environment": [
                  {
                    "name": "string",
                    "value": "string"
                  }
                  ...
                ],
                "essential": true|false,
                "firelensConfiguration": {
                  "type": "fluentd"|"fluentbit",
                  "options": {"string": "string"
                    ...}
                },
                "image": "string",
                "linuxParameters": {
                  "devices": [
                    {
                      "hostPath": "string",
                      "containerPath": "string",
                      "permissions": ["READ"|"WRITE"|"MKNOD", ...]
                    }
                    ...
                  ],
                  "initProcessEnabled": true|false,
                  "sharedMemorySize": integer,
                  "tmpfs": [
                    {
                      "containerPath": "string",
                      "size": integer,
                      "mountOptions": ["string", ...]
                    }
                    ...
                  ],
                  "maxSwap": integer,
                  "swappiness": integer
                },
                "logConfiguration": {
                  "logDriver": "json-file"|"syslog"|"journald"|"gelf"|"fluentd"|"awslogs"|"splunk"|"awsfirelens",
                  "options": {"string": "string"
                    ...},
                  "secretOptions": [
                    {
                      "name": "string",
                      "valueFrom": "string"
                    }
                    ...
                  ]
                },
                "mountPoints": [
                  {
                    "containerPath": "string",
                    "readOnly": true|false,
                    "sourceVolume": "string"
                  }
                  ...
                ],
                "name": "string",
                "privileged": true|false,
                "readonlyRootFilesystem": true|false,
                "repositoryCredentials": {
                  "credentialsParameter": "string"
                },
                "resourceRequirements": [
                  {
                    "value": "string",
                    "type": "GPU"|"VCPU"|"MEMORY"
                  }
                  ...
                ],
                "secrets": [
                  {
                    "name": "string",
                    "valueFrom": "string"
                  }
                  ...
                ],
                "ulimits": [
                  {
                    "hardLimit": integer,
                    "name": "string",
                    "softLimit": integer
                  }
                  ...
                ],
                "user": "string"
              }
              ...
            ],
            "ephemeralStorage": {
              "sizeInGiB": integer
            },
            "executionRoleArn": "string",
            "platformVersion": "string",
            "ipcMode": "string",
            "taskRoleArn": "string",
            "pidMode": "string",
            "networkConfiguration": {
              "assignPublicIp": "ENABLED"|"DISABLED"
            },
            "runtimePlatform": {
              "operatingSystemFamily": "string",
              "cpuArchitecture": "string"
            },
            "volumes": [
              {
                "host": {
                  "sourcePath": "string"
                },
                "name": "string",
                "efsVolumeConfiguration": {
                  "fileSystemId": "string",
                  "rootDirectory": "string",
                  "transitEncryption": "ENABLED"|"DISABLED",
                  "transitEncryptionPort": integer,
                  "authorizationConfig": {
                    "accessPointId": "string",
                    "iam": "ENABLED"|"DISABLED"
                  }
                }
              }
              ...
            ],
            "enableExecuteCommand": true|false
          }
          ...
        ]
      },
      "eksProperties": {
        "podProperties": {
          "serviceAccountName": "string",
          "hostNetwork": true|false,
          "dnsPolicy": "string",
          "imagePullSecrets": [
            {
              "name": "string"
            }
            ...
          ],
          "containers": [
            {
              "name": "string",
              "image": "string",
              "imagePullPolicy": "string",
              "command": ["string", ...],
              "args": ["string", ...],
              "env": [
                {
                  "name": "string",
                  "value": "string"
                }
                ...
              ],
              "resources": {
                "limits": {"string": "string"
                  ...},
                "requests": {"string": "string"
                  ...}
              },
              "volumeMounts": [
                {
                  "name": "string",
                  "mountPath": "string",
                  "subPath": "string",
                  "readOnly": true|false
                }
                ...
              ],
              "securityContext": {
                "runAsUser": long,
                "runAsGroup": long,
                "privileged": true|false,
                "allowPrivilegeEscalation": true|false,
                "readOnlyRootFilesystem": true|false,
                "runAsNonRoot": true|false
              }
            }
            ...
          ],
          "initContainers": [
            {
              "name": "string",
              "image": "string",
              "imagePullPolicy": "string",
              "command": ["string", ...],
              "args": ["string", ...],
              "env": [
                {
                  "name": "string",
                  "value": "string"
                }
                ...
              ],
              "resources": {
                "limits": {"string": "string"
                  ...},
                "requests": {"string": "string"
                  ...}
              },
              "volumeMounts": [
                {
                  "name": "string",
                  "mountPath": "string",
                  "subPath": "string",
                  "readOnly": true|false
                }
                ...
              ],
              "securityContext": {
                "runAsUser": long,
                "runAsGroup": long,
                "privileged": true|false,
                "allowPrivilegeEscalation": true|false,
                "readOnlyRootFilesystem": true|false,
                "runAsNonRoot": true|false
              }
            }
            ...
          ],
          "volumes": [
            {
              "name": "string",
              "hostPath": {
                "path": "string"
              },
              "emptyDir": {
                "medium": "string",
                "sizeLimit": "string"
              },
              "secret": {
                "secretName": "string",
                "optional": true|false
              },
              "persistentVolumeClaim": {
                "claimName": "string",
                "readOnly": true|false
              }
            }
            ...
          ],
          "metadata": {
            "labels": {"string": "string"
              ...},
            "annotations": {"string": "string"
              ...},
            "namespace": "string"
          },
          "shareProcessNamespace": true|false
        }
      },
      "consumableResourceProperties": {
        "consumableResourceList": [
          {
            "consumableResource": "string",
            "quantity": long
          }
          ...
        ]
      }
    }
    ...
  ]
}
```

`--retry-strategy` (structure)

The retry strategy to use for failed jobs that are submitted with this job definition. Any retry strategy thatâs specified during a  SubmitJob operation overrides the retry strategy defined here. If a job is terminated due to a timeout, it isnât retried.

attempts -> (integer)

The number of times to move a job to the `RUNNABLE` status. You can specify between 1 and 10 attempts. If the value of `attempts` is greater than one, the job is retried on failure the same number of attempts as the value.

evaluateOnExit -> (list)

Array of up to 5 objects that specify the conditions where jobs are retried or failed. If this parameter is specified, then the `attempts` parameter must also be specified. If none of the listed conditions match, then the job is retried.

(structure)

Specifies an array of up to 5 conditions to be met, and an action to take (`RETRY` or `EXIT` ) if all conditions are met. If none of the `EvaluateOnExit` conditions in a `RetryStrategy` match, then the job is retried.

onStatusReason -> (string)

Contains a glob pattern to match against the `StatusReason` returned for a job. The pattern can contain up to 512 characters. It can contain letters, numbers, periods (.), colons (:), and white spaces (including spaces or tabs). It can optionally end with an asterisk (*) so that only the start of the string needs to be an exact match.

onReason -> (string)

Contains a glob pattern to match against the `Reason` returned for a job. The pattern can contain up to 512 characters. It can contain letters, numbers, periods (.), colons (:), and white space (including spaces and tabs). It can optionally end with an asterisk (*) so that only the start of the string needs to be an exact match.

onExitCode -> (string)

Contains a glob pattern to match against the decimal representation of the `ExitCode` returned for a job. The pattern can be up to 512 characters long. It can contain only numbers, and can end with an asterisk (*) so that only the start of the string needs to be an exact match.

The string can contain up to 512 characters.

action -> (string)

Specifies the action to take if all of the specified conditions (`onStatusReason` , `onReason` , and `onExitCode` ) are met. The values arenât case sensitive.

Shorthand Syntax:

```
attempts=integer,evaluateOnExit=[{onStatusReason=string,onReason=string,onExitCode=string,action=string},{onStatusReason=string,onReason=string,onExitCode=string,action=string}]
```

JSON Syntax:

```
{
  "attempts": integer,
  "evaluateOnExit": [
    {
      "onStatusReason": "string",
      "onReason": "string",
      "onExitCode": "string",
      "action": "RETRY"|"EXIT"
    }
    ...
  ]
}
```

`--propagate-tags` | `--no-propagate-tags` (boolean)

Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags are not propagated. Tags can only be propagated to the tasks during task creation. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the `FAILED` state.

### Note

If the job runs on Amazon EKS resources, then you must not specify `propagateTags` .

`--timeout` (structure)

The timeout configuration for jobs that are submitted with this job definition, after which Batch terminates your jobs if they have not finished. If a job is terminated due to a timeout, it isnât retried. The minimum value for the timeout is 60 seconds. Any timeout configuration thatâs specified during a  SubmitJob operation overrides the timeout configuration defined here. For more information, see [Job Timeouts](https://docs.aws.amazon.com/batch/latest/userguide/job_timeouts.html) in the *Batch User Guide* .

attemptDurationSeconds -> (integer)

The job timeout time (in seconds) thatâs measured from the job attemptâs `startedAt` timestamp. After this time passes, Batch terminates your jobs if they arenât finished. The minimum value for the timeout is 60 seconds.

For array jobs, the timeout applies to the child jobs, not to the parent array job.

For multi-node parallel (MNP) jobs, the timeout applies to the whole job, not to the individual nodes.

Shorthand Syntax:

```
attemptDurationSeconds=integer
```

JSON Syntax:

```
{
  "attemptDurationSeconds": integer
}
```

`--tags` (map)

The tags that you apply to the job definition to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see [Tagging Amazon Web Services Resources](https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html) in *Batch User Guide* .

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--platform-capabilities` (list)

The platform capabilities required by the job definition. If no value is specified, it defaults to `EC2` . To run the job on Fargate resources, specify `FARGATE` .

### Note

If the job runs on Amazon EKS resources, then you must not specify `platformCapabilities` .

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  EC2
  FARGATE
```

`--eks-properties` (structure)

An object with properties that are specific to Amazon EKS-based jobs. This must not be specified for Amazon ECS based job definitions.

podProperties -> (structure)

The properties for the Kubernetes pod resources of a job.

serviceAccountName -> (string)

The name of the service account thatâs used to run the pod. For more information, see [Kubernetes service accounts](https://docs.aws.amazon.com/eks/latest/userguide/service-accounts.html) and [Configure a Kubernetes service account to assume an IAM role](https://docs.aws.amazon.com/eks/latest/userguide/associate-service-account-role.html) in the *Amazon EKS User Guide* and [Configure service accounts for pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) in the *Kubernetes documentation* .

hostNetwork -> (boolean)

Indicates if the pod uses the hostsâ network IP address. The default value is `true` . Setting this to `false` enables the Kubernetes pod networking model. Most Batch workloads are egress-only and donât require the overhead of IP allocation for each pod for incoming connections. For more information, see [Host namespaces](https://kubernetes.io/docs/concepts/security/pod-security-policy/#host-namespaces) and [Pod networking](https://kubernetes.io/docs/concepts/workloads/pods/#pod-networking) in the *Kubernetes documentation* .

dnsPolicy -> (string)

The DNS policy for the pod. The default value is `ClusterFirst` . If the `hostNetwork` parameter is not specified, the default is `ClusterFirstWithHostNet` . `ClusterFirst` indicates that any DNS query that does not match the configured cluster domain suffix is forwarded to the upstream nameserver inherited from the node. For more information, see [Podâs DNS policy](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pod-s-dns-policy) in the *Kubernetes documentation* .

Valid values: `Default` | `ClusterFirst` | `ClusterFirstWithHostNet`

imagePullSecrets -> (list)

References a Kubernetes secret resource. It holds a list of secrets. These secrets help to gain access to pull an images from a private registry.

`ImagePullSecret$name` is required when this object is used.

(structure)

References a Kubernetes secret resource. This name of the secret must start and end with an alphanumeric character, is required to be lowercase, can include periods (.) and hyphens (-), and canât contain more than 253 characters.

name -> (string)

Provides a unique identifier for the `ImagePullSecret` . This object is required when `EksPodProperties$imagePullSecrets` is used.

containers -> (list)

The properties of the container thatâs used on the Amazon EKS pod.

### Note

This object is limited to 10 elements.

(structure)

EKS container properties are used in job definitions for Amazon EKS based job definitions to describe the properties for a container node in the pod thatâs launched as part of a job. This canât be specified for Amazon ECS based job definitions.

name -> (string)

The name of the container. If the name isnât specified, the default name â`Default` â is used. Each container in a pod must have a unique name.

image -> (string)

The Docker image used to start the container.

imagePullPolicy -> (string)

The image pull policy for the container. Supported values are `Always` , `IfNotPresent` , and `Never` . This parameter defaults to `IfNotPresent` . However, if the `:latest` tag is specified, it defaults to `Always` . For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images) in the *Kubernetes documentation* .

command -> (list)

The entrypoint for the container. This isnât run within a shell. If this isnât specified, the `ENTRYPOINT` of the container image is used. Environment variable references are expanded using the containerâs environment.

If the referenced environment variable doesnât exist, the reference in the command isnât changed. For example, if the reference is to â`$(NAME1)` â and the `NAME1` environment variable doesnât exist, the command string will remain â`$(NAME1)` .â `$$` is replaced with `$` and the resulting string isnât expanded. For example, `$$(VAR_NAME)` will be passed as `$(VAR_NAME)` whether or not the `VAR_NAME` environment variable exists. The entrypoint canât be updated. For more information, see [ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint) in the *Dockerfile reference* and [Define a command and arguments for a container](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/) and [Entrypoint](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#entrypoint) in the *Kubernetes documentation* .

(string)

args -> (list)

An array of arguments to the entrypoint. If this isnât specified, the `CMD` of the container image is used. This corresponds to the `args` member in the [Entrypoint](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#entrypoint) portion of the [Pod](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/) in Kubernetes. Environment variable references are expanded using the containerâs environment.

If the referenced environment variable doesnât exist, the reference in the command isnât changed. For example, if the reference is to â`$(NAME1)` â and the `NAME1` environment variable doesnât exist, the command string will remain â`$(NAME1)` .â `$$` is replaced with `$` , and the resulting string isnât expanded. For example, `$$(VAR_NAME)` is passed as `$(VAR_NAME)` whether or not the `VAR_NAME` environment variable exists. For more information, see [Dockerfile reference: CMD](https://docs.docker.com/engine/reference/builder/#cmd) and [Define a command and arguments for a pod](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/) in the *Kubernetes documentation* .

(string)

env -> (list)

The environment variables to pass to a container.

### Note

Environment variables cannot start with â`AWS_BATCH` â. This naming convention is reserved for variables that Batch sets.

(structure)

An environment variable.

name -> (string)

The name of the environment variable.

value -> (string)

The value of the environment variable.

resources -> (structure)

The type and amount of resources to assign to a container. The supported resources include `memory` , `cpu` , and `nvidia.com/gpu` . For more information, see [Resource management for pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) in the *Kubernetes documentation* .

limits -> (map)

The type and quantity of the resources to reserve for the container. The values vary based on the `name` thatâs specified. Resources can be requested using either the `limits` or the `requests` objects.

memory

The memory hard limit (in MiB) for the container, using whole integers, with a âMiâ suffix. If your container attempts to exceed the memory specified, the container is terminated. You must specify at least 4 MiB of memory for a job. `memory` can be specified in `limits` , `requests` , or both. If `memory` is specified in both places, then the value thatâs specified in `limits` must be equal to the value thatâs specified in `requests` .

### Note

To maximize your resource utilization, provide your jobs with as much memory as possible for the specific instance type that you are using. To learn how, see [Memory management](https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html) in the *Batch User Guide* .

cpu

The number of CPUs thatâs reserved for the container. Values must be an even multiple of `0.25` . `cpu` can be specified in `limits` , `requests` , or both. If `cpu` is specified in both places, then the value thatâs specified in `limits` must be at least as large as the value thatâs specified in `requests` .

nvidia.com/gpu

The number of GPUs thatâs reserved for the container. Values must be a whole integer. `memory` can be specified in `limits` , `requests` , or both. If `memory` is specified in both places, then the value thatâs specified in `limits` must be equal to the value thatâs specified in `requests` .

key -> (string)

value -> (string)

requests -> (map)

The type and quantity of the resources to request for the container. The values vary based on the `name` thatâs specified. Resources can be requested by using either the `limits` or the `requests` objects.

memory

The memory hard limit (in MiB) for the container, using whole integers, with a âMiâ suffix. If your container attempts to exceed the memory specified, the container is terminated. You must specify at least 4 MiB of memory for a job. `memory` can be specified in `limits` , `requests` , or both. If `memory` is specified in both, then the value thatâs specified in `limits` must be equal to the value thatâs specified in `requests` .

### Note

If youâre trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see [Memory management](https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html) in the *Batch User Guide* .

cpu

The number of CPUs that are reserved for the container. Values must be an even multiple of `0.25` . `cpu` can be specified in `limits` , `requests` , or both. If `cpu` is specified in both, then the value thatâs specified in `limits` must be at least as large as the value thatâs specified in `requests` .

nvidia.com/gpu

The number of GPUs that are reserved for the container. Values must be a whole integer. `nvidia.com/gpu` can be specified in `limits` , `requests` , or both. If `nvidia.com/gpu` is specified in both, then the value thatâs specified in `limits` must be equal to the value thatâs specified in `requests` .

key -> (string)

value -> (string)

volumeMounts -> (list)

The volume mounts for the container. Batch supports `emptyDir` , `hostPath` , and `secret` volume types. For more information about volumes and volume mounts in Kubernetes, see [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/) in the *Kubernetes documentation* .

(structure)

The volume mounts for a container for an Amazon EKS job. For more information about volumes and volume mounts in Kubernetes, see [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/) in the *Kubernetes documentation* .

name -> (string)

The name the volume mount. This must match the name of one of the volumes in the pod.

mountPath -> (string)

The path on the container where the volume is mounted.

subPath -> (string)

A sub-path inside the referenced volume instead of its root.

readOnly -> (boolean)

If this value is `true` , the container has read-only access to the volume. Otherwise, the container can write to the volume. The default value is `false` .

securityContext -> (structure)

The security context for a job. For more information, see [Configure a security context for a pod or container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) in the *Kubernetes documentation* .

runAsUser -> (long)

When this parameter is specified, the container is run as the specified user ID (`uid` ). If this parameter isnât specified, the default is the user thatâs specified in the image metadata. This parameter maps to `RunAsUser` and `MustRanAs` policy in the [Users and groups pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups) in the *Kubernetes documentation* .

runAsGroup -> (long)

When this parameter is specified, the container is run as the specified group ID (`gid` ). If this parameter isnât specified, the default is the group thatâs specified in the image metadata. This parameter maps to `RunAsGroup` and `MustRunAs` policy in the [Users and groups pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups) in the *Kubernetes documentation* .

privileged -> (boolean)

When this parameter is `true` , the container is given elevated permissions on the host container instance. The level of permissions are similar to the `root` user permissions. The default value is `false` . This parameter maps to `privileged` policy in the [Privileged pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#privileged) in the *Kubernetes documentation* .

allowPrivilegeEscalation -> (boolean)

Whether or not a container or a Kubernetes pod is allowed to gain more privileges than its parent process. The default value is `false` .

readOnlyRootFilesystem -> (boolean)

When this parameter is `true` , the container is given read-only access to its root file system. The default value is `false` . This parameter maps to `ReadOnlyRootFilesystem` policy in the [Volumes and file systems pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#volumes-and-file-systems) in the *Kubernetes documentation* .

runAsNonRoot -> (boolean)

When this parameter is specified, the container is run as a user with a `uid` other than 0. If this parameter isnât specified, so such rule is enforced. This parameter maps to `RunAsUser` and `MustRunAsNonRoot` policy in the [Users and groups pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups) in the *Kubernetes documentation* .

initContainers -> (list)

These containers run before application containers, always runs to completion, and must complete successfully before the next container starts. These containers are registered with the Amazon EKS Connector agent and persists the registration information in the Kubernetes backend data store. For more information, see [Init Containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) in the *Kubernetes documentation* .

### Note

This object is limited to 10 elements.

(structure)

EKS container properties are used in job definitions for Amazon EKS based job definitions to describe the properties for a container node in the pod thatâs launched as part of a job. This canât be specified for Amazon ECS based job definitions.

name -> (string)

The name of the container. If the name isnât specified, the default name â`Default` â is used. Each container in a pod must have a unique name.

image -> (string)

The Docker image used to start the container.

imagePullPolicy -> (string)

The image pull policy for the container. Supported values are `Always` , `IfNotPresent` , and `Never` . This parameter defaults to `IfNotPresent` . However, if the `:latest` tag is specified, it defaults to `Always` . For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images) in the *Kubernetes documentation* .

command -> (list)

The entrypoint for the container. This isnât run within a shell. If this isnât specified, the `ENTRYPOINT` of the container image is used. Environment variable references are expanded using the containerâs environment.

If the referenced environment variable doesnât exist, the reference in the command isnât changed. For example, if the reference is to â`$(NAME1)` â and the `NAME1` environment variable doesnât exist, the command string will remain â`$(NAME1)` .â `$$` is replaced with `$` and the resulting string isnât expanded. For example, `$$(VAR_NAME)` will be passed as `$(VAR_NAME)` whether or not the `VAR_NAME` environment variable exists. The entrypoint canât be updated. For more information, see [ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint) in the *Dockerfile reference* and [Define a command and arguments for a container](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/) and [Entrypoint](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#entrypoint) in the *Kubernetes documentation* .

(string)

args -> (list)

An array of arguments to the entrypoint. If this isnât specified, the `CMD` of the container image is used. This corresponds to the `args` member in the [Entrypoint](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#entrypoint) portion of the [Pod](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/) in Kubernetes. Environment variable references are expanded using the containerâs environment.

If the referenced environment variable doesnât exist, the reference in the command isnât changed. For example, if the reference is to â`$(NAME1)` â and the `NAME1` environment variable doesnât exist, the command string will remain â`$(NAME1)` .â `$$` is replaced with `$` , and the resulting string isnât expanded. For example, `$$(VAR_NAME)` is passed as `$(VAR_NAME)` whether or not the `VAR_NAME` environment variable exists. For more information, see [Dockerfile reference: CMD](https://docs.docker.com/engine/reference/builder/#cmd) and [Define a command and arguments for a pod](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/) in the *Kubernetes documentation* .

(string)

env -> (list)

The environment variables to pass to a container.

### Note

Environment variables cannot start with â`AWS_BATCH` â. This naming convention is reserved for variables that Batch sets.

(structure)

An environment variable.

name -> (string)

The name of the environment variable.

value -> (string)

The value of the environment variable.

resources -> (structure)

The type and amount of resources to assign to a container. The supported resources include `memory` , `cpu` , and `nvidia.com/gpu` . For more information, see [Resource management for pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) in the *Kubernetes documentation* .

limits -> (map)

The type and quantity of the resources to reserve for the container. The values vary based on the `name` thatâs specified. Resources can be requested using either the `limits` or the `requests` objects.

memory

The memory hard limit (in MiB) for the container, using whole integers, with a âMiâ suffix. If your container attempts to exceed the memory specified, the container is terminated. You must specify at least 4 MiB of memory for a job. `memory` can be specified in `limits` , `requests` , or both. If `memory` is specified in both places, then the value thatâs specified in `limits` must be equal to the value thatâs specified in `requests` .

### Note

To maximize your resource utilization, provide your jobs with as much memory as possible for the specific instance type that you are using. To learn how, see [Memory management](https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html) in the *Batch User Guide* .

cpu

The number of CPUs thatâs reserved for the container. Values must be an even multiple of `0.25` . `cpu` can be specified in `limits` , `requests` , or both. If `cpu` is specified in both places, then the value thatâs specified in `limits` must be at least as large as the value thatâs specified in `requests` .

nvidia.com/gpu

The number of GPUs thatâs reserved for the container. Values must be a whole integer. `memory` can be specified in `limits` , `requests` , or both. If `memory` is specified in both places, then the value thatâs specified in `limits` must be equal to the value thatâs specified in `requests` .

key -> (string)

value -> (string)

requests -> (map)

The type and quantity of the resources to request for the container. The values vary based on the `name` thatâs specified. Resources can be requested by using either the `limits` or the `requests` objects.

memory

The memory hard limit (in MiB) for the container, using whole integers, with a âMiâ suffix. If your container attempts to exceed the memory specified, the container is terminated. You must specify at least 4 MiB of memory for a job. `memory` can be specified in `limits` , `requests` , or both. If `memory` is specified in both, then the value thatâs specified in `limits` must be equal to the value thatâs specified in `requests` .

### Note

If youâre trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see [Memory management](https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html) in the *Batch User Guide* .

cpu

The number of CPUs that are reserved for the container. Values must be an even multiple of `0.25` . `cpu` can be specified in `limits` , `requests` , or both. If `cpu` is specified in both, then the value thatâs specified in `limits` must be at least as large as the value thatâs specified in `requests` .

nvidia.com/gpu

The number of GPUs that are reserved for the container. Values must be a whole integer. `nvidia.com/gpu` can be specified in `limits` , `requests` , or both. If `nvidia.com/gpu` is specified in both, then the value thatâs specified in `limits` must be equal to the value thatâs specified in `requests` .

key -> (string)

value -> (string)

volumeMounts -> (list)

The volume mounts for the container. Batch supports `emptyDir` , `hostPath` , and `secret` volume types. For more information about volumes and volume mounts in Kubernetes, see [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/) in the *Kubernetes documentation* .

(structure)

The volume mounts for a container for an Amazon EKS job. For more information about volumes and volume mounts in Kubernetes, see [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/) in the *Kubernetes documentation* .

name -> (string)

The name the volume mount. This must match the name of one of the volumes in the pod.

mountPath -> (string)

The path on the container where the volume is mounted.

subPath -> (string)

A sub-path inside the referenced volume instead of its root.

readOnly -> (boolean)

If this value is `true` , the container has read-only access to the volume. Otherwise, the container can write to the volume. The default value is `false` .

securityContext -> (structure)

The security context for a job. For more information, see [Configure a security context for a pod or container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) in the *Kubernetes documentation* .

runAsUser -> (long)

When this parameter is specified, the container is run as the specified user ID (`uid` ). If this parameter isnât specified, the default is the user thatâs specified in the image metadata. This parameter maps to `RunAsUser` and `MustRanAs` policy in the [Users and groups pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups) in the *Kubernetes documentation* .

runAsGroup -> (long)

When this parameter is specified, the container is run as the specified group ID (`gid` ). If this parameter isnât specified, the default is the group thatâs specified in the image metadata. This parameter maps to `RunAsGroup` and `MustRunAs` policy in the [Users and groups pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups) in the *Kubernetes documentation* .

privileged -> (boolean)

When this parameter is `true` , the container is given elevated permissions on the host container instance. The level of permissions are similar to the `root` user permissions. The default value is `false` . This parameter maps to `privileged` policy in the [Privileged pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#privileged) in the *Kubernetes documentation* .

allowPrivilegeEscalation -> (boolean)

Whether or not a container or a Kubernetes pod is allowed to gain more privileges than its parent process. The default value is `false` .

readOnlyRootFilesystem -> (boolean)

When this parameter is `true` , the container is given read-only access to its root file system. The default value is `false` . This parameter maps to `ReadOnlyRootFilesystem` policy in the [Volumes and file systems pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#volumes-and-file-systems) in the *Kubernetes documentation* .

runAsNonRoot -> (boolean)

When this parameter is specified, the container is run as a user with a `uid` other than 0. If this parameter isnât specified, so such rule is enforced. This parameter maps to `RunAsUser` and `MustRunAsNonRoot` policy in the [Users and groups pod security policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups) in the *Kubernetes documentation* .

volumes -> (list)

Specifies the volumes for a job definition that uses Amazon EKS resources.

(structure)

Specifies an Amazon EKS volume for a job definition.

name -> (string)

The name of the volume. The name must be allowed as a DNS subdomain name. For more information, see [DNS subdomain names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names) in the *Kubernetes documentation* .

hostPath -> (structure)

Specifies the configuration of a Kubernetes `hostPath` volume. For more information, see [hostPath](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath) in the *Kubernetes documentation* .

path -> (string)

The path of the file or directory on the host to mount into containers on the pod.

emptyDir -> (structure)

Specifies the configuration of a Kubernetes `emptyDir` volume. For more information, see [emptyDir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) in the *Kubernetes documentation* .

medium -> (string)

The medium to store the volume. The default value is an empty string, which uses the storage of the node.

ââ

**(Default)** Use the disk storage of the node.

âMemoryâ

Use the `tmpfs` volume thatâs backed by the RAM of the node. Contents of the volume are lost when the node reboots, and any storage on the volume counts against the containerâs memory limit.

sizeLimit -> (string)

The maximum size of the volume. By default, thereâs no maximum size defined.

secret -> (structure)

Specifies the configuration of a Kubernetes `secret` volume. For more information, see [secret](https://kubernetes.io/docs/concepts/storage/volumes/#secret) in the *Kubernetes documentation* .

secretName -> (string)

The name of the secret. The name must be allowed as a DNS subdomain name. For more information, see [DNS subdomain names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names) in the *Kubernetes documentation* .

optional -> (boolean)

Specifies whether the secret or the secretâs keys must be defined.

persistentVolumeClaim -> (structure)

Specifies the configuration of a Kubernetes `persistentVolumeClaim` bounded to a `persistentVolume` . For more information, see [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) in the *Kubernetes documentation* .

claimName -> (string)

The name of the `persistentVolumeClaim` bounded to a `persistentVolume` . For more information, see [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) in the *Kubernetes documentation* .

readOnly -> (boolean)

An optional boolean value indicating if the mount is read only. Default is false. For more information, see [Read Only Mounts](https://kubernetes.io/docs/concepts/storage/volumes/#read-only-mounts) in the *Kubernetes documentation* .

metadata -> (structure)

Metadata about the Kubernetes pod. For more information, see [Understanding Kubernetes Objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) in the *Kubernetes documentation* .

labels -> (map)

Key-value pairs used to identify, sort, and organize cube resources. Can contain up to 63 uppercase letters, lowercase letters, numbers, hyphens (-), and underscores (_). Labels can be added or modified at any time. Each resource can have multiple labels, but each key must be unique for a given object.

key -> (string)

value -> (string)

annotations -> (map)

Key-value pairs used to attach arbitrary, non-identifying metadata to Kubernetes objects. Valid annotation keys have two segments: an optional prefix and a name, separated by a slash (/).

- The prefix is optional and must be 253 characters or less. If specified, the prefix must be a DNS subdomainâ a series of DNS labels separated by dots (.), and it must end with a slash (/).
- The name segment is required and must be 63 characters or less. It can include alphanumeric characters ([a-z0-9A-Z]), dashes (-), underscores (_), and dots (.), but must begin and end with an alphanumeric character.

### Note

Annotation values must be 255 characters or less.

Annotations can be added or modified at any time. Each resource can have multiple annotations.

key -> (string)

value -> (string)

namespace -> (string)

The namespace of the Amazon EKS cluster. In Kubernetes, namespaces provide a mechanism for isolating groups of resources within a single cluster. Names of resources need to be unique within a namespace, but not across namespaces. Batch places Batch Job pods in this namespace. If this field is provided, the value canât be empty or null. It must meet the following requirements:

- 1-63 characters long
- Canât be set to default
- Canât start with `kube`
- Must match the following regular expression: `^[a-z0-9]([-a-z0-9]*[a-z0-9])?$`

For more information, see [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) in the *Kubernetes documentation* . This namespace can be different from the `kubernetesNamespace` set in the compute environmentâs `EksConfiguration` , but must have identical role-based access control (RBAC) roles as the compute environmentâs `kubernetesNamespace` . For multi-node parallel jobs, the same value must be provided across all the node ranges.

shareProcessNamespace -> (boolean)

Indicates if the processes in a container are shared, or visible, to other containers in the same pod. For more information, see [Share Process Namespace between Containers in a Pod](https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/) .

JSON Syntax:

```
{
  "podProperties": {
    "serviceAccountName": "string",
    "hostNetwork": true|false,
    "dnsPolicy": "string",
    "imagePullSecrets": [
      {
        "name": "string"
      }
      ...
    ],
    "containers": [
      {
        "name": "string",
        "image": "string",
        "imagePullPolicy": "string",
        "command": ["string", ...],
        "args": ["string", ...],
        "env": [
          {
            "name": "string",
            "value": "string"
          }
          ...
        ],
        "resources": {
          "limits": {"string": "string"
            ...},
          "requests": {"string": "string"
            ...}
        },
        "volumeMounts": [
          {
            "name": "string",
            "mountPath": "string",
            "subPath": "string",
            "readOnly": true|false
          }
          ...
        ],
        "securityContext": {
          "runAsUser": long,
          "runAsGroup": long,
          "privileged": true|false,
          "allowPrivilegeEscalation": true|false,
          "readOnlyRootFilesystem": true|false,
          "runAsNonRoot": true|false
        }
      }
      ...
    ],
    "initContainers": [
      {
        "name": "string",
        "image": "string",
        "imagePullPolicy": "string",
        "command": ["string", ...],
        "args": ["string", ...],
        "env": [
          {
            "name": "string",
            "value": "string"
          }
          ...
        ],
        "resources": {
          "limits": {"string": "string"
            ...},
          "requests": {"string": "string"
            ...}
        },
        "volumeMounts": [
          {
            "name": "string",
            "mountPath": "string",
            "subPath": "string",
            "readOnly": true|false
          }
          ...
        ],
        "securityContext": {
          "runAsUser": long,
          "runAsGroup": long,
          "privileged": true|false,
          "allowPrivilegeEscalation": true|false,
          "readOnlyRootFilesystem": true|false,
          "runAsNonRoot": true|false
        }
      }
      ...
    ],
    "volumes": [
      {
        "name": "string",
        "hostPath": {
          "path": "string"
        },
        "emptyDir": {
          "medium": "string",
          "sizeLimit": "string"
        },
        "secret": {
          "secretName": "string",
          "optional": true|false
        },
        "persistentVolumeClaim": {
          "claimName": "string",
          "readOnly": true|false
        }
      }
      ...
    ],
    "metadata": {
      "labels": {"string": "string"
        ...},
      "annotations": {"string": "string"
        ...},
      "namespace": "string"
    },
    "shareProcessNamespace": true|false
  }
}
```

`--ecs-properties` (structure)

An object with properties that are specific to Amazon ECS-based jobs. This must not be specified for Amazon EKS-based job definitions.

taskProperties -> (list)

An object that contains the properties for the Amazon ECS task definition of a job.

### Note

This object is currently limited to one task element. However, the task element can run up to 10 containers.

(structure)

The properties for a task definition that describes the container and volume definitions of an Amazon ECS task. You can specify which Docker images to use, the required resources, and other configurations related to launching the task definition through an Amazon ECS service or task.

containers -> (list)

This object is a list of containers.

(structure)

Container properties are used for Amazon ECS-based job definitions. These properties to describe the container thatâs launched as part of a job.

command -> (list)

The command thatâs passed to the container. This parameter maps to `Cmd` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `COMMAND` parameter to [docker run](https://docs.docker.com/engine/reference/run/) . For more information, see [Dockerfile reference: CMD](https://docs.docker.com/engine/reference/builder/#cmd) .

(string)

dependsOn -> (list)

A list of containers that this container depends on.

(structure)

A list of containers that this task depends on.

containerName -> (string)

A unique identifier for the container.

condition -> (string)

The dependency condition of the container. The following are the available conditions and their behavior:

- `START` - This condition emulates the behavior of links and volumes today. It validates that a dependent container is started before permitting other containers to start.
- `COMPLETE` - This condition validates that a dependent container runs to completion (exits) before permitting other containers to start. This can be useful for nonessential containers that run a script and then exit. This condition canât be set on an essential container.
- `SUCCESS` - This condition is the same as `COMPLETE` , but it also requires that the container exits with a zero status. This condition canât be set on an essential container.

environment -> (list)

The environment variables to pass to a container. This parameter maps to Env in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--env` parameter to [docker run](https://docs.docker.com/engine/reference/run/) .

### Warning

We donât recommend using plaintext environment variables for sensitive information, such as credential data.

### Note

Environment variables cannot start with `AWS_BATCH` . This naming convention is reserved for variables that Batch sets.

(structure)

A key-value pair object.

name -> (string)

The name of the key-value pair. For environment variables, this is the name of the environment variable.

value -> (string)

The value of the key-value pair. For environment variables, this is the value of the environment variable.

essential -> (boolean)

If the essential parameter of a container is marked as `true` , and that container fails or stops for any reason, all other containers that are part of the task are stopped. If the `essential` parameter of a container is marked as false, its failure doesnât affect the rest of the containers in a task. If this parameter is omitted, a container is assumed to be essential.

All jobs must have at least one essential container. If you have an application thatâs composed of multiple containers, group containers that are used for a common purpose into components, and separate the different components into multiple task definitions. For more information, see [Application Architecture](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/application_architecture.html) in the *Amazon Elastic Container Service Developer Guide* .

firelensConfiguration -> (structure)

The FireLens configuration for the container. This is used to specify and configure a log router for container logs. For more information, see [Custom log](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) routing in the *Amazon Elastic Container Service Developer Guide* .

type -> (string)

The log router to use. The valid values are `fluentd` or `fluentbit` .

options -> (map)

The options to use when configuring the log router. This field is optional and can be used to specify a custom configuration file or to add additional metadata, such as the task, task definition, cluster, and container instance details to the log event. If specified, the syntax to use is `"options":{"enable-ecs-log-metadata":"true|false","config-file-type:"s3|file","config-file-value":"arn:aws:s3:::mybucket/fluent.conf|filepath"}` . For more information, see [Creating a task definition that uses a FireLens configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html#firelens-taskdef) in the *Amazon Elastic Container Service Developer Guide* .

key -> (string)

value -> (string)

image -> (string)

The image used to start a container. This string is passed directly to the Docker daemon. By default, images in the Docker Hub registry are available. Other repositories are specified with either `repository-url/image:tag` or `repository-url/image@digest` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to `Image` in the [Create a container](https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.35/) and the `IMAGE` parameter of the ` *docker run* [https://docs.docker.com/engine/reference/run/#security](https://docs.docker.com/engine/reference/run/#security)-configuration`__ .

linuxParameters -> (structure)

Linux-specific modifications that are applied to the container, such as Linux kernel capabilities. For more information, see [KernelCapabilities](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_KernelCapabilities.html) .

devices -> (list)

Any of the host devices to expose to the container. This parameter maps to `Devices` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--device` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide it for these jobs.

(structure)

An object that represents a container instance host device.

### Note

This object isnât applicable to jobs that are running on Fargate resources and shouldnât be provided.

hostPath -> (string)

The path for the device on the host container instance.

containerPath -> (string)

The path inside the container thatâs used to expose the host device. By default, the `hostPath` value is used.

permissions -> (list)

The explicit permissions to provide to the container for the device. By default, the container has permissions for `read` , `write` , and `mknod` for the device.

(string)

initProcessEnabled -> (boolean)

If true, run an `init` process inside the container that forwards signals and reaps processes. This parameter maps to the `--init` option to [docker run](https://docs.docker.com/engine/reference/run/) . This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`

sharedMemorySize -> (integer)

The value for the size (in MiB) of the `/dev/shm` volume. This parameter maps to the `--shm-size` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide it for these jobs.

tmpfs -> (list)

The container path, mount options, and size (in MiB) of the `tmpfs` mount. This parameter maps to the `--tmpfs` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide this parameter for this resource type.

(structure)

The container path, mount options, and size of the `tmpfs` mount.

### Note

This object isnât applicable to jobs that are running on Fargate resources.

containerPath -> (string)

The absolute file path in the container where the `tmpfs` volume is mounted.

size -> (integer)

The size (in MiB) of the `tmpfs` volume.

mountOptions -> (list)

The list of `tmpfs` volume mount options.

Valid values: â`defaults` â | â`ro` â | â`rw` â | â`suid` â | â`nosuid` â | â`dev` â | â`nodev` â | â`exec` â | â`noexec` â | â`sync` â | â`async` â | â`dirsync` â | â`remount` â | â`mand` â | â`nomand` â | â`atime` â | â`noatime` â | â`diratime` â | â`nodiratime` â | â`bind` â | â`rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime` â | â`norelatime` â | â`strictatime` â | â`nostrictatime` â | â`mode` â | â`uid` â | â`gid` â | â`nr_inodes` â | â`nr_blocks` â | â`mpol` â

(string)

maxSwap -> (integer)

The total amount of swap memory (in MiB) a container can use. This parameter is translated to the `--memory-swap` option to [docker run](https://docs.docker.com/engine/reference/run/) where the value is the sum of the container memory plus the `maxSwap` value. For more information, see ` `--memory-swap` details <[https://docs.docker.com/config/containers/resource_constraints/#âmemory-swap-details](https://docs.docker.com/config/containers/resource_constraints/#--memory-swap-details)>`__ in the Docker documentation.

If a `maxSwap` value of `0` is specified, the container doesnât use swap. Accepted values are `0` or any positive integer. If the `maxSwap` parameter is omitted, the container doesnât use the swap configuration for the container instance on which it runs. A `maxSwap` value must be set for the `swappiness` parameter to be used.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide it for these jobs.

swappiness -> (integer)

You can use this parameter to tune a containerâs memory swappiness behavior. A `swappiness` value of `0` causes swapping to not occur unless absolutely necessary. A `swappiness` value of `100` causes pages to be swapped aggressively. Valid values are whole numbers between `0` and `100` . If the `swappiness` parameter isnât specified, a default value of `60` is used. If a value isnât specified for `maxSwap` , then this parameter is ignored. If `maxSwap` is set to 0, the container doesnât use swap. This parameter maps to the `--memory-swappiness` option to [docker run](https://docs.docker.com/engine/reference/run/) .

Consider the following when you use a per-container swap configuration.

- Swap space must be enabled and allocated on the container instance for the containers to use.

### Note

By default, the Amazon ECS optimized AMIs donât have swap enabled. You must enable swap on the instance to use this feature. For more information, see [Instance store swap volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-swap-volumes.html) in the *Amazon EC2 User Guide for Linux Instances* or [How do I allocate memory to work as swap space in an Amazon EC2 instance by using a swap file?](http://aws.amazon.com/premiumsupport/knowledge-center/ec2-memory-swap-file/)

- The swap space parameters are only supported for job definitions using EC2 resources.
- If the `maxSwap` and `swappiness` parameters are omitted from a job definition, each container has a default `swappiness` value of 60. Moreover, the total swap usage is limited to two times the memory reservation of the container.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources. Donât provide it for these jobs.

logConfiguration -> (structure)

The log configuration specification for the container.

This parameter maps to `LogConfig` in the [Create a container](https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.35/) and the `--log-driver` option to [docker run](https://docs.docker.com/engine/reference/run/#security-configuration) .

By default, containers use the same logging driver that the Docker daemon uses. However the container can use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information about the options for different supported log drivers, see [Configure logging drivers](https://docs.docker.com/engine/admin/logging/overview/) in the *Docker documentation* .

### Note

Amazon ECS currently supports a subset of the logging drivers available to the Docker daemon (shown in the `LogConfiguration` data type). Additional log drivers may be available in future releases of the Amazon ECS container agent.

This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version `--format '{{.Server.APIVersion}}'`

### Note

The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the `ECS_AVAILABLE_LOGGING_DRIVERS` environment variable before containers placed on that instance can use these log configuration options. For more information, see [Amazon ECS container agent configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html) in the *Amazon Elastic Container Service Developer Guide* .

logDriver -> (string)

The log driver to use for the container. The valid values that are listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default.

The supported log drivers are `awslogs` , `fluentd` , `gelf` , `json-file` , `journald` , `logentries` , `syslog` , and `splunk` .

### Note

Jobs that are running on Fargate resources are restricted to the `awslogs` and `splunk` log drivers.

awsfirelens

Specifies the firelens logging driver. For more information on configuring Firelens, see [Send Amazon ECS logs to an Amazon Web Services service or Amazon Web Services Partner](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) in the *Amazon Elastic Container Service Developer Guide* .

awslogs

Specifies the Amazon CloudWatch Logs logging driver. For more information, see [Using the awslogs log driver](https://docs.aws.amazon.com/batch/latest/userguide/using_awslogs.html) in the *Batch User Guide* and [Amazon CloudWatch Logs logging driver](https://docs.docker.com/config/containers/logging/awslogs/) in the Docker documentation.

fluentd

Specifies the Fluentd logging driver. For more information including usage and options, see [Fluentd logging driver](https://docs.docker.com/config/containers/logging/fluentd/) in the *Docker documentation* .

gelf

Specifies the Graylog Extended Format (GELF) logging driver. For more information including usage and options, see [Graylog Extended Format logging driver](https://docs.docker.com/config/containers/logging/gelf/) in the *Docker documentation* .

journald

Specifies the journald logging driver. For more information including usage and options, see [Journald logging driver](https://docs.docker.com/config/containers/logging/journald/) in the *Docker documentation* .

json-file

Specifies the JSON file logging driver. For more information including usage and options, see [JSON File logging driver](https://docs.docker.com/config/containers/logging/json-file/) in the *Docker documentation* .

splunk

Specifies the Splunk logging driver. For more information including usage and options, see [Splunk logging driver](https://docs.docker.com/config/containers/logging/splunk/) in the *Docker documentation* .

syslog

Specifies the syslog logging driver. For more information including usage and options, see [Syslog logging driver](https://docs.docker.com/config/containers/logging/syslog/) in the *Docker documentation* .

### Note

If you have a custom driver thatâs not listed earlier that you want to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project thatâs [available on GitHub](https://github.com/aws/amazon-ecs-agent) and customize it to work with that driver. We encourage you to submit pull requests for changes that you want to have included. However, Amazon Web Services doesnât currently support running modified copies of this software.

This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`

options -> (map)

The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`

key -> (string)

value -> (string)

secretOptions -> (list)

The secrets to pass to the log configuration. For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the *Batch User Guide* .

(structure)

An object that represents the secret to expose to your container. Secrets can be exposed to a container in the following ways:

- To inject sensitive data into your containers as environment variables, use the `secrets` container definition parameter.
- To reference sensitive information in the log configuration of a container, use the `secretOptions` container definition parameter.

For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the *Batch User Guide* .

name -> (string)

The name of the secret.

valueFrom -> (string)

The secret to expose to the container. The supported values are either the full Amazon Resource Name (ARN) of the Secrets Manager secret or the full ARN of the parameter in the Amazon Web Services Systems Manager Parameter Store.

### Note

If the Amazon Web Services Systems Manager Parameter Store parameter exists in the same Region as the job youâre launching, then you can use either the full Amazon Resource Name (ARN) or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.

mountPoints -> (list)

The mount points for data volumes in your container.

This parameter maps to `Volumes` in the [Create a container](https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.35/) and the [âvolume option to `docker run](https://docs.docker.com/engine/reference/run/#security-configuration) .

Windows containers can mount whole directories on the same drive as `$env:ProgramData` . Windows containers canât mount directories on a different drive, and mount point canât be across drives.

(structure)

Details for a Docker volume mount point thatâs used in a jobâs container properties. This parameter maps to `Volumes` in the [Create a container](https://docs.docker.com/engine/api/v1.43/#tag/Container/operation/ContainerCreate) section of the *Docker Remote API* and the `--volume` option to docker run.

containerPath -> (string)

The path on the container where the host volume is mounted.

readOnly -> (boolean)

If this value is `true` , the container has read-only access to the volume. Otherwise, the container can write to the volume. The default value is `false` .

sourceVolume -> (string)

The name of the volume to mount.

name -> (string)

The name of a container. The name can be used as a unique identifier to target your `dependsOn` and `Overrides` objects.

privileged -> (boolean)

When this parameter is `true` , the container is given elevated privileges on the host container instance (similar to the `root` user). This parameter maps to `Privileged` in the [Create a container](https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.35/) and the `--privileged` option to [docker run](https://docs.docker.com/engine/reference/run/#security-configuration) .

### Note

This parameter is not supported for Windows containers or tasks run on Fargate.

readonlyRootFilesystem -> (boolean)

When this parameter is true, the container is given read-only access to its root file system. This parameter maps to `ReadonlyRootfs` in the [Create a container](https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.35/) and the `--read-only` option to [docker run](https://docs.docker.com/engine/reference/run/#security-configuration) .

### Note

This parameter is not supported for Windows containers.

repositoryCredentials -> (structure)

The private repository authentication credentials to use.

credentialsParameter -> (string)

The Amazon Resource Name (ARN) of the secret containing the private repository credentials.

resourceRequirements -> (list)

The type and amount of a resource to assign to a container. The only supported resource is a GPU.

(structure)

The type and amount of a resource to assign to a container. The supported resources include `GPU` , `MEMORY` , and `VCPU` .

value -> (string)

The quantity of the specified resource to reserve for the container. The values vary based on the `type` specified.

type=âGPUâ

The number of physical GPUs to reserve for the container. Make sure that the number of GPUs reserved for all containers in a job doesnât exceed the number of available GPUs on the compute resource that the job is launched on.

### Note

GPUs arenât available for jobs that are running on Fargate resources.

type=âMEMORYâ

The memory hard limit (in MiB) present to the container. This parameter is supported for jobs that are running on Amazon EC2 resources. If your container attempts to exceed the memory specified, the container is terminated. This parameter maps to `Memory` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--memory` option to [docker run](https://docs.docker.com/engine/reference/run/) . You must specify at least 4 MiB of memory for a job. This is required but can be specified in several places for multi-node parallel (MNP) jobs. It must be specified for each node at least once. This parameter maps to `Memory` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--memory` option to [docker run](https://docs.docker.com/engine/reference/run/) .

### Note

If youâre trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see [Memory management](https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html) in the *Batch User Guide* .

For jobs that are running on Fargate resources, then `value` is the hard limit (in MiB), and must match one of the supported values and the `VCPU` values must be one of the values supported for that memory value.

value = 512

`VCPU` = 0.25

value = 1024

`VCPU` = 0.25 or 0.5

value = 2048

`VCPU` = 0.25, 0.5, or 1

value = 3072

`VCPU` = 0.5, or 1

value = 4096

`VCPU` = 0.5, 1, or 2

value = 5120, 6144, or 7168

`VCPU` = 1 or 2

value = 8192

`VCPU` = 1, 2, or 4

value = 9216, 10240, 11264, 12288, 13312, 14336, or 15360

`VCPU` = 2 or 4

value = 16384

`VCPU` = 2, 4, or 8

value = 17408, 18432, 19456, 21504, 22528, 23552, 25600, 26624, 27648, 29696, or 30720

`VCPU` = 4

value = 20480, 24576, or 28672

`VCPU` = 4 or 8

value = 36864, 45056, 53248, or 61440

`VCPU` = 8

value = 32768, 40960, 49152, or 57344

`VCPU` = 8 or 16

value = 65536, 73728, 81920, 90112, 98304, 106496, 114688, or 122880

`VCPU` = 16

type=âVCPUâ

The number of vCPUs reserved for the container. This parameter maps to `CpuShares` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--cpu-shares` option to [docker run](https://docs.docker.com/engine/reference/run/) . Each vCPU is equivalent to 1,024 CPU shares. For Amazon EC2 resources, you must specify at least one vCPU. This is required but can be specified in several places; it must be specified for each node at least once.

The default for the Fargate On-Demand vCPU resource count quota is 6 vCPUs. For more information about Fargate quotas, see [Fargate quotas](https://docs.aws.amazon.com/general/latest/gr/ecs-service.html#service-quotas-fargate) in the *Amazon Web Services General Reference* .

For jobs that are running on Fargate resources, then `value` must match one of the supported values and the `MEMORY` values must be one of the values supported for that `VCPU` value. The supported values are 0.25, 0.5, 1, 2, 4, 8, and 16

value = 0.25

`MEMORY` = 512, 1024, or 2048

value = 0.5

`MEMORY` = 1024, 2048, 3072, or 4096

value = 1

`MEMORY` = 2048, 3072, 4096, 5120, 6144, 7168, or 8192

value = 2

`MEMORY` = 4096, 5120, 6144, 7168, 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, or 16384

value = 4

`MEMORY` = 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, 16384, 17408, 18432, 19456, 20480, 21504, 22528, 23552, 24576, 25600, 26624, 27648, 28672, 29696, or 30720

value = 8

`MEMORY` = 16384, 20480, 24576, 28672, 32768, 36864, 40960, 45056, 49152, 53248, 57344, or 61440

value = 16

`MEMORY` = 32768, 40960, 49152, 57344, 65536, 73728, 81920, 90112, 98304, 106496, 114688, or 122880

type -> (string)

The type of resource to assign to a container. The supported resources include `GPU` , `MEMORY` , and `VCPU` .

secrets -> (list)

The secrets to pass to the container. For more information, see [Specifying Sensitive Data](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html) in the Amazon Elastic Container Service Developer Guide.

(structure)

An object that represents the secret to expose to your container. Secrets can be exposed to a container in the following ways:

- To inject sensitive data into your containers as environment variables, use the `secrets` container definition parameter.
- To reference sensitive information in the log configuration of a container, use the `secretOptions` container definition parameter.

For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the *Batch User Guide* .

name -> (string)

The name of the secret.

valueFrom -> (string)

The secret to expose to the container. The supported values are either the full Amazon Resource Name (ARN) of the Secrets Manager secret or the full ARN of the parameter in the Amazon Web Services Systems Manager Parameter Store.

### Note

If the Amazon Web Services Systems Manager Parameter Store parameter exists in the same Region as the job youâre launching, then you can use either the full Amazon Resource Name (ARN) or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.

ulimits -> (list)

A list of `ulimits` to set in the container. If a `ulimit` value is specified in a task definition, it overrides the default values set by Docker. This parameter maps to `Ulimits` in the [Create a container](https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.35/) and the `--ulimit` option to [docker run](https://docs.docker.com/engine/reference/run/#security-configuration) .

Amazon ECS tasks hosted on Fargate use the default resource limit values set by the operating system with the exception of the nofile resource limit parameter which Fargate overrides. The `nofile` resource limit sets a restriction on the number of open files that a container can use. The default `nofile` soft limit is `1024` and the default hard limit is `65535` .

This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version `--format '{{.Server.APIVersion}}'`

### Note

This parameter is not supported for Windows containers.

(structure)

The `ulimit` settings to pass to the container. For more information, see [Ulimit](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Ulimit.html) .

### Note

This object isnât applicable to jobs that are running on Fargate resources.

hardLimit -> (integer)

The hard limit for the `ulimit` type.

name -> (string)

The `type` of the `ulimit` . Valid values are: `core` | `cpu` | `data` | `fsize` | `locks` | `memlock` | `msgqueue` | `nice` | `nofile` | `nproc` | `rss` | `rtprio` | `rttime` | `sigpending` | `stack` .

softLimit -> (integer)

The soft limit for the `ulimit` type.

user -> (string)

The user to use inside the container. This parameter maps to User in the Create a container section of the Docker Remote API and the âuser option to docker run.

### Note

When running tasks using the `host` network mode, donât run containers using the `root user (UID 0)` . We recommend using a non-root user for better security.

You can specify the `user` using the following formats. If specifying a UID or GID, you must specify it as a positive integer.

- `user`
- `user:group`
- `uid`
- `uid:gid`
- `user:gi`
- `uid:group`

### Note

This parameter is not supported for Windows containers.

ephemeralStorage -> (structure)

The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on Fargate.

sizeInGiB -> (integer)

The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is `21` GiB and the maximum supported value is `200` GiB.

executionRoleArn -> (string)

The Amazon Resource Name (ARN) of the execution role that Batch can assume. For jobs that run on Fargate resources, you must provide an execution role. For more information, see [Batch execution IAM role](https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html) in the *Batch User Guide* .

platformVersion -> (string)

The Fargate platform version where the jobs are running. A platform version is specified only for jobs that are running on Fargate resources. If one isnât specified, the `LATEST` platform version is used by default. This uses a recent, approved version of the Fargate platform for compute resources. For more information, see [Fargate platform versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide* .

ipcMode -> (string)

The IPC resource namespace to use for the containers in the task. The valid values are `host` , `task` , or `none` .

If `host` is specified, all containers within the tasks that specified the `host` IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance.

If `task` is specified, all containers within the specified `task` share the same IPC resources.

If `none` is specified, the IPC resources within the containers of a task are private, and are not shared with other containers in a task or on the container instance.

If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance. For more information, see [IPC settings](https://docs.docker.com/engine/reference/run/#ipc-settings---ipc) in the Docker run reference.

taskRoleArn -> (string)

The Amazon Resource Name (ARN) thatâs associated with the Amazon ECS task.

### Note

This is object is comparable to [ContainerProperties:jobRoleArn](https://docs.aws.amazon.com/batch/latest/APIReference/API_ContainerProperties.html) .

pidMode -> (string)

The process namespace to use for the containers in the task. The valid values are `host` or `task` . For example, monitoring sidecars might need `pidMode` to access information about other containers running in the same task.

If `host` is specified, all containers within the tasks that specified the `host` PID mode on the same container instance share the process namespace with the host Amazon EC2 instance.

If `task` is specified, all containers within the specified task share the same process namespace.

If no value is specified, the default is a private namespace for each container. For more information, see [PID settings](https://docs.docker.com/engine/reference/run/#pid-settings---pid) in the Docker run reference.

networkConfiguration -> (structure)

The network configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.

assignPublicIp -> (string)

Indicates whether the job has a public IP address. For a job thatâs running on Fargate resources in a private subnet to send outbound traffic to the internet (for example, to pull container images), the private subnet requires a NAT gateway be attached to route requests to the internet. For more information, see [Amazon ECS task networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide* . The default value is â`DISABLED` â.

runtimePlatform -> (structure)

An object that represents the compute environment architecture for Batch jobs on Fargate.

operatingSystemFamily -> (string)

The operating system for the compute environment. Valid values are: `LINUX` (default), `WINDOWS_SERVER_2019_CORE` , `WINDOWS_SERVER_2019_FULL` , `WINDOWS_SERVER_2022_CORE` , and `WINDOWS_SERVER_2022_FULL` .

### Note

The following parameters canât be set for Windows containers: `linuxParameters` , `privileged` , `user` , `ulimits` , `readonlyRootFilesystem` , and `efsVolumeConfiguration` .

### Note

The Batch Scheduler checks the compute environments that are attached to the job queue before registering a task definition with Fargate. In this scenario, the job queue is where the job is submitted. If the job requires a Windows container and the first compute environment is `LINUX` , the compute environment is skipped and the next compute environment is checked until a Windows-based compute environment is found.

### Note

Fargate Spot is not supported for `ARM64` and Windows-based containers on Fargate. A job queue will be blocked if a Fargate `ARM64` or Windows job is submitted to a job queue with only Fargate Spot compute environments. However, you can attach both `FARGATE` and `FARGATE_SPOT` compute environments to the same job queue.

cpuArchitecture -> (string)

The vCPU architecture. The default value is `X86_64` . Valid values are `X86_64` and `ARM64` .

### Note

This parameter must be set to `X86_64` for Windows containers.

### Note

Fargate Spot is not supported for `ARM64` and Windows-based containers on Fargate. A job queue will be blocked if a Fargate `ARM64` or Windows job is submitted to a job queue with only Fargate Spot compute environments. However, you can attach both `FARGATE` and `FARGATE_SPOT` compute environments to the same job queue.

volumes -> (list)

A list of volumes that are associated with the job.

(structure)

A data volume thatâs used in a jobâs container properties.

host -> (structure)

The contents of the `host` parameter determine whether your data volume persists on the host container instance and where itâs stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data isnât guaranteed to persist after the containers that are associated with it stop running.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources and shouldnât be provided.

sourcePath -> (string)

The path on the host container instance thatâs presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If this parameter contains a file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the source path location doesnât exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.

### Note

This parameter isnât applicable to jobs that run on Fargate resources. Donât provide this for these jobs.

name -> (string)

The name of the volume. It can be up to 255 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_). This name is referenced in the `sourceVolume` parameter of container definition `mountPoints` .

efsVolumeConfiguration -> (structure)

This parameter is specified when youâre using an Amazon Elastic File System file system for job storage. Jobs that are running on Fargate resources must specify a `platformVersion` of at least `1.4.0` .

fileSystemId -> (string)

The Amazon EFS file system ID to use.

rootDirectory -> (string)

The directory within the Amazon EFS file system to mount as the root directory inside the host. If this parameter is omitted, the root of the Amazon EFS volume is used instead. Specifying `/` has the same effect as omitting this parameter. The maximum length is 4,096 characters.

### Warning

If an EFS access point is specified in the `authorizationConfig` , the root directory parameter must either be omitted or set to `/` , which enforces the path set on the Amazon EFS access point.

transitEncryption -> (string)

Determines whether to enable encryption for Amazon EFS data in transit between the Amazon ECS host and the Amazon EFS server. Transit encryption must be enabled if Amazon EFS IAM authorization is used. If this parameter is omitted, the default value of `DISABLED` is used. For more information, see [Encrypting data in transit](https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html) in the *Amazon Elastic File System User Guide* .

transitEncryptionPort -> (integer)

The port to use when sending encrypted data between the Amazon ECS host and the Amazon EFS server. If you donât specify a transit encryption port, it uses the port selection strategy that the Amazon EFS mount helper uses. The value must be between 0 and 65,535. For more information, see [EFS mount helper](https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html) in the *Amazon Elastic File System User Guide* .

authorizationConfig -> (structure)

The authorization configuration details for the Amazon EFS file system.

accessPointId -> (string)

The Amazon EFS access point ID to use. If an access point is specified, the root directory value specified in the `EFSVolumeConfiguration` must either be omitted or set to `/` which enforces the path set on the EFS access point. If an access point is used, transit encryption must be enabled in the `EFSVolumeConfiguration` . For more information, see [Working with Amazon EFS access points](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html) in the *Amazon Elastic File System User Guide* .

iam -> (string)

Whether or not to use the Batch job IAM role defined in a job definition when mounting the Amazon EFS file system. If enabled, transit encryption must be enabled in the `EFSVolumeConfiguration` . If this parameter is omitted, the default value of `DISABLED` is used. For more information, see [Using Amazon EFS access points](https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html#efs-volume-accesspoints) in the *Batch User Guide* . EFS IAM authorization requires that `TransitEncryption` be `ENABLED` and that a `JobRoleArn` is specified.

enableExecuteCommand -> (boolean)

Determines whether execute command functionality is turned on for this task. If `true` , execute command functionality is turned on all the containers in the task.

JSON Syntax:

```
{
  "taskProperties": [
    {
      "containers": [
        {
          "command": ["string", ...],
          "dependsOn": [
            {
              "containerName": "string",
              "condition": "string"
            }
            ...
          ],
          "environment": [
            {
              "name": "string",
              "value": "string"
            }
            ...
          ],
          "essential": true|false,
          "firelensConfiguration": {
            "type": "fluentd"|"fluentbit",
            "options": {"string": "string"
              ...}
          },
          "image": "string",
          "linuxParameters": {
            "devices": [
              {
                "hostPath": "string",
                "containerPath": "string",
                "permissions": ["READ"|"WRITE"|"MKNOD", ...]
              }
              ...
            ],
            "initProcessEnabled": true|false,
            "sharedMemorySize": integer,
            "tmpfs": [
              {
                "containerPath": "string",
                "size": integer,
                "mountOptions": ["string", ...]
              }
              ...
            ],
            "maxSwap": integer,
            "swappiness": integer
          },
          "logConfiguration": {
            "logDriver": "json-file"|"syslog"|"journald"|"gelf"|"fluentd"|"awslogs"|"splunk"|"awsfirelens",
            "options": {"string": "string"
              ...},
            "secretOptions": [
              {
                "name": "string",
                "valueFrom": "string"
              }
              ...
            ]
          },
          "mountPoints": [
            {
              "containerPath": "string",
              "readOnly": true|false,
              "sourceVolume": "string"
            }
            ...
          ],
          "name": "string",
          "privileged": true|false,
          "readonlyRootFilesystem": true|false,
          "repositoryCredentials": {
            "credentialsParameter": "string"
          },
          "resourceRequirements": [
            {
              "value": "string",
              "type": "GPU"|"VCPU"|"MEMORY"
            }
            ...
          ],
          "secrets": [
            {
              "name": "string",
              "valueFrom": "string"
            }
            ...
          ],
          "ulimits": [
            {
              "hardLimit": integer,
              "name": "string",
              "softLimit": integer
            }
            ...
          ],
          "user": "string"
        }
        ...
      ],
      "ephemeralStorage": {
        "sizeInGiB": integer
      },
      "executionRoleArn": "string",
      "platformVersion": "string",
      "ipcMode": "string",
      "taskRoleArn": "string",
      "pidMode": "string",
      "networkConfiguration": {
        "assignPublicIp": "ENABLED"|"DISABLED"
      },
      "runtimePlatform": {
        "operatingSystemFamily": "string",
        "cpuArchitecture": "string"
      },
      "volumes": [
        {
          "host": {
            "sourcePath": "string"
          },
          "name": "string",
          "efsVolumeConfiguration": {
            "fileSystemId": "string",
            "rootDirectory": "string",
            "transitEncryption": "ENABLED"|"DISABLED",
            "transitEncryptionPort": integer,
            "authorizationConfig": {
              "accessPointId": "string",
              "iam": "ENABLED"|"DISABLED"
            }
          }
        }
        ...
      ],
      "enableExecuteCommand": true|false
    }
    ...
  ]
}
```

`--consumable-resource-properties` (structure)

Contains a list of consumable resources required by the job.

consumableResourceList -> (list)

The list of consumable resources required by a job.

(structure)

Information about a consumable resource required to run a job.

consumableResource -> (string)

The name or ARN of the consumable resource.

quantity -> (long)

The quantity of the consumable resource that is needed.

Shorthand Syntax:

```
consumableResourceList=[{consumableResource=string,quantity=long},{consumableResource=string,quantity=long}]
```

JSON Syntax:

```
{
  "consumableResourceList": [
    {
      "consumableResource": "string",
      "quantity": long
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To register a job definition**

This example registers a job definition for a simple container job.

Command:

```
aws batch register-job-definition --job-definition-name sleep30 --type container --container-properties '{ "image": "busybox", "vcpus": 1, "memory": 128, "command": [ "sleep", "30"]}'
```

Output:

```
{
    "jobDefinitionArn": "arn:aws:batch:us-east-1:012345678910:job-definition/sleep30:1",
    "jobDefinitionName": "sleep30",
    "revision": 1
}
```

## Output

jobDefinitionName -> (string)

The name of the job definition.

jobDefinitionArn -> (string)

The Amazon Resource Name (ARN) of the job definition.

revision -> (integer)

The revision of the job definition.