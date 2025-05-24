# create-pipeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pipes/create-pipe.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pipes/create-pipe.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pipes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pipes/index.html#cli-aws-pipes) ]

# create-pipe

## Description

Create a pipe. Amazon EventBridge Pipes connect event sources to targets and reduces the need for specialized knowledge and integration code.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pipes-2015-10-07/CreatePipe)

## Synopsis

```
create-pipe
--name <value>
[--description <value>]
[--desired-state <value>]
--source <value>
[--source-parameters <value>]
[--enrichment <value>]
[--enrichment-parameters <value>]
--target <value>
[--target-parameters <value>]
--role-arn <value>
[--tags <value>]
[--log-configuration <value>]
[--kms-key-identifier <value>]
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

`--name` (string)

The name of the pipe.

`--description` (string)

A description of the pipe.

`--desired-state` (string)

The state the pipe should be in.

Possible values:

- `RUNNING`
- `STOPPED`

`--source` (string)

The ARN of the source resource.

`--source-parameters` (structure)

The parameters required to set up a source for your pipe.

FilterCriteria -> (structure)

The collection of event patterns used to filter events.

To remove a filter, specify a `FilterCriteria` object with an empty array of `Filter` objects.

For more information, see [Events and Event Patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html) in the *Amazon EventBridge User Guide* .

Filters -> (list)

The event patterns.

(structure)

Filter events using an event pattern. For more information, see [Events and Event Patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html) in the *Amazon EventBridge User Guide* .

Pattern -> (string)

The event pattern.

KinesisStreamParameters -> (structure)

The parameters for using a Kinesis stream as a source.

BatchSize -> (integer)

The maximum number of records to include in each batch.

DeadLetterConfig -> (structure)

Define the target queue to send dead-letter queue events to.

Arn -> (string)

The ARN of the specified target for the dead-letter queue.

For Amazon Kinesis stream and Amazon DynamoDB stream sources, specify either an Amazon SNS topic or Amazon SQS queue ARN.

OnPartialBatchItemFailure -> (string)

Define how to handle item process failures. `AUTOMATIC_BISECT` halves each batch and retry each half until all the records are processed or there is one failed message left in the batch.

MaximumBatchingWindowInSeconds -> (integer)

The maximum length of a time to wait for events.

MaximumRecordAgeInSeconds -> (integer)

Discard records older than the specified age. The default value is -1, which sets the maximum age to infinite. When the value is set to infinite, EventBridge never discards old records.

MaximumRetryAttempts -> (integer)

Discard records after the specified number of retries. The default value is -1, which sets the maximum number of retries to infinite. When MaximumRetryAttempts is infinite, EventBridge retries failed records until the record expires in the event source.

ParallelizationFactor -> (integer)

The number of batches to process concurrently from each shard. The default value is 1.

StartingPosition -> (string)

The position in a stream from which to start reading.

StartingPositionTimestamp -> (timestamp)

With `StartingPosition` set to `AT_TIMESTAMP` , the time from which to start reading, in Unix time seconds.

DynamoDBStreamParameters -> (structure)

The parameters for using a DynamoDB stream as a source.

BatchSize -> (integer)

The maximum number of records to include in each batch.

DeadLetterConfig -> (structure)

Define the target queue to send dead-letter queue events to.

Arn -> (string)

The ARN of the specified target for the dead-letter queue.

For Amazon Kinesis stream and Amazon DynamoDB stream sources, specify either an Amazon SNS topic or Amazon SQS queue ARN.

OnPartialBatchItemFailure -> (string)

Define how to handle item process failures. `AUTOMATIC_BISECT` halves each batch and retry each half until all the records are processed or there is one failed message left in the batch.

MaximumBatchingWindowInSeconds -> (integer)

The maximum length of a time to wait for events.

MaximumRecordAgeInSeconds -> (integer)

Discard records older than the specified age. The default value is -1, which sets the maximum age to infinite. When the value is set to infinite, EventBridge never discards old records.

MaximumRetryAttempts -> (integer)

Discard records after the specified number of retries. The default value is -1, which sets the maximum number of retries to infinite. When MaximumRetryAttempts is infinite, EventBridge retries failed records until the record expires in the event source.

ParallelizationFactor -> (integer)

The number of batches to process concurrently from each shard. The default value is 1.

StartingPosition -> (string)

The position in a stream from which to start reading.

SqsQueueParameters -> (structure)

The parameters for using a Amazon SQS stream as a source.

BatchSize -> (integer)

The maximum number of records to include in each batch.

MaximumBatchingWindowInSeconds -> (integer)

The maximum length of a time to wait for events.

ActiveMQBrokerParameters -> (structure)

The parameters for using an Active MQ broker as a source.

Credentials -> (tagged union structure)

The credentials needed to access the resource.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `BasicAuth`.

BasicAuth -> (string)

The ARN of the Secrets Manager secret.

QueueName -> (string)

The name of the destination queue to consume.

BatchSize -> (integer)

The maximum number of records to include in each batch.

MaximumBatchingWindowInSeconds -> (integer)

The maximum length of a time to wait for events.

RabbitMQBrokerParameters -> (structure)

The parameters for using a Rabbit MQ broker as a source.

Credentials -> (tagged union structure)

The credentials needed to access the resource.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `BasicAuth`.

BasicAuth -> (string)

The ARN of the Secrets Manager secret.

QueueName -> (string)

The name of the destination queue to consume.

VirtualHost -> (string)

The name of the virtual host associated with the source broker.

BatchSize -> (integer)

The maximum number of records to include in each batch.

MaximumBatchingWindowInSeconds -> (integer)

The maximum length of a time to wait for events.

ManagedStreamingKafkaParameters -> (structure)

The parameters for using an MSK stream as a source.

TopicName -> (string)

The name of the topic that the pipe will read from.

StartingPosition -> (string)

The position in a stream from which to start reading.

BatchSize -> (integer)

The maximum number of records to include in each batch.

MaximumBatchingWindowInSeconds -> (integer)

The maximum length of a time to wait for events.

ConsumerGroupID -> (string)

The name of the destination queue to consume.

Credentials -> (tagged union structure)

The credentials needed to access the resource.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `SaslScram512Auth`, `ClientCertificateTlsAuth`.

SaslScram512Auth -> (string)

The ARN of the Secrets Manager secret.

ClientCertificateTlsAuth -> (string)

The ARN of the Secrets Manager secret.

SelfManagedKafkaParameters -> (structure)

The parameters for using a self-managed Apache Kafka stream as a source.

A *self managed* cluster refers to any Apache Kafka cluster not hosted by Amazon Web Services. This includes both clusters you manage yourself, as well as those hosted by a third-party provider, such as [Confluent Cloud](https://www.confluent.io/) , [CloudKarafka](https://www.cloudkarafka.com/) , or [Redpanda](https://redpanda.com/) . For more information, see [Apache Kafka streams as a source](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-kafka.html) in the *Amazon EventBridge User Guide* .

TopicName -> (string)

The name of the topic that the pipe will read from.

StartingPosition -> (string)

The position in a stream from which to start reading.

AdditionalBootstrapServers -> (list)

An array of server URLs.

(string)

BatchSize -> (integer)

The maximum number of records to include in each batch.

MaximumBatchingWindowInSeconds -> (integer)

The maximum length of a time to wait for events.

ConsumerGroupID -> (string)

The name of the destination queue to consume.

Credentials -> (tagged union structure)

The credentials needed to access the resource.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `BasicAuth`, `SaslScram512Auth`, `SaslScram256Auth`, `ClientCertificateTlsAuth`.

BasicAuth -> (string)

The ARN of the Secrets Manager secret.

SaslScram512Auth -> (string)

The ARN of the Secrets Manager secret.

SaslScram256Auth -> (string)

The ARN of the Secrets Manager secret.

ClientCertificateTlsAuth -> (string)

The ARN of the Secrets Manager secret.

ServerRootCaCertificate -> (string)

The ARN of the Secrets Manager secret used for certification.

Vpc -> (structure)

This structure specifies the VPC subnets and security groups for the stream, and whether a public IP address is to be used.

Subnets -> (list)

Specifies the subnets associated with the stream. These subnets must all be in the same VPC. You can specify as many as 16 subnets.

(string)

SecurityGroup -> (list)

Specifies the security groups associated with the stream. These security groups must all be in the same VPC. You can specify as many as five security groups.

(string)

JSON Syntax:

```
{
  "FilterCriteria": {
    "Filters": [
      {
        "Pattern": "string"
      }
      ...
    ]
  },
  "KinesisStreamParameters": {
    "BatchSize": integer,
    "DeadLetterConfig": {
      "Arn": "string"
    },
    "OnPartialBatchItemFailure": "AUTOMATIC_BISECT",
    "MaximumBatchingWindowInSeconds": integer,
    "MaximumRecordAgeInSeconds": integer,
    "MaximumRetryAttempts": integer,
    "ParallelizationFactor": integer,
    "StartingPosition": "TRIM_HORIZON"|"LATEST"|"AT_TIMESTAMP",
    "StartingPositionTimestamp": timestamp
  },
  "DynamoDBStreamParameters": {
    "BatchSize": integer,
    "DeadLetterConfig": {
      "Arn": "string"
    },
    "OnPartialBatchItemFailure": "AUTOMATIC_BISECT",
    "MaximumBatchingWindowInSeconds": integer,
    "MaximumRecordAgeInSeconds": integer,
    "MaximumRetryAttempts": integer,
    "ParallelizationFactor": integer,
    "StartingPosition": "TRIM_HORIZON"|"LATEST"
  },
  "SqsQueueParameters": {
    "BatchSize": integer,
    "MaximumBatchingWindowInSeconds": integer
  },
  "ActiveMQBrokerParameters": {
    "Credentials": {
      "BasicAuth": "string"
    },
    "QueueName": "string",
    "BatchSize": integer,
    "MaximumBatchingWindowInSeconds": integer
  },
  "RabbitMQBrokerParameters": {
    "Credentials": {
      "BasicAuth": "string"
    },
    "QueueName": "string",
    "VirtualHost": "string",
    "BatchSize": integer,
    "MaximumBatchingWindowInSeconds": integer
  },
  "ManagedStreamingKafkaParameters": {
    "TopicName": "string",
    "StartingPosition": "TRIM_HORIZON"|"LATEST",
    "BatchSize": integer,
    "MaximumBatchingWindowInSeconds": integer,
    "ConsumerGroupID": "string",
    "Credentials": {
      "SaslScram512Auth": "string",
      "ClientCertificateTlsAuth": "string"
    }
  },
  "SelfManagedKafkaParameters": {
    "TopicName": "string",
    "StartingPosition": "TRIM_HORIZON"|"LATEST",
    "AdditionalBootstrapServers": ["string", ...],
    "BatchSize": integer,
    "MaximumBatchingWindowInSeconds": integer,
    "ConsumerGroupID": "string",
    "Credentials": {
      "BasicAuth": "string",
      "SaslScram512Auth": "string",
      "SaslScram256Auth": "string",
      "ClientCertificateTlsAuth": "string"
    },
    "ServerRootCaCertificate": "string",
    "Vpc": {
      "Subnets": ["string", ...],
      "SecurityGroup": ["string", ...]
    }
  }
}
```

`--enrichment` (string)

The ARN of the enrichment resource.

`--enrichment-parameters` (structure)

The parameters required to set up enrichment on your pipe.

InputTemplate -> (string)

Valid JSON text passed to the enrichment. In this case, nothing from the event itself is passed to the enrichment. For more information, see [The JavaScript Object Notation (JSON) Data Interchange Format](http://www.rfc-editor.org/rfc/rfc7159.txt) .

To remove an input template, specify an empty string.

HttpParameters -> (structure)

Contains the HTTP parameters to use when the target is a API Gateway REST endpoint or EventBridge ApiDestination.

If you specify an API Gateway REST API or EventBridge ApiDestination as a target, you can use this parameter to specify headers, path parameters, and query string keys/values as part of your target invoking request. If youâre using ApiDestinations, the corresponding Connection can also have these values configured. In case of any conflicting keys, values from the Connection take precedence.

PathParameterValues -> (list)

The path parameter values to be used to populate API Gateway REST API or EventBridge ApiDestination path wildcards (â*â).

(string)

HeaderParameters -> (map)

The headers that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.

key -> (string)

value -> (string)

QueryStringParameters -> (map)

The query string keys/values that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.

key -> (string)

value -> (string)

Shorthand Syntax:

```
InputTemplate=string,HttpParameters={PathParameterValues=[string,string],HeaderParameters={KeyName1=string,KeyName2=string},QueryStringParameters={KeyName1=string,KeyName2=string}}
```

JSON Syntax:

```
{
  "InputTemplate": "string",
  "HttpParameters": {
    "PathParameterValues": ["string", ...],
    "HeaderParameters": {"string": "string"
      ...},
    "QueryStringParameters": {"string": "string"
      ...}
  }
}
```

`--target` (string)

The ARN of the target resource.

`--target-parameters` (structure)

The parameters required to set up a target for your pipe.

For more information about pipe target parameters, including how to use dynamic path parameters, see [Target parameters](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html) in the *Amazon EventBridge User Guide* .

InputTemplate -> (string)

Valid JSON text passed to the target. In this case, nothing from the event itself is passed to the target. For more information, see [The JavaScript Object Notation (JSON) Data Interchange Format](http://www.rfc-editor.org/rfc/rfc7159.txt) .

To remove an input template, specify an empty string.

LambdaFunctionParameters -> (structure)

The parameters for using a Lambda function as a target.

InvocationType -> (string)

Specify whether to invoke the function synchronously or asynchronously.

- `REQUEST_RESPONSE` (default) - Invoke synchronously. This corresponds to the `RequestResponse` option in the `InvocationType` parameter for the Lambda [Invoke](https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_RequestSyntax) API.
- `FIRE_AND_FORGET` - Invoke asynchronously. This corresponds to the `Event` option in the `InvocationType` parameter for the Lambda [Invoke](https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_RequestSyntax) API.

For more information, see [Invocation types](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html#pipes-invocation) in the *Amazon EventBridge User Guide* .

StepFunctionStateMachineParameters -> (structure)

The parameters for using a Step Functions state machine as a target.

InvocationType -> (string)

Specify whether to invoke the Step Functions state machine synchronously or asynchronously.

- `REQUEST_RESPONSE` (default) - Invoke synchronously. For more information, see [StartSyncExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartSyncExecution.html) in the *Step Functions API Reference* .

### Note

`REQUEST_RESPONSE` is not supported for `STANDARD` state machine workflows.

- `FIRE_AND_FORGET` - Invoke asynchronously. For more information, see [StartExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html) in the *Step Functions API Reference* .

For more information, see [Invocation types](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html#pipes-invocation) in the *Amazon EventBridge User Guide* .

KinesisStreamParameters -> (structure)

The parameters for using a Kinesis stream as a target.

PartitionKey -> (string)

Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis Data Streams uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.

EcsTaskParameters -> (structure)

The parameters for using an Amazon ECS task as a target.

TaskDefinitionArn -> (string)

The ARN of the task definition to use if the event target is an Amazon ECS task.

TaskCount -> (integer)

The number of tasks to create based on `TaskDefinition` . The default is 1.

LaunchType -> (string)

Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The `FARGATE` value is supported only in the Regions where Fargate with Amazon ECS is supported. For more information, see [Fargate on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-Fargate.html) in the *Amazon Elastic Container Service Developer Guide* .

NetworkConfiguration -> (structure)

Use this structure if the Amazon ECS task uses the `awsvpc` network mode. This structure specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. This structure is required if `LaunchType` is `FARGATE` because the `awsvpc` mode is required for Fargate tasks.

If you specify `NetworkConfiguration` when the target ECS task does not use the `awsvpc` network mode, the task fails.

awsvpcConfiguration -> (structure)

Use this structure to specify the VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the `awsvpc` network mode.

Subnets -> (list)

Specifies the subnets associated with the task. These subnets must all be in the same VPC. You can specify as many as 16 subnets.

(string)

SecurityGroups -> (list)

Specifies the security groups associated with the task. These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.

(string)

AssignPublicIp -> (string)

Specifies whether the taskâs elastic network interface receives a public IP address. You can specify `ENABLED` only when `LaunchType` in `EcsParameters` is set to `FARGATE` .

PlatformVersion -> (string)

Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as `1.1.0` .

This structure is used only if `LaunchType` is `FARGATE` . For more information about valid platform versions, see [Fargate Platform Versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide* .

Group -> (string)

Specifies an Amazon ECS task group for the task. The maximum length is 255 characters.

CapacityProviderStrategy -> (list)

The capacity provider strategy to use for the task.

If a `capacityProviderStrategy` is specified, the `launchType` parameter must be omitted. If no `capacityProviderStrategy` or launchType is specified, the `defaultCapacityProviderStrategy` for the cluster is used.

(structure)

The details of a capacity provider strategy. To learn more, see [CapacityProviderStrategyItem](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CapacityProviderStrategyItem.html) in the Amazon ECS API Reference.

capacityProvider -> (string)

The short name of the capacity provider.

weight -> (integer)

The weight value designates the relative percentage of the total number of tasks launched that should use the specified capacity provider. The weight value is taken into consideration after the base value, if defined, is satisfied.

base -> (integer)

The base value designates how many tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined. If no value is specified, the default value of 0 is used.

EnableECSManagedTags -> (boolean)

Specifies whether to enable Amazon ECS managed tags for the task. For more information, see [Tagging Your Amazon ECS Resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html) in the Amazon Elastic Container Service Developer Guide.

EnableExecuteCommand -> (boolean)

Whether or not to enable the execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task.

PlacementConstraints -> (list)

An array of placement constraint objects to use for the task. You can specify up to 10 constraints per task (including constraints in the task definition and those specified at runtime).

(structure)

An object representing a constraint on task placement. To learn more, see [Task Placement Constraints](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html) in the Amazon Elastic Container Service Developer Guide.

type -> (string)

The type of constraint. Use distinctInstance to ensure that each task in a particular group is running on a different container instance. Use memberOf to restrict the selection to a group of valid candidates.

expression -> (string)

A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is `distinctInstance` . To learn more, see [Cluster Query Language](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html) in the Amazon Elastic Container Service Developer Guide.

PlacementStrategy -> (list)

The placement strategy objects to use for the task. You can specify a maximum of five strategy rules per task.

(structure)

The task placement strategy for a task or service. To learn more, see [Task Placement Strategies](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html) in the Amazon Elastic Container Service Service Developer Guide.

type -> (string)

The type of placement strategy. The random placement strategy randomly places tasks on available candidates. The spread placement strategy spreads placement across available candidates evenly based on the field parameter. The binpack strategy places tasks on available candidates that have the least available amount of the resource that is specified with the field parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).

field -> (string)

The field to apply the placement strategy against. For the spread placement strategy, valid values are instanceId (or host, which has the same effect), or any platform or custom attribute that is applied to a container instance, such as attribute:ecs.availability-zone. For the binpack placement strategy, valid values are cpu and memory. For the random placement strategy, this field is not used.

PropagateTags -> (string)

Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the `TagResource` API action.

ReferenceId -> (string)

The reference ID to use for the task.

Overrides -> (structure)

The overrides that are associated with a task.

ContainerOverrides -> (list)

One or more container overrides that are sent to a task.

(structure)

The overrides that are sent to a container. An empty container override can be passed in. An example of an empty container override is `{"containerOverrides": [ ] }` . If a non-empty container override is specified, the `name` parameter must be included.

Command -> (list)

The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.

(string)

Cpu -> (integer)

The number of `cpu` units reserved for the container, instead of the default value from the task definition. You must also specify a container name.

Environment -> (list)

The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.

(structure)

The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.

name -> (string)

The name of the key-value pair. For environment variables, this is the name of the environment variable.

value -> (string)

The value of the key-value pair. For environment variables, this is the value of the environment variable.

EnvironmentFiles -> (list)

A list of files containing the environment variables to pass to a container, instead of the value from the container definition.

(structure)

A list of files containing the environment variables to pass to a container. You can specify up to ten environment files. The file must have a `.env` file extension. Each line in an environment file should contain an environment variable in `VARIABLE=VALUE` format. Lines beginning with `#` are treated as comments and are ignored. For more information about the environment variable file syntax, see [Declare default environment variables in file](https://docs.docker.com/compose/env-file/) .

