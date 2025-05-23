# create-volume-from-backupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/create-volume-from-backup.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/create-volume-from-backup.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [fsx](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/index.html#cli-aws-fsx) ]

# create-volume-from-backup

## Description

Creates a new Amazon FSx for NetApp ONTAP volume from an existing Amazon FSx volume backup.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/CreateVolumeFromBackup)

## Synopsis

```
create-volume-from-backup
--backup-id <value>
[--client-request-token <value>]
--name <value>
[--ontap-configuration <value>]
[--tags <value>]
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

`--backup-id` (string)

The ID of the source backup. Specifies the backup that you are copying.

`--client-request-token` (string)

(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK.

`--name` (string)

The name of the new volume youâre creating.

`--ontap-configuration` (structure)

Specifies the configuration of the ONTAP volume that you are creating.

JunctionPath -> (string)

Specifies the location in the SVMâs namespace where the volume is mounted. This parameter is required. The `JunctionPath` must have a leading forward slash, such as `/vol3` .

SecurityStyle -> (string)

Specifies the security style for the volume. If a volumeâs security style is not specified, it is automatically set to the root volumeâs security style. The security style determines the type of permissions that FSx for ONTAP uses to control data access. Specify one of the following values:

- `UNIX` if the file system is managed by a UNIX administrator, the majority of users are NFS clients, and an application accessing the data uses a UNIX user as the service account.
- `NTFS` if the file system is managed by a Windows administrator, the majority of users are SMB clients, and an application accessing the data uses a Windows user as the service account.
- `MIXED` This is an advanced setting. For more information, see the topic [What the security styles and their effects are](https://docs.netapp.com/us-en/ontap/nfs-admin/security-styles-their-effects-concept.html) in the NetApp Documentation Center.

For more information, see [Volume security style](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-volumes.html#volume-security-style) in the FSx for ONTAP User Guide.

SizeInMegabytes -> (integer)

Use `SizeInBytes` instead. Specifies the size of the volume, in megabytes (MB), that you are creating.

StorageEfficiencyEnabled -> (boolean)

Set to true to enable deduplication, compression, and compaction storage efficiency features on the volume, or set to false to disable them.

`StorageEfficiencyEnabled` is required when creating a `RW` volume (`OntapVolumeType` set to `RW` ).

StorageVirtualMachineId -> (string)

Specifies the ONTAP SVM in which to create the volume.

TieringPolicy -> (structure)

Describes the data tiering policy for an ONTAP volume. When enabled, Amazon FSx for ONTAPâs intelligent tiering automatically transitions a volumeâs data between the file systemâs primary storage and capacity pool storage based on your access patterns.

Valid tiering policies are the following:

- `SNAPSHOT_ONLY` - (Default value) moves cold snapshots to the capacity pool storage tier.
- `AUTO` - moves cold user data and snapshots to the capacity pool storage tier based on your access patterns.
- `ALL` - moves all user data blocks in both the active file system and Snapshot copies to the storage pool tier.
- `NONE` - keeps a volumeâs data in the primary storage tier, preventing it from being moved to the capacity pool tier.

CoolingPeriod -> (integer)

Specifies the number of days that user data in a volume must remain inactive before it is considered âcoldâ and moved to the capacity pool. Used with the `AUTO` and `SNAPSHOT_ONLY` tiering policies. Enter a whole number between 2 and 183. Default values are 31 days for `AUTO` and 2 days for `SNAPSHOT_ONLY` .

Name -> (string)

Specifies the tiering policy used to transition data. Default value is `SNAPSHOT_ONLY` .

- `SNAPSHOT_ONLY` - moves cold snapshots to the capacity pool storage tier.
- `AUTO` - moves cold user data and snapshots to the capacity pool storage tier based on your access patterns.
- `ALL` - moves all user data blocks in both the active file system and Snapshot copies to the storage pool tier.
- `NONE` - keeps a volumeâs data in the primary storage tier, preventing it from being moved to the capacity pool tier.

OntapVolumeType -> (string)

Specifies the type of volume you are creating. Valid values are the following:

- `RW` specifies a read/write volume. `RW` is the default.
- `DP` specifies a data-protection volume. A `DP` volume is read-only and can be used as the destination of a NetApp SnapMirror relationship.

For more information, see [Volume types](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-volumes.html#volume-types) in the Amazon FSx for NetApp ONTAP User Guide.

SnapshotPolicy -> (string)

Specifies the snapshot policy for the volume. There are three built-in snapshot policies:

- `default` : This is the default policy. A maximum of six hourly snapshots taken five minutes past the hour. A maximum of two daily snapshots taken Monday through Saturday at 10 minutes after midnight. A maximum of two weekly snapshots taken every Sunday at 15 minutes after midnight.
- `default-1weekly` : This policy is the same as the `default` policy except that it only retains one snapshot from the weekly schedule.
- `none` : This policy does not take any snapshots. This policy can be assigned to volumes to prevent automatic snapshots from being taken.

You can also provide the name of a custom policy that you created with the ONTAP CLI or REST API.

For more information, see [Snapshot policies](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snapshots-ontap.html#snapshot-policies) in the Amazon FSx for NetApp ONTAP User Guide.

CopyTagsToBackups -> (boolean)

A boolean flag indicating whether tags for the volume should be copied to backups. This value defaults to false. If itâs set to true, all tags for the volume are copied to all automatic and user-initiated backups where the user doesnât specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the volume, regardless of this value.

SnaplockConfiguration -> (structure)

Specifies the SnapLock configuration for an FSx for ONTAP volume.

AuditLogVolume -> (boolean)

Enables or disables the audit log volume for an FSx for ONTAP SnapLock volume. The default value is `false` . If you set `AuditLogVolume` to `true` , the SnapLock volume is created as an audit log volume. The minimum retention period for an audit log volume is six months.

For more information, see [SnapLock audit log volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/how-snaplock-works.html#snaplock-audit-log-volume) .

AutocommitPeriod -> (structure)

The configuration object for setting the autocommit period of files in an FSx for ONTAP SnapLock volume.

Type -> (string)

Defines the type of time for the autocommit period of a file in an FSx for ONTAP SnapLock volume. Setting this value to `NONE` disables autocommit. The default value is `NONE` .

Value -> (integer)

Defines the amount of time for the autocommit period of a file in an FSx for ONTAP SnapLock volume. The following ranges are valid:

- `Minutes` : 5 - 65,535
- `Hours` : 1 - 65,535
- `Days` : 1 - 3,650
- `Months` : 1 - 120
- `Years` : 1 - 10

PrivilegedDelete -> (string)

Enables, disables, or permanently disables privileged delete on an FSx for ONTAP SnapLock Enterprise volume. Enabling privileged delete allows SnapLock administrators to delete WORM files even if they have active retention periods. `PERMANENTLY_DISABLED` is a terminal state. If privileged delete is permanently disabled on a SnapLock volume, you canât re-enable it. The default value is `DISABLED` .

For more information, see [Privileged delete](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-enterprise.html#privileged-delete) .

RetentionPeriod -> (structure)

Specifies the retention period of an FSx for ONTAP SnapLock volume.

DefaultRetention -> (structure)

The retention period assigned to a write once, read many (WORM) file by default if an explicit retention period is not set for an FSx for ONTAP SnapLock volume. The default retention period must be greater than or equal to the minimum retention period and less than or equal to the maximum retention period.

Type -> (string)

Defines the type of time for the retention period of an FSx for ONTAP SnapLock volume. Set it to one of the valid types. If you set it to `INFINITE` , the files are retained forever. If you set it to `UNSPECIFIED` , the files are retained until you set an explicit retention period.

Value -> (integer)

Defines the amount of time for the retention period of an FSx for ONTAP SnapLock volume. You canât set a value for `INFINITE` or `UNSPECIFIED` . For all other options, the following ranges are valid:

- `Seconds` : 0 - 65,535
- `Minutes` : 0 - 65,535
- `Hours` : 0 - 24
- `Days` : 0 - 365
- `Months` : 0 - 12
- `Years` : 0 - 100

MinimumRetention -> (structure)

The shortest retention period that can be assigned to a WORM file on an FSx for ONTAP SnapLock volume.

Type -> (string)

Defines the type of time for the retention period of an FSx for ONTAP SnapLock volume. Set it to one of the valid types. If you set it to `INFINITE` , the files are retained forever. If you set it to `UNSPECIFIED` , the files are retained until you set an explicit retention period.

Value -> (integer)

Defines the amount of time for the retention period of an FSx for ONTAP SnapLock volume. You canât set a value for `INFINITE` or `UNSPECIFIED` . For all other options, the following ranges are valid:

- `Seconds` : 0 - 65,535
- `Minutes` : 0 - 65,535
- `Hours` : 0 - 24
- `Days` : 0 - 365
- `Months` : 0 - 12
- `Years` : 0 - 100

MaximumRetention -> (structure)

The longest retention period that can be assigned to a WORM file on an FSx for ONTAP SnapLock volume.

Type -> (string)

Defines the type of time for the retention period of an FSx for ONTAP SnapLock volume. Set it to one of the valid types. If you set it to `INFINITE` , the files are retained forever. If you set it to `UNSPECIFIED` , the files are retained until you set an explicit retention period.

Value -> (integer)

Defines the amount of time for the retention period of an FSx for ONTAP SnapLock volume. You canât set a value for `INFINITE` or `UNSPECIFIED` . For all other options, the following ranges are valid:

- `Seconds` : 0 - 65,535
- `Minutes` : 0 - 65,535
- `Hours` : 0 - 24
- `Days` : 0 - 365
- `Months` : 0 - 12
- `Years` : 0 - 100

SnaplockType -> (string)

Specifies the retention mode of an FSx for ONTAP SnapLock volume. After it is set, it canât be changed. You can choose one of the following retention modes:

- `COMPLIANCE` : Files transitioned to write once, read many (WORM) on a Compliance volume canât be deleted until their retention periods expire. This retention mode is used to address government or industry-specific mandates or to protect against ransomware attacks. For more information, see [SnapLock Compliance](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-compliance.html) .
- `ENTERPRISE` : Files transitioned to WORM on an Enterprise volume can be deleted by authorized users before their retention periods expire using privileged delete. This retention mode is used to advance an organizationâs data integrity and internal compliance or to test retention settings before using SnapLock Compliance. For more information, see [SnapLock Enterprise](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-enterprise.html) .

VolumeAppendModeEnabled -> (boolean)

Enables or disables volume-append mode on an FSx for ONTAP SnapLock volume. Volume-append mode allows you to create WORM-appendable files and write data to them incrementally. The default value is `false` .

For more information, see [Volume-append mode](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/worm-state.html#worm-state-append) .

VolumeStyle -> (string)

Use to specify the style of an ONTAP volume. FSx for ONTAP offers two styles of volumes that you can use for different purposes, FlexVol and FlexGroup volumes. For more information, see [Volume styles](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-volumes.html#volume-styles) in the Amazon FSx for NetApp ONTAP User Guide.

AggregateConfiguration -> (structure)

Use to specify configuration options for a volumeâs storage aggregate or aggregates.

Aggregates -> (list)

Used to specify the names of aggregates on which the volume will be created.

(string)

ConstituentsPerAggregate -> (integer)

Used to explicitly set the number of constituents within the FlexGroup per storage aggregate. This field is optional when creating a FlexGroup volume. If unspecified, the default value will be 8. This field cannot be provided when creating a FlexVol volume.

SizeInBytes -> (long)

Specifies the configured size of the volume, in bytes.

JSON Syntax:

```
{
  "JunctionPath": "string",
  "SecurityStyle": "UNIX"|"NTFS"|"MIXED",
  "SizeInMegabytes": integer,
  "StorageEfficiencyEnabled": true|false,
  "StorageVirtualMachineId": "string",
  "TieringPolicy": {
    "CoolingPeriod": integer,
    "Name": "SNAPSHOT_ONLY"|"AUTO"|"ALL"|"NONE"
  },
  "OntapVolumeType": "RW"|"DP",
  "SnapshotPolicy": "string",
  "CopyTagsToBackups": true|false,
  "SnaplockConfiguration": {
    "AuditLogVolume": true|false,
    "AutocommitPeriod": {
      "Type": "MINUTES"|"HOURS"|"DAYS"|"MONTHS"|"YEARS"|"NONE",
      "Value": integer
    },
    "PrivilegedDelete": "DISABLED"|"ENABLED"|"PERMANENTLY_DISABLED",
    "RetentionPeriod": {
      "DefaultRetention": {
        "Type": "SECONDS"|"MINUTES"|"HOURS"|"DAYS"|"MONTHS"|"YEARS"|"INFINITE"|"UNSPECIFIED",
        "Value": integer
      },
      "MinimumRetention": {
        "Type": "SECONDS"|"MINUTES"|"HOURS"|"DAYS"|"MONTHS"|"YEARS"|"INFINITE"|"UNSPECIFIED",
        "Value": integer
      },
      "MaximumRetention": {
        "Type": "SECONDS"|"MINUTES"|"HOURS"|"DAYS"|"MONTHS"|"YEARS"|"INFINITE"|"UNSPECIFIED",
        "Value": integer
      }
    },
    "SnaplockType": "COMPLIANCE"|"ENTERPRISE",
    "VolumeAppendModeEnabled": true|false
  },
  "VolumeStyle": "FLEXVOL"|"FLEXGROUP",
  "AggregateConfiguration": {
    "Aggregates": ["string", ...],
    "ConstituentsPerAggregate": integer
  },
  "SizeInBytes": long
}
```

`--tags` (list)

A list of `Tag` values, with a maximum of 50 elements.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
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

Volume -> (structure)

Returned after a successful `CreateVolumeFromBackup` API operation, describing the volume just created.

CreationTime -> (timestamp)

The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

FileSystemId -> (string)

The globally unique ID of the file system, assigned by Amazon FSx.

Lifecycle -> (string)

The lifecycle status of the volume.

- `AVAILABLE` - The volume is fully available for use.
- `CREATED` - The volume has been created.
- `CREATING` - Amazon FSx is creating the new volume.
- `DELETING` - Amazon FSx is deleting an existing volume.
- `FAILED` - Amazon FSx was unable to create the volume.
- `MISCONFIGURED` - The volume is in a failed but recoverable state.
- `PENDING` - Amazon FSx hasnât started creating the volume.

Name -> (string)

The name of the volume.

OntapConfiguration -> (structure)

The configuration of an Amazon FSx for NetApp ONTAP volume.

FlexCacheEndpointType -> (string)

Specifies the FlexCache endpoint type of the volume. Valid values are the following:

- `NONE` specifies that the volume doesnât have a FlexCache configuration. `NONE` is the default.
- `ORIGIN` specifies that the volume is the origin volume for a FlexCache volume.
- `CACHE` specifies that the volume is a FlexCache volume.

JunctionPath -> (string)

Specifies the directory that network-attached storage (NAS) clients use to mount the volume, along with the storage virtual machine (SVM) Domain Name System (DNS) name or IP address. You can create a `JunctionPath` directly below a parent volume junction or on a directory within a volume. A `JunctionPath` for a volume named `vol3` might be `/vol1/vol2/vol3` , or `/vol1/dir2/vol3` , or even `/dir1/dir2/vol3` .

SecurityStyle -> (string)

The security style for the volume, which can be `UNIX` , `NTFS` , or `MIXED` .

SizeInMegabytes -> (integer)

The configured size of the volume, in megabytes (MBs).

StorageEfficiencyEnabled -> (boolean)

The volumeâs storage efficiency setting.

StorageVirtualMachineId -> (string)

The ID of the volumeâs storage virtual machine.

StorageVirtualMachineRoot -> (boolean)

A Boolean flag indicating whether this volume is the root volume for its storage virtual machine (SVM). Only one volume on an SVM can be the root volume. This value defaults to `false` . If this value is `true` , then this is the SVM root volume.

This flag is useful when youâre deleting an SVM, because you must first delete all non-root volumes. This flag, when set to `false` , helps you identify which volumes to delete before you can delete the SVM.

TieringPolicy -> (structure)

The volumeâs `TieringPolicy` setting.

CoolingPeriod -> (integer)

Specifies the number of days that user data in a volume must remain inactive before it is considered âcoldâ and moved to the capacity pool. Used with the `AUTO` and `SNAPSHOT_ONLY` tiering policies. Enter a whole number between 2 and 183. Default values are 31 days for `AUTO` and 2 days for `SNAPSHOT_ONLY` .

Name -> (string)

Specifies the tiering policy used to transition data. Default value is `SNAPSHOT_ONLY` .

- `SNAPSHOT_ONLY` - moves cold snapshots to the capacity pool storage tier.
- `AUTO` - moves cold user data and snapshots to the capacity pool storage tier based on your access patterns.
- `ALL` - moves all user data blocks in both the active file system and Snapshot copies to the storage pool tier.
- `NONE` - keeps a volumeâs data in the primary storage tier, preventing it from being moved to the capacity pool tier.

UUID -> (string)

The volumeâs universally unique identifier (UUID).

OntapVolumeType -> (string)

Specifies the type of volume. Valid values are the following:

- `RW` specifies a read/write volume. `RW` is the default.
- `DP` specifies a data-protection volume. You can protect data by replicating it to data-protection mirror copies. If a disaster occurs, you can use these data-protection mirror copies to recover data.
- `LS` specifies a load-sharing mirror volume. A load-sharing mirror reduces the network traffic to a FlexVol volume by providing additional read-only access to clients.

SnapshotPolicy -> (string)

Specifies the snapshot policy for the volume. There are three built-in snapshot policies:

- `default` : This is the default policy. A maximum of six hourly snapshots taken five minutes past the hour. A maximum of two daily snapshots taken Monday through Saturday at 10 minutes after midnight. A maximum of two weekly snapshots taken every Sunday at 15 minutes after midnight.
- `default-1weekly` : This policy is the same as the `default` policy except that it only retains one snapshot from the weekly schedule.
- `none` : This policy does not take any snapshots. This policy can be assigned to volumes to prevent automatic snapshots from being taken.

You can also provide the name of a custom policy that you created with the ONTAP CLI or REST API.

For more information, see [Snapshot policies](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snapshots-ontap.html#snapshot-policies) in the Amazon FSx for NetApp ONTAP User Guide.

CopyTagsToBackups -> (boolean)

A boolean flag indicating whether tags for the volume should be copied to backups. This value defaults to false. If itâs set to true, all tags for the volume are copied to all automatic and user-initiated backups where the user doesnât specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the volume, regardless of this value.

SnaplockConfiguration -> (structure)

The SnapLock configuration object for an FSx for ONTAP SnapLock volume.

AuditLogVolume -> (boolean)

Enables or disables the audit log volume for an FSx for ONTAP SnapLock volume. The default value is `false` . If you set `AuditLogVolume` to `true` , the SnapLock volume is created as an audit log volume. The minimum retention period for an audit log volume is six months.

For more information, see [SnapLock audit log volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/how-snaplock-works.html#snaplock-audit-log-volume) .

AutocommitPeriod -> (structure)

The configuration object for setting the autocommit period of files in an FSx for ONTAP SnapLock volume.

Type -> (string)

Defines the type of time for the autocommit period of a file in an FSx for ONTAP SnapLock volume. Setting this value to `NONE` disables autocommit. The default value is `NONE` .

Value -> (integer)

Defines the amount of time for the autocommit period of a file in an FSx for ONTAP SnapLock volume. The following ranges are valid:

- `Minutes` : 5 - 65,535
- `Hours` : 1 - 65,535
- `Days` : 1 - 3,650
- `Months` : 1 - 120
- `Years` : 1 - 10

PrivilegedDelete -> (string)

Enables, disables, or permanently disables privileged delete on an FSx for ONTAP SnapLock Enterprise volume. Enabling privileged delete allows SnapLock administrators to delete write once, read many (WORM) files even if they have active retention periods. `PERMANENTLY_DISABLED` is a terminal state. If privileged delete is permanently disabled on a SnapLock volume, you canât re-enable it. The default value is `DISABLED` .

For more information, see [Privileged delete](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-enterprise.html#privileged-delete) .

RetentionPeriod -> (structure)

Specifies the retention period of an FSx for ONTAP SnapLock volume.

DefaultRetention -> (structure)

The retention period assigned to a write once, read many (WORM) file by default if an explicit retention period is not set for an FSx for ONTAP SnapLock volume. The default retention period must be greater than or equal to the minimum retention period and less than or equal to the maximum retention period.

Type -> (string)

Defines the type of time for the retention period of an FSx for ONTAP SnapLock volume. Set it to one of the valid types. If you set it to `INFINITE` , the files are retained forever. If you set it to `UNSPECIFIED` , the files are retained until you set an explicit retention period.

Value -> (integer)

Defines the amount of time for the retention period of an FSx for ONTAP SnapLock volume. You canât set a value for `INFINITE` or `UNSPECIFIED` . For all other options, the following ranges are valid:

- `Seconds` : 0 - 65,535
- `Minutes` : 0 - 65,535
- `Hours` : 0 - 24
- `Days` : 0 - 365
- `Months` : 0 - 12
- `Years` : 0 - 100

MinimumRetention -> (structure)

The shortest retention period that can be assigned to a WORM file on an FSx for ONTAP SnapLock volume.

Type -> (string)

Defines the type of time for the retention period of an FSx for ONTAP SnapLock volume. Set it to one of the valid types. If you set it to `INFINITE` , the files are retained forever. If you set it to `UNSPECIFIED` , the files are retained until you set an explicit retention period.

Value -> (integer)

Defines the amount of time for the retention period of an FSx for ONTAP SnapLock volume. You canât set a value for `INFINITE` or `UNSPECIFIED` . For all other options, the following ranges are valid:

- `Seconds` : 0 - 65,535
- `Minutes` : 0 - 65,535
- `Hours` : 0 - 24
- `Days` : 0 - 365
- `Months` : 0 - 12
- `Years` : 0 - 100

MaximumRetention -> (structure)

The longest retention period that can be assigned to a WORM file on an FSx for ONTAP SnapLock volume.

Type -> (string)

Defines the type of time for the retention period of an FSx for ONTAP SnapLock volume. Set it to one of the valid types. If you set it to `INFINITE` , the files are retained forever. If you set it to `UNSPECIFIED` , the files are retained until you set an explicit retention period.

Value -> (integer)

Defines the amount of time for the retention period of an FSx for ONTAP SnapLock volume. You canât set a value for `INFINITE` or `UNSPECIFIED` . For all other options, the following ranges are valid:

- `Seconds` : 0 - 65,535
- `Minutes` : 0 - 65,535
- `Hours` : 0 - 24
- `Days` : 0 - 365
- `Months` : 0 - 12
- `Years` : 0 - 100

SnaplockType -> (string)

Specifies the retention mode of an FSx for ONTAP SnapLock volume. After it is set, it canât be changed. You can choose one of the following retention modes:

- `COMPLIANCE` : Files transitioned to write once, read many (WORM) on a Compliance volume canât be deleted until their retention periods expire. This retention mode is used to address government or industry-specific mandates or to protect against ransomware attacks. For more information, see [SnapLock Compliance](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-compliance.html) .
- `ENTERPRISE` : Files transitioned to WORM on an Enterprise volume can be deleted by authorized users before their retention periods expire using privileged delete. This retention mode is used to advance an organizationâs data integrity and internal compliance or to test retention settings before using SnapLock Compliance. For more information, see [SnapLock Enterprise](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-enterprise.html) .

VolumeAppendModeEnabled -> (boolean)

Enables or disables volume-append mode on an FSx for ONTAP SnapLock volume. Volume-append mode allows you to create WORM-appendable files and write data to them incrementally. The default value is `false` .

For more information, see [Volume-append mode](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/worm-state.html#worm-state-append) .

VolumeStyle -> (string)

Use to specify the style of an ONTAP volume. For more information about FlexVols and FlexGroups, see [Volume types](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/volume-types.html) in Amazon FSx for NetApp ONTAP User Guide.

AggregateConfiguration -> (structure)

This structure specifies configuration options for a volumeâs storage aggregate or aggregates.

Aggregates -> (list)

The list of aggregates that this volume resides on. Aggregates are storage pools which make up your primary storage tier. Each high-availability (HA) pair has one aggregate. The names of the aggregates map to the names of the aggregates in the ONTAP CLI and REST API. For FlexVols, there will always be a single entry.

Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:

- The strings in the value of `Aggregates` are not are not formatted as `aggrX` , where X is a number between 1 and 12.
- The value of `Aggregates` contains aggregates that are not present.
- One or more of the aggregates supplied are too close to the volume limit to support adding more volumes.

(string)

TotalConstituents -> (integer)

The total number of constituents this FlexGroup volume has. Not applicable for FlexVols.

SizeInBytes -> (long)

The configured size of the volume, in bytes.

ResourceARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

Tags -> (list)

A list of `Tag` values, with a maximum of 50 elements.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

VolumeId -> (string)

The system-generated, unique ID of the volume.

VolumeType -> (string)

The type of the volume.

LifecycleTransitionReason -> (structure)

The reason why the volume lifecycle status changed.

Message -> (string)

A detailed error message.

AdministrativeActions -> (list)

A list of administrative actions for the volume that are in process or waiting to be processed. Administrative actions describe changes to the volume that you have initiated using the `UpdateVolume` action.

(structure)

Describes a specific Amazon FSx administrative action for the current Windows, Lustre, OpenZFS, or ONTAP file system or volume.

AdministrativeActionType -> (string)

Describes the type of administrative action, as follows:

- `FILE_SYSTEM_UPDATE` - A file system update administrative action initiated from the Amazon FSx console, API (`UpdateFileSystem` ), or CLI (`update-file-system` ).
- `THROUGHPUT_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file systemâs throughput capacity has been completed successfully, a `THROUGHPUT_OPTIMIZATION` task starts. You can track the storage-optimization progress using the `ProgressPercent` property. When `THROUGHPUT_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED` . For more information, see [Managing throughput capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-throughput-capacity.html) in the *Amazon FSx for Windows File Server User Guide* .
- `STORAGE_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file systemâs storage capacity has completed successfully, a `STORAGE_OPTIMIZATION` task starts.
- For Windows and ONTAP, storage optimization is the process of migrating the file system data to newer larger disks.
- For Lustre, storage optimization consists of rebalancing the data across the existing and newly added file servers.

You can track the storage-optimization progress using the `ProgressPercent` property. When `STORAGE_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED` . For more information, see [Managing storage capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-capacity.html) in the *Amazon FSx for Windows File Server User Guide* , [Managing storage capacity](https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-storage-capacity.html) in the *Amazon FSx for Lustre User Guide* , and [Managing storage capacity and provisioned IOPS](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-storage-capacity.html) in the *Amazon FSx for NetApp ONTAP User Guide* .

- `FILE_SYSTEM_ALIAS_ASSOCIATION` - A file system update to associate a new Domain Name System (DNS) alias with the file system. For more information, see [AssociateFileSystemAliases](https://docs.aws.amazon.com/fsx/latest/APIReference/API_AssociateFileSystemAliases.html) .
- `FILE_SYSTEM_ALIAS_DISASSOCIATION` - A file system update to disassociate a DNS alias from the file system. For more information, see [DisassociateFileSystemAliases](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DisassociateFileSystemAliases.html) .
- `IOPS_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file systemâs throughput capacity has been completed successfully, a `IOPS_OPTIMIZATION` task starts. You can track the storage-optimization progress using the `ProgressPercent` property. When `IOPS_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED` . For more information, see [Managing provisioned SSD IOPS](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-provisioned-ssd-iops.html) in the Amazon FSx for Windows File Server User Guide.
- `STORAGE_TYPE_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file systemâs throughput capacity has been completed successfully, a `STORAGE_TYPE_OPTIMIZATION` task starts. You can track the storage-optimization progress using the `ProgressPercent` property. When `STORAGE_TYPE_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED` .
- `VOLUME_UPDATE` - A volume update to an Amazon FSx for OpenZFS volume initiated from the Amazon FSx console, API (`UpdateVolume` ), or CLI (`update-volume` ).
- `VOLUME_RESTORE` - An Amazon FSx for OpenZFS volume is returned to the state saved by the specified snapshot, initiated from an API (`RestoreVolumeFromSnapshot` ) or CLI (`restore-volume-from-snapshot` ).
- `SNAPSHOT_UPDATE` - A snapshot update to an Amazon FSx for OpenZFS volume initiated from the Amazon FSx console, API (`UpdateSnapshot` ), or CLI (`update-snapshot` ).
- `RELEASE_NFS_V3_LOCKS` - Tracks the release of Network File System (NFS) V3 locks on an Amazon FSx for OpenZFS file system.
- `DOWNLOAD_DATA_FROM_BACKUP` - An FSx for ONTAP backup is being restored to a new volume on a second-generation file system. Once the all the file metadata is loaded onto the volume, you can mount the volume with read-only access. during this process.
- `VOLUME_INITIALIZE_WITH_SNAPSHOT` - A volume is being created from a snapshot on a different FSx for OpenZFS file system. You can initiate this from the Amazon FSx console, API (`CreateVolume` ), or CLI (`create-volume` ) when using the using the `FULL_COPY` strategy.
- `VOLUME_UPDATE_WITH_SNAPSHOT` - A volume is being updated from a snapshot on a different FSx for OpenZFS file system. You can initiate this from the Amazon FSx console, API (`CopySnapshotAndUpdateVolume` ), or CLI (`copy-snapshot-and-update-volume` ).

ProgressPercent -> (integer)

The percentage-complete status of a `STORAGE_OPTIMIZATION` or `DOWNLOAD_DATA_FROM_BACKUP` administrative action. Does not apply to any other administrative action type.

RequestTime -> (timestamp)

The time that the administrative action request was received.

Status -> (string)

The status of the administrative action, as follows:

- `FAILED` - Amazon FSx failed to process the administrative action successfully.
- `IN_PROGRESS` - Amazon FSx is processing the administrative action.
- `PENDING` - Amazon FSx is waiting to process the administrative action.
- `COMPLETED` - Amazon FSx has finished processing the administrative task. For a backup restore to a second-generation FSx for ONTAP file system, indicates that all data has been downloaded to the volume, and clients now have read-write access to volume.
- `UPDATED_OPTIMIZING` - For a storage-capacity increase update, Amazon FSx has updated the file system with the new storage capacity, and is now performing the storage-optimization process.
- `PENDING` - For a backup restore to a second-generation FSx for ONTAP file system, indicates that the file metadata is being downloaded onto the volume. The volumeâs Lifecycle state is CREATING.
- `IN_PROGRESS` - For a backup restore to a second-generation FSx for ONTAP file system, indicates that all metadata has been downloaded to the new volume and client can access data with read-only access while Amazon FSx downloads the file data to the volume. Track the progress of this process with the `ProgressPercent` element.

TargetFileSystemValues -> (structure)

The target value for the administration action, provided in the `UpdateFileSystem` operation. Returned for `FILE_SYSTEM_UPDATE` administrative actions.

OwnerId -> (string)

The Amazon Web Services account that created the file system. If the file system was created by a user in IAM Identity Center, the Amazon Web Services account to which the IAM user belongs is the owner.

CreationTime -> (timestamp)

The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

FileSystemId -> (string)

The system-generated, unique 17-digit ID of the file system.

FileSystemType -> (string)

The type of Amazon FSx file system, which can be `LUSTRE` , `WINDOWS` , `ONTAP` , or `OPENZFS` .

Lifecycle -> (string)

The lifecycle status of the file system. The following are the possible values and what they mean:

- `AVAILABLE` - The file system is in a healthy state, and is reachable and available for use.
- `CREATING` - Amazon FSx is creating the new file system.
- `DELETING` - Amazon FSx is deleting an existing file system.
- `FAILED` - An existing file system has experienced an unrecoverable failure. When creating a new file system, Amazon FSx was unable to create the file system.
- `MISCONFIGURED` - The file system is in a failed but recoverable state.
- `MISCONFIGURED_UNAVAILABLE` - (Amazon FSx for Windows File Server only) The file system is currently unavailable due to a change in your Active Directory configuration.
- `UPDATING` - The file system is undergoing a customer-initiated update.

FailureDetails -> (structure)

A structure providing details of any failures that occurred.

Message -> (string)

A message describing any failures that occurred.

StorageCapacity -> (integer)

The storage capacity of the file system in gibibytes (GiB).

Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `StorageCapacity` is outside of the minimum or maximum values.

StorageType -> (string)

The type of storage the file system is using. If set to `SSD` , the file system uses solid state drive storage. If set to `HDD` , the file system uses hard disk drive storage.

VpcId -> (string)

The ID of the primary virtual private cloud (VPC) for the file system.

SubnetIds -> (list)

Specifies the IDs of the subnets that the file system is accessible from. For the Amazon FSx Windows and ONTAP `MULTI_AZ_1` file system deployment type, there are two subnet IDs, one for the preferred file server and one for the standby file server. The preferred file server subnet identified in the `PreferredSubnetID` property. All other file systems have only one subnet ID.

For FSx for Lustre file systems, and Single-AZ Windows file systems, this is the ID of the subnet that contains the file systemâs endpoint. For `MULTI_AZ_1` Windows and ONTAP file systems, the file system endpoint is available in the `PreferredSubnetID` .

(string)

The ID for a subnet. A *subnet* is a range of IP addresses in your virtual private cloud (VPC). For more information, see [VPC and subnets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) in the *Amazon VPC User Guide.*

NetworkInterfaceIds -> (list)

The IDs of the elastic network interfaces from which a specific file system is accessible. The elastic network interface is automatically created in the same virtual private cloud (VPC) that the Amazon FSx file system was created in. For more information, see [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the *Amazon EC2 User Guide.*

For an Amazon FSx for Windows File Server file system, you can have one network interface ID. For an Amazon FSx for Lustre file system, you can have more than one.

(string)

An elastic network interface ID. An elastic network interface is a logical networking component in a virtual private cloud (VPC) that represents a virtual network card. For more information, see [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the *Amazon EC2 User Guide for Linux Instances* .

DNSName -> (string)

The Domain Name System (DNS) name for the file system.

KmsKeyId -> (string)

The ID of the Key Management Service (KMS) key used to encrypt Amazon FSx file system data. Used as follows with Amazon FSx file system types:

- Amazon FSx for Lustre `PERSISTENT_1` and `PERSISTENT_2` deployment types only.  `SCRATCH_1` and `SCRATCH_2` types are encrypted using the Amazon FSx service KMS key for your account.
- Amazon FSx for NetApp ONTAP
- Amazon FSx for OpenZFS
- Amazon FSx for Windows File Server

ResourceARN -> (string)

The Amazon Resource Name (ARN) of the file system resource.

Tags -> (list)

The tags to associate with the file system. For more information, see [Tagging your Amazon FSx resources](https://docs.aws.amazon.com/fsx/latest/LustreGuide/tag-resources.html) in the *Amazon FSx for Lustre User Guide* .

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

WindowsConfiguration -> (structure)

The configuration for this Amazon FSx for Windows File Server file system.

ActiveDirectoryId -> (string)

The ID for an existing Amazon Web Services Managed Microsoft Active Directory instance that the file system is joined to.

SelfManagedActiveDirectoryConfiguration -> (structure)

The configuration of the self-managed Microsoft Active Directory (AD) directory to which the Windows File Server or ONTAP storage virtual machine (SVM) instance is joined.

DomainName -> (string)

The fully qualified domain name of the self-managed AD directory.

OrganizationalUnitDistinguishedName -> (string)

The fully qualified distinguished name of the organizational unit within the self-managed AD directory to which the Windows File Server or ONTAP storage virtual machine (SVM) instance is joined.

FileSystemAdministratorsGroup -> (string)

The name of the domain group whose members have administrative privileges for the FSx file system.

UserName -> (string)

The user name for the service account on your self-managed AD domain that FSx uses to join to your AD domain.

DnsIps -> (list)

A list of up to three IP addresses of DNS servers or domain controllers in the self-managed AD directory.

(string)

DeploymentType -> (string)

Specifies the file system deployment type, valid values are the following:

- `MULTI_AZ_1` - Specifies a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability, and supports SSD and HDD storage.
- `SINGLE_AZ_1` - (Default) Specifies a file system that is configured for single AZ redundancy, only supports SSD storage.
- `SINGLE_AZ_2` - Latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports SSD and HDD storage.

For more information, see [Single-AZ and Multi-AZ File Systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html) .

RemoteAdministrationEndpoint -> (string)

For `MULTI_AZ_1` deployment types, use this endpoint when performing administrative tasks on the file system using Amazon FSx Remote PowerShell.

For `SINGLE_AZ_1` and `SINGLE_AZ_2` deployment types, this is the DNS name of the file system.

This endpoint is temporarily unavailable when the file system is undergoing maintenance.

PreferredSubnetId -> (string)

For `MULTI_AZ_1` deployment types, it specifies the ID of the subnet where the preferred file server is located. Must be one of the two subnet IDs specified in `SubnetIds` property. Amazon FSx serves traffic from this subnet except in the event of a failover to the secondary file server.

For `SINGLE_AZ_1` and `SINGLE_AZ_2` deployment types, this value is the same as that for `SubnetIDs` . For more information, see [Availability and durability: Single-AZ and Multi-AZ file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html#single-multi-az-resources) .

PreferredFileServerIp -> (string)

For `MULTI_AZ_1` deployment types, the IP address of the primary, or preferred, file server.

Use this IP address when mounting the file system on Linux SMB clients or Windows SMB clients that are not joined to a Microsoft Active Directory. Applicable for all Windows file system deployment types. This IP address is temporarily unavailable when the file system is undergoing maintenance. For Linux and Windows SMB clients that are joined to an Active Directory, use the file systemâs DNSName instead. For more information on mapping and mounting file shares, see [Accessing File Shares](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/accessing-file-shares.html) .

ThroughputCapacity -> (integer)

The throughput of the Amazon FSx file system, measured in megabytes per second.

MaintenanceOperationsInProgress -> (list)

The list of maintenance operations in progress for this file system.

(string)

An enumeration specifying the currently ongoing maintenance operation.

WeeklyMaintenanceStartTime -> (string)

The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone. d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.

DailyAutomaticBackupStartTime -> (string)

The preferred time to take daily automatic backups, in the UTC time zone.

AutomaticBackupRetentionDays -> (integer)

The number of days to retain automatic backups. Setting this to 0 disables automatic backups. You can retain automatic backups for a maximum of 90 days.

CopyTagsToBackups -> (boolean)

A boolean flag indicating whether tags on the file system should be copied to backups. This value defaults to false. If itâs set to true, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesnât specify any tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.

Aliases -> (list)

An array of one or more DNS aliases that are currently associated with the Amazon FSx file system. Aliases allow you to use existing DNS names to access the data in your Amazon FSx file system. You can associate up to 50 aliases with a file system at any time. You can associate additional DNS aliases after you create the file system using the AssociateFileSystemAliases operation. You can remove DNS aliases from the file system after it is created using the DisassociateFileSystemAliases operation. You only need to specify the alias name in the request payload. For more information, see [DNS aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html) .

(structure)

A DNS alias that is associated with the file system. You can use a DNS alias to access a file system using user-defined DNS names, in addition to the default DNS name that Amazon FSx assigns to the file system. For more information, see [DNS aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html) in the *FSx for Windows File Server User Guide* .

Name -> (string)

The name of the DNS alias. The alias name has to meet the following requirements:

- Formatted as a fully-qualified domain name (FQDN), `hostname.domain` , for example, `accounting.example.com` .
- Can contain alphanumeric characters, the underscore (_), and the hyphen (-).
- Cannot start or end with a hyphen.
- Can start with a numeric.

For DNS names, Amazon FSx stores alphabetic characters as lowercase letters (a-z), regardless of how you specify them: as uppercase letters, lowercase letters, or the corresponding letters in escape codes.

Lifecycle -> (string)

Describes the state of the DNS alias.

- AVAILABLE - The DNS alias is associated with an Amazon FSx file system.
- CREATING - Amazon FSx is creating the DNS alias and associating it with the file system.
- CREATE_FAILED - Amazon FSx was unable to associate the DNS alias with the file system.
- DELETING - Amazon FSx is disassociating the DNS alias from the file system and deleting it.
- DELETE_FAILED - Amazon FSx was unable to disassociate the DNS alias from the file system.

AuditLogConfiguration -> (structure)

The configuration that Amazon FSx for Windows File Server uses to audit and log user accesses of files, folders, and file shares on the Amazon FSx for Windows File Server file system.

FileAccessAuditLogLevel -> (string)

Sets which attempt type is logged by Amazon FSx for file and folder accesses.

- `SUCCESS_ONLY` - only successful attempts to access files or folders are logged.
- `FAILURE_ONLY` - only failed attempts to access files or folders are logged.
- `SUCCESS_AND_FAILURE` - both successful attempts and failed attempts to access files or folders are logged.
- `DISABLED` - access auditing of files and folders is turned off.

FileShareAccessAuditLogLevel -> (string)

Sets which attempt type is logged by Amazon FSx for file share accesses.

- `SUCCESS_ONLY` - only successful attempts to access file shares are logged.
- `FAILURE_ONLY` - only failed attempts to access file shares are logged.
- `SUCCESS_AND_FAILURE` - both successful attempts and failed attempts to access file shares are logged.
- `DISABLED` - access auditing of file shares is turned off.

AuditLogDestination -> (string)

The Amazon Resource Name (ARN) for the destination of the audit logs. The destination can be any Amazon CloudWatch Logs log group ARN or Amazon Kinesis Data Firehose delivery stream ARN.

The name of the Amazon CloudWatch Logs log group must begin with the `/aws/fsx` prefix. The name of the Amazon Kinesis Data Firehose delivery stream must begin with the `aws-fsx` prefix.

The destination ARN (either CloudWatch Logs log group or Kinesis Data Firehose delivery stream) must be in the same Amazon Web Services partition, Amazon Web Services Region, and Amazon Web Services account as your Amazon FSx file system.

DiskIopsConfiguration -> (structure)

The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for Windows file system. By default, Amazon FSx automatically provisions 3 IOPS per GiB of storage capacity. You can provision additional IOPS per GiB of storage, up to the maximum limit associated with your chosen throughput capacity.

Mode -> (string)

Specifies whether the file system is using the `AUTOMATIC` setting of SSD IOPS of 3 IOPS per GB of storage capacity, or if it using a `USER_PROVISIONED` value.

Iops -> (long)

The total number of SSD IOPS provisioned for the file system.

The minimum and maximum values for this property depend on the value of `HAPairs` and `StorageCapacity` . The minimum value is calculated as `StorageCapacity` * 3 * `HAPairs` (3 IOPS per GB of `StorageCapacity` ). The maximum value is calculated as 200,000 * `HAPairs` .

Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `Iops` is outside of the minimum or maximum values.

LustreConfiguration -> (structure)

The configuration for the Amazon FSx for Lustre file system.

WeeklyMaintenanceStartTime -> (string)

The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone. Here, `d` is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.

DataRepositoryConfiguration -> (structure)

The data repository configuration object for Lustre file systems returned in the response of the `CreateFileSystem` operation.

This data type is not supported on file systems with a data repository association. For file systems with a data repository association, see .

Lifecycle -> (string)

Describes the state of the file systemâs S3 durable data repository, if it is configured with an S3 repository. The lifecycle can have the following values:

- `CREATING` - The data repository configuration between the FSx file system and the linked S3 data repository is being created. The data repository is unavailable.
- `AVAILABLE` - The data repository is available for use.
- `MISCONFIGURED` - Amazon FSx cannot automatically import updates from the S3 bucket until the data repository configuration is corrected. For more information, see [Troubleshooting a Misconfigured linked S3 bucket](https://docs.aws.amazon.com/fsx/latest/LustreGuide/troubleshooting.html#troubleshooting-misconfigured-data-repository) .
- `UPDATING` - The data repository is undergoing a customer initiated update and availability may be impacted.
- `FAILED` - The data repository is in a terminal state that cannot be recovered.

ImportPath -> (string)

The import path to the Amazon S3 bucket (and optional prefix) that youâre using as the data repository for your FSx for Lustre file system, for example `s3://import-bucket/optional-prefix` . If a prefix is specified after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system.

