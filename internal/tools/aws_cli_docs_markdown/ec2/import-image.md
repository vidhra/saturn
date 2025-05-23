# import-imageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-image.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-image.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# import-image

## Description

### Note

To import your virtual machines (VMs) with a console-based experience, you can use the *Import virtual machine images to Amazon Web Services* template in the [Migration Hub Orchestrator console](https://console.aws.amazon.com/migrationhub/orchestrator) . For more information, see the ` *Migration Hub Orchestrator User Guide* [https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/import-vm-images](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/import-vm-images).html`__ .

Import single or multi-volume disk images or EBS snapshots into an Amazon Machine Image (AMI).

### Warning

Amazon Web Services VM Import/Export strongly recommends specifying a value for either the `--license-type` or `--usage-operation` parameter when you create a new VM Import task. This ensures your operating system is licensed appropriately and your billing is optimized.

For more information, see [Importing a VM as an image using VM Import/Export](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html) in the *VM Import/Export User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ImportImage)

## Synopsis

```
import-image
[--architecture <value>]
[--client-data <value>]
[--client-token <value>]
[--description <value>]
[--disk-containers <value>]
[--dry-run | --no-dry-run]
[--encrypted | --no-encrypted]
[--hypervisor <value>]
[--kms-key-id <value>]
[--license-type <value>]
[--platform <value>]
[--role-name <value>]
[--license-specifications <value>]
[--tag-specifications <value>]
[--usage-operation <value>]
[--boot-mode <value>]
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

`--architecture` (string)

The architecture of the virtual machine.

Valid values: `i386` | `x86_64`

`--client-data` (structure)

The client-specific data.

Comment -> (string)

A user-defined comment about the disk upload.

UploadEnd -> (timestamp)

The time that the disk upload ends.

UploadSize -> (double)

The size of the uploaded disk image, in GiB.

UploadStart -> (timestamp)

The time that the disk upload starts.

Shorthand Syntax:

```
Comment=string,UploadEnd=timestamp,UploadSize=double,UploadStart=timestamp
```

JSON Syntax:

```
{
  "Comment": "string",
  "UploadEnd": timestamp,
  "UploadSize": double,
  "UploadStart": timestamp
}
```

`--client-token` (string)

The token to enable idempotency for VM import requests.

`--description` (string)

A description string for the import image task.

`--disk-containers` (list)

Information about the disk containers.

(structure)

Describes the disk container object for an import image task.

Description -> (string)

The description of the disk image.

DeviceName -> (string)

The block device mapping for the disk.

Format -> (string)

The format of the disk image being imported.

Valid values: `OVA` | `VHD` | `VHDX` | `VMDK` | `RAW`

SnapshotId -> (string)

The ID of the EBS snapshot to be used for importing the snapshot.

Url -> (string)

The URL to the Amazon S3-based disk image being imported. The URL can either be a https URL ([https://](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-image.html)..) or an Amazon S3 URL (s3://..)

UserBucket -> (structure)

The S3 bucket for the disk image.

S3Bucket -> (string)

The name of the Amazon S3 bucket where the disk image is located.

S3Key -> (string)

The file name of the disk image.

Shorthand Syntax:

```
Description=string,DeviceName=string,Format=string,SnapshotId=string,Url=string,UserBucket={S3Bucket=string,S3Key=string} ...
```

JSON Syntax:

```
[
  {
    "Description": "string",
    "DeviceName": "string",
    "Format": "string",
    "SnapshotId": "string",
    "Url": "string",
    "UserBucket": {
      "S3Bucket": "string",
      "S3Key": "string"
    }
  }
  ...
]
```

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--encrypted` | `--no-encrypted` (boolean)

Specifies whether the destination AMI of the imported image should be encrypted. The default KMS key for EBS is used unless you specify a non-default KMS key using `KmsKeyId` . For more information, see [Amazon EBS Encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html) in the *Amazon Elastic Compute Cloud User Guide* .

`--hypervisor` (string)

The target hypervisor platform.

Valid values: `xen`

`--kms-key-id` (string)

An identifier for the symmetric KMS key to use when creating the encrypted AMI. This parameter is only required if you want to use a non-default KMS key; if this parameter is not specified, the default KMS key for EBS is used. If a `KmsKeyId` is specified, the `Encrypted` flag must also be set.

The KMS key identifier may be provided in any of the following formats:

- Key ID
- Key alias
- ARN using key ID. The ID ARN contains the `arn:aws:kms` namespace, followed by the Region of the key, the Amazon Web Services account ID of the key owner, the `key` namespace, and then the key ID. For example, arn:aws:kms:*us-east-1* :*012345678910* :key/*abcd1234-a123-456a-a12b-a123b4cd56ef* .
- ARN using key alias. The alias ARN contains the `arn:aws:kms` namespace, followed by the Region of the key, the Amazon Web Services account ID of the key owner, the `alias` namespace, and then the key alias. For example, arn:aws:kms:*us-east-1* :*012345678910* :alias/*ExampleAlias* .

Amazon Web Services parses `KmsKeyId` asynchronously, meaning that the action you call may appear to complete even though you provided an invalid identifier. This action will eventually report failure.

The specified KMS key must exist in the Region that the AMI is being copied to.

Amazon EBS does not support asymmetric KMS keys.

`--license-type` (string)

The license type to be used for the Amazon Machine Image (AMI) after importing.

Specify `AWS` to replace the source-system license with an Amazon Web Services license or `BYOL` to retain the source-system license. Leaving this parameter undefined is the same as choosing `AWS` when importing a Windows Server operating system, and the same as choosing `BYOL` when importing a Windows client operating system (such as Windows 10) or a Linux operating system.

To use `BYOL` , you must have existing licenses with rights to use these licenses in a third party cloud, such as Amazon Web Services. For more information, see [Prerequisites](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html#prerequisites-image) in the VM Import/Export User Guide.

`--platform` (string)

The operating system of the virtual machine. If you import a VM that is compatible with Unified Extensible Firmware Interface (UEFI) using an EBS snapshot, you must specify a value for the platform.

Valid values: `Windows` | `Linux`

`--role-name` (string)

The name of the role to use when not using the default role, âvmimportâ.

`--license-specifications` (list)

The ARNs of the license configurations.

(structure)

The request information of license configurations.

LicenseConfigurationArn -> (string)

The ARN of a license configuration.

Shorthand Syntax:

```
LicenseConfigurationArn=string ...
```

JSON Syntax:

```
[
  {
    "LicenseConfigurationArn": "string"
  }
  ...
]
```

`--tag-specifications` (list)

The tags to apply to the import image task during creation.

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

Shorthand Syntax:

```
ResourceType=string,Tags=[{Key=string,Value=string},{Key=string,Value=string}] ...
```

JSON Syntax:

```
[
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
]
```

`--usage-operation` (string)

The usage operation value. For more information, see [Licensing options](https://docs.aws.amazon.com/vm-import/latest/userguide/vmie_prereqs.html#prerequisites) in the *VM Import/Export User Guide* .

`--boot-mode` (string)

The boot mode of the virtual machine.

### Note

The `uefi-preferred` boot mode isnât supported for importing images. For more information, see [Boot modes](https://docs.aws.amazon.com/vm-import/latest/userguide/prerequisites.html#vmimport-boot-modes) in the *VM Import/Export User Guide* .

Possible values:

- `legacy-bios`
- `uefi`
- `uefi-preferred`

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

**To import a VM image file as an AMI**

The following `import-image` example imports the specified OVA.

```
aws ec2 import-image \
  --disk-containers Format=ova,UserBucket="{S3Bucket=my-import-bucket,S3Key=vms/my-server-vm.ova}"
```

Output:

```
{
    "ImportTaskId": "import-ami-1234567890abcdef0",
    "Progress": "2",
    "SnapshotDetails": [
        {
            "DiskImageSize": 0.0,
            "Format": "ova",
            "UserBucket": {
                "S3Bucket": "my-import-bucket",
                "S3Key": "vms/my-server-vm.ova"
            }
        }
    ],
    "Status": "active",
    "StatusMessage": "pending"
}
```

## Output

Architecture -> (string)

The architecture of the virtual machine.

Description -> (string)

A description of the import task.

Encrypted -> (boolean)

Indicates whether the AMI is encrypted.

Hypervisor -> (string)

The target hypervisor of the import task.

ImageId -> (string)

The ID of the Amazon Machine Image (AMI) created by the import task.

ImportTaskId -> (string)

The task ID of the import image task.

KmsKeyId -> (string)

The identifier for the symmetric KMS key that was used to create the encrypted AMI.

LicenseType -> (string)

The license type of the virtual machine.

Platform -> (string)

The operating system of the virtual machine.

Progress -> (string)

The progress of the task.

SnapshotDetails -> (list)

Information about the snapshots.

(structure)

Describes the snapshot created from the imported disk.

Description -> (string)

A description for the snapshot.

DeviceName -> (string)

The block device mapping for the snapshot.

DiskImageSize -> (double)

The size of the disk in the snapshot, in GiB.

Format -> (string)

The format of the disk image from which the snapshot is created.

Progress -> (string)

The percentage of progress for the task.

SnapshotId -> (string)

The snapshot ID of the disk being imported.

Status -> (string)

A brief status of the snapshot creation.

StatusMessage -> (string)

A detailed status message for the snapshot creation.

Url -> (string)

The URL used to access the disk image.

UserBucket -> (structure)

The Amazon S3 bucket for the disk image.

S3Bucket -> (string)

The Amazon S3 bucket from which the disk image was created.

S3Key -> (string)

The file name of the disk image.

Status -> (string)

A brief status of the task.

StatusMessage -> (string)

A detailed status message of the import task.

LicenseSpecifications -> (list)

The ARNs of the license configurations.

(structure)

The response information for license configurations.

LicenseConfigurationArn -> (string)

The ARN of a license configuration.

Tags -> (list)

Any tags assigned to the import image task.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

UsageOperation -> (string)

The usage operation value.