If there are environment variables specified using the `environment` parameter in a container definition, they take precedence over the variables contained within an environment file. If multiple environment files are specified that contain the same variable, theyâre processed from the top down. We recommend that you use unique variable names. For more information, see [Specifying environment variables](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/taskdef-envfiles.html) in the *Amazon Elastic Container Service Developer Guide* .

This parameter is only supported for tasks hosted on Fargate using the following platform versions:

- Linux platform version `1.4.0` or later.
- Windows platform version `1.0.0` or later.

type -> (string)

The file type to use. The only supported value is `s3` .

value -> (string)

The Amazon Resource Name (ARN) of the Amazon S3 object containing the environment variable file.

Memory -> (integer)

The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.

MemoryReservation -> (integer)

The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.

Name -> (string)

The name of the container that receives the override. This parameter is required if any override is specified.

ResourceRequirements -> (list)

The type and amount of a resource to assign to a container, instead of the default value from the task definition. The only supported resource is a GPU.

(structure)

The type and amount of a resource to assign to a container. The supported resource types are GPUs and Elastic Inference accelerators. For more information, see [Working with GPUs on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html) or [Working with Amazon Elastic Inference on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-inference.html) in the *Amazon Elastic Container Service Developer Guide*

type -> (string)

The type of resource to assign to a container. The supported values are `GPU` or `InferenceAccelerator` .

