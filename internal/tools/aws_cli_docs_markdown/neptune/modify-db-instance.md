# modify-db-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/modify-db-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/modify-db-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [neptune](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/index.html#cli-aws-neptune) ]

# modify-db-instance

## Description

Modifies settings for a DB instance. You can change one or more database configuration parameters by specifying these parameters and the new values in the request. To learn what modifications you can make to your DB instance, call  DescribeValidDBInstanceModifications before you call  ModifyDBInstance .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/ModifyDBInstance)

## Synopsis

```
modify-db-instance
--db-instance-identifier <value>
[--allocated-storage <value>]
[--db-instance-class <value>]
[--db-subnet-group-name <value>]
[--db-security-groups <value>]
[--vpc-security-group-ids <value>]
[--apply-immediately | --no-apply-immediately]
[--master-user-password <value>]
[--db-parameter-group-name <value>]
[--backup-retention-period <value>]
[--preferred-backup-window <value>]
[--preferred-maintenance-window <value>]
[--multi-az | --no-multi-az]
[--engine-version <value>]
[--allow-major-version-upgrade | --no-allow-major-version-upgrade]
[--auto-minor-version-upgrade | --no-auto-minor-version-upgrade]
[--license-model <value>]
[--iops <value>]
[--option-group-name <value>]
[--new-db-instance-identifier <value>]
[--storage-type <value>]
[--tde-credential-arn <value>]
[--tde-credential-password <value>]
[--ca-certificate-identifier <value>]
[--domain <value>]
[--copy-tags-to-snapshot | --no-copy-tags-to-snapshot]
[--monitoring-interval <value>]
[--db-port-number <value>]
[--publicly-accessible | --no-publicly-accessible]
[--monitoring-role-arn <value>]
[--domain-iam-role-name <value>]
[--promotion-tier <value>]
[--enable-iam-database-authentication | --no-enable-iam-database-authentication]
[--enable-performance-insights | --no-enable-performance-insights]
[--performance-insights-kms-key-id <value>]
[--cloudwatch-logs-export-configuration <value>]
[--deletion-protection | --no-deletion-protection]
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

`--db-instance-identifier` (string)

The DB instance identifier. This value is stored as a lowercase string.

Constraints:

- Must match the identifier of an existing DBInstance.

`--allocated-storage` (integer)

Not supported by Neptune.

`--db-instance-class` (string)

The new compute and memory capacity of the DB instance, for example, `db.m4.large` . Not all DB instance classes are available in all Amazon Regions.

If you modify the DB instance class, an outage occurs during the change. The change is applied during the next maintenance window, unless `ApplyImmediately` is specified as `true` for this request.

Default: Uses existing setting

`--db-subnet-group-name` (string)

The new DB subnet group for the DB instance. You can use this parameter to move your DB instance to a different VPC.

Changing the subnet group causes an outage during the change. The change is applied during the next maintenance window, unless you specify `true` for the `ApplyImmediately` parameter.

Constraints: If supplied, must match the name of an existing DBSubnetGroup.

Example: `mySubnetGroup`

`--db-security-groups` (list)

A list of DB security groups to authorize on this DB instance. Changing this setting doesnât result in an outage and the change is asynchronously applied as soon as possible.

Constraints:

- If supplied, must match existing DBSecurityGroups.

(string)

Syntax:

```
"string" "string" ...
```

`--vpc-security-group-ids` (list)

A list of EC2 VPC security groups to authorize on this DB instance. This change is asynchronously applied as soon as possible.

Not applicable. The associated list of EC2 VPC security groups is managed by the DB cluster. For more information, see  ModifyDBCluster .

Constraints:

- If supplied, must match existing VpcSecurityGroupIds.

(string)

Syntax:

```
"string" "string" ...
```

`--apply-immediately` | `--no-apply-immediately` (boolean)

Specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the `PreferredMaintenanceWindow` setting for the DB instance.

If this parameter is set to `false` , changes to the DB instance are applied during the next maintenance window. Some parameter changes can cause an outage and are applied on the next call to  RebootDBInstance , or the next failure reboot.

Default: `false`

`--master-user-password` (string)

Not supported by Neptune.

`--db-parameter-group-name` (string)

The name of the DB parameter group to apply to the DB instance. Changing this setting doesnât result in an outage. The parameter group name itself is changed immediately, but the actual parameter changes are not applied until you reboot the instance without failover. The db instance will NOT be rebooted automatically and the parameter changes will NOT be applied during the next maintenance window.

Default: Uses existing setting

Constraints: The DB parameter group must be in the same DB parameter group family as this DB instance.

`--backup-retention-period` (integer)

Not applicable. The retention period for automated backups is managed by the DB cluster. For more information, see  ModifyDBCluster .

Default: Uses existing setting

`--preferred-backup-window` (string)

The daily time range during which automated backups are created if automated backups are enabled.

Not applicable. The daily time range for creating automated backups is managed by the DB cluster. For more information, see  ModifyDBCluster .

Constraints:

- Must be in the format hh24:mi-hh24:mi
- Must be in Universal Time Coordinated (UTC)
- Must not conflict with the preferred maintenance window
- Must be at least 30 minutes

`--preferred-maintenance-window` (string)

The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter doesnât result in an outage, except in the following situation, and the change is asynchronously applied as soon as possible. If there are pending actions that cause a reboot, and the maintenance window is changed to include the current time, then changing this parameter will cause a reboot of the DB instance. If moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure pending changes are applied.

Default: Uses existing setting

Format: ddd:hh24:mi-ddd:hh24:mi

Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun

Constraints: Must be at least 30 minutes

`--multi-az` | `--no-multi-az` (boolean)

Specifies if the DB instance is a Multi-AZ deployment. Changing this parameter doesnât result in an outage and the change is applied during the next maintenance window unless the `ApplyImmediately` parameter is set to `true` for this request.

`--engine-version` (string)

The version number of the database engine to upgrade to. Currently, setting this parameter has no effect. To upgrade your database engine to the most recent release, use the  ApplyPendingMaintenanceAction API.

`--allow-major-version-upgrade` | `--no-allow-major-version-upgrade` (boolean)

Indicates that major version upgrades are allowed. Changing this parameter doesnât result in an outage and the change is asynchronously applied as soon as possible.

`--auto-minor-version-upgrade` | `--no-auto-minor-version-upgrade` (boolean)

Indicates that minor version upgrades are applied automatically to the DB instance during the maintenance window. Changing this parameter doesnât result in an outage except in the following case and the change is asynchronously applied as soon as possible. An outage will result if this parameter is set to `true` during the maintenance window, and a newer minor version is available, and Neptune has enabled auto patching for that engine version.

`--license-model` (string)

Not supported by Neptune.

`--iops` (integer)

The new Provisioned IOPS (I/O operations per second) value for the instance.

Changing this setting doesnât result in an outage and the change is applied during the next maintenance window unless the `ApplyImmediately` parameter is set to `true` for this request.

Default: Uses existing setting

`--option-group-name` (string)

*(Not supported by Neptune)*

`--new-db-instance-identifier` (string)

The new DB instance identifier for the DB instance when renaming a DB instance. When you change the DB instance identifier, an instance reboot will occur immediately if you set `Apply Immediately` to true, or will occur during the next maintenance window if `Apply Immediately` to false. This value is stored as a lowercase string.

Constraints:

- Must contain from 1 to 63 letters, numbers, or hyphens.
- The first character must be a letter.
- Cannot end with a hyphen or contain two consecutive hyphens.

Example: `mydbinstance`

`--storage-type` (string)

Not applicable. In Neptune the storage type is managed at the DB Cluster level.

`--tde-credential-arn` (string)

The ARN from the key store with which to associate the instance for TDE encryption.

`--tde-credential-password` (string)

The password for the given ARN from the key store in order to access the device.

`--ca-certificate-identifier` (string)

Indicates the certificate that needs to be associated with the instance.

`--domain` (string)

Not supported.

`--copy-tags-to-snapshot` | `--no-copy-tags-to-snapshot` (boolean)

True to copy all tags from the DB instance to snapshots of the DB instance, and otherwise false. The default is false.

`--monitoring-interval` (integer)

The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.

If `MonitoringRoleArn` is specified, then you must also set `MonitoringInterval` to a value other than 0.

Valid Values: `0, 1, 5, 10, 15, 30, 60`

`--db-port-number` (integer)

The port number on which the database accepts connections.

The value of the `DBPortNumber` parameter must not match any of the port values specified for options in the option group for the DB instance.

Your database will restart when you change the `DBPortNumber` value regardless of the value of the `ApplyImmediately` parameter.

Default: `8182`

`--publicly-accessible` | `--no-publicly-accessible` (boolean)

This flag should no longer be used.

`--monitoring-role-arn` (string)

The ARN for the IAM role that permits Neptune to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, `arn:aws:iam:123456789012:role/emaccess` .

If `MonitoringInterval` is set to a value other than 0, then you must supply a `MonitoringRoleArn` value.

`--domain-iam-role-name` (string)

Not supported

`--promotion-tier` (integer)

A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.

Default: 1

Valid Values: 0 - 15

`--enable-iam-database-authentication` | `--no-enable-iam-database-authentication` (boolean)

True to enable mapping of Amazon Identity and Access Management (IAM) accounts to database accounts, and otherwise false.

You can enable IAM database authentication for the following database engines

Not applicable. Mapping Amazon IAM accounts to database accounts is managed by the DB cluster. For more information, see  ModifyDBCluster .

Default: `false`

`--enable-performance-insights` | `--no-enable-performance-insights` (boolean)

*(Not supported by Neptune)*

`--performance-insights-kms-key-id` (string)

*(Not supported by Neptune)*

`--cloudwatch-logs-export-configuration` (structure)

The configuration setting for the log types to be enabled for export to CloudWatch Logs for a specific DB instance or DB cluster.

EnableLogTypes -> (list)

The list of log types to enable.

(string)

DisableLogTypes -> (list)

The list of log types to disable.

(string)

Shorthand Syntax:

```
EnableLogTypes=string,string,DisableLogTypes=string,string
```

JSON Syntax:

```
{
  "EnableLogTypes": ["string", ...],
  "DisableLogTypes": ["string", ...]
}
```

`--deletion-protection` | `--no-deletion-protection` (boolean)

A value that indicates whether the DB instance has deletion protection enabled. The database canât be deleted when deletion protection is enabled. By default, deletion protection is disabled. See [Deleting a DB Instance](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-instances-delete.html) .

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

DBInstance -> (structure)

Contains the details of an Amazon Neptune DB instance.

This data type is used as a response element in the  DescribeDBInstances action.

DBInstanceIdentifier -> (string)

Contains a user-supplied database identifier. This identifier is the unique key that identifies a DB instance.

DBInstanceClass -> (string)

Contains the name of the compute and memory capacity class of the DB instance.

Engine -> (string)

Provides the name of the database engine to be used for this DB instance.

DBInstanceStatus -> (string)

Specifies the current state of this database.

MasterUsername -> (string)

Not supported by Neptune.

DBName -> (string)

The database name.

Endpoint -> (structure)

Specifies the connection endpoint.

Address -> (string)

Specifies the DNS address of the DB instance.

Port -> (integer)

Specifies the port that the database engine is listening on.

HostedZoneId -> (string)

Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

AllocatedStorage -> (integer)

Not supported by Neptune.

InstanceCreateTime -> (timestamp)

Provides the date and time the DB instance was created.

PreferredBackupWindow -> (string)

Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the `BackupRetentionPeriod` .

BackupRetentionPeriod -> (integer)

Specifies the number of days for which automatic DB snapshots are retained.

DBSecurityGroups -> (list)

Provides List of DB security group elements containing only `DBSecurityGroup.Name` and `DBSecurityGroup.Status` subelements.

(structure)

Specifies membership in a designated DB security group.

DBSecurityGroupName -> (string)

The name of the DB security group.

Status -> (string)

The status of the DB security group.

VpcSecurityGroups -> (list)

Provides a list of VPC security group elements that the DB instance belongs to.

(structure)

This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId -> (string)

The name of the VPC security group.

Status -> (string)

The status of the VPC security group.

DBParameterGroups -> (list)

Provides the list of DB parameter groups applied to this DB instance.

(structure)

The status of the DB parameter group.

This data type is used as a response element in the following actions:

- CreateDBInstance
- DeleteDBInstance
- ModifyDBInstance
- RebootDBInstance

DBParameterGroupName -> (string)

The name of the DP parameter group.

ParameterApplyStatus -> (string)

The status of parameter updates.

AvailabilityZone -> (string)

Specifies the name of the Availability Zone the DB instance is located in.

DBSubnetGroup -> (structure)

Specifies information on the subnet group associated with the DB instance, including the name, description, and subnets in the subnet group.

DBSubnetGroupName -> (string)

The name of the DB subnet group.

DBSubnetGroupDescription -> (string)

Provides the description of the DB subnet group.

VpcId -> (string)

Provides the VpcId of the DB subnet group.

SubnetGroupStatus -> (string)

Provides the status of the DB subnet group.

Subnets -> (list)

Contains a list of  Subnet elements.

(structure)

Specifies a subnet.

This data type is used as a response element in the  DescribeDBSubnetGroups action.

SubnetIdentifier -> (string)

Specifies the identifier of the subnet.

SubnetAvailabilityZone -> (structure)

Specifies the EC2 Availability Zone that the subnet is in.

Name -> (string)

The name of the availability zone.

SubnetStatus -> (string)

Specifies the status of the subnet.

DBSubnetGroupArn -> (string)

The Amazon Resource Name (ARN) for the DB subnet group.

PreferredMaintenanceWindow -> (string)

Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

PendingModifiedValues -> (structure)

Specifies that changes to the DB instance are pending. This element is only included when changes are pending. Specific changes are identified by subelements.

DBInstanceClass -> (string)

Contains the new `DBInstanceClass` for the DB instance that will be applied or is currently being applied.

AllocatedStorage -> (integer)

Contains the new `AllocatedStorage` size for the DB instance that will be applied or is currently being applied.

MasterUserPassword -> (string)

Not supported by Neptune.

Port -> (integer)

Specifies the pending port for the DB instance.

BackupRetentionPeriod -> (integer)

Specifies the pending number of days for which automated backups are retained.

MultiAZ -> (boolean)

Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

EngineVersion -> (string)

Indicates the database engine version.

LicenseModel -> (string)

Not supported by Neptune.

Iops -> (integer)

Specifies the new Provisioned IOPS value for the DB instance that will be applied or is currently being applied.

DBInstanceIdentifier -> (string)

Contains the new `DBInstanceIdentifier` for the DB instance that will be applied or is currently being applied.

StorageType -> (string)

Not applicable. In Neptune the storage type is managed at the DB Cluster level.

CACertificateIdentifier -> (string)

Specifies the identifier of the CA certificate for the DB instance.

DBSubnetGroupName -> (string)

The new DB subnet group for the DB instance.

PendingCloudwatchLogsExports -> (structure)

This `PendingCloudwatchLogsExports` structure specifies pending changes to which CloudWatch logs are enabled and which are disabled.

LogTypesToEnable -> (list)

Log types that are in the process of being deactivated. After they are deactivated, these log types arenât exported to CloudWatch Logs.

(string)

LogTypesToDisable -> (list)

Log types that are in the process of being enabled. After they are enabled, these log types are exported to CloudWatch Logs.

(string)

LatestRestorableTime -> (timestamp)

Specifies the latest time to which a database can be restored with point-in-time restore.

MultiAZ -> (boolean)

Specifies if the DB instance is a Multi-AZ deployment.

EngineVersion -> (string)

Indicates the database engine version.

AutoMinorVersionUpgrade -> (boolean)

Indicates that minor version patches are applied automatically.

ReadReplicaSourceDBInstanceIdentifier -> (string)

Contains the identifier of the source DB instance if this DB instance is a Read Replica.

ReadReplicaDBInstanceIdentifiers -> (list)

Contains one or more identifiers of the Read Replicas associated with this DB instance.

(string)

ReadReplicaDBClusterIdentifiers -> (list)

Contains one or more identifiers of DB clusters that are Read Replicas of this DB instance.

(string)

LicenseModel -> (string)

License model information for this DB instance.

Iops -> (integer)

Specifies the Provisioned IOPS (I/O operations per second) value.

OptionGroupMemberships -> (list)

*(Not supported by Neptune)*

(structure)

Not supported by Neptune.

OptionGroupName -> (string)

Not supported by Neptune.

Status -> (string)

Not supported by Neptune.

CharacterSetName -> (string)

*(Not supported by Neptune)*

SecondaryAvailabilityZone -> (string)

If present, specifies the name of the secondary Availability Zone for a DB instance with multi-AZ support.

PubliclyAccessible -> (boolean)

This flag should no longer be used.

StatusInfos -> (list)

The status of a Read Replica. If the instance is not a Read Replica, this is blank.

(structure)

Provides a list of status information for a DB instance.

StatusType -> (string)

This value is currently âread replication.â

Normal -> (boolean)

Boolean value that is true if the instance is operating normally, or false if the instance is in an error state.

Status -> (string)

Status of the DB instance. For a StatusType of read replica, the values can be replicating, error, stopped, or terminated.

Message -> (string)

Details of the error if there is an error for the instance. If the instance is not in an error state, this value is blank.

StorageType -> (string)

Specifies the storage type associated with the DB instance.

TdeCredentialArn -> (string)

The ARN from the key store with which the instance is associated for TDE encryption.

DbInstancePort -> (integer)

Specifies the port that the DB instance listens on. If the DB instance is part of a DB cluster, this can be a different port than the DB cluster port.

DBClusterIdentifier -> (string)

If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.

StorageEncrypted -> (boolean)

Not supported: The encryption for DB instances is managed by the DB cluster.

KmsKeyId -> (string)

Not supported: The encryption for DB instances is managed by the DB cluster.

DbiResourceId -> (string)

The Amazon Region-unique, immutable identifier for the DB instance. This identifier is found in Amazon CloudTrail log entries whenever the Amazon KMS key for the DB instance is accessed.

CACertificateIdentifier -> (string)

The identifier of the CA certificate for this DB instance.

DomainMemberships -> (list)

Not supported

(structure)

An Active Directory Domain membership record associated with a DB instance.

Domain -> (string)

The identifier of the Active Directory Domain.

Status -> (string)

The status of the DB instanceâs Active Directory Domain membership, such as joined, pending-join, failed etc).

FQDN -> (string)

The fully qualified domain name of the Active Directory Domain.

IAMRoleName -> (string)

The name of the IAM role to be used when making API calls to the Directory Service.

CopyTagsToSnapshot -> (boolean)

Specifies whether tags are copied from the DB instance to snapshots of the DB instance.

MonitoringInterval -> (integer)

The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.

EnhancedMonitoringResourceArn -> (string)

The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the Enhanced Monitoring metrics data for the DB instance.

MonitoringRoleArn -> (string)

The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.

PromotionTier -> (integer)

A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.

DBInstanceArn -> (string)

The Amazon Resource Name (ARN) for the DB instance.

Timezone -> (string)

Not supported.

IAMDatabaseAuthenticationEnabled -> (boolean)

True if Amazon Identity and Access Management (IAM) authentication is enabled, and otherwise false.

PerformanceInsightsEnabled -> (boolean)

*(Not supported by Neptune)*

PerformanceInsightsKMSKeyId -> (string)

*(Not supported by Neptune)*

EnabledCloudwatchLogsExports -> (list)

A list of log types that this DB instance is configured to export to CloudWatch Logs.

(string)

DeletionProtection -> (boolean)

Indicates whether or not the DB instance has deletion protection enabled. The instance canât be deleted when deletion protection is enabled. See [Deleting a DB Instance](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-instances-delete.html) .