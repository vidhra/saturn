# request-spot-instancesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/request-spot-instances.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/request-spot-instances.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# request-spot-instances

## Description

Creates a Spot Instance request.

For more information, see [Work with Spot Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html) in the *Amazon EC2 User Guide* .

### Warning

We strongly discourage using the RequestSpotInstances API because it is a legacy API with no planned investment. For options for requesting Spot Instances, see [Which is the best Spot request method to use?](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html#which-spot-request-method-to-use) in the *Amazon EC2 User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/RequestSpotInstances)

## Synopsis

```
request-spot-instances
[--launch-specification <value>]
[--tag-specifications <value>]
[--instance-interruption-behavior <value>]
[--dry-run | --no-dry-run]
[--spot-price <value>]
[--client-token <value>]
[--instance-count <value>]
[--type <value>]
[--valid-from <value>]
[--valid-until <value>]
[--launch-group <value>]
[--availability-zone-group <value>]
[--block-duration-minutes <value>]
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

`--launch-specification` (structure)

The launch specification.

SecurityGroupIds -> (list)

The IDs of the security groups.

(string)

SecurityGroups -> (list)

Not supported.

(string)

AddressingType -> (string)

Deprecated.

BlockDeviceMappings -> (list)

The block device mapping entries. You canât specify both a snapshot ID and an encryption value. This is because only blank volumes can be encrypted on creation. If a snapshot is the basis for a volume, it is not blank and its encryption status is used for the volume encryption status.

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

EbsOptimized -> (boolean)

Indicates whether the instance is optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isnât available with all instance types. Additional usage charges apply when using an EBS Optimized instance.

Default: `false`

IamInstanceProfile -> (structure)

The IAM instance profile.

Arn -> (string)

The Amazon Resource Name (ARN) of the instance profile.

Name -> (string)

The name of the instance profile.

ImageId -> (string)

The ID of the AMI.

InstanceType -> (string)

The instance type. Only one instance type can be specified.

KernelId -> (string)

The ID of the kernel.

KeyName -> (string)

The name of the key pair.

Monitoring -> (structure)

Indicates whether basic or detailed monitoring is enabled for the instance.

Default: Disabled

Enabled -> (boolean)

Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.

NetworkInterfaces -> (list)

The network interfaces. If you specify a network interface, you must specify subnet IDs and security group IDs using the network interface.

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

Placement -> (structure)

The placement information for the instance.

AvailabilityZone -> (string)

The Availability Zone.

[Spot Fleet only] To specify multiple Availability Zones, separate them using commas; for example, âus-west-2a, us-west-2bâ.

GroupName -> (string)

The name of the placement group.

Tenancy -> (string)

The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of `dedicated` runs on single-tenant hardware. The `host` tenancy is not supported for Spot Instances.

RamdiskId -> (string)

The ID of the RAM disk.

SubnetId -> (string)

The ID of the subnet in which to launch the instance.

UserData -> (string)

The base64-encoded user data that instances use when starting up. User data is limited to 16 KB.

JSON Syntax:

```
{
  "SecurityGroupIds": ["string", ...],
  "SecurityGroups": ["string", ...],
  "AddressingType": "string",
  "BlockDeviceMappings": [
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
  ],
  "EbsOptimized": true|false,
  "IamInstanceProfile": {
    "Arn": "string",
    "Name": "string"
  },
  "ImageId": "string",
  "InstanceType": "a1.medium"|"a1.large"|"a1.xlarge"|"a1.2xlarge"|"a1.4xlarge"|"a1.metal"|"c1.medium"|"c1.xlarge"|"c3.large"|"c3.xlarge"|"c3.2xlarge"|"c3.4xlarge"|"c3.8xlarge"|"c4.large"|"c4.xlarge"|"c4.2xlarge"|"c4.4xlarge"|"c4.8xlarge"|"c5.large"|"c5.xlarge"|"c5.2xlarge"|"c5.4xlarge"|"c5.9xlarge"|"c5.12xlarge"|"c5.18xlarge"|"c5.24xlarge"|"c5.metal"|"c5a.large"|"c5a.xlarge"|"c5a.2xlarge"|"c5a.4xlarge"|"c5a.8xlarge"|"c5a.12xlarge"|"c5a.16xlarge"|"c5a.24xlarge"|"c5ad.large"|"c5ad.xlarge"|"c5ad.2xlarge"|"c5ad.4xlarge"|"c5ad.8xlarge"|"c5ad.12xlarge"|"c5ad.16xlarge"|"c5ad.24xlarge"|"c5d.large"|"c5d.xlarge"|"c5d.2xlarge"|"c5d.4xlarge"|"c5d.9xlarge"|"c5d.12xlarge"|"c5d.18xlarge"|"c5d.24xlarge"|"c5d.metal"|"c5n.large"|"c5n.xlarge"|"c5n.2xlarge"|"c5n.4xlarge"|"c5n.9xlarge"|"c5n.18xlarge"|"c5n.metal"|"c6g.medium"|"c6g.large"|"c6g.xlarge"|"c6g.2xlarge"|"c6g.4xlarge"|"c6g.8xlarge"|"c6g.12xlarge"|"c6g.16xlarge"|"c6g.metal"|"c6gd.medium"|"c6gd.large"|"c6gd.xlarge"|"c6gd.2xlarge"|"c6gd.4xlarge"|"c6gd.8xlarge"|"c6gd.12xlarge"|"c6gd.16xlarge"|"c6gd.metal"|"c6gn.medium"|"c6gn.large"|"c6gn.xlarge"|"c6gn.2xlarge"|"c6gn.4xlarge"|"c6gn.8xlarge"|"c6gn.12xlarge"|"c6gn.16xlarge"|"c6i.large"|"c6i.xlarge"|"c6i.2xlarge"|"c6i.4xlarge"|"c6i.8xlarge"|"c6i.12xlarge"|"c6i.16xlarge"|"c6i.24xlarge"|"c6i.32xlarge"|"c6i.metal"|"cc1.4xlarge"|"cc2.8xlarge"|"cg1.4xlarge"|"cr1.8xlarge"|"d2.xlarge"|"d2.2xlarge"|"d2.4xlarge"|"d2.8xlarge"|"d3.xlarge"|"d3.2xlarge"|"d3.4xlarge"|"d3.8xlarge"|"d3en.xlarge"|"d3en.2xlarge"|"d3en.4xlarge"|"d3en.6xlarge"|"d3en.8xlarge"|"d3en.12xlarge"|"dl1.24xlarge"|"f1.2xlarge"|"f1.4xlarge"|"f1.16xlarge"|"g2.2xlarge"|"g2.8xlarge"|"g3.4xlarge"|"g3.8xlarge"|"g3.16xlarge"|"g3s.xlarge"|"g4ad.xlarge"|"g4ad.2xlarge"|"g4ad.4xlarge"|"g4ad.8xlarge"|"g4ad.16xlarge"|"g4dn.xlarge"|"g4dn.2xlarge"|"g4dn.4xlarge"|"g4dn.8xlarge"|"g4dn.12xlarge"|"g4dn.16xlarge"|"g4dn.metal"|"g5.xlarge"|"g5.2xlarge"|"g5.4xlarge"|"g5.8xlarge"|"g5.12xlarge"|"g5.16xlarge"|"g5.24xlarge"|"g5.48xlarge"|"g5g.xlarge"|"g5g.2xlarge"|"g5g.4xlarge"|"g5g.8xlarge"|"g5g.16xlarge"|"g5g.metal"|"hi1.4xlarge"|"hpc6a.48xlarge"|"hs1.8xlarge"|"h1.2xlarge"|"h1.4xlarge"|"h1.8xlarge"|"h1.16xlarge"|"i2.xlarge"|"i2.2xlarge"|"i2.4xlarge"|"i2.8xlarge"|"i3.large"|"i3.xlarge"|"i3.2xlarge"|"i3.4xlarge"|"i3.8xlarge"|"i3.16xlarge"|"i3.metal"|"i3en.large"|"i3en.xlarge"|"i3en.2xlarge"|"i3en.3xlarge"|"i3en.6xlarge"|"i3en.12xlarge"|"i3en.24xlarge"|"i3en.metal"|"im4gn.large"|"im4gn.xlarge"|"im4gn.2xlarge"|"im4gn.4xlarge"|"im4gn.8xlarge"|"im4gn.16xlarge"|"inf1.xlarge"|"inf1.2xlarge"|"inf1.6xlarge"|"inf1.24xlarge"|"is4gen.medium"|"is4gen.large"|"is4gen.xlarge"|"is4gen.2xlarge"|"is4gen.4xlarge"|"is4gen.8xlarge"|"m1.small"|"m1.medium"|"m1.large"|"m1.xlarge"|"m2.xlarge"|"m2.2xlarge"|"m2.4xlarge"|"m3.medium"|"m3.large"|"m3.xlarge"|"m3.2xlarge"|"m4.large"|"m4.xlarge"|"m4.2xlarge"|"m4.4xlarge"|"m4.10xlarge"|"m4.16xlarge"|"m5.large"|"m5.xlarge"|"m5.2xlarge"|"m5.4xlarge"|"m5.8xlarge"|"m5.12xlarge"|"m5.16xlarge"|"m5.24xlarge"|"m5.metal"|"m5a.large"|"m5a.xlarge"|"m5a.2xlarge"|"m5a.4xlarge"|"m5a.8xlarge"|"m5a.12xlarge"|"m5a.16xlarge"|"m5a.24xlarge"|"m5ad.large"|"m5ad.xlarge"|"m5ad.2xlarge"|"m5ad.4xlarge"|"m5ad.8xlarge"|"m5ad.12xlarge"|"m5ad.16xlarge"|"m5ad.24xlarge"|"m5d.large"|"m5d.xlarge"|"m5d.2xlarge"|"m5d.4xlarge"|"m5d.8xlarge"|"m5d.12xlarge"|"m5d.16xlarge"|"m5d.24xlarge"|"m5d.metal"|"m5dn.large"|"m5dn.xlarge"|"m5dn.2xlarge"|"m5dn.4xlarge"|"m5dn.8xlarge"|"m5dn.12xlarge"|"m5dn.16xlarge"|"m5dn.24xlarge"|"m5dn.metal"|"m5n.large"|"m5n.xlarge"|"m5n.2xlarge"|"m5n.4xlarge"|"m5n.8xlarge"|"m5n.12xlarge"|"m5n.16xlarge"|"m5n.24xlarge"|"m5n.metal"|"m5zn.large"|"m5zn.xlarge"|"m5zn.2xlarge"|"m5zn.3xlarge"|"m5zn.6xlarge"|"m5zn.12xlarge"|"m5zn.metal"|"m6a.large"|"m6a.xlarge"|"m6a.2xlarge"|"m6a.4xlarge"|"m6a.8xlarge"|"m6a.12xlarge"|"m6a.16xlarge"|"m6a.24xlarge"|"m6a.32xlarge"|"m6a.48xlarge"|"m6g.metal"|"m6g.medium"|"m6g.large"|"m6g.xlarge"|"m6g.2xlarge"|"m6g.4xlarge"|"m6g.8xlarge"|"m6g.12xlarge"|"m6g.16xlarge"|"m6gd.metal"|"m6gd.medium"|"m6gd.large"|"m6gd.xlarge"|"m6gd.2xlarge"|"m6gd.4xlarge"|"m6gd.8xlarge"|"m6gd.12xlarge"|"m6gd.16xlarge"|"m6i.large"|"m6i.xlarge"|"m6i.2xlarge"|"m6i.4xlarge"|"m6i.8xlarge"|"m6i.12xlarge"|"m6i.16xlarge"|"m6i.24xlarge"|"m6i.32xlarge"|"m6i.metal"|"mac1.metal"|"p2.xlarge"|"p2.8xlarge"|"p2.16xlarge"|"p3.2xlarge"|"p3.8xlarge"|"p3.16xlarge"|"p3dn.24xlarge"|"p4d.24xlarge"|"r3.large"|"r3.xlarge"|"r3.2xlarge"|"r3.4xlarge"|"r3.8xlarge"|"r4.large"|"r4.xlarge"|"r4.2xlarge"|"r4.4xlarge"|"r4.8xlarge"|"r4.16xlarge"|"r5.large"|"r5.xlarge"|"r5.2xlarge"|"r5.4xlarge"|"r5.8xlarge"|"r5.12xlarge"|"r5.16xlarge"|"r5.24xlarge"|"r5.metal"|"r5a.large"|"r5a.xlarge"|"r5a.2xlarge"|"r5a.4xlarge"|"r5a.8xlarge"|"r5a.12xlarge"|"r5a.16xlarge"|"r5a.24xlarge"|"r5ad.large"|"r5ad.xlarge"|"r5ad.2xlarge"|"r5ad.4xlarge"|"r5ad.8xlarge"|"r5ad.12xlarge"|"r5ad.16xlarge"|"r5ad.24xlarge"|"r5b.large"|"r5b.xlarge"|"r5b.2xlarge"|"r5b.4xlarge"|"r5b.8xlarge"|"r5b.12xlarge"|"r5b.16xlarge"|"r5b.24xlarge"|"r5b.metal"|"r5d.large"|"r5d.xlarge"|"r5d.2xlarge"|"r5d.4xlarge"|"r5d.8xlarge"|"r5d.12xlarge"|"r5d.16xlarge"|"r5d.24xlarge"|"r5d.metal"|"r5dn.large"|"r5dn.xlarge"|"r5dn.2xlarge"|"r5dn.4xlarge"|"r5dn.8xlarge"|"r5dn.12xlarge"|"r5dn.16xlarge"|"r5dn.24xlarge"|"r5dn.metal"|"r5n.large"|"r5n.xlarge"|"r5n.2xlarge"|"r5n.4xlarge"|"r5n.8xlarge"|"r5n.12xlarge"|"r5n.16xlarge"|"r5n.24xlarge"|"r5n.metal"|"r6g.medium"|"r6g.large"|"r6g.xlarge"|"r6g.2xlarge"|"r6g.4xlarge"|"r6g.8xlarge"|"r6g.12xlarge"|"r6g.16xlarge"|"r6g.metal"|"r6gd.medium"|"r6gd.large"|"r6gd.xlarge"|"r6gd.2xlarge"|"r6gd.4xlarge"|"r6gd.8xlarge"|"r6gd.12xlarge"|"r6gd.16xlarge"|"r6gd.metal"|"r6i.large"|"r6i.xlarge"|"r6i.2xlarge"|"r6i.4xlarge"|"r6i.8xlarge"|"r6i.12xlarge"|"r6i.16xlarge"|"r6i.24xlarge"|"r6i.32xlarge"|"r6i.metal"|"t1.micro"|"t2.nano"|"t2.micro"|"t2.small"|"t2.medium"|"t2.large"|"t2.xlarge"|"t2.2xlarge"|"t3.nano"|"t3.micro"|"t3.small"|"t3.medium"|"t3.large"|"t3.xlarge"|"t3.2xlarge"|"t3a.nano"|"t3a.micro"|"t3a.small"|"t3a.medium"|"t3a.large"|"t3a.xlarge"|"t3a.2xlarge"|"t4g.nano"|"t4g.micro"|"t4g.small"|"t4g.medium"|"t4g.large"|"t4g.xlarge"|"t4g.2xlarge"|"u-6tb1.56xlarge"|"u-6tb1.112xlarge"|"u-9tb1.112xlarge"|"u-12tb1.112xlarge"|"u-6tb1.metal"|"u-9tb1.metal"|"u-12tb1.metal"|"u-18tb1.metal"|"u-24tb1.metal"|"vt1.3xlarge"|"vt1.6xlarge"|"vt1.24xlarge"|"x1.16xlarge"|"x1.32xlarge"|"x1e.xlarge"|"x1e.2xlarge"|"x1e.4xlarge"|"x1e.8xlarge"|"x1e.16xlarge"|"x1e.32xlarge"|"x2iezn.2xlarge"|"x2iezn.4xlarge"|"x2iezn.6xlarge"|"x2iezn.8xlarge"|"x2iezn.12xlarge"|"x2iezn.metal"|"x2gd.medium"|"x2gd.large"|"x2gd.xlarge"|"x2gd.2xlarge"|"x2gd.4xlarge"|"x2gd.8xlarge"|"x2gd.12xlarge"|"x2gd.16xlarge"|"x2gd.metal"|"z1d.large"|"z1d.xlarge"|"z1d.2xlarge"|"z1d.3xlarge"|"z1d.6xlarge"|"z1d.12xlarge"|"z1d.metal"|"x2idn.16xlarge"|"x2idn.24xlarge"|"x2idn.32xlarge"|"x2iedn.xlarge"|"x2iedn.2xlarge"|"x2iedn.4xlarge"|"x2iedn.8xlarge"|"x2iedn.16xlarge"|"x2iedn.24xlarge"|"x2iedn.32xlarge"|"c6a.large"|"c6a.xlarge"|"c6a.2xlarge"|"c6a.4xlarge"|"c6a.8xlarge"|"c6a.12xlarge"|"c6a.16xlarge"|"c6a.24xlarge"|"c6a.32xlarge"|"c6a.48xlarge"|"c6a.metal"|"m6a.metal"|"i4i.large"|"i4i.xlarge"|"i4i.2xlarge"|"i4i.4xlarge"|"i4i.8xlarge"|"i4i.16xlarge"|"i4i.32xlarge"|"i4i.metal"|"x2idn.metal"|"x2iedn.metal"|"c7g.medium"|"c7g.large"|"c7g.xlarge"|"c7g.2xlarge"|"c7g.4xlarge"|"c7g.8xlarge"|"c7g.12xlarge"|"c7g.16xlarge"|"mac2.metal"|"c6id.large"|"c6id.xlarge"|"c6id.2xlarge"|"c6id.4xlarge"|"c6id.8xlarge"|"c6id.12xlarge"|"c6id.16xlarge"|"c6id.24xlarge"|"c6id.32xlarge"|"c6id.metal"|"m6id.large"|"m6id.xlarge"|"m6id.2xlarge"|"m6id.4xlarge"|"m6id.8xlarge"|"m6id.12xlarge"|"m6id.16xlarge"|"m6id.24xlarge"|"m6id.32xlarge"|"m6id.metal"|"r6id.large"|"r6id.xlarge"|"r6id.2xlarge"|"r6id.4xlarge"|"r6id.8xlarge"|"r6id.12xlarge"|"r6id.16xlarge"|"r6id.24xlarge"|"r6id.32xlarge"|"r6id.metal"|"r6a.large"|"r6a.xlarge"|"r6a.2xlarge"|"r6a.4xlarge"|"r6a.8xlarge"|"r6a.12xlarge"|"r6a.16xlarge"|"r6a.24xlarge"|"r6a.32xlarge"|"r6a.48xlarge"|"r6a.metal"|"p4de.24xlarge"|"u-3tb1.56xlarge"|"u-18tb1.112xlarge"|"u-24tb1.112xlarge"|"trn1.2xlarge"|"trn1.32xlarge"|"hpc6id.32xlarge"|"c6in.large"|"c6in.xlarge"|"c6in.2xlarge"|"c6in.4xlarge"|"c6in.8xlarge"|"c6in.12xlarge"|"c6in.16xlarge"|"c6in.24xlarge"|"c6in.32xlarge"|"m6in.large"|"m6in.xlarge"|"m6in.2xlarge"|"m6in.4xlarge"|"m6in.8xlarge"|"m6in.12xlarge"|"m6in.16xlarge"|"m6in.24xlarge"|"m6in.32xlarge"|"m6idn.large"|"m6idn.xlarge"|"m6idn.2xlarge"|"m6idn.4xlarge"|"m6idn.8xlarge"|"m6idn.12xlarge"|"m6idn.16xlarge"|"m6idn.24xlarge"|"m6idn.32xlarge"|"r6in.large"|"r6in.xlarge"|"r6in.2xlarge"|"r6in.4xlarge"|"r6in.8xlarge"|"r6in.12xlarge"|"r6in.16xlarge"|"r6in.24xlarge"|"r6in.32xlarge"|"r6idn.large"|"r6idn.xlarge"|"r6idn.2xlarge"|"r6idn.4xlarge"|"r6idn.8xlarge"|"r6idn.12xlarge"|"r6idn.16xlarge"|"r6idn.24xlarge"|"r6idn.32xlarge"|"c7g.metal"|"m7g.medium"|"m7g.large"|"m7g.xlarge"|"m7g.2xlarge"|"m7g.4xlarge"|"m7g.8xlarge"|"m7g.12xlarge"|"m7g.16xlarge"|"m7g.metal"|"r7g.medium"|"r7g.large"|"r7g.xlarge"|"r7g.2xlarge"|"r7g.4xlarge"|"r7g.8xlarge"|"r7g.12xlarge"|"r7g.16xlarge"|"r7g.metal"|"c6in.metal"|"m6in.metal"|"m6idn.metal"|"r6in.metal"|"r6idn.metal"|"inf2.xlarge"|"inf2.8xlarge"|"inf2.24xlarge"|"inf2.48xlarge"|"trn1n.32xlarge"|"i4g.large"|"i4g.xlarge"|"i4g.2xlarge"|"i4g.4xlarge"|"i4g.8xlarge"|"i4g.16xlarge"|"hpc7g.4xlarge"|"hpc7g.8xlarge"|"hpc7g.16xlarge"|"c7gn.medium"|"c7gn.large"|"c7gn.xlarge"|"c7gn.2xlarge"|"c7gn.4xlarge"|"c7gn.8xlarge"|"c7gn.12xlarge"|"c7gn.16xlarge"|"p5.48xlarge"|"m7i.large"|"m7i.xlarge"|"m7i.2xlarge"|"m7i.4xlarge"|"m7i.8xlarge"|"m7i.12xlarge"|"m7i.16xlarge"|"m7i.24xlarge"|"m7i.48xlarge"|"m7i-flex.large"|"m7i-flex.xlarge"|"m7i-flex.2xlarge"|"m7i-flex.4xlarge"|"m7i-flex.8xlarge"|"m7a.medium"|"m7a.large"|"m7a.xlarge"|"m7a.2xlarge"|"m7a.4xlarge"|"m7a.8xlarge"|"m7a.12xlarge"|"m7a.16xlarge"|"m7a.24xlarge"|"m7a.32xlarge"|"m7a.48xlarge"|"m7a.metal-48xl"|"hpc7a.12xlarge"|"hpc7a.24xlarge"|"hpc7a.48xlarge"|"hpc7a.96xlarge"|"c7gd.medium"|"c7gd.large"|"c7gd.xlarge"|"c7gd.2xlarge"|"c7gd.4xlarge"|"c7gd.8xlarge"|"c7gd.12xlarge"|"c7gd.16xlarge"|"m7gd.medium"|"m7gd.large"|"m7gd.xlarge"|"m7gd.2xlarge"|"m7gd.4xlarge"|"m7gd.8xlarge"|"m7gd.12xlarge"|"m7gd.16xlarge"|"r7gd.medium"|"r7gd.large"|"r7gd.xlarge"|"r7gd.2xlarge"|"r7gd.4xlarge"|"r7gd.8xlarge"|"r7gd.12xlarge"|"r7gd.16xlarge"|"r7a.medium"|"r7a.large"|"r7a.xlarge"|"r7a.2xlarge"|"r7a.4xlarge"|"r7a.8xlarge"|"r7a.12xlarge"|"r7a.16xlarge"|"r7a.24xlarge"|"r7a.32xlarge"|"r7a.48xlarge"|"c7i.large"|"c7i.xlarge"|"c7i.2xlarge"|"c7i.4xlarge"|"c7i.8xlarge"|"c7i.12xlarge"|"c7i.16xlarge"|"c7i.24xlarge"|"c7i.48xlarge"|"mac2-m2pro.metal"|"r7iz.large"|"r7iz.xlarge"|"r7iz.2xlarge"|"r7iz.4xlarge"|"r7iz.8xlarge"|"r7iz.12xlarge"|"r7iz.16xlarge"|"r7iz.32xlarge"|"c7a.medium"|"c7a.large"|"c7a.xlarge"|"c7a.2xlarge"|"c7a.4xlarge"|"c7a.8xlarge"|"c7a.12xlarge"|"c7a.16xlarge"|"c7a.24xlarge"|"c7a.32xlarge"|"c7a.48xlarge"|"c7a.metal-48xl"|"r7a.metal-48xl"|"r7i.large"|"r7i.xlarge"|"r7i.2xlarge"|"r7i.4xlarge"|"r7i.8xlarge"|"r7i.12xlarge"|"r7i.16xlarge"|"r7i.24xlarge"|"r7i.48xlarge"|"dl2q.24xlarge"|"mac2-m2.metal"|"i4i.12xlarge"|"i4i.24xlarge"|"c7i.metal-24xl"|"c7i.metal-48xl"|"m7i.metal-24xl"|"m7i.metal-48xl"|"r7i.metal-24xl"|"r7i.metal-48xl"|"r7iz.metal-16xl"|"r7iz.metal-32xl"|"c7gd.metal"|"m7gd.metal"|"r7gd.metal"|"g6.xlarge"|"g6.2xlarge"|"g6.4xlarge"|"g6.8xlarge"|"g6.12xlarge"|"g6.16xlarge"|"g6.24xlarge"|"g6.48xlarge"|"gr6.4xlarge"|"gr6.8xlarge"|"c7i-flex.large"|"c7i-flex.xlarge"|"c7i-flex.2xlarge"|"c7i-flex.4xlarge"|"c7i-flex.8xlarge"|"u7i-12tb.224xlarge"|"u7in-16tb.224xlarge"|"u7in-24tb.224xlarge"|"u7in-32tb.224xlarge"|"u7ib-12tb.224xlarge"|"c7gn.metal"|"r8g.medium"|"r8g.large"|"r8g.xlarge"|"r8g.2xlarge"|"r8g.4xlarge"|"r8g.8xlarge"|"r8g.12xlarge"|"r8g.16xlarge"|"r8g.24xlarge"|"r8g.48xlarge"|"r8g.metal-24xl"|"r8g.metal-48xl"|"mac2-m1ultra.metal"|"g6e.xlarge"|"g6e.2xlarge"|"g6e.4xlarge"|"g6e.8xlarge"|"g6e.12xlarge"|"g6e.16xlarge"|"g6e.24xlarge"|"g6e.48xlarge"|"c8g.medium"|"c8g.large"|"c8g.xlarge"|"c8g.2xlarge"|"c8g.4xlarge"|"c8g.8xlarge"|"c8g.12xlarge"|"c8g.16xlarge"|"c8g.24xlarge"|"c8g.48xlarge"|"c8g.metal-24xl"|"c8g.metal-48xl"|"m8g.medium"|"m8g.large"|"m8g.xlarge"|"m8g.2xlarge"|"m8g.4xlarge"|"m8g.8xlarge"|"m8g.12xlarge"|"m8g.16xlarge"|"m8g.24xlarge"|"m8g.48xlarge"|"m8g.metal-24xl"|"m8g.metal-48xl"|"x8g.medium"|"x8g.large"|"x8g.xlarge"|"x8g.2xlarge"|"x8g.4xlarge"|"x8g.8xlarge"|"x8g.12xlarge"|"x8g.16xlarge"|"x8g.24xlarge"|"x8g.48xlarge"|"x8g.metal-24xl"|"x8g.metal-48xl"|"i7ie.large"|"i7ie.xlarge"|"i7ie.2xlarge"|"i7ie.3xlarge"|"i7ie.6xlarge"|"i7ie.12xlarge"|"i7ie.18xlarge"|"i7ie.24xlarge"|"i7ie.48xlarge"|"i8g.large"|"i8g.xlarge"|"i8g.2xlarge"|"i8g.4xlarge"|"i8g.8xlarge"|"i8g.12xlarge"|"i8g.16xlarge"|"i8g.24xlarge"|"i8g.metal-24xl"|"u7i-6tb.112xlarge"|"u7i-8tb.112xlarge"|"u7inh-32tb.480xlarge"|"p5e.48xlarge"|"p5en.48xlarge"|"f2.12xlarge"|"f2.48xlarge"|"trn2.48xlarge",
  "KernelId": "string",
  "KeyName": "string",
  "Monitoring": {
    "Enabled": true|false
  },
  "NetworkInterfaces": [
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
  ],
  "Placement": {
    "AvailabilityZone": "string",
    "GroupName": "string",
    "Tenancy": "default"|"dedicated"|"host"
  },
  "RamdiskId": "string",
  "SubnetId": "string",
  "UserData": "string"
}
```

`--tag-specifications` (list)

The key-value pair for tagging the Spot Instance request on creation. The value for `ResourceType` must be `spot-instances-request` , otherwise the Spot Instance request fails. To tag the Spot Instance request after it has been created, see [CreateTags](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html) .

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

`--instance-interruption-behavior` (string)

The behavior when a Spot Instance is interrupted. The default is `terminate` .

Possible values:

- `hibernate`
- `stop`
- `terminate`

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--spot-price` (string)

The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.

### Warning

If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.

`--client-token` (string)

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency in Amazon EC2 API requests](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Run_Instance_Idempotency.html) in the *Amazon EC2 User Guide* .

