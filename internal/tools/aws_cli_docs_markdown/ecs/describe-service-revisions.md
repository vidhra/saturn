# describe-service-revisionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-service-revisions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-service-revisions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ecs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/index.html#cli-aws-ecs) ]

# describe-service-revisions

## Description

Describes one or more service revisions.

A service revision is a version of the service that includes the values for the Amazon ECS resources (for example, task definition) and the environment resources (for example, load balancers, subnets, and security groups). For more information, see [Amazon ECS service revisions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision.html) .

You canât describe a service revision that was created before October 25, 2024.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeServiceRevisions)

## Synopsis

```
describe-service-revisions
--service-revision-arns <value>
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

`--service-revision-arns` (list)

The ARN of the service revision.

You can specify a maximum of 20 ARNs.

You can call [ListServiceDeployments](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServiceDeployments.html) to get the ARNs.

(string)

Syntax:

```
"string" "string" ...
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

**To describe service revision details**

The following `describe-service-revisions` example returns the service revision details for the service revision with the ARN `arn:aws:ecs:us-east-1:123456789012:service-revision/example-cluster/example-service/1485800978477494678`.

```
aws ecs describe-service-revisions \
    --service-revision-arns arn:aws:ecs:us-east-1:123456789012:service-revision/example-cluster/example-service/1485800978477494678
```

Output:

```
{
    "serviceRevisions": [
        {
            "serviceRevisionArn": "arn:aws:ecs:us-east-1:123456789012:service-revision/example-cluster/example-service/1485800978477494678",
            "serviceArn": "arn:aws:ecs:us-east-1:123456789012:service/example-cluster/example-service",
            "clusterArn": "arn:aws:ecs:us-east-1:123456789012:cluster/example-cluster",
            "taskDefinition": "arn:aws:ecs:us-east-1:123456789012:task-definition/webserver:5",
            "capacityProviderStrategy": [
                {
                    "capacityProvider": "FARGATE",
                    "weight": 1,
                    "base": 0
                }
            ],
            "platformVersion": "1.4.0",
            "platformFamily": "Linux",
            "networkConfiguration": {
                "awsvpcConfiguration": {
                    "subnets": [
                        "subnet-0d0eab1bb38d5ca64",
                        "subnet-0db5010045995c2d5"
                    ],
                    "securityGroups": [
                        "sg-02556bf85a191f59a"
                    ],
                    "assignPublicIp": "ENABLED"
                }
            },
            "containerImages": [
                {
                    "containerName": "aws-otel-collector",
                    "imageDigest": "sha256:7a1b3560655071bcacd66902c20ebe9a69470d5691fe3bd36baace7c2f3c4640",
                    "image": "public.ecr.aws/aws-observability/aws-otel-collector:v0.32.0"
                },
                {
                    "containerName": "web",
                    "imageDigest": "sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb",
                    "image": "nginx"
                }
            ],
            "guardDutyEnabled": false,
            "serviceConnectConfiguration": {
                "enabled": false
            },
            "createdAt": "2024-10-31T08:03:29.302000-04:00"
        }
    ],
    "failures": []
}
```

For more information, see [Amazon ECS service revisions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision.html) in the *Amazon ECS Developer Guide*.

## Output

serviceRevisions -> (list)

The list of service revisions described.

(structure)

Information about the service revision.

A service revision contains a record of the workload configuration Amazon ECS is attempting to deploy. Whenever you create or deploy a service, Amazon ECS automatically creates and captures the configuration that youâre trying to deploy in the service revision. For information about service revisions, see [Amazon ECS service revisions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision.html) in the * *Amazon Elastic Container Service Developer Guide* * .

serviceRevisionArn -> (string)

The ARN of the service revision.

serviceArn -> (string)

The ARN of the service for the service revision.

clusterArn -> (string)

The ARN of the cluster that hosts the service.

taskDefinition -> (string)

The task definition the service revision uses.

capacityProviderStrategy -> (list)

The capacity provider strategy the service revision uses.

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

The launch type the service revision uses.

platformVersion -> (string)

For the Fargate launch type, the platform version the service revision uses.

platformFamily -> (string)

The platform family the service revision uses.

loadBalancers -> (list)

The load balancers the service revision uses.

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

The service registries (for Service Discovery) the service revision uses.

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

networkConfiguration -> (structure)

The network configuration for a task or service.

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

containerImages -> (list)

The container images the service revision uses.

(structure)

The details about the container image a service revision uses.

To ensure that all tasks in a service use the same container image, Amazon ECS resolves container image names and any image tags specified in the task definition to container image digests.

After the container image digest has been established, Amazon ECS uses the digest to start any other desired tasks, and for any future service and service revision updates. This leads to all tasks in a service always running identical container images, resulting in version consistency for your software. For more information, see [Container image resolution](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html#deployment-container-image-stability) in the Amazon ECS Developer Guide.

containerName -> (string)

The name of the container.

imageDigest -> (string)

The container image digest.

image -> (string)

The container image.

guardDutyEnabled -> (boolean)

Indicates whether Runtime Monitoring is turned on.

serviceConnectConfiguration -> (structure)

The Service Connect configuration of your Amazon ECS service. The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.

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

volumeConfigurations -> (list)

The volumes that are configured at deployment that the service revision uses.

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

- General Purpose SSD: `gp2` [|](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-service-revisions.html#id1)`gp3`
- Provisioned IOPS SSD: `io1` [|](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-service-revisions.html#id3)`io2`
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

The amount of ephemeral storage to allocate for the deployment.

kmsKeyId -> (string)

Specify an Key Management Service key ID to encrypt the ephemeral storage for deployment.

createdAt -> (timestamp)

The time that the service revision was created. The format is yyyy-mm-dd HH:mm:ss.SSSSS.

vpcLatticeConfigurations -> (list)

The VPC Lattice configuration for the service revision.

(structure)

The VPC Lattice configuration for your service that holds the information for the target group(s) Amazon ECS tasks will be registered to.

roleArn -> (string)

The ARN of the IAM role to associate with this VPC Lattice configuration. This is the Amazon ECS infrastructure IAM role that is used to manage your VPC Lattice infrastructure.

targetGroupArn -> (string)

The full Amazon Resource Name (ARN) of the target group or groups associated with the VPC Lattice configuration that the Amazon ECS tasks will be registered to.

portName -> (string)

The name of the port mapping to register in the VPC Lattice target group. This is the name of the `portMapping` you defined in your task definition.

failures -> (list)

Any failures associated with the call.

(structure)

A failed resource. For a list of common causes, see [API failure reasons](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/api_failures_messages.html) in the *Amazon Elastic Container Service Developer Guide* .

arn -> (string)

The Amazon Resource Name (ARN) of the failed resource.

reason -> (string)

The reason for the failure.

detail -> (string)

The details of the failure.