# get-deployment-targetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment-target.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment-target.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [deploy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/index.html#cli-aws-deploy) ]

# get-deployment-target

## Description

Returns information about a deployment target.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetDeploymentTarget)

## Synopsis

```
get-deployment-target
--deployment-id <value>
--target-id <value>
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

`--deployment-id` (string)

The unique ID of a deployment.

`--target-id` (string)

The unique ID of a deployment target.

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

**To return information about a deployment target**

The following `get-deployment-target` example returns information about a deployment target that is associated with the specified deployment.

```
aws deploy get-deployment-target \
    --deployment-id "d-A1B2C3111" \
    --target-id "i-a1b2c3d4e5f611111"
```

Output:

```
{
    "deploymentTarget": {
        "deploymentTargetType": "InstanceTarget",
        "instanceTarget": {
            "lastUpdatedAt": 1556918687.504,
            "targetId": "i-a1b2c3d4e5f611111",
            "targetArn": "arn:aws:ec2:us-west-2:123456789012:instance/i-a1b2c3d4e5f611111",
            "status": "Succeeded",
            "lifecycleEvents": [
                {
                    "status": "Succeeded",
                    "diagnostics": {
                        "errorCode": "Success",
                        "message": "Succeeded",
                        "logTail": "",
                        "scriptName": ""
                    },
                    "lifecycleEventName": "ApplicationStop",
                    "startTime": 1556918592.162,
                    "endTime": 1556918592.247
                },
                {
                    "status": "Succeeded",
                    "diagnostics": {
                        "errorCode": "Success",
                        "message": "Succeeded",
                        "logTail": "",
                        "scriptName": ""
                    },
                    "lifecycleEventName": "DownloadBundle",
                    "startTime": 1556918593.193,
                    "endTime": 1556918593.981
                },
                {
                    "status": "Succeeded",
                    "diagnostics": {
                        "errorCode": "Success",
                        "message": "Succeeded",
                        "logTail": "",
                        "scriptName": ""
                    },
                    "lifecycleEventName": "BeforeInstall",
                    "startTime": 1556918594.805,
                    "endTime": 1556918681.807
                },
                {
                    "status": "Succeeded",
                    "diagnostics": {
                        "errorCode": "Success",
                        "message": "Succeeded",
                        "logTail": "",
                        "scriptName": ""
                    },
                    "lifecycleEventName": "Install",
                    "startTime": 1556918682.696,
                    "endTime": 1556918683.005
                },
                {
                    "status": "Succeeded",
                    "diagnostics": {
                        "errorCode": "Success",
                        "message": "Succeeded",
                        "logTail": "",
                        "scriptName": ""
                    },
                    "lifecycleEventName": "AfterInstall",
                    "startTime": 1556918684.135,
                    "endTime": 1556918684.216
                },
                {
                    "status": "Succeeded",
                    "diagnostics": {
                        "errorCode": "Success",
                        "message": "Succeeded",
                        "logTail": "",
                        "scriptName": ""
                    },
                    "lifecycleEventName": "ApplicationStart",
                    "startTime": 1556918685.211,
                    "endTime": 1556918685.295
                },
                {
                    "status": "Succeeded",
                    "diagnostics": {
                        "errorCode": "Success",
                        "message": "Succeeded",
                        "logTail": "",
                        "scriptName": ""
                    },
                    "lifecycleEventName": "ValidateService",
                    "startTime": 1556918686.65,
                    "endTime": 1556918686.747
                }
            ],
            "deploymentId": "d-A1B2C3111"
        }
    }
}
```

For more information, see [GetDeploymentTarget](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentTarget.html) in the *AWS CodeDeploy API Reference*.

## Output

deploymentTarget -> (structure)

A deployment target that contains information about a deployment such as its status, lifecycle events, and when it was last updated. It also contains metadata about the deployment target. The deployment target metadata depends on the deployment targetâs type (`instanceTarget` , `lambdaTarget` , or `ecsTarget` ).

deploymentTargetType -> (string)

The deployment type that is specific to the deploymentâs compute platform or deployments initiated by a CloudFormation stack update.

instanceTarget -> (structure)

Information about the target for a deployment that uses the EC2/On-premises compute platform.

deploymentId -> (string)

The unique ID of a deployment.

targetId -> (string)

The unique ID of a deployment target that has a type of `instanceTarget` .

targetArn -> (string)

The Amazon Resource Name (ARN) of the target.

status -> (string)

The status an EC2/On-premises deploymentâs target instance.

lastUpdatedAt -> (timestamp)

The date and time when the target instance was updated by a deployment.

lifecycleEvents -> (list)

The lifecycle events of the deployment to this target instance.

(structure)

Information about a deployment lifecycle event.

lifecycleEventName -> (string)

The deployment lifecycle event name, such as `ApplicationStop` , `BeforeInstall` , `AfterInstall` , `ApplicationStart` , or `ValidateService` .

diagnostics -> (structure)

Diagnostic information about the deployment lifecycle event.

errorCode -> (string)

The associated error code:

- Success: The specified script ran.
- ScriptMissing: The specified script was not found in the specified location.
- ScriptNotExecutable: The specified script is not a recognized executable file type.
- ScriptTimedOut: The specified script did not finish running in the specified time period.
- ScriptFailed: The specified script failed to run as expected.
- UnknownError: The specified script did not run for an unknown reason.

scriptName -> (string)

The name of the script.

message -> (string)

The message associated with the error.

logTail -> (string)

The last portion of the diagnostic log.

If available, CodeDeploy returns up to the last 4 KB of the diagnostic log.

startTime -> (timestamp)

A timestamp that indicates when the deployment lifecycle event started.

endTime -> (timestamp)

A timestamp that indicates when the deployment lifecycle event ended.

status -> (string)

The deployment lifecycle event status:

- Pending: The deployment lifecycle event is pending.
- InProgress: The deployment lifecycle event is in progress.
- Succeeded: The deployment lifecycle event ran successfully.
- Failed: The deployment lifecycle event has failed.
- Skipped: The deployment lifecycle event has been skipped.
- Unknown: The deployment lifecycle event is unknown.

instanceLabel -> (string)

A label that identifies whether the instance is an original target (`BLUE` ) or a replacement target (`GREEN` ).

lambdaTarget -> (structure)

Information about the target for a deployment that uses the Lambda compute platform.

deploymentId -> (string)

The unique ID of a deployment.

targetId -> (string)

The unique ID of a deployment target that has a type of `lambdaTarget` .

targetArn -> (string)

The Amazon Resource Name (ARN) of the target.

status -> (string)

The status an Lambda deploymentâs target Lambda function.

lastUpdatedAt -> (timestamp)

The date and time when the target Lambda function was updated by a deployment.

lifecycleEvents -> (list)

The lifecycle events of the deployment to this target Lambda function.

(structure)

Information about a deployment lifecycle event.

lifecycleEventName -> (string)

The deployment lifecycle event name, such as `ApplicationStop` , `BeforeInstall` , `AfterInstall` , `ApplicationStart` , or `ValidateService` .

diagnostics -> (structure)

Diagnostic information about the deployment lifecycle event.

errorCode -> (string)

The associated error code:

- Success: The specified script ran.
- ScriptMissing: The specified script was not found in the specified location.
- ScriptNotExecutable: The specified script is not a recognized executable file type.
- ScriptTimedOut: The specified script did not finish running in the specified time period.
- ScriptFailed: The specified script failed to run as expected.
- UnknownError: The specified script did not run for an unknown reason.

scriptName -> (string)

The name of the script.

message -> (string)

The message associated with the error.

logTail -> (string)

The last portion of the diagnostic log.

If available, CodeDeploy returns up to the last 4 KB of the diagnostic log.

startTime -> (timestamp)

A timestamp that indicates when the deployment lifecycle event started.

endTime -> (timestamp)

A timestamp that indicates when the deployment lifecycle event ended.

status -> (string)

The deployment lifecycle event status:

- Pending: The deployment lifecycle event is pending.
- InProgress: The deployment lifecycle event is in progress.
- Succeeded: The deployment lifecycle event ran successfully.
- Failed: The deployment lifecycle event has failed.
- Skipped: The deployment lifecycle event has been skipped.
- Unknown: The deployment lifecycle event is unknown.

lambdaFunctionInfo -> (structure)

A `LambdaFunctionInfo` object that describes a target Lambda function.

functionName -> (string)

The name of a Lambda function.

functionAlias -> (string)

The alias of a Lambda function. For more information, see [Lambda Function Aliases](https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html) in the *Lambda Developer Guide* .

currentVersion -> (string)

The version of a Lambda function that production traffic points to.

targetVersion -> (string)

The version of a Lambda function that production traffic points to after the Lambda function is deployed.

targetVersionWeight -> (double)

The percentage of production traffic that the target version of a Lambda function receives.

ecsTarget -> (structure)

Information about the target for a deployment that uses the Amazon ECS compute platform.

deploymentId -> (string)

The unique ID of a deployment.

targetId -> (string)

The unique ID of a deployment target that has a type of `ecsTarget` .

targetArn -> (string)

The Amazon Resource Name (ARN) of the target.

lastUpdatedAt -> (timestamp)

The date and time when the target Amazon ECS application was updated by a deployment.

lifecycleEvents -> (list)

The lifecycle events of the deployment to this target Amazon ECS application.

(structure)

Information about a deployment lifecycle event.

lifecycleEventName -> (string)

The deployment lifecycle event name, such as `ApplicationStop` , `BeforeInstall` , `AfterInstall` , `ApplicationStart` , or `ValidateService` .

diagnostics -> (structure)

Diagnostic information about the deployment lifecycle event.

errorCode -> (string)

The associated error code:

- Success: The specified script ran.
- ScriptMissing: The specified script was not found in the specified location.
- ScriptNotExecutable: The specified script is not a recognized executable file type.
- ScriptTimedOut: The specified script did not finish running in the specified time period.
- ScriptFailed: The specified script failed to run as expected.
- UnknownError: The specified script did not run for an unknown reason.

scriptName -> (string)

The name of the script.

message -> (string)

The message associated with the error.

logTail -> (string)

The last portion of the diagnostic log.

If available, CodeDeploy returns up to the last 4 KB of the diagnostic log.

startTime -> (timestamp)

A timestamp that indicates when the deployment lifecycle event started.

endTime -> (timestamp)

A timestamp that indicates when the deployment lifecycle event ended.

status -> (string)

The deployment lifecycle event status:

- Pending: The deployment lifecycle event is pending.
- InProgress: The deployment lifecycle event is in progress.
- Succeeded: The deployment lifecycle event ran successfully.
- Failed: The deployment lifecycle event has failed.
- Skipped: The deployment lifecycle event has been skipped.
- Unknown: The deployment lifecycle event is unknown.

status -> (string)

The status an Amazon ECS deploymentâs target ECS application.

taskSetsInfo -> (list)

The `ECSTaskSet` objects associated with the ECS target.

(structure)

Information about a set of Amazon ECS tasks in an CodeDeploy deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic. An CodeDeploy application that uses the Amazon ECS compute platform deploys a containerized application in an Amazon ECS service as a task set.

identifer -> (string)

A unique ID of an `ECSTaskSet` .

desiredCount -> (long)

The number of tasks in a task set. During a deployment that uses the Amazon ECS compute type, CodeDeploy instructs Amazon ECS to create a new task set and uses this value to determine how many tasks to create. After the updated task set is created, CodeDeploy shifts traffic to the new task set.

pendingCount -> (long)

The number of tasks in the task set that are in the `PENDING` status during an Amazon ECS deployment. A task in the `PENDING` state is preparing to enter the `RUNNING` state. A task set enters the `PENDING` status when it launches for the first time, or when it is restarted after being in the `STOPPED` state.

runningCount -> (long)

The number of tasks in the task set that are in the `RUNNING` status during an Amazon ECS deployment. A task in the `RUNNING` state is running and ready for use.

status -> (string)

The status of the task set. There are three valid task set statuses:

- `PRIMARY` : Indicates the task set is serving production traffic.
- `ACTIVE` : Indicates the task set is not serving production traffic.
- `DRAINING` : Indicates the tasks in the task set are being stopped and their corresponding targets are being deregistered from their target group.

trafficWeight -> (double)

The percentage of traffic served by this task set.

targetGroup -> (structure)

The target group associated with the task set. The target group is used by CodeDeploy to manage traffic to a task set.

name -> (string)

For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.

taskSetLabel -> (string)

A label that identifies whether the ECS task set is an original target (`BLUE` ) or a replacement target (`GREEN` ).

cloudFormationTarget -> (structure)

Information about the target to be updated by an CloudFormation blue/green deployment. This target type is used for all deployments initiated by a CloudFormation stack update.

deploymentId -> (string)

The unique ID of an CloudFormation blue/green deployment.

targetId -> (string)

The unique ID of a deployment target that has a type of `CloudFormationTarget` .

lastUpdatedAt -> (timestamp)

The date and time when the target application was updated by an CloudFormation blue/green deployment.

lifecycleEvents -> (list)

The lifecycle events of the CloudFormation blue/green deployment to this target application.

(structure)

Information about a deployment lifecycle event.

lifecycleEventName -> (string)

The deployment lifecycle event name, such as `ApplicationStop` , `BeforeInstall` , `AfterInstall` , `ApplicationStart` , or `ValidateService` .

diagnostics -> (structure)

Diagnostic information about the deployment lifecycle event.

errorCode -> (string)

The associated error code:

- Success: The specified script ran.
- ScriptMissing: The specified script was not found in the specified location.
- ScriptNotExecutable: The specified script is not a recognized executable file type.
- ScriptTimedOut: The specified script did not finish running in the specified time period.
- ScriptFailed: The specified script failed to run as expected.
- UnknownError: The specified script did not run for an unknown reason.

scriptName -> (string)

The name of the script.

message -> (string)

The message associated with the error.

logTail -> (string)

The last portion of the diagnostic log.

If available, CodeDeploy returns up to the last 4 KB of the diagnostic log.

startTime -> (timestamp)

A timestamp that indicates when the deployment lifecycle event started.

endTime -> (timestamp)

A timestamp that indicates when the deployment lifecycle event ended.

status -> (string)

The deployment lifecycle event status:

- Pending: The deployment lifecycle event is pending.
- InProgress: The deployment lifecycle event is in progress.
- Succeeded: The deployment lifecycle event ran successfully.
- Failed: The deployment lifecycle event has failed.
- Skipped: The deployment lifecycle event has been skipped.
- Unknown: The deployment lifecycle event is unknown.

status -> (string)

The status of an CloudFormation blue/green deploymentâs target application.

resourceType -> (string)

The resource type for the CloudFormation blue/green deployment.

targetVersionWeight -> (double)

The percentage of production traffic that the target version of an CloudFormation blue/green deployment receives.