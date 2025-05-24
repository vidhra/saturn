# describe-launch-configurationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-launch-configurations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-launch-configurations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [autoscaling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/index.html#cli-aws-autoscaling) ]

# describe-launch-configurations

## Description

Gets information about the launch configurations in the account and Region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeLaunchConfigurations)

`describe-launch-configurations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `LaunchConfigurations`

## Synopsis

```
describe-launch-configurations
[--launch-configuration-names <value>]
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

`--launch-configuration-names` (list)

The launch configuration names. If you omit this property, all launch configurations are described.

Array Members: Maximum number of 50 items.

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

**Example 1: To describe the specified launch configuration**

This example describes the specified launch configuration.

```
aws autoscaling describe-launch-configurations \
    --launch-configuration-names my-launch-config
```

Output:

```
{
    "LaunchConfigurations": [
        {
            "LaunchConfigurationName": "my-launch-config",
            "LaunchConfigurationARN": "arn:aws:autoscaling:us-west-2:123456789012:launchConfiguration:98d3b196-4cf9-4e88-8ca1-8547c24ced8b:launchConfigurationName/my-launch-config",
            "ImageId": "ami-0528a5175983e7f28",
            "KeyName": "my-key-pair-uswest2",
            "SecurityGroups": [
                "sg-05eaec502fcdadc2e"
            ],
            "ClassicLinkVPCSecurityGroups": [],
            "UserData": "",
            "InstanceType": "t2.micro",
            "KernelId": "",
            "RamdiskId": "",
            "BlockDeviceMappings": [
                {
                    "DeviceName": "/dev/xvda",
                    "Ebs": {
                        "SnapshotId": "snap-06c1606ba5ca274b1",
                        "VolumeSize": 8,
                        "VolumeType": "gp2",
                        "DeleteOnTermination": true,
                        "Encrypted": false
                    }
                }
            ],
            "InstanceMonitoring": {
                "Enabled": true
            },
            "CreatedTime": "2020-10-28T02:39:22.321Z",
            "EbsOptimized": false,
            "AssociatePublicIpAddress": true,
            "MetadataOptions": {
                "HttpTokens": "required",
                "HttpPutResponseHopLimit": 1,
                "HttpEndpoint": "disabled"
            }
        }
    ]
}
```

**Example 2: To describe a specified number of launch configurations**

To return a specific number of launch configurations, use the `--max-items` option.

```
aws autoscaling describe-launch-configurations \
    --max-items 1
```

If the output includes a `NextToken` field, there are more launch configurations. To get the additional launch configurations, use the value of this field with the `--starting-token` option in a subsequent call as follows.

```
aws autoscaling describe-launch-configurations \
    --starting-token Z3M3LMPEXAMPLE
```

## Output

LaunchConfigurations -> (list)

The launch configurations.

(structure)

Describes a launch configuration.

LaunchConfigurationName -> (string)

The name of the launch configuration.

LaunchConfigurationARN -> (string)

The Amazon Resource Name (ARN) of the launch configuration.

ImageId -> (string)

The ID of the Amazon Machine Image (AMI) to use to launch your EC2 instances. For more information, see [Find a Linux AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html) in the *Amazon EC2 User Guide for Linux Instances* .

KeyName -> (string)

The name of the key pair.

For more information, see [Amazon EC2 key pairs and Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in the *Amazon EC2 User Guide for Linux Instances* .

SecurityGroups -> (list)

A list that contains the security groups to assign to the instances in the Auto Scaling group. For more information, see [Control traffic to your Amazon Web Services resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) in the *Amazon Virtual Private Cloud User Guide* .

(string)

ClassicLinkVPCId -> (string)

Available for backward compatibility.

ClassicLinkVPCSecurityGroups -> (list)

Available for backward compatibility.

(string)

UserData -> (string)

The user data to make available to the launched EC2 instances. For more information, see [Instance metadata and user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) (Linux) and [Instance metadata and user data](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-instance-metadata.html) (Windows). If you are using a command line tool, base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide base64-encoded text. User data is limited to 16 KB.

InstanceType -> (string)

The instance type for the instances. For information about available instance types, see [Available instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes) in the *Amazon EC2 User Guide for Linux Instances* .

KernelId -> (string)

The ID of the kernel associated with the AMI.

RamdiskId -> (string)

The ID of the RAM disk associated with the AMI.

BlockDeviceMappings -> (list)

The block device mapping entries that define the block devices to attach to the instances at launch. By default, the block devices specified in the block device mapping for the AMI are used. For more information, see [Block device mappings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html) in the *Amazon EC2 User Guide for Linux Instances* .

(structure)

Describes a block device mapping.

VirtualName -> (string)

The name of the instance store volume (virtual device) to attach to an instance at launch. The name must be in the form ephemeral*X* where *X* is a number starting from zero (0), for example, `ephemeral0` .

DeviceName -> (string)

The device name assigned to the volume (for example, `/dev/sdh` or `xvdh` ). For more information, see [Device naming on Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html) in the *Amazon EC2 User Guide for Linux Instances* .

### Note

To define a block device mapping, set the device name and exactly one of the following properties: `Ebs` , `NoDevice` , or `VirtualName` .

Ebs -> (structure)

Information to attach an EBS volume to an instance at launch.

SnapshotId -> (string)

The snapshot ID of the volume to use.

You must specify either a `VolumeSize` or a `SnapshotId` .

VolumeSize -> (integer)

The volume size, in GiBs. The following are the supported volumes sizes for each volume type:

- `gp2` and `gp3` : 1-16,384
- `io1` : 4-16,384
- `st1` and `sc1` : 125-16,384
- `standard` : 1-1,024

You must specify either a `SnapshotId` or a `VolumeSize` . If you specify both `SnapshotId` and `VolumeSize` , the volume size must be equal or greater than the size of the snapshot.

VolumeType -> (string)

The volume type. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) in the *Amazon EBS User Guide* .

