# run-taskÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/run-task.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/run-task.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ecs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/index.html#cli-aws-ecs) ]

# run-task

## Description

Starts a new task using the specified task definition.

### Note

On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.

### Note

Amazon Elastic Inference (EI) is no longer available to customers.

You can allow Amazon ECS to place tasks for you, or you can customize how Amazon ECS places tasks using placement constraints and placement strategies. For more information, see [Scheduling Tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html) in the *Amazon Elastic Container Service Developer Guide* .

Alternatively, you can use `StartTask` to use your own scheduler or place tasks manually on specific container instances.

You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when creating or updating a service. For more infomation, see [Amazon EBS volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types) in the *Amazon Elastic Container Service Developer Guide* .

The Amazon ECS API follows an eventual consistency model. This is because of the distributed nature of the system supporting the API. This means that the result of an API command you run that affects your Amazon ECS resources might not be immediately visible to all subsequent commands you run. Keep this in mind when you carry out an API command that immediately follows a previous API command.

To manage eventual consistency, you can do the following:

- Confirm the state of the resource before you run a command to modify it. Run the DescribeTasks command using an exponential backoff algorithm to ensure that you allow enough time for the previous command to propagate through the system. To do this, run the DescribeTasks command repeatedly, starting with a couple of seconds of wait time and increasing gradually up to five minutes of wait time.
- Add wait time between subsequent commands, even if the DescribeTasks command returns an accurate response. Apply an exponential backoff algorithm starting with a couple of seconds of wait time, and increase gradually up to about five minutes of wait time.

If you get a `ConflictException` error, the `RunTask` request could not be processed due to conflicts. The provided `clientToken` is already in use with a different `RunTask` request. The `resourceIds` are the existing task ARNs which are already associated with the `clientToken` .

To fix this issue:

- Run `RunTask` with a unique `clientToken` .
- Run `RunTask` with the `clientToken` and the original set of parameters

If you get a `ClientException` error, the `RunTask` could not be processed because you use managed scaling and there is a capacity error because the quota of tasks in the `PROVISIONING` per cluster has been reached. For information about the service quotas, see [Amazon ECS service quotas](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-quotas.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/RunTask)

## Synopsis

```
run-task
[--capacity-provider-strategy <value>]
[--cluster <value>]
[--count <value>]
[--enable-ecs-managed-tags | --no-enable-ecs-managed-tags]
[--enable-execute-command | --disable-execute-command]
[--group <value>]
[--launch-type <value>]
[--network-configuration <value>]
[--overrides <value>]
[--placement-constraints <value>]
[--placement-strategy <value>]
[--platform-version <value>]
[--propagate-tags <value>]
[--reference-id <value>]
[--started-by <value>]
[--tags <value>]
--task-definition <value>
[--client-token <value>]
[--volume-configurations <value>]
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

`--capacity-provider-strategy` (list)

The capacity provider strategy to use for the task.

If a `capacityProviderStrategy` is specified, the `launchType` parameter must be omitted. If no `capacityProviderStrategy` or `launchType` is specified, the `defaultCapacityProviderStrategy` for the cluster is used.

When you use cluster auto scaling, you must specify `capacityProviderStrategy` and not `launchType` .

A capacity provider strategy can contain a maximum of 20 capacity providers.

(structure)

The details of a capacity provider strategy. A capacity provider strategy can be set when using the [RunTask](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html) or [CreateCluster](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCluster.html) APIs or as the default capacity provider strategy for a cluster with the `CreateCluster` API.

Only capacity providers that are already associated with a cluster and have an `ACTIVE` or `UPDATING` status can be used in a capacity provider strategy. The [PutClusterCapacityProviders](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html) API is used to associate a capacity provider with a cluster.

If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must already be created. New Auto Scaling group capacity providers can be created with the [CreateClusterCapacityProvider](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateClusterCapacityProvider.html) API operation.

To use a Fargate capacity provider, specify either the `FARGATE` or `FARGATE_SPOT` capacity providers. The Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used in a capacity provider strategy.

With `FARGATE_SPOT` , you can run interruption tolerant tasks at a rate thatâs discounted compared to the `FARGATE` price. `FARGATE_SPOT` runs tasks on spare compute capacity. When Amazon Web Services needs the capacity back, your tasks are interrupted with a two-minute warning. `FARGATE_SPOT` supports Linux tasks with the X86_64 architecture on platform version 1.3.0 or later. `FARGATE_SPOT` supports Linux tasks with the ARM64 architecture on platform version 1.4.0 or later.

A capacity provider strategy can contain a maximum of 20 capacity providers.

capacityProvider -> (string)

The short name of the capacity provider.

weight -> (integer)

The *weight* value designates the relative percentage of the total number of tasks launched that should use the specified capacity provider. The `weight` value is taken into consideration after the `base` value, if defined, is satisfied.

If no `weight` value is specified, the default value of `0` is used. When multiple capacity providers are specified within a capacity provider strategy, at least one of the capacity providers must have a weight value greater than zero and any capacity providers with a weight of `0` canât be used to place tasks. If you specify multiple capacity providers in a strategy that all have a weight of `0` , any `RunTask` or `CreateService` actions using the capacity provider strategy will fail.

An example scenario for using weights is defining a strategy that contains two capacity providers and both have a weight of `1` , then when the `base` is satisfied, the tasks will be split evenly across the two capacity providers. Using that same logic, if you specify a weight of `1` for *capacityProviderA* and a weight of `4` for *capacityProviderB* , then for every one task thatâs run using *capacityProviderA* , four tasks would use *capacityProviderB* .

base -> (integer)

The *base* value designates how many tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a *base* defined. If no value is specified, the default value of `0` is used.

Shorthand Syntax:

```
capacityProvider=string,weight=integer,base=integer ...
```

JSON Syntax:

```
[
  {
    "capacityProvider": "string",
    "weight": integer,
    "base": integer
  }
  ...
]
```

`--cluster` (string)

The short name or full Amazon Resource Name (ARN) of the cluster to run your task on. If you do not specify a cluster, the default cluster is assumed.

Each account receives a default cluster the first time you use the service, but you may also create other clusters.

`--count` (integer)

The number of instantiations of the specified task to place on your cluster. You can specify up to 10 tasks for each call.

`--enable-ecs-managed-tags` | `--no-enable-ecs-managed-tags` (boolean)

Specifies whether to use Amazon ECS managed tags for the task. For more information, see [Tagging Your Amazon ECS Resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html) in the *Amazon Elastic Container Service Developer Guide* .

`--enable-execute-command` | `--disable-execute-command` (boolean)

Determines whether to use the execute command functionality for the containers in this task. If `true` , this enables execute command functionality on all containers in the task.

If `true` , then the task definition must have a task role, or you must provide one as an override.

`--group` (string)

The name of the task group to associate with the task. The default value is the family name of the task definition (for example, `family:my-family-name` ).

`--launch-type` (string)

The infrastructure to run your standalone task on. For more information, see [Amazon ECS launch types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html) in the *Amazon Elastic Container Service Developer Guide* .

The `FARGATE` launch type runs your tasks on Fargate On-Demand infrastructure.

### Note

Fargate Spot infrastructure is available for use but a capacity provider strategy must be used. For more information, see [Fargate capacity providers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-capacity-providers.html) in the *Amazon ECS Developer Guide* .

The `EC2` launch type runs your tasks on Amazon EC2 instances registered to your cluster.

The `EXTERNAL` launch type runs your tasks on your on-premises server or virtual machine (VM) capacity registered to your cluster.

A task can use either a launch type or a capacity provider strategy. If a `launchType` is specified, the `capacityProviderStrategy` parameter must be omitted.

When you use cluster auto scaling, you must specify `capacityProviderStrategy` and not `launchType` .

Possible values:

- `EC2`
- `FARGATE`
- `EXTERNAL`

`--network-configuration` (structure)

The network configuration for the task. This parameter is required for task definitions that use the `awsvpc` network mode to receive their own elastic network interface, and it isnât supported for other network modes. For more information, see [Task networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide* .

awsvpcConfiguration -> (structure)

The VPC subnets and security groups that are associated with a task.

### Note

All specified subnets and security groups must be from the same VPC.

subnets -> (list)

The IDs of the subnets associated with the task or service. Thereâs a limit of 16 subnets that can be specified.

### Note

All specified subnets must be from the same VPC.

(string)

securityGroups -> (list)

The IDs of the security groups associated with the task or service. If you donât specify a security group, the default security group for the VPC is used. Thereâs a limit of 5 security groups that can be specified.

### Note

All specified security groups must be from the same VPC.

(string)

assignPublicIp -> (string)

Whether the taskâs elastic network interface receives a public IP address.

Consider the following when you set this value:

- When you use `create-service` or `update-service` , the default is `DISABLED` .
- When the service `deploymentController` is `ECS` , the value must be `DISABLED` .

Shorthand Syntax:

```
awsvpcConfiguration={subnets=[string,string],securityGroups=[string,string],assignPublicIp=string}
```

JSON Syntax:

```
{
  "awsvpcConfiguration": {
    "subnets": ["string", ...],
    "securityGroups": ["string", ...],
    "assignPublicIp": "ENABLED"|"DISABLED"
  }
}
```

`--overrides` (structure)

A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it should receive. You can override the default command for a container (thatâs specified in the task definition or Docker image) with a `command` override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an `environment` override.

A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.

containerOverrides -> (list)

One or more container overrides that are sent to a task.

(structure)

The overrides that are sent to a container. An empty container override can be passed in. An example of an empty container override is `{"containerOverrides": [ ] }` . If a non-empty container override is specified, the `name` parameter must be included.

You can use Secrets Manager or Amazon Web Services Systems Manager Parameter Store to store the sensitive data. For more information, see [Retrieve secrets through environment variables](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/secrets-envvar.html) in the Amazon ECS Developer Guide.

name -> (string)

The name of the container that receives the override. This parameter is required if any override is specified.

command -> (list)

The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.

(string)

environment -> (list)

The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.

(structure)

A key-value pair object.

name -> (string)

The name of the key-value pair. For environment variables, this is the name of the environment variable.

value -> (string)

The value of the key-value pair. For environment variables, this is the value of the environment variable.

environmentFiles -> (list)

A list of files containing the environment variables to pass to a container, instead of the value from the container definition.

(structure)

A list of files containing the environment variables to pass to a container. You can specify up to ten environment files. The file must have a `.env` file extension. Each line in an environment file should contain an environment variable in `VARIABLE=VALUE` format. Lines beginning with `#` are treated as comments and are ignored.

