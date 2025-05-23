# modify-db-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# modify-db-instance

## Description

Modifies settings for a DB instance. You can change one or more database configuration parameters by specifying these parameters and the new values in the request. To learn what modifications you can make to your DB instance, call `DescribeValidDBInstanceModifications` before you call `ModifyDBInstance` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/ModifyDBInstance)

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
[--domain-fqdn <value>]
[--domain-ou <value>]
[--domain-auth-secret-arn <value>]
[--domain-dns-ips <value>]
[--copy-tags-to-snapshot | --no-copy-tags-to-snapshot]
[--monitoring-interval <value>]
[--db-port-number <value>]
[--publicly-accessible | --no-publicly-accessible]
[--monitoring-role-arn <value>]
[--domain-iam-role-name <value>]
[--disable-domain | --no-disable-domain]
[--promotion-tier <value>]
[--enable-iam-database-authentication | --no-enable-iam-database-authentication]
[--database-insights-mode <value>]
[--enable-performance-insights | --no-enable-performance-insights]
[--performance-insights-kms-key-id <value>]
[--performance-insights-retention-period <value>]
[--cloudwatch-logs-export-configuration <value>]
[--processor-features <value>]
[--use-default-processor-features | --no-use-default-processor-features]
[--deletion-protection | --no-deletion-protection]
[--max-allocated-storage <value>]
[--certificate-rotation-restart | --no-certificate-rotation-restart]
[--replica-mode <value>]
[--enable-customer-owned-ip | --no-enable-customer-owned-ip]
[--aws-backup-recovery-point-arn <value>]
[--automation-mode <value>]
[--resume-full-automation-mode-minutes <value>]
[--network-type <value>]
[--storage-throughput <value>]
[--manage-master-user-password | --no-manage-master-user-password]
[--rotate-master-user-password | --no-rotate-master-user-password]
[--master-user-secret-kms-key-id <value>]
[--engine <value>]
[--dedicated-log-volume | --no-dedicated-log-volume]
[--multi-tenant | --no-multi-tenant]
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

The identifier of DB instance to modify. This value is stored as a lowercase string.

Constraints:

- Must match the identifier of an existing DB instance.

`--allocated-storage` (integer)

The new amount of storage in gibibytes (GiB) to allocate for the DB instance.

For RDS for Db2, MariaDB, RDS for MySQL, RDS for Oracle, and RDS for PostgreSQL, the value supplied must be at least 10% greater than the current value. Values that are not at least 10% greater than the existing value are rounded up so that they are 10% greater than the current value.

For the valid values for allocated storage for each engine, see `CreateDBInstance` .

Constraints:

- When you increase the allocated storage for a DB instance that uses Provisioned IOPS (`gp3` , `io1` , or `io2` storage type), you must also specify the `Iops` parameter. You can use the current value for `Iops` .

`--db-instance-class` (string)

