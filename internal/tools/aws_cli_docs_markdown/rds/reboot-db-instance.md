# reboot-db-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/reboot-db-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/reboot-db-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# reboot-db-instance

## Description

You might need to reboot your DB instance, usually for maintenance reasons. For example, if you make certain modifications, or if you change the DB parameter group associated with the DB instance, you must reboot the instance for the changes to take effect.

Rebooting a DB instance restarts the database engine service. Rebooting a DB instance results in a momentary outage, during which the DB instance status is set to rebooting.

For more information about rebooting, see [Rebooting a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RebootInstance.html) in the *Amazon RDS User Guide.*

This command doesnât apply to RDS Custom.

If your DB instance is part of a Multi-AZ DB cluster, you can reboot the DB cluster with the `RebootDBCluster` operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/RebootDBInstance)

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

Specifies whether the reboot is conducted through a Multi-AZ failover.

Constraint: You canât enable force failover if the instance isnât configured for Multi-AZ.

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

**To reboot a DB instance**

The following `reboot-db-instance` example starts a reboot of the specified DB instance.

```
aws rds reboot-db-instance \
    --db-instance-identifier test-mysql-instance
```

Output:

```
{
    "DBInstance": {
        "DBInstanceIdentifier": "test-mysql-instance",
        "DBInstanceClass": "db.t3.micro",
        "Engine": "mysql",
        "DBInstanceStatus": "rebooting",
        "MasterUsername": "admin",
        "Endpoint": {
            "Address": "test-mysql-instance.############.us-west-2.rds.amazonaws.com",
            "Port": 3306,
            "HostedZoneId": "Z1PVIF0EXAMPLE"
        },

    ... output omitted...

    }
}
```

For more information, see [Rebooting a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RebootInstance.html) in the *Amazon RDS User Guide*.

## Output

DBInstance -> (structure)

Contains the details of an Amazon RDS DB instance.

This data type is used as a response element in the operations `CreateDBInstance` , `CreateDBInstanceReadReplica` , `DeleteDBInstance` , `DescribeDBInstances` , `ModifyDBInstance` , `PromoteReadReplica` , `RebootDBInstance` , `RestoreDBInstanceFromDBSnapshot` , `RestoreDBInstanceFromS3` , `RestoreDBInstanceToPointInTime` , `StartDBInstance` , and `StopDBInstance` .

DBInstanceIdentifier -> (string)

The user-supplied database identifier. This identifier is the unique key that identifies a DB instance.

DBInstanceClass -> (string)

The name of the compute and memory capacity class of the DB instance.

Engine -> (string)

The database engine used for this DB instance.

DBInstanceStatus -> (string)

The current state of this database.