ExportPath -> (string)

The export path to the Amazon S3 bucket (and prefix) that you are using to store new and changed Lustre file system files in S3.

ImportedFileChunkSize -> (integer)

For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.

The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.

AutoImportPolicy -> (string)

Describes the file systemâs linked S3 data repositoryâs `AutoImportPolicy` . The AutoImportPolicy configures how Amazon FSx keeps your file and directory listings up to date as you add or modify objects in your linked S3 bucket. `AutoImportPolicy` can have the following values:

- `NONE` - (Default) AutoImport is off. Amazon FSx only updates file and directory listings from the linked S3 bucket when the file system is created. FSx does not update file and directory listings for any new or changed objects after choosing this option.
- `NEW` - AutoImport is on. Amazon FSx automatically imports directory listings of any new objects added to the linked S3 bucket that do not currently exist in the FSx file system.
- `NEW_CHANGED` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket and any existing objects that are changed in the S3 bucket after you choose this option.
- `NEW_CHANGED_DELETED` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket, any existing objects that are changed in the S3 bucket, and any objects that were deleted in the S3 bucket.

FailureDetails -> (structure)

Provides detailed information about the data repository if its `Lifecycle` is set to `MISCONFIGURED` or `FAILED` .

Message -> (string)

A detailed error message.

DeploymentType -> (string)

The deployment type of the FSx for Lustre file system. *Scratch deployment type* is designed for temporary storage and shorter-term processing of data.

`SCRATCH_1` and `SCRATCH_2` deployment types are best suited for when you need temporary storage and shorter-term processing of data. The `SCRATCH_2` deployment type provides in-transit encryption of data and higher burst throughput capacity than `SCRATCH_1` .

