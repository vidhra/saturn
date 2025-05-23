# update-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# update-cluster

## Description

Updates a SageMaker HyperPod cluster.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateCluster)

## Synopsis

```
update-cluster
--cluster-name <value>
--instance-groups <value>
[--node-recovery <value>]
[--instance-groups-to-delete <value>]
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

Specify the name of the SageMaker HyperPod cluster you want to update.

`--instance-groups` (list)

Specify the instance groups to update.

(structure)

The specifications of an instance group that you need to define.

InstanceCount -> (integer)

Specifies the number of instances to add to the instance group of a SageMaker HyperPod cluster.

InstanceGroupName -> (string)

Specifies the name of the instance group.

InstanceType -> (string)

Specifies the instance type of the instance group.

LifeCycleConfig -> (structure)

Specifies the LifeCycle configuration for the instance group.

SourceS3Uri -> (string)

An Amazon S3 bucket path where your lifecycle scripts are stored.

### Warning

Make sure that the S3 bucket path starts with `s3://sagemaker-` . The [IAM role for SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod) has the managed ` `AmazonSageMakerClusterInstanceRolePolicy` [https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-cluster).html`__ attached, which allows access to S3 buckets with the specific prefix `sagemaker-` .

OnCreate -> (string)

The file name of the entrypoint script of lifecycle scripts under `SourceS3Uri` . This entrypoint script runs during cluster creation.

ExecutionRole -> (string)

Specifies an IAM execution role to be assumed by the instance group.

ThreadsPerCore -> (integer)

Specifies the value for **Threads per core** . For instance types that support multithreading, you can specify `1` for disabling multithreading and `2` for enabling multithreading. For instance types that doesnât support multithreading, specify `1` . For more information, see the reference table of [CPU cores and threads per CPU core per instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.html) in the *Amazon Elastic Compute Cloud User Guide* .

InstanceStorageConfigs -> (list)

Specifies the additional storage configurations for the instances in the SageMaker HyperPod cluster instance group.

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

TrainingPlanArn -> (string)

The Amazon Resource Name (ARN); of the training plan to use for this cluster instance group.

For more information about how to reserve GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see `` [CreateTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html) `` .

OverrideVpcConfig -> (structure)

To configure multi-AZ deployments, customize the Amazon VPC configuration at the instance group level. You can specify different subnets and security groups across different AZs in the instance group specification to override a SageMaker HyperPod clusterâs default Amazon VPC configuration. For more information about deploying a cluster in multiple AZs, see [Setting up SageMaker HyperPod clusters across multiple AZs](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html#sagemaker-hyperpod-prerequisites-multiple-availability-zones) .

### Note

When your Amazon VPC and subnets support IPv6, network communications differ based on the cluster orchestration platform:

- Slurm-orchestrated clusters automatically configure nodes with dual IPv6 and IPv4 addresses, allowing immediate IPv6 network communications.
- In Amazon EKS-orchestrated clusters, nodes receive dual-stack addressing, but pods can only use IPv6 when the Amazon EKS cluster is explicitly IPv6-enabled. For information about deploying an IPv6 Amazon EKS cluster, see [Amazon EKS IPv6 Cluster Deployment](https://docs.aws.amazon.com/eks/latest/userguide/deploy-ipv6-cluster.html#_deploy_an_ipv6_cluster_with_eksctl) .

Additional resources for IPv6 configuration:

- For information about adding IPv6 support to your VPC, see to [IPv6 Support for VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6.html) .
- For information about creating a new IPv6-compatible VPC, see [Amazon VPC Creation Guide](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html) .
- To configure SageMaker HyperPod with a custom Amazon VPC, see [Custom Amazon VPC Setup for SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html#sagemaker-hyperpod-prerequisites-optional-vpc) .

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

ScheduledUpdateConfig -> (structure)

The configuration object of the schedule that SageMaker uses to update the AMI.

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

JSON Syntax:

```
[
  {
    "InstanceCount": integer,
    "InstanceGroupName": "string",
    "InstanceType": "ml.p4d.24xlarge"|"ml.p4de.24xlarge"|"ml.p5.48xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.12xlarge"|"ml.g5.16xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.c5.large"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.12xlarge"|"ml.c5.18xlarge"|"ml.c5.24xlarge"|"ml.c5n.large"|"ml.c5n.2xlarge"|"ml.c5n.4xlarge"|"ml.c5n.9xlarge"|"ml.c5n.18xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.8xlarge"|"ml.m5.12xlarge"|"ml.m5.16xlarge"|"ml.m5.24xlarge"|"ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.16xlarge"|"ml.g6.12xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.gr6.4xlarge"|"ml.gr6.8xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.16xlarge"|"ml.g6e.12xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.p5e.48xlarge"|"ml.p5en.48xlarge"|"ml.trn2.48xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.i3en.large"|"ml.i3en.xlarge"|"ml.i3en.2xlarge"|"ml.i3en.3xlarge"|"ml.i3en.6xlarge"|"ml.i3en.12xlarge"|"ml.i3en.24xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge",
    "LifeCycleConfig": {
      "SourceS3Uri": "string",
      "OnCreate": "string"
    },
    "ExecutionRole": "string",
    "ThreadsPerCore": integer,
    "InstanceStorageConfigs": [
      {
        "EbsVolumeConfig": {
          "VolumeSizeInGB": integer
        }
      }
      ...
    ],
    "OnStartDeepHealthChecks": ["InstanceStress"|"InstanceConnectivity", ...],
    "TrainingPlanArn": "string",
    "OverrideVpcConfig": {
      "SecurityGroupIds": ["string", ...],
      "Subnets": ["string", ...]
    },
    "ScheduledUpdateConfig": {
      "ScheduleExpression": "string",
      "DeploymentConfig": {
        "RollingUpdatePolicy": {
          "MaximumBatchSize": {
            "Type": "INSTANCE_COUNT"|"CAPACITY_PERCENTAGE",
            "Value": integer
          },
          "RollbackMaximumBatchSize": {
            "Type": "INSTANCE_COUNT"|"CAPACITY_PERCENTAGE",
            "Value": integer
          }
        },
        "WaitIntervalInSeconds": integer,
        "AutoRollbackConfiguration": [
          {
            "AlarmName": "string"
          }
          ...
        ]
      }
    }
  }
  ...
]
```

`--node-recovery` (string)

The node recovery mode to be applied to the SageMaker HyperPod cluster.

Possible values:

- `Automatic`
- `None`

`--instance-groups-to-delete` (list)

Specify the names of the instance groups to delete. Use a single `,` as the separator between multiple names.

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

## Output

ClusterArn -> (string)

The Amazon Resource Name (ARN) of the updated SageMaker HyperPod cluster.