For information about DB instance statuses, see [Viewing DB instance status](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/accessing-monitoring.html#Overview.DBInstance.Status) in the *Amazon RDS User Guide.*

AutomaticRestartTime -> (timestamp)

The time when a stopped DB instance is restarted automatically.

MasterUsername -> (string)

The master username for the DB instance.

DBName -> (string)

The initial database name that you provided (if required) when you created the DB instance. This name is returned for the life of your DB instance. For an RDS for Oracle CDB instance, the name identifies the PDB rather than the CDB.

Endpoint -> (structure)

The connection endpoint for the DB instance.

### Note

The endpoint might not be shown for instances with the status of `creating` .

Address -> (string)

Specifies the DNS address of the DB instance.

Port -> (integer)

Specifies the port that the database engine is listening on.

HostedZoneId -> (string)

Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

AllocatedStorage -> (integer)

The amount of storage in gibibytes (GiB) allocated for the DB instance.

InstanceCreateTime -> (timestamp)

The date and time when the DB instance was created.

PreferredBackupWindow -> (string)

The daily time range during which automated backups are created if automated backups are enabled, as determined by the `BackupRetentionPeriod` .

BackupRetentionPeriod -> (integer)

The number of days for which automatic DB snapshots are retained.

DBSecurityGroups -> (list)

A list of DB security group elements containing `DBSecurityGroup.Name` and `DBSecurityGroup.Status` subelements.

(structure)

This data type is used as a response element in the following actions:

- `ModifyDBInstance`
- `RebootDBInstance`
- `RestoreDBInstanceFromDBSnapshot`
- `RestoreDBInstanceToPointInTime`

DBSecurityGroupName -> (string)

The name of the DB security group.

Status -> (string)

The status of the DB security group.

VpcSecurityGroups -> (list)

The list of Amazon EC2 VPC security groups that the DB instance belongs to.

(structure)

This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId -> (string)

The name of the VPC security group.

Status -> (string)

The membership status of the VPC security group.

Currently, the only valid status is `active` .

DBParameterGroups -> (list)

The list of DB parameter groups applied to this DB instance.

(structure)

The status of the DB parameter group.

This data type is used as a response element in the following actions:

- `CreateDBInstance`
- `CreateDBInstanceReadReplica`
- `DeleteDBInstance`
- `ModifyDBInstance`
- `RebootDBInstance`
- `RestoreDBInstanceFromDBSnapshot`

DBParameterGroupName -> (string)

The name of the DB parameter group.

ParameterApplyStatus -> (string)

The status of parameter updates. Valid values are:

- `applying` : The parameter group change is being applied to the database.
- `failed-to-apply` : The parameter group is in an invalid state.
- `in-sync` : The parameter group change is synchronized with the database.
- `pending-database-upgrade` : The parameter group change will be applied after the DB instance is upgraded.
- `pending-reboot` : The parameter group change will be applied after the DB instance reboots.

AvailabilityZone -> (string)

The name of the Availability Zone where the DB instance is located.

DBSubnetGroup -> (structure)

Information about the subnet group associated with the DB instance, including the name, description, and subnets in the subnet group.

DBSubnetGroupName -> (string)

The name of the DB subnet group.

DBSubnetGroupDescription -> (string)

Provides the description of the DB subnet group.

VpcId -> (string)

Provides the VpcId of the DB subnet group.

SubnetGroupStatus -> (string)

Provides the status of the DB subnet group.

Subnets -> (list)

Contains a list of `Subnet` elements.

(structure)

This data type is used as a response element for the `DescribeDBSubnetGroups` operation.

SubnetIdentifier -> (string)

The identifier of the subnet.

SubnetAvailabilityZone -> (structure)

Contains Availability Zone information.

This data type is used as an element in the `OrderableDBInstanceOption` data type.

Name -> (string)

The name of the Availability Zone.

SubnetOutpost -> (structure)

If the subnet is associated with an Outpost, this value specifies the Outpost.

For more information about RDS on Outposts, see [Amazon RDS on Amazon Web Services Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html) in the *Amazon RDS User Guide.*

Arn -> (string)

The Amazon Resource Name (ARN) of the Outpost.

SubnetStatus -> (string)

The status of the subnet.

DBSubnetGroupArn -> (string)

The Amazon Resource Name (ARN) for the DB subnet group.

SupportedNetworkTypes -> (list)

The network type of the DB subnet group.

Valid values:

- `IPV4`
- `DUAL`

A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL` ).

For more information, see [Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon RDS User Guide.*

(string)

PreferredMaintenanceWindow -> (string)

The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

PendingModifiedValues -> (structure)

Information about pending changes to the DB instance. This information is returned only when there are pending changes. Specific changes are identified by subelements.

DBInstanceClass -> (string)

The name of the compute and memory capacity class for the DB instance.

AllocatedStorage -> (integer)

The allocated storage size for the DB instance specified in gibibytes (GiB).

MasterUserPassword -> (string)

The master credentials for the DB instance.

Port -> (integer)

The port for the DB instance.

BackupRetentionPeriod -> (integer)

The number of days for which automated backups are retained.

MultiAZ -> (boolean)

Indicates whether the Single-AZ DB instance will change to a Multi-AZ deployment.

EngineVersion -> (string)

The database engine version.

LicenseModel -> (string)

The license model for the DB instance.

Valid values: `license-included` | `bring-your-own-license` | `general-public-license`

Iops -> (integer)

The Provisioned IOPS value for the DB instance.

DBInstanceIdentifier -> (string)

The database identifier for the DB instance.

StorageType -> (string)

The storage type of the DB instance.

CACertificateIdentifier -> (string)

The identifier of the CA certificate for the DB instance.

For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide* .

DBSubnetGroupName -> (string)

The DB subnet group for the DB instance.

PendingCloudwatchLogsExports -> (structure)

A list of the log types whose configuration is still pending. In other words, these log types are in the process of being activated or deactivated.

LogTypesToEnable -> (list)

Log types that are in the process of being deactivated. After they are deactivated, these log types arenât exported to CloudWatch Logs.

(string)

LogTypesToDisable -> (list)

Log types that are in the process of being enabled. After they are enabled, these log types are exported to CloudWatch Logs.

(string)

ProcessorFeatures -> (list)

The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.

(structure)

Contains the processor features of a DB instance class.

To specify the number of CPU cores, use the `coreCount` feature name for the `Name` parameter. To specify the number of threads per core, use the `threadsPerCore` feature name for the `Name` parameter.

You can set the processor features of the DB instance class for a DB instance when you call one of the following actions:

- `CreateDBInstance`
- `ModifyDBInstance`
- `RestoreDBInstanceFromDBSnapshot`
- `RestoreDBInstanceFromS3`
- `RestoreDBInstanceToPointInTime`

You can view the valid processor values for a particular instance class by calling the `DescribeOrderableDBInstanceOptions` action and specifying the instance class for the `DBInstanceClass` parameter.

In addition, you can use the following actions for DB instance class processor information:

- `DescribeDBInstances`
- `DescribeDBSnapshots`
- `DescribeValidDBInstanceModifications`

If you call `DescribeDBInstances` , `ProcessorFeature` returns non-null values only if the following conditions are met:

- You are accessing an Oracle DB instance.
- Your Oracle DB instance class supports configuring the number of CPU cores and threads per core.
- The current number CPU cores and threads is set to a non-default value.

For more information, see [Configuring the processor for a DB instance class in RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor) in the *Amazon RDS User Guide.*

Name -> (string)

The name of the processor feature. Valid names are `coreCount` and `threadsPerCore` .

Value -> (string)

The value of a processor feature.

IAMDatabaseAuthenticationEnabled -> (boolean)

Indicates whether mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts is enabled.

AutomationMode -> (string)

The automation mode of the RDS Custom DB instance: `full` or `all-paused` . If `full` , the DB instance automates monitoring and instance recovery. If `all-paused` , the instance pauses automation for the duration set by `--resume-full-automation-mode-minutes` .

ResumeFullAutomationModeTime -> (timestamp)

The number of minutes to pause the automation. When the time period ends, RDS Custom resumes full automation. The minimum value is 60 (default). The maximum value is 1,440.

StorageThroughput -> (integer)

The storage throughput of the DB instance.

Engine -> (string)

The database engine of the DB instance.

DedicatedLogVolume -> (boolean)

Indicates whether the DB instance has a dedicated log volume (DLV) enabled.>

MultiTenant -> (boolean)

Indicates whether the DB instance will change to the multi-tenant configuration (TRUE) or the single-tenant configuration (FALSE).

LatestRestorableTime -> (timestamp)

The latest time to which a database in this DB instance can be restored with point-in-time restore.

MultiAZ -> (boolean)

Indicates whether the DB instance is a Multi-AZ deployment. This setting doesnât apply to RDS Custom DB instances.

EngineVersion -> (string)

The version of the database engine.

AutoMinorVersionUpgrade -> (boolean)

Indicates whether minor version patches are applied automatically.

For more information about automatic minor version upgrades, see [Automatically upgrading the minor engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades) .

ReadReplicaSourceDBInstanceIdentifier -> (string)

The identifier of the source DB instance if this DB instance is a read replica.

ReadReplicaDBInstanceIdentifiers -> (list)

The identifiers of the read replicas associated with this DB instance.

(string)

ReadReplicaDBClusterIdentifiers -> (list)

The identifiers of Aurora DB clusters to which the RDS DB instance is replicated as a read replica. For example, when you create an Aurora read replica of an RDS for MySQL DB instance, the Aurora MySQL DB cluster for the Aurora read replica is shown. This output doesnât contain information about cross-Region Aurora read replicas.

### Note

Currently, each RDS DB instance can have only one Aurora read replica.

(string)

ReplicaMode -> (string)

The open mode of an Oracle read replica. The default is `open-read-only` . For more information, see [Working with Oracle Read Replicas for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.html) in the *Amazon RDS User Guide* .

### Note

This attribute is only supported in RDS for Oracle.

LicenseModel -> (string)

The license model information for this DB instance. This setting doesnât apply to Amazon Aurora or RDS Custom DB instances.

Iops -> (integer)

The Provisioned IOPS (I/O operations per second) value for the DB instance.

OptionGroupMemberships -> (list)

The list of option group memberships for this DB instance.

(structure)

Provides information on the option groups the DB instance is a member of.

OptionGroupName -> (string)

The name of the option group that the instance belongs to.

Status -> (string)

The status of the DB instanceâs option group membership. Valid values are: `in-sync` , `pending-apply` , `pending-removal` , `pending-maintenance-apply` , `pending-maintenance-removal` , `applying` , `removing` , and `failed` .

CharacterSetName -> (string)

If present, specifies the name of the character set that this instance is associated with.

NcharCharacterSetName -> (string)

The name of the NCHAR character set for the Oracle DB instance. This character set specifies the Unicode encoding for data stored in table columns of type NCHAR, NCLOB, or NVARCHAR2.

SecondaryAvailabilityZone -> (string)

If present, specifies the name of the secondary Availability Zone for a DB instance with multi-AZ support.

PubliclyAccessible -> (boolean)

Indicates whether the DB instance is publicly accessible.

When the DB instance is publicly accessible and you connect from outside of the DB instanceâs virtual private cloud (VPC), its Domain Name System (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB instance, the endpoint resolves to the private IP address. Access to the DB cluster is ultimately controlled by the security group it uses. That public access isnât permitted if the security group assigned to the DB cluster doesnât permit it.

When the DB instance isnât publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.

For more information, see  CreateDBInstance .

StatusInfos -> (list)

The status of a read replica. If the DB instance isnât a read replica, the value is blank.

(structure)

Provides a list of status information for a DB instance.

StatusType -> (string)

This value is currently âread replication.â

Normal -> (boolean)

Indicates whether the instance is operating normally (TRUE) or is in an error state (FALSE).

Status -> (string)

The status of the DB instance. For a StatusType of read replica, the values can be replicating, replication stop point set, replication stop point reached, error, stopped, or terminated.

Message -> (string)

Details of the error if there is an error for the instance. If the instance isnât in an error state, this value is blank.

StorageType -> (string)

The storage type associated with the DB instance.

TdeCredentialArn -> (string)

The ARN from the key store with which the instance is associated for TDE encryption.

DbInstancePort -> (integer)

The port that the DB instance listens on. If the DB instance is part of a DB cluster, this can be a different port than the DB cluster port.

DBClusterIdentifier -> (string)

If the DB instance is a member of a DB cluster, indicates the name of the DB cluster that the DB instance is a member of.

StorageEncrypted -> (boolean)

Indicates whether the DB instance is encrypted.

KmsKeyId -> (string)

If `StorageEncrypted` is enabled, the Amazon Web Services KMS key identifier for the encrypted DB instance.

The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

DbiResourceId -> (string)

The Amazon Web Services Region-unique, immutable identifier for the DB instance. This identifier is found in Amazon Web Services CloudTrail log entries whenever the Amazon Web Services KMS key for the DB instance is accessed.

CACertificateIdentifier -> (string)

The identifier of the CA certificate for this DB instance.

For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide* .

DomainMemberships -> (list)

The Active Directory Domain membership records associated with the DB instance.

(structure)

An Active Directory Domain membership record associated with the DB instance or cluster.

Domain -> (string)

The identifier of the Active Directory Domain.

Status -> (string)

The status of the Active Directory Domain membership for the DB instance or cluster. Values include `joined` , `pending-join` , `failed` , and so on.

FQDN -> (string)

The fully qualified domain name (FQDN) of the Active Directory Domain.

IAMRoleName -> (string)

The name of the IAM role used when making API calls to the Directory Service.

OU -> (string)

The Active Directory organizational unit for the DB instance or cluster.

AuthSecretArn -> (string)

The ARN for the Secrets Manager secret with the credentials for the user thatâs a member of the domain.

DnsIps -> (list)

The IPv4 DNS IP addresses of the primary and secondary Active Directory domain controllers.

(string)

CopyTagsToSnapshot -> (boolean)

Indicates whether tags are copied from the DB instance to snapshots of the DB instance.

This setting doesnât apply to Amazon Aurora DB instances. Copying tags to snapshots is managed by the DB cluster. Setting this value for an Aurora DB instance has no effect on the DB cluster setting. For more information, see `DBCluster` .

MonitoringInterval -> (integer)

The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.

EnhancedMonitoringResourceArn -> (string)

The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the Enhanced Monitoring metrics data for the DB instance.

MonitoringRoleArn -> (string)

The ARN for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.

PromotionTier -> (integer)

The order of priority in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see [Fault Tolerance for an Aurora DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html#Aurora.Managing.FaultTolerance) in the *Amazon Aurora User Guide* .

DBInstanceArn -> (string)

The Amazon Resource Name (ARN) for the DB instance.

Timezone -> (string)

The time zone of the DB instance. In most cases, the `Timezone` element is empty. `Timezone` content appears only for RDS for Db2 and RDS for SQL Server DB instances that were created with a time zone specified.

IAMDatabaseAuthenticationEnabled -> (boolean)

Indicates whether mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts is enabled for the DB instance.

For a list of engine versions that support IAM database authentication, see [IAM database authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.IamDatabaseAuthentication.html) in the *Amazon RDS User Guide* and [IAM database authentication in Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.IAMdbauth.html) in the *Amazon Aurora User Guide* .

DatabaseInsightsMode -> (string)

The mode of Database Insights that is enabled for the instance.

PerformanceInsightsEnabled -> (boolean)

Indicates whether Performance Insights is enabled for the DB instance.

PerformanceInsightsKMSKeyId -> (string)

The Amazon Web Services KMS key identifier for encryption of Performance Insights data.

The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

PerformanceInsightsRetentionPeriod -> (integer)

The number of days to retain Performance Insights data.

Valid Values:

- `7`
- *month* * 31, where *month* is a number of months from 1-23. Examples: `93` (3 months * 31), `341` (11 months * 31), `589` (19 months * 31)
- `731`

Default: `7` days

EnabledCloudwatchLogsExports -> (list)

A list of log types that this DB instance is configured to export to CloudWatch Logs.

Log types vary by DB engine. For information about the log types for each DB engine, see [Monitoring Amazon RDS log files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html) in the *Amazon RDS User Guide.*

(string)

ProcessorFeatures -> (list)

The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.

(structure)

Contains the processor features of a DB instance class.

To specify the number of CPU cores, use the `coreCount` feature name for the `Name` parameter. To specify the number of threads per core, use the `threadsPerCore` feature name for the `Name` parameter.

You can set the processor features of the DB instance class for a DB instance when you call one of the following actions:

- `CreateDBInstance`
- `ModifyDBInstance`
- `RestoreDBInstanceFromDBSnapshot`
- `RestoreDBInstanceFromS3`
- `RestoreDBInstanceToPointInTime`

You can view the valid processor values for a particular instance class by calling the `DescribeOrderableDBInstanceOptions` action and specifying the instance class for the `DBInstanceClass` parameter.

In addition, you can use the following actions for DB instance class processor information:

- `DescribeDBInstances`
- `DescribeDBSnapshots`
- `DescribeValidDBInstanceModifications`

If you call `DescribeDBInstances` , `ProcessorFeature` returns non-null values only if the following conditions are met:

- You are accessing an Oracle DB instance.
- Your Oracle DB instance class supports configuring the number of CPU cores and threads per core.
- The current number CPU cores and threads is set to a non-default value.

For more information, see [Configuring the processor for a DB instance class in RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor) in the *Amazon RDS User Guide.*

Name -> (string)

The name of the processor feature. Valid names are `coreCount` and `threadsPerCore` .

Value -> (string)

The value of a processor feature.

DeletionProtection -> (boolean)

Indicates whether the DB instance has deletion protection enabled. The database canât be deleted when deletion protection is enabled. For more information, see [Deleting a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html) .

AssociatedRoles -> (list)

The Amazon Web Services Identity and Access Management (IAM) roles associated with the DB instance.

(structure)

Information about an Amazon Web Services Identity and Access Management (IAM) role that is associated with a DB instance.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that is associated with the DB instance.

FeatureName -> (string)

The name of the feature associated with the Amazon Web Services Identity and Access Management (IAM) role. For information about supported feature names, see `DBEngineVersion` .

Status -> (string)

Information about the state of association between the IAM role and the DB instance. The Status property returns one of the following values:

- `ACTIVE` - the IAM role ARN is associated with the DB instance and can be used to access other Amazon Web Services services on your behalf.
- `PENDING` - the IAM role ARN is being associated with the DB instance.
- `INVALID` - the IAM role ARN is associated with the DB instance, but the DB instance is unable to assume the IAM role in order to access other Amazon Web Services services on your behalf.

ListenerEndpoint -> (structure)

The listener connection endpoint for SQL Server Always On.

Address -> (string)

Specifies the DNS address of the DB instance.

Port -> (integer)

Specifies the port that the database engine is listening on.

HostedZoneId -> (string)

Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

MaxAllocatedStorage -> (integer)

The upper limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance.

TagList -> (list)

A list of tags.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide* .

(structure)

Metadata assigned to an Amazon RDS resource consisting of a key-value pair.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide* .

Key -> (string)

A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and canât be prefixed with `aws:` or `rds:` . The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â:â, â/â, â=â, â+â, â-â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$â).

Value -> (string)

A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and canât be prefixed with `aws:` or `rds:` . The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â:â, â/â, â=â, â+â, â-â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$â).

DBInstanceAutomatedBackupsReplications -> (list)

The list of replicated automated backups associated with the DB instance.

(structure)

Automated backups of a DB instance replicated to another Amazon Web Services Region. They consist of system backups, transaction logs, and database instance properties.

DBInstanceAutomatedBackupsArn -> (string)

The Amazon Resource Name (ARN) of the replicated automated backups.

CustomerOwnedIpEnabled -> (boolean)

Indicates whether a customer-owned IP address (CoIP) is enabled for an RDS on Outposts DB instance.

A *CoIP* provides local or external connectivity to resources in your Outpost subnets through your on-premises network. For some use cases, a CoIP can provide lower latency for connections to the DB instance from outside of its virtual private cloud (VPC) on your local network.

For more information about RDS on Outposts, see [Working with Amazon RDS on Amazon Web Services Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html) in the *Amazon RDS User Guide* .

For more information about CoIPs, see [Customer-owned IP addresses](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing) in the *Amazon Web Services Outposts User Guide* .

AwsBackupRecoveryPointArn -> (string)

The Amazon Resource Name (ARN) of the recovery point in Amazon Web Services Backup.

ActivityStreamStatus -> (string)

The status of the database activity stream.

ActivityStreamKmsKeyId -> (string)

The Amazon Web Services KMS key identifier used for encrypting messages in the database activity stream. The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

ActivityStreamKinesisStreamName -> (string)

The name of the Amazon Kinesis data stream used for the database activity stream.

ActivityStreamMode -> (string)

The mode of the database activity stream. Database events such as a change or access generate an activity stream event. RDS for Oracle always handles these events asynchronously.

ActivityStreamEngineNativeAuditFieldsIncluded -> (boolean)

Indicates whether engine-native audit fields are included in the database activity stream.

AutomationMode -> (string)

The automation mode of the RDS Custom DB instance: `full` or `all paused` . If `full` , the DB instance automates monitoring and instance recovery. If `all paused` , the instance pauses automation for the duration set by `--resume-full-automation-mode-minutes` .

ResumeFullAutomationModeTime -> (timestamp)

The number of minutes to pause the automation. When the time period ends, RDS Custom resumes full automation. The minimum value is 60 (default). The maximum value is 1,440.

CustomIamInstanceProfile -> (string)

The instance profile associated with the underlying Amazon EC2 instance of an RDS Custom DB instance. The instance profile must meet the following requirements:

- The profile must exist in your account.
- The profile must have an IAM role that Amazon EC2 has permissions to assume.
- The instance profile name and the associated IAM role name must start with the prefix `AWSRDSCustom` .

For the list of permissions required for the IAM role, see [Configure IAM and your VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-setup-orcl.html#custom-setup-orcl.iam-vpc) in the *Amazon RDS User Guide* .

BackupTarget -> (string)

The location where automated backups and manual snapshots are stored: Amazon Web Services Outposts or the Amazon Web Services Region.

NetworkType -> (string)

The network type of the DB instance.

The network type is determined by the `DBSubnetGroup` specified for the DB instance. A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL` ).

