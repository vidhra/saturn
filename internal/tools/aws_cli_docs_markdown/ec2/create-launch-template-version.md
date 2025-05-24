# create-launch-template-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-launch-template-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-launch-template-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# create-launch-template-version

## Description

Creates a new version of a launch template. You must specify an existing launch template, either by name or ID. You can determine whether the new version inherits parameters from a source version, and add or overwrite parameters as needed.

Launch template versions are numbered in the order in which they are created. You canât specify, change, or replace the numbering of launch template versions.

Launch templates are immutable; after you create a launch template, you canât modify it. Instead, you can create a new version of the launch template that includes the changes that you require.

For more information, see [Modify a launch template (manage launch template versions)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-launch-template-versions.html) in the *Amazon EC2 User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateLaunchTemplateVersion)

## Synopsis

```
create-launch-template-version
[--dry-run | --no-dry-run]
[--client-token <value>]
[--launch-template-id <value>]
[--launch-template-name <value>]
[--source-version <value>]
[--version-description <value>]
--launch-template-data <value>
[--resolve-alias | --no-resolve-alias]
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

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--client-token` (string)

Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If a client token isnât specified, a randomly generated token is used in the request to ensure idempotency.

For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .

Constraint: Maximum 128 ASCII characters.

`--launch-template-id` (string)

The ID of the launch template.

You must specify either the launch template ID or the launch template name, but not both.

`--launch-template-name` (string)

The name of the launch template.

You must specify either the launch template ID or the launch template name, but not both.

`--source-version` (string)

The version of the launch template on which to base the new version. Snapshots applied to the block device mapping are ignored when creating a new version unless they are explicitly included.

If you specify this parameter, the new version inherits the launch parameters from the source version. If you specify additional launch parameters for the new version, they overwrite any corresponding launch parameters inherited from the source version.

If you omit this parameter, the new version contains only the launch parameters that you specify for the new version.

`--version-description` (string)

A description for the version of the launch template.

`--launch-template-data` (structure)

The information for the launch template.

KernelId -> (string)

The ID of the kernel.

### Warning

We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see [User provided kernels](https://docs.aws.amazon.com/linux/al2/ug/UserProvidedKernels.html) in the *Amazon Linux 2 User Guide* .

EbsOptimized -> (boolean)

Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal Amazon EBS I/O performance. This optimization isnât available with all instance types. Additional usage charges apply when using an EBS-optimized instance.

IamInstanceProfile -> (structure)

The name or Amazon Resource Name (ARN) of an IAM instance profile.

Arn -> (string)

The Amazon Resource Name (ARN) of the instance profile.

Name -> (string)

The name of the instance profile.

BlockDeviceMappings -> (list)

The block device mapping.

(structure)

Describes a block device mapping.

DeviceName -> (string)

The device name (for example, /dev/sdh or xvdh).

VirtualName -> (string)

The virtual device name (ephemeralN). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ephemeral0 and ephemeral1. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.

Ebs -> (structure)

Parameters used to automatically set up EBS volumes when the instance is launched.

Encrypted -> (boolean)

Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption. If you are creating a volume from a snapshot, you canât specify an encryption value.

DeleteOnTermination -> (boolean)

Indicates whether the EBS volume is deleted on instance termination.

Iops -> (integer)

The number of I/O operations per second (IOPS). For `gp3` , `io1` , and `io2` volumes, this represents the number of IOPS that are provisioned for the volume. For `gp2` volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.

The following are the supported values for each volume type:

- `gp3` : 3,000 - 16,000 IOPS
- `io1` : 100 - 64,000 IOPS
- `io2` : 100 - 256,000 IOPS

For `io2` volumes, you can achieve up to 256,000 IOPS on [instances built on the Nitro System](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) . On other instances, you can achieve performance up to 32,000 IOPS.

This parameter is supported for `io1` , `io2` , and `gp3` volumes only.

KmsKeyId -> (string)

Identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed KMS key to use for EBS encryption.

SnapshotId -> (string)

The ID of the snapshot.

VolumeSize -> (integer)

The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size. The following are the supported volumes sizes for each volume type:

- `gp2` and `gp3` : 1 - 16,384 GiB
- `io1` : 4 - 16,384 GiB
- `io2` : 4 - 65,536 GiB
- `st1` and `sc1` : 125 - 16,384 GiB
- `standard` : 1 - 1024 GiB

VolumeType -> (string)

The volume type. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) in the *Amazon EBS User Guide* .

Throughput -> (integer)

The throughput to provision for a `gp3` volume, with a maximum of 1,000 MiB/s.

Valid Range: Minimum value of 125. Maximum value of 1000.

VolumeInitializationRate -> (integer)

Specifies the Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate), in MiB/s, at which to download the snapshot blocks from Amazon S3 to the volume. This is also known as *volume initialization* . Specifying a volume initialization rate ensures that the volume is initialized at a predictable and consistent rate after creation.

This parameter is supported only for volumes created from snapshots. Omit this parameter if:

- You want to create the volume using fast snapshot restore. You must specify a snapshot that is enabled for fast snapshot restore. In this case, the volume is fully initialized at creation.

### Note

If you specify a snapshot that is enabled for fast snapshot restore and a volume initialization rate, the volume will be initialized at the specified rate instead of fast snapshot restore.

- You want to create a volume that is initialized at the default rate.

For more information, see [Initialize Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html) in the *Amazon EC2 User Guide* .

Valid range: 100 - 300 MiB/s

NoDevice -> (string)

To omit the device from the block device mapping, specify an empty string.

NetworkInterfaces -> (list)

The network interfaces for the instance.

(structure)

The parameters for a network interface.

AssociateCarrierIpAddress -> (boolean)

Associates a Carrier IP address with eth0 for a new network interface.

