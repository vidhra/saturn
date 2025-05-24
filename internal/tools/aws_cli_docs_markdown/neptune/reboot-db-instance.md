# reboot-db-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/reboot-db-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/reboot-db-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [neptune](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/index.html#cli-aws-neptune) ]

# reboot-db-instance

## Description

You might need to reboot your DB instance, usually for maintenance reasons. For example, if you make certain modifications, or if you change the DB parameter group associated with the DB instance, you must reboot the instance for the changes to take effect.

Rebooting a DB instance restarts the database engine service. Rebooting a DB instance results in a momentary outage, during which the DB instance status is set to rebooting.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/RebootDBInstance)

## Synopsis

```
reboot-db-instance
--db-instance-identifier <value>
[--force-failover | --no-force-failover]
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

The DB instance identifier. This parameter is stored as a lowercase string.

Constraints:

- Must match the identifier of an existing DBInstance.

`--force-failover` | `--no-force-failover` (boolean)

When `true` , the reboot is conducted through a MultiAZ failover.

Constraint: You canât specify `true` if the instance is not configured for MultiAZ.

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