# describe-stored-iscsi-volumesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-stored-iscsi-volumes.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-stored-iscsi-volumes.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [storagegateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/index.html#cli-aws-storagegateway) ]

# describe-stored-iscsi-volumes

## Description

Returns the description of the gateway volumes specified in the request. The list of gateway volumes in the request must be from one gateway. In the response, Storage Gateway returns volume information sorted by volume ARNs. This operation is only supported in stored volume gateway type.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeStorediSCSIVolumes)

## Synopsis

```
describe-stored-iscsi-volumes
--volume-arns <value>
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

`--volume-arns` (list)

An array of strings where each string represents the Amazon Resource Name (ARN) of a stored volume. All of the specified stored volumes must be from the same gateway. Use  ListVolumes to get volume ARNs for a gateway.

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

## Output

StorediSCSIVolumes -> (list)

Describes a single unit of output from  DescribeStorediSCSIVolumes . The following fields are returned:

- `ChapEnabled` : Indicates whether mutual CHAP is enabled for the iSCSI target.
- `LunNumber` : The logical disk number.
- `NetworkInterfaceId` : The network interface ID of the stored volume that initiator use to map the stored volume as an iSCSI target.
- `NetworkInterfacePort` : The port used to communicate with iSCSI targets.
- `PreservedExistingData` : Indicates when the stored volume was created, existing data on the underlying local disk was preserved.
- `SourceSnapshotId` : If the stored volume was created from a snapshot, this field contains the snapshot ID used, e.g. `snap-1122aabb` . Otherwise, this field is not included.
- `StorediSCSIVolumes` : An array of StorediSCSIVolume objects where each object contains metadata about one stored volume.
- `TargetARN` : The Amazon Resource Name (ARN) of the volume target.
- `VolumeARN` : The Amazon Resource Name (ARN) of the stored volume.
- `VolumeDiskId` : The disk ID of the local disk that was specified in the  CreateStorediSCSIVolume operation.
- `VolumeId` : The unique identifier of the storage volume, e.g. `vol-1122AABB` .
- `VolumeiSCSIAttributes` : An  VolumeiSCSIAttributes object that represents a collection of iSCSI attributes for one stored volume.
- `VolumeProgress` : Represents the percentage complete if the volume is restoring or bootstrapping that represents the percent of data transferred. This field does not appear in the response if the stored volume is not restoring or bootstrapping.
- `VolumeSizeInBytes` : The size of the volume in bytes.
- `VolumeStatus` : One of the `VolumeStatus` values that indicates the state of the volume.
- `VolumeType` : One of the enumeration values describing the type of the volume. Currently, only `STORED` volumes are supported.

(structure)

Describes an iSCSI stored volume.

VolumeARN -> (string)

The Amazon Resource Name (ARN) of the storage volume.

VolumeId -> (string)

The unique identifier of the volume, e.g., vol-AE4B946D.

VolumeType -> (string)

One of the VolumeType enumeration values describing the type of the volume.

VolumeStatus -> (string)

One of the VolumeStatus values that indicates the state of the storage volume.

VolumeAttachmentStatus -> (string)

A value that indicates whether a storage volume is attached to, detached from, or is in the process of detaching from a gateway. For more information, see [Moving your volumes to a different gateway](https://docs.aws.amazon.com/storagegateway/latest/userguide/managing-volumes.html#attach-detach-volume) .

VolumeSizeInBytes -> (long)

The size of the volume in bytes.

VolumeProgress -> (double)

Represents the percentage complete if the volume is restoring or bootstrapping that represents the percent of data transferred. This field does not appear in the response if the stored volume is not restoring or bootstrapping.

VolumeDiskId -> (string)

The ID of the local disk that was specified in the  CreateStorediSCSIVolume operation.

SourceSnapshotId -> (string)

If the stored volume was created from a snapshot, this field contains the snapshot ID used, e.g. snap-78e22663. Otherwise, this field is not included.

PreservedExistingData -> (boolean)

Indicates if when the stored volume was created, existing data on the underlying local disk was preserved.

Valid Values: `true` | `false`

VolumeiSCSIAttributes -> (structure)

An  VolumeiSCSIAttributes object that represents a collection of iSCSI attributes for one stored volume.

TargetARN -> (string)

The Amazon Resource Name (ARN) of the volume target.

NetworkInterfaceId -> (string)

The network interface identifier.

NetworkInterfacePort -> (integer)

The port used to communicate with iSCSI targets.

LunNumber -> (integer)

The logical disk number.

ChapEnabled -> (boolean)

Indicates whether mutual CHAP is enabled for the iSCSI target.

CreatedDate -> (timestamp)

The date the volume was created. Volumes created prior to March 28, 2017 donât have this timestamp.

VolumeUsedInBytes -> (long)

The size of the data stored on the volume in bytes. This value is calculated based on the number of blocks that are touched, instead of the actual amount of data written. This value can be useful for sequential write patterns but less accurate for random write patterns. `VolumeUsedInBytes` is different from the compressed size of the volume, which is the value that is used to calculate your bill.

### Note

This value is not available for volumes created prior to May 13, 2015, until you store data on the volume.

KMSKey -> (string)

Optional. The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value must be set if `KMSEncrypted` is `true` , or if `EncryptionType` is `SseKms` or `DsseKms` .

TargetName -> (string)

The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN. For example, specifying `TargetName` as *myvolume* results in the target ARN of `arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume` . The target name must be unique across all volumes on a gateway.

If you donât specify a value, Storage Gateway uses the value that was previously used for this volume as the new target name.