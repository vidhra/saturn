# describe-image-attributeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-image-attribute.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-image-attribute.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-image-attribute

## Description

Describes the specified attribute of the specified AMI. You can specify only one attribute at a time.

### Note

The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeImageAttribute)

## Synopsis

```
describe-image-attribute
--attribute <value>
--image-id <value>
[--dry-run | --no-dry-run]
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

`--attribute` (string)

The AMI attribute.

**Note** : The `blockDeviceMapping` attribute is deprecated. Using this attribute returns the `Client.AuthFailure` error. To get information about the block device mappings for an AMI, use the  DescribeImages action.

Possible values:

- `description`
- `kernel`
- `ramdisk`
- `launchPermission`
- `productCodes`
- `blockDeviceMapping`
- `sriovNetSupport`
- `bootMode`
- `tpmSupport`
- `uefiData`
- `lastLaunchedTime`
- `imdsSupport`
- `deregistrationProtection`

`--image-id` (string)

The ID of the AMI.

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

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

**To describe the launch permissions for an AMI**

This example describes the launch permissions for the specified AMI.

Command:

```
aws ec2 describe-image-attribute --image-id ami-5731123e --attribute launchPermission
```

Output:

```
{
    "LaunchPermissions": [
        {
            "UserId": "123456789012"
        }
    ],
    "ImageId": "ami-5731123e",
}
```

**To describe the product codes for an AMI**

This example describes the product codes for the specified AMI. Note that this AMI has no product codes.

Command:

```
aws ec2 describe-image-attribute --image-id ami-5731123e --attribute productCodes
```

Output:

```
{
    "ProductCodes": [],
    "ImageId": "ami-5731123e",
}
```

## Output

Description -> (structure)

A description for the AMI.

Value -> (string)

The attribute value. The value is case-sensitive.

KernelId -> (structure)

The kernel ID.

Value -> (string)

The attribute value. The value is case-sensitive.

RamdiskId -> (structure)

The RAM disk ID.

Value -> (string)

The attribute value. The value is case-sensitive.

SriovNetSupport -> (structure)

Indicates whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.

Value -> (string)

The attribute value. The value is case-sensitive.

BootMode -> (structure)

The boot mode.

Value -> (string)

The attribute value. The value is case-sensitive.

TpmSupport -> (structure)

If the image is configured for NitroTPM support, the value is `v2.0` .

Value -> (string)

The attribute value. The value is case-sensitive.

UefiData -> (structure)

Base64 representation of the non-volatile UEFI variable store. To retrieve the UEFI data, use the [GetInstanceUefiData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceUefiData) command. You can inspect and modify the UEFI data by using the [python-uefivars tool](https://github.com/awslabs/python-uefivars) on GitHub. For more information, see [UEFI Secure Boot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/uefi-secure-boot.html) in the *Amazon EC2 User Guide* .

Value -> (string)

The attribute value. The value is case-sensitive.

LastLaunchedTime -> (structure)

The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601) , when the AMI was last used to launch an EC2 instance. When the AMI is used to launch an instance, there is a 24-hour delay before that usage is reported.

### Note

`lastLaunchedTime` data is available starting April 2017.

Value -> (string)

The attribute value. The value is case-sensitive.

ImdsSupport -> (structure)

If `v2.0` , it indicates that IMDSv2 is specified in the AMI. Instances launched from this AMI will have `HttpTokens` automatically set to `required` so that, by default, the instance requires that IMDSv2 is used when requesting instance metadata. In addition, `HttpPutResponseHopLimit` is set to `2` . For more information, see [Configure the AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration) in the *Amazon EC2 User Guide* .

Value -> (string)

The attribute value. The value is case-sensitive.

DeregistrationProtection -> (structure)

Indicates whether deregistration protection is enabled for the AMI.

Value -> (string)

The attribute value. The value is case-sensitive.

ImageId -> (string)

The ID of the AMI.

LaunchPermissions -> (list)

The launch permissions.

(structure)

Describes a launch permission.

OrganizationArn -> (string)

The Amazon Resource Name (ARN) of an organization.

OrganizationalUnitArn -> (string)

The Amazon Resource Name (ARN) of an organizational unit (OU).

UserId -> (string)

The Amazon Web Services account ID.

Constraints: Up to 10 000 account IDs can be specified in a single request.

Group -> (string)

The name of the group.

ProductCodes -> (list)

The product codes.

(structure)

Describes a product code.

ProductCodeId -> (string)

The product code.

ProductCodeType -> (string)

The type of product code.

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