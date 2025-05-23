# describe-cluster-nodeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-cluster-node.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-cluster-node.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# describe-cluster-node

## Description

Retrieves information of a node (also called a *instance* interchangeably) of a SageMaker HyperPod cluster.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeClusterNode)

## Synopsis

```
describe-cluster-node
--cluster-name <value>
--node-id <value>
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

The string name or the Amazon Resource Name (ARN) of the SageMaker HyperPod cluster in which the node is.

`--node-id` (string)

The ID of the SageMaker HyperPod cluster node.

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

NodeDetails -> (structure)

The details of the SageMaker HyperPod cluster node.

InstanceGroupName -> (string)

The instance group name in which the instance is.

InstanceId -> (string)

The ID of the instance.

InstanceStatus -> (structure)

The status of the instance.

Status -> (string)

The status of an instance in a SageMaker HyperPod cluster.

Message -> (string)

The message from an instance in a SageMaker HyperPod cluster.

InstanceType -> (string)

The type of the instance.

LaunchTime -> (timestamp)

The time when the instance is launched.

LastSoftwareUpdateTime -> (timestamp)

The time when the cluster was last updated.

LifeCycleConfig -> (structure)

The LifeCycle configuration applied to the instance.

SourceS3Uri -> (string)

An Amazon S3 bucket path where your lifecycle scripts are stored.

### Warning

Make sure that the S3 bucket path starts with `s3://sagemaker-` . The [IAM role for SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod) has the managed ` `AmazonSageMakerClusterInstanceRolePolicy` [https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-cluster).html`__ attached, which allows access to S3 buckets with the specific prefix `sagemaker-` .

OnCreate -> (string)

The file name of the entrypoint script of lifecycle scripts under `SourceS3Uri` . This entrypoint script runs during cluster creation.

OverrideVpcConfig -> (structure)

The customized Amazon VPC configuration at the instance group level that overrides the default Amazon VPC configuration of the SageMaker HyperPod cluster.

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

ThreadsPerCore -> (integer)

The number of threads per CPU core you specified under `CreateCluster` .

InstanceStorageConfigs -> (list)

The configurations of additional storage specified to the instance group where the instance (node) is launched.

(tagged union structure)

Defines the configuration for attaching additional storage to the instances in the SageMaker HyperPod cluster instance group. To learn more, see [SageMaker HyperPod release notes: June 20, 2024](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-release-notes.html#sagemaker-hyperpod-release-notes-20240620) .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `EbsVolumeConfig`.

EbsVolumeConfig -> (structure)

Defines the configuration for attaching additional Amazon Elastic Block Store (EBS) volumes to the instances in the SageMaker HyperPod cluster instance group. The additional EBS volume is attached to each instance within the SageMaker HyperPod cluster instance group and mounted to `/opt/sagemaker` .

VolumeSizeInGB -> (integer)

The size in gigabytes (GB) of the additional EBS volume to be attached to the instances in the SageMaker HyperPod cluster instance group. The additional EBS volume is attached to each instance within the SageMaker HyperPod cluster instance group and mounted to `/opt/sagemaker` .

PrivatePrimaryIp -> (string)

The private primary IP address of the SageMaker HyperPod cluster node.

PrivatePrimaryIpv6 -> (string)

The private primary IPv6 address of the SageMaker HyperPod cluster node when configured with an Amazon VPC that supports IPv6 and includes subnets with IPv6 addressing enabled in either the cluster Amazon VPC configuration or the instance group Amazon VPC configuration.

PrivateDnsHostname -> (string)

The private DNS hostname of the SageMaker HyperPod cluster node.

Placement -> (structure)

The placement details of the SageMaker HyperPod cluster node.

AvailabilityZone -> (string)

The Availability Zone where the node in the SageMaker HyperPod cluster is launched.

AvailabilityZoneId -> (string)

The unique identifier (ID) of the Availability Zone where the node in the SageMaker HyperPod cluster is launched.