value -> (string)

The value for the specified resource type.

If the `GPU` type is used, the value is the number of physical `GPUs` the Amazon ECS container agent reserves for the container. The number of GPUs thatâs reserved for all containers in a task canât exceed the number of available GPUs on the container instance that the task is launched on.

If the `InferenceAccelerator` type is used, the `value` matches the `deviceName` for an InferenceAccelerator specified in a task definition.

Cpu -> (string)

The cpu override for the task.

EphemeralStorage -> (structure)

The ephemeral storage setting override for the task.

### Note

This parameter is only supported for tasks hosted on Fargate that use the following platform versions:

- Linux platform version `1.4.0` or later.
- Windows platform version `1.0.0` or later.

sizeInGiB -> (integer)

The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is `21` GiB and the maximum supported value is `200` GiB.

ExecutionRoleArn -> (string)

The Amazon Resource Name (ARN) of the task execution IAM role override for the task. For more information, see [Amazon ECS task execution IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html) in the *Amazon Elastic Container Service Developer Guide* .

InferenceAcceleratorOverrides -> (list)

The Elastic Inference accelerator override for the task.

(structure)

Details on an Elastic Inference accelerator task override. This parameter is used to override the Elastic Inference accelerator specified in the task definition. For more information, see [Working with Amazon Elastic Inference on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/userguide/ecs-inference.html) in the *Amazon Elastic Container Service Developer Guide* .