Use this option when you launch an instance in a Wavelength Zone and want to associate a Carrier IP address with the network interface. For more information about Carrier IP addresses, see [Carrier IP addresses](https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html#provider-owned-ip) in the *Wavelength Developer Guide* .

AssociatePublicIpAddress -> (boolean)

Associates a public IPv4 address with eth0 for a new network interface.

Amazon Web Services charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the *Public IPv4 Address* tab on the [Amazon VPC pricing page](http://aws.amazon.com/vpc/pricing/) .

DeleteOnTermination -> (boolean)

Indicates whether the network interface is deleted when the instance is terminated.

Description -> (string)

A description for the network interface.

DeviceIndex -> (integer)

The device index for the network interface attachment. The primary network interface has a device index of 0. Each network interface is of type `interface` , you must specify a device index. If you create a launch template that includes secondary network interfaces but not a primary network interface, then you must add a primary network interface as a launch parameter when you launch an instance from the template.

Groups -> (list)

The IDs of one or more security groups.

(string)

InterfaceType -> (string)

The type of network interface. To create an Elastic Fabric Adapter (EFA), specify `efa` or `efa` . For more information, see [Elastic Fabric Adapter for AI/ML and HPC workloads on Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html) in the *Amazon EC2 User Guide* .

If you are not creating an EFA, specify `interface` or omit this parameter.

If you specify `efa-only` , do not assign any IP addresses to the network interface. EFA-only network interfaces do not support IP addresses.

Valid values: `interface` | `efa` | `efa-only`

Ipv6AddressCount -> (integer)

The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You canât use this option if specifying specific IPv6 addresses.

Ipv6Addresses -> (list)

One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet. You canât use this option if youâre specifying a number of IPv6 addresses.

(structure)

Describes an IPv6 address.

Ipv6Address -> (string)

The IPv6 address.

NetworkInterfaceId -> (string)

The ID of the network interface.

PrivateIpAddress -> (string)

The primary private IPv4 address of the network interface.

PrivateIpAddresses -> (list)

One or more private IPv4 addresses.

(structure)

Describes a secondary private IPv4 address for a network interface.

Primary -> (boolean)

Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.

PrivateIpAddress -> (string)

The private IPv4 address.

SecondaryPrivateIpAddressCount -> (integer)

The number of secondary private IPv4 addresses to assign to a network interface.

SubnetId -> (string)

The ID of the subnet for the network interface.

NetworkCardIndex -> (integer)

The index of the network card. Some instance types support multiple network cards. The primary network interface must be assigned to network card index 0. The default is network card index 0.

Ipv4Prefixes -> (list)

One or more IPv4 prefixes to be assigned to the network interface. You cannot use this option if you use the `Ipv4PrefixCount` option.

(structure)

Describes the IPv4 prefix option for a network interface.

Ipv4Prefix -> (string)

The IPv4 prefix. For information, see [Assigning prefixes to network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-prefix-eni.html) in the *Amazon EC2 User Guide* .

Ipv4PrefixCount -> (integer)

The number of IPv4 prefixes to be automatically assigned to the network interface. You cannot use this option if you use the `Ipv4Prefix` option.

Ipv6Prefixes -> (list)

One or more IPv6 prefixes to be assigned to the network interface. You cannot use this option if you use the `Ipv6PrefixCount` option.

(structure)

Describes the IPv6 prefix option for a network interface.

Ipv6Prefix -> (string)

The IPv6 prefix.

Ipv6PrefixCount -> (integer)

The number of IPv6 prefixes to be automatically assigned to the network interface. You cannot use this option if you use the `Ipv6Prefix` option.

PrimaryIpv6 -> (boolean)

The primary IPv6 address of the network interface. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information about primary IPv6 addresses, see [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) .

EnaSrdSpecification -> (structure)

Configure ENA Express settings for your launch template.

EnaSrdEnabled -> (boolean)

Specifies whether ENA Express is enabled for the network interface when you launch an instance.

EnaSrdUdpSpecification -> (structure)

Contains ENA Express settings for UDP network traffic for the network interface attached to the instance.

EnaSrdUdpEnabled -> (boolean)

Indicates whether UDP traffic uses ENA Express for your instance. To ensure that UDP traffic can use ENA Express when you launch an instance, you must also set **EnaSrdEnabled** in the **EnaSrdSpecificationRequest** to `true` .

ConnectionTrackingSpecification -> (structure)

A security group connection tracking specification that enables you to set the timeout for connection tracking on an Elastic network interface. For more information, see [Idle connection tracking timeout](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts) in the *Amazon EC2 User Guide* .

TcpEstablishedTimeout -> (integer)

Timeout (in seconds) for idle TCP connections in an established state. Min: 60 seconds. Max: 432000 seconds (5 days). Default: 432000 seconds. Recommended: Less than 432000 seconds.

UdpStreamTimeout -> (integer)

Timeout (in seconds) for idle UDP flows classified as streams which have seen more than one request-response transaction. Min: 60 seconds. Max: 180 seconds (3 minutes). Default: 180 seconds.

UdpTimeout -> (integer)

Timeout (in seconds) for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction. Min: 30 seconds. Max: 60 seconds. Default: 30 seconds.

EnaQueueCount -> (integer)

The number of ENA queues to be created with the instance.

ImageId -> (string)

The ID of the AMI in the format `ami-0ac394d6a3example` .

Alternatively, you can specify a Systems Manager parameter, using one of the following formats. The Systems Manager parameter will resolve to an AMI ID on launch.

To reference a public parameter:

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-launch-template-version.html#id1)resolve:ssm:*public-parameter* ``

To reference a parameter stored in the same account:

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-launch-template-version.html#id3)resolve:ssm:*parameter-name* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-launch-template-version.html#id5)resolve:ssm:*parameter-name:version-number* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-launch-template-version.html#id7)resolve:ssm:*parameter-name:label* ``

To reference a parameter shared from another Amazon Web Services account:

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-launch-template-version.html#id9)resolve:ssm:*parameter-ARN* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-launch-template-version.html#id11)resolve:ssm:*parameter-ARN:version-number* ``
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-launch-template-version.html#id13)resolve:ssm:*parameter-ARN:label* ``

For more information, see [Use a Systems Manager parameter instead of an AMI ID](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#use-an-ssm-parameter-instead-of-an-ami-id) in the *Amazon EC2 User Guide* .

### Note

If the launch template will be used for an EC2 Fleet or Spot Fleet, note the following:

- Only EC2 Fleets of type `instant` support specifying a Systems Manager parameter.
- For EC2 Fleets of type `maintain` or `request` , or for Spot Fleets, you must specify the AMI ID.

InstanceType -> (string)

The instance type. For more information, see [Amazon EC2 instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide* .

If you specify `InstanceType` , you canât specify `InstanceRequirements` .

KeyName -> (string)

The name of the key pair. You can create a key pair using [CreateKeyPair](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateKeyPair.html) or [ImportKeyPair](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportKeyPair.html) .

### Warning

If you do not specify a key pair, you canât connect to the instance unless you choose an AMI that is configured to allow users another way to log in.

Monitoring -> (structure)

The monitoring for the instance.

Enabled -> (boolean)

Specify `true` to enable detailed monitoring. Otherwise, basic monitoring is enabled.

Placement -> (structure)

The placement for the instance.

AvailabilityZone -> (string)

The Availability Zone for the instance.

Affinity -> (string)

The affinity setting for an instance on a Dedicated Host.

GroupName -> (string)

The name of the placement group for the instance.

HostId -> (string)

The ID of the Dedicated Host for the instance.

Tenancy -> (string)

The tenancy of the instance. An instance with a tenancy of dedicated runs on single-tenant hardware.

SpreadDomain -> (string)

Reserved for future use.

HostResourceGroupArn -> (string)

The ARN of the host resource group in which to launch the instances. If you specify a host resource group ARN, omit the **Tenancy** parameter or set it to `host` .

PartitionNumber -> (integer)

The number of the partition the instance should launch in. Valid only if the placement group strategy is set to `partition` .

GroupId -> (string)

The Group Id of a placement group. You must specify the Placement Group **Group Id** to launch an instance in a shared placement group.

RamDiskId -> (string)

The ID of the RAM disk.

### Warning

We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see [User provided kernels](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedkernels.html) in the *Amazon EC2 User Guide* .

DisableApiTermination -> (boolean)

Indicates whether termination protection is enabled for the instance. The default is `false` , which means that you can terminate the instance using the Amazon EC2 console, command line tools, or API. You can enable termination protection when you launch an instance, while the instance is running, or while the instance is stopped.

InstanceInitiatedShutdownBehavior -> (string)

Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).

Default: `stop`

UserData -> (string)

The user data to make available to the instance. You must provide base64-encoded text. User data is limited to 16 KB. For more information, see [Run commands when you launch an EC2 instance with user data input](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html) in the *Amazon EC2 User Guide* .

If you are creating the launch template for use with Batch, the user data must be provided in the [MIME multi-part archive format](https://cloudinit.readthedocs.io/en/latest/topics/format.html#mime-multi-part-archive) . For more information, see [Amazon EC2 user data in launch templates](https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html#lt-user-data) in the *Batch User Guide* .

TagSpecifications -> (list)

The tags to apply to the resources that are created during instance launch. These tags are not applied to the launch template.

(structure)

The tags specification for the resources that are created during instance launch.

ResourceType -> (string)

The type of resource to tag.

Valid Values lists all resource types for Amazon EC2 that can be tagged. When you create a launch template, you can specify tags for the following resource types only: `instance` | `volume` | `network-interface` | `spot-instances-request` . If the instance does not include the resource type that you specify, the instance launch fails. For example, not all instance types include a volume.

To tag a resource after it has been created, see [CreateTags](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html) .

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

ElasticGpuSpecifications -> (list)

Deprecated.

### Note

Amazon Elastic Graphics reached end of life on January 8, 2024.

(structure)

### Note

Amazon Elastic Graphics reached end of life on January 8, 2024.

A specification for an Elastic Graphics accelerator.

Type -> (string)

The type of Elastic Graphics accelerator.

ElasticInferenceAccelerators -> (list)

### Note

Amazon Elastic Inference is no longer available.

An elastic inference accelerator to associate with the instance. Elastic inference accelerators are a resource you can attach to your Amazon EC2 instances to accelerate your Deep Learning (DL) inference workloads.

You cannot specify accelerators from different generations in the same request.

(structure)

### Note

Amazon Elastic Inference is no longer available.

Describes an elastic inference accelerator.

Type -> (string)

The type of elastic inference accelerator. The possible values are eia1.medium, eia1.large, and eia1.xlarge.

Count -> (integer)

The number of elastic inference accelerators to attach to the instance.

Default: 1

SecurityGroupIds -> (list)

The IDs of the security groups.

If you specify a network interface, you must specify any security groups as part of the network interface instead of using this parameter.

(string)

SecurityGroups -> (list)

The names of the security groups. For a nondefault VPC, you must use security group IDs instead.

If you specify a network interface, you must specify any security groups as part of the network interface instead of using this parameter.

(string)

InstanceMarketOptions -> (structure)

The market (purchasing) option for the instances.

MarketType -> (string)

The market type.

SpotOptions -> (structure)

The options for Spot Instances.

MaxPrice -> (string)

The maximum hourly price youâre willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price. If you do specify this parameter, it must be more than USD $0.001. Specifying a value below USD $0.001 will result in an `InvalidParameterValue` error message when the launch template is used to launch an instance.

### Warning

If you specify a maximum price, your Spot Instances will be interrupted more frequently than if you do not specify this parameter.

SpotInstanceType -> (string)

The Spot Instance request type.

BlockDurationMinutes -> (integer)

Deprecated.

ValidUntil -> (timestamp)

The end date of the request, in UTC format (*YYYY-MM-DD* T*HH:MM:SS* Z). Supported only for persistent requests.

- For a persistent request, the request remains active until the `ValidUntil` date and time is reached. Otherwise, the request remains active until you cancel it.
- For a one-time request, `ValidUntil` is not supported. The request remains active until all instances launch or you cancel the request.

Default: 7 days from the current date

InstanceInterruptionBehavior -> (string)

The behavior when a Spot Instance is interrupted. The default is `terminate` .

CreditSpecification -> (structure)

The credit option for CPU usage of the instance. Valid only for T instances.

CpuCredits -> (string)

The credit option for CPU usage of a T instance.

Valid values: `standard` | `unlimited`

CpuOptions -> (structure)

The CPU options for the instance. For more information, see [CPU options for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) in the *Amazon EC2 User Guide* .

CoreCount -> (integer)

The number of CPU cores for the instance.

ThreadsPerCore -> (integer)

The number of threads per CPU core. To disable multithreading for the instance, specify a value of `1` . Otherwise, specify the default value of `2` .

AmdSevSnp -> (string)

Indicates whether to enable the instance for AMD SEV-SNP. AMD SEV-SNP is supported with M6a, R6a, and C6a instance types only. For more information, see [AMD SEV-SNP for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html) .

CapacityReservationSpecification -> (structure)

The Capacity Reservation targeting option. If you do not specify this parameter, the instanceâs Capacity Reservation preference defaults to `open` , which enables it to run in any open Capacity Reservation that has matching attributes (instance type, platform, Availability Zone).

CapacityReservationPreference -> (string)

Indicates the instanceâs Capacity Reservation preferences. Possible preferences include:

- `capacity-reservations-only` - The instance will only run in a Capacity Reservation or Capacity Reservation group. If capacity isnât available, the instance will fail to launch.
- `open` - The instance can run in any `open` Capacity Reservation that has matching attributes (instance type, platform, Availability Zone, tenancy).
- `none` - The instance avoids running in a Capacity Reservation even if one is available. The instance runs in On-Demand capacity.

CapacityReservationTarget -> (structure)

Information about the target Capacity Reservation or Capacity Reservation group.

CapacityReservationId -> (string)

The ID of the Capacity Reservation in which to run the instance.

CapacityReservationResourceGroupArn -> (string)

The ARN of the Capacity Reservation resource group in which to run the instance.

LicenseSpecifications -> (list)

The license configurations.

(structure)

Describes a license configuration.

LicenseConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the license configuration.

HibernationOptions -> (structure)

Indicates whether an instance is enabled for hibernation. This parameter is valid only if the instance meets the [hibernation prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html) . For more information, see [Hibernate your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html) in the *Amazon EC2 User Guide* .

Configured -> (boolean)

If you set this parameter to `true` , the instance is enabled for hibernation.

Default: `false`

MetadataOptions -> (structure)

The metadata options for the instance. For more information, see [Configure the Instance Metadata Service options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html) in the *Amazon EC2 User Guide* .

HttpTokens -> (string)

Indicates whether IMDSv2 is required.

- `optional` - IMDSv2 is optional. You can choose whether to send a session token in your instance metadata retrieval requests. If you retrieve IAM role credentials without a session token, you receive the IMDSv1 role credentials. If you retrieve IAM role credentials using a valid session token, you receive the IMDSv2 role credentials.
- `required` - IMDSv2 is required. You must send a session token in your instance metadata retrieval requests. With this option, retrieving the IAM role credentials always returns IMDSv2 credentials; IMDSv1 credentials are not available.

Default: If the value of `ImdsSupport` for the Amazon Machine Image (AMI) for your instance is `v2.0` , the default is `required` .

HttpPutResponseHopLimit -> (integer)

The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel.

Default: `1`

Possible values: Integers from 1 to 64

HttpEndpoint -> (string)

Enables or disables the HTTP metadata endpoint on your instances. If the parameter is not specified, the default state is `enabled` .

### Note

If you specify a value of `disabled` , you will not be able to access your instance metadata.

HttpProtocolIpv6 -> (string)

Enables or disables the IPv6 endpoint for the instance metadata service.

Default: `disabled`

InstanceMetadataTags -> (string)

Set to `enabled` to allow access to instance tags from the instance metadata. Set to `disabled` to turn off access to instance tags from the instance metadata. For more information, see [View tags for your EC2 instances using instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html) .

Default: `disabled`

EnclaveOptions -> (structure)

Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves. For more information, see [What is Nitro Enclaves?](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html) in the *Amazon Web Services Nitro Enclaves User Guide* .

You canât enable Amazon Web Services Nitro Enclaves and hibernation on the same instance.

Enabled -> (boolean)

To enable the instance for Amazon Web Services Nitro Enclaves, set this parameter to `true` .

InstanceRequirements -> (structure)

The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with these attributes.

You must specify `VCpuCount` and `MemoryMiB` . All other attributes are optional. Any unspecified optional attribute is set to its default.

When you specify multiple attributes, you get instance types that satisfy all of the specified attributes. If you specify multiple values for an attribute, you get instance types that satisfy any of the specified values.

To limit the list of instance types from which Amazon EC2 can identify matching instance types, you can use one of the following parameters, but not both in the same request:

- `AllowedInstanceTypes` - The instance types to include in the list. All other instance types are ignored, even if they match your specified attributes.
- `ExcludedInstanceTypes` - The instance types to exclude from the list, even if they match your specified attributes.

### Note

If you specify `InstanceRequirements` , you canât specify `InstanceType` .

Attribute-based instance type selection is only supported when using Auto Scaling groups, EC2 Fleet, and Spot Fleet to launch instances. If you plan to use the launch template in the [launch instance wizard](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html) , or with the [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) API or [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) Amazon Web Services CloudFormation resource, you canât specify `InstanceRequirements` .

For more information, see [Specify attributes for instance type selection for EC2 Fleet or Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html) and [Spot placement score](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-placement-score.html) in the *Amazon EC2 User Guide* .

VCpuCount -> (structure)

The minimum and maximum number of vCPUs.

Min -> (integer)

The minimum number of vCPUs. To specify no minimum limit, specify `0` .

Max -> (integer)

The maximum number of vCPUs. To specify no maximum limit, omit this parameter.

MemoryMiB -> (structure)

The minimum and maximum amount of memory, in MiB.

Min -> (integer)

The minimum amount of memory, in MiB. To specify no minimum limit, specify `0` .

Max -> (integer)

The maximum amount of memory, in MiB. To specify no maximum limit, omit this parameter.

CpuManufacturers -> (list)

The CPU manufacturers to include.

- For instance types with Intel CPUs, specify `intel` .
- For instance types with AMD CPUs, specify `amd` .
- For instance types with Amazon Web Services CPUs, specify `amazon-web-services` .
- For instance types with Apple CPUs, specify `apple` .

### Note

Donât confuse the CPU manufacturer with the CPU architecture. Instances will be launched with a compatible CPU architecture based on the Amazon Machine Image (AMI) that you specify in your launch template.

Default: Any manufacturer

(string)

MemoryGiBPerVCpu -> (structure)

The minimum and maximum amount of memory per vCPU, in GiB.

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of memory per vCPU, in GiB. To specify no minimum limit, omit this parameter.

Max -> (double)

The maximum amount of memory per vCPU, in GiB. To specify no maximum limit, omit this parameter.

ExcludedInstanceTypes -> (list)

The instance types to exclude.

You can use strings with one or more wild cards, represented by an asterisk (`*` ), to exclude an instance family, type, size, or generation. The following are examples: `m5.8xlarge` , `c5*.*` , `m5a.*` , `r*` , `*3*` .

For example, if you specify `c5*` ,Amazon EC2 will exclude the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*` , Amazon EC2 will exclude all the M5a instance types, but not the M5n instance types.

### Note

If you specify `ExcludedInstanceTypes` , you canât specify `AllowedInstanceTypes` .

Default: No excluded instance types

(string)

InstanceGenerations -> (list)

Indicates whether current or previous generation instance types are included. The current generation instance types are recommended for use. Current generation instance types are typically the latest two to three generations in each instance family. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide* .

For current generation instance types, specify `current` .

For previous generation instance types, specify `previous` .

Default: Current and previous generation instance types

(string)

SpotMaxPricePercentageOverLowestPrice -> (integer)

[Price protection] The price protection threshold for Spot Instances, as a percentage higher than an identified Spot price. The identified Spot price is the Spot price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified Spot price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose Spot price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 interprets as a percentage.

If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib` , the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.

This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) and [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html) .

### Note

Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you donât specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999` .

Default: `100`

OnDemandMaxPricePercentageOverLowestPrice -> (integer)

[Price protection] The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 interprets as a percentage.

To indicate no price protection threshold, specify a high value, such as `999999` .

This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) and [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html) .

### Note

If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib` , the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.

Default: `20`

BareMetal -> (string)

Indicates whether bare metal instance types must be included, excluded, or required.

- To include bare metal instance types, specify `included` .
- To require only bare metal instance types, specify `required` .
- To exclude bare metal instance types, specify `excluded` .

Default: `excluded`

BurstablePerformance -> (string)

Indicates whether burstable performance T instance types are included, excluded, or required. For more information, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) .

- To include burstable performance instance types, specify `included` .
- To require only burstable performance instance types, specify `required` .
- To exclude burstable performance instance types, specify `excluded` .

Default: `excluded`

RequireHibernateSupport -> (boolean)

Indicates whether instance types must support hibernation for On-Demand Instances.

This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) .

Default: `false`

NetworkInterfaceCount -> (structure)

The minimum and maximum number of network interfaces.

Default: No minimum or maximum limits

Min -> (integer)

The minimum number of network interfaces. To specify no minimum limit, omit this parameter.

Max -> (integer)

The maximum number of network interfaces. To specify no maximum limit, omit this parameter.

LocalStorage -> (string)

Indicates whether instance types with instance store volumes are included, excluded, or required. For more information, [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) in the *Amazon EC2 User Guide* .

- To include instance types with instance store volumes, specify `included` .
- To require only instance types with instance store volumes, specify `required` .
- To exclude instance types with instance store volumes, specify `excluded` .

Default: `included`

LocalStorageTypes -> (list)

The type of local storage that is required.

- For instance types with hard disk drive (HDD) storage, specify `hdd` .
- For instance types with solid state drive (SSD) storage, specify `ssd` .

Default: `hdd` and `ssd`

(string)

TotalLocalStorageGB -> (structure)

The minimum and maximum amount of total local storage, in GB.

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of total local storage, in GB. To specify no minimum limit, omit this parameter.

Max -> (double)

The maximum amount of total local storage, in GB. To specify no maximum limit, omit this parameter.

BaselineEbsBandwidthMbps -> (structure)

The minimum and maximum baseline bandwidth to Amazon EBS, in Mbps. For more information, see [Amazon EBSâoptimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) in the *Amazon EC2 User Guide* .

Default: No minimum or maximum limits

Min -> (integer)

The minimum baseline bandwidth, in Mbps. To specify no minimum limit, omit this parameter.

Max -> (integer)

The maximum baseline bandwidth, in Mbps. To specify no maximum limit, omit this parameter.

AcceleratorTypes -> (list)

The accelerator types that must be on the instance type.

- For instance types with FPGA accelerators, specify `fpga` .
- For instance types with GPU accelerators, specify `gpu` .
- For instance types with Inference accelerators, specify `inference` .

Default: Any accelerator type

(string)

AcceleratorCount -> (structure)

The minimum and maximum number of accelerators (GPUs, FPGAs, or Amazon Web Services Inferentia chips) on an instance.

To exclude accelerator-enabled instance types, set `Max` to `0` .

Default: No minimum or maximum limits

Min -> (integer)

The minimum number of accelerators. To specify no minimum limit, omit this parameter.

Max -> (integer)

The maximum number of accelerators. To specify no maximum limit, omit this parameter. To exclude accelerator-enabled instance types, set `Max` to `0` .

AcceleratorManufacturers -> (list)

Indicates whether instance types must have accelerators by specific manufacturers.

- For instance types with Amazon Web Services devices, specify `amazon-web-services` .
- For instance types with AMD devices, specify `amd` .
- For instance types with Habana devices, specify `habana` .
- For instance types with NVIDIA devices, specify `nvidia` .
- For instance types with Xilinx devices, specify `xilinx` .

Default: Any manufacturer

(string)

AcceleratorNames -> (list)

The accelerators that must be on the instance type.

- For instance types with NVIDIA A10G GPUs, specify `a10g` .
- For instance types with NVIDIA A100 GPUs, specify `a100` .
- For instance types with NVIDIA H100 GPUs, specify `h100` .
- For instance types with Amazon Web Services Inferentia chips, specify `inferentia` .
- For instance types with NVIDIA GRID K520 GPUs, specify `k520` .
- For instance types with NVIDIA K80 GPUs, specify `k80` .
- For instance types with NVIDIA M60 GPUs, specify `m60` .
- For instance types with AMD Radeon Pro V520 GPUs, specify `radeon-pro-v520` .
- For instance types with NVIDIA T4 GPUs, specify `t4` .
- For instance types with NVIDIA T4G GPUs, specify `t4g` .
- For instance types with Xilinx VU9P FPGAs, specify `vu9p` .
- For instance types with NVIDIA V100 GPUs, specify `v100` .

Default: Any accelerator

(string)

AcceleratorTotalMemoryMiB -> (structure)

The minimum and maximum amount of total accelerator memory, in MiB.

Default: No minimum or maximum limits

Min -> (integer)

The minimum amount of accelerator memory, in MiB. To specify no minimum limit, omit this parameter.

Max -> (integer)

The maximum amount of accelerator memory, in MiB. To specify no maximum limit, omit this parameter.

NetworkBandwidthGbps -> (structure)

The minimum and maximum amount of baseline network bandwidth, in gigabits per second (Gbps). For more information, see [Amazon EC2 instance network bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html) in the *Amazon EC2 User Guide* .

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of network bandwidth, in Gbps. To specify no minimum limit, omit this parameter.

Max -> (double)

The maximum amount of network bandwidth, in Gbps. To specify no maximum limit, omit this parameter.

AllowedInstanceTypes -> (list)

The instance types to apply your specified attributes against. All other instance types are ignored, even if they match your specified attributes.

You can use strings with one or more wild cards, represented by an asterisk (`*` ), to allow an instance type, size, or generation. The following are examples: `m5.8xlarge` , `c5*.*` , `m5a.*` , `r*` , `*3*` .

For example, if you specify `c5*` ,Amazon EC2 will allow the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*` , Amazon EC2 will allow all the M5a instance types, but not the M5n instance types.

### Note

If you specify `AllowedInstanceTypes` , you canât specify `ExcludedInstanceTypes` .

Default: All instance types

(string)

MaxSpotPriceAsPercentageOfOptimalOnDemandPrice -> (integer)

[Price protection] The price protection threshold for Spot Instances, as a percentage of an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 interprets as a percentage.

If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib` , the price protection threshold is based on the per vCPU or per memory price instead of the per instance price.

### Note

Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you donât specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999` .

BaselinePerformanceFactors -> (structure)

The baseline performance to consider, using an instance family as a baseline reference. The instance family establishes the lowest acceptable level of performance. Amazon EC2 uses this baseline to guide instance type selection, but there is no guarantee that the selected instance types will always exceed the baseline for every application. Currently, this parameter only supports CPU performance as a baseline performance factor. For more information, see [Performance protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html#ec2fleet-abis-performance-protection) in the *Amazon EC2 User Guide* .

Cpu -> (structure)

The CPU performance to consider, using an instance family as the baseline reference.

References -> (list)

Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture differences.

### Note

Currently, only one instance family can be specified in the list.

(structure)

Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture.

### Note

Currently, only one instance family can be specified in the list.

InstanceFamily -> (string)

The instance family to use as a baseline reference.

### Note

Ensure that you specify the correct value for the instance family. The instance family is everything before the period (`.` ) in the instance type name. For example, in the instance type `c6i.large` , the instance family is `c6i` , not `c6` . For more information, see [Amazon EC2 instance type naming conventions](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html) in *Amazon EC2 Instance Types* .

The following instance families are *not supported* for performance protection:

- `c1`
- `g3` | `g3s`
- `hpc7g`
- `m1` | `m2`
- `mac1` | `mac2` | `mac2-m1ultra` | `mac2-m2` | `mac2-m2pro`
- `p3dn` | `p4d` | `p5`
- `t1`
- `u-12tb1` | `u-18tb1` | `u-24tb1` | `u-3tb1` | `u-6tb1` | `u-9tb1` | `u7i-12tb` | `u7in-16tb` | `u7in-24tb` | `u7in-32tb`

If you enable performance protection by specifying a supported instance family, the returned instance types will exclude the above unsupported instance families.

If you specify an unsupported instance family as a value for baseline performance, the API returns an empty response for [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements) and an exception for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) , [RequestSpotFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet) , [ModifyFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyFleet) , and [ModifySpotFleetRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySpotFleetRequest) .

PrivateDnsNameOptions -> (structure)

The options for the instance hostname. The default values are inherited from the subnet.

HostnameType -> (string)

The type of hostname for Amazon EC2 instances. For IPv4 only subnets, an instance DNS name must be based on the instance IPv4 address. For IPv6 native subnets, an instance DNS name must be based on the instance ID. For dual-stack subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID.

EnableResourceNameDnsARecord -> (boolean)

Indicates whether to respond to DNS queries for instance hostnames with DNS A records.

EnableResourceNameDnsAAAARecord -> (boolean)

Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.

MaintenanceOptions -> (structure)

The maintenance options for the instance.

AutoRecovery -> (string)

Disables the automatic recovery behavior of your instance or sets it to default. For more information, see [Simplified automatic recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html#instance-configuration-recovery) .

DisableApiStop -> (boolean)

Indicates whether to enable the instance for stop protection. For more information, see [Enable stop protection for your EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-stop-protection.html) in the *Amazon EC2 User Guide* .

Operator -> (structure)

The entity that manages the launch template.

Principal -> (string)

The service provider that manages the resource.

NetworkPerformanceOptions -> (structure)

Contains launch template settings to boost network performance for the type of workload that runs on your instance.

BandwidthWeighting -> (string)

Specify the bandwidth weighting option to boost the associated type of baseline bandwidth, as follows:

default

This option uses the standard bandwidth configuration for your instance type.

vpc-1

This option boosts your networking baseline bandwidth and reduces your EBS baseline bandwidth.

ebs-1

This option boosts your EBS baseline bandwidth and reduces your networking baseline bandwidth.

JSON Syntax:

```
{
  "KernelId": "string",
  "EbsOptimized": true|false,
  "IamInstanceProfile": {
    "Arn": "string",
    "Name": "string"
  },
  "BlockDeviceMappings": [
    {
      "DeviceName": "string",
      "VirtualName": "string",
      "Ebs": {
        "Encrypted": true|false,
        "DeleteOnTermination": true|false,
        "Iops": integer,
        "KmsKeyId": "string",
        "SnapshotId": "string",
        "VolumeSize": integer,
        "VolumeType": "standard"|"io1"|"io2"|"gp2"|"sc1"|"st1"|"gp3",
        "Throughput": integer,
        "VolumeInitializationRate": integer
      },
      "NoDevice": "string"
    }
    ...
  ],
  "NetworkInterfaces": [
    {
      "AssociateCarrierIpAddress": true|false,
      "AssociatePublicIpAddress": true|false,
      "DeleteOnTermination": true|false,
      "Description": "string",
      "DeviceIndex": integer,
      "Groups": ["string", ...],
      "InterfaceType": "string",
      "Ipv6AddressCount": integer,
      "Ipv6Addresses": [
        {
          "Ipv6Address": "string"
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
  "ImageId": "string",
  "InstanceType": "a1.medium"|"a1.large"|"a1.xlarge"|"a1.2xlarge"|"a1.4xlarge"|"a1.metal"|"c1.medium"|"c1.xlarge"|"c3.large"|"c3.xlarge"|"c3.2xlarge"|"c3.4xlarge"|"c3.8xlarge"|"c4.large"|"c4.xlarge"|"c4.2xlarge"|"c4.4xlarge"|"c4.8xlarge"|"c5.large"|"c5.xlarge"|"c5.2xlarge"|"c5.4xlarge"|"c5.9xlarge"|"c5.12xlarge"|"c5.18xlarge"|"c5.24xlarge"|"c5.metal"|"c5a.large"|"c5a.xlarge"|"c5a.2xlarge"|"c5a.4xlarge"|"c5a.8xlarge"|"c5a.12xlarge"|"c5a.16xlarge"|"c5a.24xlarge"|"c5ad.large"|"c5ad.xlarge"|"c5ad.2xlarge"|"c5ad.4xlarge"|"c5ad.8xlarge"|"c5ad.12xlarge"|"c5ad.16xlarge"|"c5ad.24xlarge"|"c5d.large"|"c5d.xlarge"|"c5d.2xlarge"|"c5d.4xlarge"|"c5d.9xlarge"|"c5d.12xlarge"|"c5d.18xlarge"|"c5d.24xlarge"|"c5d.metal"|"c5n.large"|"c5n.xlarge"|"c5n.2xlarge"|"c5n.4xlarge"|"c5n.9xlarge"|"c5n.18xlarge"|"c5n.metal"|"c6g.medium"|"c6g.large"|"c6g.xlarge"|"c6g.2xlarge"|"c6g.4xlarge"|"c6g.8xlarge"|"c6g.12xlarge"|"c6g.16xlarge"|"c6g.metal"|"c6gd.medium"|"c6gd.large"|"c6gd.xlarge"|"c6gd.2xlarge"|"c6gd.4xlarge"|"c6gd.8xlarge"|"c6gd.12xlarge"|"c6gd.16xlarge"|"c6gd.metal"|"c6gn.medium"|"c6gn.large"|"c6gn.xlarge"|"c6gn.2xlarge"|"c6gn.4xlarge"|"c6gn.8xlarge"|"c6gn.12xlarge"|"c6gn.16xlarge"|"c6i.large"|"c6i.xlarge"|"c6i.2xlarge"|"c6i.4xlarge"|"c6i.8xlarge"|"c6i.12xlarge"|"c6i.16xlarge"|"c6i.24xlarge"|"c6i.32xlarge"|"c6i.metal"|"cc1.4xlarge"|"cc2.8xlarge"|"cg1.4xlarge"|"cr1.8xlarge"|"d2.xlarge"|"d2.2xlarge"|"d2.4xlarge"|"d2.8xlarge"|"d3.xlarge"|"d3.2xlarge"|"d3.4xlarge"|"d3.8xlarge"|"d3en.xlarge"|"d3en.2xlarge"|"d3en.4xlarge"|"d3en.6xlarge"|"d3en.8xlarge"|"d3en.12xlarge"|"dl1.24xlarge"|"f1.2xlarge"|"f1.4xlarge"|"f1.16xlarge"|"g2.2xlarge"|"g2.8xlarge"|"g3.4xlarge"|"g3.8xlarge"|"g3.16xlarge"|"g3s.xlarge"|"g4ad.xlarge"|"g4ad.2xlarge"|"g4ad.4xlarge"|"g4ad.8xlarge"|"g4ad.16xlarge"|"g4dn.xlarge"|"g4dn.2xlarge"|"g4dn.4xlarge"|"g4dn.8xlarge"|"g4dn.12xlarge"|"g4dn.16xlarge"|"g4dn.metal"|"g5.xlarge"|"g5.2xlarge"|"g5.4xlarge"|"g5.8xlarge"|"g5.12xlarge"|"g5.16xlarge"|"g5.24xlarge"|"g5.48xlarge"|"g5g.xlarge"|"g5g.2xlarge"|"g5g.4xlarge"|"g5g.8xlarge"|"g5g.16xlarge"|"g5g.metal"|"hi1.4xlarge"|"hpc6a.48xlarge"|"hs1.8xlarge"|"h1.2xlarge"|"h1.4xlarge"|"h1.8xlarge"|"h1.16xlarge"|"i2.xlarge"|"i2.2xlarge"|"i2.4xlarge"|"i2.8xlarge"|"i3.large"|"i3.xlarge"|"i3.2xlarge"|"i3.4xlarge"|"i3.8xlarge"|"i3.16xlarge"|"i3.metal"|"i3en.large"|"i3en.xlarge"|"i3en.2xlarge"|"i3en.3xlarge"|"i3en.6xlarge"|"i3en.12xlarge"|"i3en.24xlarge"|"i3en.metal"|"im4gn.large"|"im4gn.xlarge"|"im4gn.2xlarge"|"im4gn.4xlarge"|"im4gn.8xlarge"|"im4gn.16xlarge"|"inf1.xlarge"|"inf1.2xlarge"|"inf1.6xlarge"|"inf1.24xlarge"|"is4gen.medium"|"is4gen.large"|"is4gen.xlarge"|"is4gen.2xlarge"|"is4gen.4xlarge"|"is4gen.8xlarge"|"m1.small"|"m1.medium"|"m1.large"|"m1.xlarge"|"m2.xlarge"|"m2.2xlarge"|"m2.4xlarge"|"m3.medium"|"m3.large"|"m3.xlarge"|"m3.2xlarge"|"m4.large"|"m4.xlarge"|"m4.2xlarge"|"m4.4xlarge"|"m4.10xlarge"|"m4.16xlarge"|"m5.large"|"m5.xlarge"|"m5.2xlarge"|"m5.4xlarge"|"m5.8xlarge"|"m5.12xlarge"|"m5.16xlarge"|"m5.24xlarge"|"m5.metal"|"m5a.large"|"m5a.xlarge"|"m5a.2xlarge"|"m5a.4xlarge"|"m5a.8xlarge"|"m5a.12xlarge"|"m5a.16xlarge"|"m5a.24xlarge"|"m5ad.large"|"m5ad.xlarge"|"m5ad.2xlarge"|"m5ad.4xlarge"|"m5ad.8xlarge"|"m5ad.12xlarge"|"m5ad.16xlarge"|"m5ad.24xlarge"|"m5d.large"|"m5d.xlarge"|"m5d.2xlarge"|"m5d.4xlarge"|"m5d.8xlarge"|"m5d.12xlarge"|"m5d.16xlarge"|"m5d.24xlarge"|"m5d.metal"|"m5dn.large"|"m5dn.xlarge"|"m5dn.2xlarge"|"m5dn.4xlarge"|"m5dn.8xlarge"|"m5dn.12xlarge"|"m5dn.16xlarge"|"m5dn.24xlarge"|"m5dn.metal"|"m5n.large"|"m5n.xlarge"|"m5n.2xlarge"|"m5n.4xlarge"|"m5n.8xlarge"|"m5n.12xlarge"|"m5n.16xlarge"|"m5n.24xlarge"|"m5n.metal"|"m5zn.large"|"m5zn.xlarge"|"m5zn.2xlarge"|"m5zn.3xlarge"|"m5zn.6xlarge"|"m5zn.12xlarge"|"m5zn.metal"|"m6a.large"|"m6a.xlarge"|"m6a.2xlarge"|"m6a.4xlarge"|"m6a.8xlarge"|"m6a.12xlarge"|"m6a.16xlarge"|"m6a.24xlarge"|"m6a.32xlarge"|"m6a.48xlarge"|"m6g.metal"|"m6g.medium"|"m6g.large"|"m6g.xlarge"|"m6g.2xlarge"|"m6g.4xlarge"|"m6g.8xlarge"|"m6g.12xlarge"|"m6g.16xlarge"|"m6gd.metal"|"m6gd.medium"|"m6gd.large"|"m6gd.xlarge"|"m6gd.2xlarge"|"m6gd.4xlarge"|"m6gd.8xlarge"|"m6gd.12xlarge"|"m6gd.16xlarge"|"m6i.large"|"m6i.xlarge"|"m6i.2xlarge"|"m6i.4xlarge"|"m6i.8xlarge"|"m6i.12xlarge"|"m6i.16xlarge"|"m6i.24xlarge"|"m6i.32xlarge"|"m6i.metal"|"mac1.metal"|"p2.xlarge"|"p2.8xlarge"|"p2.16xlarge"|"p3.2xlarge"|"p3.8xlarge"|"p3.16xlarge"|"p3dn.24xlarge"|"p4d.24xlarge"|"r3.large"|"r3.xlarge"|"r3.2xlarge"|"r3.4xlarge"|"r3.8xlarge"|"r4.large"|"r4.xlarge"|"r4.2xlarge"|"r4.4xlarge"|"r4.8xlarge"|"r4.16xlarge"|"r5.large"|"r5.xlarge"|"r5.2xlarge"|"r5.4xlarge"|"r5.8xlarge"|"r5.12xlarge"|"r5.16xlarge"|"r5.24xlarge"|"r5.metal"|"r5a.large"|"r5a.xlarge"|"r5a.2xlarge"|"r5a.4xlarge"|"r5a.8xlarge"|"r5a.12xlarge"|"r5a.16xlarge"|"r5a.24xlarge"|"r5ad.large"|"r5ad.xlarge"|"r5ad.2xlarge"|"r5ad.4xlarge"|"r5ad.8xlarge"|"r5ad.12xlarge"|"r5ad.16xlarge"|"r5ad.24xlarge"|"r5b.large"|"r5b.xlarge"|"r5b.2xlarge"|"r5b.4xlarge"|"r5b.8xlarge"|"r5b.12xlarge"|"r5b.16xlarge"|"r5b.24xlarge"|"r5b.metal"|"r5d.large"|"r5d.xlarge"|"r5d.2xlarge"|"r5d.4xlarge"|"r5d.8xlarge"|"r5d.12xlarge"|"r5d.16xlarge"|"r5d.24xlarge"|"r5d.metal"|"r5dn.large"|"r5dn.xlarge"|"r5dn.2xlarge"|"r5dn.4xlarge"|"r5dn.8xlarge"|"r5dn.12xlarge"|"r5dn.16xlarge"|"r5dn.24xlarge"|"r5dn.metal"|"r5n.large"|"r5n.xlarge"|"r5n.2xlarge"|"r5n.4xlarge"|"r5n.8xlarge"|"r5n.12xlarge"|"r5n.16xlarge"|"r5n.24xlarge"|"r5n.metal"|"r6g.medium"|"r6g.large"|"r6g.xlarge"|"r6g.2xlarge"|"r6g.4xlarge"|"r6g.8xlarge"|"r6g.12xlarge"|"r6g.16xlarge"|"r6g.metal"|"r6gd.medium"|"r6gd.large"|"r6gd.xlarge"|"r6gd.2xlarge"|"r6gd.4xlarge"|"r6gd.8xlarge"|"r6gd.12xlarge"|"r6gd.16xlarge"|"r6gd.metal"|"r6i.large"|"r6i.xlarge"|"r6i.2xlarge"|"r6i.4xlarge"|"r6i.8xlarge"|"r6i.12xlarge"|"r6i.16xlarge"|"r6i.24xlarge"|"r6i.32xlarge"|"r6i.metal"|"t1.micro"|"t2.nano"|"t2.micro"|"t2.small"|"t2.medium"|"t2.large"|"t2.xlarge"|"t2.2xlarge"|"t3.nano"|"t3.micro"|"t3.small"|"t3.medium"|"t3.large"|"t3.xlarge"|"t3.2xlarge"|"t3a.nano"|"t3a.micro"|"t3a.small"|"t3a.medium"|"t3a.large"|"t3a.xlarge"|"t3a.2xlarge"|"t4g.nano"|"t4g.micro"|"t4g.small"|"t4g.medium"|"t4g.large"|"t4g.xlarge"|"t4g.2xlarge"|"u-6tb1.56xlarge"|"u-6tb1.112xlarge"|"u-9tb1.112xlarge"|"u-12tb1.112xlarge"|"u-6tb1.metal"|"u-9tb1.metal"|"u-12tb1.metal"|"u-18tb1.metal"|"u-24tb1.metal"|"vt1.3xlarge"|"vt1.6xlarge"|"vt1.24xlarge"|"x1.16xlarge"|"x1.32xlarge"|"x1e.xlarge"|"x1e.2xlarge"|"x1e.4xlarge"|"x1e.8xlarge"|"x1e.16xlarge"|"x1e.32xlarge"|"x2iezn.2xlarge"|"x2iezn.4xlarge"|"x2iezn.6xlarge"|"x2iezn.8xlarge"|"x2iezn.12xlarge"|"x2iezn.metal"|"x2gd.medium"|"x2gd.large"|"x2gd.xlarge"|"x2gd.2xlarge"|"x2gd.4xlarge"|"x2gd.8xlarge"|"x2gd.12xlarge"|"x2gd.16xlarge"|"x2gd.metal"|"z1d.large"|"z1d.xlarge"|"z1d.2xlarge"|"z1d.3xlarge"|"z1d.6xlarge"|"z1d.12xlarge"|"z1d.metal"|"x2idn.16xlarge"|"x2idn.24xlarge"|"x2idn.32xlarge"|"x2iedn.xlarge"|"x2iedn.2xlarge"|"x2iedn.4xlarge"|"x2iedn.8xlarge"|"x2iedn.16xlarge"|"x2iedn.24xlarge"|"x2iedn.32xlarge"|"c6a.large"|"c6a.xlarge"|"c6a.2xlarge"|"c6a.4xlarge"|"c6a.8xlarge"|"c6a.12xlarge"|"c6a.16xlarge"|"c6a.24xlarge"|"c6a.32xlarge"|"c6a.48xlarge"|"c6a.metal"|"m6a.metal"|"i4i.large"|"i4i.xlarge"|"i4i.2xlarge"|"i4i.4xlarge"|"i4i.8xlarge"|"i4i.16xlarge"|"i4i.32xlarge"|"i4i.metal"|"x2idn.metal"|"x2iedn.metal"|"c7g.medium"|"c7g.large"|"c7g.xlarge"|"c7g.2xlarge"|"c7g.4xlarge"|"c7g.8xlarge"|"c7g.12xlarge"|"c7g.16xlarge"|"mac2.metal"|"c6id.large"|"c6id.xlarge"|"c6id.2xlarge"|"c6id.4xlarge"|"c6id.8xlarge"|"c6id.12xlarge"|"c6id.16xlarge"|"c6id.24xlarge"|"c6id.32xlarge"|"c6id.metal"|"m6id.large"|"m6id.xlarge"|"m6id.2xlarge"|"m6id.4xlarge"|"m6id.8xlarge"|"m6id.12xlarge"|"m6id.16xlarge"|"m6id.24xlarge"|"m6id.32xlarge"|"m6id.metal"|"r6id.large"|"r6id.xlarge"|"r6id.2xlarge"|"r6id.4xlarge"|"r6id.8xlarge"|"r6id.12xlarge"|"r6id.16xlarge"|"r6id.24xlarge"|"r6id.32xlarge"|"r6id.metal"|"r6a.large"|"r6a.xlarge"|"r6a.2xlarge"|"r6a.4xlarge"|"r6a.8xlarge"|"r6a.12xlarge"|"r6a.16xlarge"|"r6a.24xlarge"|"r6a.32xlarge"|"r6a.48xlarge"|"r6a.metal"|"p4de.24xlarge"|"u-3tb1.56xlarge"|"u-18tb1.112xlarge"|"u-24tb1.112xlarge"|"trn1.2xlarge"|"trn1.32xlarge"|"hpc6id.32xlarge"|"c6in.large"|"c6in.xlarge"|"c6in.2xlarge"|"c6in.4xlarge"|"c6in.8xlarge"|"c6in.12xlarge"|"c6in.16xlarge"|"c6in.24xlarge"|"c6in.32xlarge"|"m6in.large"|"m6in.xlarge"|"m6in.2xlarge"|"m6in.4xlarge"|"m6in.8xlarge"|"m6in.12xlarge"|"m6in.16xlarge"|"m6in.24xlarge"|"m6in.32xlarge"|"m6idn.large"|"m6idn.xlarge"|"m6idn.2xlarge"|"m6idn.4xlarge"|"m6idn.8xlarge"|"m6idn.12xlarge"|"m6idn.16xlarge"|"m6idn.24xlarge"|"m6idn.32xlarge"|"r6in.large"|"r6in.xlarge"|"r6in.2xlarge"|"r6in.4xlarge"|"r6in.8xlarge"|"r6in.12xlarge"|"r6in.16xlarge"|"r6in.24xlarge"|"r6in.32xlarge"|"r6idn.large"|"r6idn.xlarge"|"r6idn.2xlarge"|"r6idn.4xlarge"|"r6idn.8xlarge"|"r6idn.12xlarge"|"r6idn.16xlarge"|"r6idn.24xlarge"|"r6idn.32xlarge"|"c7g.metal"|"m7g.medium"|"m7g.large"|"m7g.xlarge"|"m7g.2xlarge"|"m7g.4xlarge"|"m7g.8xlarge"|"m7g.12xlarge"|"m7g.16xlarge"|"m7g.metal"|"r7g.medium"|"r7g.large"|"r7g.xlarge"|"r7g.2xlarge"|"r7g.4xlarge"|"r7g.8xlarge"|"r7g.12xlarge"|"r7g.16xlarge"|"r7g.metal"|"c6in.metal"|"m6in.metal"|"m6idn.metal"|"r6in.metal"|"r6idn.metal"|"inf2.xlarge"|"inf2.8xlarge"|"inf2.24xlarge"|"inf2.48xlarge"|"trn1n.32xlarge"|"i4g.large"|"i4g.xlarge"|"i4g.2xlarge"|"i4g.4xlarge"|"i4g.8xlarge"|"i4g.16xlarge"|"hpc7g.4xlarge"|"hpc7g.8xlarge"|"hpc7g.16xlarge"|"c7gn.medium"|"c7gn.large"|"c7gn.xlarge"|"c7gn.2xlarge"|"c7gn.4xlarge"|"c7gn.8xlarge"|"c7gn.12xlarge"|"c7gn.16xlarge"|"p5.48xlarge"|"m7i.large"|"m7i.xlarge"|"m7i.2xlarge"|"m7i.4xlarge"|"m7i.8xlarge"|"m7i.12xlarge"|"m7i.16xlarge"|"m7i.24xlarge"|"m7i.48xlarge"|"m7i-flex.large"|"m7i-flex.xlarge"|"m7i-flex.2xlarge"|"m7i-flex.4xlarge"|"m7i-flex.8xlarge"|"m7a.medium"|"m7a.large"|"m7a.xlarge"|"m7a.2xlarge"|"m7a.4xlarge"|"m7a.8xlarge"|"m7a.12xlarge"|"m7a.16xlarge"|"m7a.24xlarge"|"m7a.32xlarge"|"m7a.48xlarge"|"m7a.metal-48xl"|"hpc7a.12xlarge"|"hpc7a.24xlarge"|"hpc7a.48xlarge"|"hpc7a.96xlarge"|"c7gd.medium"|"c7gd.large"|"c7gd.xlarge"|"c7gd.2xlarge"|"c7gd.4xlarge"|"c7gd.8xlarge"|"c7gd.12xlarge"|"c7gd.16xlarge"|"m7gd.medium"|"m7gd.large"|"m7gd.xlarge"|"m7gd.2xlarge"|"m7gd.4xlarge"|"m7gd.8xlarge"|"m7gd.12xlarge"|"m7gd.16xlarge"|"r7gd.medium"|"r7gd.large"|"r7gd.xlarge"|"r7gd.2xlarge"|"r7gd.4xlarge"|"r7gd.8xlarge"|"r7gd.12xlarge"|"r7gd.16xlarge"|"r7a.medium"|"r7a.large"|"r7a.xlarge"|"r7a.2xlarge"|"r7a.4xlarge"|"r7a.8xlarge"|"r7a.12xlarge"|"r7a.16xlarge"|"r7a.24xlarge"|"r7a.32xlarge"|"r7a.48xlarge"|"c7i.large"|"c7i.xlarge"|"c7i.2xlarge"|"c7i.4xlarge"|"c7i.8xlarge"|"c7i.12xlarge"|"c7i.16xlarge"|"c7i.24xlarge"|"c7i.48xlarge"|"mac2-m2pro.metal"|"r7iz.large"|"r7iz.xlarge"|"r7iz.2xlarge"|"r7iz.4xlarge"|"r7iz.8xlarge"|"r7iz.12xlarge"|"r7iz.16xlarge"|"r7iz.32xlarge"|"c7a.medium"|"c7a.large"|"c7a.xlarge"|"c7a.2xlarge"|"c7a.4xlarge"|"c7a.8xlarge"|"c7a.12xlarge"|"c7a.16xlarge"|"c7a.24xlarge"|"c7a.32xlarge"|"c7a.48xlarge"|"c7a.metal-48xl"|"r7a.metal-48xl"|"r7i.large"|"r7i.xlarge"|"r7i.2xlarge"|"r7i.4xlarge"|"r7i.8xlarge"|"r7i.12xlarge"|"r7i.16xlarge"|"r7i.24xlarge"|"r7i.48xlarge"|"dl2q.24xlarge"|"mac2-m2.metal"|"i4i.12xlarge"|"i4i.24xlarge"|"c7i.metal-24xl"|"c7i.metal-48xl"|"m7i.metal-24xl"|"m7i.metal-48xl"|"r7i.metal-24xl"|"r7i.metal-48xl"|"r7iz.metal-16xl"|"r7iz.metal-32xl"|"c7gd.metal"|"m7gd.metal"|"r7gd.metal"|"g6.xlarge"|"g6.2xlarge"|"g6.4xlarge"|"g6.8xlarge"|"g6.12xlarge"|"g6.16xlarge"|"g6.24xlarge"|"g6.48xlarge"|"gr6.4xlarge"|"gr6.8xlarge"|"c7i-flex.large"|"c7i-flex.xlarge"|"c7i-flex.2xlarge"|"c7i-flex.4xlarge"|"c7i-flex.8xlarge"|"u7i-12tb.224xlarge"|"u7in-16tb.224xlarge"|"u7in-24tb.224xlarge"|"u7in-32tb.224xlarge"|"u7ib-12tb.224xlarge"|"c7gn.metal"|"r8g.medium"|"r8g.large"|"r8g.xlarge"|"r8g.2xlarge"|"r8g.4xlarge"|"r8g.8xlarge"|"r8g.12xlarge"|"r8g.16xlarge"|"r8g.24xlarge"|"r8g.48xlarge"|"r8g.metal-24xl"|"r8g.metal-48xl"|"mac2-m1ultra.metal"|"g6e.xlarge"|"g6e.2xlarge"|"g6e.4xlarge"|"g6e.8xlarge"|"g6e.12xlarge"|"g6e.16xlarge"|"g6e.24xlarge"|"g6e.48xlarge"|"c8g.medium"|"c8g.large"|"c8g.xlarge"|"c8g.2xlarge"|"c8g.4xlarge"|"c8g.8xlarge"|"c8g.12xlarge"|"c8g.16xlarge"|"c8g.24xlarge"|"c8g.48xlarge"|"c8g.metal-24xl"|"c8g.metal-48xl"|"m8g.medium"|"m8g.large"|"m8g.xlarge"|"m8g.2xlarge"|"m8g.4xlarge"|"m8g.8xlarge"|"m8g.12xlarge"|"m8g.16xlarge"|"m8g.24xlarge"|"m8g.48xlarge"|"m8g.metal-24xl"|"m8g.metal-48xl"|"x8g.medium"|"x8g.large"|"x8g.xlarge"|"x8g.2xlarge"|"x8g.4xlarge"|"x8g.8xlarge"|"x8g.12xlarge"|"x8g.16xlarge"|"x8g.24xlarge"|"x8g.48xlarge"|"x8g.metal-24xl"|"x8g.metal-48xl"|"i7ie.large"|"i7ie.xlarge"|"i7ie.2xlarge"|"i7ie.3xlarge"|"i7ie.6xlarge"|"i7ie.12xlarge"|"i7ie.18xlarge"|"i7ie.24xlarge"|"i7ie.48xlarge"|"i8g.large"|"i8g.xlarge"|"i8g.2xlarge"|"i8g.4xlarge"|"i8g.8xlarge"|"i8g.12xlarge"|"i8g.16xlarge"|"i8g.24xlarge"|"i8g.metal-24xl"|"u7i-6tb.112xlarge"|"u7i-8tb.112xlarge"|"u7inh-32tb.480xlarge"|"p5e.48xlarge"|"p5en.48xlarge"|"f2.12xlarge"|"f2.48xlarge"|"trn2.48xlarge",
  "KeyName": "string",
  "Monitoring": {
    "Enabled": true|false
  },
  "Placement": {
    "AvailabilityZone": "string",
    "Affinity": "string",
    "GroupName": "string",
    "HostId": "string",
    "Tenancy": "default"|"dedicated"|"host",
    "SpreadDomain": "string",
    "HostResourceGroupArn": "string",
    "PartitionNumber": integer,
    "GroupId": "string"
  },
  "RamDiskId": "string",
  "DisableApiTermination": true|false,
  "InstanceInitiatedShutdownBehavior": "stop"|"terminate",
  "UserData": "string",
  "TagSpecifications": [
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
  ],
  "ElasticGpuSpecifications": [
    {
      "Type": "string"
    }
    ...
  ],
  "ElasticInferenceAccelerators": [
    {
      "Type": "string",
      "Count": integer
    }
    ...
  ],
  "SecurityGroupIds": ["string", ...],
  "SecurityGroups": ["string", ...],
  "InstanceMarketOptions": {
    "MarketType": "spot"|"capacity-block",
    "SpotOptions": {
      "MaxPrice": "string",
      "SpotInstanceType": "one-time"|"persistent",
      "BlockDurationMinutes": integer,
      "ValidUntil": timestamp,
      "InstanceInterruptionBehavior": "hibernate"|"stop"|"terminate"
    }
  },
  "CreditSpecification": {
    "CpuCredits": "string"
  },
  "CpuOptions": {
    "CoreCount": integer,
    "ThreadsPerCore": integer,
    "AmdSevSnp": "enabled"|"disabled"
  },
  "CapacityReservationSpecification": {
    "CapacityReservationPreference": "capacity-reservations-only"|"open"|"none",
    "CapacityReservationTarget": {
      "CapacityReservationId": "string",
      "CapacityReservationResourceGroupArn": "string"
    }
  },
  "LicenseSpecifications": [
    {
      "LicenseConfigurationArn": "string"
    }
    ...
  ],
  "HibernationOptions": {
    "Configured": true|false
  },
  "MetadataOptions": {
    "HttpTokens": "optional"|"required",
    "HttpPutResponseHopLimit": integer,
    "HttpEndpoint": "disabled"|"enabled",
    "HttpProtocolIpv6": "disabled"|"enabled",
    "InstanceMetadataTags": "disabled"|"enabled"
  },
  "EnclaveOptions": {
    "Enabled": true|false
  },
  "InstanceRequirements": {
    "VCpuCount": {
      "Min": integer,
      "Max": integer
    },
    "MemoryMiB": {
      "Min": integer,
      "Max": integer
    },
    "CpuManufacturers": ["intel"|"amd"|"amazon-web-services"|"apple", ...],
    "MemoryGiBPerVCpu": {
      "Min": double,
      "Max": double
    },
    "ExcludedInstanceTypes": ["string", ...],
    "InstanceGenerations": ["current"|"previous", ...],
    "SpotMaxPricePercentageOverLowestPrice": integer,
    "OnDemandMaxPricePercentageOverLowestPrice": integer,
    "BareMetal": "included"|"required"|"excluded",
    "BurstablePerformance": "included"|"required"|"excluded",
    "RequireHibernateSupport": true|false,
    "NetworkInterfaceCount": {
      "Min": integer,
      "Max": integer
    },
    "LocalStorage": "included"|"required"|"excluded",
    "LocalStorageTypes": ["hdd"|"ssd", ...],
    "TotalLocalStorageGB": {
      "Min": double,
      "Max": double
    },
    "BaselineEbsBandwidthMbps": {
      "Min": integer,
      "Max": integer
    },
    "AcceleratorTypes": ["gpu"|"fpga"|"inference", ...],
    "AcceleratorCount": {
      "Min": integer,
      "Max": integer
    },
    "AcceleratorManufacturers": ["amazon-web-services"|"amd"|"nvidia"|"xilinx"|"habana", ...],
    "AcceleratorNames": ["a100"|"inferentia"|"k520"|"k80"|"m60"|"radeon-pro-v520"|"t4"|"vu9p"|"v100"|"a10g"|"h100"|"t4g", ...],
    "AcceleratorTotalMemoryMiB": {
      "Min": integer,
      "Max": integer
    },
    "NetworkBandwidthGbps": {
      "Min": double,
      "Max": double
    },
    "AllowedInstanceTypes": ["string", ...],
    "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice": integer,
    "BaselinePerformanceFactors": {
      "Cpu": {
        "References": [
          {
            "InstanceFamily": "string"
          }
          ...
        ]
      }
    }
  },
  "PrivateDnsNameOptions": {
    "HostnameType": "ip-name"|"resource-name",
    "EnableResourceNameDnsARecord": true|false,
    "EnableResourceNameDnsAAAARecord": true|false
  },
  "MaintenanceOptions": {
    "AutoRecovery": "default"|"disabled"
  },
  "DisableApiStop": true|false,
  "Operator": {
    "Principal": "string"
  },
  "NetworkPerformanceOptions": {
    "BandwidthWeighting": "default"|"vpc-1"|"ebs-1"
  }
}
```

`--resolve-alias` | `--no-resolve-alias` (boolean)

If `true` , and if a Systems Manager parameter is specified for `ImageId` , the AMI ID is displayed in the response for `imageID` . For more information, see [Use a Systems Manager parameter instead of an AMI ID](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#use-an-ssm-parameter-instead-of-an-ami-id) in the *Amazon EC2 User Guide* .

Default: `false`

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

**To create a launch template version**

This example creates a new launch template version based on version 1 of the launch template and specifies a different AMI ID.

Command:

```
aws ec2 create-launch-template-version --launch-template-id lt-0abcd290751193123 --version-description WebVersion2 --source-version 1 --launch-template-data '{"ImageId":"ami-c998b6b2"}'
```

Output:

```
{
  "LaunchTemplateVersion": {
      "VersionDescription": "WebVersion2",
      "LaunchTemplateId": "lt-0abcd290751193123",
      "LaunchTemplateName": "WebServers",
      "VersionNumber": 2,
      "CreatedBy": "arn:aws:iam::123456789012:root",
      "LaunchTemplateData": {
          "ImageId": "ami-c998b6b2",
          "InstanceType": "t2.micro",
          "NetworkInterfaces": [
              {
                  "Ipv6Addresses": [
                      {
                          "Ipv6Address": "2001:db8:1234:1a00::123"
                      }
                  ],
                  "DeviceIndex": 0,
                  "SubnetId": "subnet-7b16de0c",
                  "AssociatePublicIpAddress": true
              }
          ]
      },
      "DefaultVersion": false,
      "CreateTime": "2017-12-01T13:35:46.000Z"
  }
}
```

## Output

LaunchTemplateVersion -> (structure)

Information about the launch template version.

LaunchTemplateId -> (string)

The ID of the launch template.

LaunchTemplateName -> (string)

The name of the launch template.

VersionNumber -> (long)

The version number.

VersionDescription -> (string)

The description for the version.

CreateTime -> (timestamp)

The time the version was created.

CreatedBy -> (string)

The principal that created the version.

DefaultVersion -> (boolean)

Indicates whether the version is the default version.

LaunchTemplateData -> (structure)

Information about the launch template.

KernelId -> (string)

The ID of the kernel, if applicable.

EbsOptimized -> (boolean)

Indicates whether the instance is optimized for Amazon EBS I/O.

IamInstanceProfile -> (structure)

The IAM instance profile.

Arn -> (string)

The Amazon Resource Name (ARN) of the instance profile.

Name -> (string)

The name of the instance profile.

BlockDeviceMappings -> (list)

The block device mappings.

(structure)

Describes a block device mapping.

DeviceName -> (string)

The device name.

VirtualName -> (string)

The virtual device name (ephemeralN).

Ebs -> (structure)

Information about the block device for an EBS volume.

Encrypted -> (boolean)

Indicates whether the EBS volume is encrypted.

DeleteOnTermination -> (boolean)

Indicates whether the EBS volume is deleted on instance termination.

Iops -> (integer)

The number of I/O operations per second (IOPS) that the volume supports.

KmsKeyId -> (string)

Identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed KMS key to use for EBS encryption.

SnapshotId -> (string)

The ID of the snapshot.

VolumeSize -> (integer)

The size of the volume, in GiB.

VolumeType -> (string)

The volume type.

Throughput -> (integer)

The throughput that the volume supports, in MiB/s.

VolumeInitializationRate -> (integer)

The Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate) specified for the volume, in MiB/s. If no volume initialization rate was specified, the value is `null` .

NoDevice -> (string)

To omit the device from the block device mapping, specify an empty string.

NetworkInterfaces -> (list)

The network interfaces.

(structure)

Describes a network interface.

AssociateCarrierIpAddress -> (boolean)

Indicates whether to associate a Carrier IP address with eth0 for a new network interface.

Use this option when you launch an instance in a Wavelength Zone and want to associate a Carrier IP address with the network interface. For more information about Carrier IP addresses, see [Carrier IP address](https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html#provider-owned-ip) in the *Wavelength Developer Guide* .

AssociatePublicIpAddress -> (boolean)

Indicates whether to associate a public IPv4 address with eth0 for a new network interface.

Amazon Web Services charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the *Public IPv4 Address* tab on the [Amazon VPC pricing page](http://aws.amazon.com/vpc/pricing/) .

DeleteOnTermination -> (boolean)

Indicates whether the network interface is deleted when the instance is terminated.

Description -> (string)

A description for the network interface.

DeviceIndex -> (integer)

The device index for the network interface attachment.

Groups -> (list)

The IDs of one or more security groups.

(string)

InterfaceType -> (string)

The type of network interface.

Ipv6AddressCount -> (integer)

The number of IPv6 addresses for the network interface.

Ipv6Addresses -> (list)

The IPv6 addresses for the network interface.

(structure)

Describes an IPv6 address.

Ipv6Address -> (string)

The IPv6 address.

IsPrimaryIpv6 -> (boolean)

Determines if an IPv6 address associated with a network interface is the primary IPv6 address. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information, see [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) .

NetworkInterfaceId -> (string)

The ID of the network interface.

PrivateIpAddress -> (string)

The primary private IPv4 address of the network interface.

PrivateIpAddresses -> (list)

One or more private IPv4 addresses.

(structure)

Describes a secondary private IPv4 address for a network interface.

Primary -> (boolean)

Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.

PrivateIpAddress -> (string)

The private IPv4 address.

SecondaryPrivateIpAddressCount -> (integer)

The number of secondary private IPv4 addresses for the network interface.

SubnetId -> (string)

The ID of the subnet for the network interface.

NetworkCardIndex -> (integer)

The index of the network card.

Ipv4Prefixes -> (list)

One or more IPv4 prefixes assigned to the network interface.

(structure)

Information about the IPv4 delegated prefixes assigned to a network interface.

Ipv4Prefix -> (string)

The IPv4 delegated prefixes assigned to the network interface.

Ipv4PrefixCount -> (integer)

The number of IPv4 prefixes that Amazon Web Services automatically assigned to the network interface.

Ipv6Prefixes -> (list)

One or more IPv6 prefixes assigned to the network interface.

(structure)

Information about the IPv6 delegated prefixes assigned to a network interface.

Ipv6Prefix -> (string)

The IPv6 delegated prefixes assigned to the network interface.

Ipv6PrefixCount -> (integer)

The number of IPv6 prefixes that Amazon Web Services automatically assigned to the network interface.

PrimaryIpv6 -> (boolean)

The primary IPv6 address of the network interface. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information about primary IPv6 addresses, see [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) .

EnaSrdSpecification -> (structure)

Contains the ENA Express settings for instances launched from your launch template.

EnaSrdEnabled -> (boolean)

Indicates whether ENA Express is enabled for the network interface.

EnaSrdUdpSpecification -> (structure)

Configures ENA Express for UDP network traffic.

EnaSrdUdpEnabled -> (boolean)

Indicates whether UDP traffic to and from the instance uses ENA Express. To specify this setting, you must first enable ENA Express.

ConnectionTrackingSpecification -> (structure)

A security group connection tracking specification that enables you to set the timeout for connection tracking on an Elastic network interface. For more information, see [Idle connection tracking timeout](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts) in the *Amazon EC2 User Guide* .

TcpEstablishedTimeout -> (integer)

Timeout (in seconds) for idle TCP connections in an established state. Min: 60 seconds. Max: 432000 seconds (5 days). Default: 432000 seconds. Recommended: Less than 432000 seconds.

UdpTimeout -> (integer)

Timeout (in seconds) for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction. Min: 30 seconds. Max: 60 seconds. Default: 30 seconds.

UdpStreamTimeout -> (integer)

Timeout (in seconds) for idle UDP flows classified as streams which have seen more than one request-response transaction. Min: 60 seconds. Max: 180 seconds (3 minutes). Default: 180 seconds.

EnaQueueCount -> (integer)

The number of ENA queues created with the instance.

ImageId -> (string)

The ID of the AMI or a Systems Manager parameter. The Systems Manager parameter will resolve to the ID of the AMI at instance launch.

The value depends on what you specified in the request. The possible values are:

- If an AMI ID was specified in the request, then this is the AMI ID.
- If a Systems Manager parameter was specified in the request, and `ResolveAlias` was configured as `true` , then this is the AMI ID that the parameter is mapped to in the Parameter Store.
- If a Systems Manager parameter was specified in the request, and `ResolveAlias` was configured as `false` , then this is the parameter value.

For more information, see [Use a Systems Manager parameter instead of an AMI ID](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#use-an-ssm-parameter-instead-of-an-ami-id) in the *Amazon EC2 User Guide* .

InstanceType -> (string)

The instance type.

KeyName -> (string)

The name of the key pair.

Monitoring -> (structure)

The monitoring for the instance.

Enabled -> (boolean)

Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.

Placement -> (structure)

The placement of the instance.

AvailabilityZone -> (string)

The Availability Zone of the instance.

Affinity -> (string)

The affinity setting for the instance on the Dedicated Host.

GroupName -> (string)

The name of the placement group for the instance.

HostId -> (string)

The ID of the Dedicated Host for the instance.

Tenancy -> (string)

The tenancy of the instance. An instance with a tenancy of `dedicated` runs on single-tenant hardware.

SpreadDomain -> (string)

Reserved for future use.

HostResourceGroupArn -> (string)

The ARN of the host resource group in which to launch the instances.

PartitionNumber -> (integer)

The number of the partition the instance should launch in. Valid only if the placement group strategy is set to `partition` .

GroupId -> (string)

The Group ID of the placement group. You must specify the Placement Group **Group ID** to launch an instance in a shared placement group.

RamDiskId -> (string)

The ID of the RAM disk, if applicable.

DisableApiTermination -> (boolean)

If set to `true` , indicates that the instance cannot be terminated using the Amazon EC2 console, command line tool, or API.

InstanceInitiatedShutdownBehavior -> (string)

Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).

UserData -> (string)

The user data for the instance.

TagSpecifications -> (list)

The tags that are applied to the resources that are created during instance launch.

(structure)

The tags specification for the launch template.

ResourceType -> (string)

The type of resource to tag.

Tags -> (list)

The tags for the resource.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

ElasticGpuSpecifications -> (list)

Deprecated.

### Note

Amazon Elastic Graphics reached end of life on January 8, 2024.

(structure)

Deprecated.

### Note

Amazon Elastic Graphics reached end of life on January 8, 2024.

Type -> (string)

Deprecated.

### Note

Amazon Elastic Graphics reached end of life on January 8, 2024.

ElasticInferenceAccelerators -> (list)

### Note

Amazon Elastic Inference is no longer available.

An elastic inference accelerator to associate with the instance. Elastic inference accelerators are a resource you can attach to your Amazon EC2 instances to accelerate your Deep Learning (DL) inference workloads.

You cannot specify accelerators from different generations in the same request.

(structure)

### Note

Amazon Elastic Inference is no longer available.

Describes an elastic inference accelerator.

Type -> (string)

The type of elastic inference accelerator. The possible values are eia1.medium, eia1.large, and eia1.xlarge.

Count -> (integer)

The number of elastic inference accelerators to attach to the instance.

Default: 1

SecurityGroupIds -> (list)

The security group IDs.

(string)

SecurityGroups -> (list)

The security group names.

(string)

InstanceMarketOptions -> (structure)

The market (purchasing) option for the instances.

MarketType -> (string)

The market type.

SpotOptions -> (structure)

The options for Spot Instances.

MaxPrice -> (string)

The maximum hourly price youâre willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price. If you do specify this parameter, it must be more than USD $0.001. Specifying a value below USD $0.001 will result in an `InvalidParameterValue` error message when the launch template is used to launch an instance.

SpotInstanceType -> (string)

The Spot Instance request type.

BlockDurationMinutes -> (integer)

The required duration for the Spot Instances (also known as Spot blocks), in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360).

ValidUntil -> (timestamp)

The end date of the request. For a one-time request, the request remains active until all instances launch, the request is canceled, or this date is reached. If the request is persistent, it remains active until it is canceled or this date and time is reached.

InstanceInterruptionBehavior -> (string)

The behavior when a Spot Instance is interrupted.

CreditSpecification -> (structure)

The credit option for CPU usage of the instance.

CpuCredits -> (string)

The credit option for CPU usage of a T instance.

Valid values: `standard` | `unlimited`

CpuOptions -> (structure)

The CPU options for the instance. For more information, see [CPU options for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) in the *Amazon EC2 User Guide* .

CoreCount -> (integer)

The number of CPU cores for the instance.

ThreadsPerCore -> (integer)

The number of threads per CPU core.

AmdSevSnp -> (string)

Indicates whether the instance is enabled for AMD SEV-SNP. For more information, see [AMD SEV-SNP for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html) .

CapacityReservationSpecification -> (structure)

Information about the Capacity Reservation targeting option.

CapacityReservationPreference -> (string)

Indicates the instanceâs Capacity Reservation preferences. Possible preferences include:

- `open` - The instance can run in any `open` Capacity Reservation that has matching attributes (instance type, platform, Availability Zone).
- `none` - The instance avoids running in a Capacity Reservation even if one is available. The instance runs in On-Demand capacity.

CapacityReservationTarget -> (structure)

Information about the target Capacity Reservation or Capacity Reservation group.

CapacityReservationId -> (string)

The ID of the targeted Capacity Reservation.

CapacityReservationResourceGroupArn -> (string)

The ARN of the targeted Capacity Reservation group.

LicenseSpecifications -> (list)

The license configurations.

(structure)

Describes a license configuration.

LicenseConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the license configuration.

HibernationOptions -> (structure)

Indicates whether an instance is configured for hibernation. For more information, see [Hibernate your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html) in the *Amazon EC2 User Guide* .

Configured -> (boolean)

If this parameter is set to `true` , the instance is enabled for hibernation; otherwise, it is not enabled for hibernation.

MetadataOptions -> (structure)

The metadata options for the instance. For more information, see [Configure the Instance Metadata Service options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html) in the *Amazon EC2 User Guide* .

State -> (string)

The state of the metadata option changes.

`pending` - The metadata options are being updated and the instance is not ready to process metadata traffic with the new selection.

`applied` - The metadata options have been successfully applied on the instance.

HttpTokens -> (string)

Indicates whether IMDSv2 is required.

- `optional` - IMDSv2 is optional. You can choose whether to send a session token in your instance metadata retrieval requests. If you retrieve IAM role credentials without a session token, you receive the IMDSv1 role credentials. If you retrieve IAM role credentials using a valid session token, you receive the IMDSv2 role credentials.
- `required` - IMDSv2 is required. You must send a session token in your instance metadata retrieval requests. With this option, retrieving the IAM role credentials always returns IMDSv2 credentials; IMDSv1 credentials are not available.

HttpPutResponseHopLimit -> (integer)

The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel.

Default: 1

Possible values: Integers from 1 to 64

HttpEndpoint -> (string)

Enables or disables the HTTP metadata endpoint on your instances. If the parameter is not specified, the default state is `enabled` .

### Note

If you specify a value of `disabled` , you will not be able to access your instance metadata.

HttpProtocolIpv6 -> (string)

Enables or disables the IPv6 endpoint for the instance metadata service.

Default: `disabled`

InstanceMetadataTags -> (string)

Set to `enabled` to allow access to instance tags from the instance metadata. Set to `disabled` to turn off access to instance tags from the instance metadata. For more information, see [View tags for your EC2 instances using instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html) .

Default: `disabled`

EnclaveOptions -> (structure)

Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves.

Enabled -> (boolean)

If this parameter is set to `true` , the instance is enabled for Amazon Web Services Nitro Enclaves; otherwise, it is not enabled for Amazon Web Services Nitro Enclaves.

InstanceRequirements -> (structure)

The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with these attributes.

If you specify `InstanceRequirements` , you canât specify `InstanceTypes` .

VCpuCount -> (structure)

The minimum and maximum number of vCPUs.

Min -> (integer)

The minimum number of vCPUs. If the value is `0` , there is no minimum limit.

Max -> (integer)

The maximum number of vCPUs. If this parameter is not specified, there is no maximum limit.

MemoryMiB -> (structure)

The minimum and maximum amount of memory, in MiB.

Min -> (integer)

The minimum amount of memory, in MiB. If this parameter is not specified, there is no minimum limit.

Max -> (integer)

The maximum amount of memory, in MiB. If this parameter is not specified, there is no maximum limit.

CpuManufacturers -> (list)

The CPU manufacturers to include.

- For instance types with Intel CPUs, specify `intel` .
- For instance types with AMD CPUs, specify `amd` .
- For instance types with Amazon Web Services CPUs, specify `amazon-web-services` .
- For instance types with Apple CPUs, specify `apple` .

### Note

Donât confuse the CPU manufacturer with the CPU architecture. Instances will be launched with a compatible CPU architecture based on the Amazon Machine Image (AMI) that you specify in your launch template.

Default: Any manufacturer

(string)

MemoryGiBPerVCpu -> (structure)

The minimum and maximum amount of memory per vCPU, in GiB.

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of memory per vCPU, in GiB. If this parameter is not specified, there is no minimum limit.

Max -> (double)

The maximum amount of memory per vCPU, in GiB. If this parameter is not specified, there is no maximum limit.

ExcludedInstanceTypes -> (list)

The instance types to exclude.

You can use strings with one or more wild cards, represented by an asterisk (`*` ), to exclude an instance type, size, or generation. The following are examples: `m5.8xlarge` , `c5*.*` , `m5a.*` , `r*` , `*3*` .

For example, if you specify `c5*` ,Amazon EC2 will exclude the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*` , Amazon EC2 will exclude all the M5a instance types, but not the M5n instance types.

### Note

If you specify `ExcludedInstanceTypes` , you canât specify `AllowedInstanceTypes` .

Default: No excluded instance types

(string)

InstanceGenerations -> (list)

Indicates whether current or previous generation instance types are included. The current generation instance types are recommended for use. Current generation instance types are typically the latest two to three generations in each instance family. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide* .

For current generation instance types, specify `current` .

For previous generation instance types, specify `previous` .

Default: Current and previous generation instance types

(string)

SpotMaxPricePercentageOverLowestPrice -> (integer)

[Price protection] The price protection threshold for Spot Instances, as a percentage higher than an identified Spot price. The identified Spot price is the Spot price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified Spot price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose Spot price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 interprets as a percentage.

If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib` , the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.

This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) and [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html) .

### Note

Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you donât specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999` .

Default: `100`

OnDemandMaxPricePercentageOverLowestPrice -> (integer)

[Price protection] The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 interprets as a percentage.

To turn off price protection, specify a high value, such as `999999` .

This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) and [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html) .

### Note

If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib` , the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.

Default: `20`

BareMetal -> (string)

Indicates whether bare metal instance types must be included, excluded, or required.

- To include bare metal instance types, specify `included` .
- To require only bare metal instance types, specify `required` .
- To exclude bare metal instance types, specify `excluded` .

Default: `excluded`

BurstablePerformance -> (string)

Indicates whether burstable performance T instance types are included, excluded, or required. For more information, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) .

- To include burstable performance instance types, specify `included` .
- To require only burstable performance instance types, specify `required` .
- To exclude burstable performance instance types, specify `excluded` .

Default: `excluded`

RequireHibernateSupport -> (boolean)

Indicates whether instance types must support hibernation for On-Demand Instances.

This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) .

Default: `false`

NetworkInterfaceCount -> (structure)

The minimum and maximum number of network interfaces.

Default: No minimum or maximum limits

Min -> (integer)

The minimum number of network interfaces. If this parameter is not specified, there is no minimum limit.

Max -> (integer)

The maximum number of network interfaces. If this parameter is not specified, there is no maximum limit.

LocalStorage -> (string)

Indicates whether instance types with instance store volumes are included, excluded, or required. For more information, [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) in the *Amazon EC2 User Guide* .

- To include instance types with instance store volumes, specify `included` .
- To require only instance types with instance store volumes, specify `required` .
- To exclude instance types with instance store volumes, specify `excluded` .

Default: `included`

LocalStorageTypes -> (list)

The type of local storage that is required.

- For instance types with hard disk drive (HDD) storage, specify `hdd` .
- For instance types with solid state drive (SSD) storage, specify `ssd` .

Default: `hdd` and `ssd`

(string)

TotalLocalStorageGB -> (structure)

The minimum and maximum amount of total local storage, in GB.

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of total local storage, in GB. If this parameter is not specified, there is no minimum limit.

Max -> (double)

The maximum amount of total local storage, in GB. If this parameter is not specified, there is no maximum limit.

BaselineEbsBandwidthMbps -> (structure)

The minimum and maximum baseline bandwidth to Amazon EBS, in Mbps. For more information, see [Amazon EBSâoptimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) in the *Amazon EC2 User Guide* .

Default: No minimum or maximum limits

Min -> (integer)

The minimum baseline bandwidth, in Mbps. If this parameter is not specified, there is no minimum limit.

Max -> (integer)

The maximum baseline bandwidth, in Mbps. If this parameter is not specified, there is no maximum limit.

AcceleratorTypes -> (list)

The accelerator types that must be on the instance type.

- For instance types with FPGA accelerators, specify `fpga` .
- For instance types with GPU accelerators, specify `gpu` .
- For instance types with Inference accelerators, specify `inference` .

Default: Any accelerator type

(string)

AcceleratorCount -> (structure)

The minimum and maximum number of accelerators (GPUs, FPGAs, or Amazon Web Services Inferentia chips) on an instance.

To exclude accelerator-enabled instance types, set `Max` to `0` .

Default: No minimum or maximum limits

Min -> (integer)

The minimum number of accelerators. If this parameter is not specified, there is no minimum limit.

Max -> (integer)

The maximum number of accelerators. If this parameter is not specified, there is no maximum limit.

AcceleratorManufacturers -> (list)

Indicates whether instance types must have accelerators by specific manufacturers.

- For instance types with Amazon Web Services devices, specify `amazon-web-services` .
- For instance types with AMD devices, specify `amd` .
- For instance types with Habana devices, specify `habana` .
- For instance types with NVIDIA devices, specify `nvidia` .
- For instance types with Xilinx devices, specify `xilinx` .

Default: Any manufacturer

(string)

AcceleratorNames -> (list)

The accelerators that must be on the instance type.

- For instance types with NVIDIA A10G GPUs, specify `a10g` .
- For instance types with NVIDIA A100 GPUs, specify `a100` .
- For instance types with NVIDIA H100 GPUs, specify `h100` .
- For instance types with Amazon Web Services Inferentia chips, specify `inferentia` .
- For instance types with NVIDIA GRID K520 GPUs, specify `k520` .
- For instance types with NVIDIA K80 GPUs, specify `k80` .
- For instance types with NVIDIA M60 GPUs, specify `m60` .
- For instance types with AMD Radeon Pro V520 GPUs, specify `radeon-pro-v520` .
- For instance types with NVIDIA T4 GPUs, specify `t4` .
- For instance types with NVIDIA T4G GPUs, specify `t4g` .
- For instance types with Xilinx VU9P FPGAs, specify `vu9p` .
- For instance types with NVIDIA V100 GPUs, specify `v100` .

Default: Any accelerator

(string)

AcceleratorTotalMemoryMiB -> (structure)

The minimum and maximum amount of total accelerator memory, in MiB.

Default: No minimum or maximum limits

Min -> (integer)

The minimum amount of accelerator memory, in MiB. If this parameter is not specified, there is no minimum limit.

Max -> (integer)

The maximum amount of accelerator memory, in MiB. If this parameter is not specified, there is no maximum limit.

NetworkBandwidthGbps -> (structure)

The minimum and maximum amount of network bandwidth, in gigabits per second (Gbps).

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of network bandwidth, in Gbps. If this parameter is not specified, there is no minimum limit.

Max -> (double)

The maximum amount of network bandwidth, in Gbps. If this parameter is not specified, there is no maximum limit.

AllowedInstanceTypes -> (list)

The instance types to apply your specified attributes against. All other instance types are ignored, even if they match your specified attributes.

You can use strings with one or more wild cards, represented by an asterisk (`*` ), to allow an instance type, size, or generation. The following are examples: `m5.8xlarge` , `c5*.*` , `m5a.*` , `r*` , `*3*` .

For example, if you specify `c5*` ,Amazon EC2 will allow the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*` , Amazon EC2 will allow all the M5a instance types, but not the M5n instance types.

### Note

If you specify `AllowedInstanceTypes` , you canât specify `ExcludedInstanceTypes` .

Default: All instance types

(string)

MaxSpotPriceAsPercentageOfOptimalOnDemandPrice -> (integer)

[Price protection] The price protection threshold for Spot Instances, as a percentage of an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 interprets as a percentage.

If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib` , the price protection threshold is based on the per vCPU or per memory price instead of the per instance price.

### Note

Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you donât specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999` .

BaselinePerformanceFactors -> (structure)

The baseline performance to consider, using an instance family as a baseline reference. The instance family establishes the lowest acceptable level of performance. Amazon EC2 uses this baseline to guide instance type selection, but there is no guarantee that the selected instance types will always exceed the baseline for every application. Currently, this parameter only supports CPU performance as a baseline performance factor. For more information, see [Performance protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html#ec2fleet-abis-performance-protection) in the *Amazon EC2 User Guide* .

Cpu -> (structure)

The CPU performance to consider, using an instance family as the baseline reference.

References -> (list)

Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture differences.

### Note

Currently, only one instance family can be specified in the list.

(structure)

Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture.

### Note

Currently, only one instance family can be specified in the list.

InstanceFamily -> (string)

The instance family to use as a baseline reference.

### Note

Ensure that you specify the correct value for the instance family. The instance family is everything before the period (`.` ) in the instance type name. For example, in the instance type `c6i.large` , the instance family is `c6i` , not `c6` . For more information, see [Amazon EC2 instance type naming conventions](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html) in *Amazon EC2 Instance Types* .

The following instance families are *not supported* for performance protection:

- `c1`
- `g3` | `g3s`
- `hpc7g`
- `m1` | `m2`
- `mac1` | `mac2` | `mac2-m1ultra` | `mac2-m2` | `mac2-m2pro`
- `p3dn` | `p4d` | `p5`
- `t1`
- `u-12tb1` | `u-18tb1` | `u-24tb1` | `u-3tb1` | `u-6tb1` | `u-9tb1` | `u7i-12tb` | `u7in-16tb` | `u7in-24tb` | `u7in-32tb`

If you enable performance protection by specifying a supported instance family, the returned instance types will exclude the above unsupported instance families.

If you specify an unsupported instance family as a value for baseline performance, the API returns an empty response for [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements) and an exception for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) , [RequestSpotFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet) , [ModifyFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyFleet) , and [ModifySpotFleetRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySpotFleetRequest) .

PrivateDnsNameOptions -> (structure)

The options for the instance hostname.

HostnameType -> (string)

The type of hostname to assign to an instance.

EnableResourceNameDnsARecord -> (boolean)

Indicates whether to respond to DNS queries for instance hostnames with DNS A records.

EnableResourceNameDnsAAAARecord -> (boolean)

Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.

MaintenanceOptions -> (structure)

The maintenance options for your instance.

AutoRecovery -> (string)

Disables the automatic recovery behavior of your instance or sets it to default.

DisableApiStop -> (boolean)

Indicates whether the instance is enabled for stop protection. For more information, see [Enable stop protection for your EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-stop-protection.html) in the *Amazon EC2 User Guide* .

Operator -> (structure)

The entity that manages the launch template.

Managed -> (boolean)

If `true` , the resource is managed by a service provider.

Principal -> (string)

If `managed` is `true` , then the principal is returned. The principal is the service provider that manages the resource.

NetworkPerformanceOptions -> (structure)

Contains the launch template settings for network performance options for your instance.

BandwidthWeighting -> (string)

When you configure network bandwidth weighting, you can boost baseline bandwidth for either networking or EBS by up to 25%. The total available baseline bandwidth for your instance remains the same. The default option uses the standard bandwidth configuration for your instance type.

Operator -> (structure)

The entity that manages the launch template.

Managed -> (boolean)

If `true` , the resource is managed by a service provider.

Principal -> (string)

If `managed` is `true` , then the principal is returned. The principal is the service provider that manages the resource.

Warning -> (structure)

If the new version of the launch template contains parameters or parameter combinations that are not valid, an error code and an error message are returned for each issue thatâs found.

Errors -> (list)

The error codes and error messages.

(structure)

The error code and error message that is returned for a parameter or parameter combination that is not valid when a new launch template or new version of a launch template is created.

Code -> (string)

The error code that indicates why the parameter or parameter combination is not valid. For more information about error codes, see [Error codes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html) .

Message -> (string)

The error message that describes why the parameter or parameter combination is not valid. For more information about error messages, see [Error codes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html) .