Valid values: `standard` | `io1` | `gp2` | `st1` | `sc1` | `gp3`

DeleteOnTermination -> (boolean)

Indicates whether the volume is deleted on instance termination. For Amazon EC2 Auto Scaling, the default value is `true` .

Iops -> (integer)

The number of input/output (I/O) operations per second (IOPS) to provision for the volume. For `gp3` and `io1` volumes, this represents the number of IOPS that are provisioned for the volume. For `gp2` volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.

The following are the supported values for each volume type:

- `gp3` : 3,000-16,000 IOPS
- `io1` : 100-64,000 IOPS

For `io1` volumes, we guarantee 64,000 IOPS only for [Instances built on the Amazon Web Services Nitro System](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) . Other instance families guarantee performance up to 32,000 IOPS.

`Iops` is supported when the volume type is `gp3` or `io1` and required only when the volume type is `io1` . (Not used with `standard` , `gp2` , `st1` , or `sc1` volumes.)

Encrypted -> (boolean)

Specifies whether the volume should be encrypted. Encrypted EBS volumes can only be attached to instances that support Amazon EBS encryption. For more information, see [Requirements for Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption-requirements.html) in the *Amazon EBS User Guide* . If your AMI uses encrypted volumes, you can also only launch it on supported instance types.

### Note

If you are creating a volume from a snapshot, you cannot create an unencrypted volume from an encrypted snapshot. Also, you cannot specify a KMS key ID when using a launch configuration.

If you enable encryption by default, the EBS volumes that you create are always encrypted, either using the Amazon Web Services managed KMS key or a customer-managed KMS key, regardless of whether the snapshot was encrypted.

For more information, see [Use Amazon Web Services KMS keys to encrypt Amazon EBS volumes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-data-protection.html#encryption) in the *Amazon EC2 Auto Scaling User Guide* .

Throughput -> (integer)

The throughput (MiBps) to provision for a `gp3` volume.

NoDevice -> (boolean)

Setting this value to `true` prevents a volume that is included in the block device mapping of the AMI from being mapped to the specified device name at launch.

If `NoDevice` is `true` for the root device, instances might fail the EC2 health check. In that case, Amazon EC2 Auto Scaling launches replacement instances.

InstanceMonitoring -> (structure)

Controls whether instances in this group are launched with detailed (`true` ) or basic (`false` ) monitoring.

For more information, see [Configure monitoring for Auto Scaling instances](https://docs.aws.amazon.com/autoscaling/latest/userguide/enable-as-instance-metrics.html) in the *Amazon EC2 Auto Scaling User Guide* .

Enabled -> (boolean)

If `true` , detailed monitoring is enabled. Otherwise, basic monitoring is enabled.

SpotPrice -> (string)

The maximum hourly price to be paid for any Spot Instance launched to fulfill the request. Spot Instances are launched when the price you specify exceeds the current Spot price. For more information, see [Requesting Spot Instances for fault-tolerant and flexible applications](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-template-spot-instances.html) in the *Amazon EC2 Auto Scaling User Guide* .

IamInstanceProfile -> (string)

The name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance. The instance profile contains the IAM role. For more information, see [IAM role for applications that run on Amazon EC2 instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html) in the *Amazon EC2 Auto Scaling User Guide* .

CreatedTime -> (timestamp)

The creation date and time for the launch configuration.

EbsOptimized -> (boolean)

Specifies whether the launch configuration is optimized for EBS I/O (`true` ) or not (`false` ). For more information, see [Amazon EBS-optimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) in the *Amazon EC2 User Guide for Linux Instances* .

AssociatePublicIpAddress -> (boolean)

Specifies whether to assign a public IPv4 address to the groupâs instances. If the instance is launched into a default subnet, the default is to assign a public IPv4 address, unless you disabled the option to assign a public IPv4 address on the subnet. If the instance is launched into a nondefault subnet, the default is not to assign a public IPv4 address, unless you enabled the option to assign a public IPv4 address on the subnet. For more information, see [Provide network connectivity for your Auto Scaling instances using Amazon VPC](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html) in the *Amazon EC2 Auto Scaling User Guide* .

PlacementTenancy -> (string)

The tenancy of the instance, either `default` or `dedicated` . An instance with `dedicated` tenancy runs on isolated, single-tenant hardware and can only be launched into a VPC.

MetadataOptions -> (structure)

The metadata options for the instances. For more information, see [Configure the instance metadata options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-config.html#launch-configurations-imds) in the *Amazon EC2 Auto Scaling User Guide* .

HttpTokens -> (string)

The state of token usage for your instance metadata requests. If the parameter is not specified in the request, the default state is `optional` .

If the state is `optional` , you can choose to retrieve instance metadata with or without a signed token header on your request. If you retrieve the IAM role credentials without a token, the version 1.0 role credentials are returned. If you retrieve the IAM role credentials using a valid signed token, the version 2.0 role credentials are returned.

If the state is `required` , you must send a signed token header with any instance metadata retrieval requests. In this state, retrieving the IAM role credentials always returns the version 2.0 credentials; the version 1.0 credentials are not available.

HttpPutResponseHopLimit -> (integer)

The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel.

Default: 1

HttpEndpoint -> (string)

This parameter enables or disables the HTTP metadata endpoint on your instances. If the parameter is not specified, the default state is `enabled` .

### Note

If you specify a value of `disabled` , you will not be able to access your instance metadata.

NextToken -> (string)

A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the `NextToken` value when requesting the next set of items. This value is null when there are no more items to return.