`--instance-count` (integer)

The maximum number of Spot Instances to launch.

Default: 1

`--type` (string)

The Spot Instance request type.

Default: `one-time`

Possible values:

- `one-time`
- `persistent`

`--valid-from` (timestamp)

The start date of the request. If this is a one-time request, the request becomes active at this date and time and remains active until all instances launch, the request expires, or the request is canceled. If the request is persistent, the request becomes active at this date and time and remains active until it expires or is canceled.

The specified start date and time cannot be equal to the current date and time. You must specify a start date and time that occurs after the current date and time.

`--valid-until` (timestamp)

The end date of the request, in UTC format (*YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z).

- For a persistent request, the request remains active until the `ValidUntil` date and time is reached. Otherwise, the request remains active until you cancel it.
- For a one-time request, the request remains active until all instances launch, the request is canceled, or the `ValidUntil` date and time is reached. By default, the request is valid for 7 days from the date the request was created.

`--launch-group` (string)

The instance launch group. Launch groups are Spot Instances that launch together and terminate together.

Default: Instances are launched and terminated individually

`--availability-zone-group` (string)

The user-specified name for a logical grouping of requests.

When you specify an Availability Zone group in a Spot Instance request, all Spot Instances in the request are launched in the same Availability Zone. Instance proximity is maintained with this parameter, but the choice of Availability Zone is not. The group applies only to requests for Spot Instances of the same instance type. Any additional Spot Instance requests that are specified with the same Availability Zone group name are launched in that same Availability Zone, as long as at least one instance from the group is still active.

