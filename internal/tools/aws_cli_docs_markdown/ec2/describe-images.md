# describe-imagesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-images.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-images.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-images

## Description

Describes the specified images (AMIs, AKIs, and ARIs) available to you or all of the images available to you.

The images available to you include public images, private images that you own, and private images owned by other Amazon Web Services accounts for which you have explicit launch permissions.

Recently deregistered images appear in the returned results for a short interval and then return empty results. After all instances that reference a deregistered AMI are terminated, specifying the ID of the image will eventually return an error indicating that the AMI ID cannot be found.

When Allowed AMIs is set to `enabled` , only allowed images are returned in the results, with the `imageAllowed` field set to `true` for each image. In `audit-mode` , the `imageAllowed` field is set to `true` for images that meet the accountâs Allowed AMIs criteria, and `false` for images that donât meet the criteria. For more information, see  EnableAllowedImagesSettings .

The Amazon EC2 API follows an eventual consistency model. This means that the result of an API command you run that creates or modifies resources might not be immediately available to all subsequent commands you run. For guidance on how to manage eventual consistency, see [Eventual consistency in the Amazon EC2 API](https://docs.aws.amazon.com/ec2/latest/devguide/eventual-consistency.html) in the *Amazon EC2 Developer Guide* .

### Warning

We strongly recommend using only paginated requests. Unpaginated requests are susceptible to throttling and timeouts.

### Note

The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeImages)

`describe-images` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Images`

## Synopsis

```
describe-images
[--executable-users <value>]
[--image-ids <value>]
[--owners <value>]
[--include-deprecated | --no-include-deprecated]
[--include-disabled | --no-include-disabled]
[--dry-run | --no-dry-run]
[--filters <value>]
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

`--executable-users` (list)

Scopes the images by users with explicit launch permissions. Specify an Amazon Web Services account ID, `self` (the sender of the request), or `all` (public AMIs).

- If you specify an Amazon Web Services account ID that is not your own, only AMIs shared with that specific Amazon Web Services account ID are returned. However, AMIs that are shared with the accountâs organization or organizational unit (OU) are not returned.
- If you specify `self` or your own Amazon Web Services account ID, AMIs shared with your account are returned. In addition, AMIs that are shared with the organization or OU of which you are member are also returned.
- If you specify `all` , all public AMIs are returned.

(string)

Syntax:

```
"string" "string" ...
```

`--image-ids` (list)

The image IDs.

Default: Describes all images available to you.

(string)

Syntax:

```
"string" "string" ...
```

`--owners` (list)

Scopes the results to images with the specified owners. You can specify a combination of Amazon Web Services account IDs, `self` , `amazon` , `aws-backup-vault` , and `aws-marketplace` . If you omit this parameter, the results include all images for which you have launch permissions, regardless of ownership.

(string)

Syntax:

```
"string" "string" ...
```

`--include-deprecated` | `--no-include-deprecated` (boolean)

Specifies whether to include deprecated AMIs.

Default: No deprecated AMIs are included in the response.

### Note

If you are the AMI owner, all deprecated AMIs appear in the response regardless of what you specify for this parameter.

`--include-disabled` | `--no-include-disabled` (boolean)

Specifies whether to include disabled AMIs.

