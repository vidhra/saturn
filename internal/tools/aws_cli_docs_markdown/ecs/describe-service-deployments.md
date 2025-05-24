# describe-service-deploymentsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-service-deployments.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-service-deployments.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ecs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/index.html#cli-aws-ecs) ]

# describe-service-deployments

## Description

Describes one or more of your service deployments.

A service deployment happens when you release a software update for the service. For more information, see [View service history using Amazon ECS service deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-deployment.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeServiceDeployments)

## Synopsis

```
describe-service-deployments
--service-deployment-arns <value>
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

`--service-deployment-arns` (list)

The ARN of the service deployment.

You can specify a maximum of 20 ARNs.

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

**To describe service deployment details**

The following `describe-service-deployments` example returns the service deployment details for the service deployment with the ARN `arn:aws:ecs:us-east-1:123456789012:service-deployment/example-cluster/example-service/ejGvqq2ilnbKT9qj0vLJe`.

```
aws ecs describe-service-deployments \
    --service-deployment-arn arn:aws:ecs:us-east-1:123456789012:service-deployment/example-cluster/example-service/ejGvqq2ilnbKT9qj0vLJe
```

Output:

```
{
    "serviceDeployments": [
        {
            "serviceDeploymentArn": "arn:aws:ecs:us-east-1:123456789012:service-deployment/example-cluster/example-service/ejGvqq2ilnbKT9qj0vLJe",
            "serviceArn": "arn:aws:ecs:us-east-1:123456789012:service/example-cluster/example-service",
            "clusterArn": "arn:aws:ecs:us-east-1:123456789012:cluster/example-cluster",
            "createdAt": "2024-10-31T08:03:30.917000-04:00",
            "startedAt": "2024-10-31T08:03:32.510000-04:00",
            "finishedAt": "2024-10-31T08:05:04.527000-04:00",
            "updatedAt": "2024-10-31T08:05:04.527000-04:00",
            "sourceServiceRevisions": [],
            "targetServiceRevision": {
                "arn": "arn:aws:ecs:us-east-1:123456789012:service-revision/example-cluster/example-service/1485800978477494678",
                "requestedTaskCount": 1,
                "runningTaskCount": 1,
                "pendingTaskCount": 0
            },
            "status": "SUCCESSFUL",
            "deploymentConfiguration": {
                "deploymentCircuitBreaker": {
                    "enable": true,
                    "rollback": true
                },
                "maximumPercent": 200,
                "minimumHealthyPercent": 100,
                "alarms": {
                    "alarmNames": [],
                    "rollback": false,
                    "enable": false
                }
            },
            "deploymentCircuitBreaker": {
                "status": "MONITORING_COMPLETE",
                "failureCount": 0,
                "threshold": 3
            },
            "alarms": {
                "status": "DISABLED"
            }
        }
    ],
    "failures": []
}
```

For more information, see [View service history using Amazon ECS service deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-deployment.html) in the *Amazon ECS Developer Guide*.

## Output

serviceDeployments -> (list)

The list of service deployments described.

(structure)

Information about the service deployment.

Service deployments provide a comprehensive view of your deployments. For information about service deployments, see [View service history using Amazon ECS service deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-deployment.html) in the * *Amazon Elastic Container Service Developer Guide* * .

serviceDeploymentArn -> (string)

The ARN of the service deployment.

serviceArn -> (string)

The ARN of the service for this service deployment.

clusterArn -> (string)

The ARN of the cluster that hosts the service.

createdAt -> (timestamp)

The time the service deployment was created. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.

startedAt -> (timestamp)

The time the service deployment statred. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.

finishedAt -> (timestamp)

The time the service deployment finished. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.

stoppedAt -> (timestamp)

The time the service deployment stopped. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.

The service deployment stops when any of the following actions happen:

- A user manually stops the deployment
- The rollback option is not in use for the failure detection mechanism (the circuit breaker or alarm-based) and the service fails.

updatedAt -> (timestamp)

The time that the service deployment was last updated. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.

sourceServiceRevisions -> (list)

The currently deployed workload configuration.

(structure)

The information about the number of requested, pending, and running tasks for a service revision.

arn -> (string)

The ARN of the service revision.

requestedTaskCount -> (integer)

The number of requested tasks for the service revision.

runningTaskCount -> (integer)

The number of running tasks for the service revision.

pendingTaskCount -> (integer)

The number of pending tasks for the service revision.

targetServiceRevision -> (structure)

The workload configuration being deployed.

arn -> (string)

The ARN of the service revision.

requestedTaskCount -> (integer)

The number of requested tasks for the service revision.

runningTaskCount -> (integer)

The number of running tasks for the service revision.

pendingTaskCount -> (integer)

The number of pending tasks for the service revision.

status -> (string)

The service deployment state.

statusReason -> (string)

Information about why the service deployment is in the current status. For example, the circuit breaker detected a failure.

deploymentConfiguration -> (structure)

Optional deployment parameters that control how many tasks run during a deployment and the ordering of stopping and starting tasks.

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

rollback -> (structure)

The rollback options the service deployment uses when the deployment fails.

reason -> (string)

The reason the rollback happened. For example, the circuit breaker initiated the rollback operation.

startedAt -> (timestamp)

Time time that the rollback started. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.

serviceRevisionArn -> (string)

The ARN of the service revision deployed as part of the rollback.

deploymentCircuitBreaker -> (structure)

The circuit breaker configuration that determines a service deployment failed.

status -> (string)

The circuit breaker status. Amazon ECS is not using the circuit breaker for service deployment failures when the status is `DISABLED` .

failureCount -> (integer)

The number of times the circuit breaker detected a service deploymeny failure.

threshold -> (integer)

The threshhold which determines that the service deployment failed.

The deployment circuit breaker calculates the threshold value, and then uses the value to determine when to move the deployment to a FAILED state. The deployment circuit breaker has a minimum threshold of 3 and a maximum threshold of 200. and uses the values in the following formula to determine the deployment failure.

`0.5 * desired task count`

alarms -> (structure)

The CloudWatch alarms that determine when a service deployment fails.

status -> (string)

The status of the alarms check. Amazon ECS is not using alarms for service deployment failures when the status is `DISABLED` .

alarmNames -> (list)

The name of the CloudWatch alarms that determine when a service deployment failed. A â,â separates the alarms.

(string)

triggeredAlarmNames -> (list)

One or more CloudWatch alarm names that have been triggered during the service deployment. A â,â separates the alarm names.

(string)

failures -> (list)

Any failures associated with the call.

If you decsribe a deployment with a service revision created before October 25, 2024, the call fails. The failure includes the service revision ARN and the reason set to `MISSING` .

(structure)

A failed resource. For a list of common causes, see [API failure reasons](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/api_failures_messages.html) in the *Amazon Elastic Container Service Developer Guide* .

arn -> (string)

The Amazon Resource Name (ARN) of the failed resource.

reason -> (string)

The reason for the failure.

detail -> (string)

The details of the failure.