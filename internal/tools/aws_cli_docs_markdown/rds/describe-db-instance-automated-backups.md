# describe-db-instance-automated-backupsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-instance-automated-backups.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-instance-automated-backups.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# describe-db-instance-automated-backups

## Description

Displays backups for both current and deleted instances. For example, use this operation to find details about automated backups for previously deleted instances. Current instances with retention periods greater than zero (0) are returned for both the `DescribeDBInstanceAutomatedBackups` and `DescribeDBInstances` operations.

All parameters are optional.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBInstanceAutomatedBackups)

`describe-db-instance-automated-backups` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `DBInstanceAutomatedBackups`

## Synopsis

```
describe-db-instance-automated-backups
[--dbi-resource-id <value>]
[--db-instance-identifier <value>]
[--filters <value>]
[--db-instance-automated-backups-arn <value>]
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

`--dbi-resource-id` (string)

The resource ID of the DB instance that is the source of the automated backup. This parameter isnât case-sensitive.

`--db-instance-identifier` (string)

(Optional) The user-supplied instance identifier. If this parameter is specified, it must match the identifier of an existing DB instance. It returns information from the specific DB instanceâs automated backup. This parameter isnât case-sensitive.

`--filters` (list)

A filter that specifies which resources to return based on status.

Supported filters are the following:

- `status`
- `active` - Automated backups for current instances.
- `creating` - Automated backups that are waiting for the first automated snapshot to be available.
- `retained` - Automated backups for deleted instances and after backup replication is stopped.
- `db-instance-id` - Accepts DB instance identifiers and Amazon Resource Names (ARNs). The results list includes only information about the DB instance automated backups identified by these ARNs.
- `dbi-resource-id` - Accepts DB resource identifiers and Amazon Resource Names (ARNs). The results list includes only information about the DB instance resources identified by these ARNs.

Returns all resources by default. The status for each resource is specified in the response.

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

`--db-instance-automated-backups-arn` (string)

The Amazon Resource Name (ARN) of the replicated automated backups, for example, `arn:aws:rds:us-east-1:123456789012:auto-backup:ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE` .

This setting doesnât apply to RDS Custom.

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

**To describe the automated backups for a DB instance**

The following `describe-db-instance-automated-backups` example displays details about the automated backups for the specified DB instance. The details include replicated automated backups in other AWS Regions.

```
aws rds describe-db-instance-automated-backups \
    --db-instance-identifier new-orcl-db
```

Output:

```
{
    "DBInstanceAutomatedBackups": [
        {
            "DBInstanceArn": "arn:aws:rds:us-east-1:123456789012:db:new-orcl-db",
            "DbiResourceId": "db-JKIB2GFQ5RV7REPLZA4EXAMPLE",
            "Region": "us-east-1",
            "DBInstanceIdentifier": "new-orcl-db",
            "RestoreWindow": {
                "EarliestTime": "2020-12-07T21:05:20.939Z",
                "LatestTime": "2020-12-07T21:05:20.939Z"
            },
            "AllocatedStorage": 20,
            "Status": "replicating",
            "Port": 1521,
            "InstanceCreateTime": "2020-12-04T15:28:31Z",
            "MasterUsername": "admin",
            "Engine": "oracle-se2",
            "EngineVersion": "12.1.0.2.v21",
            "LicenseModel": "bring-your-own-license",
            "OptionGroupName": "default:oracle-se2-12-1",
            "Encrypted": false,
            "StorageType": "gp2",
            "IAMDatabaseAuthenticationEnabled": false,
            "BackupRetentionPeriod": 14,
            "DBInstanceAutomatedBackupsArn": "arn:aws:rds:us-west-2:123456789012:auto-backup:ab-jkib2gfq5rv7replzadausbrktni2bn4example"
        }
    ]
}
```

For more information, see [Finding information about replicated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html#AutomatedBackups.Replicating.Describe) in the *Amazon RDS User Guide*.

## Output

Marker -> (string)

An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords` .

