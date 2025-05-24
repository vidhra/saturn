# stop-db-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/stop-db-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/stop-db-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# stop-db-cluster

## Description

Stops an Amazon Aurora DB cluster. When you stop a DB cluster, Aurora retains the DB clusterâs metadata, including its endpoints and DB parameter groups. Aurora also retains the transaction logs so you can do a point-in-time restore if necessary.

For more information, see [Stopping and Starting an Aurora Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-cluster-stop-start.html) in the *Amazon Aurora User Guide* .

### Note

This operation only applies to Aurora DB clusters.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/StopDBCluster)

## Synopsis

```
stop-db-cluster
--db-cluster-identifier <value>
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

`--db-cluster-identifier` (string)

The DB cluster identifier of the Amazon Aurora DB cluster to be stopped. This parameter is stored as a lowercase string.

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

**To stop a DB cluster**

The following `stop-db-cluster` example stops a DB cluster and its DB instances.

```
aws rds stop-db-cluster \
    --db-cluster-identifier mydbcluster
```

Output:

```
{
    "DBCluster": {
        "AllocatedStorage": 1,
        "AvailabilityZones": [
            "us-east-1a",
            "us-east-1e",
            "us-east-1b"
        ],
        "BackupRetentionPeriod": 1,
        "DatabaseName": "mydb",
        "DBClusterIdentifier": "mydbcluster",
        ...some output truncated...
    }
}
```

For more information, see [Stopping and starting an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-cluster-stop-start.html) in the *Amazon Aurora User Guide*.

## Output

DBCluster -> (structure)

Contains the details of an Amazon Aurora DB cluster or Multi-AZ DB cluster.

For an Amazon Aurora DB cluster, this data type is used as a response element in the operations `CreateDBCluster` , `DeleteDBCluster` , `DescribeDBClusters` , `FailoverDBCluster` , `ModifyDBCluster` , `PromoteReadReplicaDBCluster` , `RestoreDBClusterFromS3` , `RestoreDBClusterFromSnapshot` , `RestoreDBClusterToPointInTime` , `StartDBCluster` , and `StopDBCluster` .

For a Multi-AZ DB cluster, this data type is used as a response element in the operations `CreateDBCluster` , `DeleteDBCluster` , `DescribeDBClusters` , `FailoverDBCluster` , `ModifyDBCluster` , `RebootDBCluster` , `RestoreDBClusterFromSnapshot` , and `RestoreDBClusterToPointInTime` .

For more information on Amazon Aurora DB clusters, see [What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide.*

For more information on Multi-AZ DB clusters, see [Multi-AZ deployments with two readable standby DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide.*

AllocatedStorage -> (integer)

`AllocatedStorage` specifies the allocated storage size in gibibytes (GiB). For Aurora, `AllocatedStorage` can vary because Aurora DB cluster storage size adjusts as needed.

AvailabilityZones -> (list)

The list of Availability Zones (AZs) where instances in the DB cluster can be created.

(string)

BackupRetentionPeriod -> (integer)

The number of days for which automatic DB snapshots are retained.

CharacterSetName -> (string)

If present, specifies the name of the character set that this cluster is associated with.

DatabaseName -> (string)

The name of the initial database that was specified for the DB cluster when it was created, if one was provided. This same name is returned for the life of the DB cluster.

DBClusterIdentifier -> (string)

The user-supplied identifier for the DB cluster. This identifier is the unique key that identifies a DB cluster.

DBClusterParameterGroup -> (string)

The name of the DB cluster parameter group for the DB cluster.

DBSubnetGroup -> (string)

Information about the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.

Status -> (string)

The current state of this DB cluster.

AutomaticRestartTime -> (timestamp)

The time when a stopped DB cluster is restarted automatically.

PercentProgress -> (string)

The progress of the operation as a percentage.

EarliestRestorableTime -> (timestamp)

The earliest time to which a database can be restored with point-in-time restore.

Endpoint -> (string)

The connection endpoint for the primary instance of the DB cluster.

ReaderEndpoint -> (string)

The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Aurora Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Aurora distributes the connection requests among the Aurora Replicas in the DB cluster. This functionality can help balance your read workload across multiple Aurora Replicas in your DB cluster.

If a failover occurs, and the Aurora Replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Aurora Replicas in the cluster, you can then reconnect to the reader endpoint.

CustomEndpoints -> (list)

The custom endpoints associated with the DB cluster.

(string)

MultiAZ -> (boolean)

Indicates whether the DB cluster has instances in multiple Availability Zones.

Engine -> (string)

The database engine used for this DB cluster.

EngineVersion -> (string)

The version of the database engine.

LatestRestorableTime -> (timestamp)

The latest time to which a database can be restored with point-in-time restore.

Port -> (integer)

The port that the database engine is listening on.

MasterUsername -> (string)

The master username for the DB cluster.

DBClusterOptionGroupMemberships -> (list)

The list of option group memberships for this DB cluster.

(structure)

Contains status information for a DB cluster option group.

DBClusterOptionGroupName -> (string)

Specifies the name of the DB cluster option group.

Status -> (string)

Specifies the status of the DB cluster option group.

PreferredBackupWindow -> (string)

The daily time range during which automated backups are created if automated backups are enabled, as determined by the `BackupRetentionPeriod` .

PreferredMaintenanceWindow -> (string)

The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

ReplicationSourceIdentifier -> (string)

The identifier of the source DB cluster if this DB cluster is a read replica.

ReadReplicaIdentifiers -> (list)

Contains one or more identifiers of the read replicas associated with this DB cluster.

(string)

StatusInfos -> (list)

Reserved for future use.

(structure)

Reserved for future use.

StatusType -> (string)

Reserved for future use.

Normal -> (boolean)

Reserved for future use.

Status -> (string)

Reserved for future use.

Message -> (string)

Reserved for future use.

DBClusterMembers -> (list)

The list of DB instances that make up the DB cluster.

(structure)

Contains information about an instance that is part of a DB cluster.

DBInstanceIdentifier -> (string)

Specifies the instance identifier for this member of the DB cluster.

IsClusterWriter -> (boolean)

Indicates whether the cluster member is the primary DB instance for the DB cluster.

DBClusterParameterGroupStatus -> (string)

Specifies the status of the DB cluster parameter group for this member of the DB cluster.

PromotionTier -> (integer)

A value that specifies the order in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see [Fault Tolerance for an Aurora DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html#Aurora.Managing.FaultTolerance) in the *Amazon Aurora User Guide* .

VpcSecurityGroups -> (list)

The list of VPC security groups that the DB cluster belongs to.

(structure)

This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId -> (string)

The name of the VPC security group.

Status -> (string)

The membership status of the VPC security group.

Currently, the only valid status is `active` .

HostedZoneId -> (string)

The ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted -> (boolean)

Indicates whether the DB cluster is encrypted.

KmsKeyId -> (string)

If `StorageEncrypted` is enabled, the Amazon Web Services KMS key identifier for the encrypted DB cluster.

The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

DbClusterResourceId -> (string)

The Amazon Web Services Region-unique, immutable identifier for the DB cluster. This identifier is found in Amazon Web Services CloudTrail log entries whenever the KMS key for the DB cluster is accessed.

DBClusterArn -> (string)

The Amazon Resource Name (ARN) for the DB cluster.

AssociatedRoles -> (list)

A list of the Amazon Web Services Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other Amazon Web Services on your behalf.

(structure)

Describes an Amazon Web Services Identity and Access Management (IAM) role that is associated with a DB cluster.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status -> (string)

Describes the state of association between the IAM role and the DB cluster. The Status property returns one of the following values:

- `ACTIVE` - the IAM role ARN is associated with the DB cluster and can be used to access other Amazon Web Services on your behalf.
- `PENDING` - the IAM role ARN is being associated with the DB cluster.
- `INVALID` - the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other Amazon Web Services on your behalf.

FeatureName -> (string)

The name of the feature associated with the Amazon Web Services Identity and Access Management (IAM) role. For information about supported feature names, see  DBEngineVersion .

IAMDatabaseAuthenticationEnabled -> (boolean)

Indicates whether the mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts is enabled.

CloneGroupId -> (string)

The ID of the clone group with which the DB cluster is associated. For newly created clusters, the ID is typically null.

If you clone a DB cluster when the ID is null, the operation populates the ID value for the source cluster and the clone because both clusters become part of the same clone group. Even if you delete the clone cluster, the clone group ID remains for the lifetime of the source cluster to show that it was used in a cloning operation.

For PITR, the clone group ID is inherited from the source cluster. For snapshot restore operations, the clone group ID isnât inherited from the source cluster.

ClusterCreateTime -> (timestamp)

The time when the DB cluster was created, in Universal Coordinated Time (UTC).

EarliestBacktrackTime -> (timestamp)

The earliest time to which a DB cluster can be backtracked.

BacktrackWindow -> (long)

The target backtrack window, in seconds. If this value is set to `0` , backtracking is disabled for the DB cluster. Otherwise, backtracking is enabled.

BacktrackConsumedChangeRecords -> (long)

The number of change records stored for Backtrack.

EnabledCloudwatchLogsExports -> (list)

A list of log types that this DB cluster is configured to export to CloudWatch Logs.

Log types vary by DB engine. For information about the log types for each DB engine, see [Amazon RDS Database Log Files](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html) in the *Amazon Aurora User Guide.*

(string)

Capacity -> (integer)

The current capacity of an Aurora Serverless v1 DB cluster. The capacity is `0` (zero) when the cluster is paused.

For more information about Aurora Serverless v1, see [Using Amazon Aurora Serverless v1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html) in the *Amazon Aurora User Guide* .

EngineMode -> (string)

The DB engine mode of the DB cluster, either `provisioned` or `serverless` .

For more information, see [CreateDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html) .

ScalingConfigurationInfo -> (structure)

The scaling configuration for an Aurora DB cluster in `serverless` DB engine mode.

For more information, see [Using Amazon Aurora Serverless v1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html) in the *Amazon Aurora User Guide* .

MinCapacity -> (integer)

The minimum capacity for an Aurora DB cluster in `serverless` DB engine mode.

MaxCapacity -> (integer)

The maximum capacity for an Aurora DB cluster in `serverless` DB engine mode.

AutoPause -> (boolean)

Indicates whether automatic pause is allowed for the Aurora DB cluster in `serverless` DB engine mode.

When the value is set to false for an Aurora Serverless v1 DB cluster, the DB cluster automatically resumes.

SecondsUntilAutoPause -> (integer)

The remaining amount of time, in seconds, before the Aurora DB cluster in `serverless` mode is paused. A DB cluster can be paused only when itâs idle (it has no connections).

TimeoutAction -> (string)

The action that occurs when Aurora times out while attempting to change the capacity of an Aurora Serverless v1 cluster. The value is either `ForceApplyCapacityChange` or `RollbackCapacityChange` .

`ForceApplyCapacityChange` , the default, sets the capacity to the specified value as soon as possible.

`RollbackCapacityChange` ignores the capacity change if a scaling point isnât found in the timeout period.

SecondsBeforeTimeout -> (integer)

The number of seconds before scaling times out. What happens when an attempted scaling action times out is determined by the `TimeoutAction` setting.

RdsCustomClusterConfiguration -> (structure)

Reserved for future use.

InterconnectSubnetId -> (string)

Reserved for future use.

TransitGatewayMulticastDomainId -> (string)

Reserved for future use.

ReplicaMode -> (string)

Reserved for future use.

DeletionProtection -> (boolean)

Indicates whether the DB cluster has deletion protection enabled. The database canât be deleted when deletion protection is enabled.

HttpEndpointEnabled -> (boolean)

Indicates whether the HTTP endpoint is enabled for an Aurora DB cluster.

When enabled, the HTTP endpoint provides a connectionless web service API (RDS Data API) for running SQL queries on the DB cluster. You can also query your database from inside the RDS console with the RDS query editor.

For more information, see [Using RDS Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) in the *Amazon Aurora User Guide* .

ActivityStreamMode -> (string)

The mode of the database activity stream. Database events such as a change or access generate an activity stream event. The database session can handle these events either synchronously or asynchronously.

ActivityStreamStatus -> (string)

The status of the database activity stream.

ActivityStreamKmsKeyId -> (string)

The Amazon Web Services KMS key identifier used for encrypting messages in the database activity stream.

The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

ActivityStreamKinesisStreamName -> (string)

The name of the Amazon Kinesis data stream used for the database activity stream.

CopyTagsToSnapshot -> (boolean)

Indicates whether tags are copied from the DB cluster to snapshots of the DB cluster.

CrossAccountClone -> (boolean)

Indicates whether the DB cluster is a clone of a DB cluster owned by a different Amazon Web Services account.

DomainMemberships -> (list)

The Active Directory Domain membership records associated with the DB cluster.

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

GlobalWriteForwardingStatus -> (string)

The status of write forwarding for a secondary cluster in an Aurora global database.

GlobalWriteForwardingRequested -> (boolean)

Indicates whether write forwarding is enabled for a secondary cluster in an Aurora global database. Because write forwarding takes time to enable, check the value of `GlobalWriteForwardingStatus` to confirm that the request has completed before using the write forwarding feature for this cluster.

PendingModifiedValues -> (structure)

Information about pending changes to the DB cluster. This information is returned only when there are pending changes. Specific changes are identified by subelements.

PendingCloudwatchLogsExports -> (structure)

A list of the log types whose configuration is still pending. In other words, these log types are in the process of being activated or deactivated.

LogTypesToEnable -> (list)

Log types that are in the process of being deactivated. After they are deactivated, these log types arenât exported to CloudWatch Logs.

(string)

LogTypesToDisable -> (list)

Log types that are in the process of being enabled. After they are enabled, these log types are exported to CloudWatch Logs.

(string)

DBClusterIdentifier -> (string)

The DBClusterIdentifier value for the DB cluster.

MasterUserPassword -> (string)

The master credentials for the DB cluster.

IAMDatabaseAuthenticationEnabled -> (boolean)

Indicates whether mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts is enabled.

EngineVersion -> (string)

The database engine version.

BackupRetentionPeriod -> (integer)

The number of days for which automatic DB snapshots are retained.

AllocatedStorage -> (integer)

The allocated storage size in gibibytes (GiB) for all database engines except Amazon Aurora. For Aurora, `AllocatedStorage` always returns 1, because Aurora DB cluster storage size isnât fixed, but instead automatically adjusts as needed.

RdsCustomClusterConfiguration -> (structure)

Reserved for future use.

InterconnectSubnetId -> (string)

Reserved for future use.

TransitGatewayMulticastDomainId -> (string)

Reserved for future use.

ReplicaMode -> (string)

Reserved for future use.

Iops -> (integer)

The Provisioned IOPS (I/O operations per second) value. This setting is only for non-Aurora Multi-AZ DB clusters.

StorageType -> (string)

The storage type for the DB cluster.

CertificateDetails -> (structure)

The details of the DB instanceâs server certificate.

For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide* .

CAIdentifier -> (string)

The CA identifier of the CA certificate used for the DB instanceâs server certificate.

ValidTill -> (timestamp)

The expiration date of the DB instanceâs server certificate.

DBClusterInstanceClass -> (string)

The name of the compute and memory capacity class of the DB instance.

This setting is only for non-Aurora Multi-AZ DB clusters.

StorageType -> (string)

The storage type associated with the DB cluster.

Iops -> (integer)

The Provisioned IOPS (I/O operations per second) value.

This setting is only for non-Aurora Multi-AZ DB clusters.

PubliclyAccessible -> (boolean)

Indicates whether the DB cluster is publicly accessible.

When the DB cluster is publicly accessible and you connect from outside of the DB clusterâs virtual private cloud (VPC), its Domain Name System (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB cluster, the endpoint resolves to the private IP address. Access to the DB cluster is ultimately controlled by the security group it uses. That public access isnât permitted if the security group assigned to the DB cluster doesnât permit it.

When the DB cluster isnât publicly accessible, it is an internal DB cluster with a DNS name that resolves to a private IP address.

For more information, see  CreateDBCluster .

This setting is only for non-Aurora Multi-AZ DB clusters.

AutoMinorVersionUpgrade -> (boolean)

Indicates whether minor version patches are applied automatically.

This setting is for Aurora DB clusters and Multi-AZ DB clusters.

For more information about automatic minor version upgrades, see [Automatically upgrading the minor engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades) .

MonitoringInterval -> (integer)

The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster.

This setting is only for -Aurora DB clusters and Multi-AZ DB clusters.

MonitoringRoleArn -> (string)

The ARN for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.

This setting is only for Aurora DB clusters and Multi-AZ DB clusters.

DatabaseInsightsMode -> (string)

The mode of Database Insights that is enabled for the DB cluster.

PerformanceInsightsEnabled -> (boolean)

Indicates whether Performance Insights is enabled for the DB cluster.

This setting is only for Aurora DB clusters and Multi-AZ DB clusters.

PerformanceInsightsKMSKeyId -> (string)

The Amazon Web Services KMS key identifier for encryption of Performance Insights data.

The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

This setting is only for Aurora DB clusters and Multi-AZ DB clusters.

PerformanceInsightsRetentionPeriod -> (integer)

The number of days to retain Performance Insights data.

This setting is only for Aurora DB clusters and Multi-AZ DB clusters.

Valid Values:

- `7`
- *month* * 31, where *month* is a number of months from 1-23. Examples: `93` (3 months * 31), `341` (11 months * 31), `589` (19 months * 31)
- `731`

Default: `7` days

ServerlessV2ScalingConfiguration -> (structure)

The scaling configuration for an Aurora Serverless v2 DB cluster.

For more information, see [Using Amazon Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html) in the *Amazon Aurora User Guide* .

MinCapacity -> (double)

The minimum number of Aurora capacity units (ACUs) for a DB instance in an Aurora Serverless v2 cluster. You can specify ACU values in half-step increments, such as 8, 8.5, 9, and so on. For Aurora versions that support the Aurora Serverless v2 auto-pause feature, the smallest value that you can use is 0. For versions that donât support Aurora Serverless v2 auto-pause, the smallest value that you can use is 0.5.

MaxCapacity -> (double)

The maximum number of Aurora capacity units (ACUs) for a DB instance in an Aurora Serverless v2 cluster. You can specify ACU values in half-step increments, such as 32, 32.5, 33, and so on. The largest value that you can use is 256 for recent Aurora versions, or 128 for older versions.

SecondsUntilAutoPause -> (integer)

The number of seconds an Aurora Serverless v2 DB instance must be idle before Aurora attempts to automatically pause it. This property is only shown when the minimum capacity for the cluster is set to 0 ACUs. Changing the minimum capacity to a nonzero value removes this property. If you later change the minimum capacity back to 0 ACUs, this property is reset to its default value unless you specify it again.

This value ranges between 300 seconds (five minutes) and 86,400 seconds (one day). The default is 300 seconds.

NetworkType -> (string)

The network type of the DB instance.

The network type is determined by the `DBSubnetGroup` specified for the DB cluster. A `DBSubnetGroup` can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL` ).