If there is no active instance running in the Availability Zone group that you specify for a new Spot Instance request (all instances are terminated, the request is expired, or the maximum price you specified falls below current Spot price), then Amazon EC2 launches the instance in any Availability Zone where the constraint can be met. Consequently, the subsequent set of Spot Instances could be placed in a different zone from the original request, even if you specified the same Availability Zone group.

Default: Instances are launched in any available Availability Zone.

`--block-duration-minutes` (integer)

Deprecated.

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

**To request Spot Instances**

This example command creates a one-time Spot Instance request for five instances in the specified Availability Zone.
If your account supports EC2-VPC only, Amazon EC2 launches the instances in the default subnet of the specified Availability Zone.
If your account supports EC2-Classic, Amazon EC2 launches the instances in EC2-Classic in the specified Availability Zone.

Command:

```
aws ec2 request-spot-instances --spot-price "0.03" --instance-count 5 --type "one-time" --launch-specification file://specification.json
```

Specification.json:

```
{
  "ImageId": "ami-1a2b3c4d",
  "KeyName": "my-key-pair",
  "SecurityGroupIds": [ "sg-1a2b3c4d" ],
  "InstanceType": "m3.medium",
  "Placement": {
    "AvailabilityZone": "us-west-2a"
  },
  "IamInstanceProfile": {
      "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role"
  }
}
```

