# create-serviceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/create-service.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/create-service.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ecs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/index.html#cli-aws-ecs) ]

# create-service

## Description

Runs and maintains your desired number of tasks from a specified task definition. If the number of tasks running in a service drops below the `desiredCount` , Amazon ECS runs another copy of the task in the specified cluster. To update an existing service, use [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) .

### Note

On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.

### Note

Amazon Elastic Inference (EI) is no longer available to customers.

In addition to maintaining the desired count of tasks in your service, you can optionally run your service behind one or more load balancers. The load balancers distribute traffic across the tasks that are associated with the service. For more information, see [Service load balancing](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html) in the *Amazon Elastic Container Service Developer Guide* .

You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when creating or updating a service. `volumeConfigurations` is only supported for REPLICA service and not DAEMON service. For more infomation, see [Amazon EBS volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types) in the *Amazon Elastic Container Service Developer Guide* .

Tasks for services that donât use a load balancer are considered healthy if theyâre in the `RUNNING` state. Tasks for services that use a load balancer are considered healthy if theyâre in the `RUNNING` state and are reported as healthy by the load balancer.

There are two service scheduler strategies available:

- `REPLICA` - The replica scheduling strategy places and maintains your desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. For more information, see [Service scheduler concepts](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html) in the *Amazon Elastic Container Service Developer Guide* .
- `DAEMON` - The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks. It also stops tasks that donât meet the placement constraints. When using this strategy, you donât need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies. For more information, see [Service scheduler concepts](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html) in the *Amazon Elastic Container Service Developer Guide* .

You can optionally specify a deployment configuration for your service. The deployment is initiated by changing properties. For example, the deployment might be initiated by the task definition or by your desired count of a service. You can use [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) . The default value for a replica service for `minimumHealthyPercent` is 100%. The default value for a daemon service for `minimumHealthyPercent` is 0%.

If a service uses the `ECS` deployment controller, the minimum healthy percent represents a lower limit on the number of tasks in a service that must remain in the `RUNNING` state during a deployment. Specifically, it represents it as a percentage of your desired number of tasks (rounded up to the nearest integer). This happens when any of your container instances are in the `DRAINING` state if the service contains tasks using the EC2 launch type. Using this parameter, you can deploy without using additional cluster capacity. For example, if you set your service to have desired number of four tasks and a minimum healthy percent of 50%, the scheduler might stop two existing tasks to free up cluster capacity before starting two new tasks. If theyâre in the `RUNNING` state, tasks for services that donât use a load balancer are considered healthy . If theyâre in the `RUNNING` state and reported as healthy by the load balancer, tasks for services that *do* use a load balancer are considered healthy . The default value for minimum healthy percent is 100%.

If a service uses the `ECS` deployment controller, the **maximum percent** parameter represents an upper limit on the number of tasks in a service that are allowed in the `RUNNING` or `PENDING` state during a deployment. Specifically, it represents it as a percentage of the desired number of tasks (rounded down to the nearest integer). This happens when any of your container instances are in the `DRAINING` state if the service contains tasks using the EC2 launch type. Using this parameter, you can define the deployment batch size. For example, if your service has a desired number of four tasks and a maximum percent value of 200%, the scheduler may start four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). The default value for maximum percent is 200%.

If a service uses either the `CODE_DEPLOY` or `EXTERNAL` deployment controller types and tasks that use the EC2 launch type, the **minimum healthy percent** and **maximum percent** values are used only to define the lower and upper limit on the number of the tasks in the service that remain in the `RUNNING` state. This is while the container instances are in the `DRAINING` state. If the tasks in the service use the Fargate launch type, the minimum healthy percent and maximum percent values arenât used. This is the case even if theyâre currently visible when describing your service.

When creating a service that uses the `EXTERNAL` deployment controller, you can specify only parameters that arenât controlled at the task set level. The only required parameter is the service name. You control your services using the [CreateTaskSet](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateTaskSet.html) . For more information, see [Amazon ECS deployment types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html) in the *Amazon Elastic Container Service Developer Guide* .

When the service scheduler launches new tasks, it determines task placement. For information about task placement and task placement strategies, see [Amazon ECS task placement](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement.html) in the *Amazon Elastic Container Service Developer Guide*

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/CreateService)

## Synopsis

