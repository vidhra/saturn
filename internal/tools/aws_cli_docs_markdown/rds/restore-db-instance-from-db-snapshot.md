# restore-db-instance-from-db-snapshotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/restore-db-instance-from-db-snapshot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/restore-db-instance-from-db-snapshot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# restore-db-instance-from-db-snapshot

## Description

Creates a new DB instance from a DB snapshot. The target database is created from the source database restore point with most of the sourceâs original configuration, including the default security group and DB parameter group. By default, the new DB instance is created as a Single-AZ deployment, except when the instance is a SQL Server instance that has an option group associated with mirroring. In this case, the instance becomes a Multi-AZ deployment, not a Single-AZ deployment.

If you want to replace your original DB instance with the new, restored DB instance, then rename your original DB instance before you call the `RestoreDBInstanceFromDBSnapshot` operation. RDS doesnât allow two DB instances with the same name. After you have renamed your original DB instance with a different identifier, then you can pass the original name of the DB instance as the `DBInstanceIdentifier` in the call to the `RestoreDBInstanceFromDBSnapshot` operation. The result is that you replace the original DB instance with the DB instance created from the snapshot.

If you are restoring from a shared manual DB snapshot, the `DBSnapshotIdentifier` must be the ARN of the shared DB snapshot.

To restore from a DB snapshot with an unsupported engine version, you must first upgrade the engine version of the snapshot. For more information about upgrading a RDS for MySQL DB snapshot engine version, see [Upgrading a MySQL DB snapshot engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-upgrade-snapshot.html) . For more information about upgrading a RDS for PostgreSQL DB snapshot engine version, [Upgrading a PostgreSQL DB snapshot engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBSnapshot.PostgreSQL.html) .

### Note

This command doesnât apply to Aurora MySQL and Aurora PostgreSQL. For Aurora, use `RestoreDBClusterFromSnapshot` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/RestoreDBInstanceFromDBSnapshot)

## Synopsis

