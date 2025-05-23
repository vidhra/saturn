# run-scheduled-instancesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-scheduled-instances.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-scheduled-instances.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# run-scheduled-instances

## Description

Launches the specified Scheduled Instances.

Before you can launch a Scheduled Instance, you must purchase it and obtain an identifier using  PurchaseScheduledInstances .

You must launch a Scheduled Instance during its scheduled time period. You canât stop or reboot a Scheduled Instance, but you can terminate it as needed. If you terminate a Scheduled Instance before the current scheduled time period ends, you can launch it again after a few minutes.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/RunScheduledInstances)

## Synopsis

```
run-scheduled-instances
[--client-token <value>]
[--dry-run | --no-dry-run]
[--instance-count <value>]
--launch-specification <value>
--scheduled-instance-id <value>
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

`--client-token` (string)

Unique, case-sensitive identifier that ensures the idempotency of the request. For more information, see [Ensuring Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--instance-count` (integer)

The number of instances.

Default: 1

`--launch-specification` (structure)

The launch specification. You must match the instance type, Availability Zone, network, and platform of the schedule that you purchased.

BlockDeviceMappings -> (list)

The block device mapping entries.

(structure)

Describes a block device mapping for a Scheduled Instance.

DeviceName -> (string)

The device name (for example, `/dev/sdh` or `xvdh` ).

Ebs -> (structure)

Parameters used to set up EBS volumes automatically when the instance is launched.

DeleteOnTermination -> (boolean)

Indicates whether the volume is deleted on instance termination.

Encrypted -> (boolean)

Indicates whether the volume is encrypted. You can attached encrypted volumes only to instances that support them.

Iops -> (integer)

The number of I/O operations per second (IOPS) to provision for a `gp3` , `io1` , or `io2` volume.

SnapshotId -> (string)

The ID of the snapshot.

VolumeSize -> (integer)

The size of the volume, in GiB.

Default: If youâre creating the volume from a snapshot and donât specify a volume size, the default is the snapshot size.

VolumeType -> (string)

The volume type.

Default: `gp2`

NoDevice -> (string)

To omit the device from the block device mapping, specify an empty string.

VirtualName -> (string)

The virtual device name (`ephemeral` N). Instance store volumes are numbered starting from 0. An instance type with two available instance store volumes can specify mappings for `ephemeral0` and `ephemeral1` . The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.

Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.

EbsOptimized -> (boolean)

Indicates whether the instances are optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isnât available with all instance types. Additional usage charges apply when using an EBS-optimized instance.

Default: `false`

IamInstanceProfile -> (structure)

The IAM instance profile.

Arn -> (string)

The Amazon Resource Name (ARN).

Name -> (string)

The name.

ImageId -> (string)

The ID of the Amazon Machine Image (AMI).

InstanceType -> (string)

The instance type.

KernelId -> (string)

The ID of the kernel.

KeyName -> (string)

The name of the key pair.

Monitoring -> (structure)

Enable or disable monitoring for the instances.

Enabled -> (boolean)

Indicates whether monitoring is enabled.

NetworkInterfaces -> (list)

The network interfaces.

(structure)

Describes a network interface for a Scheduled Instance.

AssociatePublicIpAddress -> (boolean)

Indicates whether to assign a public IPv4 address to instances launched in a VPC. The public IPv4 address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is `true` .