deviceName -> (string)

The Elastic Inference accelerator device name to override for the task. This parameter must match a `deviceName` specified in the task definition.

deviceType -> (string)

The Elastic Inference accelerator type to use.

Memory -> (string)

The memory override for the task.

TaskRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. For more information, see [IAM Role for Tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide* .

Tags -> (list)

The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. To learn more, see [RunTask](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html#ECS-RunTask-request-tags) in the Amazon ECS API Reference.

(structure)

A key-value pair associated with an Amazon Web Services resource. In EventBridge, rules and event buses support tagging.

Key -> (string)

A string you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.

Value -> (string)

The value for the specified tag key.

BatchJobParameters -> (structure)

The parameters for using an Batch job as a target.

JobDefinition -> (string)

The job definition used by this job. This value can be one of `name` , `name:revision` , or the Amazon Resource Name (ARN) for the job definition. If name is specified without a revision then the latest active revision is used.

JobName -> (string)

The name of the job. It can be up to 128 letters long. The first character must be alphanumeric, can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).

ArrayProperties -> (structure)

The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. This parameter is used only if the target is an Batch job.

Size -> (integer)

The size of the array, if this is an array batch job.

RetryStrategy -> (structure)

The retry strategy to use for failed jobs. When a retry strategy is specified here, it overrides the retry strategy defined in the job definition.

Attempts -> (integer)

The number of times to move a job to the `RUNNABLE` status. If the value of `attempts` is greater than one, the job is retried on failure the same number of attempts as the value.

ContainerOverrides -> (structure)

The overrides that are sent to a container.

Command -> (list)

The command to send to the container that overrides the default command from the Docker image or the task definition.

(string)

Environment -> (list)

The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition.

### Note

Environment variables cannot start with â`Batch` â. This naming convention is reserved for variables that Batch sets.

(structure)

The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition.

### Note

Environment variables cannot start with â`Batch` â. This naming convention is reserved for variables that Batch sets.

Name -> (string)

The name of the key-value pair. For environment variables, this is the name of the environment variable.

Value -> (string)

The value of the key-value pair. For environment variables, this is the value of the environment variable.

InstanceType -> (string)

The instance type to use for a multi-node parallel job.

### Note

This parameter isnât applicable to single-node container jobs or jobs that run on Fargate resources, and shouldnât be provided.

ResourceRequirements -> (list)

The type and amount of resources to assign to a container. This overrides the settings in the job definition. The supported resources include `GPU` , `MEMORY` , and `VCPU` .

(structure)

The type and amount of a resource to assign to a container. The supported resources include `GPU` , `MEMORY` , and `VCPU` .

Type -> (string)

The type of resource to assign to a container. The supported resources include `GPU` , `MEMORY` , and `VCPU` .

Value -> (string)

The quantity of the specified resource to reserve for the container. The values vary based on the `type` specified.

type=âGPUâ

The number of physical GPUs to reserve for the container. Make sure that the number of GPUs reserved for all containers in a job doesnât exceed the number of available GPUs on the compute resource that the job is launched on.

### Note

GPUs arenât available for jobs that are running on Fargate resources.

type=âMEMORYâ

The memory hard limit (in MiB) present to the container. This parameter is supported for jobs that are running on EC2 resources. If your container attempts to exceed the memory specified, the container is terminated. This parameter maps to `Memory` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--memory` option to [docker run](https://docs.docker.com/engine/reference/run/) . You must specify at least 4 MiB of memory for a job. This is required but can be specified in several places for multi-node parallel (MNP) jobs. It must be specified for each node at least once. This parameter maps to `Memory` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--memory` option to [docker run](https://docs.docker.com/engine/reference/run/) .

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

`VCPU` = 1, 2, 4, or 8

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

The number of vCPUs reserved for the container. This parameter maps to `CpuShares` in the [Create a container](https://docs.docker.com/engine/api/v1.23/#create-a-container) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.23/) and the `--cpu-shares` option to [docker run](https://docs.docker.com/engine/reference/run/) . Each vCPU is equivalent to 1,024 CPU shares. For EC2 resources, you must specify at least one vCPU. This is required but can be specified in several places; it must be specified for each node at least once.

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

DependsOn -> (list)

A list of dependencies for the job. A job can depend upon a maximum of 20 jobs. You can specify a `SEQUENTIAL` type dependency without specifying a job ID for array jobs so that each child array job completes sequentially, starting at index 0. You can also specify an `N_TO_N` type dependency with a job ID for array jobs. In that case, each index child of this job must wait for the corresponding index child of each dependency to complete before it can begin.

(structure)

An object that represents an Batch job dependency.

JobId -> (string)

The job ID of the Batch job thatâs associated with this dependency.

Type -> (string)

The type of the job dependency.

Parameters -> (map)

Additional parameters passed to the job that replace parameter substitution placeholders that are set in the job definition. Parameters are specified as a key and value pair mapping. Parameters included here override any corresponding parameter defaults from the job definition.

key -> (string)

value -> (string)

SqsQueueParameters -> (structure)

The parameters for using a Amazon SQS stream as a target.

MessageGroupId -> (string)

The FIFO message group ID to use as the target.

MessageDeduplicationId -> (string)

This parameter applies only to FIFO (first-in-first-out) queues.

The token used for deduplication of sent messages.

HttpParameters -> (structure)

These are custom parameter to be used when the target is an API Gateway REST APIs or EventBridge ApiDestinations.

PathParameterValues -> (list)

The path parameter values to be used to populate API Gateway REST API or EventBridge ApiDestination path wildcards (â*â).

(string)

HeaderParameters -> (map)

The headers that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.

key -> (string)

value -> (string)

QueryStringParameters -> (map)

The query string keys/values that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.

key -> (string)

value -> (string)

RedshiftDataParameters -> (structure)

These are custom parameters to be used when the target is a Amazon Redshift cluster to invoke the Amazon Redshift Data API BatchExecuteStatement.

SecretManagerArn -> (string)

The name or ARN of the secret that enables access to the database. Required when authenticating using Secrets Manager.

Database -> (string)

The name of the database. Required when authenticating using temporary credentials.

DbUser -> (string)

The database user name. Required when authenticating using temporary credentials.

StatementName -> (string)

The name of the SQL statement. You can name the SQL statement when you create it to identify the query.

WithEvent -> (boolean)

Indicates whether to send an event back to EventBridge after the SQL statement runs.

Sqls -> (list)

The SQL statement text to run.

(string)

// A single Redshift SQL

SageMakerPipelineParameters -> (structure)

The parameters for using a SageMaker pipeline as a target.

PipelineParameterList -> (list)

List of Parameter names and values for SageMaker Model Building Pipeline execution.

(structure)

Name/Value pair of a parameter to start execution of a SageMaker Model Building Pipeline.

Name -> (string)

Name of parameter to start execution of a SageMaker Model Building Pipeline.

Value -> (string)

Value of parameter to start execution of a SageMaker Model Building Pipeline.

EventBridgeEventBusParameters -> (structure)

The parameters for using an EventBridge event bus as a target.

EndpointId -> (string)

The URL subdomain of the endpoint. For example, if the URL for Endpoint is [https://abcde.veo.endpoints.event.amazonaws.com](https://abcde.veo.endpoints.event.amazonaws.com), then the EndpointId is `abcde.veo` .

DetailType -> (string)

A free-form string, with a maximum of 128 characters, used to decide what fields to expect in the event detail.

Source -> (string)

The source of the event.

Resources -> (list)

Amazon Web Services resources, identified by Amazon Resource Name (ARN), which the event primarily concerns. Any number, including zero, may be present.

(string)

Time -> (string)

The time stamp of the event, per [RFC3339](https://www.rfc-editor.org/rfc/rfc3339.txt) . If no time stamp is provided, the time stamp of the [PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html) call is used.

CloudWatchLogsParameters -> (structure)

The parameters for using an CloudWatch Logs log stream as a target.

LogStreamName -> (string)

The name of the log stream.

Timestamp -> (string)

The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

TimestreamParameters -> (structure)

The parameters for using a Timestream for LiveAnalytics table as a target.

TimeValue -> (string)

Dynamic path to the source data field that represents the time value for your data.

EpochTimeUnit -> (string)

The granularity of the time units used. Default is `MILLISECONDS` .

Required if `TimeFieldType` is specified as `EPOCH` .

TimeFieldType -> (string)

The type of time value used.

The default is `EPOCH` .

TimestampFormat -> (string)

How to format the timestamps. For example, `yyyy-MM-dd'T'HH:mm:ss'Z'` .

Required if `TimeFieldType` is specified as `TIMESTAMP_FORMAT` .

VersionValue -> (string)

64 bit version value or source data field that represents the version value for your data.

Write requests with a higher version number will update the existing measure values of the record and version. In cases where the measure value is the same, the version will still be updated.

Default value is 1.

Timestream for LiveAnalytics does not support updating partial measure values in a record.

Write requests for duplicate data with a higher version number will update the existing measure value and version. In cases where the measure value is the same, `Version` will still be updated. Default value is `1` .

### Note

`Version` must be `1` or greater, or you will receive a `ValidationException` error.

DimensionMappings -> (list)

Map source data to dimensions in the target Timestream for LiveAnalytics table.

For more information, see [Amazon Timestream for LiveAnalytics concepts](https://docs.aws.amazon.com/timestream/latest/developerguide/concepts.html)

(structure)

Maps source data to a dimension in the target Timestream for LiveAnalytics table.

For more information, see [Amazon Timestream for LiveAnalytics concepts](https://docs.aws.amazon.com/timestream/latest/developerguide/concepts.html)

DimensionValue -> (string)

Dynamic path to the dimension value in the source event.

DimensionValueType -> (string)

The data type of the dimension for the time-series data.

DimensionName -> (string)

The metadata attributes of the time series. For example, the name and Availability Zone of an Amazon EC2 instance or the name of the manufacturer of a wind turbine are dimensions.

SingleMeasureMappings -> (list)

Mappings of single source data fields to individual records in the specified Timestream for LiveAnalytics table.

(structure)

Maps a single source data field to a single record in the specified Timestream for LiveAnalytics table.

For more information, see [Amazon Timestream for LiveAnalytics concepts](https://docs.aws.amazon.com/timestream/latest/developerguide/concepts.html)

MeasureValue -> (string)

Dynamic path of the source field to map to the measure in the record.

MeasureValueType -> (string)

Data type of the source field.

MeasureName -> (string)

Target measure name for the measurement attribute in the Timestream table.

MultiMeasureMappings -> (list)

Maps multiple measures from the source event to the same record in the specified Timestream for LiveAnalytics table.

(structure)

Maps multiple measures from the source event to the same Timestream for LiveAnalytics record.

For more information, see [Amazon Timestream for LiveAnalytics concepts](https://docs.aws.amazon.com/timestream/latest/developerguide/concepts.html)

MultiMeasureName -> (string)

The name of the multiple measurements per record (multi-measure).

MultiMeasureAttributeMappings -> (list)

Mappings that represent multiple source event fields mapped to measures in the same Timestream for LiveAnalytics record.

(structure)

A mapping of a source event data field to a measure in a Timestream for LiveAnalytics record.

MeasureValue -> (string)

Dynamic path to the measurement attribute in the source event.

MeasureValueType -> (string)

Data type of the measurement attribute in the source event.

MultiMeasureAttributeName -> (string)

Target measure name to be used.

JSON Syntax:

```
{
  "InputTemplate": "string",
  "LambdaFunctionParameters": {
    "InvocationType": "REQUEST_RESPONSE"|"FIRE_AND_FORGET"
  },
  "StepFunctionStateMachineParameters": {
    "InvocationType": "REQUEST_RESPONSE"|"FIRE_AND_FORGET"
  },
  "KinesisStreamParameters": {
    "PartitionKey": "string"
  },
  "EcsTaskParameters": {
    "TaskDefinitionArn": "string",
    "TaskCount": integer,
    "LaunchType": "EC2"|"FARGATE"|"EXTERNAL",
    "NetworkConfiguration": {
      "awsvpcConfiguration": {
        "Subnets": ["string", ...],
        "SecurityGroups": ["string", ...],
        "AssignPublicIp": "ENABLED"|"DISABLED"
      }
    },
    "PlatformVersion": "string",
    "Group": "string",
    "CapacityProviderStrategy": [
      {
        "capacityProvider": "string",
        "weight": integer,
        "base": integer
      }
      ...
    ],
    "EnableECSManagedTags": true|false,
    "EnableExecuteCommand": true|false,
    "PlacementConstraints": [
      {
        "type": "distinctInstance"|"memberOf",
        "expression": "string"
      }
      ...
    ],
    "PlacementStrategy": [
      {
        "type": "random"|"spread"|"binpack",
        "field": "string"
      }
      ...
    ],
    "PropagateTags": "TASK_DEFINITION",
    "ReferenceId": "string",
    "Overrides": {
      "ContainerOverrides": [
        {
          "Command": ["string", ...],
          "Cpu": integer,
          "Environment": [
            {
              "name": "string",
              "value": "string"
            }
            ...
          ],
          "EnvironmentFiles": [
            {
              "type": "s3",
              "value": "string"
            }
            ...
          ],
          "Memory": integer,
          "MemoryReservation": integer,
          "Name": "string",
          "ResourceRequirements": [
            {
              "type": "GPU"|"InferenceAccelerator",
              "value": "string"
            }
            ...
          ]
        }
        ...
      ],
      "Cpu": "string",
      "EphemeralStorage": {
        "sizeInGiB": integer
      },
      "ExecutionRoleArn": "string",
      "InferenceAcceleratorOverrides": [
        {
          "deviceName": "string",
          "deviceType": "string"
        }
        ...
      ],
      "Memory": "string",
      "TaskRoleArn": "string"
    },
    "Tags": [
      {
        "Key": "string",
        "Value": "string"
      }
      ...
    ]
  },
  "BatchJobParameters": {
    "JobDefinition": "string",
    "JobName": "string",
    "ArrayProperties": {
      "Size": integer
    },
    "RetryStrategy": {
      "Attempts": integer
    },
    "ContainerOverrides": {
      "Command": ["string", ...],
      "Environment": [
        {
          "Name": "string",
          "Value": "string"
        }
        ...
      ],
      "InstanceType": "string",
      "ResourceRequirements": [
        {
          "Type": "GPU"|"MEMORY"|"VCPU",
          "Value": "string"
        }
        ...
      ]
    },
    "DependsOn": [
      {
        "JobId": "string",
        "Type": "N_TO_N"|"SEQUENTIAL"
      }
      ...
    ],
    "Parameters": {"string": "string"
      ...}
  },
  "SqsQueueParameters": {
    "MessageGroupId": "string",
    "MessageDeduplicationId": "string"
  },
  "HttpParameters": {
    "PathParameterValues": ["string", ...],
    "HeaderParameters": {"string": "string"
      ...},
    "QueryStringParameters": {"string": "string"
      ...}
  },
  "RedshiftDataParameters": {
    "SecretManagerArn": "string",
    "Database": "string",
    "DbUser": "string",
    "StatementName": "string",
    "WithEvent": true|false,
    "Sqls": ["string", ...]
  },
  "SageMakerPipelineParameters": {
    "PipelineParameterList": [
      {
        "Name": "string",
        "Value": "string"
      }
      ...
    ]
  },
  "EventBridgeEventBusParameters": {
    "EndpointId": "string",
    "DetailType": "string",
    "Source": "string",
    "Resources": ["string", ...],
    "Time": "string"
  },
  "CloudWatchLogsParameters": {
    "LogStreamName": "string",
    "Timestamp": "string"
  },
  "TimestreamParameters": {
    "TimeValue": "string",
    "EpochTimeUnit": "MILLISECONDS"|"SECONDS"|"MICROSECONDS"|"NANOSECONDS",
    "TimeFieldType": "EPOCH"|"TIMESTAMP_FORMAT",
    "TimestampFormat": "string",
    "VersionValue": "string",
    "DimensionMappings": [
      {
        "DimensionValue": "string",
        "DimensionValueType": "VARCHAR",
        "DimensionName": "string"
      }
      ...
    ],
    "SingleMeasureMappings": [
      {
        "MeasureValue": "string",
        "MeasureValueType": "DOUBLE"|"BIGINT"|"VARCHAR"|"BOOLEAN"|"TIMESTAMP",
        "MeasureName": "string"
      }
      ...
    ],
    "MultiMeasureMappings": [
      {
        "MultiMeasureName": "string",
        "MultiMeasureAttributeMappings": [
          {
            "MeasureValue": "string",
            "MeasureValueType": "DOUBLE"|"BIGINT"|"VARCHAR"|"BOOLEAN"|"TIMESTAMP",
            "MultiMeasureAttributeName": "string"
          }
          ...
        ]
      }
      ...
    ]
  }
}
```

`--role-arn` (string)

The ARN of the role that allows the pipe to send data to the target.

`--tags` (map)

The list of key-value pairs to associate with the pipe.

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

`--log-configuration` (structure)

The logging configuration settings for the pipe.

S3LogDestination -> (structure)

The Amazon S3 logging configuration settings for the pipe.

BucketName -> (string)

Specifies the name of the Amazon S3 bucket to which EventBridge delivers the log records for the pipe.

BucketOwner -> (string)

Specifies the Amazon Web Services account that owns the Amazon S3 bucket to which EventBridge delivers the log records for the pipe.

OutputFormat -> (string)

How EventBridge should format the log records.

EventBridge currently only supports `json` formatting.

Prefix -> (string)

Specifies any prefix text with which to begin Amazon S3 log object names.

You can use prefixes to organize the data that you store in Amazon S3 buckets. A prefix is a string of characters at the beginning of the object key name. A prefix can be any length, subject to the maximum length of the object key name (1,024 bytes). For more information, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) in the *Amazon Simple Storage Service User Guide* .

FirehoseLogDestination -> (structure)

The Amazon Data Firehose logging configuration settings for the pipe.

DeliveryStreamArn -> (string)

Specifies the Amazon Resource Name (ARN) of the Firehose delivery stream to which EventBridge delivers the pipe log records.

CloudwatchLogsLogDestination -> (structure)

The Amazon CloudWatch Logs logging configuration settings for the pipe.

LogGroupArn -> (string)

The Amazon Web Services Resource Name (ARN) for the CloudWatch log group to which EventBridge sends the log records.

Level -> (string)

The level of logging detail to include. This applies to all log destinations for the pipe.

For more information, see [Specifying EventBridge Pipes log level](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-logs.html#eb-pipes-logs-level) in the *Amazon EventBridge User Guide* .

IncludeExecutionData -> (list)

Specify `ALL` to include the execution data (specifically, the `payload` , `awsRequest` , and `awsResponse` fields) in the log messages for this pipe.

This applies to all log destinations for the pipe.

For more information, see [Including execution data in logs](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-logs.html#eb-pipes-logs-execution-data) in the *Amazon EventBridge User Guide* .

By default, execution data is not included.

(string)

Shorthand Syntax:

```
S3LogDestination={BucketName=string,BucketOwner=string,OutputFormat=string,Prefix=string},FirehoseLogDestination={DeliveryStreamArn=string},CloudwatchLogsLogDestination={LogGroupArn=string},Level=string,IncludeExecutionData=string,string
```

JSON Syntax:

```
{
  "S3LogDestination": {
    "BucketName": "string",
    "BucketOwner": "string",
    "OutputFormat": "json"|"plain"|"w3c",
    "Prefix": "string"
  },
  "FirehoseLogDestination": {
    "DeliveryStreamArn": "string"
  },
  "CloudwatchLogsLogDestination": {
    "LogGroupArn": "string"
  },
  "Level": "OFF"|"ERROR"|"INFO"|"TRACE",
  "IncludeExecutionData": ["ALL", ...]
}
```

`--kms-key-identifier` (string)

The identifier of the KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt pipe data. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.

If you do not specify a customer managed key identifier, EventBridge uses an Amazon Web Services owned key to encrypt pipe data.

For more information, see [Managing keys](https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html) in the *Key Management Service Developer Guide* .

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

**To Create a pipe**

The following `create-pipe` example creates a Pipe named `Demo_Pipe` with SQS as the source and CloudWatch Log Group as the target for the Pipe.

```
aws pipes create-pipe \
    --name Demo_Pipe \
    --desired-state RUNNING \
    --role-arn arn:aws:iam::123456789012:role/service-role/Amazon_EventBridge_Pipe_Demo_Pipe_28b3aa4f \
    --source arn:aws:sqs:us-east-1:123456789012:Demo_Queue \
    --target arn:aws:logs:us-east-1:123456789012:log-group:/aws/pipes/Demo_LogGroup
```

Output:

```
{
    "Arn": "arn:aws:pipes:us-east-1:123456789012:pipe/Demo_Pipe",
    "Name": "Demo_Pipe",
    "DesiredState": "RUNNING",
    "CurrentState": "CREATING",
    "CreationTime": "2024-10-08T12:33:59-05:00",
    "LastModifiedTime": "2024-10-08T12:33:59.684839-05:00"
}
```

For more information, see [Amazon EventBridge Pipes concepts](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-concepts.html) in the *Amazon EventBridge User Guide*.

## Output

Arn -> (string)

The ARN of the pipe.

Name -> (string)

The name of the pipe.

DesiredState -> (string)

The state the pipe should be in.

CurrentState -> (string)

The state the pipe is in.

CreationTime -> (timestamp)

The time the pipe was created.

LastModifiedTime -> (timestamp)

When the pipe was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).