Output:

```
{
  "SpotInstanceRequests": [
      {
          "Status": {
              "UpdateTime": "2014-03-25T20:54:21.000Z",
              "Code": "pending-evaluation",
              "Message": "Your Spot request has been submitted for review, and is pending evaluation."
          },
          "ProductDescription": "Linux/UNIX",
          "SpotInstanceRequestId": "sir-df6f405d",
          "State": "open",
          "LaunchSpecification": {
              "Placement": {
                  "AvailabilityZone": "us-west-2a"
              },
              "ImageId": "ami-1a2b3c4d",
              "KeyName": "my-key-pair",
              "SecurityGroups": [
                  {
                      "GroupName": "my-security-group",
                      "GroupId": "sg-1a2b3c4d"
                  }
              ],
              "Monitoring": {
                  "Enabled": false
              },
              "IamInstanceProfile": {
                  "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role"
              },
              "InstanceType": "m3.medium"
          },
          "Type": "one-time",
          "CreateTime": "2014-03-25T20:54:20.000Z",
          "SpotPrice": "0.050000"
      },
      ...
  ]
}
```

This example command creates a one-time Spot Instance request for five instances in the specified subnet.
Amazon EC2 launches the instances in the specified subnet. If the VPC is a nondefault VPC, the instances
do not receive a public IP address by default.

