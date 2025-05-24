# describe-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# describe-cluster

## Description

Retrieves information of a SageMaker HyperPod cluster.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeCluster)

## Synopsis

```
describe-cluster
--cluster-name <value>
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

`--cluster-name` (string)

The string name or the Amazon Resource Name (ARN) of the SageMaker HyperPod cluster.

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

ClusterArn -> (string)

The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster.

ClusterName -> (string)

The name of the SageMaker HyperPod cluster.

ClusterStatus -> (string)

The status of the SageMaker HyperPod cluster.

CreationTime -> (timestamp)

The time when the SageMaker Cluster is created.

FailureMessage -> (string)

The failure message of the SageMaker HyperPod cluster.

InstanceGroups -> (list)

The instance groups of the SageMaker HyperPod cluster.

(structure)

Details of an instance group in a SageMaker HyperPod cluster.

CurrentCount -> (integer)

The number of instances that are currently in the instance group of a SageMaker HyperPod cluster.

TargetCount -> (integer)

The number of instances you specified to add to the instance group of a SageMaker HyperPod cluster.

InstanceGroupName -> (string)

The name of the instance group of a SageMaker HyperPod cluster.

InstanceType -> (string)

The instance type of the instance group of a SageMaker HyperPod cluster.

LifeCycleConfig -> (structure)

Details of LifeCycle configuration for the instance group.

SourceS3Uri -> (string)

An Amazon S3 bucket path where your lifecycle scripts are stored.

### Warning

Make sure that the S3 bucket path starts with `s3://sagemaker-` . The [IAM role for SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod) has the managed ` `AmazonSageMakerClusterInstanceRolePolicy` [https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-cluster).html`__ attached, which allows access to S3 buckets with the specific prefix `sagemaker-` .

OnCreate -> (string)

The file name of the entrypoint script of lifecycle scripts under `SourceS3Uri` . This entrypoint script runs during cluster creation.

ExecutionRole -> (string)

The execution role for the instance group to assume.

ThreadsPerCore -> (integer)

The number you specified to `TreadsPerCore` in `CreateCluster` for enabling or disabling multithreading. For instance types that support multithreading, you can specify 1 for disabling multithreading and 2 for enabling multithreading. For more information, see the reference table of [CPU cores and threads per CPU core per instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.html) in the *Amazon Elastic Compute Cloud User Guide* .

InstanceStorageConfigs -> (list)

The additional storage configurations for the instances in the SageMaker HyperPod cluster instance group.

(tagged union structure)

Defines the configuration for attaching additional storage to the instances in the SageMaker HyperPod cluster instance group. To learn more, see [SageMaker HyperPod release notes: June 20, 2024](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-release-notes.html#sagemaker-hyperpod-release-notes-20240620) .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `EbsVolumeConfig`.

EbsVolumeConfig -> (structure)

Defines the configuration for attaching additional Amazon Elastic Block Store (EBS) volumes to the instances in the SageMaker HyperPod cluster instance group. The additional EBS volume is attached to each instance within the SageMaker HyperPod cluster instance group and mounted to `/opt/sagemaker` .

VolumeSizeInGB -> (integer)

The size in gigabytes (GB) of the additional EBS volume to be attached to the instances in the SageMaker HyperPod cluster instance group. The additional EBS volume is attached to each instance within the SageMaker HyperPod cluster instance group and mounted to `/opt/sagemaker` .

OnStartDeepHealthChecks -> (list)

A flag indicating whether deep health checks should be performed when the cluster instance group is created or updated.

(string)

Status -> (string)

The current status of the cluster instance group.

- `InService` : The instance group is active and healthy.
- `Creating` : The instance group is being provisioned.
- `Updating` : The instance group is being updated.
- `Failed` : The instance group has failed to provision or is no longer healthy.
- `Degraded` : The instance group is degraded, meaning that some instances have failed to provision or are no longer healthy.
- `Deleting` : The instance group is being deleted.

TrainingPlanArn -> (string)

The Amazon Resource Name (ARN); of the training plan associated with this cluster instance group.

For more information about how to reserve GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see `` [CreateTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html) `` .

TrainingPlanStatus -> (string)

The current status of the training plan associated with this cluster instance group.

OverrideVpcConfig -> (structure)

The customized Amazon VPC configuration at the instance group level that overrides the default Amazon VPC configuration of the SageMaker HyperPod cluster.

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

ScheduledUpdateConfig -> (structure)

The configuration object of the schedule that SageMaker follows when updating the AMI.

ScheduleExpression -> (string)

A cron expression that specifies the schedule that SageMaker follows when updating the AMI.

DeploymentConfig -> (structure)

The configuration to use when updating the AMI versions.

RollingUpdatePolicy -> (structure)

The policy that SageMaker uses when updating the AMI versions of the cluster.

MaximumBatchSize -> (structure)

The maximum amount of instances in the cluster that SageMaker can update at a time.

Type -> (string)

Specifies whether SageMaker should process the update by amount or percentage of instances.

Value -> (integer)

Specifies the amount or percentage of instances SageMaker updates at a time.

RollbackMaximumBatchSize -> (structure)

The maximum amount of instances in the cluster that SageMaker can roll back at a time.

Type -> (string)

Specifies whether SageMaker should process the update by amount or percentage of instances.

Value -> (integer)

Specifies the amount or percentage of instances SageMaker updates at a time.

WaitIntervalInSeconds -> (integer)

The duration in seconds that SageMaker waits before updating more instances in the cluster.

AutoRollbackConfiguration -> (list)

An array that contains the alarms that SageMaker monitors to know whether to roll back the AMI update.

(structure)

The details of the alarm to monitor during the AMI update.

AlarmName -> (string)

The name of the alarm.

VpcConfig -> (structure)

Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html) .

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

Orchestrator -> (structure)

The type of orchestrator used for the SageMaker HyperPod cluster.

Eks -> (structure)

The Amazon EKS cluster used as the orchestrator for the SageMaker HyperPod cluster.

ClusterArn -> (string)

The Amazon Resource Name (ARN) of the Amazon EKS cluster associated with the SageMaker HyperPod cluster.

NodeRecovery -> (string)

The node recovery mode configured for the SageMaker HyperPod cluster.