# failover-db-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/failover-db-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/failover-db-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [neptune](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/index.html#cli-aws-neptune) ]

# failover-db-cluster

## Description

Forces a failover for a DB cluster.

A failover for a DB cluster promotes one of the Read Replicas (read-only instances) in the DB cluster to be the primary instance (the cluster writer).

Amazon Neptune will automatically fail over to a Read Replica, if one exists, when the primary instance fails. You can force a failover when you want to simulate a failure of a primary instance for testing. Because each instance in a DB cluster has its own endpoint address, you will need to clean up and re-establish any existing connections that use those endpoint addresses when the failover is complete.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/FailoverDBCluster)

## Synopsis

```
failover-db-cluster
[--db-cluster-identifier <value>]
[--target-db-instance-identifier <value>]
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

A DB cluster identifier to force a failover for. This parameter is not case-sensitive.

Constraints:

- Must match the identifier of an existing DBCluster.

`--target-db-instance-identifier` (string)

The name of the instance to promote to the primary instance.

You must specify the instance identifier for an Read Replica in the DB cluster. For example, `mydbcluster-replica1` .

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

DBCluster -> (structure)

Contains the details of an Amazon Neptune DB cluster.

This data type is used as a response element in the  DescribeDBClusters .

AllocatedStorage -> (integer)

`AllocatedStorage` always returns 1, because Neptune DB cluster storage size is not fixed, but instead automatically adjusts as needed.

AvailabilityZones -> (list)

Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.

(string)

BackupRetentionPeriod -> (integer)

Specifies the number of days for which automatic DB snapshots are retained.

CharacterSetName -> (string)

Not supported by Neptune.

DatabaseName -> (string)

Contains the name of the initial database of this DB cluster that was provided at create time, if one was specified when the DB cluster was created. This same name is returned for the life of the DB cluster.

DBClusterIdentifier -> (string)

Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.

DBClusterParameterGroup -> (string)

Specifies the name of the DB cluster parameter group for the DB cluster.

DBSubnetGroup -> (string)

Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.

Status -> (string)

Specifies the current state of this DB cluster.

PercentProgress -> (string)

Specifies the progress of the operation as a percentage.

EarliestRestorableTime -> (timestamp)

Specifies the earliest time to which a database can be restored with point-in-time restore.

Endpoint -> (string)

Specifies the connection endpoint for the primary instance of the DB cluster.

ReaderEndpoint -> (string)

The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Read Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Neptune distributes the connection requests among the Read Replicas in the DB cluster. This functionality can help balance your read workload across multiple Read Replicas in your DB cluster.

If a failover occurs, and the Read Replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ -> (boolean)

Specifies whether the DB cluster has instances in multiple Availability Zones.

Engine -> (string)

Provides the name of the database engine to be used for this DB cluster.

EngineVersion -> (string)

Indicates the database engine version.

LatestRestorableTime -> (timestamp)

Specifies the latest time to which a database can be restored with point-in-time restore.

Port -> (integer)

Specifies the port that the database engine is listening on.

MasterUsername -> (string)

Not supported by Neptune.

DBClusterOptionGroupMemberships -> (list)

Not supported by Neptune.

(structure)

Not supported by Neptune.

DBClusterOptionGroupName -> (string)

Not supported by Neptune.

Status -> (string)

Not supported by Neptune.

PreferredBackupWindow -> (string)

Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the `BackupRetentionPeriod` .

PreferredMaintenanceWindow -> (string)

Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

ReplicationSourceIdentifier -> (string)

Not supported by Neptune.

ReadReplicaIdentifiers -> (list)

Contains one or more identifiers of the Read Replicas associated with this DB cluster.

(string)

DBClusterMembers -> (list)

Provides the list of instances that make up the DB cluster.

(structure)

Contains information about an instance that is part of a DB cluster.

DBInstanceIdentifier -> (string)

Specifies the instance identifier for this member of the DB cluster.

IsClusterWriter -> (boolean)

Value that is `true` if the cluster member is the primary instance for the DB cluster and `false` otherwise.

DBClusterParameterGroupStatus -> (string)

Specifies the status of the DB cluster parameter group for this member of the DB cluster.

PromotionTier -> (integer)

A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.

VpcSecurityGroups -> (list)

Provides a list of VPC security groups that the DB cluster belongs to.

(structure)

This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId -> (string)

The name of the VPC security group.

Status -> (string)

The status of the VPC security group.

HostedZoneId -> (string)

Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted -> (boolean)

Specifies whether the DB cluster is encrypted.

KmsKeyId -> (string)

If `StorageEncrypted` is true, the Amazon KMS key identifier for the encrypted DB cluster.

DbClusterResourceId -> (string)

The Amazon Region-unique, immutable identifier for the DB cluster. This identifier is found in Amazon CloudTrail log entries whenever the Amazon KMS key for the DB cluster is accessed.

DBClusterArn -> (string)

The Amazon Resource Name (ARN) for the DB cluster.

AssociatedRoles -> (list)

Provides a list of the Amazon Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other Amazon services on your behalf.

(structure)

Describes an Amazon Identity and Access Management (IAM) role that is associated with a DB cluster.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status -> (string)

Describes the state of association between the IAM role and the DB cluster. The Status property returns one of the following values:

- `ACTIVE` - the IAM role ARN is associated with the DB cluster and can be used to access other Amazon services on your behalf.
- `PENDING` - the IAM role ARN is being associated with the DB cluster.
- `INVALID` - the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other Amazon services on your behalf.

FeatureName -> (string)

The name of the feature associated with the Amazon Identity and Access Management (IAM) role. For the list of supported feature names, see  DescribeDBEngineVersions .

IAMDatabaseAuthenticationEnabled -> (boolean)

True if mapping of Amazon Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.

CloneGroupId -> (string)

Identifies the clone group to which the DB cluster is associated.

ClusterCreateTime -> (timestamp)

Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

CopyTagsToSnapshot -> (boolean)

*If set to ``true`` , tags are copied to any snapshot of the DB cluster that is created.*

EnabledCloudwatchLogsExports -> (list)

A list of the log types that this DB cluster is configured to export to CloudWatch Logs. Valid log types are: `audit` (to publish audit logs to CloudWatch) and slowquery (to publish slow-query logs to CloudWatch). See [Publishing Neptune logs to Amazon CloudWatch logs](https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch-logs.html) .

(string)

PendingModifiedValues -> (structure)

This data type is used as a response element in the `ModifyDBCluster` operation and contains changes that will be applied during the next maintenance window.

PendingCloudwatchLogsExports -> (structure)

This `PendingCloudwatchLogsExports` structure specifies pending changes to which CloudWatch logs are enabled and which are disabled.

LogTypesToEnable -> (list)

Log types that are in the process of being deactivated. After they are deactivated, these log types arenât exported to CloudWatch Logs.

(string)

LogTypesToDisable -> (list)

Log types that are in the process of being enabled. After they are enabled, these log types are exported to CloudWatch Logs.

(string)

DBClusterIdentifier -> (string)

The DBClusterIdentifier value for the DB cluster.

IAMDatabaseAuthenticationEnabled -> (boolean)

A value that indicates whether mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts is enabled.

EngineVersion -> (string)

The database engine version.

BackupRetentionPeriod -> (integer)

The number of days for which automatic DB snapshots are retained.

StorageType -> (string)

The pending change in storage type for the DB cluster. Valid Values:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/failover-db-cluster.html#id1)`standard` ** â ( *the default* ) Configures cost-effective database storage for applications with moderate to small I/O usage.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/failover-db-cluster.html#id3)`iopt1` ** â Enables [I/O-Optimized storage](https://docs.aws.amazon.com/neptune/latest/userguide/storage-types.html#provisioned-iops-storage) thatâs designed to meet the needs of I/O-intensive graph workloads that require predictable pricing with low I/O latency and consistent I/O throughput. Neptune I/O-Optimized storage is only available starting with engine release 1.3.0.0.

AllocatedStorage -> (integer)

The allocated storage size in gibibytes (GiB) for database engines. For Neptune, `AllocatedStorage` always returns 1, because Neptune DB cluster storage size isnât fixed, but instead automatically adjusts as needed.

Iops -> (integer)

The Provisioned IOPS (I/O operations per second) value. This setting is only for Multi-AZ DB clusters.

DeletionProtection -> (boolean)

Indicates whether or not the DB cluster has deletion protection enabled. The database canât be deleted when deletion protection is enabled.

CrossAccountClone -> (boolean)

If set to `true` , the DB cluster can be cloned across accounts.

AutomaticRestartTime -> (timestamp)

Time at which the DB cluster will be automatically restarted.

ServerlessV2ScalingConfiguration -> (structure)

Shows the scaling configuration for a Neptune Serverless DB cluster.

For more information, see [Using Amazon Neptune Serverless](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless-using.html) in the *Amazon Neptune User Guide* .

MinCapacity -> (double)

The minimum number of Neptune capacity units (NCUs) for a DB instance in a Neptune Serverless cluster. You can specify NCU values in half-step increments, such as 8, 8.5, 9, and so on.

MaxCapacity -> (double)

The maximum number of Neptune capacity units (NCUs) for a DB instance in a Neptune Serverless cluster. You can specify NCU values in half-step increments, such as 40, 40.5, 41, and so on.

GlobalClusterIdentifier -> (string)

Contains a user-supplied global database cluster identifier. This identifier is the unique key that identifies a global database.

IOOptimizedNextAllowedModificationTime -> (timestamp)

The next time you can modify the DB cluster to use the `iopt1` storage type.

StorageType -> (string)

The storage type used by the DB cluster.

Valid Values:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/failover-db-cluster.html#id5)`standard` ** â ( *the default* ) Provides cost-effective database storage for applications with moderate to small I/O usage.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/failover-db-cluster.html#id7)`iopt1` ** â Enables [I/O-Optimized storage](https://docs.aws.amazon.com/neptune/latest/userguide/storage-types.html#provisioned-iops-storage) thatâs designed to meet the needs of I/O-intensive graph workloads that require predictable pricing with low I/O latency and consistent I/O throughput. Neptune I/O-Optimized storage is only available starting with engine release 1.3.0.0.