Command:

```
aws ec2 request-spot-instances --spot-price "0.050" --instance-count 5 --type "one-time" --launch-specification file://specification.json
```

Specification.json:

```
{
  "ImageId": "ami-1a2b3c4d",
  "SecurityGroupIds": [ "sg-1a2b3c4d" ],
  "InstanceType": "m3.medium",
  "SubnetId": "subnet-1a2b3c4d",
  "IamInstanceProfile": {
      "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role"
  }
}
```

Output:

```
{
  "SpotInstanceRequests": [
      {
          "Status": {
             "UpdateTime": "2014-03-25T22:21:58.000Z",
             "Code": "pending-evaluation",
             "Message": "Your Spot request has been submitted for review, and is pending evaluation."
          },
          "ProductDescription": "Linux/UNIX",
          "SpotInstanceRequestId": "sir-df6f405d",
          "State": "open",
          "LaunchSpecification": {
             "Placement": {
                 "AvailabilityZone": "us-west-2a"
             }
             "ImageId": "ami-1a2b3c4d"
             "SecurityGroups": [
                 {
                     "GroupName": "my-security-group",
                     "GroupID": "sg-1a2b3c4d"
                 }
             ]
             "SubnetId": "subnet-1a2b3c4d",
             "Monitoring": {
                 "Enabled": false
             },
             "IamInstanceProfile": {
                 "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role"
             },
             "InstanceType": "m3.medium",
         },
         "Type": "one-time",
         "CreateTime": "2014-03-25T22:21:58.000Z",
         "SpotPrice": "0.050000"
      },
      ...
  ]
}
```