The `PERSISTENT_1` and `PERSISTENT_2` deployment type is used for longer-term storage and workloads and encryption of data in transit. `PERSISTENT_2` offers higher `PerUnitStorageThroughput` (up to 1000 MB/s/TiB) along with a lower minimum storage capacity requirement (600 GiB). To learn more about FSx for Lustre deployment types, see [FSx for Lustre deployment options](https://docs.aws.amazon.com/fsx/latest/LustreGuide/lustre-deployment-types.html) .

The default is `SCRATCH_1` .

PerUnitStorageThroughput -> (integer)

Per unit storage throughput represents the megabytes per second of read or write throughput per 1 tebibyte of storage provisioned. File system throughput capacity is equal to Storage capacity (TiB) * PerUnitStorageThroughput (MB/s/TiB). This option is only valid for `PERSISTENT_1` and `PERSISTENT_2` deployment types.

Valid values:

- For `PERSISTENT_1` SSD storage: 50, 100, 200.
- For `PERSISTENT_1` HDD storage: 12, 40.
- For `PERSISTENT_2` SSD storage: 125, 250, 500, 1000.

MountName -> (string)

You use the `MountName` value when mounting the file system.

For the `SCRATCH_1` deployment type, this value is always â`fsx` â. For `SCRATCH_2` , `PERSISTENT_1` , and `PERSISTENT_2` deployment types, this value is a string that is unique within an Amazon Web Services Region.

DailyAutomaticBackupStartTime -> (string)

A recurring daily time, in the format `HH:MM` . `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.

AutomaticBackupRetentionDays -> (integer)

The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30` .

CopyTagsToBackups -> (boolean)

A boolean flag indicating whether tags on the file system are copied to backups. If itâs set to true, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesnât specify any tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value. (Default = false)

DriveCacheType -> (string)

The type of drive cache used by `PERSISTENT_1` file systems that are provisioned with HDD storage devices. This parameter is required when `StorageType` is HDD. When set to `READ` the file system has an SSD storage cache that is sized to 20% of the file systemâs storage capacity. This improves the performance for frequently accessed files by caching up to 20% of the total storage capacity.

This parameter is required when `StorageType` is set to HDD.

DataCompressionType -> (string)

The data compression configuration for the file system. `DataCompressionType` can have the following values:

- `NONE` - Data compression is turned off for the file system.
- `LZ4` - Data compression is turned on with the LZ4 algorithm.

For more information, see [Lustre data compression](https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-compression.html) .

LogConfiguration -> (structure)

The Lustre logging configuration. Lustre logging writes the enabled log events for your file system to Amazon CloudWatch Logs.

Level -> (string)

The data repository events that are logged by Amazon FSx.

- `WARN_ONLY` - only warning events are logged.
- `ERROR_ONLY` - only error events are logged.
- `WARN_ERROR` - both warning events and error events are logged.
- `DISABLED` - logging of data repository events is turned off.

Note that Amazon File Cache uses a default setting of `WARN_ERROR` , which canât be changed.

Destination -> (string)

The Amazon Resource Name (ARN) that specifies the destination of the logs. The destination can be any Amazon CloudWatch Logs log group ARN. The destination ARN must be in the same Amazon Web Services partition, Amazon Web Services Region, and Amazon Web Services account as your Amazon FSx file system.

RootSquashConfiguration -> (structure)

The Lustre root squash configuration for an Amazon FSx for Lustre file system. When enabled, root squash restricts root-level access from clients that try to access your file system as a root user.

RootSquash -> (string)

You enable root squash by setting a user ID (UID) and group ID (GID) for the file system in the format `UID:GID` (for example, `365534:65534` ). The UID and GID values can range from `0` to `4294967294` :

- A non-zero value for UID and GID enables root squash. The UID and GID values can be different, but each must be a non-zero value.
- A value of `0` (zero) for UID and GID indicates root, and therefore disables root squash.

When root squash is enabled, the user ID and group ID of a root user accessing the file system are re-mapped to the UID and GID you provide.

NoSquashNids -> (list)

When root squash is enabled, you can optionally specify an array of NIDs of clients for which root squash does not apply. A client NID is a Lustre Network Identifier used to uniquely identify a client. You can specify the NID as either a single address or a range of addresses:

- A single address is described in standard Lustre NID format by specifying the clientâs IP address followed by the Lustre network ID (for example, `10.0.1.6@tcp` ).
- An address range is described using a dash to separate the range (for example, `10.0.[2-10].[1-255]@tcp` ).

(string)

MetadataConfiguration -> (structure)

The Lustre metadata performance configuration for an Amazon FSx for Lustre file system using a `PERSISTENT_2` deployment type.

Iops -> (integer)

The number of Metadata IOPS provisioned for the file system. Valid values are `1500` , `3000` , `6000` , `12000` , and multiples of `12000` up to a maximum of `192000` .

Mode -> (string)

The metadata configuration mode for provisioning Metadata IOPS for the file system.

- In AUTOMATIC mode, FSx for Lustre automatically provisions and scales the number of Metadata IOPS on your file system based on your file system storage capacity.
- In USER_PROVISIONED mode, you can choose to specify the number of Metadata IOPS to provision for your file system.

EfaEnabled -> (boolean)

Specifies whether Elastic Fabric Adapter (EFA) and GPUDirect Storage (GDS) support is enabled for the Amazon FSx for Lustre file system.

AdministrativeActions -> (list)

A list of administrative actions for the file system that are in process or waiting to be processed. Administrative actions describe changes to the Amazon FSx system that you have initiated using the `UpdateFileSystem` operation.

(structure)

Describes a specific Amazon FSx administrative action for the current Windows, Lustre, OpenZFS, or ONTAP file system or volume.

AdministrativeActionType -> (string)

Describes the type of administrative action, as follows:

- `FILE_SYSTEM_UPDATE` - A file system update administrative action initiated from the Amazon FSx console, API (`UpdateFileSystem` ), or CLI (`update-file-system` ).
- `THROUGHPUT_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file systemâs throughput capacity has been completed successfully, a `THROUGHPUT_OPTIMIZATION` task starts. You can track the storage-optimization progress using the `ProgressPercent` property. When `THROUGHPUT_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED` . For more information, see [Managing throughput capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-throughput-capacity.html) in the *Amazon FSx for Windows File Server User Guide* .
- `STORAGE_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file systemâs storage capacity has completed successfully, a `STORAGE_OPTIMIZATION` task starts.
- For Windows and ONTAP, storage optimization is the process of migrating the file system data to newer larger disks.
- For Lustre, storage optimization consists of rebalancing the data across the existing and newly added file servers.

You can track the storage-optimization progress using the `ProgressPercent` property. When `STORAGE_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED` . For more information, see [Managing storage capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-capacity.html) in the *Amazon FSx for Windows File Server User Guide* , [Managing storage capacity](https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-storage-capacity.html) in the *Amazon FSx for Lustre User Guide* , and [Managing storage capacity and provisioned IOPS](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-storage-capacity.html) in the *Amazon FSx for NetApp ONTAP User Guide* .

- `FILE_SYSTEM_ALIAS_ASSOCIATION` - A file system update to associate a new Domain Name System (DNS) alias with the file system. For more information, see [AssociateFileSystemAliases](https://docs.aws.amazon.com/fsx/latest/APIReference/API_AssociateFileSystemAliases.html) .
- `FILE_SYSTEM_ALIAS_DISASSOCIATION` - A file system update to disassociate a DNS alias from the file system. For more information, see [DisassociateFileSystemAliases](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DisassociateFileSystemAliases.html) .
- `IOPS_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file systemâs throughput capacity has been completed successfully, a `IOPS_OPTIMIZATION` task starts. You can track the storage-optimization progress using the `ProgressPercent` property. When `IOPS_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED` . For more information, see [Managing provisioned SSD IOPS](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-provisioned-ssd-iops.html) in the Amazon FSx for Windows File Server User Guide.
- `STORAGE_TYPE_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file systemâs throughput capacity has been completed successfully, a `STORAGE_TYPE_OPTIMIZATION` task starts. You can track the storage-optimization progress using the `ProgressPercent` property. When `STORAGE_TYPE_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED` .
- `VOLUME_UPDATE` - A volume update to an Amazon FSx for OpenZFS volume initiated from the Amazon FSx console, API (`UpdateVolume` ), or CLI (`update-volume` ).
- `VOLUME_RESTORE` - An Amazon FSx for OpenZFS volume is returned to the state saved by the specified snapshot, initiated from an API (`RestoreVolumeFromSnapshot` ) or CLI (`restore-volume-from-snapshot` ).
- `SNAPSHOT_UPDATE` - A snapshot update to an Amazon FSx for OpenZFS volume initiated from the Amazon FSx console, API (`UpdateSnapshot` ), or CLI (`update-snapshot` ).
- `RELEASE_NFS_V3_LOCKS` - Tracks the release of Network File System (NFS) V3 locks on an Amazon FSx for OpenZFS file system.
- `DOWNLOAD_DATA_FROM_BACKUP` - An FSx for ONTAP backup is being restored to a new volume on a second-generation file system. Once the all the file metadata is loaded onto the volume, you can mount the volume with read-only access. during this process.
- `VOLUME_INITIALIZE_WITH_SNAPSHOT` - A volume is being created from a snapshot on a different FSx for OpenZFS file system. You can initiate this from the Amazon FSx console, API (`CreateVolume` ), or CLI (`create-volume` ) when using the using the `FULL_COPY` strategy.
- `VOLUME_UPDATE_WITH_SNAPSHOT` - A volume is being updated from a snapshot on a different FSx for OpenZFS file system. You can initiate this from the Amazon FSx console, API (`CopySnapshotAndUpdateVolume` ), or CLI (`copy-snapshot-and-update-volume` ).

ProgressPercent -> (integer)

The percentage-complete status of a `STORAGE_OPTIMIZATION` or `DOWNLOAD_DATA_FROM_BACKUP` administrative action. Does not apply to any other administrative action type.

RequestTime -> (timestamp)

The time that the administrative action request was received.

Status -> (string)

The status of the administrative action, as follows:

- `FAILED` - Amazon FSx failed to process the administrative action successfully.
- `IN_PROGRESS` - Amazon FSx is processing the administrative action.
- `PENDING` - Amazon FSx is waiting to process the administrative action.
- `COMPLETED` - Amazon FSx has finished processing the administrative task. For a backup restore to a second-generation FSx for ONTAP file system, indicates that all data has been downloaded to the volume, and clients now have read-write access to volume.
- `UPDATED_OPTIMIZING` - For a storage-capacity increase update, Amazon FSx has updated the file system with the new storage capacity, and is now performing the storage-optimization process.
- `PENDING` - For a backup restore to a second-generation FSx for ONTAP file system, indicates that the file metadata is being downloaded onto the volume. The volumeâs Lifecycle state is CREATING.
- `IN_PROGRESS` - For a backup restore to a second-generation FSx for ONTAP file system, indicates that all metadata has been downloaded to the new volume and client can access data with read-only access while Amazon FSx downloads the file data to the volume. Track the progress of this process with the `ProgressPercent` element.

TargetFileSystemValues -> (structure)

The target value for the administration action, provided in the `UpdateFileSystem` operation. Returned for `FILE_SYSTEM_UPDATE` administrative actions.

OwnerId -> (string)

The Amazon Web Services account that created the file system. If the file system was created by a user in IAM Identity Center, the Amazon Web Services account to which the IAM user belongs is the owner.

CreationTime -> (timestamp)

The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

FileSystemId -> (string)

The system-generated, unique 17-digit ID of the file system.

FileSystemType -> (string)

The type of Amazon FSx file system, which can be `LUSTRE` , `WINDOWS` , `ONTAP` , or `OPENZFS` .

Lifecycle -> (string)

The lifecycle status of the file system. The following are the possible values and what they mean:

- `AVAILABLE` - The file system is in a healthy state, and is reachable and available for use.
- `CREATING` - Amazon FSx is creating the new file system.
- `DELETING` - Amazon FSx is deleting an existing file system.
- `FAILED` - An existing file system has experienced an unrecoverable failure. When creating a new file system, Amazon FSx was unable to create the file system.
- `MISCONFIGURED` - The file system is in a failed but recoverable state.
- `MISCONFIGURED_UNAVAILABLE` - (Amazon FSx for Windows File Server only) The file system is currently unavailable due to a change in your Active Directory configuration.
- `UPDATING` - The file system is undergoing a customer-initiated update.

FailureDetails -> (structure)

A structure providing details of any failures that occurred.

Message -> (string)

A message describing any failures that occurred.

StorageCapacity -> (integer)

The storage capacity of the file system in gibibytes (GiB).

Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `StorageCapacity` is outside of the minimum or maximum values.

StorageType -> (string)

The type of storage the file system is using. If set to `SSD` , the file system uses solid state drive storage. If set to `HDD` , the file system uses hard disk drive storage.

VpcId -> (string)

The ID of the primary virtual private cloud (VPC) for the file system.

SubnetIds -> (list)

Specifies the IDs of the subnets that the file system is accessible from. For the Amazon FSx Windows and ONTAP `MULTI_AZ_1` file system deployment type, there are two subnet IDs, one for the preferred file server and one for the standby file server. The preferred file server subnet identified in the `PreferredSubnetID` property. All other file systems have only one subnet ID.

For FSx for Lustre file systems, and Single-AZ Windows file systems, this is the ID of the subnet that contains the file systemâs endpoint. For `MULTI_AZ_1` Windows and ONTAP file systems, the file system endpoint is available in the `PreferredSubnetID` .

(string)

The ID for a subnet. A *subnet* is a range of IP addresses in your virtual private cloud (VPC). For more information, see [VPC and subnets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) in the *Amazon VPC User Guide.*

NetworkInterfaceIds -> (list)

The IDs of the elastic network interfaces from which a specific file system is accessible. The elastic network interface is automatically created in the same virtual private cloud (VPC) that the Amazon FSx file system was created in. For more information, see [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the *Amazon EC2 User Guide.*

For an Amazon FSx for Windows File Server file system, you can have one network interface ID. For an Amazon FSx for Lustre file system, you can have more than one.

(string)

An elastic network interface ID. An elastic network interface is a logical networking component in a virtual private cloud (VPC) that represents a virtual network card. For more information, see [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the *Amazon EC2 User Guide for Linux Instances* .

DNSName -> (string)

The Domain Name System (DNS) name for the file system.

KmsKeyId -> (string)

The ID of the Key Management Service (KMS) key used to encrypt Amazon FSx file system data. Used as follows with Amazon FSx file system types:

- Amazon FSx for Lustre `PERSISTENT_1` and `PERSISTENT_2` deployment types only.  `SCRATCH_1` and `SCRATCH_2` types are encrypted using the Amazon FSx service KMS key for your account.
- Amazon FSx for NetApp ONTAP
- Amazon FSx for OpenZFS
- Amazon FSx for Windows File Server

ResourceARN -> (string)

The Amazon Resource Name (ARN) of the file system resource.

Tags -> (list)

The tags to associate with the file system. For more information, see [Tagging your Amazon FSx resources](https://docs.aws.amazon.com/fsx/latest/LustreGuide/tag-resources.html) in the *Amazon FSx for Lustre User Guide* .

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

WindowsConfiguration -> (structure)

The configuration for this Amazon FSx for Windows File Server file system.

ActiveDirectoryId -> (string)

The ID for an existing Amazon Web Services Managed Microsoft Active Directory instance that the file system is joined to.

SelfManagedActiveDirectoryConfiguration -> (structure)

The configuration of the self-managed Microsoft Active Directory (AD) directory to which the Windows File Server or ONTAP storage virtual machine (SVM) instance is joined.

DomainName -> (string)

The fully qualified domain name of the self-managed AD directory.

OrganizationalUnitDistinguishedName -> (string)

The fully qualified distinguished name of the organizational unit within the self-managed AD directory to which the Windows File Server or ONTAP storage virtual machine (SVM) instance is joined.

FileSystemAdministratorsGroup -> (string)

The name of the domain group whose members have administrative privileges for the FSx file system.

UserName -> (string)

The user name for the service account on your self-managed AD domain that FSx uses to join to your AD domain.

DnsIps -> (list)

A list of up to three IP addresses of DNS servers or domain controllers in the self-managed AD directory.

(string)

DeploymentType -> (string)

Specifies the file system deployment type, valid values are the following:

- `MULTI_AZ_1` - Specifies a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability, and supports SSD and HDD storage.
- `SINGLE_AZ_1` - (Default) Specifies a file system that is configured for single AZ redundancy, only supports SSD storage.
- `SINGLE_AZ_2` - Latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports SSD and HDD storage.

For more information, see [Single-AZ and Multi-AZ File Systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html) .

RemoteAdministrationEndpoint -> (string)

For `MULTI_AZ_1` deployment types, use this endpoint when performing administrative tasks on the file system using Amazon FSx Remote PowerShell.

For `SINGLE_AZ_1` and `SINGLE_AZ_2` deployment types, this is the DNS name of the file system.

This endpoint is temporarily unavailable when the file system is undergoing maintenance.

PreferredSubnetId -> (string)

For `MULTI_AZ_1` deployment types, it specifies the ID of the subnet where the preferred file server is located. Must be one of the two subnet IDs specified in `SubnetIds` property. Amazon FSx serves traffic from this subnet except in the event of a failover to the secondary file server.

For `SINGLE_AZ_1` and `SINGLE_AZ_2` deployment types, this value is the same as that for `SubnetIDs` . For more information, see [Availability and durability: Single-AZ and Multi-AZ file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html#single-multi-az-resources) .

PreferredFileServerIp -> (string)

For `MULTI_AZ_1` deployment types, the IP address of the primary, or preferred, file server.

Use this IP address when mounting the file system on Linux SMB clients or Windows SMB clients that are not joined to a Microsoft Active Directory. Applicable for all Windows file system deployment types. This IP address is temporarily unavailable when the file system is undergoing maintenance. For Linux and Windows SMB clients that are joined to an Active Directory, use the file systemâs DNSName instead. For more information on mapping and mounting file shares, see [Accessing File Shares](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/accessing-file-shares.html) .

ThroughputCapacity -> (integer)

The throughput of the Amazon FSx file system, measured in megabytes per second.

MaintenanceOperationsInProgress -> (list)

The list of maintenance operations in progress for this file system.

(string)

An enumeration specifying the currently ongoing maintenance operation.

WeeklyMaintenanceStartTime -> (string)

The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone. d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.

DailyAutomaticBackupStartTime -> (string)

The preferred time to take daily automatic backups, in the UTC time zone.

AutomaticBackupRetentionDays -> (integer)

The number of days to retain automatic backups. Setting this to 0 disables automatic backups. You can retain automatic backups for a maximum of 90 days.

CopyTagsToBackups -> (boolean)

A boolean flag indicating whether tags on the file system should be copied to backups. This value defaults to false. If itâs set to true, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesnât specify any tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.

Aliases -> (list)

An array of one or more DNS aliases that are currently associated with the Amazon FSx file system. Aliases allow you to use existing DNS names to access the data in your Amazon FSx file system. You can associate up to 50 aliases with a file system at any time. You can associate additional DNS aliases after you create the file system using the AssociateFileSystemAliases operation. You can remove DNS aliases from the file system after it is created using the DisassociateFileSystemAliases operation. You only need to specify the alias name in the request payload. For more information, see [DNS aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html) .

(structure)

A DNS alias that is associated with the file system. You can use a DNS alias to access a file system using user-defined DNS names, in addition to the default DNS name that Amazon FSx assigns to the file system. For more information, see [DNS aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html) in the *FSx for Windows File Server User Guide* .

Name -> (string)

The name of the DNS alias. The alias name has to meet the following requirements:

- Formatted as a fully-qualified domain name (FQDN), `hostname.domain` , for example, `accounting.example.com` .
- Can contain alphanumeric characters, the underscore (_), and the hyphen (-).
- Cannot start or end with a hyphen.
- Can start with a numeric.

For DNS names, Amazon FSx stores alphabetic characters as lowercase letters (a-z), regardless of how you specify them: as uppercase letters, lowercase letters, or the corresponding letters in escape codes.

Lifecycle -> (string)

Describes the state of the DNS alias.

- AVAILABLE - The DNS alias is associated with an Amazon FSx file system.
- CREATING - Amazon FSx is creating the DNS alias and associating it with the file system.
- CREATE_FAILED - Amazon FSx was unable to associate the DNS alias with the file system.
- DELETING - Amazon FSx is disassociating the DNS alias from the file system and deleting it.
- DELETE_FAILED - Amazon FSx was unable to disassociate the DNS alias from the file system.

AuditLogConfiguration -> (structure)

The configuration that Amazon FSx for Windows File Server uses to audit and log user accesses of files, folders, and file shares on the Amazon FSx for Windows File Server file system.

FileAccessAuditLogLevel -> (string)

Sets which attempt type is logged by Amazon FSx for file and folder accesses.

- `SUCCESS_ONLY` - only successful attempts to access files or folders are logged.
- `FAILURE_ONLY` - only failed attempts to access files or folders are logged.
- `SUCCESS_AND_FAILURE` - both successful attempts and failed attempts to access files or folders are logged.
- `DISABLED` - access auditing of files and folders is turned off.

FileShareAccessAuditLogLevel -> (string)

Sets which attempt type is logged by Amazon FSx for file share accesses.

- `SUCCESS_ONLY` - only successful attempts to access file shares are logged.
- `FAILURE_ONLY` - only failed attempts to access file shares are logged.
- `SUCCESS_AND_FAILURE` - both successful attempts and failed attempts to access file shares are logged.
- `DISABLED` - access auditing of file shares is turned off.

AuditLogDestination -> (string)

The Amazon Resource Name (ARN) for the destination of the audit logs. The destination can be any Amazon CloudWatch Logs log group ARN or Amazon Kinesis Data Firehose delivery stream ARN.

The name of the Amazon CloudWatch Logs log group must begin with the `/aws/fsx` prefix. The name of the Amazon Kinesis Data Firehose delivery stream must begin with the `aws-fsx` prefix.

The destination ARN (either CloudWatch Logs log group or Kinesis Data Firehose delivery stream) must be in the same Amazon Web Services partition, Amazon Web Services Region, and Amazon Web Services account as your Amazon FSx file system.

DiskIopsConfiguration -> (structure)

The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for Windows file system. By default, Amazon FSx automatically provisions 3 IOPS per GiB of storage capacity. You can provision additional IOPS per GiB of storage, up to the maximum limit associated with your chosen throughput capacity.

Mode -> (string)

Specifies whether the file system is using the `AUTOMATIC` setting of SSD IOPS of 3 IOPS per GB of storage capacity, or if it using a `USER_PROVISIONED` value.

Iops -> (long)

The total number of SSD IOPS provisioned for the file system.

The minimum and maximum values for this property depend on the value of `HAPairs` and `StorageCapacity` . The minimum value is calculated as `StorageCapacity` * 3 * `HAPairs` (3 IOPS per GB of `StorageCapacity` ). The maximum value is calculated as 200,000 * `HAPairs` .

Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `Iops` is outside of the minimum or maximum values.

LustreConfiguration -> (structure)

The configuration for the Amazon FSx for Lustre file system.

WeeklyMaintenanceStartTime -> (string)

The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone. Here, `d` is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.

DataRepositoryConfiguration -> (structure)

The data repository configuration object for Lustre file systems returned in the response of the `CreateFileSystem` operation.

This data type is not supported on file systems with a data repository association. For file systems with a data repository association, see .

Lifecycle -> (string)

Describes the state of the file systemâs S3 durable data repository, if it is configured with an S3 repository. The lifecycle can have the following values:

- `CREATING` - The data repository configuration between the FSx file system and the linked S3 data repository is being created. The data repository is unavailable.
- `AVAILABLE` - The data repository is available for use.
- `MISCONFIGURED` - Amazon FSx cannot automatically import updates from the S3 bucket until the data repository configuration is corrected. For more information, see [Troubleshooting a Misconfigured linked S3 bucket](https://docs.aws.amazon.com/fsx/latest/LustreGuide/troubleshooting.html#troubleshooting-misconfigured-data-repository) .
- `UPDATING` - The data repository is undergoing a customer initiated update and availability may be impacted.
- `FAILED` - The data repository is in a terminal state that cannot be recovered.

ImportPath -> (string)

The import path to the Amazon S3 bucket (and optional prefix) that youâre using as the data repository for your FSx for Lustre file system, for example `s3://import-bucket/optional-prefix` . If a prefix is specified after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system.

ExportPath -> (string)

The export path to the Amazon S3 bucket (and prefix) that you are using to store new and changed Lustre file system files in S3.

ImportedFileChunkSize -> (integer)

For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.

The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.

AutoImportPolicy -> (string)

Describes the file systemâs linked S3 data repositoryâs `AutoImportPolicy` . The AutoImportPolicy configures how Amazon FSx keeps your file and directory listings up to date as you add or modify objects in your linked S3 bucket. `AutoImportPolicy` can have the following values:

- `NONE` - (Default) AutoImport is off. Amazon FSx only updates file and directory listings from the linked S3 bucket when the file system is created. FSx does not update file and directory listings for any new or changed objects after choosing this option.
- `NEW` - AutoImport is on. Amazon FSx automatically imports directory listings of any new objects added to the linked S3 bucket that do not currently exist in the FSx file system.
- `NEW_CHANGED` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket and any existing objects that are changed in the S3 bucket after you choose this option.
- `NEW_CHANGED_DELETED` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket, any existing objects that are changed in the S3 bucket, and any objects that were deleted in the S3 bucket.

FailureDetails -> (structure)

Provides detailed information about the data repository if its `Lifecycle` is set to `MISCONFIGURED` or `FAILED` .

Message -> (string)

A detailed error message.

DeploymentType -> (string)

The deployment type of the FSx for Lustre file system. *Scratch deployment type* is designed for temporary storage and shorter-term processing of data.

`SCRATCH_1` and `SCRATCH_2` deployment types are best suited for when you need temporary storage and shorter-term processing of data. The `SCRATCH_2` deployment type provides in-transit encryption of data and higher burst throughput capacity than `SCRATCH_1` .

The `PERSISTENT_1` and `PERSISTENT_2` deployment type is used for longer-term storage and workloads and encryption of data in transit. `PERSISTENT_2` offers higher `PerUnitStorageThroughput` (up to 1000 MB/s/TiB) along with a lower minimum storage capacity requirement (600 GiB). To learn more about FSx for Lustre deployment types, see [FSx for Lustre deployment options](https://docs.aws.amazon.com/fsx/latest/LustreGuide/lustre-deployment-types.html) .

The default is `SCRATCH_1` .

PerUnitStorageThroughput -> (integer)

Per unit storage throughput represents the megabytes per second of read or write throughput per 1 tebibyte of storage provisioned. File system throughput capacity is equal to Storage capacity (TiB) * PerUnitStorageThroughput (MB/s/TiB). This option is only valid for `PERSISTENT_1` and `PERSISTENT_2` deployment types.

Valid values:

- For `PERSISTENT_1` SSD storage: 50, 100, 200.
- For `PERSISTENT_1` HDD storage: 12, 40.
- For `PERSISTENT_2` SSD storage: 125, 250, 500, 1000.

MountName -> (string)

You use the `MountName` value when mounting the file system.

For the `SCRATCH_1` deployment type, this value is always â`fsx` â. For `SCRATCH_2` , `PERSISTENT_1` , and `PERSISTENT_2` deployment types, this value is a string that is unique within an Amazon Web Services Region.

DailyAutomaticBackupStartTime -> (string)

A recurring daily time, in the format `HH:MM` . `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.

AutomaticBackupRetentionDays -> (integer)

The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30` .

CopyTagsToBackups -> (boolean)

A boolean flag indicating whether tags on the file system are copied to backups. If itâs set to true, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesnât specify any tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value. (Default = false)

DriveCacheType -> (string)

The type of drive cache used by `PERSISTENT_1` file systems that are provisioned with HDD storage devices. This parameter is required when `StorageType` is HDD. When set to `READ` the file system has an SSD storage cache that is sized to 20% of the file systemâs storage capacity. This improves the performance for frequently accessed files by caching up to 20% of the total storage capacity.

This parameter is required when `StorageType` is set to HDD.

DataCompressionType -> (string)

The data compression configuration for the file system. `DataCompressionType` can have the following values:

- `NONE` - Data compression is turned off for the file system.
- `LZ4` - Data compression is turned on with the LZ4 algorithm.

For more information, see [Lustre data compression](https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-compression.html) .

LogConfiguration -> (structure)

The Lustre logging configuration. Lustre logging writes the enabled log events for your file system to Amazon CloudWatch Logs.

Level -> (string)

The data repository events that are logged by Amazon FSx.

- `WARN_ONLY` - only warning events are logged.
- `ERROR_ONLY` - only error events are logged.
- `WARN_ERROR` - both warning events and error events are logged.
- `DISABLED` - logging of data repository events is turned off.

Note that Amazon File Cache uses a default setting of `WARN_ERROR` , which canât be changed.

Destination -> (string)

The Amazon Resource Name (ARN) that specifies the destination of the logs. The destination can be any Amazon CloudWatch Logs log group ARN. The destination ARN must be in the same Amazon Web Services partition, Amazon Web Services Region, and Amazon Web Services account as your Amazon FSx file system.

RootSquashConfiguration -> (structure)

The Lustre root squash configuration for an Amazon FSx for Lustre file system. When enabled, root squash restricts root-level access from clients that try to access your file system as a root user.

RootSquash -> (string)

You enable root squash by setting a user ID (UID) and group ID (GID) for the file system in the format `UID:GID` (for example, `365534:65534` ). The UID and GID values can range from `0` to `4294967294` :

- A non-zero value for UID and GID enables root squash. The UID and GID values can be different, but each must be a non-zero value.
- A value of `0` (zero) for UID and GID indicates root, and therefore disables root squash.

When root squash is enabled, the user ID and group ID of a root user accessing the file system are re-mapped to the UID and GID you provide.

NoSquashNids -> (list)

When root squash is enabled, you can optionally specify an array of NIDs of clients for which root squash does not apply. A client NID is a Lustre Network Identifier used to uniquely identify a client. You can specify the NID as either a single address or a range of addresses:

- A single address is described in standard Lustre NID format by specifying the clientâs IP address followed by the Lustre network ID (for example, `10.0.1.6@tcp` ).
- An address range is described using a dash to separate the range (for example, `10.0.[2-10].[1-255]@tcp` ).

(string)

MetadataConfiguration -> (structure)

The Lustre metadata performance configuration for an Amazon FSx for Lustre file system using a `PERSISTENT_2` deployment type.

Iops -> (integer)

The number of Metadata IOPS provisioned for the file system. Valid values are `1500` , `3000` , `6000` , `12000` , and multiples of `12000` up to a maximum of `192000` .

Mode -> (string)

The metadata configuration mode for provisioning Metadata IOPS for the file system.

- In AUTOMATIC mode, FSx for Lustre automatically provisions and scales the number of Metadata IOPS on your file system based on your file system storage capacity.
- In USER_PROVISIONED mode, you can choose to specify the number of Metadata IOPS to provision for your file system.

EfaEnabled -> (boolean)

Specifies whether Elastic Fabric Adapter (EFA) and GPUDirect Storage (GDS) support is enabled for the Amazon FSx for Lustre file system.

OntapConfiguration -> (structure)

The configuration for this Amazon FSx for NetApp ONTAP file system.

AutomaticBackupRetentionDays -> (integer)

The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30` .

DailyAutomaticBackupStartTime -> (string)

A recurring daily time, in the format `HH:MM` . `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.

DeploymentType -> (string)

Specifies the FSx for ONTAP file system deployment type in use in the file system.

- `MULTI_AZ_1` - A high availability file system configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability. This is a first-generation FSx for ONTAP file system.
- `MULTI_AZ_2` - A high availability file system configured for Multi-AZ redundancy to tolerate temporary AZ unavailability. This is a second-generation FSx for ONTAP file system.
- `SINGLE_AZ_1` - A file system configured for Single-AZ redundancy. This is a first-generation FSx for ONTAP file system.
- `SINGLE_AZ_2` - A file system configured with multiple high-availability (HA) pairs for Single-AZ redundancy. This is a second-generation FSx for ONTAP file system.

For information about the use cases for Multi-AZ and Single-AZ deployments, refer to [Choosing Multi-AZ or Single-AZ file system deployment](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-multiAZ.html) .

EndpointIpAddressRange -> (string)

(Multi-AZ only) Specifies the IP address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API, Amazon FSx selects an unused IP address range for you from the 198.19.* range. By default in the Amazon FSx console, Amazon FSx chooses the last 64 IP addresses from the VPCâs primary CIDR range to use as the endpoint IP address range for the file system. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables.

Endpoints -> (structure)

The `Management` and `Intercluster` endpoints that are used to access data or to manage the file system using the NetApp ONTAP CLI, REST API, or NetApp SnapMirror.

Intercluster -> (structure)

An endpoint for managing your file system by setting up NetApp SnapMirror with other ONTAP systems.

DNSName -> (string)

The file systemâs DNS name. You can mount your file system using its DNS name.

IpAddresses -> (list)

IP addresses of the file system endpoint.

(string)

Management -> (structure)

An endpoint for managing your file system using the NetApp ONTAP CLI and NetApp ONTAP API.

DNSName -> (string)

The file systemâs DNS name. You can mount your file system using its DNS name.

IpAddresses -> (list)

IP addresses of the file system endpoint.

(string)

DiskIopsConfiguration -> (structure)

The SSD IOPS configuration for the ONTAP file system, specifying the number of provisioned IOPS and the provision mode.

Mode -> (string)

Specifies whether the file system is using the `AUTOMATIC` setting of SSD IOPS of 3 IOPS per GB of storage capacity, or if it using a `USER_PROVISIONED` value.

Iops -> (long)

The total number of SSD IOPS provisioned for the file system.

The minimum and maximum values for this property depend on the value of `HAPairs` and `StorageCapacity` . The minimum value is calculated as `StorageCapacity` * 3 * `HAPairs` (3 IOPS per GB of `StorageCapacity` ). The maximum value is calculated as 200,000 * `HAPairs` .

Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `Iops` is outside of the minimum or maximum values.

PreferredSubnetId -> (string)

The ID for a subnet. A *subnet* is a range of IP addresses in your virtual private cloud (VPC). For more information, see [VPC and subnets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) in the *Amazon VPC User Guide.*

RouteTableIds -> (list)

(Multi-AZ only) The VPC route tables in which your file systemâs endpoints are created.

(string)

ThroughputCapacity -> (integer)

The sustained throughput of an Amazon FSx file system in Megabytes per second (MBps).

WeeklyMaintenanceStartTime -> (string)

A recurring weekly time, in the format `D:HH:MM` .

`D` is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see [the ISO-8601 spec as described on Wikipedia](https://en.wikipedia.org/wiki/ISO_week_date) .

`HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour.

For example, `1:05:00` specifies maintenance at 5 AM Monday.

FsxAdminPassword -> (string)

You can use the `fsxadmin` user account to access the NetApp ONTAP CLI and REST API. The password value is always redacted in the response.

HAPairs -> (integer)

Specifies how many high-availability (HA) file server pairs the file system will have. The default value is 1. The value of this property affects the values of `StorageCapacity` , `Iops` , and `ThroughputCapacity` . For more information, see [High-availability (HA) pairs](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/HA-pairs.html) in the FSx for ONTAP user guide.

Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:

- The value of `HAPairs` is less than 1 or greater than 12.
- The value of `HAPairs` is greater than 1 and the value of `DeploymentType` is `SINGLE_AZ_1` , `MULTI_AZ_1` , or `MULTI_AZ_2` .

ThroughputCapacityPerHAPair -> (integer)

Use to choose the throughput capacity per HA pair. When the value of `HAPairs` is equal to 1, the value of `ThroughputCapacityPerHAPair` is the total throughput for the file system.

This field and `ThroughputCapacity` cannot be defined in the same API call, but one is required.

This field and `ThroughputCapacity` are the same for file systems with one HA pair.

- For `SINGLE_AZ_1` and `MULTI_AZ_1` file systems, valid values are 128, 256, 512, 1024, 2048, or 4096 MBps.
- For `SINGLE_AZ_2` , valid values are 1536, 3072, or 6144 MBps.
- For `MULTI_AZ_2` , valid values are 384, 768, 1536, 3072, or 6144 MBps.

Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:

- The value of `ThroughputCapacity` and `ThroughputCapacityPerHAPair` are not the same value.
- The value of deployment type is `SINGLE_AZ_2` and `ThroughputCapacity` / `ThroughputCapacityPerHAPair` is not a valid HA pair (a value between 1 and 12).
- The value of `ThroughputCapacityPerHAPair` is not a valid value.

FileSystemTypeVersion -> (string)

The Lustre version of the Amazon FSx for Lustre file system, which can be `2.10` , `2.12` , or `2.15` .

OpenZFSConfiguration -> (structure)

The configuration for this Amazon FSx for OpenZFS file system.

AutomaticBackupRetentionDays -> (integer)

The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30` .

CopyTagsToBackups -> (boolean)

A Boolean value indicating whether tags on the file system should be copied to backups. If itâs set to `true` , all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesnât specify any tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.

CopyTagsToVolumes -> (boolean)

A Boolean value indicating whether tags for the volume should be copied to snapshots. This value defaults to `false` . If itâs set to `true` , all tags for the volume are copied to snapshots where the user doesnât specify tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.

DailyAutomaticBackupStartTime -> (string)

A recurring daily time, in the format `HH:MM` . `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.

DeploymentType -> (string)

Specifies the file-system deployment type. Amazon FSx for OpenZFS supports `MULTI_AZ_1` , `SINGLE_AZ_HA_2` , `SINGLE_AZ_HA_1` , `SINGLE_AZ_2` , and `SINGLE_AZ_1` .

ThroughputCapacity -> (integer)

The throughput of an Amazon FSx file system, measured in megabytes per second (MBps).

WeeklyMaintenanceStartTime -> (string)

A recurring weekly time, in the format `D:HH:MM` .

`D` is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see [the ISO-8601 spec as described on Wikipedia](https://en.wikipedia.org/wiki/ISO_week_date) .

`HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour.

For example, `1:05:00` specifies maintenance at 5 AM Monday.

DiskIopsConfiguration -> (structure)

The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for NetApp ONTAP, Amazon FSx for Windows File Server, or FSx for OpenZFS file system. By default, Amazon FSx automatically provisions 3 IOPS per GB of storage capacity. You can provision additional IOPS per GB of storage. The configuration consists of the total number of provisioned SSD IOPS and how it is was provisioned, or the mode (by the customer or by Amazon FSx).

Mode -> (string)

Specifies whether the file system is using the `AUTOMATIC` setting of SSD IOPS of 3 IOPS per GB of storage capacity, or if it using a `USER_PROVISIONED` value.

Iops -> (long)

The total number of SSD IOPS provisioned for the file system.

The minimum and maximum values for this property depend on the value of `HAPairs` and `StorageCapacity` . The minimum value is calculated as `StorageCapacity` * 3 * `HAPairs` (3 IOPS per GB of `StorageCapacity` ). The maximum value is calculated as 200,000 * `HAPairs` .

Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `Iops` is outside of the minimum or maximum values.

RootVolumeId -> (string)

The ID of the root volume of the OpenZFS file system.

PreferredSubnetId -> (string)

Required when `DeploymentType` is set to `MULTI_AZ_1` . This specifies the subnet in which you want the preferred file server to be located.

EndpointIpAddressRange -> (string)

(Multi-AZ only) Specifies the IP address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API and Amazon FSx console, Amazon FSx selects an available /28 IP address range for you from one of the VPCâs CIDR ranges. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables.

RouteTableIds -> (list)

(Multi-AZ only) The VPC route tables in which your file systemâs endpoints are created.

(string)

EndpointIpAddress -> (string)

The IP address of the endpoint that is used to access data or to manage the file system.

ReadCacheConfiguration -> (structure)

Required when `StorageType` is set to `INTELLIGENT_TIERING` . Specifies the optional provisioned SSD read cache.

SizingMode -> (string)

Specifies how the provisioned SSD read cache is sized, as follows:

- Set to `NO_CACHE` if you do not want to use an SSD read cache with your Intelligent-Tiering file system.
- Set to `USER_PROVISIONED` to specify the exact size of your SSD read cache.
- Set to `PROPORTIONAL_TO_THROUGHPUT_CAPACITY` to have your SSD read cache automatically sized based on your throughput capacity.

SizeGiB -> (integer)

Required if `SizingMode` is set to `USER_PROVISIONED` . Specifies the size of the file systemâs SSD read cache, in gibibytes (GiB).

FailureDetails -> (structure)

Provides information about a failed administrative action.

Message -> (string)

Error message providing details about the failed administrative action.

TargetVolumeValues -> (structure)

Describes an Amazon FSx volume.

CreationTime -> (timestamp)

The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

FileSystemId -> (string)

The globally unique ID of the file system, assigned by Amazon FSx.

Lifecycle -> (string)

The lifecycle status of the volume.

- `AVAILABLE` - The volume is fully available for use.
- `CREATED` - The volume has been created.
- `CREATING` - Amazon FSx is creating the new volume.
- `DELETING` - Amazon FSx is deleting an existing volume.
- `FAILED` - Amazon FSx was unable to create the volume.
- `MISCONFIGURED` - The volume is in a failed but recoverable state.
- `PENDING` - Amazon FSx hasnât started creating the volume.

Name -> (string)

The name of the volume.

OntapConfiguration -> (structure)

The configuration of an Amazon FSx for NetApp ONTAP volume.

FlexCacheEndpointType -> (string)

Specifies the FlexCache endpoint type of the volume. Valid values are the following:

- `NONE` specifies that the volume doesnât have a FlexCache configuration. `NONE` is the default.
- `ORIGIN` specifies that the volume is the origin volume for a FlexCache volume.
- `CACHE` specifies that the volume is a FlexCache volume.

JunctionPath -> (string)

Specifies the directory that network-attached storage (NAS) clients use to mount the volume, along with the storage virtual machine (SVM) Domain Name System (DNS) name or IP address. You can create a `JunctionPath` directly below a parent volume junction or on a directory within a volume. A `JunctionPath` for a volume named `vol3` might be `/vol1/vol2/vol3` , or `/vol1/dir2/vol3` , or even `/dir1/dir2/vol3` .

SecurityStyle -> (string)

The security style for the volume, which can be `UNIX` , `NTFS` , or `MIXED` .

SizeInMegabytes -> (integer)

The configured size of the volume, in megabytes (MBs).

StorageEfficiencyEnabled -> (boolean)

The volumeâs storage efficiency setting.

StorageVirtualMachineId -> (string)

The ID of the volumeâs storage virtual machine.

StorageVirtualMachineRoot -> (boolean)

A Boolean flag indicating whether this volume is the root volume for its storage virtual machine (SVM). Only one volume on an SVM can be the root volume. This value defaults to `false` . If this value is `true` , then this is the SVM root volume.

This flag is useful when youâre deleting an SVM, because you must first delete all non-root volumes. This flag, when set to `false` , helps you identify which volumes to delete before you can delete the SVM.

TieringPolicy -> (structure)

The volumeâs `TieringPolicy` setting.

CoolingPeriod -> (integer)

Specifies the number of days that user data in a volume must remain inactive before it is considered âcoldâ and moved to the capacity pool. Used with the `AUTO` and `SNAPSHOT_ONLY` tiering policies. Enter a whole number between 2 and 183. Default values are 31 days for `AUTO` and 2 days for `SNAPSHOT_ONLY` .

Name -> (string)

Specifies the tiering policy used to transition data. Default value is `SNAPSHOT_ONLY` .

- `SNAPSHOT_ONLY` - moves cold snapshots to the capacity pool storage tier.
- `AUTO` - moves cold user data and snapshots to the capacity pool storage tier based on your access patterns.
- `ALL` - moves all user data blocks in both the active file system and Snapshot copies to the storage pool tier.
- `NONE` - keeps a volumeâs data in the primary storage tier, preventing it from being moved to the capacity pool tier.

UUID -> (string)

The volumeâs universally unique identifier (UUID).

OntapVolumeType -> (string)

Specifies the type of volume. Valid values are the following:

- `RW` specifies a read/write volume. `RW` is the default.
- `DP` specifies a data-protection volume. You can protect data by replicating it to data-protection mirror copies. If a disaster occurs, you can use these data-protection mirror copies to recover data.
- `LS` specifies a load-sharing mirror volume. A load-sharing mirror reduces the network traffic to a FlexVol volume by providing additional read-only access to clients.

SnapshotPolicy -> (string)

Specifies the snapshot policy for the volume. There are three built-in snapshot policies:

- `default` : This is the default policy. A maximum of six hourly snapshots taken five minutes past the hour. A maximum of two daily snapshots taken Monday through Saturday at 10 minutes after midnight. A maximum of two weekly snapshots taken every Sunday at 15 minutes after midnight.
- `default-1weekly` : This policy is the same as the `default` policy except that it only retains one snapshot from the weekly schedule.
- `none` : This policy does not take any snapshots. This policy can be assigned to volumes to prevent automatic snapshots from being taken.

You can also provide the name of a custom policy that you created with the ONTAP CLI or REST API.

For more information, see [Snapshot policies](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snapshots-ontap.html#snapshot-policies) in the Amazon FSx for NetApp ONTAP User Guide.

CopyTagsToBackups -> (boolean)

A boolean flag indicating whether tags for the volume should be copied to backups. This value defaults to false. If itâs set to true, all tags for the volume are copied to all automatic and user-initiated backups where the user doesnât specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the volume, regardless of this value.

SnaplockConfiguration -> (structure)

The SnapLock configuration object for an FSx for ONTAP SnapLock volume.

AuditLogVolume -> (boolean)

Enables or disables the audit log volume for an FSx for ONTAP SnapLock volume. The default value is `false` . If you set `AuditLogVolume` to `true` , the SnapLock volume is created as an audit log volume. The minimum retention period for an audit log volume is six months.

For more information, see [SnapLock audit log volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/how-snaplock-works.html#snaplock-audit-log-volume) .

AutocommitPeriod -> (structure)

The configuration object for setting the autocommit period of files in an FSx for ONTAP SnapLock volume.

Type -> (string)

Defines the type of time for the autocommit period of a file in an FSx for ONTAP SnapLock volume. Setting this value to `NONE` disables autocommit. The default value is `NONE` .

Value -> (integer)

Defines the amount of time for the autocommit period of a file in an FSx for ONTAP SnapLock volume. The following ranges are valid:

- `Minutes` : 5 - 65,535
- `Hours` : 1 - 65,535
- `Days` : 1 - 3,650
- `Months` : 1 - 120
- `Years` : 1 - 10

PrivilegedDelete -> (string)

Enables, disables, or permanently disables privileged delete on an FSx for ONTAP SnapLock Enterprise volume. Enabling privileged delete allows SnapLock administrators to delete write once, read many (WORM) files even if they have active retention periods. `PERMANENTLY_DISABLED` is a terminal state. If privileged delete is permanently disabled on a SnapLock volume, you canât re-enable it. The default value is `DISABLED` .

For more information, see [Privileged delete](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-enterprise.html#privileged-delete) .

RetentionPeriod -> (structure)

Specifies the retention period of an FSx for ONTAP SnapLock volume.

DefaultRetention -> (structure)

The retention period assigned to a write once, read many (WORM) file by default if an explicit retention period is not set for an FSx for ONTAP SnapLock volume. The default retention period must be greater than or equal to the minimum retention period and less than or equal to the maximum retention period.

Type -> (string)

Defines the type of time for the retention period of an FSx for ONTAP SnapLock volume. Set it to one of the valid types. If you set it to `INFINITE` , the files are retained forever. If you set it to `UNSPECIFIED` , the files are retained until you set an explicit retention period.

Value -> (integer)

Defines the amount of time for the retention period of an FSx for ONTAP SnapLock volume. You canât set a value for `INFINITE` or `UNSPECIFIED` . For all other options, the following ranges are valid:

- `Seconds` : 0 - 65,535
- `Minutes` : 0 - 65,535
- `Hours` : 0 - 24
- `Days` : 0 - 365
- `Months` : 0 - 12
- `Years` : 0 - 100

MinimumRetention -> (structure)

The shortest retention period that can be assigned to a WORM file on an FSx for ONTAP SnapLock volume.

Type -> (string)

Defines the type of time for the retention period of an FSx for ONTAP SnapLock volume. Set it to one of the valid types. If you set it to `INFINITE` , the files are retained forever. If you set it to `UNSPECIFIED` , the files are retained until you set an explicit retention period.

Value -> (integer)

Defines the amount of time for the retention period of an FSx for ONTAP SnapLock volume. You canât set a value for `INFINITE` or `UNSPECIFIED` . For all other options, the following ranges are valid:

- `Seconds` : 0 - 65,535
- `Minutes` : 0 - 65,535
- `Hours` : 0 - 24
- `Days` : 0 - 365
- `Months` : 0 - 12
- `Years` : 0 - 100

MaximumRetention -> (structure)

The longest retention period that can be assigned to a WORM file on an FSx for ONTAP SnapLock volume.

Type -> (string)

Defines the type of time for the retention period of an FSx for ONTAP SnapLock volume. Set it to one of the valid types. If you set it to `INFINITE` , the files are retained forever. If you set it to `UNSPECIFIED` , the files are retained until you set an explicit retention period.

Value -> (integer)

Defines the amount of time for the retention period of an FSx for ONTAP SnapLock volume. You canât set a value for `INFINITE` or `UNSPECIFIED` . For all other options, the following ranges are valid:

- `Seconds` : 0 - 65,535
- `Minutes` : 0 - 65,535
- `Hours` : 0 - 24
- `Days` : 0 - 365
- `Months` : 0 - 12
- `Years` : 0 - 100

SnaplockType -> (string)

Specifies the retention mode of an FSx for ONTAP SnapLock volume. After it is set, it canât be changed. You can choose one of the following retention modes:

- `COMPLIANCE` : Files transitioned to write once, read many (WORM) on a Compliance volume canât be deleted until their retention periods expire. This retention mode is used to address government or industry-specific mandates or to protect against ransomware attacks. For more information, see [SnapLock Compliance](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-compliance.html) .
- `ENTERPRISE` : Files transitioned to WORM on an Enterprise volume can be deleted by authorized users before their retention periods expire using privileged delete. This retention mode is used to advance an organizationâs data integrity and internal compliance or to test retention settings before using SnapLock Compliance. For more information, see [SnapLock Enterprise](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-enterprise.html) .

VolumeAppendModeEnabled -> (boolean)

Enables or disables volume-append mode on an FSx for ONTAP SnapLock volume. Volume-append mode allows you to create WORM-appendable files and write data to them incrementally. The default value is `false` .

For more information, see [Volume-append mode](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/worm-state.html#worm-state-append) .

VolumeStyle -> (string)

Use to specify the style of an ONTAP volume. For more information about FlexVols and FlexGroups, see [Volume types](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/volume-types.html) in Amazon FSx for NetApp ONTAP User Guide.

AggregateConfiguration -> (structure)

This structure specifies configuration options for a volumeâs storage aggregate or aggregates.

Aggregates -> (list)

The list of aggregates that this volume resides on. Aggregates are storage pools which make up your primary storage tier. Each high-availability (HA) pair has one aggregate. The names of the aggregates map to the names of the aggregates in the ONTAP CLI and REST API. For FlexVols, there will always be a single entry.

Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:

- The strings in the value of `Aggregates` are not are not formatted as `aggrX` , where X is a number between 1 and 12.
- The value of `Aggregates` contains aggregates that are not present.
- One or more of the aggregates supplied are too close to the volume limit to support adding more volumes.

(string)

TotalConstituents -> (integer)

The total number of constituents this FlexGroup volume has. Not applicable for FlexVols.

SizeInBytes -> (long)

The configured size of the volume, in bytes.

ResourceARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

Tags -> (list)

A list of `Tag` values, with a maximum of 50 elements.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

VolumeId -> (string)

The system-generated, unique ID of the volume.

VolumeType -> (string)

The type of the volume.

LifecycleTransitionReason -> (structure)

The reason why the volume lifecycle status changed.

Message -> (string)

A detailed error message.

OpenZFSConfiguration -> (structure)

The configuration of an Amazon FSx for OpenZFS volume.

ParentVolumeId -> (string)

The ID of the parent volume.

VolumePath -> (string)

The path to the volume from the root volume. For example, `fsx/parentVolume/volume1` .

StorageCapacityReservationGiB -> (integer)

The amount of storage in gibibytes (GiB) to reserve from the parent volume. You canât reserve more storage than the parent volume has reserved.

StorageCapacityQuotaGiB -> (integer)

The maximum amount of storage in gibibytes (GiB) that the volume can use from its parent. You can specify a quota larger than the storage on the parent volume.

RecordSizeKiB -> (integer)

The record size of an OpenZFS volume, in kibibytes (KiB). Valid values are 4, 8, 16, 32, 64, 128, 256, 512, or 1024 KiB. The default is 128 KiB. Most workloads should use the default record size. For guidance on when to set a custom record size, see the *Amazon FSx for OpenZFS User Guide* .

DataCompressionType -> (string)

Specifies the method used to compress the data on the volume. The compression type is `NONE` by default.

- `NONE` - Doesnât compress the data on the volume. `NONE` is the default.
- `ZSTD` - Compresses the data in the volume using the Zstandard (ZSTD) compression algorithm. Compared to LZ4, Z-Standard provides a better compression ratio to minimize on-disk storage utilization.
- `LZ4` - Compresses the data in the volume using the LZ4 compression algorithm. Compared to Z-Standard, LZ4 is less compute-intensive and delivers higher write throughput speeds.

CopyTagsToSnapshots -> (boolean)

A Boolean value indicating whether tags for the volume should be copied to snapshots. This value defaults to `false` . If itâs set to `true` , all tags for the volume are copied to snapshots where the user doesnât specify tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.

OriginSnapshot -> (structure)

The configuration object that specifies the snapshot to use as the origin of the data for the volume.

SnapshotARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

CopyStrategy -> (string)

The strategy used when copying data from the snapshot to the new volume.

- `CLONE` - The new volume references the data in the origin snapshot. Cloning a snapshot is faster than copying the data from a snapshot to a new volume and doesnât consume disk throughput. However, the origin snapshot canât be deleted if there is a volume using its copied data.
- `FULL_COPY` - Copies all data from the snapshot to the new volume.

### Note

The `INCREMENTAL_COPY` option is only for updating an existing volume by using a snapshot from another FSx for OpenZFS file system. For more information, see [CopySnapshotAndUpdateVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CopySnapshotAndUpdateVolume.html) .

ReadOnly -> (boolean)

A Boolean value indicating whether the volume is read-only.

NfsExports -> (list)

The configuration object for mounting a Network File System (NFS) file system.

(structure)

The Network File System (NFS) configurations for mounting an Amazon FSx for OpenZFS file system.

ClientConfigurations -> (list)

A list of configuration objects that contain the client and options for mounting the OpenZFS file system.

(structure)

Specifies who can mount an OpenZFS file system and the options available while mounting the file system.

Clients -> (string)

A value that specifies who can mount the file system. You can provide a wildcard character (`*` ), an IP address (`0.0.0.0` ), or a CIDR address (`192.0.2.0/24` ). By default, Amazon FSx uses the wildcard character when specifying the client.

Options -> (list)

The options to use when mounting the file system. For a list of options that you can use with Network File System (NFS), see the [exports(5) - Linux man page](https://linux.die.net/man/5/exports) . When choosing your options, consider the following:

- `crossmnt` is used by default. If you donât specify `crossmnt` when changing the client configuration, you wonât be able to see or access snapshots in your file systemâs snapshot directory.
- `sync` is used by default. If you instead specify `async` , the system acknowledges writes before writing to disk. If the system crashes before the writes are finished, you lose the unwritten data.

(string)

UserAndGroupQuotas -> (list)

An object specifying how much storage users or groups can use on the volume.

(structure)

Used to configure quotas that define how much storage a user or group can use on an FSx for OpenZFS volume. For more information, see [Volume properties](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-volumes.html#volume-properties) in the FSx for OpenZFS User Guide.

Type -> (string)

Specifies whether the quota applies to a user or group.

Id -> (integer)

The ID of the user or group that the quota applies to.

StorageCapacityQuotaGiB -> (integer)

The user or groupâs storage quota, in gibibytes (GiB).

RestoreToSnapshot -> (string)

Specifies the ID of the snapshot to which the volume was restored.

DeleteIntermediateSnaphots -> (boolean)

A Boolean value indicating whether snapshots between the current state and the specified snapshot should be deleted when a volume is restored from snapshot.

DeleteClonedVolumes -> (boolean)

A Boolean value indicating whether dependent clone volumes created from intermediate snapshots should be deleted when a volume is restored from snapshot.

DeleteIntermediateData -> (boolean)

A Boolean value indicating whether snapshot data that differs between the current state and the specified snapshot should be overwritten when a volume is restored from a snapshot.

SourceSnapshotARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

DestinationSnapshot -> (string)

The ID of the snapshot thatâs being copied or was most recently copied to the destination volume.

CopyStrategy -> (string)

Specifies the strategy used when copying data from the snapshot to the new volume.

- `CLONE` - The new volume references the data in the origin snapshot. Cloning a snapshot is faster than copying data from the snapshot to a new volume and doesnât consume disk throughput. However, the origin snapshot canât be deleted if there is a volume using its copied data.
- `FULL_COPY` - Copies all data from the snapshot to the new volume. Specify this option to create the volume from a snapshot on another FSx for OpenZFS file system.

### Note

The `INCREMENTAL_COPY` option is only for updating an existing volume by using a snapshot from another FSx for OpenZFS file system. For more information, see [CopySnapshotAndUpdateVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CopySnapshotAndUpdateVolume.html) .

TargetSnapshotValues -> (structure)

A snapshot of an Amazon FSx for OpenZFS volume.

ResourceARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

SnapshotId -> (string)

The ID of the snapshot.

Name -> (string)

The name of the snapshot.

VolumeId -> (string)

The ID of the volume that the snapshot is of.

CreationTime -> (timestamp)

The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

Lifecycle -> (string)

The lifecycle status of the snapshot.

- `PENDING` - Amazon FSx hasnât started creating the snapshot.
- `CREATING` - Amazon FSx is creating the snapshot.
- `DELETING` - Amazon FSx is deleting the snapshot.
- `AVAILABLE` - The snapshot is fully available.

LifecycleTransitionReason -> (structure)

Describes why a resource lifecycle state changed.

Message -> (string)

A detailed error message.

Tags -> (list)

A list of `Tag` values, with a maximum of 50 elements.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

TotalTransferBytes -> (long)

The number of bytes that have transferred for the FSx for OpenZFS snapshot that youâre copying.

RemainingTransferBytes -> (long)

The remaining bytes to transfer for the FSx for OpenZFS snapshot that youâre copying.

OntapConfiguration -> (structure)

The configuration for this Amazon FSx for NetApp ONTAP file system.

AutomaticBackupRetentionDays -> (integer)

The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30` .

DailyAutomaticBackupStartTime -> (string)

A recurring daily time, in the format `HH:MM` . `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.

DeploymentType -> (string)

Specifies the FSx for ONTAP file system deployment type in use in the file system.

- `MULTI_AZ_1` - A high availability file system configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability. This is a first-generation FSx for ONTAP file system.
- `MULTI_AZ_2` - A high availability file system configured for Multi-AZ redundancy to tolerate temporary AZ unavailability. This is a second-generation FSx for ONTAP file system.
- `SINGLE_AZ_1` - A file system configured for Single-AZ redundancy. This is a first-generation FSx for ONTAP file system.
- `SINGLE_AZ_2` - A file system configured with multiple high-availability (HA) pairs for Single-AZ redundancy. This is a second-generation FSx for ONTAP file system.

For information about the use cases for Multi-AZ and Single-AZ deployments, refer to [Choosing Multi-AZ or Single-AZ file system deployment](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-multiAZ.html) .

EndpointIpAddressRange -> (string)

(Multi-AZ only) Specifies the IP address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API, Amazon FSx selects an unused IP address range for you from the 198.19.* range. By default in the Amazon FSx console, Amazon FSx chooses the last 64 IP addresses from the VPCâs primary CIDR range to use as the endpoint IP address range for the file system. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables.

Endpoints -> (structure)

The `Management` and `Intercluster` endpoints that are used to access data or to manage the file system using the NetApp ONTAP CLI, REST API, or NetApp SnapMirror.

Intercluster -> (structure)

An endpoint for managing your file system by setting up NetApp SnapMirror with other ONTAP systems.

DNSName -> (string)

The file systemâs DNS name. You can mount your file system using its DNS name.

IpAddresses -> (list)

IP addresses of the file system endpoint.

(string)

Management -> (structure)

An endpoint for managing your file system using the NetApp ONTAP CLI and NetApp ONTAP API.

DNSName -> (string)

The file systemâs DNS name. You can mount your file system using its DNS name.

IpAddresses -> (list)

IP addresses of the file system endpoint.

(string)

DiskIopsConfiguration -> (structure)

The SSD IOPS configuration for the ONTAP file system, specifying the number of provisioned IOPS and the provision mode.

Mode -> (string)

Specifies whether the file system is using the `AUTOMATIC` setting of SSD IOPS of 3 IOPS per GB of storage capacity, or if it using a `USER_PROVISIONED` value.

Iops -> (long)

The total number of SSD IOPS provisioned for the file system.

The minimum and maximum values for this property depend on the value of `HAPairs` and `StorageCapacity` . The minimum value is calculated as `StorageCapacity` * 3 * `HAPairs` (3 IOPS per GB of `StorageCapacity` ). The maximum value is calculated as 200,000 * `HAPairs` .

Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `Iops` is outside of the minimum or maximum values.

PreferredSubnetId -> (string)

The ID for a subnet. A *subnet* is a range of IP addresses in your virtual private cloud (VPC). For more information, see [VPC and subnets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) in the *Amazon VPC User Guide.*

RouteTableIds -> (list)

(Multi-AZ only) The VPC route tables in which your file systemâs endpoints are created.

(string)

ThroughputCapacity -> (integer)

The sustained throughput of an Amazon FSx file system in Megabytes per second (MBps).

WeeklyMaintenanceStartTime -> (string)

A recurring weekly time, in the format `D:HH:MM` .

`D` is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see [the ISO-8601 spec as described on Wikipedia](https://en.wikipedia.org/wiki/ISO_week_date) .

`HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour.

For example, `1:05:00` specifies maintenance at 5 AM Monday.

FsxAdminPassword -> (string)

You can use the `fsxadmin` user account to access the NetApp ONTAP CLI and REST API. The password value is always redacted in the response.

HAPairs -> (integer)

Specifies how many high-availability (HA) file server pairs the file system will have. The default value is 1. The value of this property affects the values of `StorageCapacity` , `Iops` , and `ThroughputCapacity` . For more information, see [High-availability (HA) pairs](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/HA-pairs.html) in the FSx for ONTAP user guide.

Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:

- The value of `HAPairs` is less than 1 or greater than 12.
- The value of `HAPairs` is greater than 1 and the value of `DeploymentType` is `SINGLE_AZ_1` , `MULTI_AZ_1` , or `MULTI_AZ_2` .

ThroughputCapacityPerHAPair -> (integer)

Use to choose the throughput capacity per HA pair. When the value of `HAPairs` is equal to 1, the value of `ThroughputCapacityPerHAPair` is the total throughput for the file system.

This field and `ThroughputCapacity` cannot be defined in the same API call, but one is required.

This field and `ThroughputCapacity` are the same for file systems with one HA pair.

- For `SINGLE_AZ_1` and `MULTI_AZ_1` file systems, valid values are 128, 256, 512, 1024, 2048, or 4096 MBps.
- For `SINGLE_AZ_2` , valid values are 1536, 3072, or 6144 MBps.
- For `MULTI_AZ_2` , valid values are 384, 768, 1536, 3072, or 6144 MBps.

Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:

- The value of `ThroughputCapacity` and `ThroughputCapacityPerHAPair` are not the same value.
- The value of deployment type is `SINGLE_AZ_2` and `ThroughputCapacity` / `ThroughputCapacityPerHAPair` is not a valid HA pair (a value between 1 and 12).
- The value of `ThroughputCapacityPerHAPair` is not a valid value.

FileSystemTypeVersion -> (string)

The Lustre version of the Amazon FSx for Lustre file system, which can be `2.10` , `2.12` , or `2.15` .

OpenZFSConfiguration -> (structure)

The configuration for this Amazon FSx for OpenZFS file system.

AutomaticBackupRetentionDays -> (integer)

The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30` .

CopyTagsToBackups -> (boolean)

A Boolean value indicating whether tags on the file system should be copied to backups. If itâs set to `true` , all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesnât specify any tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.

CopyTagsToVolumes -> (boolean)

A Boolean value indicating whether tags for the volume should be copied to snapshots. This value defaults to `false` . If itâs set to `true` , all tags for the volume are copied to snapshots where the user doesnât specify tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.

DailyAutomaticBackupStartTime -> (string)

A recurring daily time, in the format `HH:MM` . `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.

DeploymentType -> (string)

Specifies the file-system deployment type. Amazon FSx for OpenZFS supports `MULTI_AZ_1` , `SINGLE_AZ_HA_2` , `SINGLE_AZ_HA_1` , `SINGLE_AZ_2` , and `SINGLE_AZ_1` .

ThroughputCapacity -> (integer)

The throughput of an Amazon FSx file system, measured in megabytes per second (MBps).

WeeklyMaintenanceStartTime -> (string)

A recurring weekly time, in the format `D:HH:MM` .

`D` is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see [the ISO-8601 spec as described on Wikipedia](https://en.wikipedia.org/wiki/ISO_week_date) .

`HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour.

For example, `1:05:00` specifies maintenance at 5 AM Monday.

DiskIopsConfiguration -> (structure)

The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for NetApp ONTAP, Amazon FSx for Windows File Server, or FSx for OpenZFS file system. By default, Amazon FSx automatically provisions 3 IOPS per GB of storage capacity. You can provision additional IOPS per GB of storage. The configuration consists of the total number of provisioned SSD IOPS and how it is was provisioned, or the mode (by the customer or by Amazon FSx).

Mode -> (string)

Specifies whether the file system is using the `AUTOMATIC` setting of SSD IOPS of 3 IOPS per GB of storage capacity, or if it using a `USER_PROVISIONED` value.

Iops -> (long)

The total number of SSD IOPS provisioned for the file system.

The minimum and maximum values for this property depend on the value of `HAPairs` and `StorageCapacity` . The minimum value is calculated as `StorageCapacity` * 3 * `HAPairs` (3 IOPS per GB of `StorageCapacity` ). The maximum value is calculated as 200,000 * `HAPairs` .

Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `Iops` is outside of the minimum or maximum values.

RootVolumeId -> (string)

The ID of the root volume of the OpenZFS file system.

PreferredSubnetId -> (string)

Required when `DeploymentType` is set to `MULTI_AZ_1` . This specifies the subnet in which you want the preferred file server to be located.

EndpointIpAddressRange -> (string)

(Multi-AZ only) Specifies the IP address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API and Amazon FSx console, Amazon FSx selects an available /28 IP address range for you from one of the VPCâs CIDR ranges. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables.

RouteTableIds -> (list)

(Multi-AZ only) The VPC route tables in which your file systemâs endpoints are created.

(string)

EndpointIpAddress -> (string)

The IP address of the endpoint that is used to access data or to manage the file system.

ReadCacheConfiguration -> (structure)

Required when `StorageType` is set to `INTELLIGENT_TIERING` . Specifies the optional provisioned SSD read cache.

SizingMode -> (string)

Specifies how the provisioned SSD read cache is sized, as follows:

- Set to `NO_CACHE` if you do not want to use an SSD read cache with your Intelligent-Tiering file system.
- Set to `USER_PROVISIONED` to specify the exact size of your SSD read cache.
- Set to `PROPORTIONAL_TO_THROUGHPUT_CAPACITY` to have your SSD read cache automatically sized based on your throughput capacity.

SizeGiB -> (integer)

Required if `SizingMode` is set to `USER_PROVISIONED` . Specifies the size of the file systemâs SSD read cache, in gibibytes (GiB).

FailureDetails -> (structure)

Provides information about a failed administrative action.

Message -> (string)

Error message providing details about the failed administrative action.

TargetVolumeValues -> (structure)

Describes an Amazon FSx volume.

CreationTime -> (timestamp)

The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

FileSystemId -> (string)

The globally unique ID of the file system, assigned by Amazon FSx.

Lifecycle -> (string)

The lifecycle status of the volume.

- `AVAILABLE` - The volume is fully available for use.
- `CREATED` - The volume has been created.
- `CREATING` - Amazon FSx is creating the new volume.
- `DELETING` - Amazon FSx is deleting an existing volume.
- `FAILED` - Amazon FSx was unable to create the volume.
- `MISCONFIGURED` - The volume is in a failed but recoverable state.
- `PENDING` - Amazon FSx hasnât started creating the volume.

Name -> (string)

The name of the volume.

OntapConfiguration -> (structure)

The configuration of an Amazon FSx for NetApp ONTAP volume.

FlexCacheEndpointType -> (string)

Specifies the FlexCache endpoint type of the volume. Valid values are the following:

- `NONE` specifies that the volume doesnât have a FlexCache configuration. `NONE` is the default.
- `ORIGIN` specifies that the volume is the origin volume for a FlexCache volume.
- `CACHE` specifies that the volume is a FlexCache volume.

JunctionPath -> (string)

Specifies the directory that network-attached storage (NAS) clients use to mount the volume, along with the storage virtual machine (SVM) Domain Name System (DNS) name or IP address. You can create a `JunctionPath` directly below a parent volume junction or on a directory within a volume. A `JunctionPath` for a volume named `vol3` might be `/vol1/vol2/vol3` , or `/vol1/dir2/vol3` , or even `/dir1/dir2/vol3` .

SecurityStyle -> (string)

The security style for the volume, which can be `UNIX` , `NTFS` , or `MIXED` .

SizeInMegabytes -> (integer)

The configured size of the volume, in megabytes (MBs).

StorageEfficiencyEnabled -> (boolean)

The volumeâs storage efficiency setting.

StorageVirtualMachineId -> (string)

The ID of the volumeâs storage virtual machine.

StorageVirtualMachineRoot -> (boolean)

A Boolean flag indicating whether this volume is the root volume for its storage virtual machine (SVM). Only one volume on an SVM can be the root volume. This value defaults to `false` . If this value is `true` , then this is the SVM root volume.

This flag is useful when youâre deleting an SVM, because you must first delete all non-root volumes. This flag, when set to `false` , helps you identify which volumes to delete before you can delete the SVM.

TieringPolicy -> (structure)

The volumeâs `TieringPolicy` setting.

CoolingPeriod -> (integer)

Specifies the number of days that user data in a volume must remain inactive before it is considered âcoldâ and moved to the capacity pool. Used with the `AUTO` and `SNAPSHOT_ONLY` tiering policies. Enter a whole number between 2 and 183. Default values are 31 days for `AUTO` and 2 days for `SNAPSHOT_ONLY` .

Name -> (string)

Specifies the tiering policy used to transition data. Default value is `SNAPSHOT_ONLY` .

- `SNAPSHOT_ONLY` - moves cold snapshots to the capacity pool storage tier.
- `AUTO` - moves cold user data and snapshots to the capacity pool storage tier based on your access patterns.
- `ALL` - moves all user data blocks in both the active file system and Snapshot copies to the storage pool tier.
- `NONE` - keeps a volumeâs data in the primary storage tier, preventing it from being moved to the capacity pool tier.

UUID -> (string)

The volumeâs universally unique identifier (UUID).

OntapVolumeType -> (string)

Specifies the type of volume. Valid values are the following:

- `RW` specifies a read/write volume. `RW` is the default.
- `DP` specifies a data-protection volume. You can protect data by replicating it to data-protection mirror copies. If a disaster occurs, you can use these data-protection mirror copies to recover data.
- `LS` specifies a load-sharing mirror volume. A load-sharing mirror reduces the network traffic to a FlexVol volume by providing additional read-only access to clients.

SnapshotPolicy -> (string)

Specifies the snapshot policy for the volume. There are three built-in snapshot policies:

- `default` : This is the default policy. A maximum of six hourly snapshots taken five minutes past the hour. A maximum of two daily snapshots taken Monday through Saturday at 10 minutes after midnight. A maximum of two weekly snapshots taken every Sunday at 15 minutes after midnight.
- `default-1weekly` : This policy is the same as the `default` policy except that it only retains one snapshot from the weekly schedule.
- `none` : This policy does not take any snapshots. This policy can be assigned to volumes to prevent automatic snapshots from being taken.

You can also provide the name of a custom policy that you created with the ONTAP CLI or REST API.

For more information, see [Snapshot policies](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snapshots-ontap.html#snapshot-policies) in the Amazon FSx for NetApp ONTAP User Guide.

CopyTagsToBackups -> (boolean)

A boolean flag indicating whether tags for the volume should be copied to backups. This value defaults to false. If itâs set to true, all tags for the volume are copied to all automatic and user-initiated backups where the user doesnât specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the volume, regardless of this value.

SnaplockConfiguration -> (structure)

The SnapLock configuration object for an FSx for ONTAP SnapLock volume.

AuditLogVolume -> (boolean)

Enables or disables the audit log volume for an FSx for ONTAP SnapLock volume. The default value is `false` . If you set `AuditLogVolume` to `true` , the SnapLock volume is created as an audit log volume. The minimum retention period for an audit log volume is six months.

For more information, see [SnapLock audit log volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/how-snaplock-works.html#snaplock-audit-log-volume) .

AutocommitPeriod -> (structure)

The configuration object for setting the autocommit period of files in an FSx for ONTAP SnapLock volume.

Type -> (string)

Defines the type of time for the autocommit period of a file in an FSx for ONTAP SnapLock volume. Setting this value to `NONE` disables autocommit. The default value is `NONE` .

Value -> (integer)

Defines the amount of time for the autocommit period of a file in an FSx for ONTAP SnapLock volume. The following ranges are valid:

- `Minutes` : 5 - 65,535
- `Hours` : 1 - 65,535
- `Days` : 1 - 3,650
- `Months` : 1 - 120
- `Years` : 1 - 10

PrivilegedDelete -> (string)

Enables, disables, or permanently disables privileged delete on an FSx for ONTAP SnapLock Enterprise volume. Enabling privileged delete allows SnapLock administrators to delete write once, read many (WORM) files even if they have active retention periods. `PERMANENTLY_DISABLED` is a terminal state. If privileged delete is permanently disabled on a SnapLock volume, you canât re-enable it. The default value is `DISABLED` .

For more information, see [Privileged delete](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-enterprise.html#privileged-delete) .

RetentionPeriod -> (structure)

Specifies the retention period of an FSx for ONTAP SnapLock volume.

DefaultRetention -> (structure)

The retention period assigned to a write once, read many (WORM) file by default if an explicit retention period is not set for an FSx for ONTAP SnapLock volume. The default retention period must be greater than or equal to the minimum retention period and less than or equal to the maximum retention period.

Type -> (string)

Defines the type of time for the retention period of an FSx for ONTAP SnapLock volume. Set it to one of the valid types. If you set it to `INFINITE` , the files are retained forever. If you set it to `UNSPECIFIED` , the files are retained until you set an explicit retention period.

Value -> (integer)

Defines the amount of time for the retention period of an FSx for ONTAP SnapLock volume. You canât set a value for `INFINITE` or `UNSPECIFIED` . For all other options, the following ranges are valid:

- `Seconds` : 0 - 65,535
- `Minutes` : 0 - 65,535
- `Hours` : 0 - 24
- `Days` : 0 - 365
- `Months` : 0 - 12
- `Years` : 0 - 100

MinimumRetention -> (structure)

The shortest retention period that can be assigned to a WORM file on an FSx for ONTAP SnapLock volume.

Type -> (string)

Defines the type of time for the retention period of an FSx for ONTAP SnapLock volume. Set it to one of the valid types. If you set it to `INFINITE` , the files are retained forever. If you set it to `UNSPECIFIED` , the files are retained until you set an explicit retention period.

Value -> (integer)

Defines the amount of time for the retention period of an FSx for ONTAP SnapLock volume. You canât set a value for `INFINITE` or `UNSPECIFIED` . For all other options, the following ranges are valid:

- `Seconds` : 0 - 65,535
- `Minutes` : 0 - 65,535
- `Hours` : 0 - 24
- `Days` : 0 - 365
- `Months` : 0 - 12
- `Years` : 0 - 100

MaximumRetention -> (structure)

The longest retention period that can be assigned to a WORM file on an FSx for ONTAP SnapLock volume.

Type -> (string)

Defines the type of time for the retention period of an FSx for ONTAP SnapLock volume. Set it to one of the valid types. If you set it to `INFINITE` , the files are retained forever. If you set it to `UNSPECIFIED` , the files are retained until you set an explicit retention period.

Value -> (integer)

Defines the amount of time for the retention period of an FSx for ONTAP SnapLock volume. You canât set a value for `INFINITE` or `UNSPECIFIED` . For all other options, the following ranges are valid:

- `Seconds` : 0 - 65,535
- `Minutes` : 0 - 65,535
- `Hours` : 0 - 24
- `Days` : 0 - 365
- `Months` : 0 - 12
- `Years` : 0 - 100

SnaplockType -> (string)

Specifies the retention mode of an FSx for ONTAP SnapLock volume. After it is set, it canât be changed. You can choose one of the following retention modes:

- `COMPLIANCE` : Files transitioned to write once, read many (WORM) on a Compliance volume canât be deleted until their retention periods expire. This retention mode is used to address government or industry-specific mandates or to protect against ransomware attacks. For more information, see [SnapLock Compliance](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-compliance.html) .
- `ENTERPRISE` : Files transitioned to WORM on an Enterprise volume can be deleted by authorized users before their retention periods expire using privileged delete. This retention mode is used to advance an organizationâs data integrity and internal compliance or to test retention settings before using SnapLock Compliance. For more information, see [SnapLock Enterprise](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-enterprise.html) .

VolumeAppendModeEnabled -> (boolean)

Enables or disables volume-append mode on an FSx for ONTAP SnapLock volume. Volume-append mode allows you to create WORM-appendable files and write data to them incrementally. The default value is `false` .

For more information, see [Volume-append mode](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/worm-state.html#worm-state-append) .

VolumeStyle -> (string)

Use to specify the style of an ONTAP volume. For more information about FlexVols and FlexGroups, see [Volume types](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/volume-types.html) in Amazon FSx for NetApp ONTAP User Guide.

AggregateConfiguration -> (structure)

This structure specifies configuration options for a volumeâs storage aggregate or aggregates.

Aggregates -> (list)

The list of aggregates that this volume resides on. Aggregates are storage pools which make up your primary storage tier. Each high-availability (HA) pair has one aggregate. The names of the aggregates map to the names of the aggregates in the ONTAP CLI and REST API. For FlexVols, there will always be a single entry.

Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:

- The strings in the value of `Aggregates` are not are not formatted as `aggrX` , where X is a number between 1 and 12.
- The value of `Aggregates` contains aggregates that are not present.
- One or more of the aggregates supplied are too close to the volume limit to support adding more volumes.

(string)

TotalConstituents -> (integer)

The total number of constituents this FlexGroup volume has. Not applicable for FlexVols.

SizeInBytes -> (long)

The configured size of the volume, in bytes.

ResourceARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

Tags -> (list)

A list of `Tag` values, with a maximum of 50 elements.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

VolumeId -> (string)

The system-generated, unique ID of the volume.

VolumeType -> (string)

The type of the volume.

LifecycleTransitionReason -> (structure)

The reason why the volume lifecycle status changed.

Message -> (string)

A detailed error message.

AdministrativeActions -> (list)

A list of administrative actions for the volume that are in process or waiting to be processed. Administrative actions describe changes to the volume that you have initiated using the `UpdateVolume` action.

(structure)

Describes a specific Amazon FSx administrative action for the current Windows, Lustre, OpenZFS, or ONTAP file system or volume.

AdministrativeActionType -> (string)

Describes the type of administrative action, as follows:

- `FILE_SYSTEM_UPDATE` - A file system update administrative action initiated from the Amazon FSx console, API (`UpdateFileSystem` ), or CLI (`update-file-system` ).
- `THROUGHPUT_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file systemâs throughput capacity has been completed successfully, a `THROUGHPUT_OPTIMIZATION` task starts. You can track the storage-optimization progress using the `ProgressPercent` property. When `THROUGHPUT_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED` . For more information, see [Managing throughput capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-throughput-capacity.html) in the *Amazon FSx for Windows File Server User Guide* .
- `STORAGE_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file systemâs storage capacity has completed successfully, a `STORAGE_OPTIMIZATION` task starts.
- For Windows and ONTAP, storage optimization is the process of migrating the file system data to newer larger disks.
- For Lustre, storage optimization consists of rebalancing the data across the existing and newly added file servers.

You can track the storage-optimization progress using the `ProgressPercent` property. When `STORAGE_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED` . For more information, see [Managing storage capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-capacity.html) in the *Amazon FSx for Windows File Server User Guide* , [Managing storage capacity](https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-storage-capacity.html) in the *Amazon FSx for Lustre User Guide* , and [Managing storage capacity and provisioned IOPS](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-storage-capacity.html) in the *Amazon FSx for NetApp ONTAP User Guide* .

- `FILE_SYSTEM_ALIAS_ASSOCIATION` - A file system update to associate a new Domain Name System (DNS) alias with the file system. For more information, see [AssociateFileSystemAliases](https://docs.aws.amazon.com/fsx/latest/APIReference/API_AssociateFileSystemAliases.html) .
- `FILE_SYSTEM_ALIAS_DISASSOCIATION` - A file system update to disassociate a DNS alias from the file system. For more information, see [DisassociateFileSystemAliases](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DisassociateFileSystemAliases.html) .
- `IOPS_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file systemâs throughput capacity has been completed successfully, a `IOPS_OPTIMIZATION` task starts. You can track the storage-optimization progress using the `ProgressPercent` property. When `IOPS_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED` . For more information, see [Managing provisioned SSD IOPS](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-provisioned-ssd-iops.html) in the Amazon FSx for Windows File Server User Guide.
- `STORAGE_TYPE_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file systemâs throughput capacity has been completed successfully, a `STORAGE_TYPE_OPTIMIZATION` task starts. You can track the storage-optimization progress using the `ProgressPercent` property. When `STORAGE_TYPE_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED` .
- `VOLUME_UPDATE` - A volume update to an Amazon FSx for OpenZFS volume initiated from the Amazon FSx console, API (`UpdateVolume` ), or CLI (`update-volume` ).
- `VOLUME_RESTORE` - An Amazon FSx for OpenZFS volume is returned to the state saved by the specified snapshot, initiated from an API (`RestoreVolumeFromSnapshot` ) or CLI (`restore-volume-from-snapshot` ).
- `SNAPSHOT_UPDATE` - A snapshot update to an Amazon FSx for OpenZFS volume initiated from the Amazon FSx console, API (`UpdateSnapshot` ), or CLI (`update-snapshot` ).
- `RELEASE_NFS_V3_LOCKS` - Tracks the release of Network File System (NFS) V3 locks on an Amazon FSx for OpenZFS file system.
- `DOWNLOAD_DATA_FROM_BACKUP` - An FSx for ONTAP backup is being restored to a new volume on a second-generation file system. Once the all the file metadata is loaded onto the volume, you can mount the volume with read-only access. during this process.
- `VOLUME_INITIALIZE_WITH_SNAPSHOT` - A volume is being created from a snapshot on a different FSx for OpenZFS file system. You can initiate this from the Amazon FSx console, API (`CreateVolume` ), or CLI (`create-volume` ) when using the using the `FULL_COPY` strategy.
- `VOLUME_UPDATE_WITH_SNAPSHOT` - A volume is being updated from a snapshot on a different FSx for OpenZFS file system. You can initiate this from the Amazon FSx console, API (`CopySnapshotAndUpdateVolume` ), or CLI (`copy-snapshot-and-update-volume` ).

ProgressPercent -> (integer)

The percentage-complete status of a `STORAGE_OPTIMIZATION` or `DOWNLOAD_DATA_FROM_BACKUP` administrative action. Does not apply to any other administrative action type.

RequestTime -> (timestamp)

The time that the administrative action request was received.

Status -> (string)

The status of the administrative action, as follows:

- `FAILED` - Amazon FSx failed to process the administrative action successfully.
- `IN_PROGRESS` - Amazon FSx is processing the administrative action.
- `PENDING` - Amazon FSx is waiting to process the administrative action.
- `COMPLETED` - Amazon FSx has finished processing the administrative task. For a backup restore to a second-generation FSx for ONTAP file system, indicates that all data has been downloaded to the volume, and clients now have read-write access to volume.
- `UPDATED_OPTIMIZING` - For a storage-capacity increase update, Amazon FSx has updated the file system with the new storage capacity, and is now performing the storage-optimization process.
- `PENDING` - For a backup restore to a second-generation FSx for ONTAP file system, indicates that the file metadata is being downloaded onto the volume. The volumeâs Lifecycle state is CREATING.
- `IN_PROGRESS` - For a backup restore to a second-generation FSx for ONTAP file system, indicates that all metadata has been downloaded to the new volume and client can access data with read-only access while Amazon FSx downloads the file data to the volume. Track the progress of this process with the `ProgressPercent` element.

TargetFileSystemValues -> (structure)

The target value for the administration action, provided in the `UpdateFileSystem` operation. Returned for `FILE_SYSTEM_UPDATE` administrative actions.

OwnerId -> (string)

The Amazon Web Services account that created the file system. If the file system was created by a user in IAM Identity Center, the Amazon Web Services account to which the IAM user belongs is the owner.

CreationTime -> (timestamp)

The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

FileSystemId -> (string)

The system-generated, unique 17-digit ID of the file system.

FileSystemType -> (string)

The type of Amazon FSx file system, which can be `LUSTRE` , `WINDOWS` , `ONTAP` , or `OPENZFS` .

Lifecycle -> (string)

The lifecycle status of the file system. The following are the possible values and what they mean:

- `AVAILABLE` - The file system is in a healthy state, and is reachable and available for use.
- `CREATING` - Amazon FSx is creating the new file system.
- `DELETING` - Amazon FSx is deleting an existing file system.
- `FAILED` - An existing file system has experienced an unrecoverable failure. When creating a new file system, Amazon FSx was unable to create the file system.
- `MISCONFIGURED` - The file system is in a failed but recoverable state.
- `MISCONFIGURED_UNAVAILABLE` - (Amazon FSx for Windows File Server only) The file system is currently unavailable due to a change in your Active Directory configuration.
- `UPDATING` - The file system is undergoing a customer-initiated update.

FailureDetails -> (structure)

A structure providing details of any failures that occurred.

Message -> (string)

A message describing any failures that occurred.

StorageCapacity -> (integer)

The storage capacity of the file system in gibibytes (GiB).

Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `StorageCapacity` is outside of the minimum or maximum values.

StorageType -> (string)

The type of storage the file system is using. If set to `SSD` , the file system uses solid state drive storage. If set to `HDD` , the file system uses hard disk drive storage.

VpcId -> (string)

The ID of the primary virtual private cloud (VPC) for the file system.

SubnetIds -> (list)

Specifies the IDs of the subnets that the file system is accessible from. For the Amazon FSx Windows and ONTAP `MULTI_AZ_1` file system deployment type, there are two subnet IDs, one for the preferred file server and one for the standby file server. The preferred file server subnet identified in the `PreferredSubnetID` property. All other file systems have only one subnet ID.

For FSx for Lustre file systems, and Single-AZ Windows file systems, this is the ID of the subnet that contains the file systemâs endpoint. For `MULTI_AZ_1` Windows and ONTAP file systems, the file system endpoint is available in the `PreferredSubnetID` .

(string)

The ID for a subnet. A *subnet* is a range of IP addresses in your virtual private cloud (VPC). For more information, see [VPC and subnets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) in the *Amazon VPC User Guide.*

NetworkInterfaceIds -> (list)

The IDs of the elastic network interfaces from which a specific file system is accessible. The elastic network interface is automatically created in the same virtual private cloud (VPC) that the Amazon FSx file system was created in. For more information, see [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the *Amazon EC2 User Guide.*

For an Amazon FSx for Windows File Server file system, you can have one network interface ID. For an Amazon FSx for Lustre file system, you can have more than one.

(string)

An elastic network interface ID. An elastic network interface is a logical networking component in a virtual private cloud (VPC) that represents a virtual network card. For more information, see [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the *Amazon EC2 User Guide for Linux Instances* .

DNSName -> (string)

The Domain Name System (DNS) name for the file system.

KmsKeyId -> (string)

The ID of the Key Management Service (KMS) key used to encrypt Amazon FSx file system data. Used as follows with Amazon FSx file system types:

- Amazon FSx for Lustre `PERSISTENT_1` and `PERSISTENT_2` deployment types only.  `SCRATCH_1` and `SCRATCH_2` types are encrypted using the Amazon FSx service KMS key for your account.
- Amazon FSx for NetApp ONTAP
- Amazon FSx for OpenZFS
- Amazon FSx for Windows File Server

ResourceARN -> (string)

The Amazon Resource Name (ARN) of the file system resource.

Tags -> (list)

The tags to associate with the file system. For more information, see [Tagging your Amazon FSx resources](https://docs.aws.amazon.com/fsx/latest/LustreGuide/tag-resources.html) in the *Amazon FSx for Lustre User Guide* .

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

WindowsConfiguration -> (structure)

The configuration for this Amazon FSx for Windows File Server file system.

ActiveDirectoryId -> (string)

The ID for an existing Amazon Web Services Managed Microsoft Active Directory instance that the file system is joined to.

SelfManagedActiveDirectoryConfiguration -> (structure)

The configuration of the self-managed Microsoft Active Directory (AD) directory to which the Windows File Server or ONTAP storage virtual machine (SVM) instance is joined.

DomainName -> (string)

The fully qualified domain name of the self-managed AD directory.

OrganizationalUnitDistinguishedName -> (string)

The fully qualified distinguished name of the organizational unit within the self-managed AD directory to which the Windows File Server or ONTAP storage virtual machine (SVM) instance is joined.

FileSystemAdministratorsGroup -> (string)

The name of the domain group whose members have administrative privileges for the FSx file system.

UserName -> (string)

The user name for the service account on your self-managed AD domain that FSx uses to join to your AD domain.

DnsIps -> (list)

A list of up to three IP addresses of DNS servers or domain controllers in the self-managed AD directory.

(string)

DeploymentType -> (string)

Specifies the file system deployment type, valid values are the following:

- `MULTI_AZ_1` - Specifies a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability, and supports SSD and HDD storage.
- `SINGLE_AZ_1` - (Default) Specifies a file system that is configured for single AZ redundancy, only supports SSD storage.
- `SINGLE_AZ_2` - Latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports SSD and HDD storage.

For more information, see [Single-AZ and Multi-AZ File Systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html) .

RemoteAdministrationEndpoint -> (string)

For `MULTI_AZ_1` deployment types, use this endpoint when performing administrative tasks on the file system using Amazon FSx Remote PowerShell.

For `SINGLE_AZ_1` and `SINGLE_AZ_2` deployment types, this is the DNS name of the file system.

This endpoint is temporarily unavailable when the file system is undergoing maintenance.

PreferredSubnetId -> (string)

For `MULTI_AZ_1` deployment types, it specifies the ID of the subnet where the preferred file server is located. Must be one of the two subnet IDs specified in `SubnetIds` property. Amazon FSx serves traffic from this subnet except in the event of a failover to the secondary file server.

For `SINGLE_AZ_1` and `SINGLE_AZ_2` deployment types, this value is the same as that for `SubnetIDs` . For more information, see [Availability and durability: Single-AZ and Multi-AZ file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html#single-multi-az-resources) .

PreferredFileServerIp -> (string)

For `MULTI_AZ_1` deployment types, the IP address of the primary, or preferred, file server.

Use this IP address when mounting the file system on Linux SMB clients or Windows SMB clients that are not joined to a Microsoft Active Directory. Applicable for all Windows file system deployment types. This IP address is temporarily unavailable when the file system is undergoing maintenance. For Linux and Windows SMB clients that are joined to an Active Directory, use the file systemâs DNSName instead. For more information on mapping and mounting file shares, see [Accessing File Shares](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/accessing-file-shares.html) .

ThroughputCapacity -> (integer)

The throughput of the Amazon FSx file system, measured in megabytes per second.

MaintenanceOperationsInProgress -> (list)

The list of maintenance operations in progress for this file system.

(string)

An enumeration specifying the currently ongoing maintenance operation.

WeeklyMaintenanceStartTime -> (string)

The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone. d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.

DailyAutomaticBackupStartTime -> (string)

The preferred time to take daily automatic backups, in the UTC time zone.

AutomaticBackupRetentionDays -> (integer)

The number of days to retain automatic backups. Setting this to 0 disables automatic backups. You can retain automatic backups for a maximum of 90 days.

CopyTagsToBackups -> (boolean)

A boolean flag indicating whether tags on the file system should be copied to backups. This value defaults to false. If itâs set to true, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesnât specify any tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.

Aliases -> (list)

An array of one or more DNS aliases that are currently associated with the Amazon FSx file system. Aliases allow you to use existing DNS names to access the data in your Amazon FSx file system. You can associate up to 50 aliases with a file system at any time. You can associate additional DNS aliases after you create the file system using the AssociateFileSystemAliases operation. You can remove DNS aliases from the file system after it is created using the DisassociateFileSystemAliases operation. You only need to specify the alias name in the request payload. For more information, see [DNS aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html) .

(structure)

A DNS alias that is associated with the file system. You can use a DNS alias to access a file system using user-defined DNS names, in addition to the default DNS name that Amazon FSx assigns to the file system. For more information, see [DNS aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html) in the *FSx for Windows File Server User Guide* .

Name -> (string)

The name of the DNS alias. The alias name has to meet the following requirements:

- Formatted as a fully-qualified domain name (FQDN), `hostname.domain` , for example, `accounting.example.com` .
- Can contain alphanumeric characters, the underscore (_), and the hyphen (-).
- Cannot start or end with a hyphen.
- Can start with a numeric.

For DNS names, Amazon FSx stores alphabetic characters as lowercase letters (a-z), regardless of how you specify them: as uppercase letters, lowercase letters, or the corresponding letters in escape codes.

Lifecycle -> (string)

Describes the state of the DNS alias.

- AVAILABLE - The DNS alias is associated with an Amazon FSx file system.
- CREATING - Amazon FSx is creating the DNS alias and associating it with the file system.
- CREATE_FAILED - Amazon FSx was unable to associate the DNS alias with the file system.
- DELETING - Amazon FSx is disassociating the DNS alias from the file system and deleting it.
- DELETE_FAILED - Amazon FSx was unable to disassociate the DNS alias from the file system.

AuditLogConfiguration -> (structure)

The configuration that Amazon FSx for Windows File Server uses to audit and log user accesses of files, folders, and file shares on the Amazon FSx for Windows File Server file system.

FileAccessAuditLogLevel -> (string)

Sets which attempt type is logged by Amazon FSx for file and folder accesses.

- `SUCCESS_ONLY` - only successful attempts to access files or folders are logged.
- `FAILURE_ONLY` - only failed attempts to access files or folders are logged.
- `SUCCESS_AND_FAILURE` - both successful attempts and failed attempts to access files or folders are logged.
- `DISABLED` - access auditing of files and folders is turned off.

FileShareAccessAuditLogLevel -> (string)

Sets which attempt type is logged by Amazon FSx for file share accesses.

- `SUCCESS_ONLY` - only successful attempts to access file shares are logged.
- `FAILURE_ONLY` - only failed attempts to access file shares are logged.
- `SUCCESS_AND_FAILURE` - both successful attempts and failed attempts to access file shares are logged.
- `DISABLED` - access auditing of file shares is turned off.

AuditLogDestination -> (string)

The Amazon Resource Name (ARN) for the destination of the audit logs. The destination can be any Amazon CloudWatch Logs log group ARN or Amazon Kinesis Data Firehose delivery stream ARN.

The name of the Amazon CloudWatch Logs log group must begin with the `/aws/fsx` prefix. The name of the Amazon Kinesis Data Firehose delivery stream must begin with the `aws-fsx` prefix.

The destination ARN (either CloudWatch Logs log group or Kinesis Data Firehose delivery stream) must be in the same Amazon Web Services partition, Amazon Web Services Region, and Amazon Web Services account as your Amazon FSx file system.

DiskIopsConfiguration -> (structure)

The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for Windows file system. By default, Amazon FSx automatically provisions 3 IOPS per GiB of storage capacity. You can provision additional IOPS per GiB of storage, up to the maximum limit associated with your chosen throughput capacity.

Mode -> (string)

Specifies whether the file system is using the `AUTOMATIC` setting of SSD IOPS of 3 IOPS per GB of storage capacity, or if it using a `USER_PROVISIONED` value.

Iops -> (long)

The total number of SSD IOPS provisioned for the file system.

The minimum and maximum values for this property depend on the value of `HAPairs` and `StorageCapacity` . The minimum value is calculated as `StorageCapacity` * 3 * `HAPairs` (3 IOPS per GB of `StorageCapacity` ). The maximum value is calculated as 200,000 * `HAPairs` .

Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `Iops` is outside of the minimum or maximum values.

LustreConfiguration -> (structure)

The configuration for the Amazon FSx for Lustre file system.

WeeklyMaintenanceStartTime -> (string)

The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone. Here, `d` is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.

DataRepositoryConfiguration -> (structure)

The data repository configuration object for Lustre file systems returned in the response of the `CreateFileSystem` operation.

This data type is not supported on file systems with a data repository association. For file systems with a data repository association, see .

Lifecycle -> (string)

Describes the state of the file systemâs S3 durable data repository, if it is configured with an S3 repository. The lifecycle can have the following values:

- `CREATING` - The data repository configuration between the FSx file system and the linked S3 data repository is being created. The data repository is unavailable.
- `AVAILABLE` - The data repository is available for use.
- `MISCONFIGURED` - Amazon FSx cannot automatically import updates from the S3 bucket until the data repository configuration is corrected. For more information, see [Troubleshooting a Misconfigured linked S3 bucket](https://docs.aws.amazon.com/fsx/latest/LustreGuide/troubleshooting.html#troubleshooting-misconfigured-data-repository) .
- `UPDATING` - The data repository is undergoing a customer initiated update and availability may be impacted.
- `FAILED` - The data repository is in a terminal state that cannot be recovered.

ImportPath -> (string)

The import path to the Amazon S3 bucket (and optional prefix) that youâre using as the data repository for your FSx for Lustre file system, for example `s3://import-bucket/optional-prefix` . If a prefix is specified after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system.

ExportPath -> (string)

The export path to the Amazon S3 bucket (and prefix) that you are using to store new and changed Lustre file system files in S3.

ImportedFileChunkSize -> (integer)

For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.

The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.

AutoImportPolicy -> (string)

Describes the file systemâs linked S3 data repositoryâs `AutoImportPolicy` . The AutoImportPolicy configures how Amazon FSx keeps your file and directory listings up to date as you add or modify objects in your linked S3 bucket. `AutoImportPolicy` can have the following values:

- `NONE` - (Default) AutoImport is off. Amazon FSx only updates file and directory listings from the linked S3 bucket when the file system is created. FSx does not update file and directory listings for any new or changed objects after choosing this option.
- `NEW` - AutoImport is on. Amazon FSx automatically imports directory listings of any new objects added to the linked S3 bucket that do not currently exist in the FSx file system.
- `NEW_CHANGED` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket and any existing objects that are changed in the S3 bucket after you choose this option.
- `NEW_CHANGED_DELETED` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket, any existing objects that are changed in the S3 bucket, and any objects that were deleted in the S3 bucket.

FailureDetails -> (structure)

Provides detailed information about the data repository if its `Lifecycle` is set to `MISCONFIGURED` or `FAILED` .

Message -> (string)

A detailed error message.

DeploymentType -> (string)

The deployment type of the FSx for Lustre file system. *Scratch deployment type* is designed for temporary storage and shorter-term processing of data.

`SCRATCH_1` and `SCRATCH_2` deployment types are best suited for when you need temporary storage and shorter-term processing of data. The `SCRATCH_2` deployment type provides in-transit encryption of data and higher burst throughput capacity than `SCRATCH_1` .

The `PERSISTENT_1` and `PERSISTENT_2` deployment type is used for longer-term storage and workloads and encryption of data in transit. `PERSISTENT_2` offers higher `PerUnitStorageThroughput` (up to 1000 MB/s/TiB) along with a lower minimum storage capacity requirement (600 GiB). To learn more about FSx for Lustre deployment types, see [FSx for Lustre deployment options](https://docs.aws.amazon.com/fsx/latest/LustreGuide/lustre-deployment-types.html) .

The default is `SCRATCH_1` .

PerUnitStorageThroughput -> (integer)

Per unit storage throughput represents the megabytes per second of read or write throughput per 1 tebibyte of storage provisioned. File system throughput capacity is equal to Storage capacity (TiB) * PerUnitStorageThroughput (MB/s/TiB). This option is only valid for `PERSISTENT_1` and `PERSISTENT_2` deployment types.

Valid values:

- For `PERSISTENT_1` SSD storage: 50, 100, 200.
- For `PERSISTENT_1` HDD storage: 12, 40.
- For `PERSISTENT_2` SSD storage: 125, 250, 500, 1000.

MountName -> (string)

You use the `MountName` value when mounting the file system.

For the `SCRATCH_1` deployment type, this value is always â`fsx` â. For `SCRATCH_2` , `PERSISTENT_1` , and `PERSISTENT_2` deployment types, this value is a string that is unique within an Amazon Web Services Region.

DailyAutomaticBackupStartTime -> (string)

A recurring daily time, in the format `HH:MM` . `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.

AutomaticBackupRetentionDays -> (integer)

The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30` .

CopyTagsToBackups -> (boolean)

A boolean flag indicating whether tags on the file system are copied to backups. If itâs set to true, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesnât specify any tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value. (Default = false)

DriveCacheType -> (string)

The type of drive cache used by `PERSISTENT_1` file systems that are provisioned with HDD storage devices. This parameter is required when `StorageType` is HDD. When set to `READ` the file system has an SSD storage cache that is sized to 20% of the file systemâs storage capacity. This improves the performance for frequently accessed files by caching up to 20% of the total storage capacity.

This parameter is required when `StorageType` is set to HDD.

DataCompressionType -> (string)

The data compression configuration for the file system. `DataCompressionType` can have the following values:

- `NONE` - Data compression is turned off for the file system.
- `LZ4` - Data compression is turned on with the LZ4 algorithm.

For more information, see [Lustre data compression](https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-compression.html) .

LogConfiguration -> (structure)

The Lustre logging configuration. Lustre logging writes the enabled log events for your file system to Amazon CloudWatch Logs.

Level -> (string)

The data repository events that are logged by Amazon FSx.

- `WARN_ONLY` - only warning events are logged.
- `ERROR_ONLY` - only error events are logged.
- `WARN_ERROR` - both warning events and error events are logged.
- `DISABLED` - logging of data repository events is turned off.

Note that Amazon File Cache uses a default setting of `WARN_ERROR` , which canât be changed.

Destination -> (string)

The Amazon Resource Name (ARN) that specifies the destination of the logs. The destination can be any Amazon CloudWatch Logs log group ARN. The destination ARN must be in the same Amazon Web Services partition, Amazon Web Services Region, and Amazon Web Services account as your Amazon FSx file system.

RootSquashConfiguration -> (structure)

The Lustre root squash configuration for an Amazon FSx for Lustre file system. When enabled, root squash restricts root-level access from clients that try to access your file system as a root user.

RootSquash -> (string)

You enable root squash by setting a user ID (UID) and group ID (GID) for the file system in the format `UID:GID` (for example, `365534:65534` ). The UID and GID values can range from `0` to `4294967294` :

- A non-zero value for UID and GID enables root squash. The UID and GID values can be different, but each must be a non-zero value.
- A value of `0` (zero) for UID and GID indicates root, and therefore disables root squash.

When root squash is enabled, the user ID and group ID of a root user accessing the file system are re-mapped to the UID and GID you provide.

NoSquashNids -> (list)

When root squash is enabled, you can optionally specify an array of NIDs of clients for which root squash does not apply. A client NID is a Lustre Network Identifier used to uniquely identify a client. You can specify the NID as either a single address or a range of addresses:

- A single address is described in standard Lustre NID format by specifying the clientâs IP address followed by the Lustre network ID (for example, `10.0.1.6@tcp` ).
- An address range is described using a dash to separate the range (for example, `10.0.[2-10].[1-255]@tcp` ).

(string)

MetadataConfiguration -> (structure)

The Lustre metadata performance configuration for an Amazon FSx for Lustre file system using a `PERSISTENT_2` deployment type.

Iops -> (integer)

The number of Metadata IOPS provisioned for the file system. Valid values are `1500` , `3000` , `6000` , `12000` , and multiples of `12000` up to a maximum of `192000` .

Mode -> (string)

The metadata configuration mode for provisioning Metadata IOPS for the file system.

- In AUTOMATIC mode, FSx for Lustre automatically provisions and scales the number of Metadata IOPS on your file system based on your file system storage capacity.
- In USER_PROVISIONED mode, you can choose to specify the number of Metadata IOPS to provision for your file system.

EfaEnabled -> (boolean)

Specifies whether Elastic Fabric Adapter (EFA) and GPUDirect Storage (GDS) support is enabled for the Amazon FSx for Lustre file system.

OntapConfiguration -> (structure)

The configuration for this Amazon FSx for NetApp ONTAP file system.

AutomaticBackupRetentionDays -> (integer)

The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30` .

DailyAutomaticBackupStartTime -> (string)

A recurring daily time, in the format `HH:MM` . `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.

DeploymentType -> (string)

Specifies the FSx for ONTAP file system deployment type in use in the file system.

- `MULTI_AZ_1` - A high availability file system configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability. This is a first-generation FSx for ONTAP file system.
- `MULTI_AZ_2` - A high availability file system configured for Multi-AZ redundancy to tolerate temporary AZ unavailability. This is a second-generation FSx for ONTAP file system.
- `SINGLE_AZ_1` - A file system configured for Single-AZ redundancy. This is a first-generation FSx for ONTAP file system.
- `SINGLE_AZ_2` - A file system configured with multiple high-availability (HA) pairs for Single-AZ redundancy. This is a second-generation FSx for ONTAP file system.

For information about the use cases for Multi-AZ and Single-AZ deployments, refer to [Choosing Multi-AZ or Single-AZ file system deployment](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-multiAZ.html) .

EndpointIpAddressRange -> (string)

(Multi-AZ only) Specifies the IP address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API, Amazon FSx selects an unused IP address range for you from the 198.19.* range. By default in the Amazon FSx console, Amazon FSx chooses the last 64 IP addresses from the VPCâs primary CIDR range to use as the endpoint IP address range for the file system. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables.

Endpoints -> (structure)

The `Management` and `Intercluster` endpoints that are used to access data or to manage the file system using the NetApp ONTAP CLI, REST API, or NetApp SnapMirror.

Intercluster -> (structure)

An endpoint for managing your file system by setting up NetApp SnapMirror with other ONTAP systems.

DNSName -> (string)

The file systemâs DNS name. You can mount your file system using its DNS name.

IpAddresses -> (list)

IP addresses of the file system endpoint.

(string)

Management -> (structure)

An endpoint for managing your file system using the NetApp ONTAP CLI and NetApp ONTAP API.

DNSName -> (string)

The file systemâs DNS name. You can mount your file system using its DNS name.

IpAddresses -> (list)

IP addresses of the file system endpoint.

(string)

DiskIopsConfiguration -> (structure)

The SSD IOPS configuration for the ONTAP file system, specifying the number of provisioned IOPS and the provision mode.

Mode -> (string)

Specifies whether the file system is using the `AUTOMATIC` setting of SSD IOPS of 3 IOPS per GB of storage capacity, or if it using a `USER_PROVISIONED` value.

Iops -> (long)

The total number of SSD IOPS provisioned for the file system.

The minimum and maximum values for this property depend on the value of `HAPairs` and `StorageCapacity` . The minimum value is calculated as `StorageCapacity` * 3 * `HAPairs` (3 IOPS per GB of `StorageCapacity` ). The maximum value is calculated as 200,000 * `HAPairs` .

Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `Iops` is outside of the minimum or maximum values.

PreferredSubnetId -> (string)

The ID for a subnet. A *subnet* is a range of IP addresses in your virtual private cloud (VPC). For more information, see [VPC and subnets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) in the *Amazon VPC User Guide.*

RouteTableIds -> (list)

(Multi-AZ only) The VPC route tables in which your file systemâs endpoints are created.

(string)

ThroughputCapacity -> (integer)

The sustained throughput of an Amazon FSx file system in Megabytes per second (MBps).

WeeklyMaintenanceStartTime -> (string)

A recurring weekly time, in the format `D:HH:MM` .

`D` is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see [the ISO-8601 spec as described on Wikipedia](https://en.wikipedia.org/wiki/ISO_week_date) .

`HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour.

For example, `1:05:00` specifies maintenance at 5 AM Monday.

FsxAdminPassword -> (string)

You can use the `fsxadmin` user account to access the NetApp ONTAP CLI and REST API. The password value is always redacted in the response.

HAPairs -> (integer)

Specifies how many high-availability (HA) file server pairs the file system will have. The default value is 1. The value of this property affects the values of `StorageCapacity` , `Iops` , and `ThroughputCapacity` . For more information, see [High-availability (HA) pairs](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/HA-pairs.html) in the FSx for ONTAP user guide.

Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:

- The value of `HAPairs` is less than 1 or greater than 12.
- The value of `HAPairs` is greater than 1 and the value of `DeploymentType` is `SINGLE_AZ_1` , `MULTI_AZ_1` , or `MULTI_AZ_2` .

ThroughputCapacityPerHAPair -> (integer)

Use to choose the throughput capacity per HA pair. When the value of `HAPairs` is equal to 1, the value of `ThroughputCapacityPerHAPair` is the total throughput for the file system.

This field and `ThroughputCapacity` cannot be defined in the same API call, but one is required.

This field and `ThroughputCapacity` are the same for file systems with one HA pair.

- For `SINGLE_AZ_1` and `MULTI_AZ_1` file systems, valid values are 128, 256, 512, 1024, 2048, or 4096 MBps.
- For `SINGLE_AZ_2` , valid values are 1536, 3072, or 6144 MBps.
- For `MULTI_AZ_2` , valid values are 384, 768, 1536, 3072, or 6144 MBps.

Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:

- The value of `ThroughputCapacity` and `ThroughputCapacityPerHAPair` are not the same value.
- The value of deployment type is `SINGLE_AZ_2` and `ThroughputCapacity` / `ThroughputCapacityPerHAPair` is not a valid HA pair (a value between 1 and 12).
- The value of `ThroughputCapacityPerHAPair` is not a valid value.

FileSystemTypeVersion -> (string)

The Lustre version of the Amazon FSx for Lustre file system, which can be `2.10` , `2.12` , or `2.15` .

OpenZFSConfiguration -> (structure)

The configuration for this Amazon FSx for OpenZFS file system.

AutomaticBackupRetentionDays -> (integer)

The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30` .

CopyTagsToBackups -> (boolean)

A Boolean value indicating whether tags on the file system should be copied to backups. If itâs set to `true` , all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesnât specify any tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.

CopyTagsToVolumes -> (boolean)

A Boolean value indicating whether tags for the volume should be copied to snapshots. This value defaults to `false` . If itâs set to `true` , all tags for the volume are copied to snapshots where the user doesnât specify tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.

DailyAutomaticBackupStartTime -> (string)

A recurring daily time, in the format `HH:MM` . `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.

DeploymentType -> (string)

Specifies the file-system deployment type. Amazon FSx for OpenZFS supports `MULTI_AZ_1` , `SINGLE_AZ_HA_2` , `SINGLE_AZ_HA_1` , `SINGLE_AZ_2` , and `SINGLE_AZ_1` .

ThroughputCapacity -> (integer)

The throughput of an Amazon FSx file system, measured in megabytes per second (MBps).

WeeklyMaintenanceStartTime -> (string)

A recurring weekly time, in the format `D:HH:MM` .

`D` is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see [the ISO-8601 spec as described on Wikipedia](https://en.wikipedia.org/wiki/ISO_week_date) .

`HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour.

For example, `1:05:00` specifies maintenance at 5 AM Monday.

DiskIopsConfiguration -> (structure)

The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for NetApp ONTAP, Amazon FSx for Windows File Server, or FSx for OpenZFS file system. By default, Amazon FSx automatically provisions 3 IOPS per GB of storage capacity. You can provision additional IOPS per GB of storage. The configuration consists of the total number of provisioned SSD IOPS and how it is was provisioned, or the mode (by the customer or by Amazon FSx).

Mode -> (string)

Specifies whether the file system is using the `AUTOMATIC` setting of SSD IOPS of 3 IOPS per GB of storage capacity, or if it using a `USER_PROVISIONED` value.

Iops -> (long)

The total number of SSD IOPS provisioned for the file system.

The minimum and maximum values for this property depend on the value of `HAPairs` and `StorageCapacity` . The minimum value is calculated as `StorageCapacity` * 3 * `HAPairs` (3 IOPS per GB of `StorageCapacity` ). The maximum value is calculated as 200,000 * `HAPairs` .

Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `Iops` is outside of the minimum or maximum values.

RootVolumeId -> (string)

The ID of the root volume of the OpenZFS file system.

PreferredSubnetId -> (string)

Required when `DeploymentType` is set to `MULTI_AZ_1` . This specifies the subnet in which you want the preferred file server to be located.

EndpointIpAddressRange -> (string)

(Multi-AZ only) Specifies the IP address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API and Amazon FSx console, Amazon FSx selects an available /28 IP address range for you from one of the VPCâs CIDR ranges. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables.

RouteTableIds -> (list)

(Multi-AZ only) The VPC route tables in which your file systemâs endpoints are created.

(string)

EndpointIpAddress -> (string)

The IP address of the endpoint that is used to access data or to manage the file system.

ReadCacheConfiguration -> (structure)

Required when `StorageType` is set to `INTELLIGENT_TIERING` . Specifies the optional provisioned SSD read cache.

SizingMode -> (string)

Specifies how the provisioned SSD read cache is sized, as follows:

- Set to `NO_CACHE` if you do not want to use an SSD read cache with your Intelligent-Tiering file system.
- Set to `USER_PROVISIONED` to specify the exact size of your SSD read cache.
- Set to `PROPORTIONAL_TO_THROUGHPUT_CAPACITY` to have your SSD read cache automatically sized based on your throughput capacity.

SizeGiB -> (integer)

Required if `SizingMode` is set to `USER_PROVISIONED` . Specifies the size of the file systemâs SSD read cache, in gibibytes (GiB).

FailureDetails -> (structure)

Provides information about a failed administrative action.

Message -> (string)

Error message providing details about the failed administrative action.

( â¦ recursive â¦ )TargetSnapshotValues -> (structure)

A snapshot of an Amazon FSx for OpenZFS volume.

ResourceARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

SnapshotId -> (string)

The ID of the snapshot.

Name -> (string)

The name of the snapshot.

VolumeId -> (string)

The ID of the volume that the snapshot is of.

CreationTime -> (timestamp)

The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

Lifecycle -> (string)

The lifecycle status of the snapshot.

- `PENDING` - Amazon FSx hasnât started creating the snapshot.
- `CREATING` - Amazon FSx is creating the snapshot.
- `DELETING` - Amazon FSx is deleting the snapshot.
- `AVAILABLE` - The snapshot is fully available.

LifecycleTransitionReason -> (structure)

Describes why a resource lifecycle state changed.

Message -> (string)

A detailed error message.

Tags -> (list)

A list of `Tag` values, with a maximum of 50 elements.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

TotalTransferBytes -> (long)

The number of bytes that have transferred for the FSx for OpenZFS snapshot that youâre copying.

RemainingTransferBytes -> (long)

The remaining bytes to transfer for the FSx for OpenZFS snapshot that youâre copying.

OpenZFSConfiguration -> (structure)

The configuration of an Amazon FSx for OpenZFS volume.

ParentVolumeId -> (string)

The ID of the parent volume.

VolumePath -> (string)

The path to the volume from the root volume. For example, `fsx/parentVolume/volume1` .

StorageCapacityReservationGiB -> (integer)

The amount of storage in gibibytes (GiB) to reserve from the parent volume. You canât reserve more storage than the parent volume has reserved.

StorageCapacityQuotaGiB -> (integer)

The maximum amount of storage in gibibytes (GiB) that the volume can use from its parent. You can specify a quota larger than the storage on the parent volume.

RecordSizeKiB -> (integer)

The record size of an OpenZFS volume, in kibibytes (KiB). Valid values are 4, 8, 16, 32, 64, 128, 256, 512, or 1024 KiB. The default is 128 KiB. Most workloads should use the default record size. For guidance on when to set a custom record size, see the *Amazon FSx for OpenZFS User Guide* .

DataCompressionType -> (string)

Specifies the method used to compress the data on the volume. The compression type is `NONE` by default.

- `NONE` - Doesnât compress the data on the volume. `NONE` is the default.
- `ZSTD` - Compresses the data in the volume using the Zstandard (ZSTD) compression algorithm. Compared to LZ4, Z-Standard provides a better compression ratio to minimize on-disk storage utilization.
- `LZ4` - Compresses the data in the volume using the LZ4 compression algorithm. Compared to Z-Standard, LZ4 is less compute-intensive and delivers higher write throughput speeds.

CopyTagsToSnapshots -> (boolean)

A Boolean value indicating whether tags for the volume should be copied to snapshots. This value defaults to `false` . If itâs set to `true` , all tags for the volume are copied to snapshots where the user doesnât specify tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.

OriginSnapshot -> (structure)

The configuration object that specifies the snapshot to use as the origin of the data for the volume.

SnapshotARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

CopyStrategy -> (string)

The strategy used when copying data from the snapshot to the new volume.

- `CLONE` - The new volume references the data in the origin snapshot. Cloning a snapshot is faster than copying the data from a snapshot to a new volume and doesnât consume disk throughput. However, the origin snapshot canât be deleted if there is a volume using its copied data.
- `FULL_COPY` - Copies all data from the snapshot to the new volume.

### Note

The `INCREMENTAL_COPY` option is only for updating an existing volume by using a snapshot from another FSx for OpenZFS file system. For more information, see [CopySnapshotAndUpdateVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CopySnapshotAndUpdateVolume.html) .

ReadOnly -> (boolean)

A Boolean value indicating whether the volume is read-only.

NfsExports -> (list)

The configuration object for mounting a Network File System (NFS) file system.

(structure)

The Network File System (NFS) configurations for mounting an Amazon FSx for OpenZFS file system.

ClientConfigurations -> (list)

A list of configuration objects that contain the client and options for mounting the OpenZFS file system.

(structure)

Specifies who can mount an OpenZFS file system and the options available while mounting the file system.

Clients -> (string)

A value that specifies who can mount the file system. You can provide a wildcard character (`*` ), an IP address (`0.0.0.0` ), or a CIDR address (`192.0.2.0/24` ). By default, Amazon FSx uses the wildcard character when specifying the client.

Options -> (list)

The options to use when mounting the file system. For a list of options that you can use with Network File System (NFS), see the [exports(5) - Linux man page](https://linux.die.net/man/5/exports) . When choosing your options, consider the following:

- `crossmnt` is used by default. If you donât specify `crossmnt` when changing the client configuration, you wonât be able to see or access snapshots in your file systemâs snapshot directory.
- `sync` is used by default. If you instead specify `async` , the system acknowledges writes before writing to disk. If the system crashes before the writes are finished, you lose the unwritten data.

(string)

UserAndGroupQuotas -> (list)

An object specifying how much storage users or groups can use on the volume.

(structure)

Used to configure quotas that define how much storage a user or group can use on an FSx for OpenZFS volume. For more information, see [Volume properties](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-volumes.html#volume-properties) in the FSx for OpenZFS User Guide.

Type -> (string)

Specifies whether the quota applies to a user or group.

Id -> (integer)

The ID of the user or group that the quota applies to.

StorageCapacityQuotaGiB -> (integer)

The user or groupâs storage quota, in gibibytes (GiB).

RestoreToSnapshot -> (string)

Specifies the ID of the snapshot to which the volume was restored.

DeleteIntermediateSnaphots -> (boolean)

A Boolean value indicating whether snapshots between the current state and the specified snapshot should be deleted when a volume is restored from snapshot.

DeleteClonedVolumes -> (boolean)

A Boolean value indicating whether dependent clone volumes created from intermediate snapshots should be deleted when a volume is restored from snapshot.

DeleteIntermediateData -> (boolean)

A Boolean value indicating whether snapshot data that differs between the current state and the specified snapshot should be overwritten when a volume is restored from a snapshot.

SourceSnapshotARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

DestinationSnapshot -> (string)

The ID of the snapshot thatâs being copied or was most recently copied to the destination volume.

CopyStrategy -> (string)

Specifies the strategy used when copying data from the snapshot to the new volume.

- `CLONE` - The new volume references the data in the origin snapshot. Cloning a snapshot is faster than copying data from the snapshot to a new volume and doesnât consume disk throughput. However, the origin snapshot canât be deleted if there is a volume using its copied data.
- `FULL_COPY` - Copies all data from the snapshot to the new volume. Specify this option to create the volume from a snapshot on another FSx for OpenZFS file system.

### Note

The `INCREMENTAL_COPY` option is only for updating an existing volume by using a snapshot from another FSx for OpenZFS file system. For more information, see [CopySnapshotAndUpdateVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CopySnapshotAndUpdateVolume.html) .

TargetSnapshotValues -> (structure)

A snapshot of an Amazon FSx for OpenZFS volume.

ResourceARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

SnapshotId -> (string)

The ID of the snapshot.

Name -> (string)

The name of the snapshot.

VolumeId -> (string)

The ID of the volume that the snapshot is of.

CreationTime -> (timestamp)

The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

Lifecycle -> (string)

The lifecycle status of the snapshot.

- `PENDING` - Amazon FSx hasnât started creating the snapshot.
- `CREATING` - Amazon FSx is creating the snapshot.
- `DELETING` - Amazon FSx is deleting the snapshot.
- `AVAILABLE` - The snapshot is fully available.

LifecycleTransitionReason -> (structure)

Describes why a resource lifecycle state changed.

Message -> (string)

A detailed error message.

Tags -> (list)

A list of `Tag` values, with a maximum of 50 elements.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

AdministrativeActions -> (list)

A list of administrative actions for the file system that are in process or waiting to be processed. Administrative actions describe changes to the Amazon FSx system.

(structure)

Describes a specific Amazon FSx administrative action for the current Windows, Lustre, OpenZFS, or ONTAP file system or volume.

AdministrativeActionType -> (string)

Describes the type of administrative action, as follows:

- `FILE_SYSTEM_UPDATE` - A file system update administrative action initiated from the Amazon FSx console, API (`UpdateFileSystem` ), or CLI (`update-file-system` ).
- `THROUGHPUT_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file systemâs throughput capacity has been completed successfully, a `THROUGHPUT_OPTIMIZATION` task starts. You can track the storage-optimization progress using the `ProgressPercent` property. When `THROUGHPUT_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED` . For more information, see [Managing throughput capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-throughput-capacity.html) in the *Amazon FSx for Windows File Server User Guide* .
- `STORAGE_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file systemâs storage capacity has completed successfully, a `STORAGE_OPTIMIZATION` task starts.
- For Windows and ONTAP, storage optimization is the process of migrating the file system data to newer larger disks.
- For Lustre, storage optimization consists of rebalancing the data across the existing and newly added file servers.

You can track the storage-optimization progress using the `ProgressPercent` property. When `STORAGE_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED` . For more information, see [Managing storage capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-capacity.html) in the *Amazon FSx for Windows File Server User Guide* , [Managing storage capacity](https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-storage-capacity.html) in the *Amazon FSx for Lustre User Guide* , and [Managing storage capacity and provisioned IOPS](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-storage-capacity.html) in the *Amazon FSx for NetApp ONTAP User Guide* .

- `FILE_SYSTEM_ALIAS_ASSOCIATION` - A file system update to associate a new Domain Name System (DNS) alias with the file system. For more information, see [AssociateFileSystemAliases](https://docs.aws.amazon.com/fsx/latest/APIReference/API_AssociateFileSystemAliases.html) .
- `FILE_SYSTEM_ALIAS_DISASSOCIATION` - A file system update to disassociate a DNS alias from the file system. For more information, see [DisassociateFileSystemAliases](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DisassociateFileSystemAliases.html) .
- `IOPS_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file systemâs throughput capacity has been completed successfully, a `IOPS_OPTIMIZATION` task starts. You can track the storage-optimization progress using the `ProgressPercent` property. When `IOPS_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED` . For more information, see [Managing provisioned SSD IOPS](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-provisioned-ssd-iops.html) in the Amazon FSx for Windows File Server User Guide.
- `STORAGE_TYPE_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file systemâs throughput capacity has been completed successfully, a `STORAGE_TYPE_OPTIMIZATION` task starts. You can track the storage-optimization progress using the `ProgressPercent` property. When `STORAGE_TYPE_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED` .
- `VOLUME_UPDATE` - A volume update to an Amazon FSx for OpenZFS volume initiated from the Amazon FSx console, API (`UpdateVolume` ), or CLI (`update-volume` ).
- `VOLUME_RESTORE` - An Amazon FSx for OpenZFS volume is returned to the state saved by the specified snapshot, initiated from an API (`RestoreVolumeFromSnapshot` ) or CLI (`restore-volume-from-snapshot` ).
- `SNAPSHOT_UPDATE` - A snapshot update to an Amazon FSx for OpenZFS volume initiated from the Amazon FSx console, API (`UpdateSnapshot` ), or CLI (`update-snapshot` ).
- `RELEASE_NFS_V3_LOCKS` - Tracks the release of Network File System (NFS) V3 locks on an Amazon FSx for OpenZFS file system.
- `DOWNLOAD_DATA_FROM_BACKUP` - An FSx for ONTAP backup is being restored to a new volume on a second-generation file system. Once the all the file metadata is loaded onto the volume, you can mount the volume with read-only access. during this process.
- `VOLUME_INITIALIZE_WITH_SNAPSHOT` - A volume is being created from a snapshot on a different FSx for OpenZFS file system. You can initiate this from the Amazon FSx console, API (`CreateVolume` ), or CLI (`create-volume` ) when using the using the `FULL_COPY` strategy.
- `VOLUME_UPDATE_WITH_SNAPSHOT` - A volume is being updated from a snapshot on a different FSx for OpenZFS file system. You can initiate this from the Amazon FSx console, API (`CopySnapshotAndUpdateVolume` ), or CLI (`copy-snapshot-and-update-volume` ).

ProgressPercent -> (integer)

The percentage-complete status of a `STORAGE_OPTIMIZATION` or `DOWNLOAD_DATA_FROM_BACKUP` administrative action. Does not apply to any other administrative action type.

RequestTime -> (timestamp)

The time that the administrative action request was received.

Status -> (string)

The status of the administrative action, as follows:

- `FAILED` - Amazon FSx failed to process the administrative action successfully.
- `IN_PROGRESS` - Amazon FSx is processing the administrative action.
- `PENDING` - Amazon FSx is waiting to process the administrative action.
- `COMPLETED` - Amazon FSx has finished processing the administrative task. For a backup restore to a second-generation FSx for ONTAP file system, indicates that all data has been downloaded to the volume, and clients now have read-write access to volume.
- `UPDATED_OPTIMIZING` - For a storage-capacity increase update, Amazon FSx has updated the file system with the new storage capacity, and is now performing the storage-optimization process.
- `PENDING` - For a backup restore to a second-generation FSx for ONTAP file system, indicates that the file metadata is being downloaded onto the volume. The volumeâs Lifecycle state is CREATING.
- `IN_PROGRESS` - For a backup restore to a second-generation FSx for ONTAP file system, indicates that all metadata has been downloaded to the new volume and client can access data with read-only access while Amazon FSx downloads the file data to the volume. Track the progress of this process with the `ProgressPercent` element.

TargetFileSystemValues -> (structure)

The target value for the administration action, provided in the `UpdateFileSystem` operation. Returned for `FILE_SYSTEM_UPDATE` administrative actions.

OwnerId -> (string)

The Amazon Web Services account that created the file system. If the file system was created by a user in IAM Identity Center, the Amazon Web Services account to which the IAM user belongs is the owner.

CreationTime -> (timestamp)

The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

FileSystemId -> (string)

The system-generated, unique 17-digit ID of the file system.

FileSystemType -> (string)

The type of Amazon FSx file system, which can be `LUSTRE` , `WINDOWS` , `ONTAP` , or `OPENZFS` .

Lifecycle -> (string)

The lifecycle status of the file system. The following are the possible values and what they mean:

- `AVAILABLE` - The file system is in a healthy state, and is reachable and available for use.
- `CREATING` - Amazon FSx is creating the new file system.
- `DELETING` - Amazon FSx is deleting an existing file system.
- `FAILED` - An existing file system has experienced an unrecoverable failure. When creating a new file system, Amazon FSx was unable to create the file system.
- `MISCONFIGURED` - The file system is in a failed but recoverable state.
- `MISCONFIGURED_UNAVAILABLE` - (Amazon FSx for Windows File Server only) The file system is currently unavailable due to a change in your Active Directory configuration.
- `UPDATING` - The file system is undergoing a customer-initiated update.

FailureDetails -> (structure)

A structure providing details of any failures that occurred.

Message -> (string)

A message describing any failures that occurred.

StorageCapacity -> (integer)

The storage capacity of the file system in gibibytes (GiB).

Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `StorageCapacity` is outside of the minimum or maximum values.

StorageType -> (string)

The type of storage the file system is using. If set to `SSD` , the file system uses solid state drive storage. If set to `HDD` , the file system uses hard disk drive storage.

VpcId -> (string)

The ID of the primary virtual private cloud (VPC) for the file system.

SubnetIds -> (list)

Specifies the IDs of the subnets that the file system is accessible from. For the Amazon FSx Windows and ONTAP `MULTI_AZ_1` file system deployment type, there are two subnet IDs, one for the preferred file server and one for the standby file server. The preferred file server subnet identified in the `PreferredSubnetID` property. All other file systems have only one subnet ID.

For FSx for Lustre file systems, and Single-AZ Windows file systems, this is the ID of the subnet that contains the file systemâs endpoint. For `MULTI_AZ_1` Windows and ONTAP file systems, the file system endpoint is available in the `PreferredSubnetID` .

(string)

The ID for a subnet. A *subnet* is a range of IP addresses in your virtual private cloud (VPC). For more information, see [VPC and subnets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) in the *Amazon VPC User Guide.*

NetworkInterfaceIds -> (list)

The IDs of the elastic network interfaces from which a specific file system is accessible. The elastic network interface is automatically created in the same virtual private cloud (VPC) that the Amazon FSx file system was created in. For more information, see [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the *Amazon EC2 User Guide.*

For an Amazon FSx for Windows File Server file system, you can have one network interface ID. For an Amazon FSx for Lustre file system, you can have more than one.

(string)

An elastic network interface ID. An elastic network interface is a logical networking component in a virtual private cloud (VPC) that represents a virtual network card. For more information, see [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the *Amazon EC2 User Guide for Linux Instances* .

DNSName -> (string)

The Domain Name System (DNS) name for the file system.

KmsKeyId -> (string)

The ID of the Key Management Service (KMS) key used to encrypt Amazon FSx file system data. Used as follows with Amazon FSx file system types:

- Amazon FSx for Lustre `PERSISTENT_1` and `PERSISTENT_2` deployment types only.  `SCRATCH_1` and `SCRATCH_2` types are encrypted using the Amazon FSx service KMS key for your account.
- Amazon FSx for NetApp ONTAP
- Amazon FSx for OpenZFS
- Amazon FSx for Windows File Server

ResourceARN -> (string)

The Amazon Resource Name (ARN) of the file system resource.

Tags -> (list)

The tags to associate with the file system. For more information, see [Tagging your Amazon FSx resources](https://docs.aws.amazon.com/fsx/latest/LustreGuide/tag-resources.html) in the *Amazon FSx for Lustre User Guide* .

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

WindowsConfiguration -> (structure)

The configuration for this Amazon FSx for Windows File Server file system.

ActiveDirectoryId -> (string)

The ID for an existing Amazon Web Services Managed Microsoft Active Directory instance that the file system is joined to.

SelfManagedActiveDirectoryConfiguration -> (structure)

The configuration of the self-managed Microsoft Active Directory (AD) directory to which the Windows File Server or ONTAP storage virtual machine (SVM) instance is joined.

DomainName -> (string)

The fully qualified domain name of the self-managed AD directory.

OrganizationalUnitDistinguishedName -> (string)

The fully qualified distinguished name of the organizational unit within the self-managed AD directory to which the Windows File Server or ONTAP storage virtual machine (SVM) instance is joined.

FileSystemAdministratorsGroup -> (string)

The name of the domain group whose members have administrative privileges for the FSx file system.

UserName -> (string)

The user name for the service account on your self-managed AD domain that FSx uses to join to your AD domain.

DnsIps -> (list)

A list of up to three IP addresses of DNS servers or domain controllers in the self-managed AD directory.

(string)

DeploymentType -> (string)

Specifies the file system deployment type, valid values are the following:

- `MULTI_AZ_1` - Specifies a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability, and supports SSD and HDD storage.
- `SINGLE_AZ_1` - (Default) Specifies a file system that is configured for single AZ redundancy, only supports SSD storage.
- `SINGLE_AZ_2` - Latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports SSD and HDD storage.

For more information, see [Single-AZ and Multi-AZ File Systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html) .

RemoteAdministrationEndpoint -> (string)

For `MULTI_AZ_1` deployment types, use this endpoint when performing administrative tasks on the file system using Amazon FSx Remote PowerShell.

For `SINGLE_AZ_1` and `SINGLE_AZ_2` deployment types, this is the DNS name of the file system.

This endpoint is temporarily unavailable when the file system is undergoing maintenance.

PreferredSubnetId -> (string)

For `MULTI_AZ_1` deployment types, it specifies the ID of the subnet where the preferred file server is located. Must be one of the two subnet IDs specified in `SubnetIds` property. Amazon FSx serves traffic from this subnet except in the event of a failover to the secondary file server.

For `SINGLE_AZ_1` and `SINGLE_AZ_2` deployment types, this value is the same as that for `SubnetIDs` . For more information, see [Availability and durability: Single-AZ and Multi-AZ file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html#single-multi-az-resources) .

PreferredFileServerIp -> (string)

For `MULTI_AZ_1` deployment types, the IP address of the primary, or preferred, file server.

Use this IP address when mounting the file system on Linux SMB clients or Windows SMB clients that are not joined to a Microsoft Active Directory. Applicable for all Windows file system deployment types. This IP address is temporarily unavailable when the file system is undergoing maintenance. For Linux and Windows SMB clients that are joined to an Active Directory, use the file systemâs DNSName instead. For more information on mapping and mounting file shares, see [Accessing File Shares](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/accessing-file-shares.html) .

ThroughputCapacity -> (integer)

The throughput of the Amazon FSx file system, measured in megabytes per second.

MaintenanceOperationsInProgress -> (list)

The list of maintenance operations in progress for this file system.

(string)

An enumeration specifying the currently ongoing maintenance operation.

WeeklyMaintenanceStartTime -> (string)

The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone. d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.

DailyAutomaticBackupStartTime -> (string)

The preferred time to take daily automatic backups, in the UTC time zone.

AutomaticBackupRetentionDays -> (integer)

The number of days to retain automatic backups. Setting this to 0 disables automatic backups. You can retain automatic backups for a maximum of 90 days.

CopyTagsToBackups -> (boolean)

A boolean flag indicating whether tags on the file system should be copied to backups. This value defaults to false. If itâs set to true, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesnât specify any tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.

Aliases -> (list)

An array of one or more DNS aliases that are currently associated with the Amazon FSx file system. Aliases allow you to use existing DNS names to access the data in your Amazon FSx file system. You can associate up to 50 aliases with a file system at any time. You can associate additional DNS aliases after you create the file system using the AssociateFileSystemAliases operation. You can remove DNS aliases from the file system after it is created using the DisassociateFileSystemAliases operation. You only need to specify the alias name in the request payload. For more information, see [DNS aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html) .

(structure)

A DNS alias that is associated with the file system. You can use a DNS alias to access a file system using user-defined DNS names, in addition to the default DNS name that Amazon FSx assigns to the file system. For more information, see [DNS aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html) in the *FSx for Windows File Server User Guide* .

Name -> (string)

The name of the DNS alias. The alias name has to meet the following requirements:

- Formatted as a fully-qualified domain name (FQDN), `hostname.domain` , for example, `accounting.example.com` .
- Can contain alphanumeric characters, the underscore (_), and the hyphen (-).
- Cannot start or end with a hyphen.
- Can start with a numeric.

For DNS names, Amazon FSx stores alphabetic characters as lowercase letters (a-z), regardless of how you specify them: as uppercase letters, lowercase letters, or the corresponding letters in escape codes.

Lifecycle -> (string)

Describes the state of the DNS alias.

- AVAILABLE - The DNS alias is associated with an Amazon FSx file system.
- CREATING - Amazon FSx is creating the DNS alias and associating it with the file system.
- CREATE_FAILED - Amazon FSx was unable to associate the DNS alias with the file system.
- DELETING - Amazon FSx is disassociating the DNS alias from the file system and deleting it.
- DELETE_FAILED - Amazon FSx was unable to disassociate the DNS alias from the file system.

AuditLogConfiguration -> (structure)

The configuration that Amazon FSx for Windows File Server uses to audit and log user accesses of files, folders, and file shares on the Amazon FSx for Windows File Server file system.

FileAccessAuditLogLevel -> (string)

Sets which attempt type is logged by Amazon FSx for file and folder accesses.

- `SUCCESS_ONLY` - only successful attempts to access files or folders are logged.
- `FAILURE_ONLY` - only failed attempts to access files or folders are logged.
- `SUCCESS_AND_FAILURE` - both successful attempts and failed attempts to access files or folders are logged.
- `DISABLED` - access auditing of files and folders is turned off.

FileShareAccessAuditLogLevel -> (string)

Sets which attempt type is logged by Amazon FSx for file share accesses.

- `SUCCESS_ONLY` - only successful attempts to access file shares are logged.
- `FAILURE_ONLY` - only failed attempts to access file shares are logged.
- `SUCCESS_AND_FAILURE` - both successful attempts and failed attempts to access file shares are logged.
- `DISABLED` - access auditing of file shares is turned off.

AuditLogDestination -> (string)

The Amazon Resource Name (ARN) for the destination of the audit logs. The destination can be any Amazon CloudWatch Logs log group ARN or Amazon Kinesis Data Firehose delivery stream ARN.

The name of the Amazon CloudWatch Logs log group must begin with the `/aws/fsx` prefix. The name of the Amazon Kinesis Data Firehose delivery stream must begin with the `aws-fsx` prefix.

The destination ARN (either CloudWatch Logs log group or Kinesis Data Firehose delivery stream) must be in the same Amazon Web Services partition, Amazon Web Services Region, and Amazon Web Services account as your Amazon FSx file system.

DiskIopsConfiguration -> (structure)

The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for Windows file system. By default, Amazon FSx automatically provisions 3 IOPS per GiB of storage capacity. You can provision additional IOPS per GiB of storage, up to the maximum limit associated with your chosen throughput capacity.

Mode -> (string)

Specifies whether the file system is using the `AUTOMATIC` setting of SSD IOPS of 3 IOPS per GB of storage capacity, or if it using a `USER_PROVISIONED` value.

Iops -> (long)

The total number of SSD IOPS provisioned for the file system.

The minimum and maximum values for this property depend on the value of `HAPairs` and `StorageCapacity` . The minimum value is calculated as `StorageCapacity` * 3 * `HAPairs` (3 IOPS per GB of `StorageCapacity` ). The maximum value is calculated as 200,000 * `HAPairs` .

Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `Iops` is outside of the minimum or maximum values.

LustreConfiguration -> (structure)

The configuration for the Amazon FSx for Lustre file system.

WeeklyMaintenanceStartTime -> (string)

The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone. Here, `d` is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.

DataRepositoryConfiguration -> (structure)

The data repository configuration object for Lustre file systems returned in the response of the `CreateFileSystem` operation.

This data type is not supported on file systems with a data repository association. For file systems with a data repository association, see .

Lifecycle -> (string)

Describes the state of the file systemâs S3 durable data repository, if it is configured with an S3 repository. The lifecycle can have the following values:

- `CREATING` - The data repository configuration between the FSx file system and the linked S3 data repository is being created. The data repository is unavailable.
- `AVAILABLE` - The data repository is available for use.
- `MISCONFIGURED` - Amazon FSx cannot automatically import updates from the S3 bucket until the data repository configuration is corrected. For more information, see [Troubleshooting a Misconfigured linked S3 bucket](https://docs.aws.amazon.com/fsx/latest/LustreGuide/troubleshooting.html#troubleshooting-misconfigured-data-repository) .
- `UPDATING` - The data repository is undergoing a customer initiated update and availability may be impacted.
- `FAILED` - The data repository is in a terminal state that cannot be recovered.

ImportPath -> (string)

The import path to the Amazon S3 bucket (and optional prefix) that youâre using as the data repository for your FSx for Lustre file system, for example `s3://import-bucket/optional-prefix` . If a prefix is specified after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system.

ExportPath -> (string)

The export path to the Amazon S3 bucket (and prefix) that you are using to store new and changed Lustre file system files in S3.

ImportedFileChunkSize -> (integer)

For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.

The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.

AutoImportPolicy -> (string)

Describes the file systemâs linked S3 data repositoryâs `AutoImportPolicy` . The AutoImportPolicy configures how Amazon FSx keeps your file and directory listings up to date as you add or modify objects in your linked S3 bucket. `AutoImportPolicy` can have the following values:

- `NONE` - (Default) AutoImport is off. Amazon FSx only updates file and directory listings from the linked S3 bucket when the file system is created. FSx does not update file and directory listings for any new or changed objects after choosing this option.
- `NEW` - AutoImport is on. Amazon FSx automatically imports directory listings of any new objects added to the linked S3 bucket that do not currently exist in the FSx file system.
- `NEW_CHANGED` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket and any existing objects that are changed in the S3 bucket after you choose this option.
- `NEW_CHANGED_DELETED` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket, any existing objects that are changed in the S3 bucket, and any objects that were deleted in the S3 bucket.

FailureDetails -> (structure)

Provides detailed information about the data repository if its `Lifecycle` is set to `MISCONFIGURED` or `FAILED` .

Message -> (string)

A detailed error message.

DeploymentType -> (string)

The deployment type of the FSx for Lustre file system. *Scratch deployment type* is designed for temporary storage and shorter-term processing of data.

`SCRATCH_1` and `SCRATCH_2` deployment types are best suited for when you need temporary storage and shorter-term processing of data. The `SCRATCH_2` deployment type provides in-transit encryption of data and higher burst throughput capacity than `SCRATCH_1` .

The `PERSISTENT_1` and `PERSISTENT_2` deployment type is used for longer-term storage and workloads and encryption of data in transit. `PERSISTENT_2` offers higher `PerUnitStorageThroughput` (up to 1000 MB/s/TiB) along with a lower minimum storage capacity requirement (600 GiB). To learn more about FSx for Lustre deployment types, see [FSx for Lustre deployment options](https://docs.aws.amazon.com/fsx/latest/LustreGuide/lustre-deployment-types.html) .

The default is `SCRATCH_1` .

PerUnitStorageThroughput -> (integer)

Per unit storage throughput represents the megabytes per second of read or write throughput per 1 tebibyte of storage provisioned. File system throughput capacity is equal to Storage capacity (TiB) * PerUnitStorageThroughput (MB/s/TiB). This option is only valid for `PERSISTENT_1` and `PERSISTENT_2` deployment types.

Valid values:

- For `PERSISTENT_1` SSD storage: 50, 100, 200.
- For `PERSISTENT_1` HDD storage: 12, 40.
- For `PERSISTENT_2` SSD storage: 125, 250, 500, 1000.

MountName -> (string)

You use the `MountName` value when mounting the file system.

For the `SCRATCH_1` deployment type, this value is always â`fsx` â. For `SCRATCH_2` , `PERSISTENT_1` , and `PERSISTENT_2` deployment types, this value is a string that is unique within an Amazon Web Services Region.

DailyAutomaticBackupStartTime -> (string)

A recurring daily time, in the format `HH:MM` . `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.

AutomaticBackupRetentionDays -> (integer)

The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30` .

CopyTagsToBackups -> (boolean)

A boolean flag indicating whether tags on the file system are copied to backups. If itâs set to true, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesnât specify any tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value. (Default = false)

DriveCacheType -> (string)

The type of drive cache used by `PERSISTENT_1` file systems that are provisioned with HDD storage devices. This parameter is required when `StorageType` is HDD. When set to `READ` the file system has an SSD storage cache that is sized to 20% of the file systemâs storage capacity. This improves the performance for frequently accessed files by caching up to 20% of the total storage capacity.

This parameter is required when `StorageType` is set to HDD.

DataCompressionType -> (string)

The data compression configuration for the file system. `DataCompressionType` can have the following values:

- `NONE` - Data compression is turned off for the file system.
- `LZ4` - Data compression is turned on with the LZ4 algorithm.

For more information, see [Lustre data compression](https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-compression.html) .

LogConfiguration -> (structure)

The Lustre logging configuration. Lustre logging writes the enabled log events for your file system to Amazon CloudWatch Logs.

Level -> (string)

The data repository events that are logged by Amazon FSx.

- `WARN_ONLY` - only warning events are logged.
- `ERROR_ONLY` - only error events are logged.
- `WARN_ERROR` - both warning events and error events are logged.
- `DISABLED` - logging of data repository events is turned off.

Note that Amazon File Cache uses a default setting of `WARN_ERROR` , which canât be changed.

Destination -> (string)

The Amazon Resource Name (ARN) that specifies the destination of the logs. The destination can be any Amazon CloudWatch Logs log group ARN. The destination ARN must be in the same Amazon Web Services partition, Amazon Web Services Region, and Amazon Web Services account as your Amazon FSx file system.

RootSquashConfiguration -> (structure)

The Lustre root squash configuration for an Amazon FSx for Lustre file system. When enabled, root squash restricts root-level access from clients that try to access your file system as a root user.

RootSquash -> (string)

You enable root squash by setting a user ID (UID) and group ID (GID) for the file system in the format `UID:GID` (for example, `365534:65534` ). The UID and GID values can range from `0` to `4294967294` :

- A non-zero value for UID and GID enables root squash. The UID and GID values can be different, but each must be a non-zero value.
- A value of `0` (zero) for UID and GID indicates root, and therefore disables root squash.

When root squash is enabled, the user ID and group ID of a root user accessing the file system are re-mapped to the UID and GID you provide.

NoSquashNids -> (list)

When root squash is enabled, you can optionally specify an array of NIDs of clients for which root squash does not apply. A client NID is a Lustre Network Identifier used to uniquely identify a client. You can specify the NID as either a single address or a range of addresses:

- A single address is described in standard Lustre NID format by specifying the clientâs IP address followed by the Lustre network ID (for example, `10.0.1.6@tcp` ).
- An address range is described using a dash to separate the range (for example, `10.0.[2-10].[1-255]@tcp` ).

(string)

MetadataConfiguration -> (structure)

The Lustre metadata performance configuration for an Amazon FSx for Lustre file system using a `PERSISTENT_2` deployment type.

Iops -> (integer)

The number of Metadata IOPS provisioned for the file system. Valid values are `1500` , `3000` , `6000` , `12000` , and multiples of `12000` up to a maximum of `192000` .

Mode -> (string)

The metadata configuration mode for provisioning Metadata IOPS for the file system.

- In AUTOMATIC mode, FSx for Lustre automatically provisions and scales the number of Metadata IOPS on your file system based on your file system storage capacity.
- In USER_PROVISIONED mode, you can choose to specify the number of Metadata IOPS to provision for your file system.

EfaEnabled -> (boolean)

Specifies whether Elastic Fabric Adapter (EFA) and GPUDirect Storage (GDS) support is enabled for the Amazon FSx for Lustre file system.

OntapConfiguration -> (structure)

The configuration for this Amazon FSx for NetApp ONTAP file system.

AutomaticBackupRetentionDays -> (integer)

The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30` .

DailyAutomaticBackupStartTime -> (string)

A recurring daily time, in the format `HH:MM` . `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.

DeploymentType -> (string)

Specifies the FSx for ONTAP file system deployment type in use in the file system.

- `MULTI_AZ_1` - A high availability file system configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability. This is a first-generation FSx for ONTAP file system.
- `MULTI_AZ_2` - A high availability file system configured for Multi-AZ redundancy to tolerate temporary AZ unavailability. This is a second-generation FSx for ONTAP file system.
- `SINGLE_AZ_1` - A file system configured for Single-AZ redundancy. This is a first-generation FSx for ONTAP file system.
- `SINGLE_AZ_2` - A file system configured with multiple high-availability (HA) pairs for Single-AZ redundancy. This is a second-generation FSx for ONTAP file system.

For information about the use cases for Multi-AZ and Single-AZ deployments, refer to [Choosing Multi-AZ or Single-AZ file system deployment](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-multiAZ.html) .

EndpointIpAddressRange -> (string)

(Multi-AZ only) Specifies the IP address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API, Amazon FSx selects an unused IP address range for you from the 198.19.* range. By default in the Amazon FSx console, Amazon FSx chooses the last 64 IP addresses from the VPCâs primary CIDR range to use as the endpoint IP address range for the file system. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables.

Endpoints -> (structure)

The `Management` and `Intercluster` endpoints that are used to access data or to manage the file system using the NetApp ONTAP CLI, REST API, or NetApp SnapMirror.

Intercluster -> (structure)

An endpoint for managing your file system by setting up NetApp SnapMirror with other ONTAP systems.

DNSName -> (string)

The file systemâs DNS name. You can mount your file system using its DNS name.

IpAddresses -> (list)

IP addresses of the file system endpoint.

(string)

Management -> (structure)

An endpoint for managing your file system using the NetApp ONTAP CLI and NetApp ONTAP API.

DNSName -> (string)

The file systemâs DNS name. You can mount your file system using its DNS name.

IpAddresses -> (list)

IP addresses of the file system endpoint.

(string)

DiskIopsConfiguration -> (structure)

The SSD IOPS configuration for the ONTAP file system, specifying the number of provisioned IOPS and the provision mode.

Mode -> (string)

Specifies whether the file system is using the `AUTOMATIC` setting of SSD IOPS of 3 IOPS per GB of storage capacity, or if it using a `USER_PROVISIONED` value.

Iops -> (long)

The total number of SSD IOPS provisioned for the file system.

The minimum and maximum values for this property depend on the value of `HAPairs` and `StorageCapacity` . The minimum value is calculated as `StorageCapacity` * 3 * `HAPairs` (3 IOPS per GB of `StorageCapacity` ). The maximum value is calculated as 200,000 * `HAPairs` .

Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `Iops` is outside of the minimum or maximum values.

PreferredSubnetId -> (string)

The ID for a subnet. A *subnet* is a range of IP addresses in your virtual private cloud (VPC). For more information, see [VPC and subnets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) in the *Amazon VPC User Guide.*

RouteTableIds -> (list)

(Multi-AZ only) The VPC route tables in which your file systemâs endpoints are created.

(string)

ThroughputCapacity -> (integer)

The sustained throughput of an Amazon FSx file system in Megabytes per second (MBps).

WeeklyMaintenanceStartTime -> (string)

A recurring weekly time, in the format `D:HH:MM` .

`D` is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see [the ISO-8601 spec as described on Wikipedia](https://en.wikipedia.org/wiki/ISO_week_date) .

`HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour.

For example, `1:05:00` specifies maintenance at 5 AM Monday.

FsxAdminPassword -> (string)

You can use the `fsxadmin` user account to access the NetApp ONTAP CLI and REST API. The password value is always redacted in the response.

HAPairs -> (integer)

Specifies how many high-availability (HA) file server pairs the file system will have. The default value is 1. The value of this property affects the values of `StorageCapacity` , `Iops` , and `ThroughputCapacity` . For more information, see [High-availability (HA) pairs](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/HA-pairs.html) in the FSx for ONTAP user guide.

Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:

- The value of `HAPairs` is less than 1 or greater than 12.
- The value of `HAPairs` is greater than 1 and the value of `DeploymentType` is `SINGLE_AZ_1` , `MULTI_AZ_1` , or `MULTI_AZ_2` .

ThroughputCapacityPerHAPair -> (integer)

Use to choose the throughput capacity per HA pair. When the value of `HAPairs` is equal to 1, the value of `ThroughputCapacityPerHAPair` is the total throughput for the file system.

This field and `ThroughputCapacity` cannot be defined in the same API call, but one is required.

This field and `ThroughputCapacity` are the same for file systems with one HA pair.

- For `SINGLE_AZ_1` and `MULTI_AZ_1` file systems, valid values are 128, 256, 512, 1024, 2048, or 4096 MBps.
- For `SINGLE_AZ_2` , valid values are 1536, 3072, or 6144 MBps.
- For `MULTI_AZ_2` , valid values are 384, 768, 1536, 3072, or 6144 MBps.

Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:

- The value of `ThroughputCapacity` and `ThroughputCapacityPerHAPair` are not the same value.
- The value of deployment type is `SINGLE_AZ_2` and `ThroughputCapacity` / `ThroughputCapacityPerHAPair` is not a valid HA pair (a value between 1 and 12).
- The value of `ThroughputCapacityPerHAPair` is not a valid value.

FileSystemTypeVersion -> (string)

The Lustre version of the Amazon FSx for Lustre file system, which can be `2.10` , `2.12` , or `2.15` .

OpenZFSConfiguration -> (structure)

The configuration for this Amazon FSx for OpenZFS file system.

AutomaticBackupRetentionDays -> (integer)

The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30` .

CopyTagsToBackups -> (boolean)

A Boolean value indicating whether tags on the file system should be copied to backups. If itâs set to `true` , all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesnât specify any tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.

CopyTagsToVolumes -> (boolean)

A Boolean value indicating whether tags for the volume should be copied to snapshots. This value defaults to `false` . If itâs set to `true` , all tags for the volume are copied to snapshots where the user doesnât specify tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.

DailyAutomaticBackupStartTime -> (string)

A recurring daily time, in the format `HH:MM` . `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.

DeploymentType -> (string)

Specifies the file-system deployment type. Amazon FSx for OpenZFS supports `MULTI_AZ_1` , `SINGLE_AZ_HA_2` , `SINGLE_AZ_HA_1` , `SINGLE_AZ_2` , and `SINGLE_AZ_1` .

ThroughputCapacity -> (integer)

The throughput of an Amazon FSx file system, measured in megabytes per second (MBps).

WeeklyMaintenanceStartTime -> (string)

A recurring weekly time, in the format `D:HH:MM` .

`D` is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see [the ISO-8601 spec as described on Wikipedia](https://en.wikipedia.org/wiki/ISO_week_date) .

`HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour.

For example, `1:05:00` specifies maintenance at 5 AM Monday.

DiskIopsConfiguration -> (structure)

The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for NetApp ONTAP, Amazon FSx for Windows File Server, or FSx for OpenZFS file system. By default, Amazon FSx automatically provisions 3 IOPS per GB of storage capacity. You can provision additional IOPS per GB of storage. The configuration consists of the total number of provisioned SSD IOPS and how it is was provisioned, or the mode (by the customer or by Amazon FSx).

Mode -> (string)

Specifies whether the file system is using the `AUTOMATIC` setting of SSD IOPS of 3 IOPS per GB of storage capacity, or if it using a `USER_PROVISIONED` value.

Iops -> (long)

The total number of SSD IOPS provisioned for the file system.

The minimum and maximum values for this property depend on the value of `HAPairs` and `StorageCapacity` . The minimum value is calculated as `StorageCapacity` * 3 * `HAPairs` (3 IOPS per GB of `StorageCapacity` ). The maximum value is calculated as 200,000 * `HAPairs` .

Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `Iops` is outside of the minimum or maximum values.

RootVolumeId -> (string)

The ID of the root volume of the OpenZFS file system.

PreferredSubnetId -> (string)

Required when `DeploymentType` is set to `MULTI_AZ_1` . This specifies the subnet in which you want the preferred file server to be located.

EndpointIpAddressRange -> (string)

(Multi-AZ only) Specifies the IP address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API and Amazon FSx console, Amazon FSx selects an available /28 IP address range for you from one of the VPCâs CIDR ranges. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables.

RouteTableIds -> (list)

(Multi-AZ only) The VPC route tables in which your file systemâs endpoints are created.

(string)

EndpointIpAddress -> (string)

The IP address of the endpoint that is used to access data or to manage the file system.

ReadCacheConfiguration -> (structure)

Required when `StorageType` is set to `INTELLIGENT_TIERING` . Specifies the optional provisioned SSD read cache.

SizingMode -> (string)

Specifies how the provisioned SSD read cache is sized, as follows:

- Set to `NO_CACHE` if you do not want to use an SSD read cache with your Intelligent-Tiering file system.
- Set to `USER_PROVISIONED` to specify the exact size of your SSD read cache.
- Set to `PROPORTIONAL_TO_THROUGHPUT_CAPACITY` to have your SSD read cache automatically sized based on your throughput capacity.

SizeGiB -> (integer)

Required if `SizingMode` is set to `USER_PROVISIONED` . Specifies the size of the file systemâs SSD read cache, in gibibytes (GiB).

FailureDetails -> (structure)

Provides information about a failed administrative action.

Message -> (string)

Error message providing details about the failed administrative action.

TargetVolumeValues -> (structure)

Describes an Amazon FSx volume.

CreationTime -> (timestamp)

The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

FileSystemId -> (string)

The globally unique ID of the file system, assigned by Amazon FSx.

Lifecycle -> (string)

The lifecycle status of the volume.

- `AVAILABLE` - The volume is fully available for use.
- `CREATED` - The volume has been created.
- `CREATING` - Amazon FSx is creating the new volume.
- `DELETING` - Amazon FSx is deleting an existing volume.
- `FAILED` - Amazon FSx was unable to create the volume.
- `MISCONFIGURED` - The volume is in a failed but recoverable state.
- `PENDING` - Amazon FSx hasnât started creating the volume.

Name -> (string)

The name of the volume.

OntapConfiguration -> (structure)

The configuration of an Amazon FSx for NetApp ONTAP volume.

FlexCacheEndpointType -> (string)

Specifies the FlexCache endpoint type of the volume. Valid values are the following:

- `NONE` specifies that the volume doesnât have a FlexCache configuration. `NONE` is the default.
- `ORIGIN` specifies that the volume is the origin volume for a FlexCache volume.
- `CACHE` specifies that the volume is a FlexCache volume.

JunctionPath -> (string)

Specifies the directory that network-attached storage (NAS) clients use to mount the volume, along with the storage virtual machine (SVM) Domain Name System (DNS) name or IP address. You can create a `JunctionPath` directly below a parent volume junction or on a directory within a volume. A `JunctionPath` for a volume named `vol3` might be `/vol1/vol2/vol3` , or `/vol1/dir2/vol3` , or even `/dir1/dir2/vol3` .

SecurityStyle -> (string)

The security style for the volume, which can be `UNIX` , `NTFS` , or `MIXED` .

SizeInMegabytes -> (integer)

The configured size of the volume, in megabytes (MBs).

StorageEfficiencyEnabled -> (boolean)

The volumeâs storage efficiency setting.

StorageVirtualMachineId -> (string)

The ID of the volumeâs storage virtual machine.

StorageVirtualMachineRoot -> (boolean)

A Boolean flag indicating whether this volume is the root volume for its storage virtual machine (SVM). Only one volume on an SVM can be the root volume. This value defaults to `false` . If this value is `true` , then this is the SVM root volume.

This flag is useful when youâre deleting an SVM, because you must first delete all non-root volumes. This flag, when set to `false` , helps you identify which volumes to delete before you can delete the SVM.

TieringPolicy -> (structure)

The volumeâs `TieringPolicy` setting.

CoolingPeriod -> (integer)

Specifies the number of days that user data in a volume must remain inactive before it is considered âcoldâ and moved to the capacity pool. Used with the `AUTO` and `SNAPSHOT_ONLY` tiering policies. Enter a whole number between 2 and 183. Default values are 31 days for `AUTO` and 2 days for `SNAPSHOT_ONLY` .

Name -> (string)

Specifies the tiering policy used to transition data. Default value is `SNAPSHOT_ONLY` .

- `SNAPSHOT_ONLY` - moves cold snapshots to the capacity pool storage tier.
- `AUTO` - moves cold user data and snapshots to the capacity pool storage tier based on your access patterns.
- `ALL` - moves all user data blocks in both the active file system and Snapshot copies to the storage pool tier.
- `NONE` - keeps a volumeâs data in the primary storage tier, preventing it from being moved to the capacity pool tier.

UUID -> (string)

The volumeâs universally unique identifier (UUID).

OntapVolumeType -> (string)

Specifies the type of volume. Valid values are the following:

- `RW` specifies a read/write volume. `RW` is the default.
- `DP` specifies a data-protection volume. You can protect data by replicating it to data-protection mirror copies. If a disaster occurs, you can use these data-protection mirror copies to recover data.
- `LS` specifies a load-sharing mirror volume. A load-sharing mirror reduces the network traffic to a FlexVol volume by providing additional read-only access to clients.

SnapshotPolicy -> (string)

Specifies the snapshot policy for the volume. There are three built-in snapshot policies:

- `default` : This is the default policy. A maximum of six hourly snapshots taken five minutes past the hour. A maximum of two daily snapshots taken Monday through Saturday at 10 minutes after midnight. A maximum of two weekly snapshots taken every Sunday at 15 minutes after midnight.
- `default-1weekly` : This policy is the same as the `default` policy except that it only retains one snapshot from the weekly schedule.
- `none` : This policy does not take any snapshots. This policy can be assigned to volumes to prevent automatic snapshots from being taken.

You can also provide the name of a custom policy that you created with the ONTAP CLI or REST API.

For more information, see [Snapshot policies](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snapshots-ontap.html#snapshot-policies) in the Amazon FSx for NetApp ONTAP User Guide.

CopyTagsToBackups -> (boolean)

A boolean flag indicating whether tags for the volume should be copied to backups. This value defaults to false. If itâs set to true, all tags for the volume are copied to all automatic and user-initiated backups where the user doesnât specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the volume, regardless of this value.

SnaplockConfiguration -> (structure)

The SnapLock configuration object for an FSx for ONTAP SnapLock volume.

AuditLogVolume -> (boolean)

Enables or disables the audit log volume for an FSx for ONTAP SnapLock volume. The default value is `false` . If you set `AuditLogVolume` to `true` , the SnapLock volume is created as an audit log volume. The minimum retention period for an audit log volume is six months.

For more information, see [SnapLock audit log volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/how-snaplock-works.html#snaplock-audit-log-volume) .

AutocommitPeriod -> (structure)

The configuration object for setting the autocommit period of files in an FSx for ONTAP SnapLock volume.

Type -> (string)

Defines the type of time for the autocommit period of a file in an FSx for ONTAP SnapLock volume. Setting this value to `NONE` disables autocommit. The default value is `NONE` .

Value -> (integer)

Defines the amount of time for the autocommit period of a file in an FSx for ONTAP SnapLock volume. The following ranges are valid:

- `Minutes` : 5 - 65,535
- `Hours` : 1 - 65,535
- `Days` : 1 - 3,650
- `Months` : 1 - 120
- `Years` : 1 - 10

PrivilegedDelete -> (string)

Enables, disables, or permanently disables privileged delete on an FSx for ONTAP SnapLock Enterprise volume. Enabling privileged delete allows SnapLock administrators to delete write once, read many (WORM) files even if they have active retention periods. `PERMANENTLY_DISABLED` is a terminal state. If privileged delete is permanently disabled on a SnapLock volume, you canât re-enable it. The default value is `DISABLED` .

For more information, see [Privileged delete](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-enterprise.html#privileged-delete) .

RetentionPeriod -> (structure)

Specifies the retention period of an FSx for ONTAP SnapLock volume.

DefaultRetention -> (structure)

The retention period assigned to a write once, read many (WORM) file by default if an explicit retention period is not set for an FSx for ONTAP SnapLock volume. The default retention period must be greater than or equal to the minimum retention period and less than or equal to the maximum retention period.

Type -> (string)

Defines the type of time for the retention period of an FSx for ONTAP SnapLock volume. Set it to one of the valid types. If you set it to `INFINITE` , the files are retained forever. If you set it to `UNSPECIFIED` , the files are retained until you set an explicit retention period.

Value -> (integer)

Defines the amount of time for the retention period of an FSx for ONTAP SnapLock volume. You canât set a value for `INFINITE` or `UNSPECIFIED` . For all other options, the following ranges are valid:

- `Seconds` : 0 - 65,535
- `Minutes` : 0 - 65,535
- `Hours` : 0 - 24
- `Days` : 0 - 365
- `Months` : 0 - 12
- `Years` : 0 - 100

MinimumRetention -> (structure)

The shortest retention period that can be assigned to a WORM file on an FSx for ONTAP SnapLock volume.

Type -> (string)

Defines the type of time for the retention period of an FSx for ONTAP SnapLock volume. Set it to one of the valid types. If you set it to `INFINITE` , the files are retained forever. If you set it to `UNSPECIFIED` , the files are retained until you set an explicit retention period.

Value -> (integer)

Defines the amount of time for the retention period of an FSx for ONTAP SnapLock volume. You canât set a value for `INFINITE` or `UNSPECIFIED` . For all other options, the following ranges are valid:

- `Seconds` : 0 - 65,535
- `Minutes` : 0 - 65,535
- `Hours` : 0 - 24
- `Days` : 0 - 365
- `Months` : 0 - 12
- `Years` : 0 - 100

MaximumRetention -> (structure)

The longest retention period that can be assigned to a WORM file on an FSx for ONTAP SnapLock volume.

Type -> (string)

Defines the type of time for the retention period of an FSx for ONTAP SnapLock volume. Set it to one of the valid types. If you set it to `INFINITE` , the files are retained forever. If you set it to `UNSPECIFIED` , the files are retained until you set an explicit retention period.

Value -> (integer)

Defines the amount of time for the retention period of an FSx for ONTAP SnapLock volume. You canât set a value for `INFINITE` or `UNSPECIFIED` . For all other options, the following ranges are valid:

- `Seconds` : 0 - 65,535
- `Minutes` : 0 - 65,535
- `Hours` : 0 - 24
- `Days` : 0 - 365
- `Months` : 0 - 12
- `Years` : 0 - 100

SnaplockType -> (string)

Specifies the retention mode of an FSx for ONTAP SnapLock volume. After it is set, it canât be changed. You can choose one of the following retention modes:

- `COMPLIANCE` : Files transitioned to write once, read many (WORM) on a Compliance volume canât be deleted until their retention periods expire. This retention mode is used to address government or industry-specific mandates or to protect against ransomware attacks. For more information, see [SnapLock Compliance](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-compliance.html) .
- `ENTERPRISE` : Files transitioned to WORM on an Enterprise volume can be deleted by authorized users before their retention periods expire using privileged delete. This retention mode is used to advance an organizationâs data integrity and internal compliance or to test retention settings before using SnapLock Compliance. For more information, see [SnapLock Enterprise](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-enterprise.html) .

VolumeAppendModeEnabled -> (boolean)

Enables or disables volume-append mode on an FSx for ONTAP SnapLock volume. Volume-append mode allows you to create WORM-appendable files and write data to them incrementally. The default value is `false` .

For more information, see [Volume-append mode](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/worm-state.html#worm-state-append) .

VolumeStyle -> (string)

Use to specify the style of an ONTAP volume. For more information about FlexVols and FlexGroups, see [Volume types](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/volume-types.html) in Amazon FSx for NetApp ONTAP User Guide.

AggregateConfiguration -> (structure)

This structure specifies configuration options for a volumeâs storage aggregate or aggregates.

Aggregates -> (list)

The list of aggregates that this volume resides on. Aggregates are storage pools which make up your primary storage tier. Each high-availability (HA) pair has one aggregate. The names of the aggregates map to the names of the aggregates in the ONTAP CLI and REST API. For FlexVols, there will always be a single entry.

Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:

- The strings in the value of `Aggregates` are not are not formatted as `aggrX` , where X is a number between 1 and 12.
- The value of `Aggregates` contains aggregates that are not present.
- One or more of the aggregates supplied are too close to the volume limit to support adding more volumes.

(string)

TotalConstituents -> (integer)

The total number of constituents this FlexGroup volume has. Not applicable for FlexVols.

SizeInBytes -> (long)

The configured size of the volume, in bytes.

ResourceARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

Tags -> (list)

A list of `Tag` values, with a maximum of 50 elements.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

VolumeId -> (string)

The system-generated, unique ID of the volume.

VolumeType -> (string)

The type of the volume.

LifecycleTransitionReason -> (structure)

The reason why the volume lifecycle status changed.

Message -> (string)

A detailed error message.

OpenZFSConfiguration -> (structure)

The configuration of an Amazon FSx for OpenZFS volume.

ParentVolumeId -> (string)

The ID of the parent volume.

VolumePath -> (string)

The path to the volume from the root volume. For example, `fsx/parentVolume/volume1` .

StorageCapacityReservationGiB -> (integer)

The amount of storage in gibibytes (GiB) to reserve from the parent volume. You canât reserve more storage than the parent volume has reserved.

StorageCapacityQuotaGiB -> (integer)

The maximum amount of storage in gibibytes (GiB) that the volume can use from its parent. You can specify a quota larger than the storage on the parent volume.

RecordSizeKiB -> (integer)

The record size of an OpenZFS volume, in kibibytes (KiB). Valid values are 4, 8, 16, 32, 64, 128, 256, 512, or 1024 KiB. The default is 128 KiB. Most workloads should use the default record size. For guidance on when to set a custom record size, see the *Amazon FSx for OpenZFS User Guide* .

DataCompressionType -> (string)

Specifies the method used to compress the data on the volume. The compression type is `NONE` by default.

- `NONE` - Doesnât compress the data on the volume. `NONE` is the default.
- `ZSTD` - Compresses the data in the volume using the Zstandard (ZSTD) compression algorithm. Compared to LZ4, Z-Standard provides a better compression ratio to minimize on-disk storage utilization.
- `LZ4` - Compresses the data in the volume using the LZ4 compression algorithm. Compared to Z-Standard, LZ4 is less compute-intensive and delivers higher write throughput speeds.

CopyTagsToSnapshots -> (boolean)

A Boolean value indicating whether tags for the volume should be copied to snapshots. This value defaults to `false` . If itâs set to `true` , all tags for the volume are copied to snapshots where the user doesnât specify tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.

OriginSnapshot -> (structure)

The configuration object that specifies the snapshot to use as the origin of the data for the volume.

SnapshotARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

CopyStrategy -> (string)

The strategy used when copying data from the snapshot to the new volume.

- `CLONE` - The new volume references the data in the origin snapshot. Cloning a snapshot is faster than copying the data from a snapshot to a new volume and doesnât consume disk throughput. However, the origin snapshot canât be deleted if there is a volume using its copied data.
- `FULL_COPY` - Copies all data from the snapshot to the new volume.

### Note

The `INCREMENTAL_COPY` option is only for updating an existing volume by using a snapshot from another FSx for OpenZFS file system. For more information, see [CopySnapshotAndUpdateVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CopySnapshotAndUpdateVolume.html) .

ReadOnly -> (boolean)

A Boolean value indicating whether the volume is read-only.

NfsExports -> (list)

The configuration object for mounting a Network File System (NFS) file system.

(structure)

The Network File System (NFS) configurations for mounting an Amazon FSx for OpenZFS file system.

ClientConfigurations -> (list)

A list of configuration objects that contain the client and options for mounting the OpenZFS file system.

(structure)

Specifies who can mount an OpenZFS file system and the options available while mounting the file system.

Clients -> (string)

A value that specifies who can mount the file system. You can provide a wildcard character (`*` ), an IP address (`0.0.0.0` ), or a CIDR address (`192.0.2.0/24` ). By default, Amazon FSx uses the wildcard character when specifying the client.

Options -> (list)

The options to use when mounting the file system. For a list of options that you can use with Network File System (NFS), see the [exports(5) - Linux man page](https://linux.die.net/man/5/exports) . When choosing your options, consider the following:

- `crossmnt` is used by default. If you donât specify `crossmnt` when changing the client configuration, you wonât be able to see or access snapshots in your file systemâs snapshot directory.
- `sync` is used by default. If you instead specify `async` , the system acknowledges writes before writing to disk. If the system crashes before the writes are finished, you lose the unwritten data.

(string)

UserAndGroupQuotas -> (list)

An object specifying how much storage users or groups can use on the volume.

(structure)

Used to configure quotas that define how much storage a user or group can use on an FSx for OpenZFS volume. For more information, see [Volume properties](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-volumes.html#volume-properties) in the FSx for OpenZFS User Guide.

Type -> (string)

Specifies whether the quota applies to a user or group.

Id -> (integer)

The ID of the user or group that the quota applies to.

StorageCapacityQuotaGiB -> (integer)

The user or groupâs storage quota, in gibibytes (GiB).

RestoreToSnapshot -> (string)

Specifies the ID of the snapshot to which the volume was restored.

DeleteIntermediateSnaphots -> (boolean)

A Boolean value indicating whether snapshots between the current state and the specified snapshot should be deleted when a volume is restored from snapshot.

DeleteClonedVolumes -> (boolean)

A Boolean value indicating whether dependent clone volumes created from intermediate snapshots should be deleted when a volume is restored from snapshot.

DeleteIntermediateData -> (boolean)

A Boolean value indicating whether snapshot data that differs between the current state and the specified snapshot should be overwritten when a volume is restored from a snapshot.

SourceSnapshotARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

DestinationSnapshot -> (string)

The ID of the snapshot thatâs being copied or was most recently copied to the destination volume.

CopyStrategy -> (string)

Specifies the strategy used when copying data from the snapshot to the new volume.

- `CLONE` - The new volume references the data in the origin snapshot. Cloning a snapshot is faster than copying data from the snapshot to a new volume and doesnât consume disk throughput. However, the origin snapshot canât be deleted if there is a volume using its copied data.
- `FULL_COPY` - Copies all data from the snapshot to the new volume. Specify this option to create the volume from a snapshot on another FSx for OpenZFS file system.

### Note

The `INCREMENTAL_COPY` option is only for updating an existing volume by using a snapshot from another FSx for OpenZFS file system. For more information, see [CopySnapshotAndUpdateVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CopySnapshotAndUpdateVolume.html) .

TargetSnapshotValues -> (structure)

A snapshot of an Amazon FSx for OpenZFS volume.

ResourceARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

SnapshotId -> (string)

The ID of the snapshot.

Name -> (string)

The name of the snapshot.

VolumeId -> (string)

The ID of the volume that the snapshot is of.

CreationTime -> (timestamp)

The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

Lifecycle -> (string)

The lifecycle status of the snapshot.

- `PENDING` - Amazon FSx hasnât started creating the snapshot.
- `CREATING` - Amazon FSx is creating the snapshot.
- `DELETING` - Amazon FSx is deleting the snapshot.
- `AVAILABLE` - The snapshot is fully available.

LifecycleTransitionReason -> (structure)

Describes why a resource lifecycle state changed.

Message -> (string)

A detailed error message.

Tags -> (list)

A list of `Tag` values, with a maximum of 50 elements.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

TotalTransferBytes -> (long)

The number of bytes that have transferred for the FSx for OpenZFS snapshot that youâre copying.

RemainingTransferBytes -> (long)

The remaining bytes to transfer for the FSx for OpenZFS snapshot that youâre copying.

TotalTransferBytes -> (long)

The number of bytes that have transferred for the FSx for OpenZFS snapshot that youâre copying.

RemainingTransferBytes -> (long)

The remaining bytes to transfer for the FSx for OpenZFS snapshot that youâre copying.

OpenZFSConfiguration -> (structure)

The configuration of an Amazon FSx for OpenZFS volume.

ParentVolumeId -> (string)

The ID of the parent volume.

VolumePath -> (string)

The path to the volume from the root volume. For example, `fsx/parentVolume/volume1` .

StorageCapacityReservationGiB -> (integer)

The amount of storage in gibibytes (GiB) to reserve from the parent volume. You canât reserve more storage than the parent volume has reserved.

StorageCapacityQuotaGiB -> (integer)

The maximum amount of storage in gibibytes (GiB) that the volume can use from its parent. You can specify a quota larger than the storage on the parent volume.

RecordSizeKiB -> (integer)

The record size of an OpenZFS volume, in kibibytes (KiB). Valid values are 4, 8, 16, 32, 64, 128, 256, 512, or 1024 KiB. The default is 128 KiB. Most workloads should use the default record size. For guidance on when to set a custom record size, see the *Amazon FSx for OpenZFS User Guide* .

DataCompressionType -> (string)

Specifies the method used to compress the data on the volume. The compression type is `NONE` by default.

- `NONE` - Doesnât compress the data on the volume. `NONE` is the default.
- `ZSTD` - Compresses the data in the volume using the Zstandard (ZSTD) compression algorithm. Compared to LZ4, Z-Standard provides a better compression ratio to minimize on-disk storage utilization.
- `LZ4` - Compresses the data in the volume using the LZ4 compression algorithm. Compared to Z-Standard, LZ4 is less compute-intensive and delivers higher write throughput speeds.

CopyTagsToSnapshots -> (boolean)

A Boolean value indicating whether tags for the volume should be copied to snapshots. This value defaults to `false` . If itâs set to `true` , all tags for the volume are copied to snapshots where the user doesnât specify tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.

OriginSnapshot -> (structure)

The configuration object that specifies the snapshot to use as the origin of the data for the volume.

SnapshotARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

CopyStrategy -> (string)

The strategy used when copying data from the snapshot to the new volume.

- `CLONE` - The new volume references the data in the origin snapshot. Cloning a snapshot is faster than copying the data from a snapshot to a new volume and doesnât consume disk throughput. However, the origin snapshot canât be deleted if there is a volume using its copied data.
- `FULL_COPY` - Copies all data from the snapshot to the new volume.

### Note

The `INCREMENTAL_COPY` option is only for updating an existing volume by using a snapshot from another FSx for OpenZFS file system. For more information, see [CopySnapshotAndUpdateVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CopySnapshotAndUpdateVolume.html) .

ReadOnly -> (boolean)

A Boolean value indicating whether the volume is read-only.

NfsExports -> (list)

The configuration object for mounting a Network File System (NFS) file system.

(structure)

The Network File System (NFS) configurations for mounting an Amazon FSx for OpenZFS file system.

ClientConfigurations -> (list)

A list of configuration objects that contain the client and options for mounting the OpenZFS file system.

(structure)

Specifies who can mount an OpenZFS file system and the options available while mounting the file system.

Clients -> (string)

A value that specifies who can mount the file system. You can provide a wildcard character (`*` ), an IP address (`0.0.0.0` ), or a CIDR address (`192.0.2.0/24` ). By default, Amazon FSx uses the wildcard character when specifying the client.

Options -> (list)

The options to use when mounting the file system. For a list of options that you can use with Network File System (NFS), see the [exports(5) - Linux man page](https://linux.die.net/man/5/exports) . When choosing your options, consider the following:

- `crossmnt` is used by default. If you donât specify `crossmnt` when changing the client configuration, you wonât be able to see or access snapshots in your file systemâs snapshot directory.
- `sync` is used by default. If you instead specify `async` , the system acknowledges writes before writing to disk. If the system crashes before the writes are finished, you lose the unwritten data.

(string)

UserAndGroupQuotas -> (list)

An object specifying how much storage users or groups can use on the volume.

(structure)

Used to configure quotas that define how much storage a user or group can use on an FSx for OpenZFS volume. For more information, see [Volume properties](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-volumes.html#volume-properties) in the FSx for OpenZFS User Guide.

Type -> (string)

Specifies whether the quota applies to a user or group.

Id -> (integer)

The ID of the user or group that the quota applies to.

StorageCapacityQuotaGiB -> (integer)

The user or groupâs storage quota, in gibibytes (GiB).

RestoreToSnapshot -> (string)

Specifies the ID of the snapshot to which the volume was restored.

DeleteIntermediateSnaphots -> (boolean)

A Boolean value indicating whether snapshots between the current state and the specified snapshot should be deleted when a volume is restored from snapshot.

DeleteClonedVolumes -> (boolean)

A Boolean value indicating whether dependent clone volumes created from intermediate snapshots should be deleted when a volume is restored from snapshot.

DeleteIntermediateData -> (boolean)

A Boolean value indicating whether snapshot data that differs between the current state and the specified snapshot should be overwritten when a volume is restored from a snapshot.

SourceSnapshotARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

DestinationSnapshot -> (string)

The ID of the snapshot thatâs being copied or was most recently copied to the destination volume.

CopyStrategy -> (string)

Specifies the strategy used when copying data from the snapshot to the new volume.

- `CLONE` - The new volume references the data in the origin snapshot. Cloning a snapshot is faster than copying data from the snapshot to a new volume and doesnât consume disk throughput. However, the origin snapshot canât be deleted if there is a volume using its copied data.
- `FULL_COPY` - Copies all data from the snapshot to the new volume. Specify this option to create the volume from a snapshot on another FSx for OpenZFS file system.

### Note

The `INCREMENTAL_COPY` option is only for updating an existing volume by using a snapshot from another FSx for OpenZFS file system. For more information, see [CopySnapshotAndUpdateVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CopySnapshotAndUpdateVolume.html) .