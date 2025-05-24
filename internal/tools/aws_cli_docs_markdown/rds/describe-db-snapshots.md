# describe-db-snapshotsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-snapshots.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-snapshots.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# describe-db-snapshots

## Description

Returns information about DB snapshots. This API action supports pagination.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBSnapshots)

`describe-db-snapshots` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `DBSnapshots`

## Synopsis

```
describe-db-snapshots
[--db-instance-identifier <value>]
[--db-snapshot-identifier <value>]
[--snapshot-type <value>]
[--filters <value>]
[--include-shared | --no-include-shared]
[--include-public | --no-include-public]
[--dbi-resource-id <value>]
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

`--db-instance-identifier` (string)

The ID of the DB instance to retrieve the list of DB snapshots for. This parameter isnât case-sensitive.

Constraints:

- If supplied, must match the identifier of an existing DBInstance.

`--db-snapshot-identifier` (string)

A specific DB snapshot identifier to describe. This value is stored as a lowercase string.

Constraints:

- If supplied, must match the identifier of an existing DBSnapshot.
- If this identifier is for an automated snapshot, the `SnapshotType` parameter must also be specified.

`--snapshot-type` (string)

The type of snapshots to be returned. You can specify one of the following values:

- `automated` - Return all DB snapshots that have been automatically taken by Amazon RDS for my Amazon Web Services account.
- `manual` - Return all DB snapshots that have been taken by my Amazon Web Services account.
- `shared` - Return all manual DB snapshots that have been shared to my Amazon Web Services account.
- `public` - Return all DB snapshots that have been marked as public.
- `awsbackup` - Return the DB snapshots managed by the Amazon Web Services Backup service. For information about Amazon Web Services Backup, see the ` *Amazon Web Services Backup Developer Guide.* [https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup).html`__   The `awsbackup` type does not apply to Aurora.

If you donât specify a `SnapshotType` value, then both automated and manual snapshots are returned. Shared and public DB snapshots are not included in the returned results by default. You can include shared snapshots with these results by enabling the `IncludeShared` parameter. You can include public snapshots with these results by enabling the `IncludePublic` parameter.

The `IncludeShared` and `IncludePublic` parameters donât apply for `SnapshotType` values of `manual` or `automated` . The `IncludePublic` parameter doesnât apply when `SnapshotType` is set to `shared` . The `IncludeShared` parameter doesnât apply when `SnapshotType` is set to `public` .

`--filters` (list)

A filter that specifies one or more DB snapshots to describe.

Supported filters:

- `db-instance-id` - Accepts DB instance identifiers and DB instance Amazon Resource Names (ARNs).
- `db-snapshot-id` - Accepts DB snapshot identifiers.
- `dbi-resource-id` - Accepts identifiers of source DB instances.
- `snapshot-type` - Accepts types of DB snapshots.
- `engine` - Accepts names of database engines.

(structure)

A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.

### Note

Currently, wildcards are not supported in filters.

The following actions can be filtered:

- `DescribeDBClusterBacktracks`
- `DescribeDBClusterEndpoints`
- `DescribeDBClusters`
- `DescribeDBInstances`
- `DescribeDBRecommendations`
- `DescribeDBShardGroups`
- `DescribePendingMaintenanceActions`

Name -> (string)

The name of the filter. Filter names are case-sensitive.

Values -> (list)

One or more filter values. Filter values are case-sensitive.

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

`--include-shared` | `--no-include-shared` (boolean)

Specifies whether to include shared manual DB cluster snapshots from other Amazon Web Services accounts that this Amazon Web Services account has been given permission to copy or restore. By default, these snapshots are not included.

You can give an Amazon Web Services account permission to restore a manual DB snapshot from another Amazon Web Services account by using the `ModifyDBSnapshotAttribute` API action.

This setting doesnât apply to RDS Custom.

`--include-public` | `--no-include-public` (boolean)

Specifies whether to include manual DB cluster snapshots that are public and can be copied or restored by any Amazon Web Services account. By default, the public snapshots are not included.

You can share a manual DB snapshot as public by using the  ModifyDBSnapshotAttribute API.

This setting doesnât apply to RDS Custom.

`--dbi-resource-id` (string)

A specific DB resource ID to describe.

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

**Example 1: To describe a DB snapshot for a DB instance**

The following `describe-db-snapshots` example retrieves the details of a DB snapshot for a DB instance.

```
aws rds describe-db-snapshots \
    --db-snapshot-identifier mydbsnapshot
```

Output:

```
{
    "DBSnapshots": [
        {
            "DBSnapshotIdentifier": "mydbsnapshot",
            "DBInstanceIdentifier": "mysqldb",
            "SnapshotCreateTime": "2018-02-08T22:28:08.598Z",
            "Engine": "mysql",
            "AllocatedStorage": 20,
            "Status": "available",
            "Port": 3306,
            "AvailabilityZone": "us-east-1f",
            "VpcId": "vpc-6594f31c",
            "InstanceCreateTime": "2018-02-08T22:24:55.973Z",
            "MasterUsername": "mysqladmin",
            "EngineVersion": "5.6.37",
            "LicenseModel": "general-public-license",
            "SnapshotType": "manual",
            "OptionGroupName": "default:mysql-5-6",
            "PercentProgress": 100,
            "StorageType": "gp2",
            "Encrypted": false,
            "DBSnapshotArn": "arn:aws:rds:us-east-1:123456789012:snapshot:mydbsnapshot",
            "IAMDatabaseAuthenticationEnabled": false,
            "ProcessorFeatures": [],
            "DbiResourceId": "db-AKIAIOSFODNN7EXAMPLE"
        }
    ]
}
```

For more information, see [Creating a DB Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html) in the *Amazon RDS User Guide*.

**Example 2: To find the number of manual snapshots taken**

The following `describe-db-snapshots` example uses the `length` operator in the `--query` option to return the number of manual snapshots that have been taken in a particular AWS Region.

```
aws rds describe-db-snapshots \
    --snapshot-type manual \
    --query "length(*[].{DBSnapshots:SnapshotType})" \
    --region eu-central-1