DBInstanceAutomatedBackups -> (list)

A list of `DBInstanceAutomatedBackup` instances.

(structure)

An automated backup of a DB instance. It consists of system backups, transaction logs, and the database instance properties that existed at the time you deleted the source instance.

DBInstanceArn -> (string)

The Amazon Resource Name (ARN) for the automated backups.

DbiResourceId -> (string)

The resource ID for the source DB instance, which canât be changed and which is unique to an Amazon Web Services Region.

Region -> (string)

The Amazon Web Services Region associated with the automated backup.

DBInstanceIdentifier -> (string)

The identifier for the source DB instance, which canât be changed and which is unique to an Amazon Web Services Region.

RestoreWindow -> (structure)

The earliest and latest time a DB instance can be restored to.

EarliestTime -> (timestamp)

The earliest time you can restore an instance to.

LatestTime -> (timestamp)

The latest time you can restore an instance to.

AllocatedStorage -> (integer)

The allocated storage size for the the automated backup in gibibytes (GiB).

Status -> (string)

A list of status information for an automated backup:

- `active` - Automated backups for current instances.
- `retained` - Automated backups for deleted instances.
- `creating` - Automated backups that are waiting for the first automated snapshot to be available.

Port -> (integer)

The port number that the automated backup used for connections.

Default: Inherits from the source DB instance

Valid Values: `1150-65535`

AvailabilityZone -> (string)

The Availability Zone that the automated backup was created in. For information on Amazon Web Services Regions and Availability Zones, see [Regions and Availability Zones](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html) .

VpcId -> (string)

The VPC ID associated with the DB instance.

InstanceCreateTime -> (timestamp)

The date and time when the DB instance was created.

MasterUsername -> (string)

The master user name of an automated backup.

Engine -> (string)

The name of the database engine for this automated backup.

EngineVersion -> (string)

The version of the database engine for the automated backup.

LicenseModel -> (string)

The license model information for the automated backup.

Iops -> (integer)

The IOPS (I/O operations per second) value for the automated backup.

OptionGroupName -> (string)

The option group the automated backup is associated with. If omitted, the default option group for the engine specified is used.

TdeCredentialArn -> (string)

The ARN from the key store with which the automated backup is associated for TDE encryption.

Encrypted -> (boolean)

Indicates whether the automated backup is encrypted.

StorageType -> (string)

The storage type associated with the automated backup.

KmsKeyId -> (string)

The Amazon Web Services KMS key ID for an automated backup.

The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

Timezone -> (string)

The time zone of the automated backup. In most cases, the `Timezone` element is empty. `Timezone` content appears only for Microsoft SQL Server DB instances that were created with a time zone specified.

IAMDatabaseAuthenticationEnabled -> (boolean)

True if mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.

BackupRetentionPeriod -> (integer)

The retention period for the automated backups.

DBInstanceAutomatedBackupsArn -> (string)

The Amazon Resource Name (ARN) for the replicated automated backups.

DBInstanceAutomatedBackupsReplications -> (list)

The list of replications to different Amazon Web Services Regions associated with the automated backup.

(structure)

Automated backups of a DB instance replicated to another Amazon Web Services Region. They consist of system backups, transaction logs, and database instance properties.

DBInstanceAutomatedBackupsArn -> (string)

The Amazon Resource Name (ARN) of the replicated automated backups.

BackupTarget -> (string)

The location where automated backups are stored: Amazon Web Services Outposts or the Amazon Web Services Region.

StorageThroughput -> (integer)

The storage throughput for the automated backup.

AwsBackupRecoveryPointArn -> (string)

The Amazon Resource Name (ARN) of the recovery point in Amazon Web Services Backup.

DedicatedLogVolume -> (boolean)

Indicates whether the DB instance has a dedicated log volume (DLV) enabled.

MultiTenant -> (boolean)

Specifies whether the automatic backup is for a DB instance in the multi-tenant configuration (TRUE) or the single-tenant configuration (FALSE).