For more information, see [Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon Aurora User Guide.*

This setting is only for Aurora DB clusters.

Valid Values: `IPV4 | DUAL`

DBSystemId -> (string)

Reserved for future use.

MasterUserSecret -> (structure)

The secret managed by RDS in Amazon Web Services Secrets Manager for the master user password.

For more information, see [Password management with Amazon Web Services Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide* and [Password management with Amazon Web Services Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html) in the *Amazon Aurora User Guide.*

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

IOOptimizedNextAllowedModificationTime -> (timestamp)

The next time you can modify the DB cluster to use the `aurora-iopt1` storage type.

This setting is only for Aurora DB clusters.

LocalWriteForwardingStatus -> (string)

Indicates whether an Aurora DB cluster has in-cluster write forwarding enabled, not enabled, requested, or is in the process of enabling it.

AwsBackupRecoveryPointArn -> (string)

The Amazon Resource Name (ARN) of the recovery point in Amazon Web Services Backup.

LimitlessDatabase -> (structure)

The details for Aurora Limitless Database.

Status -> (string)

The status of Aurora Limitless Database.

MinRequiredACU -> (double)

The minimum required capacity for Aurora Limitless Database in Aurora capacity units (ACUs).

StorageThroughput -> (integer)

The storage throughput for the DB cluster. The throughput is automatically set based on the IOPS that you provision, and is not configurable.

This setting is only for non-Aurora Multi-AZ DB clusters.

ClusterScalabilityType -> (string)

The scalability mode of the Aurora DB cluster. When set to `limitless` , the cluster operates as an Aurora Limitless Database. When set to `standard` (the default), the cluster uses normal DB instance creation.

CertificateDetails -> (structure)

The details of the DB instanceâs server certificate.

For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide* .

CAIdentifier -> (string)

The CA identifier of the CA certificate used for the DB instanceâs server certificate.

ValidTill -> (timestamp)

The expiration date of the DB instanceâs server certificate.

EngineLifecycleSupport -> (string)

The lifecycle type for the DB cluster.

For more information, see CreateDBCluster.