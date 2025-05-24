# run-instancesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-instances.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-instances.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# run-instances

## Description

Launches the specified number of instances using an AMI for which you have permissions.

You can specify a number of options, or leave the default options. The following rules apply:

- If you donât specify a subnet ID, we choose a default subnet from your default VPC for you. If you donât have a default VPC, you must specify a subnet ID in the request.
- All instances have a network interface with a primary private IPv4 address. If you donât specify this address, we choose one from the IPv4 range of your subnet.
- Not all instance types support IPv6 addresses. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) .
- If you donât specify a security group ID, we use the default security group for the VPC. For more information, see [Security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html) .
- If any of the AMIs have a product code attached for which the user has not subscribed, the request fails.

You can create a [launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) , which is a resource that contains the parameters to launch an instance. When you launch an instance using  RunInstances , you can specify the launch template instead of specifying the launch parameters.

To ensure faster instance launches, break up large requests into smaller batches. For example, create five separate launch requests for 100 instances each instead of one launch request for 500 instances.

`RunInstances` is subject to both request rate limiting and resource rate limiting. For more information, see [Request throttling](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-throttling.html) .

An instance is ready for you to use when itâs in the `running` state. You can check the state of your instance using  DescribeInstances . You can tag instances and EBS volumes during launch, after launch, or both. For more information, see  CreateTags and [Tagging your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) .

Linux instances have access to the public key of the key pair at boot. You can use this key to provide secure access to the instance. Amazon EC2 public images use this feature to provide secure access without passwords. For more information, see [Key pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) .

For troubleshooting, see [What to do if an instance immediately terminates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_InstanceStraightToTerminated.html) , and [Troubleshooting connecting to your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/RunInstances)

## Synopsis

