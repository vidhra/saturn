# get-launch-template-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-launch-template-data.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-launch-template-data.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# get-launch-template-data

## Description

Retrieves the configuration data of the specified instance. You can use this data to create a launch template.

This action calls on other describe actions to get instance information. Depending on your instance configuration, you may need to allow the following actions in your IAM policy: `DescribeSpotInstanceRequests` , `DescribeInstanceCreditSpecifications` , `DescribeVolumes` , and `DescribeInstanceAttribute` . Or, you can allow `describe*` depending on your instance requirements.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/GetLaunchTemplateData)

## Synopsis

```
get-launch-template-data
[--dry-run | --no-dry-run]
--instance-id <value>
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

`--instance-id` (string)

The ID of the instance.

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

**To get instance data for a launch template**

This example gets data about the specified instance and uses the `--query` option to return the contents in `LaunchTemplateData`. You can use the output as a base to create a new launch template or launch template version.

Command:

```
aws ec2 get-launch-template-data --instance-id i-0123d646e8048babc --query 'LaunchTemplateData'
```

Output:

```
{
      "Monitoring": {},
      "ImageId": "ami-8c1be5f6",
      "BlockDeviceMappings": [
          {
              "DeviceName": "/dev/xvda",
              "Ebs": {
                  "DeleteOnTermination": true
              }
          }
      ],
      "EbsOptimized": false,
      "Placement": {
          "Tenancy": "default",
          "GroupName": "",
          "AvailabilityZone": "us-east-1a"
      },
      "InstanceType": "t2.micro",
      "NetworkInterfaces": [
          {
              "Description": "",
              "NetworkInterfaceId": "eni-35306abc",
              "PrivateIpAddresses": [
                  {
                      "Primary": true,
                      "PrivateIpAddress": "10.0.0.72"
                  }
              ],
              "SubnetId": "subnet-7b16de0c",
              "Groups": [
                  "sg-7c227019"
              ],
              "Ipv6Addresses": [
                  {
                      "Ipv6Address": "2001:db8:1234:1a00::123"
                  }
              ],
              "PrivateIpAddress": "10.0.0.72"
          }
      ]
}
```

## Output

LaunchTemplateData -> (structure)

The instance data.

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