# describe-spot-fleet-requestsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-spot-fleet-requests.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-spot-fleet-requests.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-spot-fleet-requests

## Description

Describes your Spot Fleet requests.

Spot Fleet requests are deleted 48 hours after they are canceled and their instances are terminated.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSpotFleetRequests)

`describe-spot-fleet-requests` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `SpotFleetRequestConfigs`

## Synopsis

```
describe-spot-fleet-requests
[--dry-run | --no-dry-run]
[--spot-fleet-request-ids <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--spot-fleet-request-ids` (list)

The IDs of the Spot Fleet requests.

(string)

Syntax:

```
"string" "string" ...
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To describe your Spot fleet requests**

This example describes all of your Spot fleet requests.

Command:

```
aws ec2 describe-spot-fleet-requests
```

Output:

```
{
  "SpotFleetRequestConfigs": [
      {
          "SpotFleetRequestId": "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE",
          "SpotFleetRequestConfig": {
              "TargetCapacity": 20,
              "LaunchSpecifications": [
                  {
                      "EbsOptimized": false,
                      "NetworkInterfaces": [
                          {
                              "SubnetId": "subnet-a61dafcf",
                              "DeviceIndex": 0,
                              "DeleteOnTermination": false,
                              "AssociatePublicIpAddress": true,
                              "SecondaryPrivateIpAddressCount": 0
                          }
                      ],
                      "InstanceType": "cc2.8xlarge",
                      "ImageId": "ami-1a2b3c4d"
                  },
                  {
                      "EbsOptimized": false,
                      "NetworkInterfaces": [
                          {
                              "SubnetId": "subnet-a61dafcf",
                              "DeviceIndex": 0,
                              "DeleteOnTermination": false,
                              "AssociatePublicIpAddress": true,
                              "SecondaryPrivateIpAddressCount": 0
                          }
                      ],
                      "InstanceType": "r3.8xlarge",
                      "ImageId": "ami-1a2b3c4d"
                  }
              ],
              "SpotPrice": "0.05",
              "IamFleetRole": "arn:aws:iam::123456789012:role/my-spot-fleet-role"
          },
          "SpotFleetRequestState": "active"
      },
      {
          "SpotFleetRequestId": "sfr-306341ed-9739-402e-881b-ce47bEXAMPLE",
          "SpotFleetRequestConfig": {
              "TargetCapacity": 20,
              "LaunchSpecifications": [
                  {
                      "EbsOptimized": false,
                      "NetworkInterfaces": [
                          {
                              "SubnetId": "subnet-6e7f829e",
                              "DeviceIndex": 0,
                              "DeleteOnTermination": false,
                              "AssociatePublicIpAddress": true,
                              "SecondaryPrivateIpAddressCount": 0
                          }
                      ],
                      "InstanceType": "m3.medium",
                      "ImageId": "ami-1a2b3c4d"
                  }
              ],
              "SpotPrice": "0.05",
              "IamFleetRole": "arn:aws:iam::123456789012:role/my-spot-fleet-role"
          },
          "SpotFleetRequestState": "active"
      }
  ]
}
```

**To describe a Spot fleet request**

This example describes the specified Spot fleet request.

Command:

```
aws ec2 describe-spot-fleet-requests --spot-fleet-request-ids sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE
```

Output:

```
{
  "SpotFleetRequestConfigs": [
      {
          "SpotFleetRequestId": "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE",
          "SpotFleetRequestConfig": {
              "TargetCapacity": 20,
              "LaunchSpecifications": [
                  {
                      "EbsOptimized": false,
                      "NetworkInterfaces": [
                          {
                              "SubnetId": "subnet-a61dafcf",
                              "DeviceIndex": 0,
                              "DeleteOnTermination": false,
                              "AssociatePublicIpAddress": true,
                              "SecondaryPrivateIpAddressCount": 0
                          }
                      ],
                      "InstanceType": "cc2.8xlarge",
                      "ImageId": "ami-1a2b3c4d"
                  },
                  {
                      "EbsOptimized": false,
                      "NetworkInterfaces": [
                          {
                              "SubnetId": "subnet-a61dafcf",
                              "DeviceIndex": 0,
                              "DeleteOnTermination": false,
                              "AssociatePublicIpAddress": true,
                              "SecondaryPrivateIpAddressCount": 0
                          }
                      ],
                      "InstanceType": "r3.8xlarge",
                      "ImageId": "ami-1a2b3c4d"
                  }
              ],
              "SpotPrice": "0.05",
              "IamFleetRole": "arn:aws:iam::123456789012:role/my-spot-fleet-role"
          },
          "SpotFleetRequestState": "active"
      }
  ]
}
```

## Output

NextToken -> (string)

The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.

SpotFleetRequestConfigs -> (list)

Information about the configuration of your Spot Fleet.

(structure)

Describes a Spot Fleet request.

ActivityStatus -> (string)

The progress of the Spot Fleet request. If there is an error, the status is `error` . After all requests are placed, the status is `pending_fulfillment` . If the size of the fleet is equal to or greater than its target capacity, the status is `fulfilled` . If the size of the fleet is decreased, the status is `pending_termination` while Spot Instances are terminating.

CreateTime -> (timestamp)

The creation date and time of the request.

SpotFleetRequestConfig -> (structure)

The configuration of the Spot Fleet request.

AllocationStrategy -> (string)

The strategy that determines how to allocate the target Spot Instance capacity across the Spot Instance pools specified by the Spot Fleet launch configuration. For more information, see [Allocation strategies for Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-allocation-strategy.html) in the *Amazon EC2 User Guide* .

priceCapacityOptimized (recommended)

Spot Fleet identifies the pools with the highest capacity availability for the number of instances that are launching. This means that we will request Spot Instances from the pools that we believe have the lowest chance of interruption in the near term. Spot Fleet then requests Spot Instances from the lowest priced of these pools.

capacityOptimized

Spot Fleet identifies the pools with the highest capacity availability for the number of instances that are launching. This means that we will request Spot Instances from the pools that we believe have the lowest chance of interruption in the near term. To give certain instance types a higher chance of launching first, use `capacityOptimizedPrioritized` . Set a priority for each instance type by using the `Priority` parameter for `LaunchTemplateOverrides` . You can assign the same priority to different `LaunchTemplateOverrides` . EC2 implements the priorities on a best-effort basis, but optimizes for capacity first. `capacityOptimizedPrioritized` is supported only if your Spot Fleet uses a launch template. Note that if the `OnDemandAllocationStrategy` is set to `prioritized` , the same priority is applied when fulfilling On-Demand capacity.

diversified

Spot Fleet requests instances from all of the Spot Instance pools that you specify.

lowestPrice (not recommended)

### Warning

We donât recommend the `lowestPrice` allocation strategy because it has the highest risk of interruption for your Spot Instances.

Spot Fleet requests instances from the lowest priced Spot Instance pool that has available capacity. If the lowest priced pool doesnât have available capacity, the Spot Instances come from the next lowest priced pool that has available capacity. If a pool runs out of capacity before fulfilling your desired capacity, Spot Fleet will continue to fulfill your request by drawing from the next lowest priced pool. To ensure that your desired capacity is met, you might receive Spot Instances from several pools. Because this strategy only considers instance price and not capacity availability, it might lead to high interruption rates.

Default: `lowestPrice`

OnDemandAllocationStrategy -> (string)

The order of the launch template overrides to use in fulfilling On-Demand capacity. If you specify `lowestPrice` , Spot Fleet uses price to determine the order, launching the lowest price first. If you specify `prioritized` , Spot Fleet uses the priority that you assign to each Spot Fleet launch template override, launching the highest priority first. If you do not specify a value, Spot Fleet defaults to `lowestPrice` .

SpotMaintenanceStrategies -> (structure)

The strategies for managing your Spot Instances that are at an elevated risk of being interrupted.

CapacityRebalance -> (structure)

The Spot Instance replacement strategy to use when Amazon EC2 emits a signal that your Spot Instance is at an elevated risk of being interrupted. For more information, see [Capacity rebalancing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-capacity-rebalance.html) in the *Amazon EC2 User Guide* .

ReplacementStrategy -> (string)

The replacement strategy to use. Only available for fleets of type `maintain` .

`launch` - Spot Fleet launches a new replacement Spot Instance when a rebalance notification is emitted for an existing Spot Instance in the fleet. Spot Fleet does not terminate the instances that receive a rebalance notification. You can terminate the old instances, or you can leave them running. You are charged for all instances while they are running.

`launch-before-terminate` - Spot Fleet launches a new replacement Spot Instance when a rebalance notification is emitted for an existing Spot Instance in the fleet, and then, after a delay that you specify (in `TerminationDelay` ), terminates the instances that received a rebalance notification.

TerminationDelay -> (integer)

The amount of time (in seconds) that Amazon EC2 waits before terminating the old Spot Instance after launching a new replacement Spot Instance.

Required when `ReplacementStrategy` is set to `launch-before-terminate` .

Not valid when `ReplacementStrategy` is set to `launch` .

Valid values: Minimum value of `120` seconds. Maximum value of `7200` seconds.

ClientToken -> (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of your listings. This helps to avoid duplicate listings. For more information, see [Ensuring Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .

ExcessCapacityTerminationPolicy -> (string)

Indicates whether running instances should be terminated if you decrease the target capacity of the Spot Fleet request below the current size of the Spot Fleet.

Supported only for fleets of type `maintain` .

FulfilledCapacity -> (double)

The number of units fulfilled by this request compared to the set target capacity. You cannot set this value.

OnDemandFulfilledCapacity -> (double)

The number of On-Demand units fulfilled by this request compared to the set target On-Demand capacity.

IamFleetRole -> (string)

The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that grants the Spot Fleet the permission to request, launch, terminate, and tag instances on your behalf. For more information, see [Spot Fleet prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-requests.html#spot-fleet-prerequisites) in the *Amazon EC2 User Guide* . Spot Fleet can terminate Spot Instances on your behalf when you cancel its Spot Fleet request using [CancelSpotFleetRequests](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelSpotFleetRequests) or when the Spot Fleet request expires, if you set `TerminateInstancesWithExpiration` .

LaunchSpecifications -> (list)

The launch specifications for the Spot Fleet request. If you specify `LaunchSpecifications` , you canât specify `LaunchTemplateConfigs` . If you include On-Demand capacity in your request, you must use `LaunchTemplateConfigs` .

### Note

If an AMI specified in a launch specification is deregistered or disabled, no new instances can be launched from the AMI. For fleets of type `maintain` , the target capacity will not be maintained.

(structure)

Describes the launch specification for one or more Spot Instances. If you include On-Demand capacity in your fleet request or want to specify an EFA network device, you canât use `SpotFleetLaunchSpecification` ; you must use [LaunchTemplateConfig](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateConfig.html) .

AddressingType -> (string)

Deprecated.

BlockDeviceMappings -> (list)

One or more block devices that are mapped to the Spot Instances. You canât specify both a snapshot ID and an encryption value. This is because only blank volumes can be encrypted on creation. If a snapshot is the basis for a volume, it is not blank and its encryption status is used for the volume encryption status.

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

Indicates whether the instances are optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isnât available with all instance types. Additional usage charges apply when using an EBS Optimized instance.

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

The instance type.

KernelId -> (string)

The ID of the kernel.

KeyName -> (string)

The name of the key pair.

Monitoring -> (structure)

Enable or disable monitoring for the instances.

Enabled -> (boolean)

Enables monitoring for the instance.

Default: `false`

NetworkInterfaces -> (list)

The network interfaces.

### Note

`SpotFleetLaunchSpecification` does not support Elastic Fabric Adapter (EFA). You must use [LaunchTemplateConfig](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateConfig.html) instead.

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

The placement information.

AvailabilityZone -> (string)

The Availability Zone.

[Spot Fleet only] To specify multiple Availability Zones, separate them using commas; for example, âus-west-2a, us-west-2bâ.

GroupName -> (string)

The name of the placement group.

Tenancy -> (string)

The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of `dedicated` runs on single-tenant hardware. The `host` tenancy is not supported for Spot Instances.

RamdiskId -> (string)

The ID of the RAM disk. Some kernels require additional drivers at launch. Check the kernel requirements for information about whether you need to specify a RAM disk. To find kernel requirements, refer to the Amazon Web Services Resource Center and search for the kernel ID.

SpotPrice -> (string)

The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.

### Warning

If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.

SubnetId -> (string)

The IDs of the subnets in which to launch the instances. To specify multiple subnets, separate them using commas; for example, âsubnet-1234abcdeexample1, subnet-0987cdef6example2â.

If you specify a network interface, you must specify any subnets as part of the network interface instead of using this parameter.

UserData -> (string)

The base64-encoded user data that instances use when starting up. User data is limited to 16 KB.

WeightedCapacity -> (double)

The number of units provided by the specified instance type. These are the same units that you chose to set the target capacity in terms of instances, or a performance characteristic such as vCPUs, memory, or I/O.

If the target capacity divided by this value is not a whole number, Amazon EC2 rounds the number of instances to the next whole number. If this value is not specified, the default is 1.

### Note

When specifying weights, the price used in the `lowestPrice` and `priceCapacityOptimized` allocation strategies is per *unit* hour (where the instance price is divided by the specified weight). However, if all the specified weights are above the requested `TargetCapacity` , resulting in only 1 instance being launched, the price used is per *instance* hour.

TagSpecifications -> (list)

The tags to apply during creation.

(structure)

The tags for a Spot Fleet resource.

ResourceType -> (string)

The type of resource. Currently, the only resource type that is supported is `instance` . To tag the Spot Fleet request on creation, use the `TagSpecifications` parameter in `` [SpotFleetRequestConfigData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotFleetRequestConfigData.html) `` .

Tags -> (list)

The tags.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

InstanceRequirements -> (structure)

The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with those attributes.

### Note

If you specify `InstanceRequirements` , you canât specify `InstanceType` .

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

SecurityGroups -> (list)

The security groups.

If you specify a network interface, you must specify any security groups as part of the network interface instead of using this parameter.

(structure)

Describes a security group.

GroupId -> (string)

The ID of the security group.

GroupName -> (string)

The name of the security group.

LaunchTemplateConfigs -> (list)

The launch template and overrides. If you specify `LaunchTemplateConfigs` , you canât specify `LaunchSpecifications` . If you include On-Demand capacity in your request, you must use `LaunchTemplateConfigs` .

(structure)

Describes a launch template and overrides.

LaunchTemplateSpecification -> (structure)

The launch template to use. Make sure that the launch template does not contain the `NetworkInterfaceId` parameter because you canât specify a network interface ID in a Spot Fleet.

LaunchTemplateId -> (string)

The ID of the launch template.

You must specify the `LaunchTemplateId` or the `LaunchTemplateName` , but not both.

LaunchTemplateName -> (string)

The name of the launch template.

You must specify the `LaunchTemplateName` or the `LaunchTemplateId` , but not both.

Version -> (string)

The launch template version number, `$Latest` , or `$Default` . You must specify a value, otherwise the request fails.

If the value is `$Latest` , Amazon EC2 uses the latest version of the launch template.

If the value is `$Default` , Amazon EC2 uses the default version of the launch template.

Overrides -> (list)

Any parameters that you specify override the same parameters in the launch template.

(structure)

Describes overrides for a launch template.

InstanceType -> (string)

The instance type.

SpotPrice -> (string)

The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.

### Warning

If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.

SubnetId -> (string)

The ID of the subnet in which to launch the instances.

AvailabilityZone -> (string)

The Availability Zone in which to launch the instances.

WeightedCapacity -> (double)

The number of units provided by the specified instance type. These are the same units that you chose to set the target capacity in terms of instances, or a performance characteristic such as vCPUs, memory, or I/O.

If the target capacity divided by this value is not a whole number, Amazon EC2 rounds the number of instances to the next whole number. If this value is not specified, the default is 1.

### Note

When specifying weights, the price used in the `lowestPrice` and `priceCapacityOptimized` allocation strategies is per *unit* hour (where the instance price is divided by the specified weight). However, if all the specified weights are above the requested `TargetCapacity` , resulting in only 1 instance being launched, the price used is per *instance* hour.

Priority -> (double)

The priority for the launch template override. The highest priority is launched first.

If `OnDemandAllocationStrategy` is set to `prioritized` , Spot Fleet uses priority to determine which launch template override to use first in fulfilling On-Demand capacity.

If the Spot `AllocationStrategy` is set to `capacityOptimizedPrioritized` , Spot Fleet uses priority on a best-effort basis to determine which launch template override to use in fulfilling Spot capacity, but optimizes for capacity first.

Valid values are whole numbers starting at `0` . The lower the number, the higher the priority. If no number is set, the launch template override has the lowest priority. You can set the same priority for different launch template overrides.

InstanceRequirements -> (structure)

The instance requirements. When you specify instance requirements, Amazon EC2 will identify instance types with the provided requirements, and then use your On-Demand and Spot allocation strategies to launch instances from these instance types, in the same way as when you specify a list of instance types.

### Note

If you specify `InstanceRequirements` , you canât specify `InstanceType` .

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

SpotPrice -> (string)

The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.

### Warning

If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.

TargetCapacity -> (integer)

The number of units to request for the Spot Fleet. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O. If the request type is `maintain` , you can specify a target capacity of 0 and add capacity later.

OnDemandTargetCapacity -> (integer)

The number of On-Demand units to request. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O. If the request type is `maintain` , you can specify a target capacity of 0 and add capacity later.

OnDemandMaxTotalPrice -> (string)

The maximum amount per hour for On-Demand Instances that youâre willing to pay. You can use the `onDemandMaxTotalPrice` parameter, the `spotMaxTotalPrice` parameter, or both parameters to ensure that your fleet cost does not exceed your budget. If you set a maximum price per hour for the On-Demand Instances and Spot Instances in your request, Spot Fleet will launch instances until it reaches the maximum amount youâre willing to pay. When the maximum amount youâre willing to pay is reached, the fleet stops launching instances even if it hasnât met the target capacity.

### Note

If your fleet includes T instances that are configured as `unlimited` , and if their average CPU usage exceeds the baseline utilization, you will incur a charge for surplus credits. The `onDemandMaxTotalPrice` does not account for surplus credits, and, if you use surplus credits, your final cost might be higher than what you specified for `onDemandMaxTotalPrice` . For more information, see [Surplus credits can incur charges](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html#unlimited-mode-surplus-credits) in the *Amazon EC2 User Guide* .

SpotMaxTotalPrice -> (string)

The maximum amount per hour for Spot Instances that youâre willing to pay. You can use the `spotMaxTotalPrice` parameter, the `onDemandMaxTotalPrice` parameter, or both parameters to ensure that your fleet cost does not exceed your budget. If you set a maximum price per hour for the On-Demand Instances and Spot Instances in your request, Spot Fleet will launch instances until it reaches the maximum amount youâre willing to pay. When the maximum amount youâre willing to pay is reached, the fleet stops launching instances even if it hasnât met the target capacity.

### Note

If your fleet includes T instances that are configured as `unlimited` , and if their average CPU usage exceeds the baseline utilization, you will incur a charge for surplus credits. The `spotMaxTotalPrice` does not account for surplus credits, and, if you use surplus credits, your final cost might be higher than what you specified for `spotMaxTotalPrice` . For more information, see [Surplus credits can incur charges](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html#unlimited-mode-surplus-credits) in the *Amazon EC2 User Guide* .

TerminateInstancesWithExpiration -> (boolean)

Indicates whether running Spot Instances are terminated when the Spot Fleet request expires.

Type -> (string)

The type of request. Indicates whether the Spot Fleet only requests the target capacity or also attempts to maintain it. When this value is `request` , the Spot Fleet only places the required requests. It does not attempt to replenish Spot Instances if capacity is diminished, nor does it submit requests in alternative Spot pools if capacity is not available. When this value is `maintain` , the Spot Fleet maintains the target capacity. The Spot Fleet places the required requests to meet capacity and automatically replenishes any interrupted instances. Default: `maintain` . `instant` is listed but is not used by Spot Fleet.

ValidFrom -> (timestamp)

The start date and time of the request, in UTC format (*YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z). By default, Amazon EC2 starts fulfilling the request immediately.

ValidUntil -> (timestamp)

The end date and time of the request, in UTC format (*YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z). After the end date and time, no new Spot Instance requests are placed or able to fulfill the request. If no value is specified, the Spot Fleet request remains until you cancel it.

ReplaceUnhealthyInstances -> (boolean)

Indicates whether Spot Fleet should replace unhealthy instances.

InstanceInterruptionBehavior -> (string)

The behavior when a Spot Instance is interrupted. The default is `terminate` .

LoadBalancersConfig -> (structure)

One or more Classic Load Balancers and target groups to attach to the Spot Fleet request. Spot Fleet registers the running Spot Instances with the specified Classic Load Balancers and target groups.

With Network Load Balancers, Spot Fleet cannot register instances that have the following instance types: C1, CC1, CC2, CG1, CG2, CR1, CS1, G1, G2, HI1, HS1, M1, M2, M3, and T1.

ClassicLoadBalancersConfig -> (structure)

The Classic Load Balancers.

ClassicLoadBalancers -> (list)

One or more Classic Load Balancers.

(structure)

Describes a Classic Load Balancer.

Name -> (string)

The name of the load balancer.

TargetGroupsConfig -> (structure)

The target groups.

TargetGroups -> (list)

One or more target groups.

(structure)

Describes a load balancer target group.

Arn -> (string)

The Amazon Resource Name (ARN) of the target group.

InstancePoolsToUseCount -> (integer)

The number of Spot pools across which to allocate your target Spot capacity. Valid only when Spot **AllocationStrategy** is set to `lowest-price` . Spot Fleet selects the cheapest Spot pools and evenly allocates your target Spot capacity across the number of Spot pools that you specify.

Note that Spot Fleet attempts to draw Spot Instances from the number of pools that you specify on a best effort basis. If a pool runs out of Spot capacity before fulfilling your target capacity, Spot Fleet will continue to fulfill your request by drawing from the next cheapest pool. To ensure that your target capacity is met, you might receive Spot Instances from more than the number of pools that you specified. Similarly, if most of the pools have no Spot capacity, you might receive your full target capacity from fewer than the number of pools that you specified.

Context -> (string)

Reserved.

TargetCapacityUnitType -> (string)

The unit for the target capacity. You can specify this parameter only when using attribute-based instance type selection.

Default: `units` (the number of instances)

TagSpecifications -> (list)

The key-value pair for tagging the Spot Fleet request on creation. The value for `ResourceType` must be `spot-fleet-request` , otherwise the Spot Fleet request fails. To tag instances at launch, specify the tags in the [launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#create-launch-template) (valid only if you use `LaunchTemplateConfigs` ) or in the `` [SpotFleetTagSpecification](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotFleetTagSpecification.html) `` (valid only if you use `LaunchSpecifications` ). For information about tagging after launch, see [Tag your resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-resources) .

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

SpotFleetRequestId -> (string)

The ID of the Spot Fleet request.

SpotFleetRequestState -> (string)

The state of the Spot Fleet request.

Tags -> (list)

The tags for a Spot Fleet resource.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.