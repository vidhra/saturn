# copy-db-snapshotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-db-snapshot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-db-snapshot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# copy-db-snapshot

## Description

Copies the specified DB snapshot. The source DB snapshot must be in the `available` state.

You can copy a snapshot from one Amazon Web Services Region to another. In that case, the Amazon Web Services Region where you call the `CopyDBSnapshot` operation is the destination Amazon Web Services Region for the DB snapshot copy.

This command doesnât apply to RDS Custom.

For more information about copying snapshots, see [Copying a DB Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html#USER_CopyDBSnapshot) in the *Amazon RDS User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/CopyDBSnapshot)

## Synopsis

```
copy-db-snapshot
--source-db-snapshot-identifier <value>
--target-db-snapshot-identifier <value>
[--kms-key-id <value>]
[--tags <value>]
[--copy-tags | --no-copy-tags]
[--pre-signed-url <value>]
[--option-group-name <value>]
[--target-custom-availability-zone <value>]
[--copy-option-group | --no-copy-option-group]
[--source-region <value>]
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

`--source-db-snapshot-identifier` (string)

The identifier for the source DB snapshot.

If the source snapshot is in the same Amazon Web Services Region as the copy, specify a valid DB snapshot identifier. For example, you might specify `rds:mysql-instance1-snapshot-20130805` .

If the source snapshot is in a different Amazon Web Services Region than the copy, specify a valid DB snapshot ARN. For example, you might specify `arn:aws:rds:us-west-2:123456789012:snapshot:mysql-instance1-snapshot-20130805` .

If you are copying from a shared manual DB snapshot, this parameter must be the Amazon Resource Name (ARN) of the shared DB snapshot.

If you are copying an encrypted snapshot this parameter must be in the ARN format for the source Amazon Web Services Region.

Constraints:

- Must specify a valid system snapshot in the âavailableâ state.

Example: `rds:mydb-2012-04-02-00-01`

Example: `arn:aws:rds:us-west-2:123456789012:snapshot:mysql-instance1-snapshot-20130805`

`--target-db-snapshot-identifier` (string)

The identifier for the copy of the snapshot.

Constraints:

- Canât be null, empty, or blank
- Must contain from 1 to 255 letters, numbers, or hyphens
- First character must be a letter
- Canât end with a hyphen or contain two consecutive hyphens

Example: `my-db-snapshot`

`--kms-key-id` (string)

The Amazon Web Services KMS key identifier for an encrypted DB snapshot. The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

If you copy an encrypted DB snapshot from your Amazon Web Services account, you can specify a value for this parameter to encrypt the copy with a new KMS key. If you donât specify a value for this parameter, then the copy of the DB snapshot is encrypted with the same Amazon Web Services KMS key as the source DB snapshot.

If you copy an encrypted DB snapshot that is shared from another Amazon Web Services account, then you must specify a value for this parameter.

If you specify this parameter when you copy an unencrypted snapshot, the copy is encrypted.

If you copy an encrypted snapshot to a different Amazon Web Services Region, then you must specify an Amazon Web Services KMS key identifier for the destination Amazon Web Services Region. KMS keys are specific to the Amazon Web Services Region that they are created in, and you canât use KMS keys from one Amazon Web Services Region in another Amazon Web Services Region.

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

`--copy-tags` | `--no-copy-tags` (boolean)

Specifies whether to copy all tags from the source DB snapshot to the target DB snapshot. By default, tags arenât copied.

`--pre-signed-url` (string)

When you are copying a snapshot from one Amazon Web Services GovCloud (US) Region to another, the URL that contains a Signature Version 4 signed request for the `CopyDBSnapshot` API operation in the source Amazon Web Services Region that contains the source DB snapshot to copy.

This setting applies only to Amazon Web Services GovCloud (US) Regions. Itâs ignored in other Amazon Web Services Regions.

You must specify this parameter when you copy an encrypted DB snapshot from another Amazon Web Services Region by using the Amazon RDS API. Donât specify `PreSignedUrl` when you are copying an encrypted DB snapshot in the same Amazon Web Services Region.

The presigned URL must be a valid request for the `CopyDBClusterSnapshot` API operation that can run in the source Amazon Web Services Region that contains the encrypted DB cluster snapshot to copy. The presigned URL request must contain the following parameter values:

- `DestinationRegion` - The Amazon Web Services Region that the encrypted DB snapshot is copied to. This Amazon Web Services Region is the same one where the `CopyDBSnapshot` operation is called that contains this presigned URL. For example, if you copy an encrypted DB snapshot from the us-west-2 Amazon Web Services Region to the us-east-1 Amazon Web Services Region, then you call the `CopyDBSnapshot` operation in the us-east-1 Amazon Web Services Region and provide a presigned URL that contains a call to the `CopyDBSnapshot` operation in the us-west-2 Amazon Web Services Region. For this example, the `DestinationRegion` in the presigned URL must be set to the us-east-1 Amazon Web Services Region.
- `KmsKeyId` - The KMS key identifier for the KMS key to use to encrypt the copy of the DB snapshot in the destination Amazon Web Services Region. This is the same identifier for both the `CopyDBSnapshot` operation that is called in the destination Amazon Web Services Region, and the operation contained in the presigned URL.
- `SourceDBSnapshotIdentifier` - The DB snapshot identifier for the encrypted snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source Amazon Web Services Region. For example, if you are copying an encrypted DB snapshot from the us-west-2 Amazon Web Services Region, then your `SourceDBSnapshotIdentifier` looks like the following example: `arn:aws:rds:us-west-2:123456789012:snapshot:mysql-instance1-snapshot-20161115` .

To learn how to generate a Signature Version 4 signed request, see [Authenticating Requests: Using Query Parameters (Amazon Web Services Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html) and [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) .

### Note

If you are using an Amazon Web Services SDK tool or the CLI, you can specify `SourceRegion` (or `--source-region` for the CLI) instead of specifying `PreSignedUrl` manually. Specifying `SourceRegion` autogenerates a presigned URL that is a valid request for the operation that can run in the source Amazon Web Services Region.

`--option-group-name` (string)

The name of an option group to associate with the copy of the snapshot.

Specify this option if you are copying a snapshot from one Amazon Web Services Region to another, and your DB instance uses a nondefault option group. If your source DB instance uses Transparent Data Encryption for Oracle or Microsoft SQL Server, you must specify this option when copying across Amazon Web Services Regions. For more information, see [Option group considerations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html#USER_CopySnapshot.Options) in the *Amazon RDS User Guide* .

`--target-custom-availability-zone` (string)

The external custom Availability Zone (CAZ) identifier for the target CAZ.

Example: `rds-caz-aiqhTgQv` .

`--copy-option-group` | `--no-copy-option-group` (boolean)

Specifies whether to copy the DB option group associated with the source DB snapshot to the target Amazon Web Services account and associate with the target DB snapshot. The associated option group can be copied only with cross-account snapshot copy calls.

`--source-region` (string)

The ID of the region that contains the snapshot to be copied.

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

**To copy a DB snapshot**

The following `copy-db-snapshot` example creates a copy of a DB snapshot.

```
aws rds copy-db-snapshot \
    --source-db-snapshot-identifier rds:database-mysql-2019-06-06-08-38
    --target-db-snapshot-identifier mydbsnapshotcopy
```

Output:

```
{
    "DBSnapshot": {
        "VpcId": "vpc-6594f31c",
        "Status": "creating",
        "Encrypted": true,
        "SourceDBSnapshotIdentifier": "arn:aws:rds:us-east-1:123456789012:snapshot:rds:database-mysql-2019-06-06-08-38",
        "MasterUsername": "admin",
        "Iops": 1000,
        "Port": 3306,
        "LicenseModel": "general-public-license",
        "DBSnapshotArn": "arn:aws:rds:us-east-1:123456789012:snapshot:mydbsnapshotcopy",
        "EngineVersion": "5.6.40",
        "OptionGroupName": "default:mysql-5-6",
        "ProcessorFeatures": [],
        "Engine": "mysql",
        "StorageType": "io1",
        "DbiResourceId": "db-ZI7UJ5BLKMBYFGX7FDENCKADC4",
        "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/AKIAIOSFODNN7EXAMPLE",
        "SnapshotType": "manual",
        "IAMDatabaseAuthenticationEnabled": false,
        "SourceRegion": "us-east-1",
        "DBInstanceIdentifier": "database-mysql",
        "InstanceCreateTime": "2019-04-30T15:45:53.663Z",
        "AvailabilityZone": "us-east-1f",
        "PercentProgress": 0,
        "AllocatedStorage": 100,
        "DBSnapshotIdentifier": "mydbsnapshotcopy"
    }
}
```

For more information, see [Copying a Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html) in the *Amazon RDS User Guide*.

## Output

DBSnapshot -> (structure)

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