# describe-db-clustersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-clusters.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-clusters.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [docdb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/index.html#cli-aws-docdb) ]

# describe-db-clusters

## Description

Returns information about provisioned Amazon DocumentDB clusters. This API operation supports pagination. For certain management features such as cluster and instance lifecycle management, Amazon DocumentDB leverages operational technology that is shared with Amazon RDS and Amazon Neptune. Use the `filterName=engine,Values=docdb` filter parameter to return only Amazon DocumentDB clusters.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeDBClusters)

`describe-db-clusters` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `DBClusters`

## Synopsis

```
describe-db-clusters
[--db-cluster-identifier <value>]
[--filters <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

The user-provided cluster identifier. If this parameter is specified, information from only the specific cluster is returned. This parameter isnât case sensitive.

Constraints:

- If provided, must match an existing `DBClusterIdentifier` .

`--filters` (list)

A filter that specifies one or more clusters to describe.

Supported filters:

- `db-cluster-id` - Accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list only includes information about the clusters identified by these ARNs.

(structure)

A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.

Wildcards are not supported in filters.

Name -> (string)

The name of the filter. Filter names are case sensitive.

Values -> (list)

One or more filter values. Filter values are case sensitive.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Values": ["string", ...]
  }
  ...
]
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To get detailed information about one or more Amazon DocumentDB clusters.**

The following `describe-db-clusters` example displays details for the Amazon DocumentDB cluster `sample-cluster`. By omitting the `--db-cluster-identifier` parameter you can get information of up to 100 clusters.

```
aws docdb describe-db-clusters
    --db-cluster-identifier sample-cluster
```

Output:

```
{
    "DBClusters": [
        {
            "DBClusterParameterGroup": "default.docdb3.6",
            "Endpoint": "sample-cluster.cluster-corcjozrlsfc.us-west-2.docdb.amazonaws.com",
            "PreferredBackupWindow": "00:00-00:30",
            "DBClusterIdentifier": "sample-cluster",
            "ClusterCreateTime": "2019-03-15T20:29:58.836Z",
            "LatestRestorableTime": "2019-03-18T20:28:03.239Z",
            "MasterUsername": "master-user",
            "DBClusterMembers": [
                {
                    "PromotionTier": 1,
                    "DBClusterParameterGroupStatus": "in-sync",
                    "IsClusterWriter": false,
                    "DBInstanceIdentifier": "sample-cluster"
                },
                {
                    "PromotionTier": 1,
                    "DBClusterParameterGroupStatus": "in-sync",
                    "IsClusterWriter": true,
                    "DBInstanceIdentifier": "sample-cluster2"
                }
            ],
            "PreferredMaintenanceWindow": "sat:04:30-sat:05:00",
            "VpcSecurityGroups": [
                {
                    "VpcSecurityGroupId": "sg-77186e0d",
                    "Status": "active"
                }
            ],
            "Engine": "docdb",
            "ReaderEndpoint": "sample-cluster.cluster-ro-corcjozrlsfc.us-west-2.docdb.amazonaws.com",
            "DBSubnetGroup": "default",
            "MultiAZ": true,
            "AvailabilityZones": [
                "us-west-2a",
                "us-west-2c",
                "us-west-2b"
            ],
            "EarliestRestorableTime": "2019-03-15T20:30:47.020Z",
            "DbClusterResourceId": "cluster-UP4EF2PVDDFVHHDJQTYDAIGHLE",
            "DBClusterArn": "arn:aws:rds:us-west-2:123456789012:cluster:sample-cluster",
            "BackupRetentionPeriod": 3,
            "HostedZoneId": "ZNKXH85TT8WVW",
            "StorageEncrypted": false,
            "EnabledCloudwatchLogsExports": [
                "audit"
            ],
            "AssociatedRoles": [],
            "EngineVersion": "3.6.0",
            "Port": 27017,
            "Status": "available"
        }
    ]
}
```

For more information, see [Describing Amazon DocumentDB Clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-view-details.html) in the *Amazon DocumentDB Developer Guide*.

## Output

Marker -> (string)

An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords` .

DBClusters -> (list)

A list of clusters.

(structure)

Detailed information about a cluster.

AvailabilityZones -> (list)

Provides the list of Amazon EC2 Availability Zones that instances in the cluster can be created in.

(string)

BackupRetentionPeriod -> (integer)

Specifies the number of days for which automatic snapshots are retained.

DBClusterIdentifier -> (string)

Contains a user-supplied cluster identifier. This identifier is the unique key that identifies a cluster.

DBClusterParameterGroup -> (string)

Specifies the name of the cluster parameter group for the cluster.

DBSubnetGroup -> (string)

Specifies information on the subnet group that is associated with the cluster, including the name, description, and subnets in the subnet group.

Status -> (string)

Specifies the current state of this cluster.

PercentProgress -> (string)

Specifies the progress of the operation as a percentage.

EarliestRestorableTime -> (timestamp)

The earliest time to which a database can be restored with point-in-time restore.

Endpoint -> (string)

Specifies the connection endpoint for the primary instance of the cluster.

