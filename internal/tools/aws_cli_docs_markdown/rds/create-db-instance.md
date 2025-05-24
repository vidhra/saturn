# create-db-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# create-db-instance

## Description

Creates a new DB instance.

The new DB instance can be an RDS DB instance, or it can be a DB instance in an Aurora DB cluster. For an Aurora DB cluster, you can call this operation multiple times to add more than one DB instance to the cluster.

For more information about creating an RDS DB instance, see [Creating an Amazon RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html) in the *Amazon RDS User Guide* .

For more information about creating a DB instance in an Aurora DB cluster, see [Creating an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html) in the *Amazon Aurora User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/CreateDBInstance)

## Synopsis

```
create-db-instance
[--db-name <value>]
--db-instance-identifier <value>
[--allocated-storage <value>]
--db-instance-class <value>
--engine <value>
[--master-username <value>]
[--master-user-password <value>]
[--db-security-groups <value>]
[--vpc-security-group-ids <value>]
[--availability-zone <value>]
[--db-subnet-group-name <value>]
[--preferred-maintenance-window <value>]
[--db-parameter-group-name <value>]
[--backup-retention-period <value>]
[--preferred-backup-window <value>]
[--port <value>]
[--multi-az | --no-multi-az]
[--engine-version <value>]
[--auto-minor-version-upgrade | --no-auto-minor-version-upgrade]
[--license-model <value>]
[--iops <value>]
[--option-group-name <value>]
[--character-set-name <value>]
[--nchar-character-set-name <value>]
[--publicly-accessible | --no-publicly-accessible]
[--tags <value>]
[--db-cluster-identifier <value>]
[--storage-type <value>]
[--tde-credential-arn <value>]
[--tde-credential-password <value>]
[--storage-encrypted | --no-storage-encrypted]
[--kms-key-id <value>]
[--domain <value>]
[--domain-fqdn <value>]
[--domain-ou <value>]
[--domain-auth-secret-arn <value>]
[--domain-dns-ips <value>]
[--copy-tags-to-snapshot | --no-copy-tags-to-snapshot]
[--monitoring-interval <value>]
[--monitoring-role-arn <value>]
[--domain-iam-role-name <value>]
[--promotion-tier <value>]
[--timezone <value>]
[--enable-iam-database-authentication | --no-enable-iam-database-authentication]
[--database-insights-mode <value>]
[--enable-performance-insights | --no-enable-performance-insights]
[--performance-insights-kms-key-id <value>]
[--performance-insights-retention-period <value>]
[--enable-cloudwatch-logs-exports <value>]
[--processor-features <value>]
[--deletion-protection | --no-deletion-protection]
[--max-allocated-storage <value>]
[--enable-customer-owned-ip | --no-enable-customer-owned-ip]
[--custom-iam-instance-profile <value>]
[--backup-target <value>]
[--network-type <value>]
[--storage-throughput <value>]
[--manage-master-user-password | --no-manage-master-user-password]
[--master-user-secret-kms-key-id <value>]
[--ca-certificate-identifier <value>]
[--db-system-id <value>]
[--dedicated-log-volume | --no-dedicated-log-volume]
[--multi-tenant | --no-multi-tenant]
[--engine-lifecycle-support <value>]
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

`--db-name` (string)

The meaning of this parameter differs according to the database engine you use.

Amazon Aurora MySQL

The name of the database to create when the primary DB instance of the Aurora MySQL DB cluster is created. If this parameter isnât specified for an Aurora MySQL DB cluster, no database is created in the DB cluster.

Constraints:

- Must contain 1 to 64 alphanumeric characters.
- Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).
- Canât be a word reserved by the database engine.

Amazon Aurora PostgreSQL

The name of the database to create when the primary DB instance of the Aurora PostgreSQL DB cluster is created. A database named `postgres` is always created. If this parameter is specified, an additional database with this name is created.

Constraints:

- It must contain 1 to 63 alphanumeric characters.
- Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0 to 9).
- Canât be a word reserved by the database engine.

Amazon RDS Custom for Oracle

The Oracle System ID (SID) of the created RDS Custom DB instance. If you donât specify a value, the default value is `ORCL` for non-CDBs and `RDSCDB` for CDBs.

Default: `ORCL`

Constraints:

- Must contain 1 to 8 alphanumeric characters.
- Must contain a letter.
- Canât be a word reserved by the database engine.

Amazon RDS Custom for SQL Server

Not applicable. Must be null.

RDS for Db2

The name of the database to create when the DB instance is created. If this parameter isnât specified, no database is created in the DB instance. In some cases, we recommend that you donât add a database name. For more information, see [Additional considerations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-db-instance-prereqs.html#db2-prereqs-additional-considerations) in the *Amazon RDS User Guide* .

Constraints:

- Must contain 1 to 64 letters or numbers.
- Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).
- Canât be a word reserved by the specified database engine.

RDS for MariaDB

The name of the database to create when the DB instance is created. If this parameter isnât specified, no database is created in the DB instance.

Constraints:

- Must contain 1 to 64 letters or numbers.
- Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).
- Canât be a word reserved by the specified database engine.

RDS for MySQL

The name of the database to create when the DB instance is created. If this parameter isnât specified, no database is created in the DB instance.

Constraints:

- Must contain 1 to 64 letters or numbers.
- Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).
- Canât be a word reserved by the specified database engine.

RDS for Oracle

The Oracle System ID (SID) of the created DB instance. If you donât specify a value, the default value is `ORCL` . You canât specify the string `null` , or any other reserved word, for `DBName` .

Default: `ORCL`

Constraints:

- Canât be longer than 8 characters.

RDS for PostgreSQL

The name of the database to create when the DB instance is created. A database named `postgres` is always created. If this parameter is specified, an additional database with this name is created.

Constraints:

- Must contain 1 to 63 letters, numbers, or underscores.
- Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).
- Canât be a word reserved by the specified database engine.

RDS for SQL Server

Not applicable. Must be null.

`--db-instance-identifier` (string)

The identifier for this DB instance. This parameter is stored as a lowercase string.

Constraints:

- Must contain from 1 to 63 letters, numbers, or hyphens.
- First character must be a letter.
- Canât end with a hyphen or contain two consecutive hyphens.

Example: `mydbinstance`

`--allocated-storage` (integer)

The amount of storage in gibibytes (GiB) to allocate for the DB instance.

This setting doesnât apply to Amazon Aurora DB instances. Aurora cluster volumes automatically grow as the amount of data in your database increases, though you are only charged for the space that you use in an Aurora cluster volume.

Amazon RDS Custom

Constraints to the amount of storage for each storage type are the following:

- General Purpose (SSD) storage (gp2, gp3): Must be an integer from 40 to 65536 for RDS Custom for Oracle, 16384 for RDS Custom for SQL Server.
- Provisioned IOPS storage (io1, io2): Must be an integer from 40 to 65536 for RDS Custom for Oracle, 16384 for RDS Custom for SQL Server.

RDS for Db2

Constraints to the amount of storage for each storage type are the following:

- General Purpose (SSD) storage (gp3): Must be an integer from 20 to 65536.
- Provisioned IOPS storage (io1, io2): Must be an integer from 100 to 65536.

RDS for MariaDB

Constraints to the amount of storage for each storage type are the following:

- General Purpose (SSD) storage (gp2, gp3): Must be an integer from 20 to 65536.
- Provisioned IOPS storage (io1, io2): Must be an integer from 100 to 65536.
- Magnetic storage (standard): Must be an integer from 5 to 3072.

RDS for MySQL

Constraints to the amount of storage for each storage type are the following:

- General Purpose (SSD) storage (gp2, gp3): Must be an integer from 20 to 65536.
- Provisioned IOPS storage (io1, io2): Must be an integer from 100 to 65536.
- Magnetic storage (standard): Must be an integer from 5 to 3072.

RDS for Oracle

Constraints to the amount of storage for each storage type are the following:

- General Purpose (SSD) storage (gp2, gp3): Must be an integer from 20 to 65536.
- Provisioned IOPS storage (io1, io2): Must be an integer from 100 to 65536.
- Magnetic storage (standard): Must be an integer from 10 to 3072.

RDS for PostgreSQL

Constraints to the amount of storage for each storage type are the following:

- General Purpose (SSD) storage (gp2, gp3): Must be an integer from 20 to 65536.
- Provisioned IOPS storage (io1, io2): Must be an integer from 100 to 65536.
- Magnetic storage (standard): Must be an integer from 5 to 3072.

RDS for SQL Server

Constraints to the amount of storage for each storage type are the following:

- General Purpose (SSD) storage (gp2, gp3):
- Enterprise and Standard editions: Must be an integer from 20 to 16384.
- Web and Express editions: Must be an integer from 20 to 16384.
- Provisioned IOPS storage (io1, io2):
- Enterprise and Standard editions: Must be an integer from 100 to 16384.
- Web and Express editions: Must be an integer from 100 to 16384.
- Magnetic storage (standard):
- Enterprise and Standard editions: Must be an integer from 20 to 1024.
- Web and Express editions: Must be an integer from 20 to 1024.

`--db-instance-class` (string)

The compute and memory capacity of the DB instance, for example `db.m5.large` . Not all DB instance classes are available in all Amazon Web Services Regions, or for all database engines. For the full list of DB instance classes, and availability for your engine, see [DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the *Amazon RDS User Guide* or [Aurora DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html) in the *Amazon Aurora User Guide* .

`--engine` (string)

The database engine to use for this DB instance.

Not every database engine is available in every Amazon Web Services Region.

Valid Values:

- `aurora-mysql` (for Aurora MySQL DB instances)
- `aurora-postgresql` (for Aurora PostgreSQL DB instances)
- `custom-oracle-ee` (for RDS Custom for Oracle DB instances)
- `custom-oracle-ee-cdb` (for RDS Custom for Oracle DB instances)
- `custom-oracle-se2` (for RDS Custom for Oracle DB instances)
- `custom-oracle-se2-cdb` (for RDS Custom for Oracle DB instances)
- `custom-sqlserver-ee` (for RDS Custom for SQL Server DB instances)
- `custom-sqlserver-se` (for RDS Custom for SQL Server DB instances)
- `custom-sqlserver-web` (for RDS Custom for SQL Server DB instances)
- `custom-sqlserver-dev` (for RDS Custom for SQL Server DB instances)
- `db2-ae`
- `db2-se`
- `mariadb`
- `mysql`
- `oracle-ee`
- `oracle-ee-cdb`
- `oracle-se2`
- `oracle-se2-cdb`
- `postgres`
- `sqlserver-ee`
- `sqlserver-se`
- `sqlserver-ex`
- `sqlserver-web`

`--master-username` (string)

The name for the master user.

This setting doesnât apply to Amazon Aurora DB instances. The name for the master user is managed by the DB cluster.

This setting is required for RDS DB instances.

Constraints:

- Must be 1 to 16 letters, numbers, or underscores.
- First character must be a letter.
- Canât be a reserved word for the chosen database engine.

`--master-user-password` (string)

The password for the master user.

This setting doesnât apply to Amazon Aurora DB instances. The password for the master user is managed by the DB cluster.

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

`--db-security-groups` (list)

A list of DB security groups to associate with this DB instance.

This setting applies to the legacy EC2-Classic platform, which is no longer used to create new DB instances. Use the `VpcSecurityGroupIds` setting instead.

(string)

Syntax:

```
"string" "string" ...
```

`--vpc-security-group-ids` (list)

A list of Amazon EC2 VPC security groups to associate with this DB instance.

This setting doesnât apply to Amazon Aurora DB instances. The associated list of EC2 VPC security groups is managed by the DB cluster.

Default: The default EC2 VPC security group for the DB subnet groupâs VPC.

(string)

Syntax:

```
"string" "string" ...
```

`--availability-zone` (string)

The Availability Zone (AZ) where the database will be created. For information on Amazon Web Services Regions and Availability Zones, see [Regions and Availability Zones](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html) .

For Amazon Aurora, each Aurora DB cluster hosts copies of its storage in three separate Availability Zones. Specify one of these Availability Zones. Aurora automatically chooses an appropriate Availability Zone if you donât specify one.

Default: A random, system-chosen Availability Zone in the endpointâs Amazon Web Services Region.

Constraints:

- The `AvailabilityZone` parameter canât be specified if the DB instance is a Multi-AZ deployment.
- The specified Availability Zone must be in the same Amazon Web Services Region as the current endpoint.

Example: `us-east-1d`

`--db-subnet-group-name` (string)

A DB subnet group to associate with this DB instance.

Constraints:

- Must match the name of an existing DB subnet group.

Example: `mydbsubnetgroup`

`--preferred-maintenance-window` (string)

The time range each week during which system maintenance can occur. For more information, see [Amazon RDS Maintenance Window](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#Concepts.DBMaintenance) in the *Amazon RDS User Guide.*

The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week.

Constraints:

- Must be in the format `ddd:hh24:mi-ddd:hh24:mi` .
- The day values must be `mon | tue | wed | thu | fri | sat | sun` .
- Must be in Universal Coordinated Time (UTC).
- Must not conflict with the preferred backup window.
- Must be at least 30 minutes.

`--db-parameter-group-name` (string)

The name of the DB parameter group to associate with this DB instance. If you donât specify a value, then Amazon RDS uses the default DB parameter group for the specified DB engine and version.

This setting doesnât apply to RDS Custom DB instances.

Constraints:

- Must be 1 to 255 letters, numbers, or hyphens.
- The first character must be a letter.
- Canât end with a hyphen or contain two consecutive hyphens.

`--backup-retention-period` (integer)

The number of days for which automated backups are retained. Setting this parameter to a positive number enables backups. Setting this parameter to `0` disables automated backups.

This setting doesnât apply to Amazon Aurora DB instances. The retention period for automated backups is managed by the DB cluster.

Default: `1`

Constraints:

- Must be a value from 0 to 35.
- Canât be set to 0 if the DB instance is a source to read replicas.
- Canât be set to 0 for an RDS Custom for Oracle DB instance.

`--preferred-backup-window` (string)

The daily time range during which automated backups are created if automated backups are enabled, using the `BackupRetentionPeriod` parameter. The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region. For more information, see [Backup window](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupWindow) in the *Amazon RDS User Guide* .

This setting doesnât apply to Amazon Aurora DB instances. The daily time range for creating automated backups is managed by the DB cluster.

Constraints:

- Must be in the format `hh24:mi-hh24:mi` .
- Must be in Universal Coordinated Time (UTC).
- Must not conflict with the preferred maintenance window.
- Must be at least 30 minutes.

`--port` (integer)

The port number on which the database accepts connections.

This setting doesnât apply to Aurora DB instances. The port number is managed by the cluster.

Valid Values: `1150-65535`

Default:

- RDS for Db2 - `50000`
- RDS for MariaDB - `3306`
- RDS for Microsoft SQL Server - `1433`
- RDS for MySQL - `3306`
- RDS for Oracle - `1521`
- RDS for PostgreSQL - `5432`

Constraints:

- For RDS for Microsoft SQL Server, the value canât be `1234` , `1434` , `3260` , `3343` , `3389` , `47001` , or `49152-49156` .

`--multi-az` | `--no-multi-az` (boolean)

Specifies whether the DB instance is a Multi-AZ deployment. You canât set the `AvailabilityZone` parameter if the DB instance is a Multi-AZ deployment.

This setting doesnât apply to the following DB instances:

- Amazon Aurora (DB instance Availability Zones (AZs) are managed by the DB cluster.)
- RDS Custom

`--engine-version` (string)

The version number of the database engine to use.

This setting doesnât apply to Amazon Aurora DB instances. The version number of the database engine the DB instance uses is managed by the DB cluster.

For a list of valid engine versions, use the `DescribeDBEngineVersions` operation.

The following are the database engines and links to information about the major and minor versions that are available with Amazon RDS. Not every database engine is available for every Amazon Web Services Region.

Amazon RDS Custom for Oracle

A custom engine version (CEV) that you have previously created. This setting is required for RDS Custom for Oracle. The CEV name has the following format: 19.*customized_string* . A valid CEV name is `19.my_cev1` . For more information, see [Creating an RDS Custom for Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-creating.html#custom-creating.create) in the *Amazon RDS User Guide* .

Amazon RDS Custom for SQL Server

See [RDS Custom for SQL Server general requirements](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits-MS.html) in the *Amazon RDS User Guide* .

RDS for Db2

For information, see [Db2 on Amazon RDS versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Db2.html#Db2.Concepts.VersionMgmt) in the *Amazon RDS User Guide* .

RDS for MariaDB

For information, see [MariaDB on Amazon RDS versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MariaDB.html#MariaDB.Concepts.VersionMgmt) in the *Amazon RDS User Guide* .

RDS for Microsoft SQL Server

For information, see [Microsoft SQL Server versions on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.VersionSupport) in the *Amazon RDS User Guide* .

RDS for MySQL

For information, see [MySQL on Amazon RDS versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html#MySQL.Concepts.VersionMgmt) in the *Amazon RDS User Guide* .

RDS for Oracle

For information, see [Oracle Database Engine release notes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.PatchComposition.html) in the *Amazon RDS User Guide* .

RDS for PostgreSQL

For information, see [Amazon RDS for PostgreSQL versions and extensions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts) in the *Amazon RDS User Guide* .

`--auto-minor-version-upgrade` | `--no-auto-minor-version-upgrade` (boolean)

Specifies whether minor engine upgrades are applied automatically to the DB instance during the maintenance window. By default, minor engine upgrades are applied automatically.

If you create an RDS Custom DB instance, you must set `AutoMinorVersionUpgrade` to `false` .

For more information about automatic minor version upgrades, see [Automatically upgrading the minor engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades) .

`--license-model` (string)

The license model information for this DB instance.

### Note

License models for RDS for Db2 require additional configuration. The Bring Your Own License (BYOL) model requires a custom parameter group and an Amazon Web Services License Manager self-managed license. The Db2 license through Amazon Web Services Marketplace model requires an Amazon Web Services Marketplace subscription. For more information, see [Amazon RDS for Db2 licensing options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-licensing.html) in the *Amazon RDS User Guide* .

The default for RDS for Db2 is `bring-your-own-license` .

This setting doesnât apply to Amazon Aurora or RDS Custom DB instances.

Valid Values:

- RDS for Db2 - `bring-your-own-license | marketplace-license`
- RDS for MariaDB - `general-public-license`
- RDS for Microsoft SQL Server - `license-included`
- RDS for MySQL - `general-public-license`
- RDS for Oracle - `bring-your-own-license | license-included`
- RDS for PostgreSQL - `postgresql-license`

`--iops` (integer)

The amount of Provisioned IOPS (input/output operations per second) to initially allocate for the DB instance. For information about valid IOPS values, see [Amazon RDS DB instance storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html) in the *Amazon RDS User Guide* .

This setting doesnât apply to Amazon Aurora DB instances. Storage is managed by the DB cluster.

Constraints:

- For RDS for Db2, MariaDB, MySQL, Oracle, and PostgreSQL - Must be a multiple between .5 and 50 of the storage amount for the DB instance.
- For RDS for SQL Server - Must be a multiple between 1 and 50 of the storage amount for the DB instance.

`--option-group-name` (string)

The option group to associate the DB instance with.

Permanent options, such as the TDE option for Oracle Advanced Security TDE, canât be removed from an option group. Also, that option group canât be removed from a DB instance after it is associated with a DB instance.

This setting doesnât apply to Amazon Aurora or RDS Custom DB instances.

`--character-set-name` (string)

For supported engines, the character set (`CharacterSet` ) to associate the DB instance with.

This setting doesnât apply to the following DB instances:

- Amazon Aurora - The character set is managed by the DB cluster. For more information, see `CreateDBCluster` .
- RDS Custom - However, if you need to change the character set, you can change it on the database itself.

`--nchar-character-set-name` (string)

The name of the NCHAR character set for the Oracle DB instance.

This setting doesnât apply to RDS Custom DB instances.

`--publicly-accessible` | `--no-publicly-accessible` (boolean)

Specifies whether the DB instance is publicly accessible.

When the DB instance is publicly accessible and you connect from outside of the DB instanceâs virtual private cloud (VPC), its Domain Name System (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB instance, the endpoint resolves to the private IP address. Access to the DB instance is ultimately controlled by the security group it uses. That public access is not permitted if the security group assigned to the DB instance doesnât permit it.

When the DB instance isnât publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.

Default: The default behavior varies depending on whether `DBSubnetGroupName` is specified.

If `DBSubnetGroupName` isnât specified, and `PubliclyAccessible` isnât specified, the following applies:

- If the default VPC in the target Region doesnât have an internet gateway attached to it, the DB instance is private.
- If the default VPC in the target Region has an internet gateway attached to it, the DB instance is public.

If `DBSubnetGroupName` is specified, and `PubliclyAccessible` isnât specified, the following applies:

- If the subnets are part of a VPC that doesnât have an internet gateway attached to it, the DB instance is private.
- If the subnets are part of a VPC that has an internet gateway attached to it, the DB instance is public.

`--tags` (list)

Tags to assign to the DB instance.

(structure)

Metadata assigned to an Amazon RDS resource consisting of a key-value pair.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide* .

Key -> (string)

A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and canât be prefixed with `aws:` or `rds:` . The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â:â, â/â, â=â, â+â, â-â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$â).

Value -> (string)

A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and canât be prefixed with `aws:` or `rds:` . The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â:â, â/â, â=â, â+â, â-â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$â).

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

`--db-cluster-identifier` (string)

The identifier of the DB cluster that this DB instance will belong to.

This setting doesnât apply to RDS Custom DB instances.

`--storage-type` (string)

The storage type to associate with the DB instance.

If you specify `io1` , `io2` , or `gp3` , you must also include a value for the `Iops` parameter.

This setting doesnât apply to Amazon Aurora DB instances. Storage is managed by the DB cluster.

Valid Values: `gp2 | gp3 | io1 | io2 | standard`

Default: `io1` , if the `Iops` parameter is specified. Otherwise, `gp3` .

`--tde-credential-arn` (string)

The ARN from the key store with which to associate the instance for TDE encryption.

This setting doesnât apply to Amazon Aurora or RDS Custom DB instances.

`--tde-credential-password` (string)

The password for the given ARN from the key store in order to access the device.

This setting doesnât apply to RDS Custom DB instances.

`--storage-encrypted` | `--no-storage-encrypted` (boolean)

Specifes whether the DB instance is encrypted. By default, it isnât encrypted.

For RDS Custom DB instances, either enable this setting or leave it unset. Otherwise, Amazon RDS reports an error.

This setting doesnât apply to Amazon Aurora DB instances. The encryption for DB instances is managed by the DB cluster.

`--kms-key-id` (string)

The Amazon Web Services KMS key identifier for an encrypted DB instance.

The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.

This setting doesnât apply to Amazon Aurora DB instances. The Amazon Web Services KMS key identifier is managed by the DB cluster. For more information, see `CreateDBCluster` .

If `StorageEncrypted` is enabled, and you do not specify a value for the `KmsKeyId` parameter, then Amazon RDS uses your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.

For Amazon RDS Custom, a KMS key is required for DB instances. For most RDS engines, if you leave this parameter empty while enabling `StorageEncrypted` , the engine uses the default KMS key. However, RDS Custom doesnât use the default key when this parameter is empty. You must explicitly specify a key.

`--domain` (string)

The Active Directory directory ID to create the DB instance in. Currently, you can create only Db2, MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances in an Active Directory Domain.

For more information, see [Kerberos Authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/kerberos-authentication.html) in the *Amazon RDS User Guide* .

This setting doesnât apply to the following DB instances:

- Amazon Aurora (The domain is managed by the DB cluster.)
- RDS Custom

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

Specifies whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.

This setting doesnât apply to Amazon Aurora DB instances. Copying tags to snapshots is managed by the DB cluster. Setting this value for an Aurora DB instance has no effect on the DB cluster setting.

`--monitoring-interval` (integer)

The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collection of Enhanced Monitoring metrics, specify `0` .

If `MonitoringRoleArn` is specified, then you must set `MonitoringInterval` to a value other than `0` .

This setting doesnât apply to RDS Custom DB instances.

Valid Values: `0 | 1 | 5 | 10 | 15 | 30 | 60`

Default: `0`

`--monitoring-role-arn` (string)

The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, `arn:aws:iam:123456789012:role/emaccess` . For information on creating a monitoring role, see [Setting Up and Enabling Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html#USER_Monitoring.OS.Enabling) in the *Amazon RDS User Guide* .

If `MonitoringInterval` is set to a value other than `0` , then you must supply a `MonitoringRoleArn` value.

This setting doesnât apply to RDS Custom DB instances.

`--domain-iam-role-name` (string)

The name of the IAM role to use when making API calls to the Directory Service.

This setting doesnât apply to the following DB instances:

- Amazon Aurora (The domain is managed by the DB cluster.)
- RDS Custom

`--promotion-tier` (integer)

The order of priority in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see [Fault Tolerance for an Aurora DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html#Aurora.Managing.FaultTolerance) in the *Amazon Aurora User Guide* .

This setting doesnât apply to RDS Custom DB instances.

Default: `1`

Valid Values: `0 - 15`

`--timezone` (string)

The time zone of the DB instance. The time zone parameter is currently supported only by [RDS for Db2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-time-zone) and [RDS for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone) .

`--enable-iam-database-authentication` | `--no-enable-iam-database-authentication` (boolean)

Specifies whether to enable mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts. By default, mapping isnât enabled.

For more information, see [IAM Database Authentication for MySQL and PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html) in the *Amazon RDS User Guide* .

This setting doesnât apply to the following DB instances:

- Amazon Aurora (Mapping Amazon Web Services IAM accounts to database accounts is managed by the DB cluster.)
- RDS Custom

`--database-insights-mode` (string)

The mode of Database Insights to enable for the DB instance.

### Note

Aurora DB instances inherit this value from the DB cluster, so you canât change this value.

Possible values:

- `standard`
- `advanced`

`--enable-performance-insights` | `--no-enable-performance-insights` (boolean)

Specifies whether to enable Performance Insights for the DB instance. For more information, see [Using Amazon Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html) in the *Amazon RDS User Guide* .

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

`--enable-cloudwatch-logs-exports` (list)

The list of log types to enable for exporting to CloudWatch Logs. For more information, see [Publishing Database Logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon RDS User Guide* .

This setting doesnât apply to the following DB instances:

- Amazon Aurora (CloudWatch Logs exports are managed by the DB cluster.)
- RDS Custom

The following values are valid for each DB engine:

- RDS for Db2 - `diag.log | notify.log | iam-db-auth-error`
- RDS for MariaDB - `audit | error | general | slowquery | iam-db-auth-error`
- RDS for Microsoft SQL Server - `agent | error`
- RDS for MySQL - `audit | error | general | slowquery | iam-db-auth-error`
- RDS for Oracle - `alert | audit | listener | trace | oemagent`
- RDS for PostgreSQL - `postgresql | upgrade | iam-db-auth-error`

(string)

Syntax:

```
"string" "string" ...
```

`--processor-features` (list)

The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.

This setting doesnât apply to Amazon Aurora or RDS Custom DB instances.

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

`--deletion-protection` | `--no-deletion-protection` (boolean)

Specifies whether the DB instance has deletion protection enabled. The database canât be deleted when deletion protection is enabled. By default, deletion protection isnât enabled. For more information, see [Deleting a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html) .

This setting doesnât apply to Amazon Aurora DB instances. You can enable or disable deletion protection for the DB cluster. For more information, see `CreateDBCluster` . DB instances in a DB cluster can be deleted even when deletion protection is enabled for the DB cluster.

`--max-allocated-storage` (integer)

The upper limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance.

For more information about this setting, including limitations that apply to it, see [Managing capacity automatically with Amazon RDS storage autoscaling](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.Autoscaling) in the *Amazon RDS User Guide* .

This setting doesnât apply to the following DB instances:

- Amazon Aurora (Storage is managed by the DB cluster.)
- RDS Custom

`--enable-customer-owned-ip` | `--no-enable-customer-owned-ip` (boolean)

Specifies whether to enable a customer-owned IP address (CoIP) for an RDS on Outposts DB instance.

A *CoIP* provides local or external connectivity to resources in your Outpost subnets through your on-premises network. For some use cases, a CoIP can provide lower latency for connections to the DB instance from outside of its virtual private cloud (VPC) on your local network.

For more information about RDS on Outposts, see [Working with Amazon RDS on Amazon Web Services Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html) in the *Amazon RDS User Guide* .

For more information about CoIPs, see [Customer-owned IP addresses](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing) in the *Amazon Web Services Outposts User Guide* .

`--custom-iam-instance-profile` (string)

The instance profile associated with the underlying Amazon EC2 instance of an RDS Custom DB instance.

This setting is required for RDS Custom.

Constraints:

- The profile must exist in your account.
- The profile must have an IAM role that Amazon EC2 has permissions to assume.
- The instance profile name and the associated IAM role name must start with the prefix `AWSRDSCustom` .

For the list of permissions required for the IAM role, see [Configure IAM and your VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-setup-orcl.html#custom-setup-orcl.iam-vpc) in the *Amazon RDS User Guide* .

`--backup-target` (string)

The location for storing automated backups and manual snapshots.

Valid Values:

- `outposts` (Amazon Web Services Outposts)
- `region` (Amazon Web Services Region)

Default: `region`

For more information, see [Working with Amazon RDS on Amazon Web Services Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html) in the *Amazon RDS User Guide* .

`--network-type` (string)

The network type of the DB instance.

The network type is determined by the `DBSubnetGroup` specified for the DB instance. A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL` ).