This example assigns a public IP address to the Spot Instances that you launch in a nondefault VPC.
Note that when you specify a network interface, you must include the subnet ID and security group ID
using the network interface.

Command:

```
aws ec2 request-spot-instances --spot-price "0.050" --instance-count 1 --type "one-time" --launch-specification file://specification.json
```

Specification.json:

```
{
  "ImageId": "ami-1a2b3c4d",
  "KeyName": "my-key-pair",
  "InstanceType": "m3.medium",
  "NetworkInterfaces": [
    {
      "DeviceIndex": 0,
      "SubnetId": "subnet-1a2b3c4d",
      "Groups": [ "sg-1a2b3c4d" ],
      "AssociatePublicIpAddress": true
    }
  ],
  "IamInstanceProfile": {
      "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role"
  }
}
```

## Output

SpotInstanceRequests -> (list)

The Spot Instance requests.

(structure)

Describes a Spot Instance request.

ActualBlockHourlyPrice -> (string)

Deprecated.

AvailabilityZoneGroup -> (string)

The Availability Zone group. If you specify the same Availability Zone group for all Spot Instance requests, all Spot Instances are launched in the same Availability Zone.

BlockDurationMinutes -> (integer)

Deprecated.

CreateTime -> (timestamp)

The date and time when the Spot Instance request was created, in UTC format (for example, *YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z).

