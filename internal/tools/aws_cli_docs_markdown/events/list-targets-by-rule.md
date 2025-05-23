# list-targets-by-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-targets-by-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-targets-by-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/index.html#cli-aws-events) ]

# list-targets-by-rule

## Description

Lists the targets assigned to the specified rule.

The maximum number of results per page for requests is 100.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eventbridge-2015-10-07/ListTargetsByRule)

`list-targets-by-rule` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Targets`

## Synopsis

```
list-targets-by-rule
--rule <value>
[--event-bus-name <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--rule` (string)

The name of the rule.

`--event-bus-name` (string)

The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To display all the targets for a CloudWatch Events rule**

This example displays all the targets of the rule named DailyLambdaFunction:

```
aws events list-targets-by-rule --rule  "DailyLambdaFunction"
```

## Output

Targets -> (list)

The targets assigned to the rule.

(structure)

Targets are the resources to be invoked when a rule is triggered. For a complete list of services and resources that can be set as a target, see [PutTargets](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutTargets.html) .

If you are setting the event bus of another account as the target, and that account granted permission to your account through an organization instead of directly by the account ID, then you must specify a `RoleArn` with proper permissions in the `Target` structure. For more information, see [Sending and Receiving Events Between Amazon Web Services Accounts](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html) in the *Amazon EventBridge User Guide* .

Id -> (string)

The ID of the target within the specified rule. Use this ID to reference the target when updating the rule. We recommend using a memorable and unique string.

Arn -> (string)

The Amazon Resource Name (ARN) of the target.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. If one rule triggers multiple targets, you can use a different IAM role for each target.

Input -> (string)

Valid JSON text passed to the target. In this case, nothing from the event itself is passed to the target. For more information, see [The JavaScript Object Notation (JSON) Data Interchange Format](http://www.rfc-editor.org/rfc/rfc7159.txt) .

InputPath -> (string)

The value of the JSONPath that is used for extracting part of the matched event when passing it to the target. You may use JSON dot notation or bracket notation. For more information about JSON paths, see [JSONPath](http://goessner.net/articles/JsonPath/) .

InputTransformer -> (structure)

Settings to enable you to provide custom input to a target based on certain event data. You can extract one or more key-value pairs from the event and then use that data to send customized input to the target.

InputPathsMap -> (map)

Map of JSON paths to be extracted from the event. You can then insert these in the template in `InputTemplate` to produce the output you want to be sent to the target.

`InputPathsMap` is an array key-value pairs, where each value is a valid JSON path. You can have as many as 100 key-value pairs. You must use JSON dot notation, not bracket notation.

The keys cannot start with âAmazon Web Services.â

key -> (string)

value -> (string)

InputTemplate -> (string)

Input template where you specify placeholders that will be filled with the values of the keys from `InputPathsMap` to customize the data sent to the target. Enclose each `InputPathsMaps` value in brackets: <*value* >

If `InputTemplate` is a JSON object (surrounded by curly braces), the following restrictions apply:

- The placeholder cannot be used as an object key.

The following example shows the syntax for using `InputPathsMap` and `InputTemplate` .

`"InputTransformer":`

`{`

`"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},`

`"InputTemplate": "<instance> is in state <status>"`

`}`

To have the `InputTemplate` include quote marks within a JSON string, escape each quote marks with a slash, as in the following example:

`"InputTransformer":`

`{`

`"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},`

`"InputTemplate": "<instance> is in state \"<status>\""`

`}`

The `InputTemplate` can also be valid JSON with varibles in quotes or out, as in the following example:

`"InputTransformer":`

`{`

`"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},`

`"InputTemplate": '{"myInstance": <instance>,"myStatus": "<instance> is in state \"<status>\""}'`

`}`

KinesisParameters -> (structure)

The custom parameter you can use to control the shard assignment, when the target is a Kinesis data stream. If you do not include this parameter, the default is to use the `eventId` as the partition key.

PartitionKeyPath -> (string)

The JSON path to be extracted from the event and used as the partition key. For more information, see [Amazon Kinesis Streams Key Concepts](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#partition-key) in the *Amazon Kinesis Streams Developer Guide* .

RunCommandParameters -> (structure)

Parameters used when you are using the rule to invoke Amazon EC2 Run Command.

RunCommandTargets -> (list)

Currently, we support including only one RunCommandTarget block, which specifies either an array of InstanceIds or a tag.

(structure)

Information about the EC2 instances that are to be sent the command, specified as key-value pairs. Each `RunCommandTarget` block can include only one key, but this key may specify multiple values.

Key -> (string)

Can be either `tag:` *tag-key* or `InstanceIds` .

Values -> (list)

If `Key` is `tag:` *tag-key* , `Values` is a list of tag values. If `Key` is `InstanceIds` , `Values` is a list of Amazon EC2 instance IDs.

(string)

EcsParameters -> (structure)

Contains the Amazon ECS task definition and task count to be used, if the event target is an Amazon ECS task. For more information about Amazon ECS tasks, see [Task Definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html) in the *Amazon EC2 Container Service Developer Guide* .

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

Specifies an ECS task group for the task. The maximum length is 255 characters.

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

Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the TagResource API action.

ReferenceId -> (string)

The reference ID to use for the task.

Tags -> (list)

The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. To learn more, see [RunTask](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html#ECS-RunTask-request-tags) in the Amazon ECS API Reference.

(structure)

A key-value pair associated with an Amazon Web Services resource. In EventBridge, rules and event buses support tagging.

Key -> (string)

A string you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.

Value -> (string)

The value for the specified tag key.

BatchParameters -> (structure)

If the event target is an Batch job, this contains the job definition, job name, and other parameters. For more information, see [Jobs](https://docs.aws.amazon.com/batch/latest/userguide/jobs.html) in the *Batch User Guide* .

JobDefinition -> (string)

The ARN or name of the job definition to use if the event target is an Batch job. This job definition must already exist.

JobName -> (string)

The name to use for this execution of the job, if the target is an Batch job.

ArrayProperties -> (structure)

The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. This parameter is used only if the target is an Batch job.

Size -> (integer)

The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.

RetryStrategy -> (structure)

The retry strategy to use for failed jobs, if the target is an Batch job. The retry strategy is the number of times to retry the failed job execution. Valid values are 1â10. When you specify a retry strategy here, it overrides the retry strategy defined in the job definition.

Attempts -> (integer)

The number of times to attempt to retry, if the job fails. Valid values are 1â10.

SqsParameters -> (structure)

Contains the message group ID to use when the target is a FIFO queue.

If you specify an SQS FIFO queue as a target, the queue must have content-based deduplication enabled.

MessageGroupId -> (string)

The FIFO message group ID to use as the target.

HttpParameters -> (structure)

Contains the HTTP parameters to use when the target is a API Gateway endpoint or EventBridge ApiDestination.

If you specify an API Gateway API or EventBridge ApiDestination as a target, you can use this parameter to specify headers, path parameters, and query string keys/values as part of your target invoking request. If youâre using ApiDestinations, the corresponding Connection can also have these values configured. In case of any conflicting keys, values from the Connection take precedence.

PathParameterValues -> (list)

The path parameter values to be used to populate API Gateway API or EventBridge ApiDestination path wildcards (â*â).

(string)

HeaderParameters -> (map)

The headers that need to be sent as part of request invoking the API Gateway API or EventBridge ApiDestination.

key -> (string)

value -> (string)

QueryStringParameters -> (map)

The query string keys/values that need to be sent as part of request invoking the API Gateway API or EventBridge ApiDestination.

key -> (string)

value -> (string)

RedshiftDataParameters -> (structure)

Contains the Amazon Redshift Data API parameters to use when the target is a Amazon Redshift cluster.

If you specify a Amazon Redshift Cluster as a Target, you can use this to specify parameters to invoke the Amazon Redshift Data API ExecuteStatement based on EventBridge events.

SecretManagerArn -> (string)

The name or ARN of the secret that enables access to the database. Required when authenticating using Amazon Web Services Secrets Manager.

Database -> (string)

The name of the database. Required when authenticating using temporary credentials.

DbUser -> (string)

The database user name. Required when authenticating using temporary credentials.

Sql -> (string)

The SQL statement text to run.

StatementName -> (string)

The name of the SQL statement. You can name the SQL statement when you create it to identify the query.

WithEvent -> (boolean)

Indicates whether to send an event back to EventBridge after the SQL statement runs.

Sqls -> (list)

One or more SQL statements to run. The SQL statements are run as a single transaction. They run serially in the order of the array. Subsequent SQL statements donât start until the previous statement in the array completes. If any SQL statement fails, then because they are run as one transaction, all work is rolled back.

(string)

A single Redshift SQL

SageMakerPipelineParameters -> (structure)

Contains the SageMaker AI Model Building Pipeline parameters to start execution of a SageMaker AI Model Building Pipeline.

If you specify a SageMaker AI Model Building Pipeline as a target, you can use this to specify parameters to start a pipeline execution based on EventBridge events.

PipelineParameterList -> (list)

List of Parameter names and values for SageMaker AI Model Building Pipeline execution.

(structure)

Name/Value pair of a parameter to start execution of a SageMaker AI Model Building Pipeline.

Name -> (string)

Name of parameter to start execution of a SageMaker AI Model Building Pipeline.

Value -> (string)

Value of parameter to start execution of a SageMaker AI Model Building Pipeline.

DeadLetterConfig -> (structure)

The `DeadLetterConfig` that defines the target queue to send dead-letter queue events to.

Arn -> (string)

The ARN of the SQS queue specified as the target for the dead-letter queue.

RetryPolicy -> (structure)

The retry policy configuration to use for the dead-letter queue.

MaximumRetryAttempts -> (integer)

The maximum number of retry attempts to make before the request fails. Retry attempts continue until either the maximum number of attempts is made or until the duration of the `MaximumEventAgeInSeconds` is met.

MaximumEventAgeInSeconds -> (integer)

The maximum amount of time, in seconds, to continue to make retry attempts.

AppSyncParameters -> (structure)

Contains the GraphQL operation to be parsed and executed, if the event target is an AppSync API.

GraphQLOperation -> (string)

The GraphQL operation; that is, the query, mutation, or subscription to be parsed and executed by the GraphQL service.

For more information, see [Operations](https://docs.aws.amazon.com/appsync/latest/devguide/graphql-architecture.html#graphql-operations) in the *AppSync User Guide* .

NextToken -> (string)

A token indicating there are more results available. If there are no more results, no token is included in the response.

The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.

Using an expired pagination token results in an `HTTP 400 InvalidToken` error.