For more information, see [Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon RDS User Guide.*

Valid Values: `IPV4 | DUAL`

`--storage-throughput` (integer)

The storage throughput value, in mebibyte per second (MiBps), for the DB instance.

This setting applies only to the `gp3` storage type.

This setting doesnât apply to Amazon Aurora or RDS Custom DB instances.

`--manage-master-user-password` | `--no-manage-master-user-password` (boolean)

Specifies whether to manage the master user password with Amazon Web Services Secrets Manager.

For more information, see [Password management with Amazon Web Services Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide.*

Constraints:

- Canât manage the master user password with Amazon Web Services Secrets Manager if `MasterUserPassword` is specified.

`--master-user-secret-kms-key-id` (string)

The Amazon Web Services KMS key identifier to encrypt a secret that is automatically generated and managed in Amazon Web Services Secrets Manager.

This setting is valid only if the master user password is managed by RDS in Amazon Web Services Secrets Manager for the DB instance.

The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.

If you donât specify `MasterUserSecretKmsKeyId` , then the `aws/secretsmanager` KMS key is used to encrypt the secret. If the secret is in a different Amazon Web Services account, then you canât use the `aws/secretsmanager` KMS key to encrypt the secret, and you must use a customer managed KMS key.

There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.

`--ca-certificate-identifier` (string)

The CA certificate identifier to use for the DB instanceâs server certificate.

This setting doesnât apply to RDS Custom DB instances.

For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide* .

`--db-system-id` (string)

The Oracle system identifier (SID), which is the name of the Oracle database instance that manages your database files. In this context, the term âOracle database instanceâ refers exclusively to the system global area (SGA) and Oracle background processes. If you donât specify a SID, the value defaults to `RDSCDB` . The Oracle SID is also the name of your CDB.

`--dedicated-log-volume` | `--no-dedicated-log-volume` (boolean)

Indicates whether the DB instance has a dedicated log volume (DLV) enabled.

`--multi-tenant` | `--no-multi-tenant` (boolean)

Specifies whether to use the multi-tenant configuration or the single-tenant configuration (default). This parameter only applies to RDS for Oracle container database (CDB) engines.

Note the following restrictions:

- The DB engine that you specify in the request must support the multi-tenant configuration. If you attempt to enable the multi-tenant configuration on a DB engine that doesnât support it, the request fails.
- If you specify the multi-tenant configuration when you create your DB instance, you canât later modify this DB instance to use the single-tenant configuration.

`--engine-lifecycle-support` (string)

The life cycle type for this DB instance.

### Note

By default, this value is set to `open-source-rds-extended-support` , which enrolls your DB instance into Amazon RDS Extended Support. At the end of standard support, you can avoid charges for Extended Support by setting the value to `open-source-rds-extended-support-disabled` . In this case, creating the DB instance will fail if the DB major version is past its end of standard support date.

This setting applies only to RDS for MySQL and RDS for PostgreSQL. For Amazon Aurora DB instances, the life cycle type is managed by the DB cluster.

You can use this setting to enroll your DB instance into Amazon RDS Extended Support. With RDS Extended Support, you can run the selected major engine version on your DB instance past the end of standard support for that engine version. For more information, see [Amazon RDS Extended Support with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html) in the *Amazon RDS User Guide* .

Valid Values: `open-source-rds-extended-support | open-source-rds-extended-support-disabled`

Default: `open-source-rds-extended-support`

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

**To create a DB instance**

The following `create-db-instance` example uses the required options to launch a new DB instance.

```
aws rds create-db-instance \
    --db-instance-identifier test-mysql-instance \
    --db-instance-class db.t3.micro \
    --engine mysql \
    --master-username admin \
    --master-user-password secret99 \
    --allocated-storage 20
```

Output:

```
{
    "DBInstance": {
        "DBInstanceIdentifier": "test-mysql-instance",
        "DBInstanceClass": "db.t3.micro",
        "Engine": "mysql",
        "DBInstanceStatus": "creating",
        "MasterUsername": "admin",
        "AllocatedStorage": 20,
        "PreferredBackupWindow": "12:55-13:25",
        "BackupRetentionPeriod": 1,
        "DBSecurityGroups": [],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-12345abc",
                "Status": "active"
            }
        ],
        "DBParameterGroups": [
            {
                "DBParameterGroupName": "default.mysql5.7",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        "DBSubnetGroup": {
            "DBSubnetGroupName": "default",
            "DBSubnetGroupDescription": "default",
            "VpcId": "vpc-2ff2ff2f",
            "SubnetGroupStatus": "Complete",
            "Subnets": [
                {
                    "SubnetIdentifier": "subnet-########",
                    "SubnetAvailabilityZone": {
                        "Name": "us-west-2c"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-########",
                    "SubnetAvailabilityZone": {
                        "Name": "us-west-2d"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-########",
                    "SubnetAvailabilityZone": {
                        "Name": "us-west-2a"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-########",
                    "SubnetAvailabilityZone": {
                        "Name": "us-west-2b"
                    },
                    "SubnetStatus": "Active"
                }
            ]
        },
        "PreferredMaintenanceWindow": "sun:08:07-sun:08:37",
        "PendingModifiedValues": {
            "MasterUserPassword": "****"
        },
        "MultiAZ": false,
        "EngineVersion": "5.7.22",
        "AutoMinorVersionUpgrade": true,
        "ReadReplicaDBInstanceIdentifiers": [],
        "LicenseModel": "general-public-license",
        "OptionGroupMemberships": [
            {
                "OptionGroupName": "default:mysql-5-7",
                "Status": "in-sync"
            }
        ],
        "PubliclyAccessible": true,
        "StorageType": "gp2",
        "DbInstancePort": 0,
        "StorageEncrypted": false,
        "DbiResourceId": "db-5555EXAMPLE44444444EXAMPLE",
        "CACertificateIdentifier": "rds-ca-2019",
        "DomainMemberships": [],
        "CopyTagsToSnapshot": false,
        "MonitoringInterval": 0,
        "DBInstanceArn": "arn:aws:rds:us-west-2:123456789012:db:test-mysql-instance",
        "IAMDatabaseAuthenticationEnabled": false,
        "PerformanceInsightsEnabled": false,
        "DeletionProtection": false,
        "AssociatedRoles": []
    }
}
```

For more information, see [Creating an Amazon RDS DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html) in the *Amazon RDS User Guide*.

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