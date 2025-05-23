# modify-instance-attributeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-attribute.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-attribute.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# modify-instance-attribute

## Description

Modifies the specified attribute of the specified instance. You can specify only one attribute at a time.

**Note:** Using this action to change the security groups associated with an elastic network interface (ENI) attached to an instance can result in an error if the instance has more than one ENI. To change the security groups associated with an ENI attached to an instance that has multiple ENIs, we recommend that you use the  ModifyNetworkInterfaceAttribute action.

To modify some attributes, the instance must be stopped. For more information, see [Modify a stopped instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_ChangingAttributesWhileInstanceStopped.html) in the *Amazon EC2 User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyInstanceAttribute)

## Synopsis

```
modify-instance-attribute
[--source-dest-check | --no-source-dest-check]
[--disable-api-stop | --no-disable-api-stop]
[--dry-run | --no-dry-run]
--instance-id <value>
[--attribute <value>]
[--value <value>]
[--block-device-mappings <value>]
[--disable-api-termination | --no-disable-api-termination]
[--instance-type <value>]
[--kernel <value>]
[--ramdisk <value>]
[--user-data <value>]
[--instance-initiated-shutdown-behavior <value>]
[--groups <value>]
[--ebs-optimized | --no-ebs-optimized]
[--sriov-net-support <value>]
[--ena-support | --no-ena-support]
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

`--source-dest-check` | `--no-source-dest-check` (structure)

Enable or disable source/destination checks, which ensure that the instance is either the source or the destination of any traffic that it receives. If the value is `true` , source/destination checks are enabled; otherwise, they are disabled. The default value is `true` . You must disable source/destination checks if the instance runs services such as network address translation, routing, or firewalls.

Value -> (boolean)

The attribute value. The valid values are `true` or `false` .

`--disable-api-stop` | `--no-disable-api-stop` (structure)

Indicates whether an instance is enabled for stop protection. For more information, see [Enable stop protection for your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-stop-protection.html) .

Value -> (boolean)

The attribute value. The valid values are `true` or `false` .

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--instance-id` (string)

The ID of the instance.

`--attribute` (string)

The name of the attribute to modify.

### Note

When changing the instance type: If the original instance type is configured for configurable bandwidth, and the desired instance type doesnât support configurable bandwidth, first set the existing bandwidth configuration to `default` using the  ModifyInstanceNetworkPerformanceOptions operation.

### Warning

You can modify the following attributes only: `disableApiTermination` | `instanceType` | `kernel` | `ramdisk` | `instanceInitiatedShutdownBehavior` | `blockDeviceMapping` | `userData` | `sourceDestCheck` | `groupSet` | `ebsOptimized` | `sriovNetSupport` | `enaSupport` | `nvmeSupport` | `disableApiStop` | `enclaveOptions`

Possible values:

- `instanceType`
- `kernel`
- `ramdisk`
- `userData`
- `disableApiTermination`
- `instanceInitiatedShutdownBehavior`
- `rootDeviceName`
- `blockDeviceMapping`
- `productCodes`
- `sourceDestCheck`
- `groupSet`
- `ebsOptimized`
- `sriovNetSupport`
- `enaSupport`
- `enclaveOptions`
- `disableApiStop`

`--value` (string)

A new value for the attribute. Use only with the `kernel` , `ramdisk` , `userData` , `disableApiTermination` , or `instanceInitiatedShutdownBehavior` attribute.

`--block-device-mappings` (list)

Modifies the `DeleteOnTermination` attribute for volumes that are currently attached. The volume must be owned by the caller. If no value is specified for `DeleteOnTermination` , the default is `true` and the volume is deleted when the instance is terminated. You canât modify the `DeleteOnTermination` attribute for volumes that are attached to Fargate tasks.

To add instance store volumes to an Amazon EBS-backed instance, you must add them when you launch the instance. For more information, see [Update the block device mapping when launching an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html#Using_OverridingAMIBDM) in the *Amazon EC2 User Guide* .

(structure)

Describes a block device mapping entry.

DeviceName -> (string)

The device name (for example, `/dev/sdh` or `xvdh` ).

Ebs -> (structure)

Parameters used to automatically set up EBS volumes when the instance is launched.

VolumeId -> (string)

The ID of the EBS volume.

DeleteOnTermination -> (boolean)

Indicates whether the volume is deleted on instance termination.

VirtualName -> (string)

The virtual device name.

NoDevice -> (string)

Suppresses the specified device included in the block device mapping.

Shorthand Syntax:

```
DeviceName=string,Ebs={VolumeId=string,DeleteOnTermination=boolean},VirtualName=string,NoDevice=string ...
```

JSON Syntax:

```
[
  {
    "DeviceName": "string",
    "Ebs": {
      "VolumeId": "string",
      "DeleteOnTermination": true|false
    },
    "VirtualName": "string",
    "NoDevice": "string"
  }
  ...
]
```

`--disable-api-termination` | `--no-disable-api-termination` (structure)

Enable or disable termination protection for the instance. If the value is `true` , you canât terminate the instance using the Amazon EC2 console, command line interface, or API. You canât enable termination protection for Spot Instances.

Value -> (boolean)

The attribute value. The valid values are `true` or `false` .

`--instance-type` (structure)

Changes the instance type to the specified value. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide* . If the instance type is not valid, the error returned is `InvalidInstanceAttributeValue` .

Value -> (string)

The attribute value. The value is case-sensitive.

`--kernel` (structure)

Changes the instanceâs kernel to the specified value. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see [PV-GRUB](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedKernels.html) .

Value -> (string)

The attribute value. The value is case-sensitive.

`--ramdisk` (structure)

Changes the instanceâs RAM disk to the specified value. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see [PV-GRUB](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedKernels.html) .

Value -> (string)

The attribute value. The value is case-sensitive.

`--user-data` (structure)

Changes the instanceâs user data to the specified value. User data must be base64-encoded. Depending on the tool or SDK that youâre using, the base64-encoding might be performed for you. For more information, see [Work with instance user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-add-user-data.html) .

Value -> (blob)

Shorthand Syntax:

```
Value=blob
```

JSON Syntax:

```
{
  "Value": blob
}
```

`--instance-initiated-shutdown-behavior` (structure)

Specifies whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).