If there are environment variables specified using the `environment` parameter in a container definition, they take precedence over the variables contained within an environment file. If multiple environment files are specified that contain the same variable, theyâre processed from the top down. We recommend that you use unique variable names. For more information, see [Use a file to pass environment variables to a container](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/use-environment-file.html) in the *Amazon Elastic Container Service Developer Guide* .

Environment variable files are objects in Amazon S3 and all Amazon S3 security considerations apply.

You must use the following platforms for the Fargate launch type:

- Linux platform version `1.4.0` or later.
- Windows platform version `1.0.0` or later.

Consider the following when using the Fargate launch type:

- The file is handled like a native Docker env-file.
- There is no support for shell escape handling.
- The container entry point interperts the `VARIABLE` values.

value -> (string)

The Amazon Resource Name (ARN) of the Amazon S3 object containing the environment variable file.

type -> (string)

The file type to use. Environment files are objects in Amazon S3. The only supported value is `s3` .

cpu -> (integer)

The number of `cpu` units reserved for the container, instead of the default value from the task definition. You must also specify a container name.

memory -> (integer)

The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.

memoryReservation -> (integer)

The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.

resourceRequirements -> (list)

The type and amount of a resource to assign to a container, instead of the default value from the task definition. The only supported resource is a GPU.

(structure)

The type and amount of a resource to assign to a container. The supported resource types are GPUs and Elastic Inference accelerators. For more information, see [Working with GPUs on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html) or [Working with Amazon Elastic Inference on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-inference.html) in the *Amazon Elastic Container Service Developer Guide*

value -> (string)

The value for the specified resource type.

When the type is `GPU` , the value is the number of physical `GPUs` the Amazon ECS container agent reserves for the container. The number of GPUs thatâs reserved for all containers in a task canât exceed the number of available GPUs on the container instance that the task is launched on.

When the type is `InferenceAccelerator` , the `value` matches the `deviceName` for an [InferenceAccelerator](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_InferenceAccelerator.html) specified in a task definition.

type -> (string)

The type of resource to assign to a container.

cpu -> (string)

The CPU override for the task.

inferenceAcceleratorOverrides -> (list)

The Elastic Inference accelerator override for the task.

(structure)

Details on an Elastic Inference accelerator task override. This parameter is used to override the Elastic Inference accelerator specified in the task definition. For more information, see [Working with Amazon Elastic Inference on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-inference.html) in the *Amazon Elastic Container Service Developer Guide* .

deviceName -> (string)

The Elastic Inference accelerator device name to override for the task. This parameter must match a `deviceName` specified in the task definition.

deviceType -> (string)

The Elastic Inference accelerator type to use.

executionRoleArn -> (string)

