# modify-db-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [docdb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/index.html#cli-aws-docdb) ]

# modify-db-instance

## Description

Modifies settings for an instance. You can change one or more database configuration parameters by specifying these parameters and the new values in the request.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/ModifyDBInstance)

## Synopsis

```
modify-db-instance
--db-instance-identifier <value>
[--db-instance-class <value>]
[--apply-immediately | --no-apply-immediately]
[--preferred-maintenance-window <value>]
[--auto-minor-version-upgrade | --no-auto-minor-version-upgrade]
[--new-db-instance-identifier <value>]
[--ca-certificate-identifier <value>]
[--copy-tags-to-snapshot | --no-copy-tags-to-snapshot]
[--promotion-tier <value>]
[--enable-performance-insights | --no-enable-performance-insights]
[--performance-insights-kms-key-id <value>]
[--certificate-rotation-restart | --no-certificate-rotation-restart]
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

The instance identifier. This value is stored as a lowercase string.

Constraints:

- Must match the identifier of an existing `DBInstance` .

`--db-instance-class` (string)

The new compute and memory capacity of the instance; for example, `db.r5.large` . Not all instance classes are available in all Amazon Web Services Regions.

If you modify the instance class, an outage occurs during the change. The change is applied during the next maintenance window, unless `ApplyImmediately` is specified as `true` for this request.

Default: Uses existing setting.

`--apply-immediately` | `--no-apply-immediately` (boolean)

Specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the `PreferredMaintenanceWindow` setting for the instance.

If this parameter is set to `false` , changes to the instance are applied during the next maintenance window. Some parameter changes can cause an outage and are applied on the next reboot.

Default: `false`

`--preferred-maintenance-window` (string)

The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter doesnât result in an outage except in the following situation, and the change is asynchronously applied as soon as possible. If there are pending actions that cause a reboot, and the maintenance window is changed to include the current time, changing this parameter causes a reboot of the instance. If you are moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure that pending changes are applied.

Default: Uses existing setting.

Format: `ddd:hh24:mi-ddd:hh24:mi`

Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun

Constraints: Must be at least 30 minutes.

`--auto-minor-version-upgrade` | `--no-auto-minor-version-upgrade` (boolean)

This parameter does not apply to Amazon DocumentDB. Amazon DocumentDB does not perform minor version upgrades regardless of the value set.

`--new-db-instance-identifier` (string)

The new instance identifier for the instance when renaming an instance. When you change the instance identifier, an instance reboot occurs immediately if you set `Apply Immediately` to `true` . It occurs during the next maintenance window if you set `Apply Immediately` to `false` . This value is stored as a lowercase string.

Constraints:

- Must contain from 1 to 63 letters, numbers, or hyphens.
- The first character must be a letter.
- Cannot end with a hyphen or contain two consecutive hyphens.

Example: `mydbinstance`

`--ca-certificate-identifier` (string)

Indicates the certificate that needs to be associated with the instance.

`--copy-tags-to-snapshot` | `--no-copy-tags-to-snapshot` (boolean)

A value that indicates whether to copy all tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.

`--promotion-tier` (integer)

A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.

Default: 1

Valid values: 0-15

`--enable-performance-insights` | `--no-enable-performance-insights` (boolean)

A value that indicates whether to enable Performance Insights for the DB Instance. For more information, see [Using Amazon Performance Insights](https://docs.aws.amazon.com/documentdb/latest/developerguide/performance-insights.html) .

`--performance-insights-kms-key-id` (string)

The KMS key identifier for encryption of Performance Insights data.

The KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

If you do not specify a value for PerformanceInsightsKMSKeyId, then Amazon DocumentDB uses your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services region.

`--certificate-rotation-restart` | `--no-certificate-rotation-restart` (boolean)

Specifies whether the DB instance is restarted when you rotate your SSL/TLS certificate.

By default, the DB instance is restarted when you rotate your SSL/TLS certificate. The certificate is not updated until the DB instance is restarted.

### Warning

Set this parameter only if you are *not* using SSL/TLS to connect to the DB instance.

If you are using SSL/TLS to connect to the DB instance, see [Updating Your Amazon DocumentDB TLS Certificates](https://docs.aws.amazon.com/documentdb/latest/developerguide/ca_cert_rotation.html) and [Encrypting Data in Transit](https://docs.aws.amazon.com/documentdb/latest/developerguide/security.encryption.ssl.html) in the *Amazon DocumentDB Developer Guide* .

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

**To modify an Amazon DocumentDB instance**

The following `modify-db-instance` example modifies the Amazon DocumentDB instance `sample-cluster2` by changing its instance class to `db.r4.4xlarge` and its promotion tier to `5`. The changes are applied immediately but can only be seen after the instances status is available.

```
aws docdb modify-db-instance \
    --db-instance-identifier sample-cluster2 \
    --apply-immediately \
    --db-instance-class db.r4.4xlarge \
    --promotion-tier 5
