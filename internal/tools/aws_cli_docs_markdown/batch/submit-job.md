# submit-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/submit-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/submit-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [batch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/index.html#cli-aws-batch) ]

# submit-job

## Description

Submits an Batch job from a job definition. Parameters that are specified during  SubmitJob override parameters defined in the job definition. vCPU and memory requirements that are specified in the `resourceRequirements` objects in the job definition are the exception. They canât be overridden this way using the `memory` and `vcpus` parameters. Rather, you must specify updates to job definition parameters in a `resourceRequirements` object thatâs included in the `containerOverrides` parameter.

### Note

Job queues with a scheduling policy are limited to 500 active share identifiers at a time.

### Warning

Jobs that run on Fargate resources canât be guaranteed to run for more than 14 days. This is because, after 14 days, Fargate resources might become unavailable and job might be terminated.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/SubmitJob)

## Synopsis

```
submit-job
--job-name <value>
--job-queue <value>
[--share-identifier <value>]
[--scheduling-priority-override <value>]
[--array-properties <value>]
[--depends-on <value>]
--job-definition <value>
[--parameters <value>]
[--container-overrides <value>]
[--node-overrides <value>]
[--retry-strategy <value>]
[--propagate-tags | --no-propagate-tags]
[--timeout <value>]
[--tags <value>]
[--eks-properties-override <value>]
[--ecs-properties-override <value>]
[--consumable-resource-properties-override <value>]
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

`--job-name` (string)

The name of the job. It can be up to 128 letters long. The first character must be alphanumeric, can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).

`--job-queue` (string)

The job queue where the job is submitted. You can specify either the name or the Amazon Resource Name (ARN) of the queue.

`--share-identifier` (string)

The share identifier for the job. Donât specify this parameter if the job queue doesnât have a fair-share scheduling policy. If the job queue has a fair-share scheduling policy, then this parameter must be specified.

This string is limited to 255 alphanumeric characters, and can be followed by an asterisk (*).

`--scheduling-priority-override` (integer)

The scheduling priority for the job. This only affects jobs in job queues with a fair-share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority. This overrides any scheduling priority in the job definition and works only within a single share identifier.

The minimum supported value is 0 and the maximum supported value is 9999.

`--array-properties` (structure)

The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. For more information, see [Array Jobs](https://docs.aws.amazon.com/batch/latest/userguide/array_jobs.html) in the *Batch User Guide* .

size -> (integer)

The size of the array job.

Shorthand Syntax:

```
size=integer
```

JSON Syntax:

```
{
  "size": integer
}
```

`--depends-on` (list)

A list of dependencies for the job. A job can depend upon a maximum of 20 jobs. You can specify a `SEQUENTIAL` type dependency without specifying a job ID for array jobs so that each child array job completes sequentially, starting at index 0. You can also specify an `N_TO_N` type dependency with a job ID for array jobs. In that case, each index child of this job must wait for the corresponding index child of each dependency to complete before it can begin.

(structure)

An object that represents an Batch job dependency.

jobId -> (string)

The job ID of the Batch job thatâs associated with this dependency.

type -> (string)

The type of the job dependency.

Shorthand Syntax:

```
jobId=string,type=string ...
```

JSON Syntax:

```
[
  {
    "jobId": "string",
    "type": "N_TO_N"|"SEQUENTIAL"
  }
  ...
]
```

`--job-definition` (string)

The job definition used by this job. This value can be one of `definition-name` , `definition-name:revision` , or the Amazon Resource Name (ARN) for the job definition, with or without the revision ([``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/submit-job.html#id1)arn:aws:batch:*region* :*account* :job-definition/*definition-name* :*revision* `` , or [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/submit-job.html#id3)arn:aws:batch:*region* :*account* :job-definition/*definition-name* `` ).

If the revision is not specified, then the latest active revision is used.

`--parameters` (map)

Additional parameters passed to the job that replace parameter substitution placeholders that are set in the job definition. Parameters are specified as a key and value pair mapping. Parameters in a `SubmitJob` request override any corresponding parameter defaults from the job definition.

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

`--container-overrides` (structure)

An object with properties that override the defaults for the job definition that specify the name of a container in the specified job definition and the overrides it should receive. You can override the default command for a container, which is specified in the job definition or the Docker image, with a `command` override. You can also override existing environment variables on a container or add new environment variables to it with an `environment` override.

vcpus -> (integer)

This parameter is deprecated, use `resourceRequirements` to override the `vcpus` parameter thatâs set in the job definition. Itâs not supported for jobs running on Fargate resources. For jobs that run on Amazon EC2 resources, it overrides the `vcpus` parameter set in the job definition, but doesnât override any vCPU requirement specified in the `resourceRequirements` structure in the job definition. To override vCPU requirements that are specified in the `resourceRequirements` structure in the job definition, `resourceRequirements` must be specified in the `SubmitJob` request, with `type` set to `VCPU` and `value` set to the new value. For more information, see [Canât override job definition resource requirements](https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#override-resource-requirements) in the *Batch User Guide* .

memory -> (integer)

This parameter is deprecated, use `resourceRequirements` to override the memory requirements specified in the job definition. Itâs not supported for jobs running on Fargate resources. For jobs that run on Amazon EC2 resources, it overrides the `memory` parameter set in the job definition, but doesnât override any memory requirement thatâs specified in the `resourceRequirements` structure in the job definition. To override memory requirements that are specified in the `resourceRequirements` structure in the job definition, `resourceRequirements` must be specified in the `SubmitJob` request, with `type` set to `MEMORY` and `value` set to the new value. For more information, see [Canât override job definition resource requirements](https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#override-resource-requirements) in the *Batch User Guide* .

command -> (list)

The command to send to the container that overrides the default command from the Docker image or the job definition.

### Note

This parameter canât contain an empty string.

(string)

instanceType -> (string)

The instance type to use for a multi-node parallel job.

### Note

This parameter isnât applicable to single-node container jobs or jobs that run on Fargate resources, and shouldnât be provided.

environment -> (list)

The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the job definition.

### Note

Environment variables cannot start with â`AWS_BATCH` â. This naming convention is reserved for variables that Batch sets.

(structure)

A key-value pair object.

name -> (string)

The name of the key-value pair. For environment variables, this is the name of the environment variable.

value -> (string)

The value of the key-value pair. For environment variables, this is the value of the environment variable.

resourceRequirements -> (list)

The type and amount of resources to assign to a container. This overrides the settings in the job definition. The supported resources include `GPU` , `MEMORY` , and `VCPU` .

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

Shorthand Syntax:

```
vcpus=integer,memory=integer,command=string,string,instanceType=string,environment=[{name=string,value=string},{name=string,value=string}],resourceRequirements=[{value=string,type=string},{value=string,type=string}]
```

JSON Syntax:

```
{
  "vcpus": integer,
  "memory": integer,
  "command": ["string", ...],
  "instanceType": "string",
  "environment": [
    {
      "name": "string",
      "value": "string"
    }
    ...
  ],
  "resourceRequirements": [
    {
      "value": "string",
      "type": "GPU"|"VCPU"|"MEMORY"
    }
    ...
  ]
}
```

`--node-overrides` (structure)

A list of node overrides in JSON format that specify the node range to target and the container overrides for that node range.

### Note

This parameter isnât applicable to jobs that are running on Fargate resources; use `containerOverrides` instead.

numNodes -> (integer)

The number of nodes to use with a multi-node parallel job. This value overrides the number of nodes that are specified in the job definition. To use this override, you must meet the following conditions:

- There must be at least one node range in your job definition that has an open upper boundary, such as `:` or `n:` .
- The lower boundary of the node range thatâs specified in the job definition must be fewer than the number of nodes specified in the override.
- The main node index thatâs specified in the job definition must be fewer than the number of nodes specified in the override.

nodePropertyOverrides -> (list)

The node property overrides for the job.

(structure)

The object that represents any node overrides to a job definition thatâs used in a [SubmitJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) API operation.

targetNodes -> (string)

The range of nodes, using node index values, thatâs used to override. A range of `0:3` indicates nodes with index values of `0` through `3` . If the starting range value is omitted (`:n` ), then `0` is used to start the range. If the ending range value is omitted (`n:` ), then the highest possible node index is used to end the range.

containerOverrides -> (structure)

The overrides that are sent to a node range.

vcpus -> (integer)

This parameter is deprecated, use `resourceRequirements` to override the `vcpus` parameter thatâs set in the job definition. Itâs not supported for jobs running on Fargate resources. For jobs that run on Amazon EC2 resources, it overrides the `vcpus` parameter set in the job definition, but doesnât override any vCPU requirement specified in the `resourceRequirements` structure in the job definition. To override vCPU requirements that are specified in the `resourceRequirements` structure in the job definition, `resourceRequirements` must be specified in the `SubmitJob` request, with `type` set to `VCPU` and `value` set to the new value. For more information, see [Canât override job definition resource requirements](https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#override-resource-requirements) in the *Batch User Guide* .

memory -> (integer)

This parameter is deprecated, use `resourceRequirements` to override the memory requirements specified in the job definition. Itâs not supported for jobs running on Fargate resources. For jobs that run on Amazon EC2 resources, it overrides the `memory` parameter set in the job definition, but doesnât override any memory requirement thatâs specified in the `resourceRequirements` structure in the job definition. To override memory requirements that are specified in the `resourceRequirements` structure in the job definition, `resourceRequirements` must be specified in the `SubmitJob` request, with `type` set to `MEMORY` and `value` set to the new value. For more information, see [Canât override job definition resource requirements](https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#override-resource-requirements) in the *Batch User Guide* .

command -> (list)

The command to send to the container that overrides the default command from the Docker image or the job definition.

### Note

This parameter canât contain an empty string.

(string)

instanceType -> (string)

The instance type to use for a multi-node parallel job.

### Note

This parameter isnât applicable to single-node container jobs or jobs that run on Fargate resources, and shouldnât be provided.

environment -> (list)

The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the job definition.

### Note

Environment variables cannot start with â`AWS_BATCH` â. This naming convention is reserved for variables that Batch sets.

(structure)

A key-value pair object.

name -> (string)

The name of the key-value pair. For environment variables, this is the name of the environment variable.

value -> (string)

The value of the key-value pair. For environment variables, this is the value of the environment variable.

resourceRequirements -> (list)

The type and amount of resources to assign to a container. This overrides the settings in the job definition. The supported resources include `GPU` , `MEMORY` , and `VCPU` .

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

ecsPropertiesOverride -> (structure)

An object that contains the properties that you want to replace for the existing Amazon ECS resources of a job.

taskProperties -> (list)

The overrides for the Amazon ECS task definition of a job.

### Note

This object is currently limited to one element.

(structure)

An object that contains overrides for the task definition of a job.

containers -> (list)

The overrides for the container definition of a job.

(structure)

The overrides that should be sent to a container.

For information about using Batch overrides when you connect event sources to targets, see [BatchContainerOverrides](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_BatchContainerOverrides.html) .

command -> (list)

The command to send to the container that overrides the default command from the Docker image or the job definition.

### Note

This parameter canât contain an empty string.

(string)

environment -> (list)

The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the job definition.

### Note

Environment variables cannot start with `AWS_BATCH` . This naming convention is reserved for variables that Batch sets.

(structure)

A key-value pair object.

name -> (string)

The name of the key-value pair. For environment variables, this is the name of the environment variable.

value -> (string)

The value of the key-value pair. For environment variables, this is the value of the environment variable.

name -> (string)

A pointer to the container that you want to override. The containerâs name provides a unique identifier for the container being used.

resourceRequirements -> (list)

The type and amount of resources to assign to a container. This overrides the settings in the job definition. The supported resources include `GPU` , `MEMORY` , and `VCPU` .

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

instanceTypes -> (list)

An object that contains the instance types that you want to replace for the existing resources of a job.

(string)

eksPropertiesOverride -> (structure)

An object that contains the properties that you want to replace for the existing Amazon EKS resources of a job.

podProperties -> (structure)

The overrides for the Kubernetes pod resources of a job.

containers -> (list)

The overrides for the container thatâs used on the Amazon EKS pod.

(structure)

Object representing any Kubernetes overrides to a job definition thatâs used in a [SubmitJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) API operation.

name -> (string)

A pointer to the container that you want to override. The name must match a unique container name that you wish to override.

image -> (string)

The override of the Docker image thatâs used to start the container.

command -> (list)

The command to send to the container that overrides the default command from the Docker image or the job definition.

(string)

args -> (list)

The arguments to the entrypoint to send to the container that overrides the default arguments from the Docker image or the job definition. For more information, see [Dockerfile reference: CMD](https://docs.docker.com/engine/reference/builder/#cmd) and [Define a command an arguments for a pod](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/) in the *Kubernetes documentation* .

(string)

env -> (list)

The environment variables to send to the container. You can add new environment variables, which are added to the container at launch. Or, you can override the existing environment variables from the Docker image or the job definition.

### Note

Environment variables cannot start with â`AWS_BATCH` â. This naming convention is reserved for variables that Batch sets.

(structure)

An environment variable.

name -> (string)

The name of the environment variable.

value -> (string)

The value of the environment variable.

resources -> (structure)

The type and amount of resources to assign to a container. These override the settings in the job definition. The supported resources include `memory` , `cpu` , and `nvidia.com/gpu` . For more information, see [Resource management for pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) in the *Kubernetes documentation* .

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

initContainers -> (list)

The overrides for the `initContainers` defined in the Amazon EKS pod. These containers run before application containers, always run to completion, and must complete successfully before the next container starts. These containers are registered with the Amazon EKS Connector agent and persists the registration information in the Kubernetes backend data store. For more information, see [Init Containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) in the *Kubernetes documentation* .

(structure)

Object representing any Kubernetes overrides to a job definition thatâs used in a [SubmitJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) API operation.

name -> (string)

A pointer to the container that you want to override. The name must match a unique container name that you wish to override.

image -> (string)

The override of the Docker image thatâs used to start the container.

command -> (list)

The command to send to the container that overrides the default command from the Docker image or the job definition.

(string)

args -> (list)

The arguments to the entrypoint to send to the container that overrides the default arguments from the Docker image or the job definition. For more information, see [Dockerfile reference: CMD](https://docs.docker.com/engine/reference/builder/#cmd) and [Define a command an arguments for a pod](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/) in the *Kubernetes documentation* .

(string)

env -> (list)

The environment variables to send to the container. You can add new environment variables, which are added to the container at launch. Or, you can override the existing environment variables from the Docker image or the job definition.

### Note

Environment variables cannot start with â`AWS_BATCH` â. This naming convention is reserved for variables that Batch sets.

(structure)

An environment variable.

name -> (string)

The name of the environment variable.

value -> (string)

The value of the environment variable.

resources -> (structure)

The type and amount of resources to assign to a container. These override the settings in the job definition. The supported resources include `memory` , `cpu` , and `nvidia.com/gpu` . For more information, see [Resource management for pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) in the *Kubernetes documentation* .

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

metadata -> (structure)

Metadata about the overrides for the container thatâs used on the Amazon EKS pod.

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

consumableResourcePropertiesOverride -> (structure)

An object that contains overrides for the consumable resources of a job.

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
  "nodePropertyOverrides": [
    {
      "targetNodes": "string",
      "containerOverrides": {
        "vcpus": integer,
        "memory": integer,
        "command": ["string", ...],
        "instanceType": "string",
        "environment": [
          {
            "name": "string",
            "value": "string"
          }
          ...
        ],
        "resourceRequirements": [
          {
            "value": "string",
            "type": "GPU"|"VCPU"|"MEMORY"
          }
          ...
        ]
      },
      "ecsPropertiesOverride": {
        "taskProperties": [
          {
            "containers": [
              {
                "command": ["string", ...],
                "environment": [
                  {
                    "name": "string",
                    "value": "string"
                  }
                  ...
                ],
                "name": "string",
                "resourceRequirements": [
                  {
                    "value": "string",
                    "type": "GPU"|"VCPU"|"MEMORY"
                  }
                  ...
                ]
              }
              ...
            ]
          }
          ...
        ]
      },
      "instanceTypes": ["string", ...],
      "eksPropertiesOverride": {
        "podProperties": {
          "containers": [
            {
              "name": "string",
              "image": "string",
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
              }
            }
            ...
          ],
          "initContainers": [
            {
              "name": "string",
              "image": "string",
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
          }
        }
      },
      "consumableResourcePropertiesOverride": {
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

The retry strategy to use for failed jobs from this  SubmitJob operation. When a retry strategy is specified here, it overrides the retry strategy defined in the job definition.

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

Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags arenât propagated. Tags can only be propagated to the tasks during task creation. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the `FAILED` state. When specified, this overrides the tag propagation setting in the job definition.

`--timeout` (structure)

The timeout configuration for this  SubmitJob operation. You can specify a timeout duration after which Batch terminates your jobs if they havenât finished. If a job is terminated due to a timeout, it isnât retried. The minimum value for the timeout is 60 seconds. This configuration overrides any timeout configuration specified in the job definition. For array jobs, child jobs have the same timeout configuration as the parent job. For more information, see [Job Timeouts](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/job_timeouts.html) in the *Amazon Elastic Container Service Developer Guide* .

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

The tags that you apply to the job request to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see [Tagging Amazon Web Services Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in *Amazon Web Services General Reference* .

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

`--eks-properties-override` (structure)

An object, with properties that override defaults for the job definition, can only be specified for jobs that are run on Amazon EKS resources.

podProperties -> (structure)

The overrides for the Kubernetes pod resources of a job.

containers -> (list)

The overrides for the container thatâs used on the Amazon EKS pod.

(structure)

Object representing any Kubernetes overrides to a job definition thatâs used in a [SubmitJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) API operation.

name -> (string)

A pointer to the container that you want to override. The name must match a unique container name that you wish to override.

image -> (string)

The override of the Docker image thatâs used to start the container.

command -> (list)

The command to send to the container that overrides the default command from the Docker image or the job definition.

(string)

args -> (list)

The arguments to the entrypoint to send to the container that overrides the default arguments from the Docker image or the job definition. For more information, see [Dockerfile reference: CMD](https://docs.docker.com/engine/reference/builder/#cmd) and [Define a command an arguments for a pod](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/) in the *Kubernetes documentation* .

(string)

env -> (list)

The environment variables to send to the container. You can add new environment variables, which are added to the container at launch. Or, you can override the existing environment variables from the Docker image or the job definition.

### Note

Environment variables cannot start with â`AWS_BATCH` â. This naming convention is reserved for variables that Batch sets.

(structure)

An environment variable.

name -> (string)

The name of the environment variable.

value -> (string)

The value of the environment variable.

resources -> (structure)

The type and amount of resources to assign to a container. These override the settings in the job definition. The supported resources include `memory` , `cpu` , and `nvidia.com/gpu` . For more information, see [Resource management for pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) in the *Kubernetes documentation* .

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

initContainers -> (list)

The overrides for the `initContainers` defined in the Amazon EKS pod. These containers run before application containers, always run to completion, and must complete successfully before the next container starts. These containers are registered with the Amazon EKS Connector agent and persists the registration information in the Kubernetes backend data store. For more information, see [Init Containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) in the *Kubernetes documentation* .

(structure)

Object representing any Kubernetes overrides to a job definition thatâs used in a [SubmitJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) API operation.

name -> (string)

A pointer to the container that you want to override. The name must match a unique container name that you wish to override.

image -> (string)

The override of the Docker image thatâs used to start the container.

command -> (list)

The command to send to the container that overrides the default command from the Docker image or the job definition.

(string)

args -> (list)

The arguments to the entrypoint to send to the container that overrides the default arguments from the Docker image or the job definition. For more information, see [Dockerfile reference: CMD](https://docs.docker.com/engine/reference/builder/#cmd) and [Define a command an arguments for a pod](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/) in the *Kubernetes documentation* .

(string)

env -> (list)

The environment variables to send to the container. You can add new environment variables, which are added to the container at launch. Or, you can override the existing environment variables from the Docker image or the job definition.

### Note

Environment variables cannot start with â`AWS_BATCH` â. This naming convention is reserved for variables that Batch sets.

(structure)

An environment variable.

name -> (string)

The name of the environment variable.

value -> (string)

The value of the environment variable.

resources -> (structure)

The type and amount of resources to assign to a container. These override the settings in the job definition. The supported resources include `memory` , `cpu` , and `nvidia.com/gpu` . For more information, see [Resource management for pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) in the *Kubernetes documentation* .

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

metadata -> (structure)

Metadata about the overrides for the container thatâs used on the Amazon EKS pod.

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

JSON Syntax:

```
{
  "podProperties": {
    "containers": [
      {
        "name": "string",
        "image": "string",
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
        }
      }
      ...
    ],
    "initContainers": [
      {
        "name": "string",
        "image": "string",
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
    }
  }
}
```

`--ecs-properties-override` (structure)

An object, with properties that override defaults for the job definition, can only be specified for jobs that are run on Amazon ECS resources.

taskProperties -> (list)

The overrides for the Amazon ECS task definition of a job.

### Note

This object is currently limited to one element.

(structure)

An object that contains overrides for the task definition of a job.

containers -> (list)

The overrides for the container definition of a job.

(structure)

The overrides that should be sent to a container.

For information about using Batch overrides when you connect event sources to targets, see [BatchContainerOverrides](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_BatchContainerOverrides.html) .

command -> (list)

The command to send to the container that overrides the default command from the Docker image or the job definition.

### Note

This parameter canât contain an empty string.

(string)

environment -> (list)

The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the job definition.

### Note

Environment variables cannot start with `AWS_BATCH` . This naming convention is reserved for variables that Batch sets.

(structure)

A key-value pair object.

name -> (string)

The name of the key-value pair. For environment variables, this is the name of the environment variable.

value -> (string)

The value of the key-value pair. For environment variables, this is the value of the environment variable.

name -> (string)

A pointer to the container that you want to override. The containerâs name provides a unique identifier for the container being used.

resourceRequirements -> (list)

The type and amount of resources to assign to a container. This overrides the settings in the job definition. The supported resources include `GPU` , `MEMORY` , and `VCPU` .

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

JSON Syntax:

```
{
  "taskProperties": [
    {
      "containers": [
        {
          "command": ["string", ...],
          "environment": [
            {
              "name": "string",
              "value": "string"
            }
            ...
          ],
          "name": "string",
          "resourceRequirements": [
            {
              "value": "string",
              "type": "GPU"|"VCPU"|"MEMORY"
            }
            ...
          ]
        }
        ...
      ]
    }
    ...
  ]
}
```

`--consumable-resource-properties-override` (structure)

An object that contains overrides for the consumable resources of a job.

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

**To submit a job**

This example submits a simple container job called example to the HighPriority job queue.

Command:

```
aws batch submit-job --job-name example --job-queue HighPriority  --job-definition sleep60
```

Output:

```
{
    "jobName": "example",
    "jobId": "876da822-4198-45f2-a252-6cea32512ea8"
}
```

## Output

jobArn -> (string)

The Amazon Resource Name (ARN) for the job.

jobName -> (string)

The name of the job.

jobId -> (string)

The unique identifier for the job.