The Amazon Resource Name (ARN) of the task execution role override for the task. For more information, see [Amazon ECS task execution IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html) in the *Amazon Elastic Container Service Developer Guide* .

memory -> (string)

The memory override for the task.

taskRoleArn -> (string)

The Amazon Resource Name (ARN) of the role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. For more information, see [IAM Role for Tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide* .

ephemeralStorage -> (structure)

The ephemeral storage setting override for the task.

### Note

This parameter is only supported for tasks hosted on Fargate that use the following platform versions:

- Linux platform version `1.4.0` or later.
- Windows platform version `1.0.0` or later.

sizeInGiB -> (integer)

The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is `21` GiB and the maximum supported value is `200` GiB.

JSON Syntax:

```
{
  "containerOverrides": [
    {
      "name": "string",
      "command": ["string", ...],
      "environment": [
        {
          "name": "string",
          "value": "string"
        }
        ...
      ],
      "environmentFiles": [
        {
          "value": "string",
          "type": "s3"
        }
        ...
      ],
      "cpu": integer,
      "memory": integer,
      "memoryReservation": integer,
      "resourceRequirements": [
        {
          "value": "string",
          "type": "GPU"|"InferenceAccelerator"
        }
        ...
      ]
    }
    ...
  ],
  "cpu": "string",
  "inferenceAcceleratorOverrides": [
    {
      "deviceName": "string",
      "deviceType": "string"
    }
    ...
  ],
  "executionRoleArn": "string",
  "memory": "string",
  "taskRoleArn": "string",
  "ephemeralStorage": {
    "sizeInGiB": integer
  }
}
```

`--placement-constraints` (list)

An array of placement constraint objects to use for the task. You can specify up to 10 constraints for each task (including constraints in the task definition and those specified at runtime).

(structure)

An object representing a constraint on task placement. For more information, see [Task placement constraints](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html) in the *Amazon Elastic Container Service Developer Guide* .

### Note

If youâre using the Fargate launch type, task placement constraints arenât supported.

type -> (string)

The type of constraint. Use `distinctInstance` to ensure that each task in a particular group is running on a different container instance. Use `memberOf` to restrict the selection to a group of valid candidates.

expression -> (string)

A cluster query language expression to apply to the constraint. The expression can have a maximum length of 2000 characters. You canât specify an expression if the constraint type is `distinctInstance` . For more information, see [Cluster query language](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html) in the *Amazon Elastic Container Service Developer Guide* .

Shorthand Syntax:

```
type=string,expression=string ...
```

JSON Syntax:

```
[
  {
    "type": "distinctInstance"|"memberOf",
    "expression": "string"
  }
  ...
]
```

`--placement-strategy` (list)

The placement strategy objects to use for the task. You can specify a maximum of 5 strategy rules for each task.

(structure)

The task placement strategy for a task or service. For more information, see [Task placement strategies](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html) in the *Amazon Elastic Container Service Developer Guide* .

type -> (string)

The type of placement strategy. The `random` placement strategy randomly places tasks on available candidates. The `spread` placement strategy spreads placement across available candidates evenly based on the `field` parameter. The `binpack` strategy places tasks on available candidates that have the least available amount of the resource thatâs specified with the `field` parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory but still enough to run the task.

field -> (string)

The field to apply the placement strategy against. For the `spread` placement strategy, valid values are `instanceId` (or `host` , which has the same effect), or any platform or custom attribute thatâs applied to a container instance, such as `attribute:ecs.availability-zone` . For the `binpack` placement strategy, valid values are `cpu` and `memory` . For the `random` placement strategy, this field is not used.

Shorthand Syntax:

```
type=string,field=string ...
```

JSON Syntax:

```
[
  {
    "type": "random"|"spread"|"binpack",
    "field": "string"
  }
  ...
]
```

`--platform-version` (string)

The platform version the task uses. A platform version is only specified for tasks hosted on Fargate. If one isnât specified, the `LATEST` platform version is used. For more information, see [Fargate platform versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide* .

`--propagate-tags` (string)

Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags arenât propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the`TagResource <[https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html)>`__ API action.

### Note

An error will be received if you specify the `SERVICE` option when running a task.

Possible values:

- `TASK_DEFINITION`
- `SERVICE`
- `NONE`

`--reference-id` (string)

This parameter is only used by Amazon ECS. It is not intended for use by customers.

`--started-by` (string)

An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the `startedBy` parameter. You can then identify which tasks belong to that job by filtering the results of a [ListTasks](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html) call with the `startedBy` value. Up to 128 letters (uppercase and lowercase), numbers, hyphens (-), forward slash (/), and underscores (_) are allowed.

If a task is started by an Amazon ECS service, then the `startedBy` parameter contains the deployment ID of the service that starts it.

`--tags` (list)

The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.

The following basic restrictions apply to tags:

- Maximum number of tags per resource - 50
- For each resource, each tag key must be unique, and each tag key can have only one value.
- Maximum key length - 128 Unicode characters in UTF-8
- Maximum value length - 256 Unicode characters in UTF-8
- If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.
- Tag keys and values are case-sensitive.
- Do not use `aws:` , `AWS:` , or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.

(structure)

The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value. You define them.

The following basic restrictions apply to tags:

- Maximum number of tags per resource - 50
- For each resource, each tag key must be unique, and each tag key can have only one value.
- Maximum key length - 128 Unicode characters in UTF-8
- Maximum value length - 256 Unicode characters in UTF-8
- If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.
- Tag keys and values are case-sensitive.
- Do not use `aws:` , `AWS:` , or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.

key -> (string)

One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.

value -> (string)

The optional part of a key-value pair that make up a tag. A `value` acts as a descriptor within a tag category (key).

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
```

`--task-definition` (string)

The `family` and `revision` (`family:revision` ) or full ARN of the task definition to run. If a `revision` isnât specified, the latest `ACTIVE` revision is used.

The full ARN value must match the value that you specified as the `Resource` of the principalâs permissions policy.

When you specify a task definition, you must either specify a specific revision, or all revisions in the ARN.

To specify a specific revision, include the revision number in the ARN. For example, to specify revision 2, use `arn:aws:ecs:us-east-1:111122223333:task-definition/TaskFamilyName:2` .

To specify all revisions, use the wildcard (*) in the ARN. For example, to specify all revisions, use `arn:aws:ecs:us-east-1:111122223333:task-definition/TaskFamilyName:*` .

For more information, see [Policy Resources for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources) in the Amazon Elastic Container Service Developer Guide.

`--client-token` (string)

An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 64 characters are allowed. The valid characters are characters in the range of 33-126, inclusive. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/ECS_Idempotency.html) .

`--volume-configurations` (list)

The details of the volume that was `configuredAtLaunch` . You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in in [TaskManagedEBSVolumeConfiguration](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskManagedEBSVolumeConfiguration.html) . The `name` of the volume must match the `name` from the task definition.

(structure)

Configuration settings for the task volume that was `configuredAtLaunch` that werenât set during `RegisterTaskDef` .

name -> (string)

The name of the volume. This value must match the volume name from the `Volume` object in the task definition.

managedEBSVolume -> (structure)

The configuration for the Amazon EBS volume that Amazon ECS creates and manages on your behalf. These settings are used to create each Amazon EBS volume, with one volume created for each task. The Amazon EBS volumes are visible in your account in the Amazon EC2 console once they are created.

encrypted -> (boolean)

Indicates whether the volume should be encrypted. If you turn on Region-level Amazon EBS encryption by default but set this value as `false` , the setting is overridden and the volume is encrypted with the KMS key specified for Amazon EBS encryption by default. This parameter maps 1:1 with the `Encrypted` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference* .

kmsKeyId -> (string)

The Amazon Resource Name (ARN) identifier of the Amazon Web Services Key Management Service key to use for Amazon EBS encryption. When a key is specified using this parameter, it overrides Amazon EBS default encryption or any KMS key that you specified for cluster-level managed storage encryption. This parameter maps 1:1 with the `KmsKeyId` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference* . For more information about encrypting Amazon EBS volumes attached to a task, see [Encrypt data stored in Amazon EBS volumes attached to Amazon ECS tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-kms-encryption.html) .

### Warning

Amazon Web Services authenticates the Amazon Web Services Key Management Service key asynchronously. Therefore, if you specify an ID, alias, or ARN that is invalid, the action can appear to complete, but eventually fails.

volumeType -> (string)

The volume type. This parameter maps 1:1 with the `VolumeType` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference* . For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) in the *Amazon EC2 User Guide* .

The following are the supported volume types.

- General Purpose SSD: `gp2` [|](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/run-task.html#id1)`gp3`
- Provisioned IOPS SSD: `io1` [|](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/run-task.html#id3)`io2`
- Throughput Optimized HDD: `st1`
- Cold HDD: `sc1`
- Magnetic: `standard`

### Note

The magnetic volume type is not supported on Fargate.

sizeInGiB -> (integer)

The size of the volume in GiB. You must specify either a volume size or a snapshot ID. If you specify a snapshot ID, the snapshot size is used for the volume size by default. You can optionally specify a volume size greater than or equal to the snapshot size. This parameter maps 1:1 with the `Size` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference* .

The following are the supported volume size values for each volume type.

- `gp2` and `gp3` : 1-16,384
- `io1` and `io2` : 4-16,384
- `st1` and `sc1` : 125-16,384
- `standard` : 1-1,024

snapshotId -> (string)

The snapshot that Amazon ECS uses to create the volume. You must specify either a snapshot ID or a volume size. This parameter maps 1:1 with the `SnapshotId` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference* .

volumeInitializationRate -> (integer)

The rate, in MiB/s, at which data is fetched from a snapshot of an existing Amazon EBS volume to create a new volume for attachment to the task. This property can be specified only if you specify a `snapshotId` . For more information, see [Initialize Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html) in the *Amazon EBS User Guide* .

iops -> (integer)

The number of I/O operations per second (IOPS). For `gp3` , `io1` , and `io2` volumes, this represents the number of IOPS that are provisioned for the volume. For `gp2` volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.

The following are the supported values for each volume type.

- `gp3` : 3,000 - 16,000 IOPS
- `io1` : 100 - 64,000 IOPS
- `io2` : 100 - 256,000 IOPS

This parameter is required for `io1` and `io2` volume types. The default for `gp3` volumes is `3,000 IOPS` . This parameter is not supported for `st1` , `sc1` , or `standard` volume types.

This parameter maps 1:1 with the `Iops` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference* .

throughput -> (integer)

The throughput to provision for a volume, in MiB/s, with a maximum of 1,000 MiB/s. This parameter maps 1:1 with the `Throughput` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference* .

### Warning

This parameter is only supported for the `gp3` volume type.

tagSpecifications -> (list)

The tags to apply to the volume. Amazon ECS applies service-managed tags by default. This parameter maps 1:1 with the `TagSpecifications.N` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference* .

(structure)

The tag specifications of an Amazon EBS volume.

resourceType -> (string)

The type of volume resource.

tags -> (list)

The tags applied to this Amazon EBS volume. `AmazonECSCreated` and `AmazonECSManaged` are reserved tags that canât be used.

(structure)

The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value. You define them.

The following basic restrictions apply to tags:

- Maximum number of tags per resource - 50
- For each resource, each tag key must be unique, and each tag key can have only one value.
- Maximum key length - 128 Unicode characters in UTF-8
- Maximum value length - 256 Unicode characters in UTF-8
- If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.
- Tag keys and values are case-sensitive.
- Do not use `aws:` , `AWS:` , or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.

key -> (string)

One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.

value -> (string)

The optional part of a key-value pair that make up a tag. A `value` acts as a descriptor within a tag category (key).

propagateTags -> (string)

Determines whether to propagate the tags from the task definition to the Amazon EBS volume. Tags can only propagate to a `SERVICE` specified in `ServiceVolumeConfiguration` . If no value is specified, the tags arenât propagated.

roleArn -> (string)

The ARN of the IAM role to associate with this volume. This is the Amazon ECS infrastructure IAM role that is used to manage your Amazon Web Services infrastructure. We recommend using the Amazon ECS-managed `AmazonECSInfrastructureRolePolicyForVolumes` IAM policy with this role. For more information, see [Amazon ECS infrastructure IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html) in the *Amazon ECS Developer Guide* .

terminationPolicy -> (structure)

The termination policy for the volume when the task exits. This provides a way to control whether Amazon ECS terminates the Amazon EBS volume when the task stops.

deleteOnTermination -> (boolean)

Indicates whether the volume should be deleted on when the task stops. If a value of `true` is specified, Amazon ECS deletes the Amazon EBS volume on your behalf when the task goes into the `STOPPED` state. If no value is specified, the default value is `true` is used. When set to `false` , Amazon ECS leaves the volume in your account.

filesystemType -> (string)

The Linux filesystem type for the volume. For volumes created from a snapshot, you must specify the same filesystem type that the volume was using when the snapshot was created. If there is a filesystem type mismatch, the task will fail to start.

The available filesystem types are `ext3` , `ext4` , and `xfs` . If no value is specified, the `xfs` filesystem type is used by default.

JSON Syntax:

```
[
  {
    "name": "string",
    "managedEBSVolume": {
      "encrypted": true|false,
      "kmsKeyId": "string",
      "volumeType": "string",
      "sizeInGiB": integer,
      "snapshotId": "string",
      "volumeInitializationRate": integer,
      "iops": integer,
      "throughput": integer,
      "tagSpecifications": [
        {
          "resourceType": "volume",
          "tags": [
            {
              "key": "string",
              "value": "string"
            }
            ...
          ],
          "propagateTags": "TASK_DEFINITION"|"SERVICE"|"NONE"
        }
        ...
      ],
      "roleArn": "string",
      "terminationPolicy": {
        "deleteOnTermination": true|false
      },
      "filesystemType": "ext3"|"ext4"|"xfs"|"ntfs"
    }
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To run a task on your default cluster**

The following `run-task` example runs a task on the default cluster and uses a client token.

```
aws ecs run-task \
    --cluster default \
    --task-definition sleep360:1 \
    --client-token 550e8400-e29b-41d4-a716-446655440000
```

Output:

```
{
    "tasks": [
        {
            "attachments": [],
            "attributes": [
                {
                    "name": "ecs.cpu-architecture",
                    "value": "x86_64"
                }
            ],
            "availabilityZone": "us-east-1b",
            "capacityProviderName": "example-capacity-provider",
            "clusterArn": "arn:aws:ecs:us-east-1:123456789012:cluster/default",
            "containerInstanceArn": "arn:aws:ecs:us-east-1:123456789012:container-instance/default/bc4d2ec611d04bb7bb97e83ceEXAMPLE",
            "containers": [
                {
                    "containerArn": "arn:aws:ecs:us-east-1:123456789012:container/default/d6f51cc5bbc94a47969c92035e9f66f8/75853d2d-711e-458a-8362-0f0aEXAMPLE",
                    "taskArn": "arn:aws:ecs:us-east-1:123456789012:task/default/d6f51cc5bbc94a47969c9203EXAMPLE",
                    "name": "sleep",
                    "image": "busybox",
                    "lastStatus": "PENDING",
                    "networkInterfaces": [],
                    "cpu": "10",
                    "memory": "10"
                }
            ],
            "cpu": "10",
            "createdAt": "2023-11-21T16:59:34.403000-05:00",
            "desiredStatus": "RUNNING",
            "enableExecuteCommand": false,
            "group": "family:sleep360",
            "lastStatus": "PENDING",
            "launchType": "EC2",
            "memory": "10",
            "overrides": {
                "containerOverrides": [
                    {
                        "name": "sleep"
                    }
                ],
                "inferenceAcceleratorOverrides": []
            },
            "tags": [],
            "taskArn": "arn:aws:ecs:us-east-1:123456789012:task/default/d6f51cc5bbc94a47969c9203EXAMPLE",
            "taskDefinitionArn": "arn:aws:ecs:us-east-1:123456789012:task-definition/sleep360:1",
            "version": 1
        }
    ],
    "failures": []
}
```

For more information, see [Running an application as a standalone task](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/standalone-task-create.html) in the *Amazon ECS Developer Guide*.

**Example 2: To configure an Amazon EBS volume for a standalone task**

The following `run-task` example configures an encrypted Amazon EBS volume for a Fargate task on the default cluster. You must have an Amazon ECS infrastructure role configured with the `AmazonECSInfrastructureRolePolicyForVolumes` managed policy attached. You must specify a task definition with the same volume name as in the `run-task` request. This example uses the `--cli-input-json` option and a JSON input file called `ebs.json`.

```
aws ecs run-task \
    --cli-input-json file://ebs.json
```

Contents of `ebs.json`:

```
{
   "cluster": "default",
   "taskDefinition": "mytaskdef",
   "launchType": "FARGATE",
   "networkConfiguration":{
        "awsvpcConfiguration":{
            "assignPublicIp": "ENABLED",
            "securityGroups": ["sg-12344321"],
            "subnets":["subnet-12344321"]
        }
    },
   "volumeConfigurations": [
        {
            "name": "myEBSVolume",
            "managedEBSVolume": {
                "volumeType": "gp3",
                "sizeInGiB": 100,
                "roleArn":"arn:aws:iam::1111222333:role/ecsInfrastructureRole",
                "encrypted": true,
                "kmsKeyId": "arn:aws:kms:region:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
            }
        }
    ]
}
```

Output:

```
{
    "tasks": [
        {
            "attachments": [
                {
                    "id": "ce868693-15ca-4083-91ac-f782f64000c9",
                    "type": "ElasticNetworkInterface",
                    "status": "PRECREATED",
                    "details": [
                        {
                        "name": "subnetId",
                        "value": "subnet-070982705451dad82"
                        }
                    ]
                },
                {
                    "id": "a17ed863-786c-4372-b5b3-b23e53f37877",
                    "type": "AmazonElasticBlockStorage",
                    "status": "CREATED",
                    "details": [
                        {
                            "name": "roleArn",
                            "value": "arn:aws:iam::123456789012:role/ecsInfrastructureRole"
                        },
                        {
                            "name": "volumeName",
                            "value": "myEBSVolume"
                        },
                        {
                            "name": "deleteOnTermination",
                            "value": "true"
                        }
                    ]
                }
            ],
            "attributes": [
                {
                    "name": "ecs.cpu-architecture",
                    "value": "x86_64"
                }
            ],
            "availabilityZone": "us-west-2b",
            "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/default",
            "containers": [
                {
                    "containerArn": "arn:aws:ecs:us-west-2:123456789012:container/default/7f1fbd3629434cc4b82d72d2f09b67c9/e21962a2-f328-4699-98a3-5161ac2c186a",
                    "taskArn": "arn:aws:ecs:us-west-2:123456789012:task/default/7f1fbd3629434cc4b82d72d2f09b67c9",
                    "name": "container-using-ebs",
                    "image": "amazonlinux:2",
                    "lastStatus": "PENDING",
                    "networkInterfaces": [],
                    "cpu": "0"
                }
            ],
            "cpu": "1024",
            "createdAt": "2025-01-23T10:29:46.650000-06:00",
            "desiredStatus": "RUNNING",
            "enableExecuteCommand": false,
            "group": "family:mytaskdef",
            "lastStatus": "PROVISIONING",
            "launchType": "FARGATE",
            "memory": "3072",
            "overrides": {
                "containerOverrides": [
                    {
                        "name": "container-using-ebs"
                    }
                ],
                "inferenceAcceleratorOverrides": []
            },
            "platformVersion": "1.4.0",
            "platformFamily": "Linux",
            "tags": [],
            "taskArn": "arn:aws:ecs:us-west-2:123456789012:task/default/7f1fbd3629434cc4b82d72d2f09b67c9",
            "taskDefinitionArn": "arn:aws:ecs:us-west-2:123456789012:task-definition/mytaskdef:4",
            "version": 1,
            "ephemeralStorage": {
                "sizeInGiB": 20
            },
            "fargateEphemeralStorage": {
                "sizeInGiB": 20
            }
        }
    ],
    "failures": []
}
```

For more information, see [Use Amazon EBS volumes with Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html) in the *Amazon ECS Developer Guide*.

## Output

tasks -> (list)

A full description of the tasks that were run. The tasks that were successfully placed on your cluster are described here.

(structure)

Details on a task in a cluster.

attachments -> (list)

The Elastic Network Adapter thatâs associated with the task if the task uses the `awsvpc` network mode.

(structure)

An object representing a container instance or task attachment.

id -> (string)

The unique identifier for the attachment.

type -> (string)

The type of the attachment, such as `ElasticNetworkInterface` , `Service Connect` , and `AmazonElasticBlockStorage` .

status -> (string)

The status of the attachment. Valid values are `PRECREATED` , `CREATED` , `ATTACHING` , `ATTACHED` , `DETACHING` , `DETACHED` , `DELETED` , and `FAILED` .

details -> (list)

Details of the attachment.

For elastic network interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.

For Service Connect services, this includes `portName` , `clientAliases` , `discoveryName` , and `ingressPortOverride` .

For Elastic Block Storage, this includes `roleArn` , `deleteOnTermination` , `volumeName` , `volumeId` , and `statusReason` (only when the attachment fails to create or attach).

(structure)

A key-value pair object.

name -> (string)

The name of the key-value pair. For environment variables, this is the name of the environment variable.

value -> (string)

The value of the key-value pair. For environment variables, this is the value of the environment variable.

attributes -> (list)

The attributes of the task

(structure)

An attribute is a name-value pair thatâs associated with an Amazon ECS object. Use attributes to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see [Attributes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes) in the *Amazon Elastic Container Service Developer Guide* .

name -> (string)

The name of the attribute. The `name` must contain between 1 and 128 characters. The name may contain letters (uppercase and lowercase), numbers, hyphens (-), underscores (_), forward slashes (/), back slashes (), or periods (.).

value -> (string)

The value of the attribute. The `value` must contain between 1 and 128 characters. It can contain letters (uppercase and lowercase), numbers, hyphens (-), underscores (_), periods (.), at signs (@), forward slashes (/), back slashes (), colons (:), or spaces. The value canât start or end with a space.

targetType -> (string)

The type of the target to attach the attribute with. This parameter is required if you use the short form ID for a resource instead of the full ARN.

targetId -> (string)

The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).

availabilityZone -> (string)

The Availability Zone for the task.

capacityProviderName -> (string)

The capacity provider thatâs associated with the task.

clusterArn -> (string)

The ARN of the cluster that hosts the task.

connectivity -> (string)

The connectivity status of a task.

connectivityAt -> (timestamp)

The Unix timestamp for the time when the task last went into `CONNECTED` status.

containerInstanceArn -> (string)

The ARN of the container instances that host the task.

containers -> (list)

The containers thatâs associated with the task.

(structure)

A Docker container thatâs part of a task.

containerArn -> (string)

The Amazon Resource Name (ARN) of the container.

taskArn -> (string)

The ARN of the task.

name -> (string)

The name of the container.

image -> (string)

The image used for the container.

imageDigest -> (string)

The container image manifest digest.

runtimeId -> (string)

The ID of the Docker container.

lastStatus -> (string)

The last known status of the container.

exitCode -> (integer)

The exit code returned from the container.

reason -> (string)

A short (1024 max characters) human-readable string to provide additional details about a running or stopped container.

networkBindings -> (list)

The network bindings associated with the container.

(structure)

Details on the network bindings between a container and its host container instance. After a task reaches the `RUNNING` status, manual and automatic host and container port assignments are visible in the `networkBindings` section of [DescribeTasks](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html) API responses.

bindIP -> (string)

The IP address that the container is bound to on the container instance.

containerPort -> (integer)

The port number on the container thatâs used with the network binding.

hostPort -> (integer)

The port number on the host thatâs used with the network binding.

protocol -> (string)

The protocol used for the network binding.

containerPortRange -> (string)

The port number range on the container thatâs bound to the dynamically mapped host port range.

The following rules apply when you specify a `containerPortRange` :

- You must use either the `bridge` network mode or the `awsvpc` network mode.
- This parameter is available for both the EC2 and Fargate launch types.
- This parameter is available for both the Linux and Windows operating systems.
- The container instance must have at least version 1.67.0 of the container agent and at least version 1.67.0-1 of the `ecs-init` package
- You can specify a maximum of 100 port ranges per container.
- You do not specify a `hostPortRange` . The value of the `hostPortRange` is set as follows:
- For containers in a task with the `awsvpc` network mode, the `hostPortRange` is set to the same value as the `containerPortRange` . This is a static mapping strategy.
- For containers in a task with the `bridge` network mode, the Amazon ECS agent finds open host ports from the default ephemeral range and passes it to docker to bind them to the container ports.
- The `containerPortRange` valid values are between 1 and 65535.
- A port can only be included in one port mapping per container.
- You cannot specify overlapping port ranges.
- The first port in the range must be less than last port in the range.
- Docker recommends that you turn off the docker-proxy in the Docker daemon config file when you have a large number of ports. For more information, see [Issue #11185](https://github.com/moby/moby/issues/11185) on the Github website. For information about how to turn off the docker-proxy in the Docker daemon config file, see [Docker daemon](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/bootstrap_container_instance.html#bootstrap_docker_daemon) in the *Amazon ECS Developer Guide* .

You can call ` `DescribeTasks` [https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks).html`__ to view the `hostPortRange` which are the host ports that are bound to the container ports.

hostPortRange -> (string)

The port number range on the host thatâs used with the network binding. This is assigned is assigned by Docker and delivered by the Amazon ECS agent.

networkInterfaces -> (list)

The network interfaces associated with the container.

(structure)

An object representing the elastic network interface for tasks that use the `awsvpc` network mode.

attachmentId -> (string)

The attachment ID for the network interface.

privateIpv4Address -> (string)

The private IPv4 address for the network interface.

ipv6Address -> (string)

The private IPv6 address for the network interface.

healthStatus -> (string)

The health status of the container. If health checks arenât configured for this container in its task definition, then it reports the health status as `UNKNOWN` .

managedAgents -> (list)

The details of any Amazon ECS managed agents associated with the container.

(structure)

Details about the managed agent status for the container.

lastStartedAt -> (timestamp)

The Unix timestamp for the time when the managed agent was last started.

name -> (string)

The name of the managed agent. When the execute command feature is turned on, the managed agent name is `ExecuteCommandAgent` .

reason -> (string)

The reason for why the managed agent is in the state it is in.

lastStatus -> (string)

The last known status of the managed agent.

cpu -> (string)

The number of CPU units set for the container. The value is `0` if no value was specified in the container definition when the task definition was registered.

memory -> (string)

The hard limit (in MiB) of memory set for the container.

memoryReservation -> (string)

The soft limit (in MiB) of memory set for the container.

gpuIds -> (list)

The IDs of each GPU assigned to the container.

(string)

cpu -> (string)

The number of CPU units used by the task as expressed in a task definition. It can be expressed as an integer using CPU units (for example, `1024` ). It can also be expressed as a string using vCPUs (for example, `1 vCPU` or `1 vcpu` ). String values are converted to an integer that indicates the CPU units when the task definition is registered.

If youâre using the EC2 launch type or the external launch type, this field is optional. Supported values are between `128` CPU units (`0.125` vCPUs) and `196608` CPU units (`192` vCPUs). If you do not specify a value, the parameter is ignored.

This field is required for Fargate. For information about the valid values, see [Task size](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#task_size) in the *Amazon Elastic Container Service Developer Guide* .

createdAt -> (timestamp)

The Unix timestamp for the time when the task was created. More specifically, itâs for the time when the task entered the `PENDING` state.

desiredStatus -> (string)

The desired status of the task. For more information, see [Task Lifecycle](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-lifecycle.html) .

enableExecuteCommand -> (boolean)

Determines whether execute command functionality is turned on for this task. If `true` , execute command functionality is turned on all the containers in the task.

executionStoppedAt -> (timestamp)

The Unix timestamp for the time when the task execution stopped.

group -> (string)

The name of the task group thatâs associated with the task.

healthStatus -> (string)

The health status for the task. Itâs determined by the health of the essential containers in the task. If all essential containers in the task are reporting as `HEALTHY` , the task status also reports as `HEALTHY` . If any essential containers in the task are reporting as `UNHEALTHY` or `UNKNOWN` , the task status also reports as `UNHEALTHY` or `UNKNOWN` .

### Note

The Amazon ECS container agent doesnât monitor or report on Docker health checks that are embedded in a container image and not specified in the container definition. For example, this includes those specified in a parent image or from the imageâs Dockerfile. Health check parameters that are specified in a container definition override any Docker health checks that are found in the container image.

inferenceAccelerators -> (list)

The Elastic Inference accelerator thatâs associated with the task.

(structure)

Details on an Elastic Inference accelerator. For more information, see [Working with Amazon Elastic Inference on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-inference.html) in the *Amazon Elastic Container Service Developer Guide* .

deviceName -> (string)

The Elastic Inference accelerator device name. The `deviceName` must also be referenced in a container definition as a [ResourceRequirement](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ResourceRequirement.html) .

deviceType -> (string)

The Elastic Inference accelerator type to use.

lastStatus -> (string)

The last known status for the task. For more information, see [Task Lifecycle](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-lifecycle.html) .

launchType -> (string)

The infrastructure where your task runs on. For more information, see [Amazon ECS launch types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html) in the *Amazon Elastic Container Service Developer Guide* .

memory -> (string)

The amount of memory (in MiB) that the task uses as expressed in a task definition. It can be expressed as an integer using MiB (for example, `1024` ). If itâs expressed as a string using GB (for example, `1GB` or `1 GB` ), itâs converted to an integer indicating the MiB when the task definition is registered.

If you use the EC2 launch type, this field is optional.

If you use the Fargate launch type, this field is required. You must use one of the following values. The value that you choose determines the range of supported values for the `cpu` parameter.

- 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available `cpu` values: 256 (.25 vCPU)
- 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available `cpu` values: 512 (.5 vCPU)
- 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available `cpu` values: 1024 (1 vCPU)
- Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available `cpu` values: 2048 (2 vCPU)
- Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available `cpu` values: 4096 (4 vCPU)
- Between 16 GB and 60 GB in 4 GB increments - Available `cpu` values: 8192 (8 vCPU) This option requires Linux platform `1.4.0` or later.
- Between 32GB and 120 GB in 8 GB increments - Available `cpu` values: 16384 (16 vCPU) This option requires Linux platform `1.4.0` or later.

overrides -> (structure)

One or more container overrides.

containerOverrides -> (list)

One or more container overrides that are sent to a task.

(structure)

The overrides that are sent to a container. An empty container override can be passed in. An example of an empty container override is `{"containerOverrides": [ ] }` . If a non-empty container override is specified, the `name` parameter must be included.

You can use Secrets Manager or Amazon Web Services Systems Manager Parameter Store to store the sensitive data. For more information, see [Retrieve secrets through environment variables](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/secrets-envvar.html) in the Amazon ECS Developer Guide.

name -> (string)

The name of the container that receives the override. This parameter is required if any override is specified.

command -> (list)

The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.

(string)

environment -> (list)

The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.

(structure)

A key-value pair object.

name -> (string)

The name of the key-value pair. For environment variables, this is the name of the environment variable.

value -> (string)

The value of the key-value pair. For environment variables, this is the value of the environment variable.

environmentFiles -> (list)

A list of files containing the environment variables to pass to a container, instead of the value from the container definition.

(structure)

A list of files containing the environment variables to pass to a container. You can specify up to ten environment files. The file must have a `.env` file extension. Each line in an environment file should contain an environment variable in `VARIABLE=VALUE` format. Lines beginning with `#` are treated as comments and are ignored.

If there are environment variables specified using the `environment` parameter in a container definition, they take precedence over the variables contained within an environment file. If multiple environment files are specified that contain the same variable, theyâre processed from the top down. We recommend that you use unique variable names. For more information, see [Use a file to pass environment variables to a container](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/use-environment-file.html) in the *Amazon Elastic Container Service Developer Guide* .

Environment variable files are objects in Amazon S3 and all Amazon S3 security considerations apply.

You must use the following platforms for the Fargate launch type:

- Linux platform version `1.4.0` or later.
- Windows platform version `1.0.0` or later.

Consider the following when using the Fargate launch type:

- The file is handled like a native Docker env-file.
- There is no support for shell escape handling.
- The container entry point interperts the `VARIABLE` values.

value -> (string)

The Amazon Resource Name (ARN) of the Amazon S3 object containing the environment variable file.

type -> (string)

The file type to use. Environment files are objects in Amazon S3. The only supported value is `s3` .

cpu -> (integer)

The number of `cpu` units reserved for the container, instead of the default value from the task definition. You must also specify a container name.

memory -> (integer)

The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.

memoryReservation -> (integer)

The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.

resourceRequirements -> (list)

The type and amount of a resource to assign to a container, instead of the default value from the task definition. The only supported resource is a GPU.

(structure)

The type and amount of a resource to assign to a container. The supported resource types are GPUs and Elastic Inference accelerators. For more information, see [Working with GPUs on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html) or [Working with Amazon Elastic Inference on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-inference.html) in the *Amazon Elastic Container Service Developer Guide*

value -> (string)

The value for the specified resource type.

When the type is `GPU` , the value is the number of physical `GPUs` the Amazon ECS container agent reserves for the container. The number of GPUs thatâs reserved for all containers in a task canât exceed the number of available GPUs on the container instance that the task is launched on.

When the type is `InferenceAccelerator` , the `value` matches the `deviceName` for an [InferenceAccelerator](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_InferenceAccelerator.html) specified in a task definition.

type -> (string)

The type of resource to assign to a container.

cpu -> (string)

The CPU override for the task.

inferenceAcceleratorOverrides -> (list)

The Elastic Inference accelerator override for the task.

(structure)

Details on an Elastic Inference accelerator task override. This parameter is used to override the Elastic Inference accelerator specified in the task definition. For more information, see [Working with Amazon Elastic Inference on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-inference.html) in the *Amazon Elastic Container Service Developer Guide* .

deviceName -> (string)

The Elastic Inference accelerator device name to override for the task. This parameter must match a `deviceName` specified in the task definition.

deviceType -> (string)

The Elastic Inference accelerator type to use.

executionRoleArn -> (string)

The Amazon Resource Name (ARN) of the task execution role override for the task. For more information, see [Amazon ECS task execution IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html) in the *Amazon Elastic Container Service Developer Guide* .

memory -> (string)

The memory override for the task.

taskRoleArn -> (string)

The Amazon Resource Name (ARN) of the role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. For more information, see [IAM Role for Tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide* .

ephemeralStorage -> (structure)

The ephemeral storage setting override for the task.

### Note

This parameter is only supported for tasks hosted on Fargate that use the following platform versions:

- Linux platform version `1.4.0` or later.
- Windows platform version `1.0.0` or later.

sizeInGiB -> (integer)

The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is `21` GiB and the maximum supported value is `200` GiB.

platformVersion -> (string)

The platform version where your task runs on. A platform version is only specified for tasks that use the Fargate launch type. If you didnât specify one, the `LATEST` platform version is used. For more information, see [Fargate Platform Versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide* .

platformFamily -> (string)

The operating system that your tasks are running on. A platform family is specified only for tasks that use the Fargate launch type.

All tasks that run as part of this service must use the same `platformFamily` value as the service (for example, `LINUX.` ).

pullStartedAt -> (timestamp)

The Unix timestamp for the time when the container image pull began.

pullStoppedAt -> (timestamp)

The Unix timestamp for the time when the container image pull completed.

startedAt -> (timestamp)

The Unix timestamp for the time when the task started. More specifically, itâs for the time when the task transitioned from the `PENDING` state to the `RUNNING` state.

startedBy -> (string)

The tag specified when a task is started. If an Amazon ECS service started the task, the `startedBy` parameter contains the deployment ID of that service.

stopCode -> (string)

The stop code indicating why a task was stopped. The `stoppedReason` might contain additional details.

For more information about stop code, see [Stopped tasks error codes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/stopped-task-error-codes.html) in the *Amazon ECS Developer Guide* .

stoppedAt -> (timestamp)

The Unix timestamp for the time when the task was stopped. More specifically, itâs for the time when the task transitioned from the `RUNNING` state to the `STOPPED` state.

stoppedReason -> (string)

The reason that the task was stopped.

stoppingAt -> (timestamp)

The Unix timestamp for the time when the task stops. More specifically, itâs for the time when the task transitions from the `RUNNING` state to `STOPPING` .

tags -> (list)

The metadata that you apply to the task to help you categorize and organize the task. Each tag consists of a key and an optional value. You define both the key and value.

The following basic restrictions apply to tags:

- Maximum number of tags per resource - 50
- For each resource, each tag key must be unique, and each tag key can have only one value.
- Maximum key length - 128 Unicode characters in UTF-8
- Maximum value length - 256 Unicode characters in UTF-8
- If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.
- Tag keys and values are case-sensitive.
- Do not use `aws:` , `AWS:` , or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.

(structure)

The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value. You define them.

The following basic restrictions apply to tags:

- Maximum number of tags per resource - 50
- For each resource, each tag key must be unique, and each tag key can have only one value.
- Maximum key length - 128 Unicode characters in UTF-8
- Maximum value length - 256 Unicode characters in UTF-8
- If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.
- Tag keys and values are case-sensitive.
- Do not use `aws:` , `AWS:` , or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.

key -> (string)

One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.

value -> (string)

The optional part of a key-value pair that make up a tag. A `value` acts as a descriptor within a tag category (key).

taskArn -> (string)

The Amazon Resource Name (ARN) of the task.

taskDefinitionArn -> (string)

The ARN of the task definition that creates the task.

version -> (long)

The version counter for the task. Every time a task experiences a change that starts a CloudWatch event, the version counter is incremented. If you replicate your Amazon ECS task state with CloudWatch Events, you can compare the version of a task reported by the Amazon ECS API actions with the version reported in CloudWatch Events for the task (inside the `detail` object) to verify that the version in your event stream is current.

ephemeralStorage -> (structure)

The ephemeral storage settings for the task.

sizeInGiB -> (integer)

The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is `21` GiB and the maximum supported value is `200` GiB.

fargateEphemeralStorage -> (structure)

The Fargate ephemeral storage settings for the task.

sizeInGiB -> (integer)

The total amount, in GiB, of the ephemeral storage to set for the task. The minimum supported value is `20` GiB and the maximum supported value is `200` GiB.

kmsKeyId -> (string)

Specify an Key Management Service key ID to encrypt the ephemeral storage for the task.

failures -> (list)

Any failures associated with the call.

For information about how to address failures, see [Service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages.html#service-event-messages-list) and [API failure reasons](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/api_failures_messages.html) in the *Amazon Elastic Container Service Developer Guide* .

(structure)

A failed resource. For a list of common causes, see [API failure reasons](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/api_failures_messages.html) in the *Amazon Elastic Container Service Developer Guide* .

arn -> (string)

The Amazon Resource Name (ARN) of the failed resource.

reason -> (string)

The reason for the failure.

detail -> (string)

The details of the failure.