The new compute and memory capacity of the DB instance, for example `db.m4.large` . Not all DB instance classes are available in all Amazon Web Services Regions, or for all database engines. For the full list of DB instance classes, and availability for your engine, see [DB Instance Class](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the *Amazon RDS User Guide* or [Aurora DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html) in the *Amazon Aurora User Guide* . For RDS Custom, see [DB instance class support for RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits.html#custom-reqs-limits.instances) and [DB instance class support for RDS Custom for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits-MS.html#custom-reqs-limits.instancesMS) .

If you modify the DB instance class, an outage occurs during the change. The change is applied during the next maintenance window, unless you specify `ApplyImmediately` in your request.

Default: Uses existing setting

Constraints:

- If you are modifying the DB instance class and upgrading the engine version at the same time, the currently running engine version must be supported on the specified DB instance class. Otherwise, the operation returns an error. In this case, first run the operation to upgrade the engine version, and then run it again to modify the DB instance class.

`--db-subnet-group-name` (string)

The new DB subnet group for the DB instance. You can use this parameter to move your DB instance to a different VPC. If your DB instance isnât in a VPC, you can also use this parameter to move your DB instance into a VPC. For more information, see [Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Non-VPC2VPC) in the *Amazon RDS User Guide* .

Changing the subnet group causes an outage during the change. The change is applied during the next maintenance window, unless you enable `ApplyImmediately` .

This setting doesnât apply to RDS Custom DB instances.

Constraints:

- If supplied, must match existing DB subnet group.

Example: `mydbsubnetgroup`

`--db-security-groups` (list)

A list of DB security groups to authorize on this DB instance. Changing this setting doesnât result in an outage and the change is asynchronously applied as soon as possible.

This setting doesnât apply to RDS Custom DB instances.

Constraints:

- If supplied, must match existing DB security groups.

(string)

Syntax:

```
"string" "string" ...
```

`--vpc-security-group-ids` (list)

A list of Amazon EC2 VPC security groups to associate with this DB instance. This change is asynchronously applied as soon as possible.

This setting doesnât apply to the following DB instances:

- Amazon Aurora (The associated list of EC2 VPC security groups is managed by the DB cluster. For more information, see `ModifyDBCluster` .)
- RDS Custom

Constraints:

- If supplied, must match existing VPC security group IDs.

(string)

Syntax:

```
"string" "string" ...
```

`--apply-immediately` | `--no-apply-immediately` (boolean)

Specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the `PreferredMaintenanceWindow` setting for the DB instance. By default, this parameter is disabled.

If this parameter is disabled, changes to the DB instance are applied during the next maintenance window. Some parameter changes can cause an outage and are applied on the next call to  RebootDBInstance , or the next failure reboot. Review the table of parameters in [Modifying a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html) in the *Amazon RDS User Guide* to see the impact of enabling or disabling `ApplyImmediately` for each modified parameter and to determine when the changes are applied.

`--master-user-password` (string)

The new password for the master user.

Changing this parameter doesnât result in an outage and the change is asynchronously applied as soon as possible. Between the time of the request and the completion of the request, the `MasterUserPassword` element exists in the `PendingModifiedValues` element of the operation response.

### Note

Amazon RDS API operations never return the password, so this operation provides a way to regain access to a primary instance user if the password is lost. This includes restoring privileges that might have been accidentally revoked.

This setting doesnât apply to the following DB instances:

- Amazon Aurora The password for the master user is managed by the DB cluster. For more information, see `ModifyDBCluster` .
- RDS Custom
- RDS for Oracle CDBs in the multi-tenant configuration Specify the master password in `ModifyTenantDatabase` instead.

Default: Uses existing setting

Constraints:

- Canât be specified if `ManageMasterUserPassword` is turned on.
- Can include any printable ASCII character except â/â, âââ, or â@â. For RDS for Oracle, canât include the â&â (ampersand) or the âââ (single quotes) character.

Length Constraints:

- RDS for Db2 - Must contain from 8 to 255 characters.
- RDS for MariaDB - Must contain from 8 to 41 characters.
- RDS for Microsoft SQL Server - Must contain from 8 to 128 characters.
- RDS for MySQL - Must contain from 8 to 41 characters.
- RDS for Oracle - Must contain from 8 to 30 characters.
- RDS for PostgreSQL - Must contain from 8 to 128 characters.

`--db-parameter-group-name` (string)

The name of the DB parameter group to apply to the DB instance.

Changing this setting doesnât result in an outage. The parameter group name itself is changed immediately, but the actual parameter changes are not applied until you reboot the instance without failover. In this case, the DB instance isnât rebooted automatically, and the parameter changes arenât applied during the next maintenance window. However, if you modify dynamic parameters in the newly associated DB parameter group, these changes are applied immediately without a reboot.

This setting doesnât apply to RDS Custom DB instances.

Default: Uses existing setting

Constraints:

- Must be in the same DB parameter group family as the DB instance.

`--backup-retention-period` (integer)

The number of days to retain automated backups. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.

### Note

Enabling and disabling backups can result in a brief I/O suspension that lasts from a few seconds to a few minutes, depending on the size and class of your DB instance.

These changes are applied during the next maintenance window unless the `ApplyImmediately` parameter is enabled for this request. If you change the parameter from one non-zero value to another non-zero value, the change is asynchronously applied as soon as possible.

This setting doesnât apply to Amazon Aurora DB instances. The retention period for automated backups is managed by the DB cluster. For more information, see `ModifyDBCluster` .

Default: Uses existing setting

Constraints:

- Must be a value from 0 to 35.
- Canât be set to 0 if the DB instance is a source to read replicas.
- Canât be set to 0 for an RDS Custom for Oracle DB instance.

`--preferred-backup-window` (string)

The daily time range during which automated backups are created if automated backups are enabled, as determined by the `BackupRetentionPeriod` parameter. Changing this parameter doesnât result in an outage and the change is asynchronously applied as soon as possible. The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region. For more information, see [Backup window](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupWindow) in the *Amazon RDS User Guide* .

This setting doesnât apply to Amazon Aurora DB instances. The daily time range for creating automated backups is managed by the DB cluster. For more information, see `ModifyDBCluster` .

Constraints:

- Must be in the format `hh24:mi-hh24:mi` .
- Must be in Universal Coordinated Time (UTC).
- Must not conflict with the preferred maintenance window.
- Must be at least 30 minutes.

`--preferred-maintenance-window` (string)

The weekly time range during which system maintenance can occur, which might result in an outage. Changing this parameter doesnât result in an outage, except in the following situation, and the change is asynchronously applied as soon as possible. If there are pending actions that cause a reboot, and the maintenance window is changed to include the current time, then changing this parameter causes a reboot of the DB instance. If you change this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure pending changes are applied.

For more information, see [Amazon RDS Maintenance Window](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#Concepts.DBMaintenance) in the *Amazon RDS User Guide.*

Default: Uses existing setting

Constraints:

- Must be in the format `ddd:hh24:mi-ddd:hh24:mi` .
- The day values must be `mon | tue | wed | thu | fri | sat | sun` .
- Must be in Universal Coordinated Time (UTC).
- Must not conflict with the preferred backup window.
- Must be at least 30 minutes.

`--multi-az` | `--no-multi-az` (boolean)

Specifies whether the DB instance is a Multi-AZ deployment. Changing this parameter doesnât result in an outage. The change is applied during the next maintenance window unless the `ApplyImmediately` parameter is enabled for this request.

This setting doesnât apply to RDS Custom DB instances.

`--engine-version` (string)

The version number of the database engine to upgrade to. Changing this parameter results in an outage and the change is applied during the next maintenance window unless the `ApplyImmediately` parameter is enabled for this request.

For major version upgrades, if a nondefault DB parameter group is currently in use, a new DB parameter group in the DB parameter group family for the new engine version must be specified. The new DB parameter group can be the default for that DB parameter group family.

If you specify only a major version, Amazon RDS updates the DB instance to the default minor version if the current minor version is lower. For information about valid engine versions, see `CreateDBInstance` , or call `DescribeDBEngineVersions` .

If the instance that youâre modifying is acting as a read replica, the engine version that you specify must be the same or higher than the version that the source DB instance or cluster is running.

In RDS Custom for Oracle, this parameter is supported for read replicas only if they are in the `PATCH_DB_FAILURE` lifecycle.

Constraints:

- If you are upgrading the engine version and modifying the DB instance class at the same time, the currently running engine version must be supported on the specified DB instance class. Otherwise, the operation returns an error. In this case, first run the operation to upgrade the engine version, and then run it again to modify the DB instance class.

`--allow-major-version-upgrade` | `--no-allow-major-version-upgrade` (boolean)

Specifies whether major version upgrades are allowed. Changing this parameter doesnât result in an outage and the change is asynchronously applied as soon as possible.

This setting doesnât apply to RDS Custom DB instances.

Constraints:

- Major version upgrades must be allowed when specifying a value for the `EngineVersion` parameter thatâs a different major version than the DB instanceâs current version.

`--auto-minor-version-upgrade` | `--no-auto-minor-version-upgrade` (boolean)

Specifies whether minor version upgrades are applied automatically to the DB instance during the maintenance window. An outage occurs when all the following conditions are met:

- The automatic upgrade is enabled for the maintenance window.
- A newer minor version is available.
- RDS has enabled automatic patching for the engine version.

If any of the preceding conditions isnât met, Amazon RDS applies the change as soon as possible and doesnât cause an outage.

For an RDS Custom DB instance, donât enable this setting. Otherwise, the operation returns an error.

For more information about automatic minor version upgrades, see [Automatically upgrading the minor engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades) .

`--license-model` (string)

The license model for the DB instance.

This setting doesnât apply to Amazon Aurora or RDS Custom DB instances.

Valid Values:

- RDS for Db2 - `bring-your-own-license`
- RDS for MariaDB - `general-public-license`
- RDS for Microsoft SQL Server - `license-included`
- RDS for MySQL - `general-public-license`
- RDS for Oracle - `bring-your-own-license | license-included`
- RDS for PostgreSQL - `postgresql-license`

`--iops` (integer)

The new Provisioned IOPS (I/O operations per second) value for the RDS instance.

Changing this setting doesnât result in an outage and the change is applied during the next maintenance window unless the `ApplyImmediately` parameter is enabled for this request. If you are migrating from Provisioned IOPS to standard storage, set this value to 0. The DB instance will require a reboot for the change in storage type to take effect.

If you choose to migrate your DB instance from using standard storage to Provisioned IOPS (io1), or from Provisioned IOPS to standard storage, the process can take time. The duration of the migration depends on several factors such as database load, storage size, storage type (standard or Provisioned IOPS), amount of IOPS provisioned (if any), and the number of prior scale storage operations. Typical migration times are under 24 hours, but the process can take up to several days in some cases. During the migration, the DB instance is available for use, but might experience performance degradation. While the migration takes place, nightly backups for the instance are suspended. No other Amazon RDS operations can take place for the instance, including modifying the instance, rebooting the instance, deleting the instance, creating a read replica for the instance, and creating a DB snapshot of the instance.

Constraints:

- For RDS for MariaDB, RDS for MySQL, RDS for Oracle, and RDS for PostgreSQL - The value supplied must be at least 10% greater than the current value. Values that are not at least 10% greater than the existing value are rounded up so that they are 10% greater than the current value.
- When you increase the Provisioned IOPS, you must also specify the `AllocatedStorage` parameter. You can use the current value for `AllocatedStorage` .

Default: Uses existing setting

`--option-group-name` (string)

The option group to associate the DB instance with.

Changing this parameter doesnât result in an outage, with one exception. If the parameter change results in an option group that enables OEM, it can cause a brief period, lasting less than a second, during which new connections are rejected but existing connections arenât interrupted.

The change is applied during the next maintenance window unless the `ApplyImmediately` parameter is enabled for this request.

Permanent options, such as the TDE option for Oracle Advanced Security TDE, canât be removed from an option group, and that option group canât be removed from a DB instance after it is associated with a DB instance.

This setting doesnât apply to RDS Custom DB instances.

`--new-db-instance-identifier` (string)

The new identifier for the DB instance when renaming a DB instance. When you change the DB instance identifier, an instance reboot occurs immediately if you enable `ApplyImmediately` , or will occur during the next maintenance window if you disable `ApplyImmediately` . This value is stored as a lowercase string.

This setting doesnât apply to RDS Custom DB instances.

Constraints:

- Must contain from 1 to 63 letters, numbers, or hyphens.
- The first character must be a letter.
- Canât end with a hyphen or contain two consecutive hyphens.

Example: `mydbinstance`

`--storage-type` (string)

The storage type to associate with the DB instance.

If you specify `io1` , `io2` , or `gp3` you must also include a value for the `Iops` parameter.

If you choose to migrate your DB instance from using standard storage to gp2 (General Purpose SSD), gp3, or Provisioned IOPS (io1), or from these storage types to standard storage, the process can take time. The duration of the migration depends on several factors such as database load, storage size, storage type (standard or Provisioned IOPS), amount of IOPS provisioned (if any), and the number of prior scale storage operations. Typical migration times are under 24 hours, but the process can take up to several days in some cases. During the migration, the DB instance is available for use, but might experience performance degradation. While the migration takes place, nightly backups for the instance are suspended. No other Amazon RDS operations can take place for the instance, including modifying the instance, rebooting the instance, deleting the instance, creating a read replica for the instance, and creating a DB snapshot of the instance.

Valid Values: `gp2 | gp3 | io1 | io2 | standard`

Default: `io1` , if the `Iops` parameter is specified. Otherwise, `gp2` .

`--tde-credential-arn` (string)

The ARN from the key store with which to associate the instance for TDE encryption.

This setting doesnât apply to RDS Custom DB instances.

`--tde-credential-password` (string)

The password for the given ARN from the key store in order to access the device.

This setting doesnât apply to RDS Custom DB instances.

`--ca-certificate-identifier` (string)

The CA certificate identifier to use for the DB instanceâs server certificate.

This setting doesnât apply to RDS Custom DB instances.

For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide* .

`--domain` (string)

The Active Directory directory ID to move the DB instance to. Specify `none` to remove the instance from its current domain. You must create the domain before this operation. Currently, you can create only Db2, MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances in an Active Directory Domain.

For more information, see [Kerberos Authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/kerberos-authentication.html) in the *Amazon RDS User Guide* .

This setting doesnât apply to RDS Custom DB instances.

`--domain-fqdn` (string)

The fully qualified domain name (FQDN) of an Active Directory domain.

Constraints:

- Canât be longer than 64 characters.

Example: `mymanagedADtest.mymanagedAD.mydomain`

`--domain-ou` (string)

The Active Directory organizational unit for your DB instance to join.

Constraints:

- Must be in the distinguished name format.
- Canât be longer than 64 characters.

Example: `OU=mymanagedADtestOU,DC=mymanagedADtest,DC=mymanagedAD,DC=mydomain`

`--domain-auth-secret-arn` (string)

The ARN for the Secrets Manager secret with the credentials for the user joining the domain.

Example: `arn:aws:secretsmanager:region:account-number:secret:myselfmanagedADtestsecret-123456`

`--domain-dns-ips` (list)

The IPv4 DNS IP addresses of your primary and secondary Active Directory domain controllers.

Constraints:

- Two IP addresses must be provided. If there isnât a secondary domain controller, use the IP address of the primary domain controller for both entries in the list.

Example: `123.124.125.126,234.235.236.237`

(string)

Syntax:

```
"string" "string" ...
```

`--copy-tags-to-snapshot` | `--no-copy-tags-to-snapshot` (boolean)

Specifies whether to copy all tags from the DB instance to snapshots of the DB instance. By default, tags arenât copied.

This setting doesnât apply to Amazon Aurora DB instances. Copying tags to snapshots is managed by the DB cluster. Setting this value for an Aurora DB instance has no effect on the DB cluster setting. For more information, see `ModifyDBCluster` .

`--monitoring-interval` (integer)

The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collection of Enhanced Monitoring metrics, specify `0` .

If `MonitoringRoleArn` is specified, set `MonitoringInterval` to a value other than `0` .

This setting doesnât apply to RDS Custom DB instances.

Valid Values: `0 | 1 | 5 | 10 | 15 | 30 | 60`

Default: `0`

`--db-port-number` (integer)

The port number on which the database accepts connections.

The value of the `DBPortNumber` parameter must not match any of the port values specified for options in the option group for the DB instance.

If you change the `DBPortNumber` value, your database restarts regardless of the value of the `ApplyImmediately` parameter.

This setting doesnât apply to RDS Custom DB instances.

Valid Values: `1150-65535`

Default:

- Amazon Aurora - `3306`
- RDS for Db2 - `50000`
- RDS for MariaDB - `3306`
- RDS for Microsoft SQL Server - `1433`
- RDS for MySQL - `3306`
- RDS for Oracle - `1521`
- RDS for PostgreSQL - `5432`

Constraints:

- For RDS for Microsoft SQL Server, the value canât be `1234` , `1434` , `3260` , `3343` , `3389` , `47001` , or `49152-49156` .

`--publicly-accessible` | `--no-publicly-accessible` (boolean)

Specifies whether the DB instance is publicly accessible.

When the DB instance is publicly accessible and you connect from outside of the DB instanceâs virtual private cloud (VPC), its Domain Name System (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB instance, the endpoint resolves to the private IP address. Access to the DB instance is ultimately controlled by the security group it uses. That public access isnât permitted if the security group assigned to the DB instance doesnât permit it.

When the DB instance isnât publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.

`PubliclyAccessible` only applies to DB instances in a VPC. The DB instance must be part of a public subnet and `PubliclyAccessible` must be enabled for it to be publicly accessible.

Changes to the `PubliclyAccessible` parameter are applied immediately regardless of the value of the `ApplyImmediately` parameter.

`--monitoring-role-arn` (string)

The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, `arn:aws:iam:123456789012:role/emaccess` . For information on creating a monitoring role, see [To create an IAM role for Amazon RDS Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html#USER_Monitoring.OS.IAMRole) in the *Amazon RDS User Guide.*

If `MonitoringInterval` is set to a value other than `0` , supply a `MonitoringRoleArn` value.

This setting doesnât apply to RDS Custom DB instances.

`--domain-iam-role-name` (string)

The name of the IAM role to use when making API calls to the Directory Service.

This setting doesnât apply to RDS Custom DB instances.

`--disable-domain` | `--no-disable-domain` (boolean)

Specifies whether to remove the DB instance from the Active Directory domain.

`--promotion-tier` (integer)

The order of priority in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see [Fault Tolerance for an Aurora DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html#Aurora.Managing.FaultTolerance) in the *Amazon Aurora User Guide* .

This setting doesnât apply to RDS Custom DB instances.

Default: `1`

Valid Values: `0 - 15`

`--enable-iam-database-authentication` | `--no-enable-iam-database-authentication` (boolean)

Specifies whether to enable mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts. By default, mapping isnât enabled.

This setting doesnât apply to Amazon Aurora. Mapping Amazon Web Services IAM accounts to database accounts is managed by the DB cluster.

For more information about IAM database authentication, see [IAM Database Authentication for MySQL and PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html) in the *Amazon RDS User Guide.*

This setting doesnât apply to RDS Custom DB instances.

`--database-insights-mode` (string)

Specifies the mode of Database Insights to enable for the DB instance.

### Note

Aurora DB instances inherit this value from the DB cluster, so you canât change this value.

Possible values:

- `standard`
- `advanced`

`--enable-performance-insights` | `--no-enable-performance-insights` (boolean)

Specifies whether to enable Performance Insights for the DB instance.

For more information, see [Using Amazon Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html) in the *Amazon RDS User Guide* .

This setting doesnât apply to RDS Custom DB instances.

`--performance-insights-kms-key-id` (string)

The Amazon Web Services KMS key identifier for encryption of Performance Insights data.

The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

If you donât specify a value for `PerformanceInsightsKMSKeyId` , then Amazon RDS uses your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.

This setting doesnât apply to RDS Custom DB instances.

`--performance-insights-retention-period` (integer)

The number of days to retain Performance Insights data.

This setting doesnât apply to RDS Custom DB instances.

Valid Values:

- `7`
- *month* * 31, where *month* is a number of months from 1-23. Examples: `93` (3 months * 31), `341` (11 months * 31), `589` (19 months * 31)
- `731`

Default: `7` days

If you specify a retention period that isnât valid, such as `94` , Amazon RDS returns an error.

`--cloudwatch-logs-export-configuration` (structure)

The log types to be enabled for export to CloudWatch Logs for a specific DB instance.

A change to the `CloudwatchLogsExportConfiguration` parameter is always applied to the DB instance immediately. Therefore, the `ApplyImmediately` parameter has no effect.

This setting doesnât apply to RDS Custom DB instances.

The following values are valid for each DB engine:

- Aurora MySQL - `audit | error | general | slowquery | iam-db-auth-error`
- Aurora PostgreSQL - `postgresql | iam-db-auth-error`
- RDS for MySQL - `error | general | slowquery | iam-db-auth-error`
- RDS for PostgreSQL - `postgresql | upgrade | iam-db-auth-error`

For more information about exporting CloudWatch Logs for Amazon RDS, see [Publishing Database Logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon RDS User Guide* .

For more information about exporting CloudWatch Logs for Amazon Aurora, see [Publishing Database Logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon Aurora User Guide* .

EnableLogTypes -> (list)

The list of log types to enable.

The following values are valid for each DB engine:

- Aurora MySQL - `audit | error | general | slowquery`
- Aurora PostgreSQL - `postgresql`
- RDS for MySQL - `error | general | slowquery`
- RDS for PostgreSQL - `postgresql | upgrade`

(string)

DisableLogTypes -> (list)

The list of log types to disable.

The following values are valid for each DB engine:

- Aurora MySQL - `audit | error | general | slowquery`
- Aurora PostgreSQL - `postgresql`
- RDS for MySQL - `error | general | slowquery`
- RDS for PostgreSQL - `postgresql | upgrade`

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

`--processor-features` (list)

The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.

This setting doesnât apply to RDS Custom DB instances.

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

Shorthand Syntax:

```
Name=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Value": "string"
  }
  ...
]
```

`--use-default-processor-features` | `--no-use-default-processor-features` (boolean)

Specifies whether the DB instance class of the DB instance uses its default processor features.

This setting doesnât apply to RDS Custom DB instances.

`--deletion-protection` | `--no-deletion-protection` (boolean)

Specifies whether the DB instance has deletion protection enabled. The database canât be deleted when deletion protection is enabled. By default, deletion protection isnât enabled. For more information, see [Deleting a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html) .

This setting doesnât apply to Amazon Aurora DB instances. You can enable or disable deletion protection for the DB cluster. For more information, see `ModifyDBCluster` . DB instances in a DB cluster can be deleted even when deletion protection is enabled for the DB cluster.

`--max-allocated-storage` (integer)

The upper limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance.

For more information about this setting, including limitations that apply to it, see [Managing capacity automatically with Amazon RDS storage autoscaling](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.Autoscaling) in the *Amazon RDS User Guide* .

This setting doesnât apply to RDS Custom DB instances.

`--certificate-rotation-restart` | `--no-certificate-rotation-restart` (boolean)

Specifies whether the DB instance is restarted when you rotate your SSL/TLS certificate.

By default, the DB instance is restarted when you rotate your SSL/TLS certificate. The certificate is not updated until the DB instance is restarted.

### Warning

Set this parameter only if you are *not* using SSL/TLS to connect to the DB instance.

If you are using SSL/TLS to connect to the DB instance, follow the appropriate instructions for your DB engine to rotate your SSL/TLS certificate:

- For more information about rotating your SSL/TLS certificate for RDS DB engines, see [Rotating Your SSL/TLS Certificate.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html) in the *Amazon RDS User Guide.*
- For more information about rotating your SSL/TLS certificate for Aurora DB engines, see [Rotating Your SSL/TLS Certificate](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL-certificate-rotation.html) in the *Amazon Aurora User Guide* .

This setting doesnât apply to RDS Custom DB instances.

`--replica-mode` (string)

A value that sets the open mode of a replica database to either mounted or read-only.

### Note

Currently, this parameter is only supported for Oracle DB instances.

Mounted DB replicas are included in Oracle Enterprise Edition. The main use case for mounted replicas is cross-Region disaster recovery. The primary database doesnât use Active Data Guard to transmit information to the mounted replica. Because it doesnât accept user connections, a mounted replica canât serve a read-only workload. For more information, see [Working with Oracle Read Replicas for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.html) in the *Amazon RDS User Guide* .

This setting doesnât apply to RDS Custom DB instances.

Possible values:

- `open-read-only`
- `mounted`

`--enable-customer-owned-ip` | `--no-enable-customer-owned-ip` (boolean)

Specifies whether to enable a customer-owned IP address (CoIP) for an RDS on Outposts DB instance.

A *CoIP* provides local or external connectivity to resources in your Outpost subnets through your on-premises network. For some use cases, a CoIP can provide lower latency for connections to the DB instance from outside of its virtual private cloud (VPC) on your local network.

For more information about RDS on Outposts, see [Working with Amazon RDS on Amazon Web Services Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html) in the *Amazon RDS User Guide* .

For more information about CoIPs, see [Customer-owned IP addresses](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing) in the *Amazon Web Services Outposts User Guide* .

`--aws-backup-recovery-point-arn` (string)

The Amazon Resource Name (ARN) of the recovery point in Amazon Web Services Backup.

This setting doesnât apply to RDS Custom DB instances.

`--automation-mode` (string)

The automation mode of the RDS Custom DB instance. If `full` , the DB instance automates monitoring and instance recovery. If `all paused` , the instance pauses automation for the duration set by `ResumeFullAutomationModeMinutes` .

Possible values:

- `full`
- `all-paused`

`--resume-full-automation-mode-minutes` (integer)

The number of minutes to pause the automation. When the time period ends, RDS Custom resumes full automation.

Default: `60`

Constraints:

- Must be at least 60.
- Must be no more than 1,440.

`--network-type` (string)

The network type of the DB instance.

The network type is determined by the `DBSubnetGroup` specified for the DB instance. A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL` ).

For more information, see [Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon RDS User Guide.*

Valid Values: `IPV4 | DUAL`

`--storage-throughput` (integer)

The storage throughput value for the DB instance.

This setting applies only to the `gp3` storage type.

This setting doesnât apply to Amazon Aurora or RDS Custom DB instances.

`--manage-master-user-password` | `--no-manage-master-user-password` (boolean)

Specifies whether to manage the master user password with Amazon Web Services Secrets Manager.

If the DB instance doesnât manage the master user password with Amazon Web Services Secrets Manager, you can turn on this management. In this case, you canât specify `MasterUserPassword` .

If the DB instance already manages the master user password with Amazon Web Services Secrets Manager, and you specify that the master user password is not managed with Amazon Web Services Secrets Manager, then you must specify `MasterUserPassword` . In this case, Amazon RDS deletes the secret and uses the new password for the master user specified by `MasterUserPassword` .

For more information, see [Password management with Amazon Web Services Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide.*

Constraints:

- Canât manage the master user password with Amazon Web Services Secrets Manager if `MasterUserPassword` is specified.
- Canât specify for RDS for Oracle CDB instances in the multi-tenant configuration. Use `ModifyTenantDatabase` instead.
- Canât specify the parameters `ManageMasterUserPassword` and `MultiTenant` in the same operation.

`--rotate-master-user-password` | `--no-rotate-master-user-password` (boolean)

Specifies whether to rotate the secret managed by Amazon Web Services Secrets Manager for the master user password.

This setting is valid only if the master user password is managed by RDS in Amazon Web Services Secrets Manager for the DB instance. The secret value contains the updated password.

For more information, see [Password management with Amazon Web Services Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide.*

Constraints:

- You must apply the change immediately when rotating the master user password.

`--master-user-secret-kms-key-id` (string)

The Amazon Web Services KMS key identifier to encrypt a secret that is automatically generated and managed in Amazon Web Services Secrets Manager.

This setting is valid only if both of the following conditions are met:

- The DB instance doesnât manage the master user password in Amazon Web Services Secrets Manager. If the DB instance already manages the master user password in Amazon Web Services Secrets Manager, you canât change the KMS key used to encrypt the secret.
- You are turning on `ManageMasterUserPassword` to manage the master user password in Amazon Web Services Secrets Manager. If you are turning on `ManageMasterUserPassword` and donât specify `MasterUserSecretKmsKeyId` , then the `aws/secretsmanager` KMS key is used to encrypt the secret. If the secret is in a different Amazon Web Services account, then you canât use the `aws/secretsmanager` KMS key to encrypt the secret, and you must use a customer managed KMS key.

The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.

There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.

`--engine` (string)

The target Oracle DB engine when you convert a non-CDB to a CDB. This intermediate step is necessary to upgrade an Oracle Database 19c non-CDB to an Oracle Database 21c CDB.

Note the following requirements:

- Make sure that you specify `oracle-ee-cdb` or `oracle-se2-cdb` .
- Make sure that your DB engine runs Oracle Database 19c with an April 2021 or later RU.

Note the following limitations:

- You canât convert a CDB to a non-CDB.
- You canât convert a replica database.
- You canât convert a non-CDB to a CDB and upgrade the engine version in the same command.
- You canât convert the existing custom parameter or option group when it has options or parameters that are permanent or persistent. In this situation, the DB instance reverts to the default option and parameter group. To avoid reverting to the default, specify a new parameter group with `--db-parameter-group-name` and a new option group with `--option-group-name` .

`--dedicated-log-volume` | `--no-dedicated-log-volume` (boolean)

Indicates whether the DB instance has a dedicated log volume (DLV) enabled.

`--multi-tenant` | `--no-multi-tenant` (boolean)

Specifies whether the to convert your DB instance from the single-tenant conï¬guration to the multi-tenant conï¬guration. This parameter is supported only for RDS for Oracle CDB instances.

During the conversion, RDS creates an initial tenant database and associates the DB name, master user name, character set, and national character set metadata with this database. The tags associated with the instance also propagate to the initial tenant database. You can add more tenant databases to your DB instance by using the `CreateTenantDatabase` operation.

### Warning

The conversion to the multi-tenant configuration is permanent and irreversible, so you canât later convert back to the single-tenant configuration. When you specify this parameter, you must also specify `ApplyImmediately` .

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

**Example 1: To modify a DB instance**

The following `modify-db-instance` example associates an option group and a parameter group with a compatible Microsoft SQL Server DB instance. The `--apply-immediately` parameter causes the option and parameter groups to be associated immediately, instead of waiting until the next maintenance window.

```
aws rds modify-db-instance \
    --db-instance-identifier database-2 \
    --option-group-name test-se-2017 \
    --db-parameter-group-name test-sqlserver-se-2017 \
    --apply-immediately
```

Output:

```
{
    "DBInstance": {
        "DBInstanceIdentifier": "database-2",
        "DBInstanceClass": "db.r4.large",
        "Engine": "sqlserver-se",
        "DBInstanceStatus": "available",

        ...output omitted...

        "DBParameterGroups": [
            {
                "DBParameterGroupName": "test-sqlserver-se-2017",
                "ParameterApplyStatus": "applying"
            }
        ],
        "AvailabilityZone": "us-west-2d",

        ...output omitted...

        "MultiAZ": true,
        "EngineVersion": "14.00.3281.6.v1",
        "AutoMinorVersionUpgrade": false,
        "ReadReplicaDBInstanceIdentifiers": [],
        "LicenseModel": "license-included",
        "OptionGroupMemberships": [
            {
                "OptionGroupName": "test-se-2017",
                "Status": "pending-apply"
            }
        ],
        "CharacterSetName": "SQL_Latin1_General_CP1_CI_AS",
        "SecondaryAvailabilityZone": "us-west-2c",
        "PubliclyAccessible": true,
        "StorageType": "gp2",

        ...output omitted...

        "DeletionProtection": false,
        "AssociatedRoles": [],
        "MaxAllocatedStorage": 1000
    }
}
```

For more information, see [Modifying an Amazon RDS DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html) in the *Amazon RDS User Guide*.

**Example 2: To associate VPC security group with a DB instance**

The following `modify-db-instance` example associates a specific VPC security group and removes DB security groups from a DB instance:

```
aws rds modify-db-instance \
    --db-instance-identifier dbName \
    --vpc-security-group-ids sg-ID
```

Output:

```
{
"DBInstance": {
    "DBInstanceIdentifier": "dbName",
    "DBInstanceClass": "db.t3.micro",
    "Engine": "mysql",
    "DBInstanceStatus": "available",
    "MasterUsername": "admin",
    "Endpoint": {
        "Address": "dbName.abcdefghijk.us-west-2.rds.amazonaws.com",
        "Port": 3306,
        "HostedZoneId": "ABCDEFGHIJK1234"
    },
    "AllocatedStorage": 20,
    "InstanceCreateTime": "2024-02-15T00:37:58.793000+00:00",
    "PreferredBackupWindow": "11:57-12:27",
    "BackupRetentionPeriod": 7,
    "DBSecurityGroups": [],
    "VpcSecurityGroups": [
        {
            "VpcSecurityGroupId": "sg-ID",
            "Status": "active"
        }
    ],
    ... output omitted ...
    "MultiAZ": false,
    "EngineVersion": "8.0.35",
    "AutoMinorVersionUpgrade": true,
    "ReadReplicaDBInstanceIdentifiers": [],
    "LicenseModel": "general-public-license",

    ... output ommited ...
    }
}
```

For more information, see [Controlling access with security groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html) in the *Amazon RDS User Guide*.

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