Amazon Web Services charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the *Public IPv4 Address* tab on the [Amazon VPC pricing page](http://aws.amazon.com/vpc/pricing/) .

DeleteOnTermination -> (boolean)

Indicates whether to delete the interface when the instance is terminated.

Description -> (string)

The description.

DeviceIndex -> (integer)

The index of the device for the network interface attachment.

Groups -> (list)

The IDs of the security groups.

(string)

Ipv6AddressCount -> (integer)

The number of IPv6 addresses to assign to the network interface. The IPv6 addresses are automatically selected from the subnet range.

Ipv6Addresses -> (list)

The specific IPv6 addresses from the subnet range.

(structure)

Describes an IPv6 address.

Ipv6Address -> (string)

The IPv6 address.

NetworkInterfaceId -> (string)

The ID of the network interface.

PrivateIpAddress -> (string)

The IPv4 address of the network interface within the subnet.

PrivateIpAddressConfigs -> (list)

The private IPv4 addresses.

(structure)

Describes a private IPv4 address for a Scheduled Instance.

Primary -> (boolean)

Indicates whether this is a primary IPv4 address. Otherwise, this is a secondary IPv4 address.

PrivateIpAddress -> (string)

The IPv4 address.

SecondaryPrivateIpAddressCount -> (integer)

The number of secondary private IPv4 addresses.

SubnetId -> (string)

The ID of the subnet.

Placement -> (structure)

The placement information.

AvailabilityZone -> (string)

The Availability Zone.

GroupName -> (string)

The name of the placement group.

RamdiskId -> (string)

The ID of the RAM disk.

SecurityGroupIds -> (list)

The IDs of the security groups.

(string)

SubnetId -> (string)

The ID of the subnet in which to launch the instances.

UserData -> (string)

The base64-encoded MIME user data.

JSON Syntax:

```
{
  "BlockDeviceMappings": [
    {
      "DeviceName": "string",
      "Ebs": {
        "DeleteOnTermination": true|false,
        "Encrypted": true|false,
        "Iops": integer,
        "SnapshotId": "string",
        "VolumeSize": integer,
        "VolumeType": "string"
      },
      "NoDevice": "string",
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
  "InstanceType": "string",
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
          "Ipv6Address": "string"
        }
        ...
      ],
      "NetworkInterfaceId": "string",
      "PrivateIpAddress": "string",
      "PrivateIpAddressConfigs": [
        {
          "Primary": true|false,
          "PrivateIpAddress": "string"
        }
        ...
      ],
      "SecondaryPrivateIpAddressCount": integer,
      "SubnetId": "string"
    }
    ...
  ],
  "Placement": {
    "AvailabilityZone": "string",
    "GroupName": "string"
  },
  "RamdiskId": "string",
  "SecurityGroupIds": ["string", ...],
  "SubnetId": "string",
  "UserData": "string"
}
```

`--scheduled-instance-id` (string)

The Scheduled Instance ID.

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

**To launch a Scheduled Instance**

This example launches the specified Scheduled Instance in a VPC.

Command:

```
aws ec2 run-scheduled-instances --scheduled-instance-id sci-1234-1234-1234-1234-123456789012 --instance-count 1 --launch-specification file://launch-specification.json
```

Launch-specification.json:

```
{
  "ImageId": "ami-12345678",
  "KeyName": "my-key-pair",
  "InstanceType": "c4.large",
  "NetworkInterfaces": [
    {
        "DeviceIndex": 0,
        "SubnetId": "subnet-12345678",
        "AssociatePublicIpAddress": true,
        "Groups": ["sg-12345678"]
    }
  ],
  "IamInstanceProfile": {
      "Name": "my-iam-role"
  }
}
```

Output:

```
{
  "InstanceIdSet": [
      "i-1234567890abcdef0"
  ]
}
```

This example launches the specified Scheduled Instance in EC2-Classic.

Command:

```
aws ec2 run-scheduled-instances --scheduled-instance-id sci-1234-1234-1234-1234-123456789012 --instance-count 1 --launch-specification file://launch-specification.json
```

Launch-specification.json:

```
{
  "ImageId": "ami-12345678",
  "KeyName": "my-key-pair",
  "SecurityGroupIds": ["sg-12345678"],
  "InstanceType": "c4.large",
  "Placement": {
    "AvailabilityZone": "us-west-2b"
  }
  "IamInstanceProfile": {
      "Name": "my-iam-role"
  }
}
```

Output:

```
{
  "InstanceIdSet": [
      "i-1234567890abcdef0"
  ]
}
```

## Output

InstanceIdSet -> (list)

The IDs of the newly launched instances.

(string)