```
run-instances
[--block-device-mappings <value>]
[--image-id <value>]
[--instance-type <value>]
[--ipv6-address-count <value>]
[--ipv6-addresses <value>]
[--kernel-id <value>]
[--key-name <value>]
[--monitoring <value>]
[--placement <value>]
[--ramdisk-id <value>]
[--security-group-ids <value>]
[--security-groups <value>]
[--subnet-id <value>]
[--user-data <value>]
[--elastic-gpu-specification <value>]
[--elastic-inference-accelerators <value>]
[--tag-specifications <value>]
[--launch-template <value>]
[--instance-market-options <value>]
[--credit-specification <value>]
[--cpu-options <value>]
[--capacity-reservation-specification <value>]
[--hibernation-options <value>]
[--license-specifications <value>]
[--metadata-options <value>]
[--enclave-options <value>]
[--private-dns-name-options <value>]
[--maintenance-options <value>]
[--disable-api-stop | --no-disable-api-stop]
[--enable-primary-ipv6 | --no-enable-primary-ipv6]
[--network-performance-options <value>]
[--operator <value>]
[--dry-run | --no-dry-run]
[--disable-api-termination | --enable-api-termination]
[--instance-initiated-shutdown-behavior <value>]
[--private-ip-address <value>]
[--client-token <value>]
[--additional-info <value>]
[--network-interfaces <value>]
[--iam-instance-profile <value>]
[--ebs-optimized | --no-ebs-optimized]
[--count <value>]
[--secondary-private-ip-addresses <value>]
[--secondary-private-ip-address-count <value>]
[--associate-public-ip-address | --no-associate-public-ip-address]
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

`--block-device-mappings` (list)

The block device mapping, which defines the EBS volumes and instance store volumes to attach to the instance at launch. For more information, see [Block device mappings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html) in the *Amazon EC2 User Guide* .

(structure)

Describes a block device mapping, which defines the EBS volumes and instance store volumes to attach to an instance at launch.

Ebs -> (structure)

Parameters used to automatically set up EBS volumes when the instance is launched.

DeleteOnTermination -> (boolean)

Indicates whether the EBS volume is deleted on instance termination. For more information, see [Preserving Amazon EBS volumes on instance termination](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#preserving-volumes-on-termination) in the *Amazon EC2 User Guide* .

Iops -> (integer)

The number of I/O operations per second (IOPS). For `gp3` , `io1` , and `io2` volumes, this represents the number of IOPS that are provisioned for the volume. For `gp2` volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.

The following are the supported values for each volume type:

- `gp3` : 3,000 - 16,000 IOPS
- `io1` : 100 - 64,000 IOPS
- `io2` : 100 - 256,000 IOPS

For `io2` volumes, you can achieve up to 256,000 IOPS on [instances built on the Nitro System](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances) . On other instances, you can achieve performance up to 32,000 IOPS.

This parameter is required for `io1` and `io2` volumes. The default for `gp3` volumes is 3,000 IOPS.

SnapshotId -> (string)

The ID of the snapshot.

VolumeSize -> (integer)

The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size. If you specify a snapshot, the default is the snapshot size. You can specify a volume size that is equal to or larger than the snapshot size.

The following are the supported sizes for each volume type:

- `gp2` and `gp3` : 1 - 16,384 GiB
- `io1` : 4 - 16,384 GiB
- `io2` : 4 - 65,536 GiB
- `st1` and `sc1` : 125 - 16,384 GiB
- `standard` : 1 - 1024 GiB

VolumeType -> (string)

The volume type. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) in the *Amazon EBS User Guide* .

KmsKeyId -> (string)

Identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed KMS key to use for EBS encryption.

This parameter is only supported on `BlockDeviceMapping` objects called by [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) , [RequestSpotFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet.html) , and [RequestSpotInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html) .

Throughput -> (integer)

The throughput that the volume supports, in MiB/s.

This parameter is valid only for `gp3` volumes.

Valid Range: Minimum value of 125. Maximum value of 1000.

OutpostArn -> (string)

The ARN of the Outpost on which the snapshot is stored.

This parameter is not supported when using [CreateImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html) .

Encrypted -> (boolean)

Indicates whether the encryption state of an EBS volume is changed while being restored from a backing snapshot. The effect of setting the encryption state to `true` depends on the volume origin (new or from a snapshot), starting encryption state, ownership, and whether encryption by default is enabled. For more information, see [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html#encryption-parameters) in the *Amazon EBS User Guide* .

In no case can you remove encryption from an encrypted volume.

Encrypted volumes can only be attached to instances that support Amazon EBS encryption. For more information, see [Supported instance types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption-requirements.html#ebs-encryption_supported_instances) .

This parameter is not returned by  DescribeImageAttribute .

For  CreateImage and  RegisterImage , whether you can include this parameter, and the allowed values differ depending on the type of block device mapping you are creating.

- If you are creating a block device mapping for a **new (empty) volume** , you can include this parameter, and specify either `true` for an encrypted volume, or `false` for an unencrypted volume. If you omit this parameter, it defaults to `false` (unencrypted).
- If you are creating a block device mapping from an **existing encrypted or unencrypted snapshot** , you must omit this parameter. If you include this parameter, the request will fail, regardless of the value that you specify.
- If you are creating a block device mapping from an **existing unencrypted volume** , you can include this parameter, but you must specify `false` . If you specify `true` , the request will fail. In this case, we recommend that you omit the parameter.
- If you are creating a block device mapping from an **existing encrypted volume** , you can include this parameter, and specify either `true` or `false` . However, if you specify `false` , the parameter is ignored and the block device mapping is always encrypted. In this case, we recommend that you omit the parameter.

VolumeInitializationRate -> (integer)

Specifies the Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate), in MiB/s, at which to download the snapshot blocks from Amazon S3 to the volume. This is also known as *volume initialization* . Specifying a volume initialization rate ensures that the volume is initialized at a predictable and consistent rate after creation.

This parameter is supported only for volumes created from snapshots. Omit this parameter if:

- You want to create the volume using fast snapshot restore. You must specify a snapshot that is enabled for fast snapshot restore. In this case, the volume is fully initialized at creation.

### Note

If you specify a snapshot that is enabled for fast snapshot restore and a volume initialization rate, the volume will be initialized at the specified rate instead of fast snapshot restore.

- You want to create a volume that is initialized at the default rate.

For more information, see [Initialize Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html) in the *Amazon EC2 User Guide* .

This parameter is not supported when using [CreateImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html) .

Valid range: 100 - 300 MiB/s

NoDevice -> (string)

To omit the device from the block device mapping, specify an empty string. When this property is specified, the device is removed from the block device mapping regardless of the assigned value.

DeviceName -> (string)

The device name (for example, `/dev/sdh` or `xvdh` ).

VirtualName -> (string)

The virtual device name (`ephemeral` N). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for `ephemeral0` and `ephemeral1` . The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.

NVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect.

Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.

Shorthand Syntax:

```
Ebs={DeleteOnTermination=boolean,Iops=integer,SnapshotId=string,VolumeSize=integer,VolumeType=string,KmsKeyId=string,Throughput=integer,OutpostArn=string,Encrypted=boolean,VolumeInitializationRate=integer},NoDevice=string,DeviceName=string,VirtualName=string ...
```

JSON Syntax:

```
[
  {
    "Ebs": {
      "DeleteOnTermination": true|false,
      "Iops": integer,
      "SnapshotId": "string",
      "VolumeSize": integer,
      "VolumeType": "standard"|"io1"|"io2"|"gp2"|"sc1"|"st1"|"gp3",
      "KmsKeyId": "string",
      "Throughput": integer,
      "OutpostArn": "string",
      "Encrypted": true|false,
      "VolumeInitializationRate": integer
    },
    "NoDevice": "string",
    "DeviceName": "string",
    "VirtualName": "string"
  }
  ...
]
```

`--image-id` (string)

The ID of the AMI. An AMI ID is required to launch an instance and must be specified here or in a launch template.

`--instance-type` (string)

The instance type. For more information, see [Amazon EC2 instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide* .

Possible values:

- `a1.medium`
- `a1.large`
- `a1.xlarge`
- `a1.2xlarge`
- `a1.4xlarge`
- `a1.metal`
- `c1.medium`
- `c1.xlarge`
- `c3.large`
- `c3.xlarge`
- `c3.2xlarge`
- `c3.4xlarge`
- `c3.8xlarge`
- `c4.large`
- `c4.xlarge`
- `c4.2xlarge`
- `c4.4xlarge`
- `c4.8xlarge`
- `c5.large`
- `c5.xlarge`
- `c5.2xlarge`
- `c5.4xlarge`
- `c5.9xlarge`
- `c5.12xlarge`
- `c5.18xlarge`
- `c5.24xlarge`
- `c5.metal`
- `c5a.large`
- `c5a.xlarge`
- `c5a.2xlarge`
- `c5a.4xlarge`
- `c5a.8xlarge`
- `c5a.12xlarge`
- `c5a.16xlarge`
- `c5a.24xlarge`
- `c5ad.large`
- `c5ad.xlarge`
- `c5ad.2xlarge`
- `c5ad.4xlarge`
- `c5ad.8xlarge`
- `c5ad.12xlarge`
- `c5ad.16xlarge`
- `c5ad.24xlarge`
- `c5d.large`
- `c5d.xlarge`
- `c5d.2xlarge`
- `c5d.4xlarge`
- `c5d.9xlarge`
- `c5d.12xlarge`
- `c5d.18xlarge`
- `c5d.24xlarge`
- `c5d.metal`
- `c5n.large`
- `c5n.xlarge`
- `c5n.2xlarge`
- `c5n.4xlarge`
- `c5n.9xlarge`
- `c5n.18xlarge`
- `c5n.metal`
- `c6g.medium`
- `c6g.large`
- `c6g.xlarge`
- `c6g.2xlarge`
- `c6g.4xlarge`
- `c6g.8xlarge`
- `c6g.12xlarge`
- `c6g.16xlarge`
- `c6g.metal`
- `c6gd.medium`
- `c6gd.large`
- `c6gd.xlarge`
- `c6gd.2xlarge`
- `c6gd.4xlarge`
- `c6gd.8xlarge`
- `c6gd.12xlarge`
- `c6gd.16xlarge`
- `c6gd.metal`
- `c6gn.medium`
- `c6gn.large`
- `c6gn.xlarge`
- `c6gn.2xlarge`
- `c6gn.4xlarge`
- `c6gn.8xlarge`
- `c6gn.12xlarge`
- `c6gn.16xlarge`
- `c6i.large`
- `c6i.xlarge`
- `c6i.2xlarge`
- `c6i.4xlarge`
- `c6i.8xlarge`
- `c6i.12xlarge`
- `c6i.16xlarge`
- `c6i.24xlarge`
- `c6i.32xlarge`
- `c6i.metal`
- `cc1.4xlarge`
- `cc2.8xlarge`
- `cg1.4xlarge`
- `cr1.8xlarge`
- `d2.xlarge`
- `d2.2xlarge`
- `d2.4xlarge`
- `d2.8xlarge`
- `d3.xlarge`
- `d3.2xlarge`
- `d3.4xlarge`
- `d3.8xlarge`
- `d3en.xlarge`
- `d3en.2xlarge`
- `d3en.4xlarge`
- `d3en.6xlarge`
- `d3en.8xlarge`
- `d3en.12xlarge`
- `dl1.24xlarge`
- `f1.2xlarge`
- `f1.4xlarge`
- `f1.16xlarge`
- `g2.2xlarge`
- `g2.8xlarge`
- `g3.4xlarge`
- `g3.8xlarge`
- `g3.16xlarge`
- `g3s.xlarge`
- `g4ad.xlarge`
- `g4ad.2xlarge`
- `g4ad.4xlarge`
- `g4ad.8xlarge`
- `g4ad.16xlarge`
- `g4dn.xlarge`
- `g4dn.2xlarge`
- `g4dn.4xlarge`
- `g4dn.8xlarge`
- `g4dn.12xlarge`
- `g4dn.16xlarge`
- `g4dn.metal`
- `g5.xlarge`
- `g5.2xlarge`
- `g5.4xlarge`
- `g5.8xlarge`
- `g5.12xlarge`
- `g5.16xlarge`
- `g5.24xlarge`
- `g5.48xlarge`
- `g5g.xlarge`
- `g5g.2xlarge`
- `g5g.4xlarge`
- `g5g.8xlarge`
- `g5g.16xlarge`
- `g5g.metal`
- `hi1.4xlarge`
- `hpc6a.48xlarge`
- `hs1.8xlarge`
- `h1.2xlarge`
- `h1.4xlarge`
- `h1.8xlarge`
- `h1.16xlarge`
- `i2.xlarge`
- `i2.2xlarge`
- `i2.4xlarge`
- `i2.8xlarge`
- `i3.large`
- `i3.xlarge`
- `i3.2xlarge`
- `i3.4xlarge`
- `i3.8xlarge`
- `i3.16xlarge`
- `i3.metal`
- `i3en.large`
- `i3en.xlarge`
- `i3en.2xlarge`
- `i3en.3xlarge`
- `i3en.6xlarge`
- `i3en.12xlarge`
- `i3en.24xlarge`
- `i3en.metal`
- `im4gn.large`
- `im4gn.xlarge`
- `im4gn.2xlarge`
- `im4gn.4xlarge`
- `im4gn.8xlarge`
- `im4gn.16xlarge`
- `inf1.xlarge`
- `inf1.2xlarge`
- `inf1.6xlarge`
- `inf1.24xlarge`
- `is4gen.medium`
- `is4gen.large`
- `is4gen.xlarge`
- `is4gen.2xlarge`
- `is4gen.4xlarge`
- `is4gen.8xlarge`
- `m1.small`
- `m1.medium`
- `m1.large`
- `m1.xlarge`
- `m2.xlarge`
- `m2.2xlarge`
- `m2.4xlarge`
- `m3.medium`
- `m3.large`
- `m3.xlarge`
- `m3.2xlarge`
- `m4.large`
- `m4.xlarge`
- `m4.2xlarge`
- `m4.4xlarge`
- `m4.10xlarge`
- `m4.16xlarge`
- `m5.large`
- `m5.xlarge`
- `m5.2xlarge`
- `m5.4xlarge`
- `m5.8xlarge`
- `m5.12xlarge`
- `m5.16xlarge`
- `m5.24xlarge`
- `m5.metal`
- `m5a.large`
- `m5a.xlarge`
- `m5a.2xlarge`
- `m5a.4xlarge`
- `m5a.8xlarge`
- `m5a.12xlarge`
- `m5a.16xlarge`
- `m5a.24xlarge`
- `m5ad.large`
- `m5ad.xlarge`
- `m5ad.2xlarge`
- `m5ad.4xlarge`
- `m5ad.8xlarge`
- `m5ad.12xlarge`
- `m5ad.16xlarge`
- `m5ad.24xlarge`
- `m5d.large`
- `m5d.xlarge`
- `m5d.2xlarge`
- `m5d.4xlarge`
- `m5d.8xlarge`
- `m5d.12xlarge`
- `m5d.16xlarge`
- `m5d.24xlarge`
- `m5d.metal`
- `m5dn.large`
- `m5dn.xlarge`
- `m5dn.2xlarge`
- `m5dn.4xlarge`
- `m5dn.8xlarge`
- `m5dn.12xlarge`
- `m5dn.16xlarge`
- `m5dn.24xlarge`
- `m5dn.metal`
- `m5n.large`
- `m5n.xlarge`
- `m5n.2xlarge`
- `m5n.4xlarge`
- `m5n.8xlarge`
- `m5n.12xlarge`
- `m5n.16xlarge`
- `m5n.24xlarge`
- `m5n.metal`
- `m5zn.large`
- `m5zn.xlarge`
- `m5zn.2xlarge`
- `m5zn.3xlarge`
- `m5zn.6xlarge`
- `m5zn.12xlarge`
- `m5zn.metal`
- `m6a.large`
- `m6a.xlarge`
- `m6a.2xlarge`
- `m6a.4xlarge`
- `m6a.8xlarge`
- `m6a.12xlarge`
- `m6a.16xlarge`
- `m6a.24xlarge`
- `m6a.32xlarge`
- `m6a.48xlarge`
- `m6g.metal`
- `m6g.medium`
- `m6g.large`
- `m6g.xlarge`
- `m6g.2xlarge`
- `m6g.4xlarge`
- `m6g.8xlarge`
- `m6g.12xlarge`
- `m6g.16xlarge`
- `m6gd.metal`
- `m6gd.medium`
- `m6gd.large`
- `m6gd.xlarge`
- `m6gd.2xlarge`
- `m6gd.4xlarge`
- `m6gd.8xlarge`
- `m6gd.12xlarge`
- `m6gd.16xlarge`
- `m6i.large`
- `m6i.xlarge`
- `m6i.2xlarge`
- `m6i.4xlarge`
- `m6i.8xlarge`
- `m6i.12xlarge`
- `m6i.16xlarge`
- `m6i.24xlarge`
- `m6i.32xlarge`
- `m6i.metal`
- `mac1.metal`
- `p2.xlarge`
- `p2.8xlarge`
- `p2.16xlarge`
- `p3.2xlarge`
- `p3.8xlarge`
- `p3.16xlarge`
- `p3dn.24xlarge`
- `p4d.24xlarge`
- `r3.large`
- `r3.xlarge`
- `r3.2xlarge`
- `r3.4xlarge`
- `r3.8xlarge`
- `r4.large`
- `r4.xlarge`
- `r4.2xlarge`
- `r4.4xlarge`
- `r4.8xlarge`
- `r4.16xlarge`
- `r5.large`
- `r5.xlarge`
- `r5.2xlarge`
- `r5.4xlarge`
- `r5.8xlarge`
- `r5.12xlarge`
- `r5.16xlarge`
- `r5.24xlarge`
- `r5.metal`
- `r5a.large`
- `r5a.xlarge`
- `r5a.2xlarge`
- `r5a.4xlarge`
- `r5a.8xlarge`
- `r5a.12xlarge`
- `r5a.16xlarge`
- `r5a.24xlarge`
- `r5ad.large`
- `r5ad.xlarge`
- `r5ad.2xlarge`
- `r5ad.4xlarge`
- `r5ad.8xlarge`
- `r5ad.12xlarge`
- `r5ad.16xlarge`
- `r5ad.24xlarge`
- `r5b.large`
- `r5b.xlarge`
- `r5b.2xlarge`
- `r5b.4xlarge`
- `r5b.8xlarge`
- `r5b.12xlarge`
- `r5b.16xlarge`
- `r5b.24xlarge`
- `r5b.metal`
- `r5d.large`
- `r5d.xlarge`
- `r5d.2xlarge`
- `r5d.4xlarge`
- `r5d.8xlarge`
- `r5d.12xlarge`
- `r5d.16xlarge`
- `r5d.24xlarge`
- `r5d.metal`
- `r5dn.large`
- `r5dn.xlarge`
- `r5dn.2xlarge`
- `r5dn.4xlarge`
- `r5dn.8xlarge`
- `r5dn.12xlarge`
- `r5dn.16xlarge`
- `r5dn.24xlarge`
- `r5dn.metal`
- `r5n.large`
- `r5n.xlarge`
- `r5n.2xlarge`
- `r5n.4xlarge`
- `r5n.8xlarge`
- `r5n.12xlarge`
- `r5n.16xlarge`
- `r5n.24xlarge`
- `r5n.metal`
- `r6g.medium`
- `r6g.large`
- `r6g.xlarge`
- `r6g.2xlarge`
- `r6g.4xlarge`
- `r6g.8xlarge`
- `r6g.12xlarge`
- `r6g.16xlarge`
- `r6g.metal`
- `r6gd.medium`
- `r6gd.large`
- `r6gd.xlarge`
- `r6gd.2xlarge`
- `r6gd.4xlarge`
- `r6gd.8xlarge`
- `r6gd.12xlarge`
- `r6gd.16xlarge`
- `r6gd.metal`
- `r6i.large`
- `r6i.xlarge`
- `r6i.2xlarge`
- `r6i.4xlarge`
- `r6i.8xlarge`
- `r6i.12xlarge`
- `r6i.16xlarge`
- `r6i.24xlarge`
- `r6i.32xlarge`
- `r6i.metal`
- `t1.micro`
- `t2.nano`
- `t2.micro`
- `t2.small`
- `t2.medium`
- `t2.large`
- `t2.xlarge`
- `t2.2xlarge`
- `t3.nano`
- `t3.micro`
- `t3.small`
- `t3.medium`
- `t3.large`
- `t3.xlarge`
- `t3.2xlarge`
- `t3a.nano`
- `t3a.micro`
- `t3a.small`
- `t3a.medium`
- `t3a.large`
- `t3a.xlarge`
- `t3a.2xlarge`
- `t4g.nano`
- `t4g.micro`
- `t4g.small`
- `t4g.medium`
- `t4g.large`
- `t4g.xlarge`
- `t4g.2xlarge`
- `u-6tb1.56xlarge`
- `u-6tb1.112xlarge`
- `u-9tb1.112xlarge`
- `u-12tb1.112xlarge`
- `u-6tb1.metal`
- `u-9tb1.metal`
- `u-12tb1.metal`
- `u-18tb1.metal`
- `u-24tb1.metal`
- `vt1.3xlarge`
- `vt1.6xlarge`
- `vt1.24xlarge`
- `x1.16xlarge`
- `x1.32xlarge`
- `x1e.xlarge`
- `x1e.2xlarge`
- `x1e.4xlarge`
- `x1e.8xlarge`
- `x1e.16xlarge`
- `x1e.32xlarge`
- `x2iezn.2xlarge`
- `x2iezn.4xlarge`
- `x2iezn.6xlarge`
- `x2iezn.8xlarge`
- `x2iezn.12xlarge`
- `x2iezn.metal`
- `x2gd.medium`
- `x2gd.large`
- `x2gd.xlarge`
- `x2gd.2xlarge`
- `x2gd.4xlarge`
- `x2gd.8xlarge`
- `x2gd.12xlarge`
- `x2gd.16xlarge`
- `x2gd.metal`
- `z1d.large`
- `z1d.xlarge`
- `z1d.2xlarge`
- `z1d.3xlarge`
- `z1d.6xlarge`
- `z1d.12xlarge`
- `z1d.metal`
- `x2idn.16xlarge`
- `x2idn.24xlarge`
- `x2idn.32xlarge`
- `x2iedn.xlarge`
- `x2iedn.2xlarge`
- `x2iedn.4xlarge`
- `x2iedn.8xlarge`
- `x2iedn.16xlarge`
- `x2iedn.24xlarge`
- `x2iedn.32xlarge`
- `c6a.large`
- `c6a.xlarge`
- `c6a.2xlarge`
- `c6a.4xlarge`
- `c6a.8xlarge`
- `c6a.12xlarge`
- `c6a.16xlarge`
- `c6a.24xlarge`
- `c6a.32xlarge`
- `c6a.48xlarge`
- `c6a.metal`
- `m6a.metal`
- `i4i.large`
- `i4i.xlarge`
- `i4i.2xlarge`
- `i4i.4xlarge`
- `i4i.8xlarge`
- `i4i.16xlarge`
- `i4i.32xlarge`
- `i4i.metal`
- `x2idn.metal`
- `x2iedn.metal`
- `c7g.medium`
- `c7g.large`
- `c7g.xlarge`
- `c7g.2xlarge`
- `c7g.4xlarge`
- `c7g.8xlarge`
- `c7g.12xlarge`
- `c7g.16xlarge`
- `mac2.metal`
- `c6id.large`
- `c6id.xlarge`
- `c6id.2xlarge`
- `c6id.4xlarge`
- `c6id.8xlarge`
- `c6id.12xlarge`
- `c6id.16xlarge`
- `c6id.24xlarge`
- `c6id.32xlarge`
- `c6id.metal`
- `m6id.large`
- `m6id.xlarge`
- `m6id.2xlarge`
- `m6id.4xlarge`
- `m6id.8xlarge`
- `m6id.12xlarge`
- `m6id.16xlarge`
- `m6id.24xlarge`
- `m6id.32xlarge`
- `m6id.metal`
- `r6id.large`
- `r6id.xlarge`
- `r6id.2xlarge`
- `r6id.4xlarge`
- `r6id.8xlarge`
- `r6id.12xlarge`
- `r6id.16xlarge`
- `r6id.24xlarge`
- `r6id.32xlarge`
- `r6id.metal`
- `r6a.large`
- `r6a.xlarge`
- `r6a.2xlarge`
- `r6a.4xlarge`
- `r6a.8xlarge`
- `r6a.12xlarge`
- `r6a.16xlarge`
- `r6a.24xlarge`
- `r6a.32xlarge`
- `r6a.48xlarge`
- `r6a.metal`
- `p4de.24xlarge`
- `u-3tb1.56xlarge`
- `u-18tb1.112xlarge`
- `u-24tb1.112xlarge`
- `trn1.2xlarge`
- `trn1.32xlarge`
- `hpc6id.32xlarge`
- `c6in.large`
- `c6in.xlarge`
- `c6in.2xlarge`
- `c6in.4xlarge`
- `c6in.8xlarge`
- `c6in.12xlarge`
- `c6in.16xlarge`
- `c6in.24xlarge`
- `c6in.32xlarge`
- `m6in.large`
- `m6in.xlarge`
- `m6in.2xlarge`
- `m6in.4xlarge`
- `m6in.8xlarge`
- `m6in.12xlarge`
- `m6in.16xlarge`
- `m6in.24xlarge`
- `m6in.32xlarge`
- `m6idn.large`
- `m6idn.xlarge`
- `m6idn.2xlarge`
- `m6idn.4xlarge`
- `m6idn.8xlarge`
- `m6idn.12xlarge`
- `m6idn.16xlarge`
- `m6idn.24xlarge`
- `m6idn.32xlarge`
- `r6in.large`
- `r6in.xlarge`
- `r6in.2xlarge`
- `r6in.4xlarge`
- `r6in.8xlarge`
- `r6in.12xlarge`
- `r6in.16xlarge`
- `r6in.24xlarge`
- `r6in.32xlarge`
- `r6idn.large`
- `r6idn.xlarge`
- `r6idn.2xlarge`
- `r6idn.4xlarge`
- `r6idn.8xlarge`
- `r6idn.12xlarge`
- `r6idn.16xlarge`
- `r6idn.24xlarge`
- `r6idn.32xlarge`
- `c7g.metal`
- `m7g.medium`
- `m7g.large`
- `m7g.xlarge`
- `m7g.2xlarge`
- `m7g.4xlarge`
- `m7g.8xlarge`
- `m7g.12xlarge`
- `m7g.16xlarge`
- `m7g.metal`
- `r7g.medium`
- `r7g.large`
- `r7g.xlarge`
- `r7g.2xlarge`
- `r7g.4xlarge`
- `r7g.8xlarge`
- `r7g.12xlarge`
- `r7g.16xlarge`
- `r7g.metal`
- `c6in.metal`
- `m6in.metal`
- `m6idn.metal`
- `r6in.metal`
- `r6idn.metal`
- `inf2.xlarge`
- `inf2.8xlarge`
- `inf2.24xlarge`
- `inf2.48xlarge`
- `trn1n.32xlarge`
- `i4g.large`
- `i4g.xlarge`
- `i4g.2xlarge`
- `i4g.4xlarge`
- `i4g.8xlarge`
- `i4g.16xlarge`
- `hpc7g.4xlarge`
- `hpc7g.8xlarge`
- `hpc7g.16xlarge`
- `c7gn.medium`
- `c7gn.large`
- `c7gn.xlarge`
- `c7gn.2xlarge`
- `c7gn.4xlarge`
- `c7gn.8xlarge`
- `c7gn.12xlarge`
- `c7gn.16xlarge`
- `p5.48xlarge`
- `m7i.large`
- `m7i.xlarge`
- `m7i.2xlarge`
- `m7i.4xlarge`
- `m7i.8xlarge`
- `m7i.12xlarge`
- `m7i.16xlarge`
- `m7i.24xlarge`
- `m7i.48xlarge`
- `m7i-flex.large`
- `m7i-flex.xlarge`
- `m7i-flex.2xlarge`
- `m7i-flex.4xlarge`
- `m7i-flex.8xlarge`
- `m7a.medium`
- `m7a.large`
- `m7a.xlarge`
- `m7a.2xlarge`
- `m7a.4xlarge`
- `m7a.8xlarge`
- `m7a.12xlarge`
- `m7a.16xlarge`
- `m7a.24xlarge`
- `m7a.32xlarge`
- `m7a.48xlarge`
- `m7a.metal-48xl`
- `hpc7a.12xlarge`
- `hpc7a.24xlarge`
- `hpc7a.48xlarge`
- `hpc7a.96xlarge`
- `c7gd.medium`
- `c7gd.large`
- `c7gd.xlarge`
- `c7gd.2xlarge`
- `c7gd.4xlarge`
- `c7gd.8xlarge`
- `c7gd.12xlarge`
- `c7gd.16xlarge`
- `m7gd.medium`
- `m7gd.large`
- `m7gd.xlarge`
- `m7gd.2xlarge`
- `m7gd.4xlarge`
- `m7gd.8xlarge`
- `m7gd.12xlarge`
- `m7gd.16xlarge`
- `r7gd.medium`
- `r7gd.large`
- `r7gd.xlarge`
- `r7gd.2xlarge`
- `r7gd.4xlarge`
- `r7gd.8xlarge`
- `r7gd.12xlarge`
- `r7gd.16xlarge`
- `r7a.medium`
- `r7a.large`
- `r7a.xlarge`
- `r7a.2xlarge`
- `r7a.4xlarge`
- `r7a.8xlarge`
- `r7a.12xlarge`
- `r7a.16xlarge`
- `r7a.24xlarge`
- `r7a.32xlarge`
- `r7a.48xlarge`
- `c7i.large`
- `c7i.xlarge`
- `c7i.2xlarge`
- `c7i.4xlarge`
- `c7i.8xlarge`
- `c7i.12xlarge`
- `c7i.16xlarge`
- `c7i.24xlarge`
- `c7i.48xlarge`
- `mac2-m2pro.metal`
- `r7iz.large`
- `r7iz.xlarge`
- `r7iz.2xlarge`
- `r7iz.4xlarge`
- `r7iz.8xlarge`
- `r7iz.12xlarge`
- `r7iz.16xlarge`
- `r7iz.32xlarge`
- `c7a.medium`
- `c7a.large`
- `c7a.xlarge`
- `c7a.2xlarge`
- `c7a.4xlarge`
- `c7a.8xlarge`
- `c7a.12xlarge`
- `c7a.16xlarge`
- `c7a.24xlarge`
- `c7a.32xlarge`
- `c7a.48xlarge`
- `c7a.metal-48xl`
- `r7a.metal-48xl`
- `r7i.large`
- `r7i.xlarge`
- `r7i.2xlarge`
- `r7i.4xlarge`
- `r7i.8xlarge`
- `r7i.12xlarge`
- `r7i.16xlarge`
- `r7i.24xlarge`
- `r7i.48xlarge`
- `dl2q.24xlarge`
- `mac2-m2.metal`
- `i4i.12xlarge`
- `i4i.24xlarge`
- `c7i.metal-24xl`
- `c7i.metal-48xl`
- `m7i.metal-24xl`
- `m7i.metal-48xl`
- `r7i.metal-24xl`
- `r7i.metal-48xl`
- `r7iz.metal-16xl`
- `r7iz.metal-32xl`
- `c7gd.metal`
- `m7gd.metal`
- `r7gd.metal`
- `g6.xlarge`
- `g6.2xlarge`
- `g6.4xlarge`
- `g6.8xlarge`
- `g6.12xlarge`
- `g6.16xlarge`
- `g6.24xlarge`
- `g6.48xlarge`
- `gr6.4xlarge`
- `gr6.8xlarge`
- `c7i-flex.large`
- `c7i-flex.xlarge`
- `c7i-flex.2xlarge`
- `c7i-flex.4xlarge`
- `c7i-flex.8xlarge`
- `u7i-12tb.224xlarge`
- `u7in-16tb.224xlarge`
- `u7in-24tb.224xlarge`
- `u7in-32tb.224xlarge`
- `u7ib-12tb.224xlarge`
- `c7gn.metal`
- `r8g.medium`
- `r8g.large`
- `r8g.xlarge`
- `r8g.2xlarge`
- `r8g.4xlarge`
- `r8g.8xlarge`
- `r8g.12xlarge`
- `r8g.16xlarge`
- `r8g.24xlarge`
- `r8g.48xlarge`
- `r8g.metal-24xl`
- `r8g.metal-48xl`
- `mac2-m1ultra.metal`
- `g6e.xlarge`
- `g6e.2xlarge`
- `g6e.4xlarge`
- `g6e.8xlarge`
- `g6e.12xlarge`
- `g6e.16xlarge`
- `g6e.24xlarge`
- `g6e.48xlarge`
- `c8g.medium`
- `c8g.large`
- `c8g.xlarge`
- `c8g.2xlarge`
- `c8g.4xlarge`
- `c8g.8xlarge`
- `c8g.12xlarge`
- `c8g.16xlarge`
- `c8g.24xlarge`
- `c8g.48xlarge`
- `c8g.metal-24xl`
- `c8g.metal-48xl`
- `m8g.medium`
- `m8g.large`
- `m8g.xlarge`
- `m8g.2xlarge`
- `m8g.4xlarge`
- `m8g.8xlarge`
- `m8g.12xlarge`
- `m8g.16xlarge`
- `m8g.24xlarge`
- `m8g.48xlarge`
- `m8g.metal-24xl`
- `m8g.metal-48xl`
- `x8g.medium`
- `x8g.large`
- `x8g.xlarge`
- `x8g.2xlarge`
- `x8g.4xlarge`
- `x8g.8xlarge`
- `x8g.12xlarge`
- `x8g.16xlarge`
- `x8g.24xlarge`
- `x8g.48xlarge`
- `x8g.metal-24xl`
- `x8g.metal-48xl`
- `i7ie.large`
- `i7ie.xlarge`
- `i7ie.2xlarge`
- `i7ie.3xlarge`
- `i7ie.6xlarge`
- `i7ie.12xlarge`
- `i7ie.18xlarge`
- `i7ie.24xlarge`
- `i7ie.48xlarge`
- `i8g.large`
- `i8g.xlarge`
- `i8g.2xlarge`
- `i8g.4xlarge`
- `i8g.8xlarge`
- `i8g.12xlarge`
- `i8g.16xlarge`
- `i8g.24xlarge`
- `i8g.metal-24xl`
- `u7i-6tb.112xlarge`
- `u7i-8tb.112xlarge`
- `u7inh-32tb.480xlarge`
- `p5e.48xlarge`
- `p5en.48xlarge`
- `f2.12xlarge`
- `f2.48xlarge`
- `trn2.48xlarge`

`--ipv6-address-count` (integer)

The number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if youâve specified a minimum number of instances to launch.

You cannot specify this option and the network interfaces option in the same request.

`--ipv6-addresses` (list)

The IPv6 addresses from the range of the subnet to associate with the primary network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if youâve specified a minimum number of instances to launch.

You cannot specify this option and the network interfaces option in the same request.

(structure)

Describes an IPv6 address.

Ipv6Address -> (string)

The IPv6 address.

IsPrimaryIpv6 -> (boolean)

Determines if an IPv6 address associated with a network interface is the primary IPv6 address. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information, see [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) .

Shorthand Syntax:

```
Ipv6Address=string,IsPrimaryIpv6=boolean ...
```

JSON Syntax:

```
[
  {
    "Ipv6Address": "string",
    "IsPrimaryIpv6": true|false
  }
  ...
]
```

`--kernel-id` (string)

The ID of the kernel.

### Warning

We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see [PV-GRUB](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedkernels.html) in the *Amazon EC2 User Guide* .

`--key-name` (string)

The name of the key pair. You can create a key pair using [CreateKeyPair](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateKeyPair.html) or [ImportKeyPair](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportKeyPair.html) .

### Warning

If you do not specify a key pair, you canât connect to the instance unless you choose an AMI that is configured to allow users another way to log in.

`--monitoring` (structure)

Specifies whether detailed monitoring is enabled for the instance.

Enabled -> (boolean)

Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.

Shorthand Syntax:

```
Enabled=boolean
```

JSON Syntax:

```
{
  "Enabled": true|false
}
```

`--placement` (structure)

The placement for the instance.

Affinity -> (string)

The affinity setting for the instance on the Dedicated Host.

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) or [ImportInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html) .

GroupName -> (string)

The name of the placement group that the instance is in. If you specify `GroupName` , you canât specify `GroupId` .

PartitionNumber -> (integer)

The number of the partition that the instance is in. Valid only if the placement group strategy is set to `partition` .

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) .

HostId -> (string)

The ID of the Dedicated Host on which the instance resides.

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) or [ImportInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html) .

Tenancy -> (string)

The tenancy of the instance. An instance with a tenancy of `dedicated` runs on single-tenant hardware.

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) . The `host` tenancy is not supported for [ImportInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html) or for T3 instances that are configured for the `unlimited` CPU credit option.

SpreadDomain -> (string)

Reserved for future use.

HostResourceGroupArn -> (string)

The ARN of the host resource group in which to launch the instances.

If you specify this parameter, either omit the **Tenancy** parameter or set it to `host` .

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) .

GroupId -> (string)

The ID of the placement group that the instance is in. If you specify `GroupId` , you canât specify `GroupName` .

AvailabilityZone -> (string)

The Availability Zone of the instance.

If not specified, an Availability Zone will be automatically chosen for you based on the load balancing criteria for the Region.

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) .

Shorthand Syntax:

```
Affinity=string,GroupName=string,PartitionNumber=integer,HostId=string,Tenancy=string,SpreadDomain=string,HostResourceGroupArn=string,GroupId=string,AvailabilityZone=string
```

JSON Syntax:

```
{
  "Affinity": "string",
  "GroupName": "string",
  "PartitionNumber": integer,
  "HostId": "string",
  "Tenancy": "default"|"dedicated"|"host",
  "SpreadDomain": "string",
  "HostResourceGroupArn": "string",
  "GroupId": "string",
  "AvailabilityZone": "string"
}
```

`--ramdisk-id` (string)

The ID of the RAM disk to select. Some kernels require additional drivers at launch. Check the kernel requirements for information about whether you need to specify a RAM disk. To find kernel requirements, go to the Amazon Web Services Resource Center and search for the kernel ID.

### Warning

We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see [PV-GRUB](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedkernels.html) in the *Amazon EC2 User Guide* .

`--security-group-ids` (list)

The IDs of the security groups. You can create a security group using [CreateSecurityGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSecurityGroup.html) .

If you specify a network interface, you must specify any security groups as part of the network interface instead of using this parameter.

(string)

Syntax:

```
"string" "string" ...
```

`--security-groups` (list)

[Default VPC] The names of the security groups.

If you specify a network interface, you must specify any security groups as part of the network interface instead of using this parameter.

Default: Amazon EC2 uses the default security group.

(string)

Syntax:

```
"string" "string" ...
```

`--subnet-id` (string)

The ID of the subnet to launch the instance into.

If you specify a network interface, you must specify any subnets as part of the network interface instead of using this parameter.

`--user-data` (string)

The user data to make available to the instance. User data must be base64-encoded. Depending on the tool or SDK that youâre using, the base64-encoding might be performed for you. For more information, see [Work with instance user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-add-user-data.html) .

`--elastic-gpu-specification` (list)

An elastic GPU to associate with the instance.

### Note

Amazon Elastic Graphics reached end of life on January 8, 2024.

(structure)

### Note

Amazon Elastic Graphics reached end of life on January 8, 2024.

A specification for an Elastic Graphics accelerator.

Type -> (string)

The type of Elastic Graphics accelerator.

Shorthand Syntax:

```
Type=string ...
```

JSON Syntax:

```
[
  {
    "Type": "string"
  }
  ...
]
```

`--elastic-inference-accelerators` (list)

An elastic inference accelerator to associate with the instance.

### Note

Amazon Elastic Inference is no longer available.

(structure)

### Note

Amazon Elastic Inference is no longer available.

Describes an elastic inference accelerator.

Type -> (string)

The type of elastic inference accelerator. The possible values are `eia1.medium` , `eia1.large` , `eia1.xlarge` , `eia2.medium` , `eia2.large` , and `eia2.xlarge` .

Count -> (integer)

The number of elastic inference accelerators to attach to the instance.

Default: 1

Shorthand Syntax:

```
Type=string,Count=integer ...
```

JSON Syntax:

```
[
  {
    "Type": "string",
    "Count": integer
  }
  ...
]
```

`--tag-specifications` (list)

The tags to apply to the resources that are created during instance launch.

You can specify tags for the following resources only:

- Instances
- Volumes
- Spot Instance requests
- Network interfaces

To tag a resource after it has been created, see [CreateTags](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html) .

(structure)

The tags to apply to a resource when the resource is being created. When you specify a tag, you must specify the resource type to tag, otherwise the request will fail.

### Note

The `Valid Values` lists all the resource types that can be tagged. However, the action youâre using might not support tagging all of these resource types. If you try to tag a resource type that is unsupported for the action youâre using, youâll get an error.

ResourceType -> (string)

The type of resource to tag on creation.

Tags -> (list)

The tags to apply to the resource.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

Shorthand Syntax:

```
ResourceType=string,Tags=[{Key=string,Value=string},{Key=string,Value=string}] ...
```

JSON Syntax:

```
[
  {
    "ResourceType": "capacity-reservation"|"client-vpn-endpoint"|"customer-gateway"|"carrier-gateway"|"coip-pool"|"declarative-policies-report"|"dedicated-host"|"dhcp-options"|"egress-only-internet-gateway"|"elastic-ip"|"elastic-gpu"|"export-image-task"|"export-instance-task"|"fleet"|"fpga-image"|"host-reservation"|"image"|"import-image-task"|"import-snapshot-task"|"instance"|"instance-event-window"|"internet-gateway"|"ipam"|"ipam-pool"|"ipam-scope"|"ipv4pool-ec2"|"ipv6pool-ec2"|"key-pair"|"launch-template"|"local-gateway"|"local-gateway-route-table"|"local-gateway-virtual-interface"|"local-gateway-virtual-interface-group"|"local-gateway-route-table-vpc-association"|"local-gateway-route-table-virtual-interface-group-association"|"natgateway"|"network-acl"|"network-interface"|"network-insights-analysis"|"network-insights-path"|"network-insights-access-scope"|"network-insights-access-scope-analysis"|"outpost-lag"|"placement-group"|"prefix-list"|"replace-root-volume-task"|"reserved-instances"|"route-table"|"security-group"|"security-group-rule"|"service-link-virtual-interface"|"snapshot"|"spot-fleet-request"|"spot-instances-request"|"subnet"|"subnet-cidr-reservation"|"traffic-mirror-filter"|"traffic-mirror-session"|"traffic-mirror-target"|"transit-gateway"|"transit-gateway-attachment"|"transit-gateway-connect-peer"|"transit-gateway-multicast-domain"|"transit-gateway-policy-table"|"transit-gateway-route-table"|"transit-gateway-route-table-announcement"|"volume"|"vpc"|"vpc-endpoint"|"vpc-endpoint-connection"|"vpc-endpoint-service"|"vpc-endpoint-service-permission"|"vpc-peering-connection"|"vpn-connection"|"vpn-gateway"|"vpc-flow-log"|"capacity-reservation-fleet"|"traffic-mirror-filter-rule"|"vpc-endpoint-connection-device-type"|"verified-access-instance"|"verified-access-group"|"verified-access-endpoint"|"verified-access-policy"|"verified-access-trust-provider"|"vpn-connection-device-type"|"vpc-block-public-access-exclusion"|"route-server"|"route-server-endpoint"|"route-server-peer"|"ipam-resource-discovery"|"ipam-resource-discovery-association"|"instance-connect-endpoint"|"verified-access-endpoint-target"|"ipam-external-resource-verification-token"|"mac-modification-task",
    "Tags": [
      {
        "Key": "string",
        "Value": "string"
      }
      ...
    ]
  }
  ...
]
```

`--launch-template` (structure)

The launch template. Any additional parameters that you specify for the new instance overwrite the corresponding parameters included in the launch template.

LaunchTemplateId -> (string)

The ID of the launch template.

You must specify either the launch template ID or the launch template name, but not both.

LaunchTemplateName -> (string)

The name of the launch template.

You must specify either the launch template ID or the launch template name, but not both.

Version -> (string)

The launch template version number, `$Latest` , or `$Default` .

A value of `$Latest` uses the latest version of the launch template.

A value of `$Default` uses the default version of the launch template.

Default: The default version of the launch template.

Shorthand Syntax:

```
LaunchTemplateId=string,LaunchTemplateName=string,Version=string
```

JSON Syntax:

```
{
  "LaunchTemplateId": "string",
  "LaunchTemplateName": "string",
  "Version": "string"
}
```

`--instance-market-options` (structure)

The market (purchasing) option for the instances.

For  RunInstances , persistent Spot Instance requests are only supported when **InstanceInterruptionBehavior** is set to either `hibernate` or `stop` .

MarketType -> (string)

The market type.

SpotOptions -> (structure)

The options for Spot Instances.

MaxPrice -> (string)

The maximum hourly price that youâre willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.

### Warning

If you specify a maximum price, your Spot Instances will be interrupted more frequently than if you do not specify this parameter.

If you specify a maximum price, it must be more than USD $0.001. Specifying a value below USD $0.001 will result in an `InvalidParameterValue` error message.

SpotInstanceType -> (string)

The Spot Instance request type. For [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances) , persistent Spot Instance requests are only supported when the instance interruption behavior is either `hibernate` or `stop` .

BlockDurationMinutes -> (integer)

Deprecated.

ValidUntil -> (timestamp)

The end date of the request, in UTC format (*YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z). Supported only for persistent requests.

- For a persistent request, the request remains active until the `ValidUntil` date and time is reached. Otherwise, the request remains active until you cancel it.
- For a one-time request, `ValidUntil` is not supported. The request remains active until all instances launch or you cancel the request.

InstanceInterruptionBehavior -> (string)

The behavior when a Spot Instance is interrupted.

If `Configured` (for ` `HibernationOptions` [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HibernationOptionsRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HibernationOptionsRequest).html`__ ) is set to `true` , the `InstanceInterruptionBehavior` parameter is automatically set to `hibernate` . If you set it to `stop` or `terminate` , youâll get an error.

If `Configured` (for ` `HibernationOptions` [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HibernationOptionsRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HibernationOptionsRequest).html`__ ) is set to `false` or `null` , the `InstanceInterruptionBehavior` parameter is automatically set to `terminate` . You can also set it to `stop` or `hibernate` .

For more information, see [Interruption behavior](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interruption-behavior.html) in the *Amazon EC2 User Guide* .

Shorthand Syntax:

```
MarketType=string,SpotOptions={MaxPrice=string,SpotInstanceType=string,BlockDurationMinutes=integer,ValidUntil=timestamp,InstanceInterruptionBehavior=string}
```

JSON Syntax:

```
{
  "MarketType": "spot"|"capacity-block",
  "SpotOptions": {
    "MaxPrice": "string",
    "SpotInstanceType": "one-time"|"persistent",
    "BlockDurationMinutes": integer,
    "ValidUntil": timestamp,
    "InstanceInterruptionBehavior": "hibernate"|"stop"|"terminate"
  }
}
```

`--credit-specification` (structure)

The credit option for CPU usage of the burstable performance instance. Valid values are `standard` and `unlimited` . To change this attribute after launch, use [ModifyInstanceCreditSpecification](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceCreditSpecification.html) . For more information, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) in the *Amazon EC2 User Guide* .

Default: `standard` (T2 instances) or `unlimited` (T3/T3a/T4g instances)

For T3 instances with `host` tenancy, only `standard` is supported.

CpuCredits -> (string)

The credit option for CPU usage of a T instance.

Valid values: `standard` | `unlimited`

Shorthand Syntax:

```
CpuCredits=string
```

JSON Syntax:

```
{
  "CpuCredits": "string"
}
```

`--cpu-options` (structure)

The CPU options for the instance. For more information, see [Optimize CPU options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) in the *Amazon EC2 User Guide* .

CoreCount -> (integer)

The number of CPU cores for the instance.

ThreadsPerCore -> (integer)

The number of threads per CPU core. To disable multithreading for the instance, specify a value of `1` . Otherwise, specify the default value of `2` .

AmdSevSnp -> (string)

Indicates whether to enable the instance for AMD SEV-SNP. AMD SEV-SNP is supported with M6a, R6a, and C6a instance types only. For more information, see [AMD SEV-SNP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html) .

Shorthand Syntax:

```
CoreCount=integer,ThreadsPerCore=integer,AmdSevSnp=string
```

JSON Syntax:

```
{
  "CoreCount": integer,
  "ThreadsPerCore": integer,
  "AmdSevSnp": "enabled"|"disabled"
}
```

`--capacity-reservation-specification` (structure)

Information about the Capacity Reservation targeting option. If you do not specify this parameter, the instanceâs Capacity Reservation preference defaults to `open` , which enables it to run in any open Capacity Reservation that has matching attributes (instance type, platform, Availability Zone, and tenancy).

CapacityReservationPreference -> (string)

Indicates the instanceâs Capacity Reservation preferences. Possible preferences include:

- `capacity-reservations-only` - The instance will only run in a Capacity Reservation or Capacity Reservation group. If capacity isnât available, the instance will fail to launch.
- `open` - The instance can run in any `open` Capacity Reservation that has matching attributes (instance type, platform, Availability Zone, and tenancy). If capacity isnât available, the instance runs as an On-Demand Instance.
- `none` - The instance doesnât run in a Capacity Reservation even if one is available. The instance runs as an On-Demand Instance.

CapacityReservationTarget -> (structure)

Information about the target Capacity Reservation or Capacity Reservation group.

CapacityReservationId -> (string)

The ID of the Capacity Reservation in which to run the instance.

CapacityReservationResourceGroupArn -> (string)

The ARN of the Capacity Reservation resource group in which to run the instance.

Shorthand Syntax:

```
CapacityReservationPreference=string,CapacityReservationTarget={CapacityReservationId=string,CapacityReservationResourceGroupArn=string}
```

JSON Syntax:

```
{
  "CapacityReservationPreference": "capacity-reservations-only"|"open"|"none",
  "CapacityReservationTarget": {
    "CapacityReservationId": "string",
    "CapacityReservationResourceGroupArn": "string"
  }
}
```

`--hibernation-options` (structure)

Indicates whether an instance is enabled for hibernation. This parameter is valid only if the instance meets the [hibernation prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html) . For more information, see [Hibernate your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html) in the *Amazon EC2 User Guide* .

You canât enable hibernation and Amazon Web Services Nitro Enclaves on the same instance.

Configured -> (boolean)

Set to `true` to enable your instance for hibernation.

For Spot Instances, if you set `Configured` to `true` , either omit the `InstanceInterruptionBehavior` parameter (for ` `SpotMarketOptions` [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotMarketOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotMarketOptions).html`__ ), or set it to `hibernate` . When `Configured` is true:

- If you omit `InstanceInterruptionBehavior` , it defaults to `hibernate` .
- If you set `InstanceInterruptionBehavior` to a value other than `hibernate` , youâll get an error.

Default: `false`

Shorthand Syntax:

```
Configured=boolean
```

JSON Syntax:

```
{
  "Configured": true|false
}
```

`--license-specifications` (list)

The license configurations.

(structure)

Describes a license configuration.

LicenseConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the license configuration.

Shorthand Syntax:

```
LicenseConfigurationArn=string ...
```

JSON Syntax:

```
[
  {
    "LicenseConfigurationArn": "string"
  }
  ...
]
```

`--metadata-options` (structure)

The metadata options for the instance. For more information, see [Instance metadata and user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) .

HttpTokens -> (string)

Indicates whether IMDSv2 is required.

- `optional` - IMDSv2 is optional, which means that you can use either IMDSv2 or IMDSv1.
- `required` - IMDSv2 is required, which means that IMDSv1 is disabled, and you must use IMDSv2.

Default:

- If the value of `ImdsSupport` for the Amazon Machine Image (AMI) for your instance is `v2.0` and the account level default is set to `no-preference` , the default is `required` .
- If the value of `ImdsSupport` for the Amazon Machine Image (AMI) for your instance is `v2.0` , but the account level default is set to `V1 or V2` , the default is `optional` .

The default value can also be affected by other combinations of parameters. For more information, see [Order of precedence for instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html#instance-metadata-options-order-of-precedence) in the *Amazon EC2 User Guide* .

HttpPutResponseHopLimit -> (integer)

The maximum number of hops that the metadata token can travel.

Possible values: Integers from 1 to 64

HttpEndpoint -> (string)

Enables or disables the HTTP metadata endpoint on your instances.

If you specify a value of `disabled` , you cannot access your instance metadata.

Default: `enabled`

HttpProtocolIpv6 -> (string)

Enables or disables the IPv6 endpoint for the instance metadata service.

Default: `disabled`

InstanceMetadataTags -> (string)

Set to `enabled` to allow access to instance tags from the instance metadata. Set to `disabled` to turn off access to instance tags from the instance metadata. For more information, see [Work with instance tags using the instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#work-with-tags-in-IMDS) .

Default: `disabled`

Shorthand Syntax:

```
HttpTokens=string,HttpPutResponseHopLimit=integer,HttpEndpoint=string,HttpProtocolIpv6=string,InstanceMetadataTags=string
```

JSON Syntax:

```
{
  "HttpTokens": "optional"|"required",
  "HttpPutResponseHopLimit": integer,
  "HttpEndpoint": "disabled"|"enabled",
  "HttpProtocolIpv6": "disabled"|"enabled",
  "InstanceMetadataTags": "disabled"|"enabled"
}
```

`--enclave-options` (structure)

Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves. For more information, see [What is Amazon Web Services Nitro Enclaves?](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html) in the *Amazon Web Services Nitro Enclaves User Guide* .

You canât enable Amazon Web Services Nitro Enclaves and hibernation on the same instance.

Enabled -> (boolean)

To enable the instance for Amazon Web Services Nitro Enclaves, set this parameter to `true` .

Shorthand Syntax:

```
Enabled=boolean
```

JSON Syntax:

```
{
  "Enabled": true|false
}
```

`--private-dns-name-options` (structure)

The options for the instance hostname. The default values are inherited from the subnet. Applies only if creating a network interface, not attaching an existing one.

HostnameType -> (string)

The type of hostname for EC2 instances. For IPv4 only subnets, an instance DNS name must be based on the instance IPv4 address. For IPv6 only subnets, an instance DNS name must be based on the instance ID. For dual-stack subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID.

EnableResourceNameDnsARecord -> (boolean)

Indicates whether to respond to DNS queries for instance hostnames with DNS A records.

EnableResourceNameDnsAAAARecord -> (boolean)

Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.

Shorthand Syntax:

```
HostnameType=string,EnableResourceNameDnsARecord=boolean,EnableResourceNameDnsAAAARecord=boolean
```

JSON Syntax:

```
{
  "HostnameType": "ip-name"|"resource-name",
  "EnableResourceNameDnsARecord": true|false,
  "EnableResourceNameDnsAAAARecord": true|false
}
```

`--maintenance-options` (structure)

The maintenance and recovery options for the instance.

AutoRecovery -> (string)

Disables the automatic recovery behavior of your instance or sets it to default. For more information, see [Simplified automatic recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html#instance-configuration-recovery) .

Shorthand Syntax:

```
AutoRecovery=string
```

JSON Syntax:

```
{
  "AutoRecovery": "disabled"|"default"
}
```

`--disable-api-stop` | `--no-disable-api-stop` (boolean)

Indicates whether an instance is enabled for stop protection. For more information, see [Stop protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html#Using_StopProtection) .

`--enable-primary-ipv6` | `--no-enable-primary-ipv6` (boolean)

If youâre launching an instance into a dual-stack or IPv6-only subnet, you can enable assigning a primary IPv6 address. A primary IPv6 address is an IPv6 GUA address associated with an ENI that you have enabled to use a primary IPv6 address. Use this option if an instance relies on its IPv6 address not changing. When you launch the instance, Amazon Web Services will automatically assign an IPv6 address associated with the ENI attached to your instance to be the primary IPv6 address. Once you enable an IPv6 GUA address to be a primary IPv6, you cannot disable it. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. If you have multiple IPv6 addresses associated with an ENI attached to your instance and you enable a primary IPv6 address, the first IPv6 GUA address associated with the ENI becomes the primary IPv6 address.

`--network-performance-options` (structure)

Contains settings for the network performance options for the instance.

BandwidthWeighting -> (string)

Specify the bandwidth weighting option to boost the associated type of baseline bandwidth, as follows:

default

This option uses the standard bandwidth configuration for your instance type.

vpc-1

This option boosts your networking baseline bandwidth and reduces your EBS baseline bandwidth.

ebs-1

This option boosts your EBS baseline bandwidth and reduces your networking baseline bandwidth.

Shorthand Syntax:

```
BandwidthWeighting=string
```

JSON Syntax:

```
{
  "BandwidthWeighting": "default"|"vpc-1"|"ebs-1"
}
```

`--operator` (structure)

Reserved for internal use.

Principal -> (string)

The service provider that manages the resource.

Shorthand Syntax:

```
Principal=string
```

JSON Syntax:

```
{
  "Principal": "string"
}
```

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--disable-api-termination` | `--enable-api-termination` (boolean)