Fault -> (structure)

The fault codes for the Spot Instance request, if any.

Code -> (string)

The reason code for the Spot Instance state change.

Message -> (string)

The message for the Spot Instance state change.

InstanceId -> (string)

The instance ID, if an instance has been launched to fulfill the Spot Instance request.

LaunchGroup -> (string)

The instance launch group. Launch groups are Spot Instances that launch together and terminate together.

LaunchSpecification -> (structure)

Additional information for launching instances.

UserData -> (string)

The base64-encoded user data that instances use when starting up. User data is limited to 16 KB.

AddressingType -> (string)

Deprecated.

BlockDeviceMappings -> (list)

The block device mapping entries.

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

EbsOptimized -> (boolean)

Indicates whether the instance is optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isnât available with all instance types. Additional usage charges apply when using an EBS Optimized instance.

Default: `false`

IamInstanceProfile -> (structure)

The IAM instance profile.

Arn -> (string)

The Amazon Resource Name (ARN) of the instance profile.

Name -> (string)

The name of the instance profile.

ImageId -> (string)

The ID of the AMI.

InstanceType -> (string)

The instance type. Only one instance type can be specified.

KernelId -> (string)

The ID of the kernel.

KeyName -> (string)

The name of the key pair.

NetworkInterfaces -> (list)

