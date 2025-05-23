# describe-instancesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-instances.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-instances.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opsworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/index.html#cli-aws-opsworks) ]

# describe-instances

## Description

Requests a description of a set of instances.

### Note

This call accepts only one resource-identifying parameter.

**Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information about user permissions, see [Managing User Permissions](https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeInstances)

## Synopsis

```
describe-instances
[--stack-id <value>]
[--layer-id <value>]
[--instance-ids <value>]
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

`--stack-id` (string)

A stack ID. If you use this parameter, `DescribeInstances` returns descriptions of the instances associated with the specified stack.

`--layer-id` (string)

A layer ID. If you use this parameter, `DescribeInstances` returns descriptions of the instances associated with the specified layer.

`--instance-ids` (list)

An array of instance IDs to be described. If you use this parameter, `DescribeInstances` returns a description of the specified instances. Otherwise, it returns a description of every instance.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To describe instances**

The following `describe-instances` command describes the instances in a specified stack:

```
aws opsworks --region us-east-1 describe-instances --stack-id 8c428b08-a1a1-46ce-a5f8-feddc43771b8
```

*Output*: The following output example is for a stack with two instances. The first is a registered
EC2 instance, and the second was created by AWS OpsWorks.

```
{
  "Instances": [
    {
      "StackId": "71c7ca72-55ae-4b6a-8ee1-a8dcded3fa0f",
      "PrivateDns": "ip-10-31-39-66.us-west-2.compute.internal",
      "LayerIds": [
        "26cf1d32-6876-42fa-bbf1-9cadc0bff938"
      ],
      "EbsOptimized": false,
      "ReportedOs": {
        "Version": "14.04",
        "Name": "ubuntu",
        "Family": "debian"
      },
      "Status": "online",
      "InstanceId": "4d6d1710-ded9-42a1-b08e-b043ad7af1e2",
      "SshKeyName": "US-West-2",
      "InfrastructureClass": "ec2",
      "RootDeviceVolumeId": "vol-d08ec6c1",
      "SubnetId": "subnet-b8de0ddd",
      "InstanceType": "t1.micro",
      "CreatedAt": "2015-02-24T20:52:49+00:00",
      "AmiId": "ami-35501205",
      "Hostname": "ip-192-0-2-0",
      "Ec2InstanceId": "i-5cd23551",
      "PublicDns": "ec2-192-0-2-0.us-west-2.compute.amazonaws.com",
      "SecurityGroupIds": [
        "sg-c4d3f0a1"
      ],
      "Architecture": "x86_64",
      "RootDeviceType": "ebs",
      "InstallUpdatesOnBoot": true,
      "Os": "Custom",
      "VirtualizationType": "paravirtual",
      "AvailabilityZone": "us-west-2a",
      "PrivateIp": "10.31.39.66",
      "PublicIp": "192.0.2.06",
      "RegisteredBy": "arn:aws:iam::123456789102:user/AWS/OpsWorks/OpsWorks-EC2Register-i-5cd23551"
    },
    {
      "StackId": "71c7ca72-55ae-4b6a-8ee1-a8dcded3fa0f",
      "PrivateDns": "ip-10-31-39-158.us-west-2.compute.internal",
      "SshHostRsaKeyFingerprint": "69:6b:7b:8b:72:f3:ed:23:01:00:05:bc:9f:a4:60:c1",
      "LayerIds": [
        "26cf1d32-6876-42fa-bbf1-9cadc0bff938"
      ],
      "EbsOptimized": false,
      "ReportedOs": {},
      "Status": "booting",
      "InstanceId": "9b137a0d-2f5d-4cc0-9704-13da4b31fdcb",
      "SshKeyName": "US-West-2",
      "InfrastructureClass": "ec2",
      "RootDeviceVolumeId": "vol-e09dd5f1",
      "SubnetId": "subnet-b8de0ddd",
      "InstanceProfileArn": "arn:aws:iam::123456789102:instance-profile/aws-opsworks-ec2-role",
      "InstanceType": "c3.large",
      "CreatedAt": "2015-02-24T21:29:33+00:00",
      "AmiId": "ami-9fc29baf",
      "SshHostDsaKeyFingerprint": "fc:87:95:c3:f5:e1:3b:9f:d2:06:6e:62:9a:35:27:e8",
      "Ec2InstanceId": "i-8d2dca80",
      "PublicDns": "ec2-192-0-2-1.us-west-2.compute.amazonaws.com",
      "SecurityGroupIds": [
        "sg-b022add5",
        "sg-b122add4"
      ],
      "Architecture": "x86_64",
      "RootDeviceType": "ebs",
      "InstallUpdatesOnBoot": true,
      "Os": "Amazon Linux 2014.09",
      "VirtualizationType": "paravirtual",
      "AvailabilityZone": "us-west-2a",
      "Hostname": "custom11",
      "PrivateIp": "10.31.39.158",
      "PublicIp": "192.0.2.0"
    }
  ]
}
```

**More Information**

For more information, see [Instances](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances.html) in the *AWS OpsWorks User Guide*.

## Output

Instances -> (list)

An array of `Instance` objects that describe the instances.

(structure)

Describes an instance.

AgentVersion -> (string)

The agent version. This parameter is set to `INHERIT` if the instance inherits the default stack setting or to a a version number for a fixed agent version.

AmiId -> (string)

A custom AMI ID to be used to create the instance. For more information, see [Instances](https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html)

Architecture -> (string)

The instance architecture: âi386â or âx86_64â.

Arn -> (string)

The instanceâs Amazon Resource Number (ARN).

AutoScalingType -> (string)

For load-based or time-based instances, the type.

AvailabilityZone -> (string)

The instance Availability Zone. For more information, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) .

BlockDeviceMappings -> (list)

An array of `BlockDeviceMapping` objects that specify the instanceâs block device mappings.

(structure)

Describes a block device mapping. This data type maps directly to the Amazon EC2 [BlockDeviceMapping](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html) data type.

DeviceName -> (string)

The device name that is exposed to the instance, such as `/dev/sdh` . For the root device, you can use the explicit device name or you can set this parameter to `ROOT_DEVICE` and OpsWorks Stacks will provide the correct device name.

NoDevice -> (string)

Suppresses the specified device included in the AMIâs block device mapping.

VirtualName -> (string)

The virtual device name. For more information, see [BlockDeviceMapping](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html) .

Ebs -> (structure)

An `EBSBlockDevice` that defines how to configure an Amazon EBS volume when the instance is launched.

SnapshotId -> (string)

The snapshot ID.

Iops -> (integer)

The number of I/O operations per second (IOPS) that the volume supports. For more information, see [EbsBlockDevice](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDevice.html) .

VolumeSize -> (integer)

The volume size, in GiB. For more information, see [EbsBlockDevice](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDevice.html) .

VolumeType -> (string)

The volume type. `gp2` for General Purpose (SSD) volumes, `io1` for Provisioned IOPS (SSD) volumes, `st1` for Throughput Optimized hard disk drives (HDD), `sc1` for Cold HDD,and `standard` for Magnetic volumes.

If you specify the `io1` volume type, you must also specify a value for the `Iops` attribute. The maximum ratio of provisioned IOPS to requested volume size (in GiB) is 50:1. Amazon Web Services uses the default volume size (in GiB) specified in the AMI attributes to set IOPS to 50 x (volume size).

DeleteOnTermination -> (boolean)

Whether the volume is deleted on instance termination.

CreatedAt -> (string)

The time that the instance was created.

EbsOptimized -> (boolean)

Whether this is an Amazon EBS-optimized instance.

Ec2InstanceId -> (string)

The ID of the associated Amazon EC2 instance.

EcsClusterArn -> (string)

For container instances, the Amazon ECS clusterâs ARN.

EcsContainerInstanceArn -> (string)

For container instances, the instanceâs ARN.

ElasticIp -> (string)

The instance [Elastic IP address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) .

Hostname -> (string)

The instance host name. The following are character limits for instance host names.

- Linux-based instances: 63 characters
- Windows-based instances: 15 characters

InfrastructureClass -> (string)

For registered instances, the infrastructure class: `ec2` or `on-premises` .

InstallUpdatesOnBoot -> (boolean)

Whether to install operating system and package updates when the instance boots. The default value is `true` . If this value is set to `false` , you must update instances manually by using  CreateDeployment to run the `update_dependencies` stack command or by manually running `yum` (Amazon Linux) or `apt-get` (Ubuntu) on the instances.

### Note

We strongly recommend using the default value of `true` to ensure that your instances have the latest security updates.

InstanceId -> (string)

The instance ID.

InstanceProfileArn -> (string)

The ARN of the instanceâs IAM profile. For more information about IAM ARNs, see [Using Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) .

InstanceType -> (string)

The instance type, such as `t2.micro` .

LastServiceErrorId -> (string)

The ID of the last service error. For more information, call  DescribeServiceErrors .

LayerIds -> (list)

An array containing the instance layer IDs.

(string)

Os -> (string)

The instanceâs operating system.

Platform -> (string)

The instanceâs platform.

PrivateDns -> (string)

The instanceâs private DNS name.

PrivateIp -> (string)

The instanceâs private IP address.

PublicDns -> (string)

The instance public DNS name.

PublicIp -> (string)

The instance public IP address.

RegisteredBy -> (string)

For registered instances, who performed the registration.

ReportedAgentVersion -> (string)

The instanceâs reported OpsWorks Stacks agent version.

ReportedOs -> (structure)

For registered instances, the reported operating system.

Family -> (string)

The operating system family.

Name -> (string)

The operating system name.

Version -> (string)

The operating system version.

RootDeviceType -> (string)

The instanceâs root device type. For more information, see [Storage for the Root Device](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device) .

RootDeviceVolumeId -> (string)

The root device volume ID.

SecurityGroupIds -> (list)

An array containing the instance security group IDs.

(string)

SshHostDsaKeyFingerprint -> (string)

The SSH keyâs Deep Security Agent (DSA) fingerprint.

SshHostRsaKeyFingerprint -> (string)

The SSH keyâs RSA fingerprint.

SshKeyName -> (string)

The instanceâs Amazon EC2 key-pair name.

StackId -> (string)

The stack ID.

Status -> (string)

The instance status:

- `booting`
- `connection_lost`
- `online`
- `pending`
- `rebooting`
- `requested`
- `running_setup`
- `setup_failed`
- `shutting_down`
- `start_failed`
- `stop_failed`
- `stopped`
- `stopping`
- `terminated`
- `terminating`

SubnetId -> (string)

The instanceâs subnet ID; applicable only if the stack is running in a VPC.

Tenancy -> (string)

The instanceâs tenancy option, such as `dedicated` or `host` .

VirtualizationType -> (string)

The instanceâs virtualization type: `paravirtual` or `hvm` .