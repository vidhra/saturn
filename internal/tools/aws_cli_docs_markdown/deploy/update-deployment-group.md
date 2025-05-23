# update-deployment-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/update-deployment-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/update-deployment-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [deploy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/index.html#cli-aws-deploy) ]

# update-deployment-group

## Description

Changes information about a deployment group.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/UpdateDeploymentGroup)

## Synopsis

```
update-deployment-group
--application-name <value>
--current-deployment-group-name <value>
[--new-deployment-group-name <value>]
[--deployment-config-name <value>]
[--ec2-tag-filters <value>]
[--on-premises-instance-tag-filters <value>]
[--auto-scaling-groups <value>]
[--service-role-arn <value>]
[--trigger-configurations <value>]
[--alarm-configuration <value>]
[--auto-rollback-configuration <value>]
[--outdated-instances-strategy <value>]
[--deployment-style <value>]
[--blue-green-deployment-configuration <value>]
[--load-balancer-info <value>]
[--ec2-tag-set <value>]
[--ecs-services <value>]
[--on-premises-tag-set <value>]
[--termination-hook-enabled | --no-termination-hook-enabled]
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

`--application-name` (string)

The application name that corresponds to the deployment group to update.

`--current-deployment-group-name` (string)

The current name of the deployment group.

`--new-deployment-group-name` (string)

The new name of the deployment group, if you want to change it.

`--deployment-config-name` (string)

The replacement deployment configuration name to use, if you want to change it.

`--ec2-tag-filters` (list)

The replacement set of Amazon EC2 tags on which to filter, if you want to change them. To keep the existing tags, enter their names. To remove tags, do not enter any tag names.

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

Shorthand Syntax:

```
Key=string,Value=string,Type=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string",
    "Type": "KEY_ONLY"|"VALUE_ONLY"|"KEY_AND_VALUE"
  }
  ...
]
```

`--on-premises-instance-tag-filters` (list)

The replacement set of on-premises instance tags on which to filter, if you want to change them. To keep the existing tags, enter their names. To remove tags, do not enter any tag names.

(structure)

Information about an on-premises instance tag filter.

Key -> (string)

The on-premises instance tag filter key.

Value -> (string)

The on-premises instance tag filter value.

Type -> (string)

The on-premises instance tag filter type:

- KEY_ONLY: Key only.
- VALUE_ONLY: Value only.
- KEY_AND_VALUE: Key and value.

Shorthand Syntax:

```
Key=string,Value=string,Type=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string",
    "Type": "KEY_ONLY"|"VALUE_ONLY"|"KEY_AND_VALUE"
  }
  ...
]
```

`--auto-scaling-groups` (list)

The replacement list of Auto Scaling groups to be included in the deployment group, if you want to change them.

- To keep the Auto Scaling groups, enter their names or do not specify this parameter.
- To remove Auto Scaling groups, specify a non-null empty list of Auto Scaling group names to detach all CodeDeploy-managed Auto Scaling lifecycle hooks. For examples, see [Amazon EC2 instances in an Amazon EC2 Auto Scaling group fail to launch and receive the error âHeartbeat Timeoutâ](https://docs.aws.amazon.com/codedeploy/latest/userguide/troubleshooting-auto-scaling.html#troubleshooting-auto-scaling-heartbeat) in the *CodeDeploy User Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--service-role-arn` (string)

A replacement ARN for the service role, if you want to change it.

`--trigger-configurations` (list)