Indicates whether termination protection is enabled for the instance. The default is `false` , which means that you can terminate the instance using the Amazon EC2 console, command line tools, or API. You can enable termination protection when you launch an instance, while the instance is running, or while the instance is stopped.

`--instance-initiated-shutdown-behavior` (string)

Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).

Default: `stop`

Possible values:

- `stop`
- `terminate`

`--private-ip-address` (string)

The primary IPv4 address. You must specify a value from the IPv4 address range of the subnet.

Only one private IP address can be designated as primary. You canât specify this option if youâve specified the option to designate a private IP address as the primary IP address in a network interface specification. You cannot specify this option if youâre launching more than one instance in the request.

You cannot specify this option and the network interfaces option in the same request.

`--client-token` (string)

Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.

For more information, see [Ensuring Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .

Constraints: Maximum 64 ASCII characters

`--additional-info` (string)

Reserved.

`--network-interfaces` (list)

The network interfaces to associate with the instance.

(structure)

Describes a network interface.

AssociatePublicIpAddress -> (boolean)

Indicates whether to assign a public IPv4 address to an instance you launch in a VPC. The public IP address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is `true` .

Amazon Web Services charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the *Public IPv4 Address* tab on the [Amazon VPC pricing page](http://aws.amazon.com/vpc/pricing/) .

DeleteOnTermination -> (boolean)

If set to `true` , the interface is deleted when the instance is terminated. You can specify `true` only if creating a new network interface when launching an instance.

Description -> (string)

The description of the network interface. Applies only if creating a network interface when launching an instance.

DeviceIndex -> (integer)

The position of the network interface in the attachment order. A primary network interface has a device index of 0.

If you specify a network interface when launching an instance, you must specify the device index.

Groups -> (list)

The IDs of the security groups for the network interface. Applies only if creating a network interface when launching an instance.

(string)

Ipv6AddressCount -> (integer)

A number of IPv6 addresses to assign to the network interface. Amazon EC2 chooses the IPv6 addresses from the range of the subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if youâve specified a minimum number of instances to launch.

Ipv6Addresses -> (list)

The IPv6 addresses to assign to the network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if youâve specified a minimum number of instances to launch.

(structure)

Describes an IPv6 address.

Ipv6Address -> (string)

The IPv6 address.

IsPrimaryIpv6 -> (boolean)

Determines if an IPv6 address associated with a network interface is the primary IPv6 address. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information, see [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) .

NetworkInterfaceId -> (string)

The ID of the network interface.

If you are creating a Spot Fleet, omit this parameter because you canât specify a network interface ID in a launch specification.

PrivateIpAddress -> (string)

The private IPv4 address of the network interface. Applies only if creating a network interface when launching an instance. You cannot specify this option if youâre launching more than one instance in a [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) request.

PrivateIpAddresses -> (list)

The private IPv4 addresses to assign to the network interface. Only one private IPv4 address can be designated as primary. You cannot specify this option if youâre launching more than one instance in a [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) request.

(structure)

Describes a secondary private IPv4 address for a network interface.

Primary -> (boolean)

Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.

PrivateIpAddress -> (string)

The private IPv4 address.

SecondaryPrivateIpAddressCount -> (integer)

The number of secondary private IPv4 addresses. You canât specify this parameter and also specify a secondary private IP address using the `PrivateIpAddress` parameter.

SubnetId -> (string)

The ID of the subnet associated with the network interface. Applies only if creating a network interface when launching an instance.

AssociateCarrierIpAddress -> (boolean)

Indicates whether to assign a carrier IP address to the network interface.

You can only assign a carrier IP address to a network interface that is in a subnet in a Wavelength Zone. For more information about carrier IP addresses, see [Carrier IP address](https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html#provider-owned-ip) in the *Amazon Web Services Wavelength Developer Guide* .

InterfaceType -> (string)

The type of network interface.

If you specify `efa-only` , do not assign any IP addresses to the network interface. EFA-only network interfaces do not support IP addresses.

Valid values: `interface` | `efa` | `efa-only`

NetworkCardIndex -> (integer)

The index of the network card. Some instance types support multiple network cards. The primary network interface must be assigned to network card index 0. The default is network card index 0.

If you are using [RequestSpotInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html) to create Spot Instances, omit this parameter because you canât specify the network card index when using this API. To specify the network card index, use [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) .

Ipv4Prefixes -> (list)

The IPv4 delegated prefixes to be assigned to the network interface. You cannot use this option if you use the `Ipv4PrefixCount` option.

(structure)

Describes the IPv4 prefix option for a network interface.

Ipv4Prefix -> (string)

The IPv4 prefix. For information, see [Assigning prefixes to network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-prefix-eni.html) in the *Amazon EC2 User Guide* .

Ipv4PrefixCount -> (integer)

The number of IPv4 delegated prefixes to be automatically assigned to the network interface. You cannot use this option if you use the `Ipv4Prefix` option.

Ipv6Prefixes -> (list)

The IPv6 delegated prefixes to be assigned to the network interface. You cannot use this option if you use the `Ipv6PrefixCount` option.

(structure)

Describes the IPv6 prefix option for a network interface.

Ipv6Prefix -> (string)

The IPv6 prefix.

Ipv6PrefixCount -> (integer)

The number of IPv6 delegated prefixes to be automatically assigned to the network interface. You cannot use this option if you use the `Ipv6Prefix` option.

PrimaryIpv6 -> (boolean)

The primary IPv6 address of the network interface. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information about primary IPv6 addresses, see [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) .

EnaSrdSpecification -> (structure)

Specifies the ENA Express settings for the network interface thatâs attached to the instance.

EnaSrdEnabled -> (boolean)

Specifies whether ENA Express is enabled for the network interface when you launch an instance.

EnaSrdUdpSpecification -> (structure)

Contains ENA Express settings for UDP network traffic for the network interface attached to the instance.

EnaSrdUdpEnabled -> (boolean)

Indicates whether UDP traffic uses ENA Express for your instance. To ensure that UDP traffic can use ENA Express when you launch an instance, you must also set **EnaSrdEnabled** in the **EnaSrdSpecificationRequest** to `true` .

ConnectionTrackingSpecification -> (structure)

A security group connection tracking specification that enables you to set the timeout for connection tracking on an Elastic network interface. For more information, see [Connection tracking timeouts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts) in the *Amazon EC2 User Guide* .

TcpEstablishedTimeout -> (integer)

Timeout (in seconds) for idle TCP connections in an established state. Min: 60 seconds. Max: 432000 seconds (5 days). Default: 432000 seconds. Recommended: Less than 432000 seconds.

UdpStreamTimeout -> (integer)

Timeout (in seconds) for idle UDP flows classified as streams which have seen more than one request-response transaction. Min: 60 seconds. Max: 180 seconds (3 minutes). Default: 180 seconds.

UdpTimeout -> (integer)

Timeout (in seconds) for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction. Min: 30 seconds. Max: 60 seconds. Default: 30 seconds.

EnaQueueCount -> (integer)

The number of ENA queues to be created with the instance.

Shorthand Syntax:

```
AssociatePublicIpAddress=boolean,DeleteOnTermination=boolean,Description=string,DeviceIndex=integer,Groups=string,string,Ipv6AddressCount=integer,Ipv6Addresses=[{Ipv6Address=string,IsPrimaryIpv6=boolean},{Ipv6Address=string,IsPrimaryIpv6=boolean}],NetworkInterfaceId=string,PrivateIpAddress=string,PrivateIpAddresses=[{Primary=boolean,PrivateIpAddress=string},{Primary=boolean,PrivateIpAddress=string}],SecondaryPrivateIpAddressCount=integer,SubnetId=string,AssociateCarrierIpAddress=boolean,InterfaceType=string,NetworkCardIndex=integer,Ipv4Prefixes=[{Ipv4Prefix=string},{Ipv4Prefix=string}],Ipv4PrefixCount=integer,Ipv6Prefixes=[{Ipv6Prefix=string},{Ipv6Prefix=string}],Ipv6PrefixCount=integer,PrimaryIpv6=boolean,EnaSrdSpecification={EnaSrdEnabled=boolean,EnaSrdUdpSpecification={EnaSrdUdpEnabled=boolean}},ConnectionTrackingSpecification={TcpEstablishedTimeout=integer,UdpStreamTimeout=integer,UdpTimeout=integer},EnaQueueCount=integer ...
```

JSON Syntax:

```
[
  {
    "AssociatePublicIpAddress": true|false,
    "DeleteOnTermination": true|false,
    "Description": "string",
    "DeviceIndex": integer,
    "Groups": ["string", ...],
    "Ipv6AddressCount": integer,
    "Ipv6Addresses": [
      {
        "Ipv6Address": "string",
        "IsPrimaryIpv6": true|false
      }
      ...
    ],
    "NetworkInterfaceId": "string",
    "PrivateIpAddress": "string",
    "PrivateIpAddresses": [
      {
        "Primary": true|false,
        "PrivateIpAddress": "string"
      }
      ...
    ],
    "SecondaryPrivateIpAddressCount": integer,
    "SubnetId": "string",
    "AssociateCarrierIpAddress": true|false,
    "InterfaceType": "string",
    "NetworkCardIndex": integer,
    "Ipv4Prefixes": [
      {
        "Ipv4Prefix": "string"
      }
      ...
    ],
    "Ipv4PrefixCount": integer,
    "Ipv6Prefixes": [
      {
        "Ipv6Prefix": "string"
      }
      ...
    ],
    "Ipv6PrefixCount": integer,
    "PrimaryIpv6": true|false,
    "EnaSrdSpecification": {
      "EnaSrdEnabled": true|false,
      "EnaSrdUdpSpecification": {
        "EnaSrdUdpEnabled": true|false
      }
    },
    "ConnectionTrackingSpecification": {
      "TcpEstablishedTimeout": integer,
      "UdpStreamTimeout": integer,
      "UdpTimeout": integer
    },
    "EnaQueueCount": integer
  }
  ...
]
```

`--iam-instance-profile` (structure)

The name or Amazon Resource Name (ARN) of an IAM instance profile.

Arn -> (string)

The Amazon Resource Name (ARN) of the instance profile.

Name -> (string)

The name of the instance profile.

Shorthand Syntax:

```
Arn=string,Name=string
```

JSON Syntax:

```
{
  "Arn": "string",
  "Name": "string"
}
```

`--ebs-optimized` | `--no-ebs-optimized` (boolean)

Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal Amazon EBS I/O performance. This optimization isnât available with all instance types. Additional usage charges apply when using an EBS-optimized instance.

Default: `false`

`--count` (string)

Number of instances to launch. If a single number is provided, it is assumed to be the minimum to launch (defaults to 1). If a range is provided in the form `min:max` then the first number is interpreted as the minimum number of instances to launch and the second is interpreted as the maximum number of instances to launch.

`--secondary-private-ip-addresses` (string)
[EC2-VPC] A secondary private IP address for the network interface or instance. You can specify this multiple times to assign multiple secondary IP addresses. If you want additional private IP addresses but do not need a specific address, use the âsecondary-private-ip-address-count option.

`--secondary-private-ip-address-count` (string)
[EC2-VPC] The number of secondary IP addresses to assign to the network interface or instance.

`--associate-public-ip-address` | `--no-associate-public-ip-address` (boolean)
[EC2-VPC] If specified a public IP address will be assigned to the new instance in a VPC.

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

**Example 1: To launch an instance into a default subnet**

The following `run-instances` example launches a single instance of type `t2.micro` into the default subnet for the current Region and associates it with the default subnet for the default VPC for the Region. The key pair is optional if you do not plan to connect to your instance using SSH (Linux) or RDP (Windows).

```
aws ec2 run-instances \
    --image-id ami-0abcdef1234567890 \
    --instance-type t2.micro \
    --key-name MyKeyPair
```

Output:

```
{
    "Instances": [
        {
            "AmiLaunchIndex": 0,
            "ImageId": "ami-0abcdef1234567890",
            "InstanceId": "i-1231231230abcdef0",
            "InstanceType": "t2.micro",
            "KeyName": "MyKeyPair",
            "LaunchTime": "2018-05-10T08:05:20.000Z",
            "Monitoring": {
                "State": "disabled"
            },
            "Placement": {
                "AvailabilityZone": "us-east-2a",
                "GroupName": "",
                "Tenancy": "default"
            },
            "PrivateDnsName": "ip-10-0-0-157.us-east-2.compute.internal",
            "PrivateIpAddress": "10.0.0.157",
            "ProductCodes": [],
            "PublicDnsName": "",
            "State": {
                "Code": 0,
                "Name": "pending"
            },
            "StateTransitionReason": "",
            "SubnetId": "subnet-04a636d18e83cfacb",
            "VpcId": "vpc-1234567890abcdef0",
            "Architecture": "x86_64",
            "BlockDeviceMappings": [],
            "ClientToken": "",
            "EbsOptimized": false,
            "Hypervisor": "xen",
            "NetworkInterfaces": [
                {
                    "Attachment": {
                        "AttachTime": "2018-05-10T08:05:20.000Z",
                        "AttachmentId": "eni-attach-0e325c07e928a0405",
                        "DeleteOnTermination": true,
                        "DeviceIndex": 0,
                        "Status": "attaching"
                    },
                    "Description": "",
                    "Groups": [
                        {
                            "GroupName": "MySecurityGroup",
                            "GroupId": "sg-0598c7d356eba48d7"
                        }
                    ],
                    "Ipv6Addresses": [],
                    "MacAddress": "0a:ab:58:e0:67:e2",
                    "NetworkInterfaceId": "eni-0c0a29997760baee7",
                    "OwnerId": "123456789012",
                    "PrivateDnsName": "ip-10-0-0-157.us-east-2.compute.internal",
                    "PrivateIpAddress": "10.0.0.157",
                    "PrivateIpAddresses": [
                        {
                            "Primary": true,
                            "PrivateDnsName": "ip-10-0-0-157.us-east-2.compute.internal",
                            "PrivateIpAddress": "10.0.0.157"
                        }
                    ],
                    "SourceDestCheck": true,
                    "Status": "in-use",
                    "SubnetId": "subnet-04a636d18e83cfacb",
                    "VpcId": "vpc-1234567890abcdef0",
                    "InterfaceType": "interface"
                }
            ],
            "RootDeviceName": "/dev/xvda",
            "RootDeviceType": "ebs",
            "SecurityGroups": [
                {
                    "GroupName": "MySecurityGroup",
                    "GroupId": "sg-0598c7d356eba48d7"
                }
            ],
            "SourceDestCheck": true,
            "StateReason": {
                "Code": "pending",
                "Message": "pending"
            },
            "Tags": [],
            "VirtualizationType": "hvm",
            "CpuOptions": {
                "CoreCount": 1,
                "ThreadsPerCore": 1
            },
            "CapacityReservationSpecification": {
                "CapacityReservationPreference": "open"
            },
            "MetadataOptions": {
                "State": "pending",
                "HttpTokens": "optional",
                "HttpPutResponseHopLimit": 1,
                "HttpEndpoint": "enabled"
            }
        }
    ],
    "OwnerId": "123456789012",
    "ReservationId": "r-02a3f596d91211712"
}
```

**Example 2: To launch an instance into a non-default subnet and add a public IP address**

The following `run-instances` example requests a public IP address for an instance that youâre launching into a nondefault subnet. The instance is associated with the specified security group.

```
aws ec2 run-instances \
    --image-id ami-0abcdef1234567890 \
    --instance-type t2.micro \
    --subnet-id subnet-08fc749671b2d077c \
    --security-group-ids sg-0b0384b66d7d692f9 \
    --associate-public-ip-address \
    --key-name MyKeyPair
```

For an example of the output for `run-instances`, see Example 1.

**Example 3: To launch an instance with additional volumes**

The following `run-instances` example uses a block device mapping, specified in mapping.json, to attach additional volumes at launch. A block device mapping can specify EBS volumes, instance store volumes, or both EBS volumes and instance store volumes.

```
aws ec2 run-instances \
    --image-id ami-0abcdef1234567890 \
    --instance-type t2.micro \
    --subnet-id subnet-08fc749671b2d077c \
    --security-group-ids sg-0b0384b66d7d692f9 \
    --key-name MyKeyPair \
    --block-device-mappings file://mapping.json
```

Contents of `mapping.json`. This example adds `/dev/sdh` an empty EBS volume with a size of 100 GiB.

```
[
    {
        "DeviceName": "/dev/sdh",
        "Ebs": {
            "VolumeSize": 100
        }
    }
]
```

Contents of `mapping.json`. This example adds `ephemeral1` as an instance store volume.

```
[
    {
        "DeviceName": "/dev/sdc",
        "VirtualName": "ephemeral1"
    }
]
```

For an example of the output for `run-instances`, see Example 1.

For more information about block device mappings, see [Block device mapping](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html) in the *Amazon EC2 User Guide*.

**Example 4: To launch an instance and add tags on creation**

The following `run-instances` example adds a tag with a key of `webserver` and value of `production` to the instance. The command also applies a tag with a key of `cost-center` and a value of `cc123` to any EBS volume thatâs created (in this case, the root volume).

```
aws ec2 run-instances \
    --image-id ami-0abcdef1234567890 \
    --instance-type t2.micro \
    --count 1 \
    --subnet-id subnet-08fc749671b2d077c \
    --key-name MyKeyPair \
    --security-group-ids sg-0b0384b66d7d692f9 \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=webserver,Value=production}]' 'ResourceType=volume,Tags=[{Key=cost-center,Value=cc123}]'
```

For an example of the output for `run-instances`, see Example 1.

**Example 5: To launch an instance with user data**

The following `run-instances` example passes user data in a file called `my_script.txt` that contains a configuration script for your instance. The script runs at launch.

```
aws ec2 run-instances \
    --image-id ami-0abcdef1234567890 \
    --instance-type t2.micro \
    --count 1 \
    --subnet-id subnet-08fc749671b2d077c \
    --key-name MyKeyPair \
    --security-group-ids sg-0b0384b66d7d692f9 \
    --user-data file://my_script.txt
```

For an example of the output for `run-instances`, see Example 1.

For more information about instance user data, see [Working with instance user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-add-user-data.html) in the *Amazon EC2 User Guide*.

**Example 6: To launch a burstable performance instance**

The following `run-instances` example launches a t2.micro instance with the `unlimited` credit option. When you launch a T2 instance, if you do not specify `--credit-specification`, the default is the `standard` credit option. When you launch a T3 instance, the default is the `unlimited` credit option.

```
aws ec2 run-instances \
    --image-id ami-0abcdef1234567890 \
    --instance-type t2.micro \
    --count 1 \
    --subnet-id subnet-08fc749671b2d077c \
    --key-name MyKeyPair \
    --security-group-ids sg-0b0384b66d7d692f9 \
    --credit-specification CpuCredits=unlimited
```

For an example of the output for `run-instances`, see Example 1.

For more information about burstable performance instances, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) in the *Amazon EC2 User Guide*.

## Output

ReservationId -> (string)

The ID of the reservation.

OwnerId -> (string)

The ID of the Amazon Web Services account that owns the reservation.

RequesterId -> (string)

The ID of the requester that launched the instances on your behalf (for example, Amazon Web Services Management Console or Auto Scaling).

Groups -> (list)

Not supported.

(structure)

Describes a security group.

GroupId -> (string)

The ID of the security group.

GroupName -> (string)

The name of the security group.

Instances -> (list)

The instances.

(structure)

Describes an instance.

Architecture -> (string)

The architecture of the image.

BlockDeviceMappings -> (list)

Any block device mapping entries for the instance.

(structure)

Describes a block device mapping.

DeviceName -> (string)

The device name (for example, `/dev/sdh` or `xvdh` ).

Ebs -> (structure)

Parameters used to automatically set up EBS volumes when the instance is launched.

AttachTime -> (timestamp)

The time stamp when the attachment initiated.

DeleteOnTermination -> (boolean)

Indicates whether the volume is deleted on instance termination.

Status -> (string)

The attachment state.

VolumeId -> (string)

The ID of the EBS volume.

AssociatedResource -> (string)

The ARN of the Amazon ECS or Fargate task to which the volume is attached.

VolumeOwnerId -> (string)

The ID of the Amazon Web Services account that owns the volume.

This parameter is returned only for volumes that are attached to Fargate tasks.

Operator -> (structure)

The service provider that manages the EBS volume.

Managed -> (boolean)

If `true` , the resource is managed by a service provider.

Principal -> (string)

If `managed` is `true` , then the principal is returned. The principal is the service provider that manages the resource.

ClientToken -> (string)

The idempotency token you provided when you launched the instance, if applicable.

EbsOptimized -> (boolean)

Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isnât available with all instance types. Additional usage charges apply when using an EBS Optimized instance.

EnaSupport -> (boolean)

Specifies whether enhanced networking with ENA is enabled.

Hypervisor -> (string)

The hypervisor type of the instance. The value `xen` is used for both Xen and Nitro hypervisors.

IamInstanceProfile -> (structure)

The IAM instance profile associated with the instance, if applicable.

Arn -> (string)

The Amazon Resource Name (ARN) of the instance profile.

Id -> (string)

The ID of the instance profile.

InstanceLifecycle -> (string)

Indicates whether this is a Spot Instance or a Scheduled Instance.

ElasticGpuAssociations -> (list)

Deprecated.

### Note

Amazon Elastic Graphics reached end of life on January 8, 2024.

(structure)

### Note

Amazon Elastic Graphics reached end of life on January 8, 2024.

Describes the association between an instance and an Elastic Graphics accelerator.

ElasticGpuId -> (string)

The ID of the Elastic Graphics accelerator.

ElasticGpuAssociationId -> (string)

The ID of the association.

ElasticGpuAssociationState -> (string)

The state of the association between the instance and the Elastic Graphics accelerator.

ElasticGpuAssociationTime -> (string)

The time the Elastic Graphics accelerator was associated with the instance.

ElasticInferenceAcceleratorAssociations -> (list)

Deprecated

### Note

Amazon Elastic Inference is no longer available.

(structure)

### Note

Amazon Elastic Inference is no longer available.

Describes the association between an instance and an elastic inference accelerator.

ElasticInferenceAcceleratorArn -> (string)

The Amazon Resource Name (ARN) of the elastic inference accelerator.

ElasticInferenceAcceleratorAssociationId -> (string)

The ID of the association.

ElasticInferenceAcceleratorAssociationState -> (string)

The state of the elastic inference accelerator.

ElasticInferenceAcceleratorAssociationTime -> (timestamp)

The time at which the elastic inference accelerator is associated with an instance.

NetworkInterfaces -> (list)

The network interfaces for the instance.

(structure)

Describes a network interface.

Association -> (structure)

The association information for an Elastic IPv4 associated with the network interface.

CarrierIp -> (string)

The carrier IP address associated with the network interface.

CustomerOwnedIp -> (string)

The customer-owned IP address associated with the network interface.

IpOwnerId -> (string)

The ID of the owner of the Elastic IP address.

PublicDnsName -> (string)

The public DNS name.

PublicIp -> (string)

The public IP address or Elastic IP address bound to the network interface.

Attachment -> (structure)

The network interface attachment.

AttachTime -> (timestamp)

The time stamp when the attachment initiated.

AttachmentId -> (string)

The ID of the network interface attachment.

DeleteOnTermination -> (boolean)

Indicates whether the network interface is deleted when the instance is terminated.

DeviceIndex -> (integer)

The index of the device on the instance for the network interface attachment.

Status -> (string)

The attachment state.

NetworkCardIndex -> (integer)

The index of the network card.

EnaSrdSpecification -> (structure)

Contains the ENA Express settings for the network interface thatâs attached to the instance.

EnaSrdEnabled -> (boolean)

Indicates whether ENA Express is enabled for the network interface.

EnaSrdUdpSpecification -> (structure)

Configures ENA Express for UDP network traffic.

EnaSrdUdpEnabled -> (boolean)

Indicates whether UDP traffic to and from the instance uses ENA Express. To specify this setting, you must first enable ENA Express.

EnaQueueCount -> (integer)

The number of ENA queues created with the instance.

Description -> (string)

The description.

Groups -> (list)

The security groups.

(structure)

Describes a security group.

GroupId -> (string)

The ID of the security group.

GroupName -> (string)

The name of the security group.

Ipv6Addresses -> (list)

The IPv6 addresses associated with the network interface.

(structure)

Describes an IPv6 address.

Ipv6Address -> (string)

The IPv6 address.

IsPrimaryIpv6 -> (boolean)

Determines if an IPv6 address associated with a network interface is the primary IPv6 address. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information, see [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) .

MacAddress -> (string)

The MAC address.

NetworkInterfaceId -> (string)

The ID of the network interface.

OwnerId -> (string)

The ID of the Amazon Web Services account that created the network interface.

PrivateDnsName -> (string)

The private DNS name.

PrivateIpAddress -> (string)

The IPv4 address of the network interface within the subnet.

PrivateIpAddresses -> (list)

The private IPv4 addresses associated with the network interface.

(structure)

Describes a private IPv4 address.

Association -> (structure)

The association information for an Elastic IP address for the network interface.

CarrierIp -> (string)

The carrier IP address associated with the network interface.

CustomerOwnedIp -> (string)

The customer-owned IP address associated with the network interface.

IpOwnerId -> (string)

The ID of the owner of the Elastic IP address.

PublicDnsName -> (string)

The public DNS name.

PublicIp -> (string)

The public IP address or Elastic IP address bound to the network interface.

Primary -> (boolean)

Indicates whether this IPv4 address is the primary private IP address of the network interface.

PrivateDnsName -> (string)

The private IPv4 DNS name.

PrivateIpAddress -> (string)

The private IPv4 address of the network interface.

SourceDestCheck -> (boolean)

Indicates whether source/destination checking is enabled.

Status -> (string)

The status of the network interface.

SubnetId -> (string)

The ID of the subnet.

VpcId -> (string)

The ID of the VPC.

InterfaceType -> (string)

The type of network interface.

Valid values: `interface` | `efa` | `efa-only` | `trunk`

Ipv4Prefixes -> (list)

The IPv4 delegated prefixes that are assigned to the network interface.

(structure)

Information about an IPv4 prefix.

Ipv4Prefix -> (string)

One or more IPv4 prefixes assigned to the network interface.

Ipv6Prefixes -> (list)

The IPv6 delegated prefixes that are assigned to the network interface.

(structure)

Information about an IPv6 prefix.

Ipv6Prefix -> (string)

One or more IPv6 prefixes assigned to the network interface.

ConnectionTrackingConfiguration -> (structure)

A security group connection tracking configuration that enables you to set the timeout for connection tracking on an Elastic network interface. For more information, see [Connection tracking timeouts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts) in the *Amazon EC2 User Guide* .

TcpEstablishedTimeout -> (integer)

Timeout (in seconds) for idle TCP connections in an established state. Min: 60 seconds. Max: 432000 seconds (5 days). Default: 432000 seconds. Recommended: Less than 432000 seconds.

UdpStreamTimeout -> (integer)

Timeout (in seconds) for idle UDP flows classified as streams which have seen more than one request-response transaction. Min: 60 seconds. Max: 180 seconds (3 minutes). Default: 180 seconds.

UdpTimeout -> (integer)

Timeout (in seconds) for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction. Min: 30 seconds. Max: 60 seconds. Default: 30 seconds.

Operator -> (structure)

The service provider that manages the network interface.

Managed -> (boolean)

If `true` , the resource is managed by a service provider.

Principal -> (string)

If `managed` is `true` , then the principal is returned. The principal is the service provider that manages the resource.

OutpostArn -> (string)

The Amazon Resource Name (ARN) of the Outpost.

RootDeviceName -> (string)

The device name of the root device volume (for example, `/dev/sda1` ).

RootDeviceType -> (string)

The root device type used by the AMI. The AMI can use an EBS volume or an instance store volume.

SecurityGroups -> (list)

The security groups for the instance.

(structure)

Describes a security group.

GroupId -> (string)

The ID of the security group.

GroupName -> (string)

The name of the security group.

SourceDestCheck -> (boolean)

Indicates whether source/destination checking is enabled.

SpotInstanceRequestId -> (string)

If the request is a Spot Instance request, the ID of the request.

SriovNetSupport -> (string)

Specifies whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.

StateReason -> (structure)

The reason for the most recent state transition.

Code -> (string)

The reason code for the state change.

Message -> (string)

The message for the state change.

- `Server.InsufficientInstanceCapacity` : There was insufficient capacity available to satisfy the launch request.
- `Server.InternalError` : An internal error caused the instance to terminate during launch.
- `Server.ScheduledStop` : The instance was stopped due to a scheduled retirement.
- `Server.SpotInstanceShutdown` : The instance was stopped because the number of Spot requests with a maximum price equal to or higher than the Spot price exceeded available capacity or because of an increase in the Spot price.
- `Server.SpotInstanceTermination` : The instance was terminated because the number of Spot requests with a maximum price equal to or higher than the Spot price exceeded available capacity or because of an increase in the Spot price.
- `Client.InstanceInitiatedShutdown` : The instance was shut down from the operating system of the instance.
- `Client.InstanceTerminated` : The instance was terminated or rebooted during AMI creation.
- `Client.InternalError` : A client error caused the instance to terminate during launch.
- `Client.InvalidSnapshot.NotFound` : The specified snapshot was not found.
- `Client.UserInitiatedHibernate` : Hibernation was initiated on the instance.
- `Client.UserInitiatedShutdown` : The instance was shut down using the Amazon EC2 API.
- `Client.VolumeLimitExceeded` : The limit on the number of EBS volumes or total storage was exceeded. Decrease usage or request an increase in your account limits.

Tags -> (list)

Any tags assigned to the instance.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

VirtualizationType -> (string)

The virtualization type of the instance.

CpuOptions -> (structure)

The CPU options for the instance.

CoreCount -> (integer)

The number of CPU cores for the instance.

ThreadsPerCore -> (integer)

The number of threads per CPU core.

AmdSevSnp -> (string)

Indicates whether the instance is enabled for AMD SEV-SNP. For more information, see [AMD SEV-SNP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html) .

CapacityReservationId -> (string)

The ID of the Capacity Reservation.

CapacityReservationSpecification -> (structure)

Information about the Capacity Reservation targeting option.

CapacityReservationPreference -> (string)

Describes the instanceâs Capacity Reservation preferences. Possible preferences include:

- `open` - The instance can run in any `open` Capacity Reservation that has matching attributes (instance type, platform, Availability Zone).
- `none` - The instance avoids running in a Capacity Reservation even if one is available. The instance runs in On-Demand capacity.

CapacityReservationTarget -> (structure)

Information about the targeted Capacity Reservation or Capacity Reservation group.

CapacityReservationId -> (string)

The ID of the targeted Capacity Reservation.

CapacityReservationResourceGroupArn -> (string)

The ARN of the targeted Capacity Reservation group.

HibernationOptions -> (structure)

Indicates whether the instance is enabled for hibernation.

Configured -> (boolean)

If `true` , your instance is enabled for hibernation; otherwise, it is not enabled for hibernation.

Licenses -> (list)

The license configurations for the instance.

(structure)

Describes a license configuration.

LicenseConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the license configuration.

MetadataOptions -> (structure)

The metadata options for the instance.

State -> (string)

The state of the metadata option changes.

`pending` - The metadata options are being updated and the instance is not ready to process metadata traffic with the new selection.

`applied` - The metadata options have been successfully applied on the instance.

HttpTokens -> (string)

Indicates whether IMDSv2 is required.

- `optional` - IMDSv2 is optional, which means that you can use either IMDSv2 or IMDSv1.
- `required` - IMDSv2 is required, which means that IMDSv1 is disabled, and you must use IMDSv2.

HttpPutResponseHopLimit -> (integer)

The maximum number of hops that the metadata token can travel.

Possible values: Integers from `1` to `64`

HttpEndpoint -> (string)

Indicates whether the HTTP metadata endpoint on your instances is enabled or disabled.

If the value is `disabled` , you cannot access your instance metadata.

HttpProtocolIpv6 -> (string)

Indicates whether the IPv6 endpoint for the instance metadata service is enabled or disabled.

Default: `disabled`

InstanceMetadataTags -> (string)

Indicates whether access to instance tags from the instance metadata is enabled or disabled. For more information, see [Work with instance tags using the instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#work-with-tags-in-IMDS) .

EnclaveOptions -> (structure)

Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves.

Enabled -> (boolean)

If this parameter is set to `true` , the instance is enabled for Amazon Web Services Nitro Enclaves; otherwise, it is not enabled for Amazon Web Services Nitro Enclaves.

BootMode -> (string)

The boot mode that was specified by the AMI. If the value is `uefi-preferred` , the AMI supports both UEFI and Legacy BIOS. The `currentInstanceBootMode` parameter is the boot mode that is used to boot the instance at launch or start.

### Note

The operating system contained in the AMI must be configured to support the specified boot mode.

For more information, see [Boot modes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html) in the *Amazon EC2 User Guide* .

PlatformDetails -> (string)

The platform details value for the instance. For more information, see [AMI billing information fields](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-info-fields.html) in the *Amazon EC2 User Guide* .

UsageOperation -> (string)

The usage operation value for the instance. For more information, see [AMI billing information fields](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-info-fields.html) in the *Amazon EC2 User Guide* .

UsageOperationUpdateTime -> (timestamp)

The time that the usage operation was last updated.

PrivateDnsNameOptions -> (structure)

The options for the instance hostname.

HostnameType -> (string)

The type of hostname to assign to an instance.

EnableResourceNameDnsARecord -> (boolean)

Indicates whether to respond to DNS queries for instance hostnames with DNS A records.

EnableResourceNameDnsAAAARecord -> (boolean)

Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.

Ipv6Address -> (string)

The IPv6 address assigned to the instance.

TpmSupport -> (string)

If the instance is configured for NitroTPM support, the value is `v2.0` . For more information, see [NitroTPM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html) in the *Amazon EC2 User Guide* .

MaintenanceOptions -> (structure)

Provides information on the recovery and maintenance options of your instance.

AutoRecovery -> (string)

Provides information on the current automatic recovery behavior of your instance.

RebootMigration -> (string)

Specifies whether to attempt reboot migration during a user-initiated reboot of an instance that has a scheduled `system-reboot` event:

- `default` - Amazon EC2 attempts to migrate the instance to new hardware (reboot migration). If successful, the `system-reboot` event is cleared. If unsuccessful, an in-place reboot occurs and the event remains scheduled.
- `disabled` - Amazon EC2 keeps the instance on the same hardware (in-place reboot). The `system-reboot` event remains scheduled.

This setting only applies to supported instances that have a scheduled reboot event. For more information, see [Enable or disable reboot migration](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/schedevents_actions_reboot.html#reboot-migration) in the *Amazon EC2 User Guide* .

CurrentInstanceBootMode -> (string)

The boot mode that is used to boot the instance at launch or start. For more information, see [Boot modes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html) in the *Amazon EC2 User Guide* .

NetworkPerformanceOptions -> (structure)

Contains settings for the network performance options for your instance.

BandwidthWeighting -> (string)

When you configure network bandwidth weighting, you can boost your baseline bandwidth for either networking or EBS by up to 25%. The total available baseline bandwidth for your instance remains the same. The default option uses the standard bandwidth configuration for your instance type.

Operator -> (structure)

The service provider that manages the instance.

Managed -> (boolean)

If `true` , the resource is managed by a service provider.

Principal -> (string)

If `managed` is `true` , then the principal is returned. The principal is the service provider that manages the resource.

InstanceId -> (string)

The ID of the instance.

ImageId -> (string)

The ID of the AMI used to launch the instance.

State -> (structure)

The current state of the instance.

Code -> (integer)

The state of the instance as a 16-bit unsigned integer.

The high byte is all of the bits between 2^8 and (2^16)-1, which equals decimal values between 256 and 65,535. These numerical values are used for internal purposes and should be ignored.

The low byte is all of the bits between 2^0 and (2^8)-1, which equals decimal values between 0 and 255.

The valid values for instance-state-code will all be in the range of the low byte and they are:

- `0` : `pending`
- `16` : `running`
- `32` : `shutting-down`
- `48` : `terminated`
- `64` : `stopping`
- `80` : `stopped`

You can ignore the high byte value by zeroing out all of the bits above 2^8 or 256 in decimal.

Name -> (string)

The current state of the instance.

PrivateDnsName -> (string)

[IPv4 only] The private DNS hostname name assigned to the instance. This DNS hostname can only be used inside the Amazon EC2 network. This name is not available until the instance enters the `running` state.

The Amazon-provided DNS server resolves Amazon-provided private DNS hostnames if youâve enabled DNS resolution and DNS hostnames in your VPC. If you are not using the Amazon-provided DNS server in your VPC, your custom domain name servers must resolve the hostname as appropriate.

PublicDnsName -> (string)

[IPv4 only] The public DNS name assigned to the instance. This name is not available until the instance enters the `running` state. This name is only available if youâve enabled DNS hostnames for your VPC.

StateTransitionReason -> (string)

The reason for the most recent state transition. This might be an empty string.

KeyName -> (string)

The name of the key pair, if this instance was launched with an associated key pair.

AmiLaunchIndex -> (integer)

The AMI launch index, which can be used to find this instance in the launch group.

ProductCodes -> (list)

The product codes attached to this instance, if applicable.

(structure)

Describes a product code.

ProductCodeId -> (string)

The product code.

ProductCodeType -> (string)

The type of product code.

InstanceType -> (string)

The instance type.

LaunchTime -> (timestamp)

The time that the instance was last launched. To determine the time that instance was first launched, see the attachment time for the primary network interface.

Placement -> (structure)

The location where the instance launched, if applicable.

Affinity -> (string)

The affinity setting for the instance on the Dedicated Host.

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) or [ImportInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html) .

GroupName -> (string)

The name of the placement group that the instance is in. If you specify `GroupName` , you canât specify `GroupId` .

PartitionNumber -> (integer)

The number of the partition that the instance is in. Valid only if the placement group strategy is set to `partition` .

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) .

HostId -> (string)

The ID of the Dedicated Host on which the instance resides.

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) or [ImportInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html) .

Tenancy -> (string)

The tenancy of the instance. An instance with a tenancy of `dedicated` runs on single-tenant hardware.

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) . The `host` tenancy is not supported for [ImportInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html) or for T3 instances that are configured for the `unlimited` CPU credit option.

SpreadDomain -> (string)

Reserved for future use.

HostResourceGroupArn -> (string)

The ARN of the host resource group in which to launch the instances.

If you specify this parameter, either omit the **Tenancy** parameter or set it to `host` .

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) .

GroupId -> (string)

The ID of the placement group that the instance is in. If you specify `GroupId` , you canât specify `GroupName` .

AvailabilityZone -> (string)

The Availability Zone of the instance.

If not specified, an Availability Zone will be automatically chosen for you based on the load balancing criteria for the Region.

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) .

KernelId -> (string)

The kernel associated with this instance, if applicable.

RamdiskId -> (string)

The RAM disk associated with this instance, if applicable.

Platform -> (string)

The platform. This value is `windows` for Windows instances; otherwise, it is empty.

Monitoring -> (structure)

The monitoring for the instance.

State -> (string)

Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.

SubnetId -> (string)

The ID of the subnet in which the instance is running.

VpcId -> (string)

The ID of the VPC in which the instance is running.

PrivateIpAddress -> (string)

The private IPv4 address assigned to the instance.

PublicIpAddress -> (string)

The public IPv4 address, or the Carrier IP address assigned to the instance, if applicable.

A Carrier IP address only applies to an instance launched in a subnet associated with a Wavelength Zone.