ReaderEndpoint -> (string)

The reader endpoint for the cluster. The reader endpoint for a cluster load balances connections across the Amazon DocumentDB replicas that are available in a cluster. As clients request new connections to the reader endpoint, Amazon DocumentDB distributes the connection requests among the Amazon DocumentDB replicas in the cluster. This functionality can help balance your read workload across multiple Amazon DocumentDB replicas in your cluster.

If a failover occurs, and the Amazon DocumentDB replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ -> (boolean)

Specifies whether the cluster has instances in multiple Availability Zones.

Engine -> (string)

Provides the name of the database engine to be used for this cluster.

EngineVersion -> (string)

Indicates the database engine version.

LatestRestorableTime -> (timestamp)

Specifies the latest time to which a database can be restored with point-in-time restore.

Port -> (integer)

Specifies the port that the database engine is listening on.

MasterUsername -> (string)

Contains the master user name for the cluster.

PreferredBackupWindow -> (string)

Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the `BackupRetentionPeriod` .

PreferredMaintenanceWindow -> (string)

Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

ReplicationSourceIdentifier -> (string)

Contains the identifier of the source cluster if this cluster is a secondary cluster.

ReadReplicaIdentifiers -> (list)

Contains one or more identifiers of the secondary clusters that are associated with this cluster.

(string)

DBClusterMembers -> (list)

Provides the list of instances that make up the cluster.

(structure)

Contains information about an instance that is part of a cluster.

DBInstanceIdentifier -> (string)

Specifies the instance identifier for this member of the cluster.

IsClusterWriter -> (boolean)

A value that is `true` if the cluster member is the primary instance for the cluster and `false` otherwise.

DBClusterParameterGroupStatus -> (string)

Specifies the status of the cluster parameter group for this member of the DB cluster.

PromotionTier -> (integer)

A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.

VpcSecurityGroups -> (list)

Provides a list of virtual private cloud (VPC) security groups that the cluster belongs to.

(structure)

Used as a response element for queries on virtual private cloud (VPC) security group membership.

VpcSecurityGroupId -> (string)

The name of the VPC security group.

Status -> (string)

The status of the VPC security group.

HostedZoneId -> (string)

Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted -> (boolean)

Specifies whether the cluster is encrypted.

KmsKeyId -> (string)

If `StorageEncrypted` is `true` , the KMS key identifier for the encrypted cluster.

DbClusterResourceId -> (string)

The Amazon Web Services Region-unique, immutable identifier for the cluster. This identifier is found in CloudTrail log entries whenever the KMS key for the cluster is accessed.

DBClusterArn -> (string)

The Amazon Resource Name (ARN) for the cluster.

AssociatedRoles -> (list)

Provides a list of the Identity and Access Management (IAM) roles that are associated with the cluster. (IAM) roles that are associated with a cluster grant permission for the cluster to access other Amazon Web Services services on your behalf.

(structure)

Describes an Identity and Access Management (IAM) role that is associated with a cluster.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAMrole that is associated with the DB cluster.

Status -> (string)

Describes the state of association between the IAMrole and the cluster. The `Status` property returns one of the following values:

- `ACTIVE` - The IAMrole ARN is associated with the cluster and can be used to access other Amazon Web Services services on your behalf.
- `PENDING` - The IAMrole ARN is being associated with the cluster.
- `INVALID` - The IAMrole ARN is associated with the cluster, but the cluster cannot assume the IAMrole to access other Amazon Web Services services on your behalf.

CloneGroupId -> (string)

Identifies the clone group to which the DB cluster is associated.

ClusterCreateTime -> (timestamp)

Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports -> (list)

A list of log types that this cluster is configured to export to Amazon CloudWatch Logs.

(string)

DeletionProtection -> (boolean)

Specifies whether this cluster can be deleted. If `DeletionProtection` is enabled, the cluster cannot be deleted unless it is modified and `DeletionProtection` is disabled. `DeletionProtection` protects clusters from being accidentally deleted.

StorageType -> (string)

Storage type associated with your cluster

Storage type associated with your cluster

For information on storage types for Amazon DocumentDB clusters, see Cluster storage configurations in the *Amazon DocumentDB Developer Guide* .

Valid values for storage type - `standard | iopt1`

Default value is `standard`

MasterUserSecret -> (structure)

The secret managed by Amazon DocumentDB in Amazon Web Services Secrets Manager for the master user password.

SecretArn -> (string)

The Amazon Resource Name (ARN) of the secret.

SecretStatus -> (string)

The status of the secret.

The possible status values include the following:

- creating - The secret is being created.
- active - The secret is available for normal use and rotation.
- rotating - The secret is being rotated.
- impaired - The secret can be used to access database credentials, but it canât be rotated. A secret might have this status if, for example, permissions are changed so that Amazon DocumentDB can no longer access either the secret or the KMS key for the secret. When a secret has this status, you can correct the condition that caused the status. Alternatively, modify the instance to turn off automatic management of database credentials, and then modify the instance again to turn on automatic management of database credentials.

KmsKeyId -> (string)

The Amazon Web Services KMS key identifier that is used to encrypt the secret.