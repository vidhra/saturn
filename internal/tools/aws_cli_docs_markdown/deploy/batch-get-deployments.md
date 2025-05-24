# batch-get-deploymentsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/batch-get-deployments.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/batch-get-deployments.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [deploy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/index.html#cli-aws-deploy) ]

# batch-get-deployments

## Description

Gets information about one or more deployments. The maximum number of deployments that can be returned is 25.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/BatchGetDeployments)

## Synopsis

```
batch-get-deployments
--deployment-ids <value>
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

`--deployment-ids` (list)

A list of deployment IDs, separated by spaces. The maximum number of deployment IDs you can specify is 25.

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

**To get information about multiple deployments**

The following `batch-get-deployments` example displays information about multiple deployments that are associated with the userâs AWS account.

```
aws deploy batch-get-deployments --deployment-ids d-A1B2C3111 d-A1B2C3222
```

Output:

```
{
    "deploymentsInfo": [
        {
            "applicationName": "WordPress_App",
            "status": "Failed",
            "deploymentOverview": {
                "Failed": 0,
                "InProgress": 0,
                "Skipped": 0,
                "Succeeded": 1,
                "Pending": 0
            },
            "deploymentConfigName": "CodeDeployDefault.OneAtATime",
            "creator": "user",
            "deploymentGroupName": "WordPress_DG",
            "revision": {
                "revisionType": "S3",
                "s3Location": {
                "bundleType": "zip",
                "version": "uTecLusEXAMPLEFXtfUcyfV8bEXAMPLE",
                "bucket": "CodeDeployDemoBucket",
                "key": "WordPressApp.zip"
                }
            },
            "deploymentId": "d-A1B2C3111",
            "createTime": 1408480721.9,
            "completeTime": 1408480741.822
        },
        {
            "applicationName": "MyOther_App",
            "status": "Failed",
            "deploymentOverview": {
                "Failed": 1,
                "InProgress": 0,
                "Skipped": 0,
                "Succeeded": 0,
                "Pending": 0
            },
            "deploymentConfigName": "CodeDeployDefault.OneAtATime",
            "creator": "user",
            "errorInformation": {
                "message": "Deployment failed: Constraint default violated: No hosts succeeded.",
                "code": "HEALTH_CONSTRAINTS"
            },
            "deploymentGroupName": "MyOther_DG",
            "revision": {
                "revisionType": "S3",
                "s3Location": {
                "bundleType": "zip",
                "eTag": "\"dd56cfdEXAMPLE8e768f9d77fEXAMPLE\"",
                "bucket": "CodeDeployDemoBucket",
                "key": "MyOtherApp.zip"
                }
            },
            "deploymentId": "d-A1B2C3222",
            "createTime": 1409764576.589,
            "completeTime": 1409764596.101
        }
    ]
}
```

## Output

deploymentsInfo -> (list)

Information about the deployments.

(structure)

Information about a deployment.

applicationName -> (string)

The application name.

deploymentGroupName -> (string)

The deployment group name.

deploymentConfigName -> (string)

The deployment configuration name.

deploymentId -> (string)

The unique ID of a deployment.

previousRevision -> (structure)

Information about the application revision that was deployed to the deployment group before the most recent successful deployment.

revisionType -> (string)

The type of application revision:

- S3: An application revision stored in Amazon S3.
- GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
- String: A YAML-formatted or JSON-formatted string (Lambda deployments only).
- AppSpecContent: An `AppSpecContent` object that contains the contents of an AppSpec file for an Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.

s3Location -> (structure)

Information about the location of a revision stored in Amazon S3.

bucket -> (string)

The name of the Amazon S3 bucket where the application revision is stored.

key -> (string)

The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

bundleType -> (string)

The file type of the application revision. Must be one of the following:

- `tar` : A tar archive file.
- `tgz` : A compressed tar archive file.
- `zip` : A zip archive file.
- `YAML` : A YAML-formatted file.
- `JSON` : A JSON-formatted file.

version -> (string)

A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

If the version is not specified, the system uses the most recent version by default.

eTag -> (string)

The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

If the ETag is not specified as an input parameter, ETag validation of the object is skipped.

gitHubLocation -> (structure)

Information about the location of application artifacts stored in GitHub.

repository -> (string)

The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.

Specified as account/repository.

commitId -> (string)

The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

string -> (structure)

Information about the location of an Lambda deployment revision stored as a RawString.

content -> (string)

The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

sha256 -> (string)

The SHA256 hash value of the revision content.

appSpecContent -> (structure)

The content of an AppSpec file for an Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.

content -> (string)

The YAML-formatted or JSON-formatted revision string.

For an Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.

For an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.

For both types of deployments, the content can specify Lambda functions that run at specified hooks, such as `BeforeInstall` , during a deployment.

sha256 -> (string)

The SHA256 hash value of the revision content.

revision -> (structure)

Information about the location of stored application artifacts and the service from which to retrieve them.

revisionType -> (string)

The type of application revision:

- S3: An application revision stored in Amazon S3.
- GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
- String: A YAML-formatted or JSON-formatted string (Lambda deployments only).
- AppSpecContent: An `AppSpecContent` object that contains the contents of an AppSpec file for an Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.

s3Location -> (structure)

Information about the location of a revision stored in Amazon S3.

bucket -> (string)

The name of the Amazon S3 bucket where the application revision is stored.

key -> (string)

The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

bundleType -> (string)

The file type of the application revision. Must be one of the following:

- `tar` : A tar archive file.
- `tgz` : A compressed tar archive file.
- `zip` : A zip archive file.
- `YAML` : A YAML-formatted file.
- `JSON` : A JSON-formatted file.

version -> (string)

A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

If the version is not specified, the system uses the most recent version by default.

eTag -> (string)

The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

If the ETag is not specified as an input parameter, ETag validation of the object is skipped.

gitHubLocation -> (structure)

Information about the location of application artifacts stored in GitHub.

repository -> (string)

The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.

Specified as account/repository.

commitId -> (string)

The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

string -> (structure)

Information about the location of an Lambda deployment revision stored as a RawString.

content -> (string)

The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

sha256 -> (string)

The SHA256 hash value of the revision content.

appSpecContent -> (structure)

The content of an AppSpec file for an Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.

content -> (string)

The YAML-formatted or JSON-formatted revision string.

For an Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.

For an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.

For both types of deployments, the content can specify Lambda functions that run at specified hooks, such as `BeforeInstall` , during a deployment.

sha256 -> (string)

The SHA256 hash value of the revision content.

status -> (string)

The current state of the deployment as a whole.

errorInformation -> (structure)

Information about any error associated with this deployment.

code -> (string)

For more information, see [Error Codes for CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/error-codes.html) in the [CodeDeploy User Guide](https://docs.aws.amazon.com/codedeploy/latest/userguide) .

The error code:

- APPLICATION_MISSING: The application was missing. This error code is most likely raised if the application is deleted after the deployment is created, but before it is started.
- DEPLOYMENT_GROUP_MISSING: The deployment group was missing. This error code is most likely raised if the deployment group is deleted after the deployment is created, but before it is started.
- HEALTH_CONSTRAINTS: The deployment failed on too many instances to be successfully deployed within the instance health constraints specified.
- HEALTH_CONSTRAINTS_INVALID: The revision cannot be successfully deployed within the instance health constraints specified.
- IAM_ROLE_MISSING: The service role cannot be accessed.
- IAM_ROLE_PERMISSIONS: The service role does not have the correct permissions.
- INTERNAL_ERROR: There was an internal error.
- NO_EC2_SUBSCRIPTION: The calling account is not subscribed to Amazon EC2.
- NO_INSTANCES: No instances were specified, or no instances can be found.
- OVER_MAX_INSTANCES: The maximum number of instances was exceeded.
- THROTTLED: The operation was throttled because the calling account exceeded the throttling limits of one or more Amazon Web Services services.
- TIMEOUT: The deployment has timed out.
- REVISION_MISSING: The revision ID was missing. This error code is most likely raised if the revision is deleted after the deployment is created, but before it is started.

message -> (string)

An accompanying error message.

createTime -> (timestamp)

A timestamp that indicates when the deployment was created.

startTime -> (timestamp)

A timestamp that indicates when the deployment was deployed to the deployment group.

In some cases, the reported value of the start time might be later than the complete time. This is due to differences in the clock settings of backend servers that participate in the deployment process.

completeTime -> (timestamp)

A timestamp that indicates when the deployment was complete.

deploymentOverview -> (structure)

A summary of the deployment status of the instances in the deployment.

Pending -> (long)

The number of instances in the deployment in a pending state.

InProgress -> (long)

The number of instances in which the deployment is in progress.

Succeeded -> (long)

The number of instances in the deployment to which revisions have been successfully deployed.

Failed -> (long)

The number of instances in the deployment in a failed state.

Skipped -> (long)

The number of instances in the deployment in a skipped state.

Ready -> (long)

The number of instances in a replacement environment ready to receive traffic in a blue/green deployment.

description -> (string)

A comment about the deployment.

creator -> (string)

The means by which the deployment was created:

- `user` : A user created the deployment.
- `autoscaling` : Amazon EC2 Auto Scaling created the deployment.
- `codeDeployRollback` : A rollback process created the deployment.
- `CodeDeployAutoUpdate` : An auto-update process created the deployment when it detected outdated Amazon EC2 instances.

ignoreApplicationStopFailures -> (boolean)

If true, then if an `ApplicationStop` , `BeforeBlockTraffic` , or `AfterBlockTraffic` deployment lifecycle event to an instance fails, then the deployment continues to the next deployment lifecycle event. For example, if `ApplicationStop` fails, the deployment continues with DownloadBundle. If `BeforeBlockTraffic` fails, the deployment continues with `BlockTraffic` . If `AfterBlockTraffic` fails, the deployment continues with `ApplicationStop` .

If false or not specified, then if a lifecycle event fails during a deployment to an instance, that deployment fails. If deployment to that instance is part of an overall deployment and the number of healthy hosts is not less than the minimum number of healthy hosts, then a deployment to the next instance is attempted.

During a deployment, the CodeDeploy agent runs the scripts specified for `ApplicationStop` , `BeforeBlockTraffic` , and `AfterBlockTraffic` in the AppSpec file from the previous successful deployment. (All other scripts are run from the AppSpec file in the current deployment.) If one of these scripts contains an error and does not run successfully, the deployment can fail.

If the cause of the failure is a script from the last successful deployment that will never run successfully, create a new deployment and use `ignoreApplicationStopFailures` to specify that the `ApplicationStop` , `BeforeBlockTraffic` , and `AfterBlockTraffic` failures should be ignored.

autoRollbackConfiguration -> (structure)

Information about the automatic rollback configuration associated with the deployment.

enabled -> (boolean)

Indicates whether a defined automatic rollback configuration is currently enabled.

events -> (list)

The event type or types that trigger a rollback.

(string)

updateOutdatedInstancesOnly -> (boolean)

Indicates whether only instances that are not running the latest application revision are to be deployed to.

rollbackInfo -> (structure)

Information about a deployment rollback.

rollbackDeploymentId -> (string)

The ID of the deployment rollback.

rollbackTriggeringDeploymentId -> (string)

The deployment ID of the deployment that was underway and triggered a rollback deployment because it failed or was stopped.

rollbackMessage -> (string)

Information that describes the status of a deployment rollback (for example, whether the deployment canât be rolled back, is in progress, failed, or succeeded).

deploymentStyle -> (structure)

Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.

deploymentType -> (string)

Indicates whether to run an in-place deployment or a blue/green deployment.

deploymentOption -> (string)

Indicates whether to route deployment traffic behind a load balancer.

targetInstances -> (structure)

Information about the instances that belong to the replacement environment in a blue/green deployment.

tagFilters -> (list)

The tag filter key, type, and value used to identify Amazon EC2 instances in a replacement environment for a blue/green deployment. Cannot be used in the same call as `ec2TagSet` .

(structure)

Information about an EC2 tag filter.

Key -> (string)

The tag filter key.

Value -> (string)

The tag filter value.

Type -> (string)

The tag filter type:

- `KEY_ONLY` : Key only.
- `VALUE_ONLY` : Value only.
- `KEY_AND_VALUE` : Key and value.

autoScalingGroups -> (list)

The names of one or more Auto Scaling groups to identify a replacement environment for a blue/green deployment.

(string)

ec2TagSet -> (structure)

Information about the groups of Amazon EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment. Cannot be used in the same call as `tagFilters` .

ec2TagSetList -> (list)

A list that contains other lists of Amazon EC2 instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.

(list)

(structure)

Information about an EC2 tag filter.

Key -> (string)

The tag filter key.

Value -> (string)

The tag filter value.

Type -> (string)

The tag filter type:

- `KEY_ONLY` : Key only.
- `VALUE_ONLY` : Value only.
- `KEY_AND_VALUE` : Key and value.

instanceTerminationWaitTimeStarted -> (boolean)

Indicates whether the wait period set for the termination of instances in the original environment has started. Status is âfalseâ if the KEEP_ALIVE option is specified. Otherwise, âtrueâ as soon as the termination wait period starts.

blueGreenDeploymentConfiguration -> (structure)

Information about blue/green deployment options for this deployment.

terminateBlueInstancesOnDeploymentSuccess -> (structure)

Information about whether to terminate instances in the original fleet during a blue/green deployment.

action -> (string)

The action to take on instances in the original environment after a successful blue/green deployment.

- `TERMINATE` : Instances are terminated after a specified wait time.
- `KEEP_ALIVE` : Instances are left running after they are deregistered from the load balancer and removed from the deployment group.

terminationWaitTimeInMinutes -> (integer)

For an Amazon EC2 deployment, the number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.

For an Amazon ECS deployment, the number of minutes before deleting the original (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original (blue) task set to a replacement (green) task set.

The maximum setting is 2880 minutes (2 days).

deploymentReadyOption -> (structure)

Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.

actionOnTimeout -> (string)

Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.

- CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.
- STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic rerouting is started using  ContinueDeployment . If traffic rerouting is not started before the end of the specified wait period, the deployment status is changed to Stopped.

waitTimeInMinutes -> (integer)

The number of minutes to wait before the status of a blue/green deployment is changed to Stopped if rerouting is not started manually. Applies only to the `STOP_DEPLOYMENT` option for `actionOnTimeout` .

greenFleetProvisioningOption -> (structure)

Information about how instances are provisioned for a replacement environment in a blue/green deployment.

action -> (string)

The method used to add instances to a replacement environment.

- `DISCOVER_EXISTING` : Use instances that already exist or will be created manually.
- `COPY_AUTO_SCALING_GROUP` : Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group.

loadBalancerInfo -> (structure)

Information about the load balancer used in the deployment.

elbInfoList -> (list)

An array that contains information about the load balancers to use for load balancing in a deployment. If youâre using Classic Load Balancers, specify those load balancers in this array.

### Note

You can add up to 10 load balancers to the array.

### Note

If youâre using Application Load Balancers or Network Load Balancers, use the `targetGroupInfoList` array instead of this one.

(structure)

Information about a Classic Load Balancer in Elastic Load Balancing to use in a deployment. Instances are registered directly with a load balancer, and traffic is routed to the load balancer.

name -> (string)

For blue/green deployments, the name of the Classic Load Balancer that is used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the Classic Load Balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.

targetGroupInfoList -> (list)

An array that contains information about the target groups to use for load balancing in a deployment. If youâre using Application Load Balancers and Network Load Balancers, specify their associated target groups in this array.

### Note

You can add up to 10 target groups to the array.

### Note

If youâre using Classic Load Balancers, use the `elbInfoList` array instead of this one.

(structure)

Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.

name -> (string)

For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.

targetGroupPairInfoList -> (list)

The target group pair information. This is an array of `TargeGroupPairInfo` objects with a maximum size of one.

(structure)

Information about two target groups and how traffic is routed during an Amazon ECS deployment. An optional test traffic route can be specified.

targetGroups -> (list)

One pair of target groups. One is associated with the original task set. The second is associated with the task set that serves traffic after the deployment is complete.

(structure)

Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.

name -> (string)

For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.

prodTrafficRoute -> (structure)

The path used by a load balancer to route production traffic when an Amazon ECS deployment is complete.

listenerArns -> (list)

The Amazon Resource Name (ARN) of one listener. The listener identifies the route between a target group and a load balancer. This is an array of strings with a maximum size of one.

(string)

testTrafficRoute -> (structure)

An optional path used by a load balancer to route test traffic after an Amazon ECS deployment. Validation can occur while test traffic is served during a deployment.

listenerArns -> (list)

The Amazon Resource Name (ARN) of one listener. The listener identifies the route between a target group and a load balancer. This is an array of strings with a maximum size of one.

(string)

additionalDeploymentStatusInfo -> (string)

Provides information about the results of a deployment, such as whether instances in the original environment in a blue/green deployment were not terminated.

fileExistsBehavior -> (string)

Information about how CodeDeploy handles files that already exist in a deployment target location but werenât part of the previous successful deployment.

- `DISALLOW` : The deployment fails. This is also the default behavior if no option is specified.
- `OVERWRITE` : The version of the file from the application revision currently being deployed replaces the version already on the instance.
- `RETAIN` : The version of the file already on the instance is kept and used as part of the new deployment.

deploymentStatusMessages -> (list)

Messages that contain information about the status of a deployment.

(string)

computePlatform -> (string)

The destination platform type for the deployment (`Lambda` , `Server` , or `ECS` ).

externalId -> (string)

The unique ID for an external resource (for example, a CloudFormation stack ID) that is linked to this deployment.

relatedDeployments -> (structure)

Information about deployments related to the specified deployment.

autoUpdateOutdatedInstancesRootDeploymentId -> (string)

The deployment ID of the root deployment that triggered this deployment.

autoUpdateOutdatedInstancesDeploymentIds -> (list)

The deployment IDs of âauto-update outdated instancesâ deployments triggered by this deployment.

(string)

overrideAlarmConfiguration -> (structure)

Information about alarms associated with a deployment or deployment group.

enabled -> (boolean)

Indicates whether the alarm configuration is enabled.

ignorePollAlarmFailure -> (boolean)

Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.

- `true` : The deployment proceeds even if alarm status information canât be retrieved from Amazon CloudWatch.
- `false` : The deployment stops if alarm status information canât be retrieved from Amazon CloudWatch.

alarms -> (list)

A list of alarms configured for the deployment or deployment group. A maximum of 10 alarms can be added.

(structure)

Information about an alarm.

name -> (string)

The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only once in a list of alarms.