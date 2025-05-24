# start-export-taskÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/start-export-task.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/start-export-task.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# start-export-task

## Description

Starts an export of DB snapshot or DB cluster data to Amazon S3. The provided IAM role must have access to the S3 bucket.

You canât export snapshot data from RDS Custom DB instances. For more information, see [Supported Regions and DB engines for exporting snapshots to S3 in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.html) .

For more information on exporting DB snapshot data, see [Exporting DB snapshot data to Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.html) in the *Amazon RDS User Guide* or [Exporting DB cluster snapshot data to Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-export-snapshot.html) in the *Amazon Aurora User Guide* .

For more information on exporting DB cluster data, see [Exporting DB cluster data to Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/export-cluster-data.html) in the *Amazon Aurora User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/StartExportTask)

## Synopsis

```
start-export-task
--export-task-identifier <value>
--source-arn <value>
--s3-bucket-name <value>
--iam-role-arn <value>
--kms-key-id <value>
[--s3-prefix <value>]
[--export-only <value>]
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

`--export-task-identifier` (string)

A unique identifier for the export task. This ID isnât an identifier for the Amazon S3 bucket where the data is to be exported.

`--source-arn` (string)

The Amazon Resource Name (ARN) of the snapshot or cluster to export to Amazon S3.

`--s3-bucket-name` (string)

The name of the Amazon S3 bucket to export the snapshot or cluster data to.

`--iam-role-arn` (string)

The name of the IAM role to use for writing to the Amazon S3 bucket when exporting a snapshot or cluster.

In the IAM policy attached to your IAM role, include the following required actions to allow the transfer of files from Amazon RDS or Amazon Aurora to an S3 bucket:

- s3:PutObject*
- s3:GetObject*
- s3:ListBucket
- s3:DeleteObject*
- s3:GetBucketLocation

In the policy, include the resources to identify the S3 bucket and objects in the bucket. The following list of resources shows the Amazon Resource Name (ARN) format for accessing S3:

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/start-export-task.html#id1)arn:aws:s3:::*your-s3-bucket* ``
- `arn:aws:s3:::*your-s3-bucket* /*`

`--kms-key-id` (string)

The ID of the Amazon Web Services KMS key to use to encrypt the data exported to Amazon S3. The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. The caller of this operation must be authorized to run the following operations. These can be set in the Amazon Web Services KMS key policy:

- kms:CreateGrant
- kms:DescribeKey

`--s3-prefix` (string)

The Amazon S3 bucket prefix to use as the file name and path of the exported data.

`--export-only` (list)

The data to be exported from the snapshot or cluster. If this parameter isnât provided, all of the data is exported.

Valid Values:

- `database` - Export all the data from a specified database.
- `database.table` *table-name* - Export a table of the snapshot or cluster. This format is valid only for RDS for MySQL, RDS for MariaDB, and Aurora MySQL.
- `database.schema` *schema-name* - Export a database schema of the snapshot or cluster. This format is valid only for RDS for PostgreSQL and Aurora PostgreSQL.
- `database.schema.table` *table-name* - Export a table of the database schema. This format is valid only for RDS for PostgreSQL and Aurora PostgreSQL.

(string)

Syntax:

```
"string" "string" ...
```

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

**To export a snapshot to Amazon S3**

The following `start-export-task` example exports a DB snapshot named `db5-snapshot-test` to the Amazon S3 bucket named `amzn-s3-demo-bucket`.

```
aws rds start-export-task \
    --export-task-identifier my-s3-export \
    --source-arn arn:aws:rds:us-west-2:123456789012:snapshot:db5-snapshot-test \
    --s3-bucket-name amzn-s3-demo-bucket \
    --iam-role-arn arn:aws:iam::123456789012:role/service-role/ExportRole \
    --kms-key-id arn:aws:kms:us-west-2:123456789012:key/abcd0000-7fca-4128-82f2-aabbccddeeff
```

Output:

```
{
    "ExportTaskIdentifier": "my-s3-export",
    "SourceArn": "arn:aws:rds:us-west-2:123456789012:snapshot:db5-snapshot-test",
    "SnapshotTime": "2020-03-27T20:48:42.023Z",
    "S3Bucket": "amzn-s3-demo-bucket",
    "IamRoleArn": "arn:aws:iam::123456789012:role/service-role/ExportRole",
    "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/abcd0000-7fca-4128-82f2-aabbccddeeff",
    "Status": "STARTING",
    "PercentProgress": 0,
    "TotalExtractedDataInGB": 0
}
```

For more information, see [Exporting a Snapshot to an Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.html#USER_ExportSnapshot.Exporting) in the *Amazon RDS User Guide*.

## Output

ExportTaskIdentifier -> (string)

A unique identifier for the snapshot or cluster export task. This ID isnât an identifier for the Amazon S3 bucket where the data is exported.

SourceArn -> (string)

The Amazon Resource Name (ARN) of the snapshot or cluster exported to Amazon S3.

ExportOnly -> (list)

The data exported from the snapshot or cluster.

Valid Values:

- `database` - Export all the data from a specified database.
- `database.table` *table-name* - Export a table of the snapshot or cluster. This format is valid only for RDS for MySQL, RDS for MariaDB, and Aurora MySQL.
- `database.schema` *schema-name* - Export a database schema of the snapshot or cluster. This format is valid only for RDS for PostgreSQL and Aurora PostgreSQL.
- `database.schema.table` *table-name* - Export a table of the database schema. This format is valid only for RDS for PostgreSQL and Aurora PostgreSQL.

(string)

SnapshotTime -> (timestamp)

The time when the snapshot was created.

TaskStartTime -> (timestamp)

The time when the snapshot or cluster export task started.

TaskEndTime -> (timestamp)

The time when the snapshot or cluster export task ended.

S3Bucket -> (string)

The Amazon S3 bucket where the snapshot or cluster is exported to.

S3Prefix -> (string)

The Amazon S3 bucket prefix that is the file name and path of the exported data.

IamRoleArn -> (string)

The name of the IAM role that is used to write to Amazon S3 when exporting a snapshot or cluster.

KmsKeyId -> (string)

The key identifier of the Amazon Web Services KMS key that is used to encrypt the data when itâs exported to Amazon S3. The KMS key identifier is its key ARN, key ID, alias ARN, or alias name. The IAM role used for the export must have encryption and decryption permissions to use this KMS key.

Status -> (string)

The progress status of the export task. The status can be one of the following:

- `CANCELED`
- `CANCELING`
- `COMPLETE`
- `FAILED`
- `IN_PROGRESS`
- `STARTING`

PercentProgress -> (integer)

The progress of the snapshot or cluster export task as a percentage.

TotalExtractedDataInGB -> (integer)

The total amount of data exported, in gigabytes.

FailureCause -> (string)

The reason the export failed, if it failed.

WarningMessage -> (string)

A warning about the snapshot or cluster export task.

SourceType -> (string)

The type of source for the export.