For more information, see [Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon RDS User Guide* and [Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon Aurora User Guide.*

Valid Values: `IPV4 | DUAL`

ActivityStreamPolicyStatus -> (string)

The status of the policy state of the activity stream.

StorageThroughput -> (integer)

The storage throughput for the DB instance.

This setting applies only to the `gp3` storage type.

DBSystemId -> (string)

The Oracle system ID (Oracle SID) for a container database (CDB). The Oracle SID is also the name of the CDB. This setting is only valid for RDS Custom DB instances.

MasterUserSecret -> (structure)

The secret managed by RDS in Amazon Web Services Secrets Manager for the master user password.

For more information, see [Password management with Amazon Web Services Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide.*

SecretArn -> (string)

The Amazon Resource Name (ARN) of the secret.

SecretStatus -> (string)

The status of the secret.

The possible status values include the following:

- `creating` - The secret is being created.
- `active` - The secret is available for normal use and rotation.
- `rotating` - The secret is being rotated.
- `impaired` - The secret can be used to access database credentials, but it canât be rotated. A secret might have this status if, for example, permissions are changed so that RDS can no longer access either the secret or the KMS key for the secret. When a secret has this status, you can correct the condition that caused the status. Alternatively, modify the DB instance to turn off automatic management of database credentials, and then modify the DB instance again to turn on automatic management of database credentials.

KmsKeyId -> (string)

The Amazon Web Services KMS key identifier that is used to encrypt the secret.

CertificateDetails -> (structure)

The details of the DB instanceâs server certificate.

CAIdentifier -> (string)

The CA identifier of the CA certificate used for the DB instanceâs server certificate.

ValidTill -> (timestamp)

The expiration date of the DB instanceâs server certificate.

ReadReplicaSourceDBClusterIdentifier -> (string)

The identifier of the source DB cluster if this DB instance is a read replica.

PercentProgress -> (string)

The progress of the storage optimization operation as a percentage.

DedicatedLogVolume -> (boolean)

Indicates whether the DB instance has a dedicated log volume (DLV) enabled.

IsStorageConfigUpgradeAvailable -> (boolean)

Indicates whether an upgrade is recommended for the storage file system configuration on the DB instance. To migrate to the preferred configuration, you can either create a blue/green deployment, or create a read replica from the DB instance. For more information, see [Upgrading the storage file system for a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.UpgradeFileSystem) .

MultiTenant -> (boolean)

Specifies whether the DB instance is in the multi-tenant configuration (TRUE) or the single-tenant configuration (FALSE).

EngineLifecycleSupport -> (string)

The lifecycle type for the DB instance.

For more information, see CreateDBInstance.