Information about triggers to change when the deployment group is updated. For examples, see [Edit a Trigger in a CodeDeploy Deployment Group](https://docs.aws.amazon.com/codedeploy/latest/userguide/how-to-notify-edit.html) in the *CodeDeploy User Guide* .

(structure)

Information about notification triggers for the deployment group.

triggerName -> (string)

The name of the notification trigger.

triggerTargetArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic through which notifications about deployment or instance events are sent.

triggerEvents -> (list)

The event type or types for which notifications are triggered.

(string)

Shorthand Syntax:

```
triggerName=string,triggerTargetArn=string,triggerEvents=string,string ...
```

JSON Syntax:

```
[
  {
    "triggerName": "string",
    "triggerTargetArn": "string",
    "triggerEvents": ["DeploymentStart"|"DeploymentSuccess"|"DeploymentFailure"|"DeploymentStop"|"DeploymentRollback"|"DeploymentReady"|"InstanceStart"|"InstanceSuccess"|"InstanceFailure"|"InstanceReady", ...]
  }
  ...
]
```

`--alarm-configuration` (structure)

Information to add or change about Amazon CloudWatch alarms when the deployment group is updated.

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

Shorthand Syntax:

```
enabled=boolean,ignorePollAlarmFailure=boolean,alarms=[{name=string},{name=string}]
```

JSON Syntax:

```
{
  "enabled": true|false,
  "ignorePollAlarmFailure": true|false,
  "alarms": [
    {
      "name": "string"
    }
    ...
  ]
}
```

`--auto-rollback-configuration` (structure)

Information for an automatic rollback configuration that is added or changed when a deployment group is updated.

enabled -> (boolean)

Indicates whether a defined automatic rollback configuration is currently enabled.

events -> (list)

The event type or types that trigger a rollback.

(string)

Shorthand Syntax:

```
enabled=boolean,events=string,string
```

JSON Syntax:

```
{
  "enabled": true|false,
  "events": ["DEPLOYMENT_FAILURE"|"DEPLOYMENT_STOP_ON_ALARM"|"DEPLOYMENT_STOP_ON_REQUEST", ...]
}
```

`--outdated-instances-strategy` (string)

Indicates what happens when new Amazon EC2 instances are launched mid-deployment and do not receive the deployed application revision.

If this option is set to `UPDATE` or is unspecified, CodeDeploy initiates one or more âauto-update outdated instancesâ deployments to apply the deployed application revision to the new Amazon EC2 instances.

If this option is set to `IGNORE` , CodeDeploy does not initiate a deployment to update the new Amazon EC2 instances. This may result in instances having different revisions.

Possible values:

- `UPDATE`
- `IGNORE`

`--deployment-style` (structure)

Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.

deploymentType -> (string)

Indicates whether to run an in-place deployment or a blue/green deployment.

deploymentOption -> (string)

Indicates whether to route deployment traffic behind a load balancer.

Shorthand Syntax:

```
deploymentType=string,deploymentOption=string
```

JSON Syntax:

```
{
  "deploymentType": "IN_PLACE"|"BLUE_GREEN",
  "deploymentOption": "WITH_TRAFFIC_CONTROL"|"WITHOUT_TRAFFIC_CONTROL"
}
```

`--blue-green-deployment-configuration` (structure)

Information about blue/green deployment options for a deployment group.

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

Shorthand Syntax:

```
terminateBlueInstancesOnDeploymentSuccess={action=string,terminationWaitTimeInMinutes=integer},deploymentReadyOption={actionOnTimeout=string,waitTimeInMinutes=integer},greenFleetProvisioningOption={action=string}
```

JSON Syntax:

```
{
  "terminateBlueInstancesOnDeploymentSuccess": {
    "action": "TERMINATE"|"KEEP_ALIVE",
    "terminationWaitTimeInMinutes": integer
  },
  "deploymentReadyOption": {
    "actionOnTimeout": "CONTINUE_DEPLOYMENT"|"STOP_DEPLOYMENT",
    "waitTimeInMinutes": integer
  },
  "greenFleetProvisioningOption": {
    "action": "DISCOVER_EXISTING"|"COPY_AUTO_SCALING_GROUP"
  }
}
```

`--load-balancer-info` (structure)

Information about the load balancer used in a deployment.

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

JSON Syntax:

```
{
  "elbInfoList": [
    {
      "name": "string"
    }
    ...
  ],
  "targetGroupInfoList": [
    {
      "name": "string"
    }
    ...
  ],
  "targetGroupPairInfoList": [
    {
      "targetGroups": [
        {
          "name": "string"
        }
        ...
      ],
      "prodTrafficRoute": {
        "listenerArns": ["string", ...]
      },
      "testTrafficRoute": {
        "listenerArns": ["string", ...]
      }
    }
    ...
  ]
}
```

`--ec2-tag-set` (structure)

Information about groups of tags applied to on-premises instances. The deployment group includes only Amazon EC2 instances identified by all the tag groups.

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

JSON Syntax:

```
{
  "ec2TagSetList": [
    [
      {
        "Key": "string",
        "Value": "string",
        "Type": "KEY_ONLY"|"VALUE_ONLY"|"KEY_AND_VALUE"
      }
      ...
    ]
    ...
  ]
}
```

`--ecs-services` (list)

The target Amazon ECS services in the deployment group. This applies only to deployment groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified as an Amazon ECS cluster and service name pair using the format `<clustername>:<servicename>` .

(structure)

Contains the service and cluster names used to identify an Amazon ECS deploymentâs target.

serviceName -> (string)

The name of the target Amazon ECS service.

clusterName -> (string)

The name of the cluster that the Amazon ECS service is associated with.

Shorthand Syntax:

```
serviceName=string,clusterName=string ...
```

JSON Syntax:

```
[
  {
    "serviceName": "string",
    "clusterName": "string"
  }
  ...
]
```

`--on-premises-tag-set` (structure)

Information about an on-premises instance tag set. The deployment group includes only on-premises instances identified by all the tag groups.

onPremisesTagSetList -> (list)

A list that contains other lists of on-premises instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.

(list)

(structure)

Information about an on-premises instance tag filter.

Key -> (string)

The on-premises instance tag filter key.

Value -> (string)

The on-premises instance tag filter value.

Type -> (string)

The on-premises instance tag filter type:

- KEY_ONLY: Key only.
- VALUE_ONLY: Value only.
- KEY_AND_VALUE: Key and value.

JSON Syntax:

```
{
  "onPremisesTagSetList": [
    [
      {
        "Key": "string",
        "Value": "string",
        "Type": "KEY_ONLY"|"VALUE_ONLY"|"KEY_AND_VALUE"
      }
      ...
    ]
    ...
  ]
}
```

`--termination-hook-enabled` | `--no-termination-hook-enabled` (boolean)

This parameter only applies if you are using CodeDeploy with Amazon EC2 Auto Scaling. For more information, see [Integrating CodeDeploy with Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html) in the *CodeDeploy User Guide* .

Set `terminationHookEnabled` to `true` to have CodeDeploy install a termination hook into your Auto Scaling group when you update a deployment group. When this hook is installed, CodeDeploy will perform termination deployments.

For information about termination deployments, see [Enabling termination deployments during Auto Scaling scale-in events](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html#integrations-aws-auto-scaling-behaviors-hook-enable) in the *CodeDeploy User Guide* .

For more information about Auto Scaling scale-in events, see the [Scale in](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.html#as-lifecycle-scale-in) topic in the *Amazon EC2 Auto Scaling User Guide* .

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

**To change information about a deployment group**

The following `update-deployment-group` example changes the settings of a deployment group that is associated with the specified application.

```
aws deploy update-deployment-group \
    --application-name WordPress_App \
    --auto-scaling-groups My_CodeDeployDemo_ASG \
    --current-deployment-group-name WordPress_DG \
    --deployment-config-name CodeDeployDefault.AllAtOnce \
    --ec2-tag-filters Key=Name,Type=KEY_AND_VALUE,Value=My_CodeDeployDemo \
    --new-deployment-group-name My_WordPress_DepGroup \
    --service-role-arn arn:aws:iam::80398EXAMPLE:role/CodeDeployDemo-2
```

This command produces no output.

## Output

hooksNotCleanedUp -> (list)

If the output contains no data, and the corresponding deployment group contained at least one Auto Scaling group, CodeDeploy successfully removed all corresponding Auto Scaling lifecycle event hooks from the Amazon Web Services account. If the output contains data, CodeDeploy could not remove some Auto Scaling lifecycle event hooks from the Amazon Web Services account.

(structure)

Information about an Auto Scaling group.

name -> (string)

The Auto Scaling group name.

hook -> (string)

The name of the launch hook that CodeDeploy installed into the Auto Scaling group.

For more information about the launch hook, see [How Amazon EC2 Auto Scaling works with CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html#integrations-aws-auto-scaling-behaviors) in the *CodeDeploy User Guide* .

terminationHook -> (string)

The name of the termination hook that CodeDeploy installed into the Auto Scaling group.

For more information about the termination hook, see [Enabling termination deployments during Auto Scaling scale-in events](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html#integrations-aws-auto-scaling-behaviors-hook-enable) in the *CodeDeploy User Guide* .