Default: No disabled AMIs are included in the response.

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--filters` (list)

The filters.

- `architecture` - The image architecture (`i386` | `x86_64` | `arm64` | `x86_64_mac` | `arm64_mac` ).
- `block-device-mapping.delete-on-termination` - A Boolean value that indicates whether the Amazon EBS volume is deleted on instance termination.
- `block-device-mapping.device-name` - The device name specified in the block device mapping (for example, `/dev/sdh` or `xvdh` ).
- `block-device-mapping.snapshot-id` - The ID of the snapshot used for the Amazon EBS volume.
- `block-device-mapping.volume-size` - The volume size of the Amazon EBS volume, in GiB.
- `block-device-mapping.volume-type` - The volume type of the Amazon EBS volume (`io1` | `io2` | `gp2` | `gp3` | `sc1` | `st1` | `standard` ).
- `block-device-mapping.encrypted` - A Boolean that indicates whether the Amazon EBS volume is encrypted.
- `creation-date` - The time when the image was created, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), for example, `2021-09-29T11:04:43.305Z` . You can use a wildcard (`*` ), for example, `2021-09-29T*` , which matches an entire day.
- `description` - The description of the image (provided during image creation).
- `ena-support` - A Boolean that indicates whether enhanced networking with ENA is enabled.
- `hypervisor` - The hypervisor type (`ovm` | `xen` ).
- `image-allowed` - A Boolean that indicates whether the image meets the criteria specified for Allowed AMIs.
- `image-id` - The ID of the image.
- `image-type` - The image type (`machine` | `kernel` | `ramdisk` ).
- `is-public` - A Boolean that indicates whether the image is public.
- `kernel-id` - The kernel ID.
- `manifest-location` - The location of the image manifest.
- `name` - The name of the AMI (provided during image creation).
- `owner-alias` - The owner alias (`amazon` | `aws-backup-vault` | `aws-marketplace` ). The valid aliases are defined in an Amazon-maintained list. This is not the Amazon Web Services account alias that can be set using the IAM console. We recommend that you use the **Owner** request parameter instead of this filter.
- `owner-id` - The Amazon Web Services account ID of the owner. We recommend that you use the **Owner** request parameter instead of this filter.
- `platform` - The platform. The only supported value is `windows` .
- `product-code` - The product code.
- `product-code.type` - The type of the product code (`marketplace` ).
- `ramdisk-id` - The RAM disk ID.
- `root-device-name` - The device name of the root device volume (for example, `/dev/sda1` ).
- `root-device-type` - The type of the root device volume (`ebs` | `instance-store` ).
- `source-image-id` - The ID of the source AMI from which the AMI was created.
- `source-image-region` - The Region of the source AMI.
- `source-instance-id` - The ID of the instance that the AMI was created from if the AMI was created using CreateImage. This filter is applicable only if the AMI was created using [CreateImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html) .
- `state` - The state of the image (`available` | `pending` | `failed` ).
- `state-reason-code` - The reason code for the state change.
- `state-reason-message` - The message for the state change.
- `sriov-net-support` - A value of `simple` indicates that enhanced networking with the Intel 82599 VF interface is enabled.
- `tag:<key>` - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA` , specify `tag:Owner` for the filter name and `TeamA` for the filter value.
- `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
- `virtualization-type` - The virtualization type (`paravirtual` | `hvm` ).

(structure)

A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.

If you specify multiple filters, the filters are joined with an `AND` , and the request returns only results that match all of the specified filters.

For more information, see [List and filter using the CLI and API](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI) in the *Amazon EC2 User Guide* .

Name -> (string)

The name of the filter. Filter names are case-sensitive.

Values -> (list)

The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an `OR` , and the request returns all results that match any of the specified values.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Values": ["string", ...]
  }
  ...
]
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

**Example 1: To describe an AMI**

The following `describe-images` example describes the specified AMI in the specified Region.

```
aws ec2 describe-images \
    --region us-east-1 \
    --image-ids ami-1234567890EXAMPLE
```

Output:

```
{
    "Images": [
        {
            "VirtualizationType": "hvm",
            "Description": "Provided by Red Hat, Inc.",
            "PlatformDetails": "Red Hat Enterprise Linux",
            "EnaSupport": true,
            "Hypervisor": "xen",
            "State": "available",
            "SriovNetSupport": "simple",
            "ImageId": "ami-1234567890EXAMPLE",
            "UsageOperation": "RunInstances:0010",
            "BlockDeviceMappings": [
                {
                    "DeviceName": "/dev/sda1",
                    "Ebs": {
                        "SnapshotId": "snap-111222333444aaabb",
                        "DeleteOnTermination": true,
                        "VolumeType": "gp2",
                        "VolumeSize": 10,
                        "Encrypted": false
                    }
                }
            ],
            "Architecture": "x86_64",
            "ImageLocation": "123456789012/RHEL-8.0.0_HVM-20190618-x86_64-1-Hourly2-GP2",
            "RootDeviceType": "ebs",
            "OwnerId": "123456789012",
            "RootDeviceName": "/dev/sda1",
            "CreationDate": "2019-05-10T13:17:12.000Z",
            "Public": true,
            "ImageType": "machine",
            "Name": "RHEL-8.0.0_HVM-20190618-x86_64-1-Hourly2-GP2"
        }
    ]
}
```

For more information, see [Amazon Machine Images (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) in the *Amazon EC2 User Guide*.

**Example 2: To describe AMIs based on filters**

The following `describe-images` example describes Windows AMIs provided by Amazon that are backed by Amazon EBS.

```
aws ec2 describe-images \
    --owners amazon \
    --filters "Name=platform,Values=windows" "Name=root-device-type,Values=ebs"
