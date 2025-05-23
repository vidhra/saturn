# describe-instance-attributeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-attribute.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-attribute.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-instance-attribute

## Description

Describes the specified attribute of the specified instance. You can specify only one attribute at a time.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstanceAttribute)

## Synopsis

```
describe-instance-attribute
[--dry-run | --no-dry-run]
--instance-id <value>
--attribute <value>
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

Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--instance-id` (string)

The ID of the instance.

`--attribute` (string)

The instance attribute.

Note that the `enaSupport` attribute is not supported.

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

**To describe the instance type**

This example describes the instance type of the specified instance.

Command:

```
aws ec2 describe-instance-attribute --instance-id i-1234567890abcdef0 --attribute instanceType
```

Output:

```
{
    "InstanceId": "i-1234567890abcdef0"
    "InstanceType": {
        "Value": "t1.micro"
    }
}
```

**To describe the disableApiTermination attribute**

This example describes the `disableApiTermination` attribute of the specified instance.

Command:

```
aws ec2 describe-instance-attribute --instance-id i-1234567890abcdef0 --attribute disableApiTermination
```

Output:

```
{
"InstanceId": "i-1234567890abcdef0"
    "DisableApiTermination": {
        "Value": "false"
    }
}
```

**To describe the block device mapping for an instance**

This example describes the `blockDeviceMapping` attribute of the specified instance.

Command:

```
aws ec2 describe-instance-attribute --instance-id i-1234567890abcdef0 --attribute blockDeviceMapping
```

Output:

```
{
    "InstanceId": "i-1234567890abcdef0"
    "BlockDeviceMappings": [
        {
            "DeviceName": "/dev/sda1",
            "Ebs": {
                "Status": "attached",
                "DeleteOnTermination": true,
                "VolumeId": "vol-049df61146c4d7901",
                "AttachTime": "2013-05-17T22:42:34.000Z"
            }
        },
        {
            "DeviceName": "/dev/sdf",
            "Ebs": {
                "Status": "attached",
                "DeleteOnTermination": false,
                "VolumeId": "vol-049df61146c4d7901",
                "AttachTime": "2013-09-10T23:07:00.000Z"
            }
        }
    ],
}
```

## Output

BlockDeviceMappings -> (list)

The block device mapping of the instance.

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

DisableApiTermination -> (structure)

Indicates whether termination protection is enabled. If the value is `true` , you canât terminate the instance using the Amazon EC2 console, command line tools, or API.

Value -> (boolean)

The attribute value. The valid values are `true` or `false` .

EnaSupport -> (structure)

Indicates whether enhanced networking with ENA is enabled.

Value -> (boolean)

The attribute value. The valid values are `true` or `false` .

EnclaveOptions -> (structure)

Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves.

Enabled -> (boolean)

If this parameter is set to `true` , the instance is enabled for Amazon Web Services Nitro Enclaves; otherwise, it is not enabled for Amazon Web Services Nitro Enclaves.

EbsOptimized -> (structure)

Indicates whether the instance is optimized for Amazon EBS I/O.

Value -> (boolean)

The attribute value. The valid values are `true` or `false` .

InstanceId -> (string)

The ID of the instance.

InstanceInitiatedShutdownBehavior -> (structure)

Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).

Value -> (string)

The attribute value. The value is case-sensitive.

InstanceType -> (structure)

The instance type.

Value -> (string)

The attribute value. The value is case-sensitive.

KernelId -> (structure)

The kernel ID.

Value -> (string)

The attribute value. The value is case-sensitive.

ProductCodes -> (list)

The product codes.

(structure)

Describes a product code.

ProductCodeId -> (string)

The product code.

ProductCodeType -> (string)

The type of product code.

RamdiskId -> (structure)

The RAM disk ID.

Value -> (string)

The attribute value. The value is case-sensitive.

RootDeviceName -> (structure)

The device name of the root device volume (for example, `/dev/sda1` ).

Value -> (string)

The attribute value. The value is case-sensitive.

SourceDestCheck -> (structure)

Indicates whether source/destination checks are enabled.

Value -> (boolean)

The attribute value. The valid values are `true` or `false` .

SriovNetSupport -> (structure)

Indicates whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.

Value -> (string)

The attribute value. The value is case-sensitive.

UserData -> (structure)

The user data.

Value -> (string)

The attribute value. The value is case-sensitive.

DisableApiStop -> (structure)

Indicates whether stop protection is enabled for the instance.

Value -> (boolean)

The attribute value. The valid values are `true` or `false` .

Groups -> (list)

The security groups associated with the instance.

(structure)

Describes a security group.

GroupId -> (string)

The ID of the security group.

GroupName -> (string)

The name of the security group.