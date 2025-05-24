# create-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opsworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/index.html#cli-aws-opsworks) ]

# create-instance

## Description

Creates an instance in a specified stack. For more information, see [Adding an Instance to a Layer](https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-add.html) .

**Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see [Managing User Permissions](https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateInstance)

## Synopsis

```
create-instance
--stack-id <value>
--layer-ids <value>
--instance-type <value>
[--auto-scaling-type <value>]
[--hostname <value>]
[--os <value>]
[--ami-id <value>]
[--ssh-key-name <value>]
[--availability-zone <value>]
[--virtualization-type <value>]
[--subnet-id <value>]
[--architecture <value>]
[--root-device-type <value>]
[--block-device-mappings <value>]
[--install-updates-on-boot | --no-install-updates-on-boot]
[--ebs-optimized | --no-ebs-optimized]
[--agent-version <value>]
[--tenancy <value>]
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

The stack ID.

`--layer-ids` (list)

An array that contains the instanceâs layer IDs.

(string)

Syntax:

```
"string" "string" ...
```

`--instance-type` (string)

The instance type, such as `t2.micro` . For a list of supported instance types, open the stack in the console, choose **Instances** , and choose **+ Instance** . The **Size** list contains the currently supported types. For more information, see [Instance Families and Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) . The parameter values that you use to specify the various types are in the **API Name** column of the **Available Instance Types** table.

`--auto-scaling-type` (string)

For load-based or time-based instances, the type. Windows stacks can use only time-based instances.

Possible values:

- `load`
- `timer`

`--hostname` (string)

The instance host name. The following are character limits for instance host names.

- Linux-based instances: 63 characters
- Windows-based instances: 15 characters

`--os` (string)

The instanceâs operating system, which must be set to one of the following.

- A supported Linux operating system: An Amazon Linux version, such as `Amazon Linux 2` , `Amazon Linux 2018.03` , `Amazon Linux 2017.09` , `Amazon Linux 2017.03` , `Amazon Linux 2016.09` , `Amazon Linux 2016.03` , `Amazon Linux 2015.09` , or `Amazon Linux 2015.03` .
- A supported Ubuntu operating system, such as `Ubuntu 18.04 LTS` , `Ubuntu 16.04 LTS` , `Ubuntu 14.04 LTS` , or `Ubuntu 12.04 LTS` .
- `CentOS Linux 7`
- `Red Hat Enterprise Linux 7`
- A supported Windows operating system, such as `Microsoft Windows Server 2012 R2 Base` , `Microsoft Windows Server 2012 R2 with SQL Server Express` , `Microsoft Windows Server 2012 R2 with SQL Server Standard` , or `Microsoft Windows Server 2012 R2 with SQL Server Web` .
- A custom AMI: `Custom` .

Not all operating systems are supported with all versions of Chef. For more information about the supported operating systems, see [OpsWorks Stacks Operating Systems](https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-os.html) .

The default option is the current Amazon Linux version. If you set this parameter to `Custom` , you must use the  CreateInstance actionâs AmiId parameter to specify the custom AMI that you want to use. Block device mappings are not supported if the value is `Custom` . For more information about how to use custom AMIs with OpsWorks Stacks, see [Using Custom AMIs](https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html) .

`--ami-id` (string)

A custom AMI ID to be used to create the instance. The AMI should be based on one of the supported operating systems. For more information, see [Using Custom AMIs](https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html) .

### Note

If you specify a custom AMI, you must set `Os` to `Custom` .

`--ssh-key-name` (string)

The instanceâs Amazon EC2 key-pair name.

`--availability-zone` (string)

The instance Availability Zone. For more information, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) .

`--virtualization-type` (string)

The instanceâs virtualization type, `paravirtual` or `hvm` .

`--subnet-id` (string)

The ID of the instanceâs subnet. If the stack is running in a VPC, you can use this parameter to override the stackâs default subnet ID value and direct OpsWorks Stacks to launch the instance in a different subnet.

`--architecture` (string)

The instance architecture. The default option is `x86_64` . Instance types do not necessarily support both architectures. For a list of the architectures that are supported by the different instance types, see [Instance Families and Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) .

Possible values:

- `x86_64`
- `i386`

`--root-device-type` (string)

The instance root device type. For more information, see [Storage for the Root Device](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device) .

Possible values:

- `ebs`
- `instance-store`

`--block-device-mappings` (list)

An array of `BlockDeviceMapping` objects that specify the instanceâs block devices. For more information, see [Block Device Mapping](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html) . Note that block device mappings are not supported for custom AMIs.

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

Shorthand Syntax:

```
DeviceName=string,NoDevice=string,VirtualName=string,Ebs={SnapshotId=string,Iops=integer,VolumeSize=integer,VolumeType=string,DeleteOnTermination=boolean} ...
```

JSON Syntax:

```
[
  {
    "DeviceName": "string",
    "NoDevice": "string",
    "VirtualName": "string",
    "Ebs": {
      "SnapshotId": "string",
      "Iops": integer,
      "VolumeSize": integer,
      "VolumeType": "gp2"|"io1"|"standard",
      "DeleteOnTermination": true|false
    }
  }
  ...
]
```

`--install-updates-on-boot` | `--no-install-updates-on-boot` (boolean)

Whether to install operating system and package updates when the instance boots. The default value is `true` . To control when updates are installed, set this value to `false` . You must then update your instances manually by using  CreateDeployment to run the `update_dependencies` stack command or by manually running `yum` (Amazon Linux) or `apt-get` (Ubuntu) on the instances.

### Note

We strongly recommend using the default value of `true` to ensure that your instances have the latest security updates.

`--ebs-optimized` | `--no-ebs-optimized` (boolean)

Whether to create an Amazon EBS-optimized instance.

`--agent-version` (string)

The default OpsWorks Stacks agent version. You have the following options:

- `INHERIT` - Use the stackâs default agent version setting.
- *version_number* - Use the specified agent version. This value overrides the stackâs default setting. To update the agent version, edit the instance configuration and specify a new version. OpsWorks Stacks installs that version on the instance.

The default setting is `INHERIT` . To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call  DescribeAgentVersions . AgentVersion cannot be set to Chef 12.2.

`--tenancy` (string)

The instanceâs tenancy option. The default option is no tenancy, or if the instance is running in a VPC, inherit tenancy settings from the VPC. The following are valid values for this parameter: `dedicated` , `default` , or `host` . Because there are costs associated with changes in tenancy options, we recommend that you research tenancy options before choosing them for your instances. For more information about dedicated hosts, see [Dedicated Hosts Overview](http://aws.amazon.com/ec2/dedicated-hosts/) and [Amazon EC2 Dedicated Hosts](http://aws.amazon.com/ec2/dedicated-hosts/) . For more information about dedicated instances, see [Dedicated Instances](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/dedicated-instance.html) and [Amazon EC2 Dedicated Instances](http://aws.amazon.com/ec2/purchasing-options/dedicated-instances/) .

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

**To create an instance**

The following `create-instance` command creates an m1.large Amazon Linux instance named myinstance1 in a specified stack.
The instance is assigned to one layer.

```
aws opsworks --region us-east-1 create-instance --stack-id 935450cc-61e0-4b03-a3e0-160ac817d2bb --layer-ids 5c8c272a-f2d5-42e3-8245-5bf3927cb65b --hostname myinstance1 --instance-type m1.large --os "Amazon Linux"
```

To use an autogenerated name, call [get-hostname-suggestion](http://docs.aws.amazon.com/cli/latest/reference/opsworks/get-hostname-suggestion.html), which generates
a hostname based on the theme that you specified when you created the stack.
Then pass that name to the hostname argument.

*Output*:

```
{
  "InstanceId": "5f9adeaa-c94c-42c6-aeef-28a5376002cd"
}
```

**More Information**

For more information, see [Adding an Instance to a Layer](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-add.html) in the *AWS OpsWorks User Guide*.

## Output

InstanceId -> (string)

The instance ID.