The network interfaces. If you specify a network interface, you must specify subnet IDs and security group IDs using the network interface.

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

Placement -> (structure)

The placement information for the instance.

AvailabilityZone -> (string)

The Availability Zone.

[Spot Fleet only] To specify multiple Availability Zones, separate them using commas; for example, âus-west-2a, us-west-2bâ.

GroupName -> (string)

The name of the placement group.

Tenancy -> (string)

The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of `dedicated` runs on single-tenant hardware. The `host` tenancy is not supported for Spot Instances.

RamdiskId -> (string)

The ID of the RAM disk.

SubnetId -> (string)

The ID of the subnet in which to launch the instance.

SecurityGroups -> (list)

The IDs of the security groups.

(structure)

Describes a security group.

GroupId -> (string)

The ID of the security group.

GroupName -> (string)

The name of the security group.

Monitoring -> (structure)

Describes the monitoring of an instance.

Enabled -> (boolean)

Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.

LaunchedAvailabilityZone -> (string)

The Availability Zone in which the request is launched.

ProductDescription -> (string)

The product description associated with the Spot Instance.

SpotInstanceRequestId -> (string)

The ID of the Spot Instance request.

SpotPrice -> (string)

The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.

### Warning

If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.

State -> (string)

The state of the Spot Instance request. Spot request status information helps track your Spot Instance requests. For more information, see [Spot request status](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-request-status.html) in the *Amazon EC2 User Guide* .

Status -> (structure)

The status code and status message describing the Spot Instance request.

Code -> (string)

The status code. For a list of status codes, see [Spot request status codes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-request-status.html#spot-instance-request-status-understand) in the *Amazon EC2 User Guide* .

Message -> (string)

The description for the status code.

UpdateTime -> (timestamp)

The date and time of the most recent status update, in UTC format (for example, *YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z).

Tags -> (list)

Any tags assigned to the resource.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

Type -> (string)

The Spot Instance request type.

ValidFrom -> (timestamp)

The start date of the request, in UTC format (for example, *YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z). The request becomes active at this date and time.

ValidUntil -> (timestamp)

The end date of the request, in UTC format (*YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z).

- For a persistent request, the request remains active until the `validUntil` date and time is reached. Otherwise, the request remains active until you cancel it.
- For a one-time request, the request remains active until all instances launch, the request is canceled, or the `validUntil` date and time is reached. By default, the request is valid for 7 days from the date the request was created.

InstanceInterruptionBehavior -> (string)

The behavior when a Spot Instance is interrupted.