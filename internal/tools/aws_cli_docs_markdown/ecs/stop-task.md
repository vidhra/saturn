# stop-taskÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/stop-task.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/stop-task.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ecs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/index.html#cli-aws-ecs) ]

# stop-task

## Description

Stops a running task. Any tags associated with the task will be deleted.

When you call `StopTask` on a task, the equivalent of `docker stop` is issued to the containers running in the task. This results in a `SIGTERM` value and a default 30-second timeout, after which the `SIGKILL` value is sent and the containers are forcibly stopped. If the container handles the `SIGTERM` value gracefully and exits within 30 seconds from receiving it, no `SIGKILL` value is sent.

For Windows containers, POSIX signals do not work and runtime stops the container by sending a `CTRL_SHUTDOWN_EVENT` . For more information, see [Unable to react to graceful shutdown of (Windows) container #25982](https://github.com/moby/moby/issues/25982) on GitHub.

### Note

The default 30-second timeout can be configured on the Amazon ECS container agent with the `ECS_CONTAINER_STOP_TIMEOUT` variable. For more information, see [Amazon ECS Container Agent Configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html) in the *Amazon Elastic Container Service Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/StopTask)

## Synopsis

```
stop-task
[--cluster <value>]
--task <value>
[--reason <value>]
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

`--cluster` (string)

The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to stop. If you do not specify a cluster, the default cluster is assumed.

`--task` (string)

Thefull Amazon Resource Name (ARN) of the task.

`--reason` (string)

An optional message specified when a task is stopped. For example, if youâre using a custom scheduler, you can use this parameter to specify the reason for stopping the task here, and the message appears in subsequent [DescribeTasks](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html) > API operations on this task.

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

**To stop a task**

The following `stop-task` stops the specified task from running in the default cluster.

```
aws ecs stop-task \
    --task 666fdccc2e2d4b6894dd422f4eeee8f8
```

Output:

```
{
    "task": {
        "taskArn": "arn:aws:ecs:us-west-2:130757420319:task/default/666fdccc2e2d4b6894dd422f4eeee8f8",
        "clusterArn": "arn:aws:ecs:us-west-2:130757420319:cluster/default",
        "taskDefinitionArn": "arn:aws:ecs:us-west-2:130757420319:task-definition/sleep360:3",
        "containerInstanceArn": "arn:aws:ecs:us-west-2:130757420319:container-instance/default/765936fadbdd46b5991a4bd70c2a43d4",
        "overrides": {
            "containerOverrides": []
        },
        "lastStatus": "STOPPED",
        "desiredStatus": "STOPPED",
        "cpu": "128",
        "memory": "128",
        "containers": [],
        "version": 2,
        "stoppedReason": "Taskfailedtostart",
        "stopCode": "TaskFailedToStart",
        "connectivity": "CONNECTED",
        "connectivityAt": 1563421494.186,
        "pullStartedAt": 1563421494.252,
        "pullStoppedAt": 1563421496.252,
        "executionStoppedAt": 1563421497,
        "createdAt": 1563421494.186,
        "stoppingAt": 1563421497.252,
        "stoppedAt": 1563421497.252,
        "group": "family:sleep360",
        "launchType": "EC2",
        "attachments": [],
        "tags": []
    }
}
```

## Output

task -> (structure)

The task that was stopped.

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