```
restore-db-instance-from-db-snapshot
--db-instance-identifier <value>
[--db-snapshot-identifier <value>]
[--db-instance-class <value>]
[--port <value>]
[--availability-zone <value>]
[--db-subnet-group-name <value>]
[--multi-az | --no-multi-az]
[--publicly-accessible | --no-publicly-accessible]
[--auto-minor-version-upgrade | --no-auto-minor-version-upgrade]
[--license-model <value>]
[--db-name <value>]
[--engine <value>]
[--iops <value>]
[--option-group-name <value>]
[--tags <value>]
[--storage-type <value>]
[--tde-credential-arn <value>]
[--tde-credential-password <value>]
[--vpc-security-group-ids <value>]
[--domain <value>]
[--domain-fqdn <value>]
[--domain-ou <value>]
[--domain-auth-secret-arn <value>]
[--domain-dns-ips <value>]
[--copy-tags-to-snapshot | --no-copy-tags-to-snapshot]
[--domain-iam-role-name <value>]
[--enable-iam-database-authentication | --no-enable-iam-database-authentication]
[--enable-cloudwatch-logs-exports <value>]
[--processor-features <value>]
[--use-default-processor-features | --no-use-default-processor-features]
[--db-parameter-group-name <value>]
[--deletion-protection | --no-deletion-protection]
[--enable-customer-owned-ip | --no-enable-customer-owned-ip]
[--custom-iam-instance-profile <value>]
[--backup-target <value>]
[--network-type <value>]
[--storage-throughput <value>]
[--db-cluster-snapshot-identifier <value>]
[--allocated-storage <value>]
[--dedicated-log-volume | --no-dedicated-log-volume]
[--ca-certificate-identifier <value>]
[--engine-lifecycle-support <value>]
[--manage-master-user-password | --no-manage-master-user-password]
[--master-user-secret-kms-key-id <value>]
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

The name of the DB instance to create from the DB snapshot. This parameter isnât case-sensitive.

Constraints:

- Must contain from 1 to 63 numbers, letters, or hyphens.
- First character must be a letter.
- Canât end with a hyphen or contain two consecutive hyphens.

Example: `my-snapshot-id`

`--db-snapshot-identifier` (string)

The identifier for the DB snapshot to restore from.

Constraints:

- Must match the identifier of an existing DB snapshot.
- Canât be specified when `DBClusterSnapshotIdentifier` is specified.
- Must be specified when `DBClusterSnapshotIdentifier` isnât specified.
- If you are restoring from a shared manual DB snapshot, the `DBSnapshotIdentifier` must be the ARN of the shared DB snapshot.

`--db-instance-class` (string)

The compute and memory capacity of the Amazon RDS DB instance, for example db.m4.large. Not all DB instance classes are available in all Amazon Web Services Regions, or for all database engines. For the full list of DB instance classes, and availability for your engine, see [DB Instance Class](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the *Amazon RDS User Guide.*

Default: The same DBInstanceClass as the original DB instance.

`--port` (integer)

The port number on which the database accepts connections.

Default: The same port as the original DB instance

Constraints: Value must be `1150-65535`

`--availability-zone` (string)

The Availability Zone (AZ) where the DB instance will be created.

Default: A random, system-chosen Availability Zone.

Constraint: You canât specify the `AvailabilityZone` parameter if the DB instance is a Multi-AZ deployment.

Example: `us-east-1a`

`--db-subnet-group-name` (string)

The name of the DB subnet group to use for the new instance.

Constraints:

- If supplied, must match the name of an existing DB subnet group.

Example: `mydbsubnetgroup`

`--multi-az` | `--no-multi-az` (boolean)

Specifies whether the DB instance is a Multi-AZ deployment.

This setting doesnât apply to RDS Custom.

Constraint: You canât specify the `AvailabilityZone` parameter if the DB instance is a Multi-AZ deployment.

`--publicly-accessible` | `--no-publicly-accessible` (boolean)

Specifies whether the DB instance is publicly accessible.

When the DB instance is publicly accessible, its Domain Name System (DNS) endpoint resolves to the private IP address from within the DB instanceâs virtual private cloud (VPC). It resolves to the public IP address from outside of the DB instanceâs VPC. Access to the DB instance is ultimately controlled by the security group it uses. That public access is not permitted if the security group assigned to the DB instance doesnât permit it.

When the DB instance isnât publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.

For more information, see  CreateDBInstance .

`--auto-minor-version-upgrade` | `--no-auto-minor-version-upgrade` (boolean)

Specifies whether to automatically apply minor version upgrades to the DB instance during the maintenance window.

If you restore an RDS Custom DB instance, you must disable this parameter.

For more information about automatic minor version upgrades, see [Automatically upgrading the minor engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades) .

`--license-model` (string)

License model information for the restored DB instance.

### Note

License models for RDS for Db2 require additional configuration. The Bring Your Own License (BYOL) model requires a custom parameter group and an Amazon Web Services License Manager self-managed license. The Db2 license through Amazon Web Services Marketplace model requires an Amazon Web Services Marketplace subscription. For more information, see [Amazon RDS for Db2 licensing options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-licensing.html) in the *Amazon RDS User Guide* .

This setting doesnât apply to Amazon Aurora or RDS Custom DB instances.

Valid Values:

- RDS for Db2 - `bring-your-own-license | marketplace-license`
- RDS for MariaDB - `general-public-license`
- RDS for Microsoft SQL Server - `license-included`
- RDS for MySQL - `general-public-license`
- RDS for Oracle - `bring-your-own-license | license-included`
- RDS for PostgreSQL - `postgresql-license`

Default: Same as the source.

`--db-name` (string)

The name of the database for the restored DB instance.

This parameter only applies to RDS for Oracle and RDS for SQL Server DB instances. It doesnât apply to the other engines or to RDS Custom DB instances.

`--engine` (string)

The database engine to use for the new instance.

This setting doesnât apply to RDS Custom.

Default: The same as source

Constraint: Must be compatible with the engine of the source. For example, you can restore a MariaDB 10.1 DB instance from a MySQL 5.6 snapshot.

Valid Values:

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

`--iops` (integer)

Specifies the amount of provisioned IOPS for the DB instance, expressed in I/O operations per second. If this parameter isnât specified, the IOPS value is taken from the backup. If this parameter is set to 0, the new instance is converted to a non-PIOPS instance. The conversion takes additional time, though your DB instance is available for connections before the conversion starts.

The provisioned IOPS value must follow the requirements for your database engine. For more information, see [Amazon RDS Provisioned IOPS storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#USER_PIOPS) in the *Amazon RDS User Guide.*

Constraints: Must be an integer greater than 1000.

`--option-group-name` (string)

The name of the option group to be used for the restored DB instance.

Permanent options, such as the TDE option for Oracle Advanced Security TDE, canât be removed from an option group, and that option group canât be removed from a DB instance after it is associated with a DB instance.

This setting doesnât apply to RDS Custom.

`--tags` (list)

A list of tags.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide* .

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

`--storage-type` (string)

Specifies the storage type to be associated with the DB instance.

Valid Values: `gp2 | gp3 | io1 | io2 | standard`

If you specify `io1` , `io2` , or `gp3` , you must also include a value for the `Iops` parameter.

Default: `io1` if the `Iops` parameter is specified, otherwise `gp3`

`--tde-credential-arn` (string)

The ARN from the key store with which to associate the instance for TDE encryption.

This setting doesnât apply to RDS Custom.

`--tde-credential-password` (string)

The password for the given ARN from the key store in order to access the device.

This setting doesnât apply to RDS Custom.

`--vpc-security-group-ids` (list)

A list of EC2 VPC security groups to associate with this DB instance.

Default: The default EC2 VPC security group for the DB subnet groupâs VPC.

(string)

Syntax:

```
"string" "string" ...
```

`--domain` (string)

The Active Directory directory ID to restore the DB instance in. The domain/ must be created prior to this operation. Currently, you can create only Db2, MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances in an Active Directory Domain.

For more information, see [Kerberos Authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/kerberos-authentication.html) in the *Amazon RDS User Guide* .

This setting doesnât apply to RDS Custom.

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

Constraints:

- Canât be longer than 64 characters.

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

Specifies whether to copy all tags from the restored DB instance to snapshots of the DB instance.

In most cases, tags arenât copied by default. However, when you restore a DB instance from a DB snapshot, RDS checks whether you specify new tags. If yes, the new tags are added to the restored DB instance. If there are no new tags, RDS looks for the tags from the source DB instance for the DB snapshot, and then adds those tags to the restored DB instance.

For more information, see [Copying tags to DB instance snapshots](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html#USER_Tagging.CopyTags) in the *Amazon RDS User Guide* .

`--domain-iam-role-name` (string)

The name of the IAM role to use when making API calls to the Directory Service.

This setting doesnât apply to RDS Custom DB instances.

`--enable-iam-database-authentication` | `--no-enable-iam-database-authentication` (boolean)

Specifies whether to enable mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.

For more information about IAM database authentication, see [IAM Database Authentication for MySQL and PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html) in the *Amazon RDS User Guide.*

This setting doesnât apply to RDS Custom.

`--enable-cloudwatch-logs-exports` (list)

The list of logs for the restored DB instance to export to CloudWatch Logs. The values in the list depend on the DB engine. For more information, see [Publishing Database Logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon RDS User Guide* .

This setting doesnât apply to RDS Custom.

(string)

Syntax:

```
"string" "string" ...
```

`--processor-features` (list)

The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.

This setting doesnât apply to RDS Custom.

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

This setting doesnât apply to RDS Custom.

`--db-parameter-group-name` (string)

The name of the DB parameter group to associate with this DB instance.

If you donât specify a value for `DBParameterGroupName` , then RDS uses the default `DBParameterGroup` for the specified DB engine.

This setting doesnât apply to RDS Custom.

Constraints:

- If supplied, must match the name of an existing DB parameter group.
- Must be 1 to 255 letters, numbers, or hyphens.
- First character must be a letter.
- Canât end with a hyphen or contain two consecutive hyphens.

`--deletion-protection` | `--no-deletion-protection` (boolean)

Specifies whether to enable deletion protection for the DB instance. The database canât be deleted when deletion protection is enabled. By default, deletion protection isnât enabled. For more information, see [Deleting a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html) .

`--enable-customer-owned-ip` | `--no-enable-customer-owned-ip` (boolean)

Specifies whether to enable a customer-owned IP address (CoIP) for an RDS on Outposts DB instance.

A *CoIP* provides local or external connectivity to resources in your Outpost subnets through your on-premises network. For some use cases, a CoIP can provide lower latency for connections to the DB instance from outside of its virtual private cloud (VPC) on your local network.

This setting doesnât apply to RDS Custom.

For more information about RDS on Outposts, see [Working with Amazon RDS on Amazon Web Services Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html) in the *Amazon RDS User Guide* .

For more information about CoIPs, see [Customer-owned IP addresses](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing) in the *Amazon Web Services Outposts User Guide* .

`--custom-iam-instance-profile` (string)

The instance profile associated with the underlying Amazon EC2 instance of an RDS Custom DB instance. The instance profile must meet the following requirements:

- The profile must exist in your account.
- The profile must have an IAM role that Amazon EC2 has permissions to assume.
- The instance profile name and the associated IAM role name must start with the prefix `AWSRDSCustom` .

For the list of permissions required for the IAM role, see [Configure IAM and your VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-setup-orcl.html#custom-setup-orcl.iam-vpc) in the *Amazon RDS User Guide* .

This setting is required for RDS Custom.

`--backup-target` (string)

Specifies where automated backups and manual snapshots are stored for the restored DB instance.

Possible values are `outposts` (Amazon Web Services Outposts) and `region` (Amazon Web Services Region). The default is `region` .

For more information, see [Working with Amazon RDS on Amazon Web Services Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html) in the *Amazon RDS User Guide* .

`--network-type` (string)

The network type of the DB instance.

Valid Values:

- `IPV4`
- `DUAL`

The network type is determined by the `DBSubnetGroup` specified for the DB instance. A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL` ).