```

For an example of the output for `describe-images`, see Example 1.

For additional examples using filters, see [Listing and filtering your resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI) in the *Amazon EC2 User Guide*.

**Example 3: To describe AMIs based on tags**

The following `describe-images` example describes all AMIs that have the tag `Type=Custom`. The example uses the `--query` parameter to display only the AMI IDs.

```
aws ec2 describe-images \
    --filters "Name=tag:Type,Values=Custom" \
    --query 'Images[*].[ImageId]' \
    --output text
```

Output:

```
ami-1234567890EXAMPLE
ami-0abcdef1234567890
```

For additional examples using tag filters, see [Working with tags](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_CLI) in the *Amazon EC2 User Guide*.

## Output

NextToken -> (string)

The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.

Images -> (list)

Information about the images.

(structure)

Describes an image.

PlatformDetails -> (string)

The platform details associated with the billing code of the AMI. For more information, see [Understand AMI billing information](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-billing-info.html) in the *Amazon EC2 User Guide* .

UsageOperation -> (string)

The operation of the Amazon EC2 instance and the billing code that is associated with the AMI. `usageOperation` corresponds to the [lineitem/Operation](https://docs.aws.amazon.com/cur/latest/userguide/Lineitem-columns.html#Lineitem-details-O-Operation) column on your Amazon Web Services Cost and Usage Report and in the [Amazon Web Services Price List API](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html) . You can view these fields on the **Instances** or **AMIs** pages in the Amazon EC2 console, or in the responses that are returned by the [DescribeImages](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html) command in the Amazon EC2 API, or the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) command in the CLI.

BlockDeviceMappings -> (list)

Any block device mapping entries.

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

Description -> (string)

The description of the AMI that was provided during image creation.

EnaSupport -> (boolean)

Specifies whether enhanced networking with ENA is enabled.

Hypervisor -> (string)

The hypervisor type of the image. Only `xen` is supported. `ovm` is not supported.

ImageOwnerAlias -> (string)

The owner alias (`amazon` | `aws-backup-vault` | `aws-marketplace` ).

Name -> (string)

The name of the AMI that was provided during image creation.

RootDeviceName -> (string)

The device name of the root device volume (for example, `/dev/sda1` ).

RootDeviceType -> (string)

The type of root device used by the AMI. The AMI can use an Amazon EBS volume or an instance store volume.

SriovNetSupport -> (string)

Specifies whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.

StateReason -> (structure)

The reason for the state change.

Code -> (string)

The reason code for the state change.

Message -> (string)

The message for the state change.

- `Server.InsufficientInstanceCapacity` : There was insufficient capacity available to satisfy the launch request.
- `Server.InternalError` : An internal error caused the instance to terminate during launch.
- `Server.ScheduledStop` : The instance was stopped due to a scheduled retirement.
- `Server.SpotInstanceShutdown` : The instance was stopped because the number of Spot requests with a maximum price equal to or higher than the Spot price exceeded available capacity or because of an increase in the Spot price.
- `Server.SpotInstanceTermination` : The instance was terminated because the number of Spot requests with a maximum price equal to or higher than the Spot price exceeded available capacity or because of an increase in the Spot price.
- `Client.InstanceInitiatedShutdown` : The instance was shut down from the operating system of the instance.
- `Client.InstanceTerminated` : The instance was terminated or rebooted during AMI creation.
- `Client.InternalError` : A client error caused the instance to terminate during launch.
- `Client.InvalidSnapshot.NotFound` : The specified snapshot was not found.
- `Client.UserInitiatedHibernate` : Hibernation was initiated on the instance.
- `Client.UserInitiatedShutdown` : The instance was shut down using the Amazon EC2 API.
- `Client.VolumeLimitExceeded` : The limit on the number of EBS volumes or total storage was exceeded. Decrease usage or request an increase in your account limits.

Tags -> (list)

Any tags assigned to the image.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

VirtualizationType -> (string)

The type of virtualization of the AMI.

BootMode -> (string)

The boot mode of the image. For more information, see [Boot modes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html) in the *Amazon EC2 User Guide* .

TpmSupport -> (string)

If the image is configured for NitroTPM support, the value is `v2.0` . For more information, see [NitroTPM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html) in the *Amazon EC2 User Guide* .

DeprecationTime -> (string)

The date and time to deprecate the AMI, in UTC, in the following format: *YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z. If you specified a value for seconds, Amazon EC2 rounds the seconds to the nearest minute.

ImdsSupport -> (string)

If `v2.0` , it indicates that IMDSv2 is specified in the AMI. Instances launched from this AMI will have `HttpTokens` automatically set to `required` so that, by default, the instance requires that IMDSv2 is used when requesting instance metadata. In addition, `HttpPutResponseHopLimit` is set to `2` . For more information, see [Configure the AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration) in the *Amazon EC2 User Guide* .

SourceInstanceId -> (string)

The ID of the instance that the AMI was created from if the AMI was created using [CreateImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html) . This field only appears if the AMI was created using CreateImage.

DeregistrationProtection -> (string)

Indicates whether deregistration protection is enabled for the AMI.

LastLaunchedTime -> (string)

The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601) , when the AMI was last used to launch an EC2 instance. When the AMI is used to launch an instance, there is a 24-hour delay before that usage is reported.

### Note

`lastLaunchedTime` data is available starting April 2017.

ImageAllowed -> (boolean)

If `true` , the AMI satisfies the criteria for Allowed AMIs and can be discovered and used in the account. If `false` and Allowed AMIs is set to `enabled` , the AMI canât be discovered or used in the account. If `false` and Allowed AMIs is set to `audit-mode` , the AMI can be discovered and used in the account.

For more information, see [Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html) in *Amazon EC2 User Guide* .

SourceImageId -> (string)

The ID of the source AMI from which the AMI was created.

The ID only appears if the AMI was created using  CreateImage ,  CopyImage , or  CreateRestoreImageTask . The ID does not appear if the AMI was created using any other API. For some older AMIs, the ID might not be available. For more information, see [Identify the source AMI used to create a new AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify-source-ami-used-to-create-new-ami.html) in the *Amazon EC2 User Guide* .

SourceImageRegion -> (string)

The Region of the source AMI.

The Region only appears if the AMI was created using  CreateImage ,  CopyImage , or  CreateRestoreImageTask . The Region does not appear if the AMI was created using any other API. For some older AMIs, the Region might not be available. For more information, see [Identify the source AMI used to create a new AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify-source-ami-used-to-create-new-ami.html) in the *Amazon EC2 User Guide* .

ImageId -> (string)

The ID of the AMI.

ImageLocation -> (string)

The location of the AMI.

State -> (string)

The current state of the AMI. If the state is `available` , the image is successfully registered and can be used to launch an instance.

OwnerId -> (string)

The ID of the Amazon Web Services account that owns the image.

CreationDate -> (string)

The date and time the image was created.

Public -> (boolean)

Indicates whether the image has public launch permissions. The value is `true` if this image has public launch permissions or `false` if it has only implicit and explicit launch permissions.

ProductCodes -> (list)

Any product codes associated with the AMI.

(structure)

Describes a product code.

ProductCodeId -> (string)

The product code.

ProductCodeType -> (string)

The type of product code.

Architecture -> (string)

The architecture of the image.

ImageType -> (string)

The type of image.

KernelId -> (string)

The kernel associated with the image, if any. Only applicable for machine images.

RamdiskId -> (string)

The RAM disk associated with the image, if any. Only applicable for machine images.

Platform -> (string)

This value is set to `windows` for Windows AMIs; otherwise, it is blank.