Value -> (string)

The attribute value. The value is case-sensitive.

`--groups` (list)

Replaces the security groups of the instance with the specified security groups. You must specify the ID of at least one security group, even if itâs just the default security group for the VPC.

(string)

Syntax:

```
"string" "string" ...
```

`--ebs-optimized` | `--no-ebs-optimized` (structure)

Specifies whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isnât available with all instance types. Additional usage charges apply when using an EBS Optimized instance.

Value -> (boolean)

The attribute value. The valid values are `true` or `false` .

`--sriov-net-support` (structure)

Set to `simple` to enable enhanced networking with the Intel 82599 Virtual Function interface for the instance.

There is no way to disable enhanced networking with the Intel 82599 Virtual Function interface at this time.

This option is supported only for HVM instances. Specifying this option with a PV instance can make it unreachable.

Value -> (string)

The attribute value. The value is case-sensitive.

`--ena-support` | `--no-ena-support` (structure)

Set to `true` to enable enhanced networking with ENA for the instance.

This option is supported only for HVM instances. Specifying this option with a PV instance can make it unreachable.

Value -> (boolean)

The attribute value. The valid values are `true` or `false` .

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

**Example 1: To modify the instance type**

The following `modify-instance-attribute` example modifies the instance type of the specified instance. The instance must be in the `stopped` state.

```
aws ec2 modify-instance-attribute \
    --instance-id i-1234567890abcdef0 \
    --instance-type "{\"Value\": \"m1.small\"}"
```

This command produces no output.

**Example 2: To enable enhanced networking on an instance**

The following `modify-instance-attribute` example enables enhanced networking for the specified instance. The instance must be in the `stopped` state.

```
aws ec2 modify-instance-attribute \
    --instance-id i-1234567890abcdef0 \
    --sriov-net-support simple
```

This command produces no output.

**Example 3: To modify the sourceDestCheck attribute**

The following `modify-instance-attribute` example sets the `sourceDestCheck` attribute of the specified instance to `true`. The instance must be in a VPC.

```
aws ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --source-dest-check "{\"Value\": true}"
```

This command produces no output.

**Example 4: To modify the deleteOnTermination attribute of the root volume**

The following `modify-instance-attribute` example sets the `deleteOnTermination` attribute for the root volume of the specified Amazon EBS-backed instance to `false`. By default, this attribute is `true` for the root volume.

Command:

```
aws ec2 modify-instance-attribute \
  --instance-id i-1234567890abcdef0 \
  --block-device-mappings "[{\"DeviceName\": \"/dev/sda1\",\"Ebs\":{\"DeleteOnTermination\":false}}]"
```

This command produces no output.

**Example 5: To modify the user data attached to an instance**

The following `modify-instance-attribute` example adds the contents of the file `UserData.txt` as the UserData for the specified instance.

Contents of original file `UserData.txt`:

```
#!/bin/bash
yum update -y
service httpd start
chkconfig httpd on
```

The contents of the file must be base64 encoded. The first command converts the text file to base64 and saves it as a new file.

Linux/macOS version of the command:

```
base64 UserData.txt > UserData.base64.txt
```

This command produces no output.

Windows version of the command:

```
certutil -encode UserData.txt tmp.b64 && findstr /v /c:- tmp.b64 > UserData.base64.txt
```

Output:

```
Input Length = 67
Output Length = 152
CertUtil: -encode command completed successfully.
```

Now you can reference that file in the CLI command that follows:

```
aws ec2 modify-instance-attribute \
    --instance-id=i-09b5a14dbca622e76 \
    --attribute userData --value fileb://UserData.base64.txt
```

This command produces no output.

For more information, see [User Data and the AWS CLI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html#user-data-api-cli) in the *EC2 User Guide*.

## Output

None