For more information, see [Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon RDS User Guide.*

`--storage-throughput` (integer)

Specifies the storage throughput value for the DB instance.

This setting doesnât apply to RDS Custom or Amazon Aurora.

`--db-cluster-snapshot-identifier` (string)

The identifier for the Multi-AZ DB cluster snapshot to restore from.

For more information on Multi-AZ DB clusters, see [Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide* .

Constraints:

- Must match the identifier of an existing Multi-AZ DB cluster snapshot.
- Canât be specified when `DBSnapshotIdentifier` is specified.
- Must be specified when `DBSnapshotIdentifier` isnât specified.
- If you are restoring from a shared manual Multi-AZ DB cluster snapshot, the `DBClusterSnapshotIdentifier` must be the ARN of the shared snapshot.
- Canât be the identifier of an Aurora DB cluster snapshot.

`--allocated-storage` (integer)

The amount of storage (in gibibytes) to allocate initially for the DB instance. Follow the allocation rules specified in CreateDBInstance.

This setting isnât valid for RDS for SQL Server.

### Note

Be sure to allocate enough storage for your new DB instance so that the restore operation can succeed. You can also allocate additional storage for future growth.

`--dedicated-log-volume` | `--no-dedicated-log-volume` (boolean)

Specifies whether to enable a dedicated log volume (DLV) for the DB instance.

`--ca-certificate-identifier` (string)

The CA certificate identifier to use for the DB instanceâs server certificate.

This setting doesnât apply to RDS Custom DB instances.

For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide* .

`--engine-lifecycle-support` (string)

The life cycle type for this DB instance.

### Note

By default, this value is set to `open-source-rds-extended-support` , which enrolls your DB instance into Amazon RDS Extended Support. At the end of standard support, you can avoid charges for Extended Support by setting the value to `open-source-rds-extended-support-disabled` . In this case, RDS automatically upgrades your restored DB instance to a higher engine version, if the major engine version is past its end of standard support date.

You can use this setting to enroll your DB instance into Amazon RDS Extended Support. With RDS Extended Support, you can run the selected major engine version on your DB instance past the end of standard support for that engine version. For more information, see [Amazon RDS Extended Support with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html) in the *Amazon RDS User Guide* .

This setting applies only to RDS for MySQL and RDS for PostgreSQL. For Amazon Aurora DB instances, the life cycle type is managed by the DB cluster.

Valid Values: `open-source-rds-extended-support | open-source-rds-extended-support-disabled`

Default: `open-source-rds-extended-support`

`--manage-master-user-password` | `--no-manage-master-user-password` (boolean)

Specifies whether to manage the master user password with Amazon Web Services Secrets Manager in the restored DB instance.

For more information, see [Password management with Amazon Web Services Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide* .

Constraints:

- Applies to RDS for Oracle only.

`--master-user-secret-kms-key-id` (string)

The Amazon Web Services KMS key identifier to encrypt a secret that is automatically generated and managed in Amazon Web Services Secrets Manager.

This setting is valid only if the master user password is managed by RDS in Amazon Web Services Secrets Manager for the DB instance.

The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.

If you donât specify `MasterUserSecretKmsKeyId` , then the `aws/secretsmanager` KMS key is used to encrypt the secret. If the secret is in a different Amazon Web Services account, then you canât use the `aws/secretsmanager` KMS key to encrypt the secret, and you must use a customer managed KMS key.

There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.

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

**To restore a DB instance from a DB snapshot**

The following `restore-db-instance-from-db-snapshot` example creates a new DB instance named `db7-new-instance` with the `db.t3.small` DB instance class from the specified DB snapshot. The source DB instance from which the snapshot was taken uses a deprecated DB instance class, so you canât upgrade it.

```
aws rds restore-db-instance-from-db-snapshot \
    --db-instance-identifier db7-new-instance \
    --db-snapshot-identifier db7-test-snapshot \
    --db-instance-class db.t3.small
```

Output:

```
{
    "DBInstance": {
        "DBInstanceIdentifier": "db7-new-instance",
        "DBInstanceClass": "db.t3.small",
        "Engine": "mysql",
        "DBInstanceStatus": "creating",

        ...output omitted...

        "PreferredMaintenanceWindow": "mon:07:37-mon:08:07",
        "PendingModifiedValues": {},
        "MultiAZ": false,
        "EngineVersion": "5.7.22",
        "AutoMinorVersionUpgrade": true,
        "ReadReplicaDBInstanceIdentifiers": [],
        "LicenseModel": "general-public-license",

        ...output omitted...

        "DBInstanceArn": "arn:aws:rds:us-west-2:123456789012:db:db7-new-instance",
        "IAMDatabaseAuthenticationEnabled": false,
        "PerformanceInsightsEnabled": false,
        "DeletionProtection": false,
        "AssociatedRoles": []
    }
}
```

For more information, see [Restoring from a DB Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RestoreFromSnapshot.html) in the *Amazon RDS User Guide*.

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