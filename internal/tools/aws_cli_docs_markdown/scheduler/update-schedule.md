# update-scheduleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/update-schedule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/update-schedule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [scheduler](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/index.html#cli-aws-scheduler) ]

# update-schedule

## Description

Updates the specified schedule. When you call `UpdateSchedule` , EventBridge Scheduler uses all values, including empty values, specified in the request and overrides the existing schedule. This is by design. This means that if you do not set an optional field in your request, that field will be set to its system-default value after the update.

Before calling this operation, we recommend that you call the `GetSchedule` API operation and make a note of all optional parameters for your `UpdateSchedule` call.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/scheduler-2021-06-30/UpdateSchedule)

## Synopsis

```
update-schedule
[--action-after-completion <value>]
[--client-token <value>]
[--description <value>]
[--end-date <value>]
--flexible-time-window <value>
[--group-name <value>]
[--kms-key-arn <value>]
--name <value>
--schedule-expression <value>
[--schedule-expression-timezone <value>]
[--start-date <value>]
[--state <value>]
--target <value>
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

`--action-after-completion` (string)

Specifies the action that EventBridge Scheduler applies to the schedule after the schedule completes invoking the target.

Possible values:

- `NONE`
- `DELETE`

`--client-token` (string)

Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency.

`--description` (string)

The description you specify for the schedule.

`--end-date` (timestamp)

The date, in UTC, before which the schedule can invoke its target. Depending on the scheduleâs recurrence expression, invocations might stop on, or before, the `EndDate` you specify. EventBridge Scheduler ignores `EndDate` for one-time schedules.

`--flexible-time-window` (structure)

Allows you to configure a time window during which EventBridge Scheduler invokes the schedule.

MaximumWindowInMinutes -> (integer)

The maximum time window during which a schedule can be invoked.

Mode -> (string)

Determines whether the schedule is invoked within a flexible time window.

Shorthand Syntax:

```
MaximumWindowInMinutes=integer,Mode=string
```

JSON Syntax:

```
{
  "MaximumWindowInMinutes": integer,
  "Mode": "OFF"|"FLEXIBLE"
}
```

`--group-name` (string)

The name of the schedule group with which the schedule is associated. You must provide this value in order for EventBridge Scheduler to find the schedule you want to update. If you omit this value, EventBridge Scheduler assumes the group is associated to the default group.

`--kms-key-arn` (string)

The ARN for the customer managed KMS key that that you want EventBridge Scheduler to use to encrypt and decrypt your data.

`--name` (string)

The name of the schedule that you are updating.

`--schedule-expression` (string)

The expression that defines when the schedule runs. The following formats are supported.

- `at` expression - `at(yyyy-mm-ddThh:mm:ss)`
- `rate` expression - `rate(value unit)`
- `cron` expression - `cron(fields)`

You can use `at` expressions to create one-time schedules that invoke a target once, at the time and in the time zone, that you specify. You can use `rate` and `cron` expressions to create recurring schedules. Rate-based schedules are useful when you want to invoke a target at regular intervals, such as every 15 minutes or every five days. Cron-based schedules are useful when you want to invoke a target periodically at a specific time, such as at 8:00 am (UTC+0) every 1st day of the month.

A `cron` expression consists of six fields separated by white spaces: `(minutes hours day_of_month month day_of_week year)` .

A `rate` expression consists of a *value* as a positive integer, and a *unit* with the following options: `minute` | `minutes` | `hour` | `hours` | `day` | `days`

For more information and examples, see [Schedule types on EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html) in the *EventBridge Scheduler User Guide* .

`--schedule-expression-timezone` (string)

The timezone in which the scheduling expression is evaluated.

`--start-date` (timestamp)

The date, in UTC, after which the schedule can begin invoking its target. Depending on the scheduleâs recurrence expression, invocations might occur on, or after, the `StartDate` you specify. EventBridge Scheduler ignores `StartDate` for one-time schedules.

`--state` (string)

Specifies whether the schedule is enabled or disabled.

Possible values:

- `ENABLED`
- `DISABLED`

`--target` (structure)

The schedule target. You can use this operation to change the target that your schedule invokes.

Arn -> (string)

The Amazon Resource Name (ARN) of the target.

DeadLetterConfig -> (structure)

An object that contains information about an Amazon SQS queue that EventBridge Scheduler uses as a dead-letter queue for your schedule. If specified, EventBridge Scheduler delivers failed events that could not be successfully delivered to a target to the queue.

Arn -> (string)

The Amazon Resource Name (ARN) of the SQS queue specified as the destination for the dead-letter queue.

EcsParameters -> (structure)

The templated target type for the Amazon ECS ` `RunTask` [https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask).html`__ API operation.

CapacityProviderStrategy -> (list)

The capacity provider strategy to use for the task.

(structure)

The details of a capacity provider strategy.

base -> (integer)

The base value designates how many tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined. If no value is specified, the default value of `0` is used.

capacityProvider -> (string)

The short name of the capacity provider.

weight -> (integer)

The weight value designates the relative percentage of the total number of tasks launched that should use the specified capacity provider. The weight value is taken into consideration after the base value, if defined, is satisfied.

EnableECSManagedTags -> (boolean)

Specifies whether to enable Amazon ECS managed tags for the task. For more information, see [Tagging Your Amazon ECS Resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html) in the *Amazon ECS Developer Guide* .

EnableExecuteCommand -> (boolean)

Whether or not to enable the execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task.

Group -> (string)

Specifies an ECS task group for the task. The maximum length is 255 characters.

LaunchType -> (string)

Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The `FARGATE` value is supported only in the Regions where Fargate with Amazon ECS is supported. For more information, see [AWS Fargate on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) in the *Amazon ECS Developer Guide* .

NetworkConfiguration -> (structure)

This structure specifies the network configuration for an ECS task.

awsvpcConfiguration -> (structure)

Specifies the Amazon VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the awsvpc network mode.

AssignPublicIp -> (string)

Specifies whether the taskâs elastic network interface receives a public IP address. You can specify `ENABLED` only when `LaunchType` in `EcsParameters` is set to `FARGATE` .

SecurityGroups -> (list)

Specifies the security groups associated with the task. These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.

(string)

Subnets -> (list)

Specifies the subnets associated with the task. These subnets must all be in the same VPC. You can specify as many as 16 subnets.

(string)

PlacementConstraints -> (list)

An array of placement constraint objects to use for the task. You can specify up to 10 constraints per task (including constraints in the task definition and those specified at runtime).

(structure)

An object representing a constraint on task placement.

expression -> (string)

A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is `distinctInstance` . For more information, see [Cluster query language](https://docs.aws.amazon.com/latest/developerguide/cluster-query-language.html) in the *Amazon ECS Developer Guide* .

type -> (string)

The type of constraint. Use `distinctInstance` to ensure that each task in a particular group is running on a different container instance. Use `memberOf` to restrict the selection to a group of valid candidates.

PlacementStrategy -> (list)

The task placement strategy for a task or service.

(structure)

The task placement strategy for a task or service.

field -> (string)

The field to apply the placement strategy against. For the spread placement strategy, valid values are `instanceId` (or `instanceId` , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as `attribute:ecs.availability-zone` . For the binpack placement strategy, valid values are `cpu` and `memory` . For the random placement strategy, this field is not used.

type -> (string)

The type of placement strategy. The random placement strategy randomly places tasks on available candidates. The spread placement strategy spreads placement across available candidates evenly based on the field parameter. The binpack strategy places tasks on available candidates that have the least available amount of the resource that is specified with the field parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).

PlatformVersion -> (string)

Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as `1.1.0` .

PropagateTags -> (string)

Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use Amazon ECSâs ` `TagResource` [https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource).html`__ API action.

ReferenceId -> (string)

The reference ID to use for the task.

Tags -> (list)

The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. For more information, see ` `RunTask` [https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask).html`__ in the *Amazon ECS API Reference* .

(map)

key -> (string)

value -> (string)

TaskCount -> (integer)

The number of tasks to create based on `TaskDefinition` . The default is `1` .

TaskDefinitionArn -> (string)

The Amazon Resource Name (ARN) of the task definition to use if the event target is an Amazon ECS task.

EventBridgeParameters -> (structure)

The templated target type for the EventBridge ` `PutEvents` [https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents).html`__ API operation.

DetailType -> (string)

A free-form string, with a maximum of 128 characters, used to decide what fields to expect in the event detail.

Source -> (string)

The source of the event.

Input -> (string)

The text, or well-formed JSON, passed to the target. If you are configuring a templated Lambda, AWS Step Functions, or Amazon EventBridge target, the input must be a well-formed JSON. For all other target types, a JSON is not required. If you do not specify anything for this field, EventBridge Scheduler delivers a default notification to the target.

KinesisParameters -> (structure)

The templated target type for the Amazon Kinesis ` `PutRecord` kinesis/latest/APIReference/API_PutRecord.html`__ API operation.

PartitionKey -> (string)

Specifies the shard to which EventBridge Scheduler sends the event. For more information, see [Amazon Kinesis Data Streams terminology and concepts](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html) in the *Amazon Kinesis Streams Developer Guide* .

RetryPolicy -> (structure)

A `RetryPolicy` object that includes information about the retry policy settings, including the maximum age of an event, and the maximum number of times EventBridge Scheduler will try to deliver the event to a target.

MaximumEventAgeInSeconds -> (integer)

The maximum amount of time, in seconds, to continue to make retry attempts.

MaximumRetryAttempts -> (integer)

The maximum number of retry attempts to make before the request fails. Retry attempts with exponential backoff continue until either the maximum number of attempts is made or until the duration of the `MaximumEventAgeInSeconds` is reached.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that EventBridge Scheduler will use for this target when the schedule is invoked.

SageMakerPipelineParameters -> (structure)

The templated target type for the Amazon SageMaker ` `StartPipelineExecution` [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartPipelineExecution](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartPipelineExecution).html`__ API operation.

PipelineParameterList -> (list)

List of parameter names and values to use when executing the SageMaker Model Building Pipeline.

(structure)

The name and value pair of a parameter to use to start execution of a SageMaker Model Building Pipeline.

Name -> (string)

Name of parameter to start execution of a SageMaker Model Building Pipeline.

Value -> (string)

Value of parameter to start execution of a SageMaker Model Building Pipeline.

SqsParameters -> (structure)

The templated target type for the Amazon SQS ` `SendMessage` [https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage).html`__ API operation. Contains the message group ID to use when the target is a FIFO queue. If you specify an Amazon SQS FIFO queue as a target, the queue must have content-based deduplication enabled. For more information, see [Using the Amazon SQS message deduplication ID](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html) in the *Amazon SQS Developer Guide* .

MessageGroupId -> (string)

The FIFO message group ID to use as the target.

JSON Syntax:

```
{
  "Arn": "string",
  "DeadLetterConfig": {
    "Arn": "string"
  },
  "EcsParameters": {
    "CapacityProviderStrategy": [
      {
        "base": integer,
        "capacityProvider": "string",
        "weight": integer
      }
      ...
    ],
    "EnableECSManagedTags": true|false,
    "EnableExecuteCommand": true|false,
    "Group": "string",
    "LaunchType": "EC2"|"FARGATE"|"EXTERNAL",
    "NetworkConfiguration": {
      "awsvpcConfiguration": {
        "AssignPublicIp": "ENABLED"|"DISABLED",
        "SecurityGroups": ["string", ...],
        "Subnets": ["string", ...]
      }
    },
    "PlacementConstraints": [
      {
        "expression": "string",
        "type": "distinctInstance"|"memberOf"
      }
      ...
    ],
    "PlacementStrategy": [
      {
        "field": "string",
        "type": "random"|"spread"|"binpack"
      }
      ...
    ],
    "PlatformVersion": "string",
    "PropagateTags": "TASK_DEFINITION",
    "ReferenceId": "string",
    "Tags": [
      {"string": "string"
        ...}
      ...
    ],
    "TaskCount": integer,
    "TaskDefinitionArn": "string"
  },
  "EventBridgeParameters": {
    "DetailType": "string",
    "Source": "string"
  },
  "Input": "string",
  "KinesisParameters": {
    "PartitionKey": "string"
  },
  "RetryPolicy": {
    "MaximumEventAgeInSeconds": integer,
    "MaximumRetryAttempts": integer
  },
  "RoleArn": "string",
  "SageMakerPipelineParameters": {
    "PipelineParameterList": [
      {
        "Name": "string",
        "Value": "string"
      }
      ...
    ]
  },
  "SqsParameters": {
    "MessageGroupId": "string"
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

## Output

ScheduleArn -> (string)

The Amazon Resource Name (ARN) of the schedule that you updated.