```

Output:

```
35
```

For more information, see [Creating a DB Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html) in the *Amazon RDS User Guide*.

## Output

Marker -> (string)

An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords` .

DBSnapshots -> (list)

A list of `DBSnapshot` instances.

(structure)

Contains the details of an Amazon RDS DB snapshot.

This data type is used as a response element in the `DescribeDBSnapshots` action.

DBSnapshotIdentifier -> (string)

Specifies the identifier for the DB snapshot.

DBInstanceIdentifier -> (string)

Specifies the DB instance identifier of the DB instance this DB snapshot was created from.

SnapshotCreateTime -> (timestamp)

Specifies when the snapshot was taken in Coordinated Universal Time (UTC). Changes for the copy when the snapshot is copied.

Engine -> (string)

Specifies the name of the database engine.

AllocatedStorage -> (integer)

Specifies the allocated storage size in gibibytes (GiB).

Status -> (string)

Specifies the status of this DB snapshot.

Port -> (integer)

Specifies the port that the database engine was listening on at the time of the snapshot.

AvailabilityZone -> (string)

Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.

VpcId -> (string)

Provides the VPC ID associated with the DB snapshot.

InstanceCreateTime -> (timestamp)

Specifies the time in Coordinated Universal Time (UTC) when the DB instance, from which the snapshot was taken, was created.

MasterUsername -> (string)

Provides the master username for the DB snapshot.

EngineVersion -> (string)

Specifies the version of the database engine.

LicenseModel -> (string)

License model information for the restored DB instance.

SnapshotType -> (string)

Provides the type of the DB snapshot.

Iops -> (integer)

Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.

OptionGroupName -> (string)

Provides the option group name for the DB snapshot.

PercentProgress -> (integer)

The percentage of the estimated data that has been transferred.

SourceRegion -> (string)

The Amazon Web Services Region that the DB snapshot was created in or copied from.

SourceDBSnapshotIdentifier -> (string)

The DB snapshot Amazon Resource Name (ARN) that the DB snapshot was copied from. It only has a value in the case of a cross-account or cross-Region copy.

StorageType -> (string)

Specifies the storage type associated with DB snapshot.

TdeCredentialArn -> (string)

The ARN from the key store with which to associate the instance for TDE encryption.

Encrypted -> (boolean)

Indicates whether the DB snapshot is encrypted.

KmsKeyId -> (string)

If `Encrypted` is true, the Amazon Web Services KMS key identifier for the encrypted DB snapshot.

The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

DBSnapshotArn -> (string)

The Amazon Resource Name (ARN) for the DB snapshot.

Timezone -> (string)

The time zone of the DB snapshot. In most cases, the `Timezone` element is empty. `Timezone` content appears only for snapshots taken from Microsoft SQL Server DB instances that were created with a time zone specified.

IAMDatabaseAuthenticationEnabled -> (boolean)

Indicates whether mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts is enabled.

ProcessorFeatures -> (list)

The number of CPU cores and the number of threads per core for the DB instance class of the DB instance when the DB snapshot was created.

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

DbiResourceId -> (string)

The identifier for the source DB instance, which canât be changed and which is unique to an Amazon Web Services Region.

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

OriginalSnapshotCreateTime -> (timestamp)

Specifies the time of the CreateDBSnapshot operation in Coordinated Universal Time (UTC). Doesnât change when the snapshot is copied.

SnapshotDatabaseTime -> (timestamp)

The timestamp of the most recent transaction applied to the database that youâre backing up. Thus, if you restore a snapshot, SnapshotDatabaseTime is the most recent transaction in the restored DB instance. In contrast, originalSnapshotCreateTime specifies the system time that the snapshot completed.

If you back up a read replica, you can determine the replica lag by comparing SnapshotDatabaseTime with originalSnapshotCreateTime. For example, if originalSnapshotCreateTime is two hours later than SnapshotDatabaseTime, then the replica lag is two hours.

SnapshotTarget -> (string)

Specifies where manual snapshots are stored: Amazon Web Services Outposts or the Amazon Web Services Region.

StorageThroughput -> (integer)

Specifies the storage throughput for the DB snapshot.

DBSystemId -> (string)

The Oracle system identifier (SID), which is the name of the Oracle database instance that manages your database files. The Oracle SID is also the name of your CDB.

DedicatedLogVolume -> (boolean)

Indicates whether the DB instance has a dedicated log volume (DLV) enabled.

MultiTenant -> (boolean)

Indicates whether the snapshot is of a DB instance using the multi-tenant configuration (TRUE) or the single-tenant configuration (FALSE).