```

Output:

```
{
    "DBInstance": {
        "EngineVersion": "3.6.0",
        "StorageEncrypted": false,
        "DBInstanceClass": "db.r4.large",
        "PreferredMaintenanceWindow": "mon:08:39-mon:09:09",
        "AutoMinorVersionUpgrade": true,
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-77186e0d",
                "Status": "active"
            }
        ],
        "PreferredBackupWindow": "18:00-18:30",
        "EnabledCloudwatchLogsExports": [
            "audit"
        ],
        "AvailabilityZone": "us-west-2f",
        "DBInstanceIdentifier": "sample-cluster2",
        "InstanceCreateTime": "2019-03-15T20:36:06.338Z",
        "Engine": "docdb",
        "BackupRetentionPeriod": 7,
        "DBSubnetGroup": {
            "DBSubnetGroupName": "default",
            "DBSubnetGroupDescription": "default",
            "SubnetGroupStatus": "Complete",
            "Subnets": [
                {
                    "SubnetIdentifier": "subnet-4e26d263",
                    "SubnetAvailabilityZone": {
                        "Name": "us-west-2a"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-afc329f4",
                    "SubnetAvailabilityZone": {
                        "Name": "us-west-2c"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-53ab3636",
                    "SubnetAvailabilityZone": {
                        "Name": "us-west-2d"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-991cb8d0",
                    "SubnetAvailabilityZone": {
                        "Name": "us-west-2b"
                    },
                    "SubnetStatus": "Active"
                }
            ],
            "VpcId": "vpc-91280df6"
        },
        "PromotionTier": 2,
        "Endpoint": {
            "Address": "sample-cluster2.corcjozrlsfc.us-west-2.docdb.amazonaws.com",
            "HostedZoneId": "ZNKXH85TT8WVW",
            "Port": 27017
        },
        "DbiResourceId": "db-A2GIKUV6KPOHITGGKI2NHVISZA",
        "DBClusterIdentifier": "sample-cluster",
        "DBInstanceArn": "arn:aws:rds:us-west-2:123456789012:db:sample-cluster2",
        "PendingModifiedValues": {
            "DBInstanceClass": "db.r4.4xlarge"
        },
        "PubliclyAccessible": false,
        "DBInstanceStatus": "available"
    }
}
```

For more information, see [Modifying an Amazon DocumentDB Instance](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-modify.html) in the *Amazon DocumentDB Developer Guide*.

## Output

DBInstance -> (structure)

Detailed information about an instance.

DBInstanceIdentifier -> (string)

Contains a user-provided database identifier. This identifier is the unique key that identifies an instance.

DBInstanceClass -> (string)

Contains the name of the compute and memory capacity class of the instance.

Engine -> (string)

Provides the name of the database engine to be used for this instance.

DBInstanceStatus -> (string)

Specifies the current state of this database.

Endpoint -> (structure)

Specifies the connection endpoint.

Address -> (string)

Specifies the DNS address of the instance.

Port -> (integer)

Specifies the port that the database engine is listening on.

HostedZoneId -> (string)

Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

InstanceCreateTime -> (timestamp)

Provides the date and time that the instance was created.

PreferredBackupWindow -> (string)

Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the `BackupRetentionPeriod` .

BackupRetentionPeriod -> (integer)

Specifies the number of days for which automatic snapshots are retained.

VpcSecurityGroups -> (list)

Provides a list of VPC security group elements that the instance belongs to.

(structure)

Used as a response element for queries on virtual private cloud (VPC) security group membership.

VpcSecurityGroupId -> (string)

The name of the VPC security group.

Status -> (string)

The status of the VPC security group.

AvailabilityZone -> (string)

Specifies the name of the Availability Zone that the instance is located in.

DBSubnetGroup -> (structure)

Specifies information on the subnet group that is associated with the instance, including the name, description, and subnets in the subnet group.

DBSubnetGroupName -> (string)

The name of the subnet group.

DBSubnetGroupDescription -> (string)

Provides the description of the subnet group.

VpcId -> (string)

Provides the virtual private cloud (VPC) ID of the subnet group.

SubnetGroupStatus -> (string)

Provides the status of the subnet group.

Subnets -> (list)

Detailed information about one or more subnets within a subnet group.

(structure)

Detailed information about a subnet.

SubnetIdentifier -> (string)

Specifies the identifier of the subnet.

SubnetAvailabilityZone -> (structure)

Specifies the Availability Zone for the subnet.

Name -> (string)

The name of the Availability Zone.

SubnetStatus -> (string)

Specifies the status of the subnet.

DBSubnetGroupArn -> (string)

The Amazon Resource Name (ARN) for the DB subnet group.

PreferredMaintenanceWindow -> (string)

Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

PendingModifiedValues -> (structure)

Specifies that changes to the instance are pending. This element is included only when changes are pending. Specific changes are identified by subelements.

DBInstanceClass -> (string)

Contains the new `DBInstanceClass` for the instance that will be applied or is currently being applied.

AllocatedStorage -> (integer)

Contains the new `AllocatedStorage` size for then instance that will be applied or is currently being applied.

MasterUserPassword -> (string)

Contains the pending or currently in-progress change of the master credentials for the instance.

Port -> (integer)

Specifies the pending port for the instance.

BackupRetentionPeriod -> (integer)

Specifies the pending number of days for which automated backups are retained.

MultiAZ -> (boolean)

Indicates that the Single-AZ instance is to change to a Multi-AZ deployment.

EngineVersion -> (string)

Indicates the database engine version.

LicenseModel -> (string)

The license model for the instance.

Valid values: `license-included` , `bring-your-own-license` , `general-public-license`

Iops -> (integer)

Specifies the new Provisioned IOPS value for the instance that will be applied or is currently being applied.

DBInstanceIdentifier -> (string)

Contains the new `DBInstanceIdentifier` for the instance that will be applied or is currently being applied.

StorageType -> (string)

Specifies the storage type to be associated with the instance.

CACertificateIdentifier -> (string)

Specifies the identifier of the certificate authority (CA) certificate for the DB instance.

DBSubnetGroupName -> (string)

The new subnet group for the instance.

PendingCloudwatchLogsExports -> (structure)

A list of the log types whose configuration is still pending. These log types are in the process of being activated or deactivated.

LogTypesToEnable -> (list)

Log types that are in the process of being deactivated. After they are deactivated, these log types arenât exported to CloudWatch Logs.

(string)

LogTypesToDisable -> (list)

Log types that are in the process of being enabled. After they are enabled, these log types are exported to Amazon CloudWatch Logs.

(string)

LatestRestorableTime -> (timestamp)

Specifies the latest time to which a database can be restored with point-in-time restore.

EngineVersion -> (string)

Indicates the database engine version.

AutoMinorVersionUpgrade -> (boolean)

Does not apply. This parameter does not apply to Amazon DocumentDB. Amazon DocumentDB does not perform minor version upgrades regardless of the value set.

PubliclyAccessible -> (boolean)

Not supported. Amazon DocumentDB does not currently support public endpoints. The value of `PubliclyAccessible` is always `false` .

StatusInfos -> (list)

The status of a read replica. If the instance is not a read replica, this is blank.

(structure)

Provides a list of status information for an instance.

StatusType -> (string)

This value is currently â`read replication` .â

Normal -> (boolean)

A Boolean value that is `true` if the instance is operating normally, or `false` if the instance is in an error state.

Status -> (string)

Status of the instance. For a `StatusType` of read replica, the values can be `replicating` , error, `stopped` , or `terminated` .

Message -> (string)

Details of the error if there is an error for the instance. If the instance is not in an error state, this value is blank.

DBClusterIdentifier -> (string)

Contains the name of the cluster that the instance is a member of if the instance is a member of a cluster.

StorageEncrypted -> (boolean)

Specifies whether or not the instance is encrypted.

KmsKeyId -> (string)

If `StorageEncrypted` is `true` , the KMS key identifier for the encrypted instance.

DbiResourceId -> (string)

The Amazon Web Services Region-unique, immutable identifier for the instance. This identifier is found in CloudTrail log entries whenever the KMS key for the instance is accessed.

CACertificateIdentifier -> (string)

The identifier of the CA certificate for this DB instance.

CopyTagsToSnapshot -> (boolean)

A value that indicates whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.

PromotionTier -> (integer)

A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.

DBInstanceArn -> (string)

The Amazon Resource Name (ARN) for the instance.

EnabledCloudwatchLogsExports -> (list)

A list of log types that this instance is configured to export to CloudWatch Logs.

(string)

CertificateDetails -> (structure)

The details of the DB instanceâs server certificate.

CAIdentifier -> (string)

The CA identifier of the CA certificate used for the DB instanceâs server certificate.

ValidTill -> (timestamp)

The expiration date of the DB instanceâs server certificate.

PerformanceInsightsEnabled -> (boolean)

Set to `true` if Amazon RDS Performance Insights is enabled for the DB instance, and otherwise `false` .

PerformanceInsightsKMSKeyId -> (string)

The KMS key identifier for encryption of Performance Insights data. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.