```
create-service
[--cluster <value>]
--service-name <value>
[--task-definition <value>]
[--availability-zone-rebalancing <value>]
[--load-balancers <value>]
[--service-registries <value>]
[--desired-count <value>]
[--client-token <value>]
[--launch-type <value>]
[--capacity-provider-strategy <value>]
[--platform-version <value>]
[--role <value>]
[--deployment-configuration <value>]
[--placement-constraints <value>]
[--placement-strategy <value>]
[--network-configuration <value>]
[--health-check-grace-period-seconds <value>]
[--scheduling-strategy <value>]
[--deployment-controller <value>]
[--tags <value>]
[--enable-ecs-managed-tags | --no-enable-ecs-managed-tags]
[--propagate-tags <value>]
[--enable-execute-command | --disable-execute-command]
[--service-connect-configuration <value>]
[--volume-configurations <value>]
[--vpc-lattice-configurations <value>]
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

The short name or full Amazon Resource Name (ARN) of the cluster that you run your service on. If you do not specify a cluster, the default cluster is assumed.

`--service-name` (string)

The name of your service. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a Region or across multiple Regions.

`--task-definition` (string)

The `family` and `revision` (`family:revision` ) or full ARN of the task definition to run in your service. If a `revision` isnât specified, the latest `ACTIVE` revision is used.

A task definition must be specified if the service uses either the `ECS` or `CODE_DEPLOY` deployment controllers.

For more information about deployment types, see [Amazon ECS deployment types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html) .

`--availability-zone-rebalancing` (string)

Indicates whether to use Availability Zone rebalancing for the service.

For more information, see [Balancing an Amazon ECS service across Availability Zones](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html) in the * *Amazon Elastic Container Service Developer Guide* * .

Possible values:

- `ENABLED`
- `DISABLED`

`--load-balancers` (list)

A load balancer object representing the load balancers to use with your service. For more information, see [Service load balancing](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html) in the *Amazon Elastic Container Service Developer Guide* .

If the service uses the rolling update (`ECS` ) deployment controller and using either an Application Load Balancer or Network Load Balancer, you must specify one or more target group ARNs to attach to the service. The service-linked role is required for services that use multiple target groups. For more information, see [Using service-linked roles for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html) in the *Amazon Elastic Container Service Developer Guide* .

If the service uses the `CODE_DEPLOY` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When creating an CodeDeploy deployment group, you specify two target groups (referred to as a `targetGroupPair` ). During a deployment, CodeDeploy determines which task set in your service has the status `PRIMARY` , and it associates one target group with it. Then, it also associates the other target group with the replacement task set. The load balancer can also have up to two listeners: a required listener for production traffic and an optional listener that you can use to perform validation tests with Lambda functions before routing production traffic to it.

If you use the `CODE_DEPLOY` deployment controller, these values can be changed when updating the service.

For Application Load Balancers and Network Load Balancers, this object must contain the load balancer target group ARN, the container name, and the container port to access from the load balancer. The container name must be as it appears in a container definition. The load balancer name parameter must be omitted. When a task from this service is placed on a container instance, the container instance and port combination is registered as a target in the target group thatâs specified here.

For Classic Load Balancers, this object must contain the load balancer name, the container name , and the container port to access from the load balancer. The container name must be as it appears in a container definition. The target group ARN parameter must be omitted. When a task from this service is placed on a container instance, the container instance is registered with the load balancer thatâs specified here.

Services with tasks that use the `awsvpc` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers arenât supported. Also, when you create any target groups for these services, you must choose `ip` as the target type, not `instance` . This is because tasks that use the `awsvpc` network mode are associated with an elastic network interface, not an Amazon EC2 instance.

(structure)

The load balancer configuration to use with a service or task set.

When you add, update, or remove a load balancer configuration, Amazon ECS starts a new deployment with the updated Elastic Load Balancing configuration. This causes tasks to register to and deregister from load balancers.

We recommend that you verify this on a test environment before you update the Elastic Load Balancing configuration.

A service-linked role is required for services that use multiple target groups. For more information, see [Using service-linked roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html) in the *Amazon Elastic Container Service Developer Guide* .

targetGroupArn -> (string)

The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service or task set.

A target group ARN is only specified when using an Application Load Balancer or Network Load Balancer.

For services using the `ECS` deployment controller, you can specify one or multiple target groups. For more information, see [Registering multiple target groups with a service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/register-multiple-targetgroups.html) in the *Amazon Elastic Container Service Developer Guide* .

For services using the `CODE_DEPLOY` deployment controller, youâre required to define two target groups for the load balancer. For more information, see [Blue/green deployment with CodeDeploy](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html) in the *Amazon Elastic Container Service Developer Guide* .

### Warning

If your serviceâs task definition uses the `awsvpc` network mode, you must choose `ip` as the target type, not `instance` . Do this when creating your target groups because tasks that use the `awsvpc` network mode are associated with an elastic network interface, not an Amazon EC2 instance. This network mode is required for the Fargate launch type.

loadBalancerName -> (string)

The name of the load balancer to associate with the Amazon ECS service or task set.

If you are using an Application Load Balancer or a Network Load Balancer the load balancer name parameter should be omitted.

containerName -> (string)

The name of the container (as it appears in a container definition) to associate with the load balancer.

You need to specify the container name when configuring the target group for an Amazon ECS load balancer.

containerPort -> (integer)

The port on the container to associate with the load balancer. This port must correspond to a `containerPort` in the task definition the tasks in the service are using. For tasks that use the EC2 launch type, the container instance theyâre launched on must allow ingress traffic on the `hostPort` of the port mapping.

Shorthand Syntax:

```
targetGroupArn=string,loadBalancerName=string,containerName=string,containerPort=integer ...
```

JSON Syntax:

```
[
  {
    "targetGroupArn": "string",
    "loadBalancerName": "string",
    "containerName": "string",
    "containerPort": integer
  }
  ...
]
```

`--service-registries` (list)

The details of the service discovery registry to associate with this service. For more information, see [Service discovery](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html) .

### Note

Each service may be associated with one service registry. Multiple service registries for each service isnât supported.

(structure)

The details for the service registry.

Each service may be associated with one service registry. Multiple service registries for each service are not supported.

When you add, update, or remove the service registries configuration, Amazon ECS starts a new deployment. New tasks are registered and deregistered to the updated service registry configuration.

registryArn -> (string)

The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is Cloud Map. For more information, see [CreateService](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html) .

port -> (integer)

The port value used if your service discovery service specified an SRV record. This field might be used if both the `awsvpc` network mode and SRV records are used.

containerName -> (string)

The container name value to be used for your service discovery service. Itâs already specified in the task definition. If the task definition that your service task specifies uses the `bridge` or `host` network mode, you must specify a `containerName` and `containerPort` combination from the task definition. If the task definition that your service task specifies uses the `awsvpc` network mode and a type SRV DNS record is used, you must specify either a `containerName` and `containerPort` combination or a `port` value. However, you canât specify both.

containerPort -> (integer)

The port value to be used for your service discovery service. Itâs already specified in the task definition. If the task definition your service task specifies uses the `bridge` or `host` network mode, you must specify a `containerName` and `containerPort` combination from the task definition. If the task definition your service task specifies uses the `awsvpc` network mode and a type SRV DNS record is used, you must specify either a `containerName` and `containerPort` combination or a `port` value. However, you canât specify both.

Shorthand Syntax:

```
registryArn=string,port=integer,containerName=string,containerPort=integer ...
```

JSON Syntax:

```
[
  {
    "registryArn": "string",
    "port": integer,
    "containerName": "string",
    "containerPort": integer
  }
  ...
]
```

`--desired-count` (integer)

The number of instantiations of the specified task definition to place and keep running in your service.

This is required if `schedulingStrategy` is `REPLICA` or isnât specified. If `schedulingStrategy` is `DAEMON` then this isnât required.

`--client-token` (string)

An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 36 ASCII characters in the range of 33-126 (inclusive) are allowed.

`--launch-type` (string)

The infrastructure that you run your service on. For more information, see [Amazon ECS launch types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html) in the *Amazon Elastic Container Service Developer Guide* .

The `FARGATE` launch type runs your tasks on Fargate On-Demand infrastructure.

### Note

Fargate Spot infrastructure is available for use but a capacity provider strategy must be used. For more information, see [Fargate capacity providers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-capacity-providers.html) in the *Amazon ECS Developer Guide* .

The `EC2` launch type runs your tasks on Amazon EC2 instances registered to your cluster.

The `EXTERNAL` launch type runs your tasks on your on-premises server or virtual machine (VM) capacity registered to your cluster.

A service can use either a launch type or a capacity provider strategy. If a `launchType` is specified, the `capacityProviderStrategy` parameter must be omitted.

Possible values:

- `EC2`
- `FARGATE`
- `EXTERNAL`

`--capacity-provider-strategy` (list)

The capacity provider strategy to use for the service.

If a `capacityProviderStrategy` is specified, the `launchType` parameter must be omitted. If no `capacityProviderStrategy` or `launchType` is specified, the `defaultCapacityProviderStrategy` for the cluster is used.

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

`--platform-version` (string)

The platform version that your tasks in the service are running on. A platform version is specified only for tasks using the Fargate launch type. If one isnât specified, the `LATEST` platform version is used. For more information, see [Fargate platform versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide* .

`--role` (string)

The name or full Amazon Resource Name (ARN) of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is only permitted if you are using a load balancer with your service and your task definition doesnât use the `awsvpc` network mode. If you specify the `role` parameter, you must also specify a load balancer object with the `loadBalancers` parameter.

### Warning

If your account has already created the Amazon ECS service-linked role, that role is used for your service unless you specify a role here. The service-linked role is required if your task definition uses the `awsvpc` network mode or if the service is configured to use service discovery, an external deployment controller, multiple target groups, or Elastic Inference accelerators in which case you donât specify a role here. For more information, see [Using service-linked roles for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html) in the *Amazon Elastic Container Service Developer Guide* .

If your specified role has a path other than `/` , then you must either specify the full role ARN (this is recommended) or prefix the role name with the path. For example, if a role with the name `bar` has a path of `/foo/` then you would specify `/foo/bar` as the role name. For more information, see [Friendly names and paths](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names) in the *IAM User Guide* .

`--deployment-configuration` (structure)

Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.

deploymentCircuitBreaker -> (structure)

### Note

The deployment circuit breaker can only be used for services using the rolling update (`ECS` ) deployment type.

The **deployment circuit breaker** determines whether a service deployment will fail if the service canât reach a steady state. If you use the deployment circuit breaker, a service deployment will transition to a failed state and stop launching new tasks. If you use the rollback option, when a service deployment fails, the service is rolled back to the last deployment that completed successfully. For more information, see [Rolling update](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html) in the *Amazon Elastic Container Service Developer Guide*

enable -> (boolean)

Determines whether to use the deployment circuit breaker logic for the service.

rollback -> (boolean)

Determines whether to configure Amazon ECS to roll back the service if a service deployment fails. If rollback is on, when a service deployment fails, the service is rolled back to the last deployment that completed successfully.

maximumPercent -> (integer)

If a service is using the rolling update (`ECS` ) deployment type, the `maximumPercent` parameter represents an upper limit on the number of your serviceâs tasks that are allowed in the `RUNNING` or `PENDING` state during a deployment, as a percentage of the `desiredCount` (rounded down to the nearest integer). This parameter enables you to define the deployment batch size. For example, if your service is using the `REPLICA` service scheduler and has a `desiredCount` of four tasks and a `maximumPercent` value of 200%, the scheduler may start four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). The default `maximumPercent` value for a service using the `REPLICA` service scheduler is 200%.

The Amazon ECS scheduler uses this parameter to replace unhealthy tasks by starting replacement tasks first and then stopping the unhealthy tasks, as long as cluster resources for starting replacement tasks are available. For more information about how the scheduler replaces unhealthy tasks, see [Amazon ECS services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html) .

If a service is using either the blue/green (`CODE_DEPLOY` ) or `EXTERNAL` deployment types, and tasks in the service use the EC2 launch type, the **maximum percent** value is set to the default value. The **maximum percent** value is used to define the upper limit on the number of the tasks in the service that remain in the `RUNNING` state while the container instances are in the `DRAINING` state.

### Note

You canât specify a custom `maximumPercent` value for a service that uses either the blue/green (`CODE_DEPLOY` ) or `EXTERNAL` deployment types and has tasks that use the EC2 launch type.

If the service uses either the blue/green (`CODE_DEPLOY` ) or `EXTERNAL` deployment types, and the tasks in the service use the Fargate launch type, the maximum percent value is not used. The value is still returned when describing your service.

minimumHealthyPercent -> (integer)

If a service is using the rolling update (`ECS` ) deployment type, the `minimumHealthyPercent` represents a lower limit on the number of your serviceâs tasks that must remain in the `RUNNING` state during a deployment, as a percentage of the `desiredCount` (rounded up to the nearest integer). This parameter enables you to deploy without using additional cluster capacity. For example, if your service has a `desiredCount` of four tasks and a `minimumHealthyPercent` of 50%, the service scheduler may stop two existing tasks to free up cluster capacity before starting two new tasks.

If any tasks are unhealthy and if `maximumPercent` doesnât allow the Amazon ECS scheduler to start replacement tasks, the scheduler stops the unhealthy tasks one-by-one â using the `minimumHealthyPercent` as a constraint â to clear up capacity to launch replacement tasks. For more information about how the scheduler replaces unhealthy tasks, see [Amazon ECS services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html) .

For services that *do not* use a load balancer, the following should be noted:

- A service is considered healthy if all essential containers within the tasks in the service pass their health checks.
- If a task has no essential containers with a health check defined, the service scheduler will wait for 40 seconds after a task reaches a `RUNNING` state before the task is counted towards the minimum healthy percent total.
- If a task has one or more essential containers with a health check defined, the service scheduler will wait for the task to reach a healthy status before counting it towards the minimum healthy percent total. A task is considered healthy when all essential containers within the task have passed their health checks. The amount of time the service scheduler can wait for is determined by the container health check settings.

For services that *do* use a load balancer, the following should be noted:

- If a task has no essential containers with a health check defined, the service scheduler will wait for the load balancer target group health check to return a healthy status before counting the task towards the minimum healthy percent total.
- If a task has an essential container with a health check defined, the service scheduler will wait for both the task to reach a healthy status and the load balancer target group health check to return a healthy status before counting the task towards the minimum healthy percent total.

The default value for a replica service for `minimumHealthyPercent` is 100%. The default `minimumHealthyPercent` value for a service using the `DAEMON` service schedule is 0% for the CLI, the Amazon Web Services SDKs, and the APIs and 50% for the Amazon Web Services Management Console.

The minimum number of healthy tasks during a deployment is the `desiredCount` multiplied by the `minimumHealthyPercent` /100, rounded up to the nearest integer value.

If a service is using either the blue/green (`CODE_DEPLOY` ) or `EXTERNAL` deployment types and is running tasks that use the EC2 launch type, the **minimum healthy percent** value is set to the default value. The **minimum healthy percent** value is used to define the lower limit on the number of the tasks in the service that remain in the `RUNNING` state while the container instances are in the `DRAINING` state.

### Note

You canât specify a custom `minimumHealthyPercent` value for a service that uses either the blue/green (`CODE_DEPLOY` ) or `EXTERNAL` deployment types and has tasks that use the EC2 launch type.

If a service is using either the blue/green (`CODE_DEPLOY` ) or `EXTERNAL` deployment types and is running tasks that use the Fargate launch type, the minimum healthy percent value is not used, although it is returned when describing your service.

alarms -> (structure)

Information about the CloudWatch alarms.

alarmNames -> (list)

One or more CloudWatch alarm names. Use a â,â to separate the alarms.

(string)

rollback -> (boolean)

Determines whether to configure Amazon ECS to roll back the service if a service deployment fails. If rollback is used, when a service deployment fails, the service is rolled back to the last deployment that completed successfully.

enable -> (boolean)

Determines whether to use the CloudWatch alarm option in the service deployment process.

Shorthand Syntax:

```
deploymentCircuitBreaker={enable=boolean,rollback=boolean},maximumPercent=integer,minimumHealthyPercent=integer,alarms={alarmNames=[string,string],rollback=boolean,enable=boolean}
```

JSON Syntax:

```
{
  "deploymentCircuitBreaker": {
    "enable": true|false,
    "rollback": true|false
  },
  "maximumPercent": integer,
  "minimumHealthyPercent": integer,
  "alarms": {
    "alarmNames": ["string", ...],
    "rollback": true|false,
    "enable": true|false
  }
}
```

`--placement-constraints` (list)

An array of placement constraint objects to use for tasks in your service. You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime.

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

The placement strategy objects to use for tasks in your service. You can specify a maximum of 5 strategy rules for each service.

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

`--network-configuration` (structure)

The network configuration for the service. This parameter is required for task definitions that use the `awsvpc` network mode to receive their own elastic network interface, and it isnât supported for other network modes. For more information, see [Task networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide* .

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

`--health-check-grace-period-seconds` (integer)

The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started. If you donât specify a health check grace period value, the default value of `0` is used. If you donât use any of the health checks, then `healthCheckGracePeriodSeconds` is unused.

If your serviceâs tasks take a while to start and respond to health checks, you can specify a health check grace period of up to 2,147,483,647 seconds (about 69 years). During that time, the Amazon ECS service scheduler ignores health check status. This grace period can prevent the service scheduler from marking tasks as unhealthy and stopping them before they have time to come up.

`--scheduling-strategy` (string)

The scheduling strategy to use for the service. For more information, see [Services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html) .

There are two service scheduler strategies available:

- `REPLICA` -The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. This scheduler strategy is required if the service uses the `CODE_DEPLOY` or `EXTERNAL` deployment controller types.
- `DAEMON` -The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks and will stop tasks that donât meet the placement constraints. When youâre using this strategy, you donât need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies.

### Note

Tasks using the Fargate launch type or the `CODE_DEPLOY` or `EXTERNAL` deployment controller types donât support the `DAEMON` scheduling strategy.

Possible values:

- `REPLICA`
- `DAEMON`

`--deployment-controller` (structure)

The deployment controller to use for the service. If no deployment controller is specified, the default value of `ECS` is used.

type -> (string)

The deployment controller type to use.

There are three deployment controller types available:

ECS

The rolling update (`ECS` ) deployment type involves replacing the current running version of the container with the latest version. The number of containers Amazon ECS adds or removes from the service during a rolling update is controlled by adjusting the minimum and maximum number of healthy tasks allowed during a service deployment, as specified in the [DeploymentConfiguration](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeploymentConfiguration.html) .

For more information about rolling deployments, see [Deploy Amazon ECS services by replacing tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html) in the *Amazon Elastic Container Service Developer Guide* .

CODE_DEPLOY

The blue/green (`CODE_DEPLOY` ) deployment type uses the blue/green deployment model powered by CodeDeploy, which allows you to verify a new deployment of a service before sending production traffic to it.

For more information about blue/green deployments, see [Validate the state of an Amazon ECS service before deployment](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html) in the *Amazon Elastic Container Service Developer Guide* .

EXTERNAL

The external (`EXTERNAL` ) deployment type enables you to use any third-party deployment controller for full control over the deployment process for an Amazon ECS service.

For more information about external deployments, see [Deploy Amazon ECS services using a third-party controller](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-external.html) in the *Amazon Elastic Container Service Developer Guide* .

Shorthand Syntax:

```
type=string
```

JSON Syntax:

```
{
  "type": "ECS"|"CODE_DEPLOY"|"EXTERNAL"
}
```

`--tags` (list)

The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. When a service is deleted, the tags are deleted as well.

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

`--enable-ecs-managed-tags` | `--no-enable-ecs-managed-tags` (boolean)

Specifies whether to turn on Amazon ECS managed tags for the tasks within the service. For more information, see [Tagging your Amazon ECS resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html) in the *Amazon Elastic Container Service Developer Guide* .

When you use Amazon ECS managed tags, you need to set the `propagateTags` request parameter.

`--propagate-tags` (string)

Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags arenât propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the [TagResource](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html) API action.

You must set this to a value other than `NONE` when you use Cost Explorer. For more information, see [Amazon ECS usage reports](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/usage-reports.html) in the *Amazon Elastic Container Service Developer Guide* .

The default is `NONE` .

Possible values:

- `TASK_DEFINITION`
- `SERVICE`
- `NONE`

`--enable-execute-command` | `--disable-execute-command` (boolean)

Determines whether the execute command functionality is turned on for the service. If `true` , this enables execute command functionality on all containers in the service tasks.

`--service-connect-configuration` (structure)

The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.

Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide* .

enabled -> (boolean)

Specifies whether to use Service Connect with this service.

namespace -> (string)

The namespace name or full Amazon Resource Name (ARN) of the Cloud Map namespace for use with Service Connect. The namespace must be in the same Amazon Web Services Region as the Amazon ECS service and cluster. The type of namespace doesnât affect Service Connect. For more information about Cloud Map, see [Working with Services](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-services.html) in the *Cloud Map Developer Guide* .

services -> (list)

The list of Service Connect service objects. These are names and aliases (also known as endpoints) that are used by other Amazon ECS services to connect to this service.

This field is not required for a âclientâ Amazon ECS service thatâs a member of a namespace only to connect to other services within the namespace. An example of this would be a frontend application that accepts incoming requests from either a load balancer thatâs attached to the service or by other means.

An object selects a port from the task definition, assigns a name for the Cloud Map service, and a list of aliases (endpoints) and ports for client applications to refer to this service.

(structure)

The Service Connect service object configuration. For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide* .

portName -> (string)

The `portName` must match the name of one of the `portMappings` from all the containers in the task definition of this Amazon ECS service.

discoveryName -> (string)

The `discoveryName` is the name of the new Cloud Map service that Amazon ECS creates for this Amazon ECS service. This must be unique within the Cloud Map namespace. The name can contain up to 64 characters. The name can include lowercase letters, numbers, underscores (_), and hyphens (-). The name canât start with a hyphen.

If the `discoveryName` isnât specified, the port mapping name from the task definition is used in `portName.namespace` .

clientAliases -> (list)

The list of client aliases for this Service Connect service. You use these to assign names that can be used by client applications. The maximum number of client aliases that you can have in this list is 1.

Each alias (âendpointâ) is a fully-qualified name and port number that other Amazon ECS tasks (âclientsâ) can use to connect to this service.

Each name and port mapping must be unique within the namespace.

For each `ServiceConnectService` , you must provide at least one `clientAlias` with one `port` .

(structure)

Each alias (âendpointâ) is a fully-qualified name and port number that other tasks (âclientsâ) can use to connect to this service.

Each name and port mapping must be unique within the namespace.

Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide* .

port -> (integer)

The listening port number for the Service Connect proxy. This port is available inside of all of the tasks within the same namespace.

To avoid changing your applications in client Amazon ECS services, set this to the same port that the client application uses by default. For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide* .

dnsName -> (string)

The `dnsName` is the name that you use in the applications of client tasks to connect to this service. The name must be a valid DNS name but doesnât need to be fully-qualified. The name can include up to 127 characters. The name can include lowercase letters, numbers, underscores (_), hyphens (-), and periods (.). The name canât start with a hyphen.

If this parameter isnât specified, the default value of `discoveryName.namespace` is used. If the `discoveryName` isnât specified, the port mapping name from the task definition is used in `portName.namespace` .

To avoid changing your applications in client Amazon ECS services, set this to the same name that the client application uses by default. For example, a few common names are `database` , `db` , or the lowercase name of a database, such as `mysql` or `redis` . For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide* .

ingressPortOverride -> (integer)

The port number for the Service Connect proxy to listen on.

Use the value of this field to bypass the proxy for traffic on the port number specified in the named `portMapping` in the task definition of this application, and then use it in your VPC security groups to allow traffic into the proxy for this Amazon ECS service.

In `awsvpc` mode and Fargate, the default value is the container port number. The container port number is in the `portMapping` in the task definition. In bridge mode, the default value is the ephemeral port of the Service Connect proxy.

timeout -> (structure)

A reference to an object that represents the configured timeouts for Service Connect.

idleTimeoutSeconds -> (integer)

The amount of time in seconds a connection will stay active while idle. A value of `0` can be set to disable `idleTimeout` .

The `idleTimeout` default for `HTTP` /`HTTP2` /`GRPC` is 5 minutes.

The `idleTimeout` default for `TCP` is 1 hour.

perRequestTimeoutSeconds -> (integer)

The amount of time waiting for the upstream to respond with a complete response per request. A value of `0` can be set to disable `perRequestTimeout` . `perRequestTimeout` can only be set if Service Connect `appProtocol` isnât `TCP` . Only `idleTimeout` is allowed for `TCP` `appProtocol` .

tls -> (structure)

A reference to an object that represents a Transport Layer Security (TLS) configuration.

issuerCertificateAuthority -> (structure)

The signer certificate authority.

awsPcaAuthorityArn -> (string)

The ARN of the Amazon Web Services Private Certificate Authority certificate.

kmsKey -> (string)

The Amazon Web Services Key Management Service key.

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role thatâs associated with the Service Connect TLS.

logConfiguration -> (structure)

The log configuration for the container. This parameter maps to `LogConfig` in the docker container create command and the `--log-driver` option to docker run.

By default, containers use the same logging driver that the Docker daemon uses. However, the container might use a different logging driver than the Docker daemon by specifying a log driver configuration in the container definition.

Understand the following when specifying a log configuration for your containers.

- Amazon ECS currently supports a subset of the logging drivers available to the Docker daemon. Additional log drivers may be available in future releases of the Amazon ECS container agent. For tasks on Fargate, the supported log drivers are `awslogs` , `splunk` , and `awsfirelens` . For tasks hosted on Amazon EC2 instances, the supported log drivers are `awslogs` , `fluentd` , `gelf` , `json-file` , `journald` ,``syslog`` , `splunk` , and `awsfirelens` .
- This parameter requires version 1.18 of the Docker Remote API or greater on your container instance.
- For tasks that are hosted on Amazon EC2 instances, the Amazon ECS container agent must register the available logging drivers with the `ECS_AVAILABLE_LOGGING_DRIVERS` environment variable before containers placed on that instance can use these log configuration options. For more information, see [Amazon ECS container agent configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html) in the *Amazon Elastic Container Service Developer Guide* .
- For tasks that are on Fargate, because you donât have access to the underlying infrastructure your tasks are hosted on, any additional software needed must be installed outside of the task. For example, the Fluentd output aggregators or a remote host running Logstash to send Gelf logs to.

logDriver -> (string)

The log driver to use for the container.

For tasks on Fargate, the supported log drivers are `awslogs` , `splunk` , and `awsfirelens` .

For tasks hosted on Amazon EC2 instances, the supported log drivers are `awslogs` , `fluentd` , `gelf` , `json-file` , `journald` , `syslog` , `splunk` , and `awsfirelens` .

For more information about using the `awslogs` log driver, see [Send Amazon ECS logs to CloudWatch](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html) in the *Amazon Elastic Container Service Developer Guide* .

For more information about using the `awsfirelens` log driver, see [Send Amazon ECS logs to an Amazon Web Services service or Amazon Web Services Partner](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) .

### Note

If you have a custom driver that isnât listed, you can fork the Amazon ECS container agent project thatâs [available on GitHub](https://github.com/aws/amazon-ecs-agent) and customize it to work with that driver. We encourage you to submit pull requests for changes that you would like to have included. However, we donât currently provide support for running modified copies of this software.

options -> (map)

The configuration options to send to the log driver.

The options you can specify depend on the log driver. Some of the options you can specify when you use the `awslogs` log driver to route logs to Amazon CloudWatch include the following:

awslogs-create-group

Required: No

Specify whether you want the log group to be created automatically. If this option isnât specified, it defaults to `false` .

### Note

Your IAM policy must include the `logs:CreateLogGroup` permission before you attempt to use `awslogs-create-group` .

awslogs-region

Required: Yes

Specify the Amazon Web Services Region that the `awslogs` log driver is to send your Docker logs to. You can choose to send all of your logs from clusters in different Regions to a single region in CloudWatch Logs. This is so that theyâre all visible in one location. Otherwise, you can separate them by Region for more granularity. Make sure that the specified log group exists in the Region that you specify with this option.

awslogs-group

Required: Yes

Make sure to specify a log group that the `awslogs` log driver sends its log streams to.

awslogs-stream-prefix

Required: Yes, when using Fargate.Optional when using EC2.

Use the `awslogs-stream-prefix` option to associate a log stream with the specified prefix, the container name, and the ID of the Amazon ECS task that the container belongs to. If you specify a prefix with this option, then the log stream takes the format `prefix-name/container-name/ecs-task-id` .

If you donât specify a prefix with this option, then the log stream is named after the container ID thatâs assigned by the Docker daemon on the container instance. Because itâs difficult to trace logs back to the container that sent them with just the Docker container ID (which is only available on the container instance), we recommend that you specify a prefix with this option.

For Amazon ECS services, you can use the service name as the prefix. Doing so, you can trace log streams to the service that the container belongs to, the name of the container that sent them, and the ID of the task that the container belongs to.

You must specify a stream-prefix for your logs to have your logs appear in the Log pane when using the Amazon ECS console.

awslogs-datetime-format

Required: No

This option defines a multiline start pattern in Python `strftime` format. A log message consists of a line that matches the pattern and any following lines that donât match the pattern. The matched line is the delimiter between log messages.

One example of a use case for using this format is for parsing output such as a stack dump, which might otherwise be logged in multiple entries. The correct pattern allows it to be captured in a single entry.

For more information, see [awslogs-datetime-format](https://docs.docker.com/config/containers/logging/awslogs/#awslogs-datetime-format) .

You cannot configure both the `awslogs-datetime-format` and `awslogs-multiline-pattern` options.

### Note

Multiline logging performs regular expression parsing and matching of all log messages. This might have a negative impact on logging performance.

awslogs-multiline-pattern

Required: No

This option defines a multiline start pattern that uses a regular expression. A log message consists of a line that matches the pattern and any following lines that donât match the pattern. The matched line is the delimiter between log messages.

For more information, see [awslogs-multiline-pattern](https://docs.docker.com/config/containers/logging/awslogs/#awslogs-multiline-pattern) .

This option is ignored if `awslogs-datetime-format` is also configured.

You cannot configure both the `awslogs-datetime-format` and `awslogs-multiline-pattern` options.

### Note

Multiline logging performs regular expression parsing and matching of all log messages. This might have a negative impact on logging performance.

The following options apply to all supported log drivers.

mode

Required: No

Valid values: `non-blocking` | `blocking`

This option defines the delivery mode of log messages from the container to the log driver specified using `logDriver` . The delivery mode you choose affects application availability when the flow of logs from container is interrupted.

If you use the `blocking` mode and the flow of logs is interrupted, calls from container code to write to the `stdout` and `stderr` streams will block. The logging thread of the application will block as a result. This may cause the application to become unresponsive and lead to container healthcheck failure.

If you use the `non-blocking` mode, the containerâs logs are instead stored in an in-memory intermediate buffer configured with the `max-buffer-size` option. This prevents the application from becoming unresponsive when logs cannot be sent. We recommend using this mode if you want to ensure service availability and are okay with some log loss. For more information, see Preventing log loss with non-blocking mode in the ``awslogs` container log driver <[http://aws.amazon.com/blogs/containers/preventing-log-loss-with-non-blocking-mode-in-the-awslogs-container-log-driver/](http://aws.amazon.com/blogs/containers/preventing-log-loss-with-non-blocking-mode-in-the-awslogs-container-log-driver/)>`__ .

You can set a default `mode` for all containers in a specific Amazon Web Services Region by using the `defaultLogDriverMode` account setting. If you donât specify the `mode` option or configure the account setting, Amazon ECS will default to the `blocking` mode. For more information about the account setting, see [Default log driver mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#default-log-driver-mode) in the *Amazon Elastic Container Service Developer Guide* .

max-buffer-size

Required: No

Default value: `1m`

When `non-blocking` mode is used, the `max-buffer-size` log option controls the size of the buffer thatâs used for intermediate message storage. Make sure to specify an adequate buffer size based on your application. When the buffer fills up, further logs cannot be stored. Logs that cannot be stored are lost.

To route logs using the `splunk` log router, you need to specify a `splunk-token` and a `splunk-url` .

When you use the `awsfirelens` log router to route logs to an Amazon Web Services Service or Amazon Web Services Partner Network destination for log storage and analytics, you can set the `log-driver-buffer-limit` option to limit the number of events that are buffered in memory, before being sent to the log router container. It can help to resolve potential log loss issue because high throughput might result in memory running out for the buffer inside of Docker.

Other options you can specify when using `awsfirelens` to route logs depend on the destination. When you export logs to Amazon Data Firehose, you can specify the Amazon Web Services Region with `region` and a name for the log stream with `delivery_stream` .

When you export logs to Amazon Kinesis Data Streams, you can specify an Amazon Web Services Region with `region` and a data stream name with `stream` .

When you export logs to Amazon OpenSearch Service, you can specify options like `Name` , `Host` (OpenSearch Service endpoint without protocol), `Port` , `Index` , `Type` , `Aws_auth` , `Aws_region` , `Suppress_Type_Name` , and `tls` . For more information, see [Under the hood: FireLens for Amazon ECS Tasks](http://aws.amazon.com/blogs/containers/under-the-hood-firelens-for-amazon-ecs-tasks/) .

When you export logs to Amazon S3, you can specify the bucket using the `bucket` option. You can also specify `region` , `total_file_size` , `upload_timeout` , and `use_put_object` as options.

This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version --format '{{.Server.APIVersion}}'`

key -> (string)

value -> (string)

secretOptions -> (list)

The secrets to pass to the log configuration. For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html) in the *Amazon Elastic Container Service Developer Guide* .

(structure)

An object representing the secret to expose to your container. Secrets can be exposed to a container in the following ways:

- To inject sensitive data into your containers as environment variables, use the `secrets` container definition parameter.
- To reference sensitive information in the log configuration of a container, use the `secretOptions` container definition parameter.

For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html) in the *Amazon Elastic Container Service Developer Guide* .

name -> (string)

The name of the secret.

valueFrom -> (string)

The secret to expose to the container. The supported values are either the full ARN of the Secrets Manager secret or the full ARN of the parameter in the SSM Parameter Store.

For information about the require Identity and Access Management permissions, see [Required IAM permissions for Amazon ECS secrets](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data-secrets.html#secrets-iam) (for Secrets Manager) or [Required IAM permissions for Amazon ECS secrets](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data-parameters.html) (for Systems Manager Parameter store) in the *Amazon Elastic Container Service Developer Guide* .

### Note

If the SSM Parameter Store parameter exists in the same Region as the task youâre launching, then you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.

JSON Syntax:

```
{
  "enabled": true|false,
  "namespace": "string",
  "services": [
    {
      "portName": "string",
      "discoveryName": "string",
      "clientAliases": [
        {
          "port": integer,
          "dnsName": "string"
        }
        ...
      ],
      "ingressPortOverride": integer,
      "timeout": {
        "idleTimeoutSeconds": integer,
        "perRequestTimeoutSeconds": integer
      },
      "tls": {
        "issuerCertificateAuthority": {
          "awsPcaAuthorityArn": "string"
        },
        "kmsKey": "string",
        "roleArn": "string"
      }
    }
    ...
  ],
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
  }
}
```

`--volume-configurations` (list)

The configuration for a volume specified in the task definition as a volume that is configured at launch time. Currently, the only supported volume type is an Amazon EBS volume.

(structure)

The configuration for a volume specified in the task definition as a volume that is configured at launch time. Currently, the only supported volume type is an Amazon EBS volume.

name -> (string)

The name of the volume. This value must match the volume name from the `Volume` object in the task definition.

managedEBSVolume -> (structure)

The configuration for the Amazon EBS volume that Amazon ECS creates and manages on your behalf. These settings are used to create each Amazon EBS volume, with one volume created for each task in the service. The Amazon EBS volumes are visible in your account in the Amazon EC2 console once they are created.

encrypted -> (boolean)

Indicates whether the volume should be encrypted. If you turn on Region-level Amazon EBS encryption by default but set this value as `false` , the setting is overridden and the volume is encrypted with the KMS key specified for Amazon EBS encryption by default. This parameter maps 1:1 with the `Encrypted` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference* .

kmsKeyId -> (string)

The Amazon Resource Name (ARN) identifier of the Amazon Web Services Key Management Service key to use for Amazon EBS encryption. When a key is specified using this parameter, it overrides Amazon EBS default encryption or any KMS key that you specified for cluster-level managed storage encryption. This parameter maps 1:1 with the `KmsKeyId` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference* . For more information about encrypting Amazon EBS volumes attached to tasks, see [Encrypt data stored in Amazon EBS volumes attached to Amazon ECS tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-kms-encryption.html) .

### Warning

Amazon Web Services authenticates the Amazon Web Services Key Management Service key asynchronously. Therefore, if you specify an ID, alias, or ARN that is invalid, the action can appear to complete, but eventually fails.

volumeType -> (string)

The volume type. This parameter maps 1:1 with the `VolumeType` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference* . For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) in the *Amazon EC2 User Guide* .

The following are the supported volume types.

- General Purpose SSD: `gp2` [|](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/create-service.html#id1)`gp3`
- Provisioned IOPS SSD: `io1` [|](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/create-service.html#id3)`io2`
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

The snapshot that Amazon ECS uses to create volumes for attachment to tasks maintained by the service. You must specify either `snapshotId` or `sizeInGiB` in your volume configuration. This parameter maps 1:1 with the `SnapshotId` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference* .

volumeInitializationRate -> (integer)

The rate, in MiB/s, at which data is fetched from a snapshot of an existing EBS volume to create new volumes for attachment to the tasks maintained by the service. This property can be specified only if you specify a `snapshotId` . For more information, see [Initialize Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html) in the *Amazon EBS User Guide* .

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

filesystemType -> (string)

The filesystem type for the volume. For volumes created from a snapshot, you must specify the same filesystem type that the volume was using when the snapshot was created. If there is a filesystem type mismatch, the tasks will fail to start.

The available Linux filesystem types are `ext3` , `ext4` , and `xfs` . If no value is specified, the `xfs` filesystem type is used by default.

The available Windows filesystem types are `NTFS` .

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
      "filesystemType": "ext3"|"ext4"|"xfs"|"ntfs"
    }
  }
  ...
]
```

`--vpc-lattice-configurations` (list)

The VPC Lattice configuration for the service being created.

(structure)

The VPC Lattice configuration for your service that holds the information for the target group(s) Amazon ECS tasks will be registered to.

roleArn -> (string)

The ARN of the IAM role to associate with this VPC Lattice configuration. This is the Amazon ECS infrastructure IAM role that is used to manage your VPC Lattice infrastructure.

targetGroupArn -> (string)

The full Amazon Resource Name (ARN) of the target group or groups associated with the VPC Lattice configuration that the Amazon ECS tasks will be registered to.

portName -> (string)

The name of the port mapping to register in the VPC Lattice target group. This is the name of the `portMapping` you defined in your task definition.

Shorthand Syntax:

```
roleArn=string,targetGroupArn=string,portName=string ...
```

JSON Syntax:

```
[
  {
    "roleArn": "string",
    "targetGroupArn": "string",
    "portName": "string"
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

**Example 1: To create a service with a Fargate task**

The following `create-service` example shows how to create a service using a Fargate task.

```
aws ecs create-service \
    --cluster MyCluster \
    --service-name MyService \
    --task-definition sample-fargate:1 \
    --desired-count 2 \
    --launch-type FARGATE \
    --platform-version LATEST \
    --network-configuration 'awsvpcConfiguration={subnets=[subnet-12344321],securityGroups=[sg-12344321],assignPublicIp=ENABLED}' \
    --tags key=key1,value=value1 key=key2,value=value2 key=key3,value=value3
```

Output:

```
{
    "service": {
        "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/MyCluster/MyService",
        "serviceName": "MyService",
          "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/MyCluster",
        "loadBalancers": [],
        "serviceRegistries": [],
        "status": "ACTIVE",
        "desiredCount": 2,
        "runningCount": 0,
        "pendingCount": 0,
        "launchType": "FARGATE",
        "platformVersion": "LATEST",
        "taskDefinition": "arn:aws:ecs:us-west-2:123456789012:task-definition/sample-fargate:1",
        "deploymentConfiguration": {
            "maximumPercent": 200,
            "minimumHealthyPercent": 100
        },
        "deployments": [
            {
                "id": "ecs-svc/1234567890123456789",
                "status": "PRIMARY",
                "taskDefinition": "arn:aws:ecs:us-west-2:123456789012:task-definition/sample-fargate:1",
                "desiredCount": 2,
                "pendingCount": 0,
                "runningCount": 0,
                "createdAt": 1557119253.821,
                "updatedAt": 1557119253.821,
                "launchType": "FARGATE",
                "platformVersion": "1.3.0",
                "networkConfiguration": {
                    "awsvpcConfiguration": {
                        "subnets": [
                            "subnet-12344321"
                        ],
                        "securityGroups": [
                            "sg-12344321"
                        ],
                        "assignPublicIp": "ENABLED"
                    }
                }
            }
        ],
        "roleArn": "arn:aws:iam::123456789012:role/aws-service-role/ecs.amazonaws.com/AWSServiceRoleForECS",
        "events": [],
        "createdAt": 1557119253.821,
        "placementConstraints": [],
        "placementStrategy": [],
        "networkConfiguration": {
            "awsvpcConfiguration": {
                "subnets": [
                    "subnet-12344321"
                ],
                "securityGroups": [
                    "sg-12344321"
                ],
                "assignPublicIp": "ENABLED"
            }
        },
        "schedulingStrategy": "REPLICA",
        "tags": [
            {
                "key": "key1",
                "value": "value1"
            },
            {
                "key": "key2",
                "value": "value2"
            },
            {
                "key": "key3",
                "value": "value3"
            }
        ],
        "enableECSManagedTags": false,
        "propagateTags": "NONE"
    }
}
```

For more information, see [Creating a Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-console-v2.html) in the *Amazon ECS Developer Guide*.

**Example 2: To create a service using the EC2 launch type**

The following `create-service` example shows how to create a service called `ecs-simple-service` with a task that uses the EC2 launch type. The service uses the `sleep360` task definition and it maintains 1 instantiation of the task.

```
aws ecs create-service \
    --cluster MyCluster \
    --service-name ecs-simple-service \
    --task-definition sleep360:2 \
    --desired-count 1
```

Output:

```
{
    "service": {
        "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/MyCluster/ecs-simple-service",
        "serviceName": "ecs-simple-service",
        "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/MyCluster",
        "loadBalancers": [],
        "serviceRegistries": [],
        "status": "ACTIVE",
        "desiredCount": 1,
        "runningCount": 0,
        "pendingCount": 0,
        "launchType": "EC2",
        "taskDefinition": "arn:aws:ecs:us-west-2:123456789012:task-definition/sleep360:2",
        "deploymentConfiguration": {
            "maximumPercent": 200,
            "minimumHealthyPercent": 100
        },
        "deployments": [
            {
                "id": "ecs-svc/1234567890123456789",
                "status": "PRIMARY",
                "taskDefinition": "arn:aws:ecs:us-west-2:123456789012:task-definition/sleep360:2",
                "desiredCount": 1,
                "pendingCount": 0,
                "runningCount": 0,
                "createdAt": 1557206498.798,
                "updatedAt": 1557206498.798,
                "launchType": "EC2"
            }
        ],
        "events": [],
        "createdAt": 1557206498.798,
        "placementConstraints": [],
        "placementStrategy": [],
        "schedulingStrategy": "REPLICA",
        "enableECSManagedTags": false,
        "propagateTags": "NONE"
    }
}
```

For more information, see [Creating a Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-console-v2.html) in the *Amazon ECS Developer Guide*.

**Example 3: To create a service that uses an external deployment controller**

The following `create-service` example creates a service that uses an external deployment controller.

```
aws ecs create-service \
    --cluster MyCluster \
    --service-name MyService \
    --deployment-controller type=EXTERNAL \
    --desired-count 1
```

Output:

```
{
    "service": {
        "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/MyCluster/MyService",
        "serviceName": "MyService",
        "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/MyCluster",
        "loadBalancers": [],
        "serviceRegistries": [],
        "status": "ACTIVE",
        "desiredCount": 1,
        "runningCount": 0,
        "pendingCount": 0,
        "launchType": "EC2",
        "deploymentConfiguration": {
            "maximumPercent": 200,
            "minimumHealthyPercent": 100
        },
        "taskSets": [],
        "deployments": [],
        "roleArn": "arn:aws:iam::123456789012:role/aws-service-role/ecs.amazonaws.com/AWSServiceRoleForECS",
        "events": [],
        "createdAt": 1557128207.101,
        "placementConstraints": [],
        "placementStrategy": [],
        "schedulingStrategy": "REPLICA",
        "deploymentController": {
            "type": "EXTERNAL"
        },
        "enableECSManagedTags": false,
        "propagateTags": "NONE"
    }
}
```

For more information, see [Creating a Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-console-v2.html) in the *Amazon ECS Developer Guide*.

**Example 4: To create a new service behind a load balancer**

The following `create-service` example shows how to create a service that is behind a load balancer. You must have a load balancer configured in the same Region as your container instance. This example uses the `--cli-input-json` option and a JSON input file called `ecs-simple-service-elb.json` with the following content.

```
aws ecs create-service \
    --cluster MyCluster \
    --service-name ecs-simple-service-elb \
    --cli-input-json file://ecs-simple-service-elb.json
```

Contents of `ecs-simple-service-elb.json`:

```
{
    "serviceName": "ecs-simple-service-elb",
    "taskDefinition": "ecs-demo",
    "loadBalancers": [
        {
            "loadBalancerName": "EC2Contai-EcsElast-123456789012",
            "containerName": "simple-demo",
            "containerPort": 80
        }
    ],
    "desiredCount": 10,
    "role": "ecsServiceRole"
}
```

Output:

```
{
    "service": {
        "status": "ACTIVE",
        "taskDefinition": "arn:aws:ecs:us-west-2:123456789012:task-definition/ecs-demo:1",
        "pendingCount": 0,
        "loadBalancers": [
            {
                "containerName": "ecs-demo",
                "containerPort": 80,
                "loadBalancerName": "EC2Contai-EcsElast-123456789012"
            }
        ],
        "roleArn": "arn:aws:iam::123456789012:role/ecsServiceRole",
        "desiredCount": 10,
        "serviceName": "ecs-simple-service-elb",
        "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/MyCluster",
        "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/ecs-simple-service-elb",
        "deployments": [
            {
                "status": "PRIMARY",
                "pendingCount": 0,
                "createdAt": 1428100239.123,
                "desiredCount": 10,
                "taskDefinition": "arn:aws:ecs:us-west-2:123456789012:task-definition/ecs-demo:1",
                "updatedAt": 1428100239.123,
                "id": "ecs-svc/1234567890123456789",
                "runningCount": 0
            }
        ],
        "events": [],
        "runningCount": 0
    }
}
```

For more information, see [Use load balancing to distribute Amazon ECS service traffic](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html) in the *Amazon ECS Developer Guide*.

**Example 5: To configure Amazon EBS volumes at service creation**

The following `create-service` example shows how to configure Amazon EBS volumes for each task managed by the service. You must have an Amazon ECS infrastructure role configured with the `AmazonECSInfrastructureRolePolicyForVolumes` managed policy attached. You must specify a task definition with the same volume name as in the `create-service` request. This example uses the `--cli-input-json` option and a JSON input file called `ecs-simple-service-ebs.json` with the following content.

```
aws ecs create-service \
    --cli-input-json file://ecs-simple-service-ebs.json
```

Contents of `ecs-simple-service-ebs.json`:

```
{
    "cluster": "mycluster",
    "taskDefinition": "mytaskdef",
    "serviceName": "ecs-simple-service-ebs",
    "desiredCount": 2,
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
            "name": "myEbsVolume",
            "managedEBSVolume": {
                "roleArn":"arn:aws:iam::123456789012:role/ecsInfrastructureRole",
                "volumeType": "gp3",
                "sizeInGiB": 100,
                "iops": 3000,
                "throughput": 125,
                "filesystemType": "ext4"
            }
        }
   ]
}
```

Output:

```
{
    "service": {
        "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/mycluster/ecs-simple-service-ebs",
        "serviceName": "ecs-simple-service-ebs",
        "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/mycluster",
        "loadBalancers": [],
        "serviceRegistries": [],
        "status": "ACTIVE",
        "desiredCount": 2,
        "runningCount": 0,
        "pendingCount": 0,
        "launchType": "EC2",
        "taskDefinition": "arn:aws:ecs:us-west-2:123456789012:task-definition/mytaskdef:3",
        "deploymentConfiguration": {
            "deploymentCircuitBreaker": {
                "enable": false,
                "rollback": false
            },
            "maximumPercent": 200,
            "minimumHealthyPercent": 100
        },
        "deployments": [
            {
                "id": "ecs-svc/7851020056849183687",
                "status": "PRIMARY",
                "taskDefinition": "arn:aws:ecs:us-west-2:123456789012:task-definition/mytaskdef:3",
                "desiredCount": 0,
                "pendingCount": 0,
                "runningCount": 0,
                "failedTasks": 0,
                "createdAt": "2025-01-21T11:32:38.034000-06:00",
                "updatedAt": "2025-01-21T11:32:38.034000-06:00",
                "launchType": "EC2",
                "networkConfiguration": {
                    "awsvpcConfiguration": {
                        "subnets": [
                            "subnet-12344321"
                        ],
                        "securityGroups": [
                            "sg-12344321"
                        ],
                        "assignPublicIp": "DISABLED"
                    }
                },
                "rolloutState": "IN_PROGRESS",
                "rolloutStateReason": "ECS deployment ecs-svc/7851020056849183687 in progress.",
                "volumeConfigurations": [
                    {
                        "name": "myEBSVolume",
                        "managedEBSVolume": {
                            "volumeType": "gp3",
                            "sizeInGiB": 100,
                            "iops": 3000,
                            "throughput": 125,
                            "roleArn": "arn:aws:iam::123456789012:role/ecsInfrastructureRole",
                            "filesystemType": "ext4"
                        }
                    }
                ]
            }
        ],
        "roleArn": "arn:aws:iam::123456789012:role/aws-service-role/ecs.amazonaws.com/AWSServiceRoleForECS",
        "events": [],
        "createdAt": "2025-01-21T11:32:38.034000-06:00",
        "placementConstraints": [],
        "placementStrategy": [],
        "networkConfiguration": {
            "awsvpcConfiguration": {
                "subnets": [
                    "subnet-12344321"
                ],
                "securityGroups": [
                    "sg-12344321"
                ],
                "assignPublicIp": "DISABLED"
            }
        },
        "healthCheckGracePeriodSeconds": 0,
        "schedulingStrategy": "REPLICA",
        "deploymentController": {
            "type": "ECS"
        },
        "createdBy": "arn:aws:iam::123456789012:user/AIDACKCEVSQ6C2EXAMPLE",
        "enableECSManagedTags": false,
        "propagateTags": "NONE",
        "enableExecuteCommand": false,
        "availabilityZoneRebalancing": "DISABLED"
    }
}
```

For more information, see [Use Amazon EBS volumes with Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html) in the *Amazon ECS Developer Guide*.

## Output

service -> (structure)

The full description of your service following the create call.

A service will return either a `capacityProviderStrategy` or `launchType` parameter, but not both, depending where one was specified when it was created.

If a service is using the `ECS` deployment controller, the `deploymentController` and `taskSets` parameters will not be returned.

if the service uses the `CODE_DEPLOY` deployment controller, the `deploymentController` , `taskSets` and `deployments` parameters will be returned, however the `deployments` parameter will be an empty list.

serviceArn -> (string)

The ARN that identifies the service. For more information about the ARN format, see [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids) in the *Amazon ECS Developer Guide* .

serviceName -> (string)

The name of your service. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. Service names must be unique within a cluster. However, you can have similarly named services in multiple clusters within a Region or across multiple Regions.

clusterArn -> (string)

The Amazon Resource Name (ARN) of the cluster that hosts the service.

loadBalancers -> (list)

A list of Elastic Load Balancing load balancer objects. It contains the load balancer name, the container name, and the container port to access from the load balancer. The container name is as it appears in a container definition.

(structure)

The load balancer configuration to use with a service or task set.

When you add, update, or remove a load balancer configuration, Amazon ECS starts a new deployment with the updated Elastic Load Balancing configuration. This causes tasks to register to and deregister from load balancers.

We recommend that you verify this on a test environment before you update the Elastic Load Balancing configuration.

A service-linked role is required for services that use multiple target groups. For more information, see [Using service-linked roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html) in the *Amazon Elastic Container Service Developer Guide* .

targetGroupArn -> (string)

The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service or task set.

A target group ARN is only specified when using an Application Load Balancer or Network Load Balancer.

For services using the `ECS` deployment controller, you can specify one or multiple target groups. For more information, see [Registering multiple target groups with a service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/register-multiple-targetgroups.html) in the *Amazon Elastic Container Service Developer Guide* .

For services using the `CODE_DEPLOY` deployment controller, youâre required to define two target groups for the load balancer. For more information, see [Blue/green deployment with CodeDeploy](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html) in the *Amazon Elastic Container Service Developer Guide* .

### Warning

If your serviceâs task definition uses the `awsvpc` network mode, you must choose `ip` as the target type, not `instance` . Do this when creating your target groups because tasks that use the `awsvpc` network mode are associated with an elastic network interface, not an Amazon EC2 instance. This network mode is required for the Fargate launch type.

loadBalancerName -> (string)

The name of the load balancer to associate with the Amazon ECS service or task set.

If you are using an Application Load Balancer or a Network Load Balancer the load balancer name parameter should be omitted.

containerName -> (string)

The name of the container (as it appears in a container definition) to associate with the load balancer.

You need to specify the container name when configuring the target group for an Amazon ECS load balancer.

containerPort -> (integer)

The port on the container to associate with the load balancer. This port must correspond to a `containerPort` in the task definition the tasks in the service are using. For tasks that use the EC2 launch type, the container instance theyâre launched on must allow ingress traffic on the `hostPort` of the port mapping.

serviceRegistries -> (list)

The details for the service discovery registries to assign to this service. For more information, see [Service Discovery](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html) .

(structure)

The details for the service registry.

Each service may be associated with one service registry. Multiple service registries for each service are not supported.

When you add, update, or remove the service registries configuration, Amazon ECS starts a new deployment. New tasks are registered and deregistered to the updated service registry configuration.

registryArn -> (string)

The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is Cloud Map. For more information, see [CreateService](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html) .

port -> (integer)

The port value used if your service discovery service specified an SRV record. This field might be used if both the `awsvpc` network mode and SRV records are used.

containerName -> (string)

The container name value to be used for your service discovery service. Itâs already specified in the task definition. If the task definition that your service task specifies uses the `bridge` or `host` network mode, you must specify a `containerName` and `containerPort` combination from the task definition. If the task definition that your service task specifies uses the `awsvpc` network mode and a type SRV DNS record is used, you must specify either a `containerName` and `containerPort` combination or a `port` value. However, you canât specify both.

containerPort -> (integer)

The port value to be used for your service discovery service. Itâs already specified in the task definition. If the task definition your service task specifies uses the `bridge` or `host` network mode, you must specify a `containerName` and `containerPort` combination from the task definition. If the task definition your service task specifies uses the `awsvpc` network mode and a type SRV DNS record is used, you must specify either a `containerName` and `containerPort` combination or a `port` value. However, you canât specify both.

status -> (string)

The status of the service. The valid values are `ACTIVE` , `DRAINING` , or `INACTIVE` .

desiredCount -> (integer)

The desired number of instantiations of the task definition to keep running on the service. This value is specified when the service is created with [CreateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html) , and it can be modified with [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) .

runningCount -> (integer)

The number of tasks in the cluster that are in the `RUNNING` state.

pendingCount -> (integer)

The number of tasks in the cluster that are in the `PENDING` state.

launchType -> (string)

The launch type the service is using. When using the DescribeServices API, this field is omitted if the service was created using a capacity provider strategy.

capacityProviderStrategy -> (list)

The capacity provider strategy the service uses. When using the DescribeServices API, this field is omitted if the service was created using a launch type.

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

platformVersion -> (string)

The platform version to run your service on. A platform version is only specified for tasks that are hosted on Fargate. If one isnât specified, the `LATEST` platform version is used. For more information, see [Fargate Platform Versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide* .

platformFamily -> (string)

The operating system that your tasks in the service run on. A platform family is specified only for tasks using the Fargate launch type.

All tasks that run as part of this service must use the same `platformFamily` value as the service (for example, `LINUX` ).

taskDefinition -> (string)

The task definition to use for tasks in the service. This value is specified when the service is created with [CreateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html) , and it can be modified with [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) .

deploymentConfiguration -> (structure)

Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.

deploymentCircuitBreaker -> (structure)

### Note

The deployment circuit breaker can only be used for services using the rolling update (`ECS` ) deployment type.

The **deployment circuit breaker** determines whether a service deployment will fail if the service canât reach a steady state. If you use the deployment circuit breaker, a service deployment will transition to a failed state and stop launching new tasks. If you use the rollback option, when a service deployment fails, the service is rolled back to the last deployment that completed successfully. For more information, see [Rolling update](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html) in the *Amazon Elastic Container Service Developer Guide*

enable -> (boolean)

Determines whether to use the deployment circuit breaker logic for the service.

rollback -> (boolean)

Determines whether to configure Amazon ECS to roll back the service if a service deployment fails. If rollback is on, when a service deployment fails, the service is rolled back to the last deployment that completed successfully.

maximumPercent -> (integer)

If a service is using the rolling update (`ECS` ) deployment type, the `maximumPercent` parameter represents an upper limit on the number of your serviceâs tasks that are allowed in the `RUNNING` or `PENDING` state during a deployment, as a percentage of the `desiredCount` (rounded down to the nearest integer). This parameter enables you to define the deployment batch size. For example, if your service is using the `REPLICA` service scheduler and has a `desiredCount` of four tasks and a `maximumPercent` value of 200%, the scheduler may start four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). The default `maximumPercent` value for a service using the `REPLICA` service scheduler is 200%.

The Amazon ECS scheduler uses this parameter to replace unhealthy tasks by starting replacement tasks first and then stopping the unhealthy tasks, as long as cluster resources for starting replacement tasks are available. For more information about how the scheduler replaces unhealthy tasks, see [Amazon ECS services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html) .

If a service is using either the blue/green (`CODE_DEPLOY` ) or `EXTERNAL` deployment types, and tasks in the service use the EC2 launch type, the **maximum percent** value is set to the default value. The **maximum percent** value is used to define the upper limit on the number of the tasks in the service that remain in the `RUNNING` state while the container instances are in the `DRAINING` state.

### Note

You canât specify a custom `maximumPercent` value for a service that uses either the blue/green (`CODE_DEPLOY` ) or `EXTERNAL` deployment types and has tasks that use the EC2 launch type.

If the service uses either the blue/green (`CODE_DEPLOY` ) or `EXTERNAL` deployment types, and the tasks in the service use the Fargate launch type, the maximum percent value is not used. The value is still returned when describing your service.

minimumHealthyPercent -> (integer)

If a service is using the rolling update (`ECS` ) deployment type, the `minimumHealthyPercent` represents a lower limit on the number of your serviceâs tasks that must remain in the `RUNNING` state during a deployment, as a percentage of the `desiredCount` (rounded up to the nearest integer). This parameter enables you to deploy without using additional cluster capacity. For example, if your service has a `desiredCount` of four tasks and a `minimumHealthyPercent` of 50%, the service scheduler may stop two existing tasks to free up cluster capacity before starting two new tasks.

If any tasks are unhealthy and if `maximumPercent` doesnât allow the Amazon ECS scheduler to start replacement tasks, the scheduler stops the unhealthy tasks one-by-one â using the `minimumHealthyPercent` as a constraint â to clear up capacity to launch replacement tasks. For more information about how the scheduler replaces unhealthy tasks, see [Amazon ECS services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html) .

For services that *do not* use a load balancer, the following should be noted:

- A service is considered healthy if all essential containers within the tasks in the service pass their health checks.
- If a task has no essential containers with a health check defined, the service scheduler will wait for 40 seconds after a task reaches a `RUNNING` state before the task is counted towards the minimum healthy percent total.
- If a task has one or more essential containers with a health check defined, the service scheduler will wait for the task to reach a healthy status before counting it towards the minimum healthy percent total. A task is considered healthy when all essential containers within the task have passed their health checks. The amount of time the service scheduler can wait for is determined by the container health check settings.

For services that *do* use a load balancer, the following should be noted:

- If a task has no essential containers with a health check defined, the service scheduler will wait for the load balancer target group health check to return a healthy status before counting the task towards the minimum healthy percent total.
- If a task has an essential container with a health check defined, the service scheduler will wait for both the task to reach a healthy status and the load balancer target group health check to return a healthy status before counting the task towards the minimum healthy percent total.

The default value for a replica service for `minimumHealthyPercent` is 100%. The default `minimumHealthyPercent` value for a service using the `DAEMON` service schedule is 0% for the CLI, the Amazon Web Services SDKs, and the APIs and 50% for the Amazon Web Services Management Console.

The minimum number of healthy tasks during a deployment is the `desiredCount` multiplied by the `minimumHealthyPercent` /100, rounded up to the nearest integer value.

If a service is using either the blue/green (`CODE_DEPLOY` ) or `EXTERNAL` deployment types and is running tasks that use the EC2 launch type, the **minimum healthy percent** value is set to the default value. The **minimum healthy percent** value is used to define the lower limit on the number of the tasks in the service that remain in the `RUNNING` state while the container instances are in the `DRAINING` state.

### Note

You canât specify a custom `minimumHealthyPercent` value for a service that uses either the blue/green (`CODE_DEPLOY` ) or `EXTERNAL` deployment types and has tasks that use the EC2 launch type.

If a service is using either the blue/green (`CODE_DEPLOY` ) or `EXTERNAL` deployment types and is running tasks that use the Fargate launch type, the minimum healthy percent value is not used, although it is returned when describing your service.

alarms -> (structure)

Information about the CloudWatch alarms.

alarmNames -> (list)

One or more CloudWatch alarm names. Use a â,â to separate the alarms.

(string)

rollback -> (boolean)

Determines whether to configure Amazon ECS to roll back the service if a service deployment fails. If rollback is used, when a service deployment fails, the service is rolled back to the last deployment that completed successfully.

enable -> (boolean)

Determines whether to use the CloudWatch alarm option in the service deployment process.

taskSets -> (list)

Information about a set of Amazon ECS tasks in either an CodeDeploy or an `EXTERNAL` deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.

(structure)

Information about a set of Amazon ECS tasks in either an CodeDeploy or an `EXTERNAL` deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.

id -> (string)

The ID of the task set.

taskSetArn -> (string)

The Amazon Resource Name (ARN) of the task set.

serviceArn -> (string)

The Amazon Resource Name (ARN) of the service the task set exists in.

clusterArn -> (string)

The Amazon Resource Name (ARN) of the cluster that the service that hosts the task set exists in.

startedBy -> (string)

The tag specified when a task set is started. If an CodeDeploy deployment created the task set, the `startedBy` parameter is `CODE_DEPLOY` . If an external deployment created the task set, the `startedBy` field isnât used.

externalId -> (string)

The external ID associated with the task set.

If an CodeDeploy deployment created a task set, the `externalId` parameter contains the CodeDeploy deployment ID.

If a task set is created for an external deployment and is associated with a service discovery registry, the `externalId` parameter contains the `ECS_TASK_SET_EXTERNAL_ID` Cloud Map attribute.

status -> (string)

The status of the task set. The following describes each state.

PRIMARY

The task set is serving production traffic.

ACTIVE

The task set isnât serving production traffic.

DRAINING

The tasks in the task set are being stopped, and their corresponding targets are being deregistered from their target group.

taskDefinition -> (string)

The task definition that the task set is using.

computedDesiredCount -> (integer)

The computed desired count for the task set. This is calculated by multiplying the serviceâs `desiredCount` by the task setâs `scale` percentage. The result is always rounded up. For example, if the computed desired count is 1.2, it rounds up to 2 tasks.

pendingCount -> (integer)

The number of tasks in the task set that are in the `PENDING` status during a deployment. A task in the `PENDING` state is preparing to enter the `RUNNING` state. A task set enters the `PENDING` status when it launches for the first time or when itâs restarted after being in the `STOPPED` state.

runningCount -> (integer)

The number of tasks in the task set that are in the `RUNNING` status during a deployment. A task in the `RUNNING` state is running and ready for use.

createdAt -> (timestamp)

The Unix timestamp for the time when the task set was created.

updatedAt -> (timestamp)

The Unix timestamp for the time when the task set was last updated.

launchType -> (string)

The launch type the tasks in the task set are using. For more information, see [Amazon ECS launch types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html) in the *Amazon Elastic Container Service Developer Guide* .

capacityProviderStrategy -> (list)

The capacity provider strategy that are associated with the task set.

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

platformVersion -> (string)

The Fargate platform version where the tasks in the task set are running. A platform version is only specified for tasks run on Fargate. For more information, see [Fargate platform versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide* .

platformFamily -> (string)

The operating system that your tasks in the set are running on. A platform family is specified only for tasks that use the Fargate launch type.

All tasks in the set must have the same value.

networkConfiguration -> (structure)

The network configuration for the task set.

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

loadBalancers -> (list)

Details on a load balancer that are used with a task set.

(structure)

The load balancer configuration to use with a service or task set.

When you add, update, or remove a load balancer configuration, Amazon ECS starts a new deployment with the updated Elastic Load Balancing configuration. This causes tasks to register to and deregister from load balancers.

We recommend that you verify this on a test environment before you update the Elastic Load Balancing configuration.

A service-linked role is required for services that use multiple target groups. For more information, see [Using service-linked roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html) in the *Amazon Elastic Container Service Developer Guide* .

targetGroupArn -> (string)

The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service or task set.

A target group ARN is only specified when using an Application Load Balancer or Network Load Balancer.

For services using the `ECS` deployment controller, you can specify one or multiple target groups. For more information, see [Registering multiple target groups with a service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/register-multiple-targetgroups.html) in the *Amazon Elastic Container Service Developer Guide* .

For services using the `CODE_DEPLOY` deployment controller, youâre required to define two target groups for the load balancer. For more information, see [Blue/green deployment with CodeDeploy](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html) in the *Amazon Elastic Container Service Developer Guide* .

### Warning

If your serviceâs task definition uses the `awsvpc` network mode, you must choose `ip` as the target type, not `instance` . Do this when creating your target groups because tasks that use the `awsvpc` network mode are associated with an elastic network interface, not an Amazon EC2 instance. This network mode is required for the Fargate launch type.

loadBalancerName -> (string)

The name of the load balancer to associate with the Amazon ECS service or task set.

If you are using an Application Load Balancer or a Network Load Balancer the load balancer name parameter should be omitted.

containerName -> (string)

The name of the container (as it appears in a container definition) to associate with the load balancer.

You need to specify the container name when configuring the target group for an Amazon ECS load balancer.

containerPort -> (integer)

The port on the container to associate with the load balancer. This port must correspond to a `containerPort` in the task definition the tasks in the service are using. For tasks that use the EC2 launch type, the container instance theyâre launched on must allow ingress traffic on the `hostPort` of the port mapping.

serviceRegistries -> (list)

The details for the service discovery registries to assign to this task set. For more information, see [Service discovery](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html) .

(structure)

The details for the service registry.

Each service may be associated with one service registry. Multiple service registries for each service are not supported.

When you add, update, or remove the service registries configuration, Amazon ECS starts a new deployment. New tasks are registered and deregistered to the updated service registry configuration.

registryArn -> (string)

The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is Cloud Map. For more information, see [CreateService](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html) .

port -> (integer)

The port value used if your service discovery service specified an SRV record. This field might be used if both the `awsvpc` network mode and SRV records are used.

containerName -> (string)

The container name value to be used for your service discovery service. Itâs already specified in the task definition. If the task definition that your service task specifies uses the `bridge` or `host` network mode, you must specify a `containerName` and `containerPort` combination from the task definition. If the task definition that your service task specifies uses the `awsvpc` network mode and a type SRV DNS record is used, you must specify either a `containerName` and `containerPort` combination or a `port` value. However, you canât specify both.

containerPort -> (integer)

The port value to be used for your service discovery service. Itâs already specified in the task definition. If the task definition your service task specifies uses the `bridge` or `host` network mode, you must specify a `containerName` and `containerPort` combination from the task definition. If the task definition your service task specifies uses the `awsvpc` network mode and a type SRV DNS record is used, you must specify either a `containerName` and `containerPort` combination or a `port` value. However, you canât specify both.

scale -> (structure)

A floating-point percentage of your desired number of tasks to place and keep running in the task set.

value -> (double)

The value, specified as a percent total of a serviceâs `desiredCount` , to scale the task set. Accepted values are numbers between 0 and 100.

unit -> (string)

The unit of measure for the scale value.

stabilityStatus -> (string)

The stability status. This indicates whether the task set has reached a steady state. If the following conditions are met, the task set are in `STEADY_STATE` :

- The task `runningCount` is equal to the `computedDesiredCount` .
- The `pendingCount` is `0` .
- There are no tasks that are running on container instances in the `DRAINING` status.
- All tasks are reporting a healthy status from the load balancers, service discovery, and container health checks.

If any of those conditions arenât met, the stability status returns `STABILIZING` .

stabilityStatusAt -> (timestamp)

The Unix timestamp for the time when the task set stability status was retrieved.

tags -> (list)

The metadata that you apply to the task set to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.

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

fargateEphemeralStorage -> (structure)

The Fargate ephemeral storage settings for the task set.

kmsKeyId -> (string)

Specify an Key Management Service key ID to encrypt the ephemeral storage for deployment.

deployments -> (list)

The current state of deployments for the service.

(structure)

The details of an Amazon ECS service deployment. This is used only when a service uses the `ECS` deployment controller type.

id -> (string)

The ID of the deployment.

status -> (string)

The status of the deployment. The following describes each state.

PRIMARY

The most recent deployment of a service.

ACTIVE

A service deployment that still has running tasks, but are in the process of being replaced with a new `PRIMARY` deployment.

INACTIVE

A deployment that has been completely replaced.

taskDefinition -> (string)

The most recent task definition that was specified for the tasks in the service to use.

desiredCount -> (integer)

The most recent desired count of tasks that was specified for the service to deploy or maintain.

pendingCount -> (integer)

The number of tasks in the deployment that are in the `PENDING` status.

runningCount -> (integer)

The number of tasks in the deployment that are in the `RUNNING` status.

failedTasks -> (integer)

The number of consecutively failed tasks in the deployment. A task is considered a failure if the service scheduler canât launch the task, the task doesnât transition to a `RUNNING` state, or if it fails any of its defined health checks and is stopped.

### Note

Once a service deployment has one or more successfully running tasks, the failed task count resets to zero and stops being evaluated.

createdAt -> (timestamp)

The Unix timestamp for the time when the service deployment was created.

updatedAt -> (timestamp)

The Unix timestamp for the time when the service deployment was last updated.

capacityProviderStrategy -> (list)

The capacity provider strategy that the deployment is using.

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

launchType -> (string)

The launch type the tasks in the service are using. For more information, see [Amazon ECS Launch Types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html) in the *Amazon Elastic Container Service Developer Guide* .

platformVersion -> (string)

The platform version that your tasks in the service run on. A platform version is only specified for tasks using the Fargate launch type. If one isnât specified, the `LATEST` platform version is used. For more information, see [Fargate Platform Versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide* .

platformFamily -> (string)

The operating system that your tasks in the service, or tasks are running on. A platform family is specified only for tasks using the Fargate launch type.

All tasks that run as part of this service must use the same `platformFamily` value as the service, for example, `LINUX.` .

networkConfiguration -> (structure)

The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the `awsvpc` networking mode.

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

rolloutState -> (string)

### Note

The `rolloutState` of a service is only returned for services that use the rolling update (`ECS` ) deployment type that arenât behind a Classic Load Balancer.

The rollout state of the deployment. When a service deployment is started, it begins in an `IN_PROGRESS` state. When the service reaches a steady state, the deployment transitions to a `COMPLETED` state. If the service fails to reach a steady state and circuit breaker is turned on, the deployment transitions to a `FAILED` state. A deployment in `FAILED` state doesnât launch any new tasks. For more information, see [DeploymentCircuitBreaker](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeploymentCircuitBreaker.html) .

rolloutStateReason -> (string)

A description of the rollout state of a deployment.

serviceConnectConfiguration -> (structure)

The details of the Service Connect configuration thatâs used by this deployment. Compare the configuration between multiple deployments when troubleshooting issues with new deployments.

The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.

Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide* .

enabled -> (boolean)

Specifies whether to use Service Connect with this service.

namespace -> (string)

The namespace name or full Amazon Resource Name (ARN) of the Cloud Map namespace for use with Service Connect. The namespace must be in the same Amazon Web Services Region as the Amazon ECS service and cluster. The type of namespace doesnât affect Service Connect. For more information about Cloud Map, see [Working with Services](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-services.html) in the *Cloud Map Developer Guide* .

services -> (list)

The list of Service Connect service objects. These are names and aliases (also known as endpoints) that are used by other Amazon ECS services to connect to this service.

This field is not required for a âclientâ Amazon ECS service thatâs a member of a namespace only to connect to other services within the namespace. An example of this would be a frontend application that accepts incoming requests from either a load balancer thatâs attached to the service or by other means.

An object selects a port from the task definition, assigns a name for the Cloud Map service, and a list of aliases (endpoints) and ports for client applications to refer to this service.

(structure)

The Service Connect service object configuration. For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide* .

portName -> (string)

The `portName` must match the name of one of the `portMappings` from all the containers in the task definition of this Amazon ECS service.

discoveryName -> (string)

The `discoveryName` is the name of the new Cloud Map service that Amazon ECS creates for this Amazon ECS service. This must be unique within the Cloud Map namespace. The name can contain up to 64 characters. The name can include lowercase letters, numbers, underscores (_), and hyphens (-). The name canât start with a hyphen.

If the `discoveryName` isnât specified, the port mapping name from the task definition is used in `portName.namespace` .

clientAliases -> (list)

The list of client aliases for this Service Connect service. You use these to assign names that can be used by client applications. The maximum number of client aliases that you can have in this list is 1.

Each alias (âendpointâ) is a fully-qualified name and port number that other Amazon ECS tasks (âclientsâ) can use to connect to this service.

Each name and port mapping must be unique within the namespace.

For each `ServiceConnectService` , you must provide at least one `clientAlias` with one `port` .

(structure)

Each alias (âendpointâ) is a fully-qualified name and port number that other tasks (âclientsâ) can use to connect to this service.

Each name and port mapping must be unique within the namespace.

Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide* .

port -> (integer)

The listening port number for the Service Connect proxy. This port is available inside of all of the tasks within the same namespace.

To avoid changing your applications in client Amazon ECS services, set this to the same port that the client application uses by default. For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide* .

dnsName -> (string)

The `dnsName` is the name that you use in the applications of client tasks to connect to this service. The name must be a valid DNS name but doesnât need to be fully-qualified. The name can include up to 127 characters. The name can include lowercase letters, numbers, underscores (_), hyphens (-), and periods (.). The name canât start with a hyphen.

If this parameter isnât specified, the default value of `discoveryName.namespace` is used. If the `discoveryName` isnât specified, the port mapping name from the task definition is used in `portName.namespace` .

To avoid changing your applications in client Amazon ECS services, set this to the same name that the client application uses by default. For example, a few common names are `database` , `db` , or the lowercase name of a database, such as `mysql` or `redis` . For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide* .

ingressPortOverride -> (integer)

The port number for the Service Connect proxy to listen on.

Use the value of this field to bypass the proxy for traffic on the port number specified in the named `portMapping` in the task definition of this application, and then use it in your VPC security groups to allow traffic into the proxy for this Amazon ECS service.

In `awsvpc` mode and Fargate, the default value is the container port number. The container port number is in the `portMapping` in the task definition. In bridge mode, the default value is the ephemeral port of the Service Connect proxy.

timeout -> (structure)

A reference to an object that represents the configured timeouts for Service Connect.

idleTimeoutSeconds -> (integer)

The amount of time in seconds a connection will stay active while idle. A value of `0` can be set to disable `idleTimeout` .

The `idleTimeout` default for `HTTP` /`HTTP2` /`GRPC` is 5 minutes.

The `idleTimeout` default for `TCP` is 1 hour.

perRequestTimeoutSeconds -> (integer)

The amount of time waiting for the upstream to respond with a complete response per request. A value of `0` can be set to disable `perRequestTimeout` . `perRequestTimeout` can only be set if Service Connect `appProtocol` isnât `TCP` . Only `idleTimeout` is allowed for `TCP` `appProtocol` .

tls -> (structure)

A reference to an object that represents a Transport Layer Security (TLS) configuration.

issuerCertificateAuthority -> (structure)

The signer certificate authority.

awsPcaAuthorityArn -> (string)

The ARN of the Amazon Web Services Private Certificate Authority certificate.

kmsKey -> (string)

The Amazon Web Services Key Management Service key.

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role thatâs associated with the Service Connect TLS.

logConfiguration -> (structure)

The log configuration for the container. This parameter maps to `LogConfig` in the docker container create command and the `--log-driver` option to docker run.

By default, containers use the same logging driver that the Docker daemon uses. However, the container might use a different logging driver than the Docker daemon by specifying a log driver configuration in the container definition.

Understand the following when specifying a log configuration for your containers.

- Amazon ECS currently supports a subset of the logging drivers available to the Docker daemon. Additional log drivers may be available in future releases of the Amazon ECS container agent. For tasks on Fargate, the supported log drivers are `awslogs` , `splunk` , and `awsfirelens` . For tasks hosted on Amazon EC2 instances, the supported log drivers are `awslogs` , `fluentd` , `gelf` , `json-file` , `journald` ,``syslog`` , `splunk` , and `awsfirelens` .
- This parameter requires version 1.18 of the Docker Remote API or greater on your container instance.
- For tasks that are hosted on Amazon EC2 instances, the Amazon ECS container agent must register the available logging drivers with the `ECS_AVAILABLE_LOGGING_DRIVERS` environment variable before containers placed on that instance can use these log configuration options. For more information, see [Amazon ECS container agent configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html) in the *Amazon Elastic Container Service Developer Guide* .
- For tasks that are on Fargate, because you donât have access to the underlying infrastructure your tasks are hosted on, any additional software needed must be installed outside of the task. For example, the Fluentd output aggregators or a remote host running Logstash to send Gelf logs to.

logDriver -> (string)

The log driver to use for the container.

For tasks on Fargate, the supported log drivers are `awslogs` , `splunk` , and `awsfirelens` .

For tasks hosted on Amazon EC2 instances, the supported log drivers are `awslogs` , `fluentd` , `gelf` , `json-file` , `journald` , `syslog` , `splunk` , and `awsfirelens` .

For more information about using the `awslogs` log driver, see [Send Amazon ECS logs to CloudWatch](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html) in the *Amazon Elastic Container Service Developer Guide* .

For more information about using the `awsfirelens` log driver, see [Send Amazon ECS logs to an Amazon Web Services service or Amazon Web Services Partner](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) .

### Note

If you have a custom driver that isnât listed, you can fork the Amazon ECS container agent project thatâs [available on GitHub](https://github.com/aws/amazon-ecs-agent) and customize it to work with that driver. We encourage you to submit pull requests for changes that you would like to have included. However, we donât currently provide support for running modified copies of this software.

options -> (map)

The configuration options to send to the log driver.

The options you can specify depend on the log driver. Some of the options you can specify when you use the `awslogs` log driver to route logs to Amazon CloudWatch include the following:

awslogs-create-group

Required: No

Specify whether you want the log group to be created automatically. If this option isnât specified, it defaults to `false` .

### Note

Your IAM policy must include the `logs:CreateLogGroup` permission before you attempt to use `awslogs-create-group` .

awslogs-region

Required: Yes

Specify the Amazon Web Services Region that the `awslogs` log driver is to send your Docker logs to. You can choose to send all of your logs from clusters in different Regions to a single region in CloudWatch Logs. This is so that theyâre all visible in one location. Otherwise, you can separate them by Region for more granularity. Make sure that the specified log group exists in the Region that you specify with this option.

awslogs-group

Required: Yes

Make sure to specify a log group that the `awslogs` log driver sends its log streams to.

awslogs-stream-prefix

Required: Yes, when using Fargate.Optional when using EC2.

Use the `awslogs-stream-prefix` option to associate a log stream with the specified prefix, the container name, and the ID of the Amazon ECS task that the container belongs to. If you specify a prefix with this option, then the log stream takes the format `prefix-name/container-name/ecs-task-id` .

If you donât specify a prefix with this option, then the log stream is named after the container ID thatâs assigned by the Docker daemon on the container instance. Because itâs difficult to trace logs back to the container that sent them with just the Docker container ID (which is only available on the container instance), we recommend that you specify a prefix with this option.

For Amazon ECS services, you can use the service name as the prefix. Doing so, you can trace log streams to the service that the container belongs to, the name of the container that sent them, and the ID of the task that the container belongs to.

You must specify a stream-prefix for your logs to have your logs appear in the Log pane when using the Amazon ECS console.

awslogs-datetime-format

Required: No

This option defines a multiline start pattern in Python `strftime` format. A log message consists of a line that matches the pattern and any following lines that donât match the pattern. The matched line is the delimiter between log messages.

One example of a use case for using this format is for parsing output such as a stack dump, which might otherwise be logged in multiple entries. The correct pattern allows it to be captured in a single entry.

For more information, see [awslogs-datetime-format](https://docs.docker.com/config/containers/logging/awslogs/#awslogs-datetime-format) .

You cannot configure both the `awslogs-datetime-format` and `awslogs-multiline-pattern` options.

### Note

Multiline logging performs regular expression parsing and matching of all log messages. This might have a negative impact on logging performance.

awslogs-multiline-pattern

Required: No

This option defines a multiline start pattern that uses a regular expression. A log message consists of a line that matches the pattern and any following lines that donât match the pattern. The matched line is the delimiter between log messages.

For more information, see [awslogs-multiline-pattern](https://docs.docker.com/config/containers/logging/awslogs/#awslogs-multiline-pattern) .

This option is ignored if `awslogs-datetime-format` is also configured.

You cannot configure both the `awslogs-datetime-format` and `awslogs-multiline-pattern` options.

### Note

Multiline logging performs regular expression parsing and matching of all log messages. This might have a negative impact on logging performance.

The following options apply to all supported log drivers.

mode

Required: No

Valid values: `non-blocking` | `blocking`

This option defines the delivery mode of log messages from the container to the log driver specified using `logDriver` . The delivery mode you choose affects application availability when the flow of logs from container is interrupted.

If you use the `blocking` mode and the flow of logs is interrupted, calls from container code to write to the `stdout` and `stderr` streams will block. The logging thread of the application will block as a result. This may cause the application to become unresponsive and lead to container healthcheck failure.

If you use the `non-blocking` mode, the containerâs logs are instead stored in an in-memory intermediate buffer configured with the `max-buffer-size` option. This prevents the application from becoming unresponsive when logs cannot be sent. We recommend using this mode if you want to ensure service availability and are okay with some log loss. For more information, see Preventing log loss with non-blocking mode in the ``awslogs` container log driver <[http://aws.amazon.com/blogs/containers/preventing-log-loss-with-non-blocking-mode-in-the-awslogs-container-log-driver/](http://aws.amazon.com/blogs/containers/preventing-log-loss-with-non-blocking-mode-in-the-awslogs-container-log-driver/)>`__ .

You can set a default `mode` for all containers in a specific Amazon Web Services Region by using the `defaultLogDriverMode` account setting. If you donât specify the `mode` option or configure the account setting, Amazon ECS will default to the `blocking` mode. For more information about the account setting, see [Default log driver mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#default-log-driver-mode) in the *Amazon Elastic Container Service Developer Guide* .

max-buffer-size

Required: No

Default value: `1m`

When `non-blocking` mode is used, the `max-buffer-size` log option controls the size of the buffer thatâs used for intermediate message storage. Make sure to specify an adequate buffer size based on your application. When the buffer fills up, further logs cannot be stored. Logs that cannot be stored are lost.

To route logs using the `splunk` log router, you need to specify a `splunk-token` and a `splunk-url` .

When you use the `awsfirelens` log router to route logs to an Amazon Web Services Service or Amazon Web Services Partner Network destination for log storage and analytics, you can set the `log-driver-buffer-limit` option to limit the number of events that are buffered in memory, before being sent to the log router container. It can help to resolve potential log loss issue because high throughput might result in memory running out for the buffer inside of Docker.

Other options you can specify when using `awsfirelens` to route logs depend on the destination. When you export logs to Amazon Data Firehose, you can specify the Amazon Web Services Region with `region` and a name for the log stream with `delivery_stream` .

When you export logs to Amazon Kinesis Data Streams, you can specify an Amazon Web Services Region with `region` and a data stream name with `stream` .

When you export logs to Amazon OpenSearch Service, you can specify options like `Name` , `Host` (OpenSearch Service endpoint without protocol), `Port` , `Index` , `Type` , `Aws_auth` , `Aws_region` , `Suppress_Type_Name` , and `tls` . For more information, see [Under the hood: FireLens for Amazon ECS Tasks](http://aws.amazon.com/blogs/containers/under-the-hood-firelens-for-amazon-ecs-tasks/) .

When you export logs to Amazon S3, you can specify the bucket using the `bucket` option. You can also specify `region` , `total_file_size` , `upload_timeout` , and `use_put_object` as options.

This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version --format '{{.Server.APIVersion}}'`

key -> (string)

value -> (string)

secretOptions -> (list)

The secrets to pass to the log configuration. For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html) in the *Amazon Elastic Container Service Developer Guide* .

(structure)

An object representing the secret to expose to your container. Secrets can be exposed to a container in the following ways:

- To inject sensitive data into your containers as environment variables, use the `secrets` container definition parameter.
- To reference sensitive information in the log configuration of a container, use the `secretOptions` container definition parameter.

For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html) in the *Amazon Elastic Container Service Developer Guide* .

name -> (string)

The name of the secret.

valueFrom -> (string)

The secret to expose to the container. The supported values are either the full ARN of the Secrets Manager secret or the full ARN of the parameter in the SSM Parameter Store.

For information about the require Identity and Access Management permissions, see [Required IAM permissions for Amazon ECS secrets](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data-secrets.html#secrets-iam) (for Secrets Manager) or [Required IAM permissions for Amazon ECS secrets](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data-parameters.html) (for Systems Manager Parameter store) in the *Amazon Elastic Container Service Developer Guide* .

### Note

If the SSM Parameter Store parameter exists in the same Region as the task youâre launching, then you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.

serviceConnectResources -> (list)

The list of Service Connect resources that are associated with this deployment. Each list entry maps a discovery name to a Cloud Map service name.

(structure)

The Service Connect resource. Each configuration maps a discovery name to a Cloud Map service name. The data is stored in Cloud Map as part of the Service Connect configuration for each discovery name of this Amazon ECS service.

A task can resolve the `dnsName` for each of the `clientAliases` of a service. However a task canât resolve the discovery names. If you want to connect to a service, refer to the `ServiceConnectConfiguration` of that service for the list of `clientAliases` that you can use.

discoveryName -> (string)

The discovery name of this Service Connect resource.

The `discoveryName` is the name of the new Cloud Map service that Amazon ECS creates for this Amazon ECS service. This must be unique within the Cloud Map namespace. The name can contain up to 64 characters. The name can include lowercase letters, numbers, underscores (_), and hyphens (-). The name canât start with a hyphen.

If the `discoveryName` isnât specified, the port mapping name from the task definition is used in `portName.namespace` .

discoveryArn -> (string)

The Amazon Resource Name (ARN) for the namespace in Cloud Map that matches the discovery name for this Service Connect resource. You can use this ARN in other integrations with Cloud Map. However, Service Connect canât ensure connectivity outside of Amazon ECS.

volumeConfigurations -> (list)

The details of the volume that was `configuredAtLaunch` . You can configure different settings like the size, throughput, volumeType, and ecryption in [ServiceManagedEBSVolumeConfiguration](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceManagedEBSVolumeConfiguration.html) . The `name` of the volume must match the `name` from the task definition.

(structure)

The configuration for a volume specified in the task definition as a volume that is configured at launch time. Currently, the only supported volume type is an Amazon EBS volume.

name -> (string)

The name of the volume. This value must match the volume name from the `Volume` object in the task definition.

managedEBSVolume -> (structure)

The configuration for the Amazon EBS volume that Amazon ECS creates and manages on your behalf. These settings are used to create each Amazon EBS volume, with one volume created for each task in the service. The Amazon EBS volumes are visible in your account in the Amazon EC2 console once they are created.

encrypted -> (boolean)

Indicates whether the volume should be encrypted. If you turn on Region-level Amazon EBS encryption by default but set this value as `false` , the setting is overridden and the volume is encrypted with the KMS key specified for Amazon EBS encryption by default. This parameter maps 1:1 with the `Encrypted` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference* .

kmsKeyId -> (string)

The Amazon Resource Name (ARN) identifier of the Amazon Web Services Key Management Service key to use for Amazon EBS encryption. When a key is specified using this parameter, it overrides Amazon EBS default encryption or any KMS key that you specified for cluster-level managed storage encryption. This parameter maps 1:1 with the `KmsKeyId` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference* . For more information about encrypting Amazon EBS volumes attached to tasks, see [Encrypt data stored in Amazon EBS volumes attached to Amazon ECS tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-kms-encryption.html) .

### Warning

Amazon Web Services authenticates the Amazon Web Services Key Management Service key asynchronously. Therefore, if you specify an ID, alias, or ARN that is invalid, the action can appear to complete, but eventually fails.

volumeType -> (string)

The volume type. This parameter maps 1:1 with the `VolumeType` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference* . For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) in the *Amazon EC2 User Guide* .

The following are the supported volume types.

- General Purpose SSD: `gp2` [|](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/create-service.html#id5)`gp3`
- Provisioned IOPS SSD: `io1` [|](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/create-service.html#id7)`io2`
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

The snapshot that Amazon ECS uses to create volumes for attachment to tasks maintained by the service. You must specify either `snapshotId` or `sizeInGiB` in your volume configuration. This parameter maps 1:1 with the `SnapshotId` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference* .

volumeInitializationRate -> (integer)

The rate, in MiB/s, at which data is fetched from a snapshot of an existing EBS volume to create new volumes for attachment to the tasks maintained by the service. This property can be specified only if you specify a `snapshotId` . For more information, see [Initialize Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html) in the *Amazon EBS User Guide* .

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

filesystemType -> (string)

The filesystem type for the volume. For volumes created from a snapshot, you must specify the same filesystem type that the volume was using when the snapshot was created. If there is a filesystem type mismatch, the tasks will fail to start.

The available Linux filesystem types are `ext3` , `ext4` , and `xfs` . If no value is specified, the `xfs` filesystem type is used by default.

The available Windows filesystem types are `NTFS` .

fargateEphemeralStorage -> (structure)

The Fargate ephemeral storage settings for the deployment.

kmsKeyId -> (string)

Specify an Key Management Service key ID to encrypt the ephemeral storage for deployment.

vpcLatticeConfigurations -> (list)

The VPC Lattice configuration for the service deployment.

(structure)

The VPC Lattice configuration for your service that holds the information for the target group(s) Amazon ECS tasks will be registered to.

roleArn -> (string)

The ARN of the IAM role to associate with this VPC Lattice configuration. This is the Amazon ECS infrastructure IAM role that is used to manage your VPC Lattice infrastructure.

targetGroupArn -> (string)

The full Amazon Resource Name (ARN) of the target group or groups associated with the VPC Lattice configuration that the Amazon ECS tasks will be registered to.

portName -> (string)

The name of the port mapping to register in the VPC Lattice target group. This is the name of the `portMapping` you defined in your task definition.

roleArn -> (string)

The ARN of the IAM role thatâs associated with the service. It allows the Amazon ECS container agent to register container instances with an Elastic Load Balancing load balancer.

events -> (list)

The event stream for your service. A maximum of 100 of the latest events are displayed.

(structure)

The details for an event thatâs associated with a service.

id -> (string)

The ID string for the event.

createdAt -> (timestamp)

The Unix timestamp for the time when the event was triggered.

message -> (string)

The event message.

createdAt -> (timestamp)

The Unix timestamp for the time when the service was created.

placementConstraints -> (list)

The placement constraints for the tasks in the service.

(structure)

An object representing a constraint on task placement. For more information, see [Task placement constraints](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html) in the *Amazon Elastic Container Service Developer Guide* .

### Note

If youâre using the Fargate launch type, task placement constraints arenât supported.

type -> (string)

The type of constraint. Use `distinctInstance` to ensure that each task in a particular group is running on a different container instance. Use `memberOf` to restrict the selection to a group of valid candidates.

expression -> (string)

A cluster query language expression to apply to the constraint. The expression can have a maximum length of 2000 characters. You canât specify an expression if the constraint type is `distinctInstance` . For more information, see [Cluster query language](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html) in the *Amazon Elastic Container Service Developer Guide* .

placementStrategy -> (list)

The placement strategy that determines how tasks for the service are placed.

(structure)

The task placement strategy for a task or service. For more information, see [Task placement strategies](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html) in the *Amazon Elastic Container Service Developer Guide* .

type -> (string)

The type of placement strategy. The `random` placement strategy randomly places tasks on available candidates. The `spread` placement strategy spreads placement across available candidates evenly based on the `field` parameter. The `binpack` strategy places tasks on available candidates that have the least available amount of the resource thatâs specified with the `field` parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory but still enough to run the task.

field -> (string)

The field to apply the placement strategy against. For the `spread` placement strategy, valid values are `instanceId` (or `host` , which has the same effect), or any platform or custom attribute thatâs applied to a container instance, such as `attribute:ecs.availability-zone` . For the `binpack` placement strategy, valid values are `cpu` and `memory` . For the `random` placement strategy, this field is not used.

networkConfiguration -> (structure)

The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the `awsvpc` networking mode.

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

healthCheckGracePeriodSeconds -> (integer)

The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing target health checks after a task has first started.

schedulingStrategy -> (string)

The scheduling strategy to use for the service. For more information, see [Services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html) .

There are two service scheduler strategies available.

- `REPLICA` -The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions.
- `DAEMON` -The daemon scheduling strategy deploys exactly one task on each active container instance. This task meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks. It stop tasks that donât meet the placement constraints.

### Note

Fargate tasks donât support the `DAEMON` scheduling strategy.

deploymentController -> (structure)

The deployment controller type the service is using.

type -> (string)

The deployment controller type to use.

There are three deployment controller types available:

ECS

The rolling update (`ECS` ) deployment type involves replacing the current running version of the container with the latest version. The number of containers Amazon ECS adds or removes from the service during a rolling update is controlled by adjusting the minimum and maximum number of healthy tasks allowed during a service deployment, as specified in the [DeploymentConfiguration](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeploymentConfiguration.html) .

For more information about rolling deployments, see [Deploy Amazon ECS services by replacing tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html) in the *Amazon Elastic Container Service Developer Guide* .

CODE_DEPLOY

The blue/green (`CODE_DEPLOY` ) deployment type uses the blue/green deployment model powered by CodeDeploy, which allows you to verify a new deployment of a service before sending production traffic to it.

For more information about blue/green deployments, see [Validate the state of an Amazon ECS service before deployment](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html) in the *Amazon Elastic Container Service Developer Guide* .

EXTERNAL

The external (`EXTERNAL` ) deployment type enables you to use any third-party deployment controller for full control over the deployment process for an Amazon ECS service.

For more information about external deployments, see [Deploy Amazon ECS services using a third-party controller](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-external.html) in the *Amazon Elastic Container Service Developer Guide* .

tags -> (list)

The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value. You define bot the key and value.

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

createdBy -> (string)

The principal that created the service.

enableECSManagedTags -> (boolean)

Determines whether to use Amazon ECS managed tags for the tasks in the service. For more information, see [Tagging Your Amazon ECS Resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html) in the *Amazon Elastic Container Service Developer Guide* .

propagateTags -> (string)

Determines whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags arenât propagated.

enableExecuteCommand -> (boolean)

Determines whether the execute command functionality is turned on for the service. If `true` , the execute command functionality is turned on for all containers in tasks as part of the service.

availabilityZoneRebalancing -> (string)

Indicates whether to use Availability Zone rebalancing for the service.

For more information, see [Balancing an Amazon ECS service across Availability Zones](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html) in the * *Amazon Elastic Container Service Developer Guide* * .