# describe-db-snapshot-tenant-databasesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-snapshot-tenant-databases.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-snapshot-tenant-databases.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# describe-db-snapshot-tenant-databases

## Description

Describes the tenant databases that exist in a DB snapshot. This command only applies to RDS for Oracle DB instances in the multi-tenant configuration.

You can use this command to inspect the tenant databases within a snapshot before restoring it. You canât directly interact with the tenant databases in a DB snapshot. If you restore a snapshot that was taken from DB instance using the multi-tenant configuration, you restore all its tenant databases.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBSnapshotTenantDatabases)

`describe-db-snapshot-tenant-databases` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `DBSnapshotTenantDatabases`

## Synopsis

```
describe-db-snapshot-tenant-databases
[--db-instance-identifier <value>]
[--db-snapshot-identifier <value>]
[--snapshot-type <value>]
[--filters <value>]
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

The ID of the DB instance used to create the DB snapshots. This parameter isnât case-sensitive.

Constraints:

- If supplied, must match the identifier of an existing `DBInstance` .

`--db-snapshot-identifier` (string)

The ID of a DB snapshot that contains the tenant databases to describe. This value is stored as a lowercase string.

Constraints:

- If you specify this parameter, the value must match the ID of an existing DB snapshot.
- If you specify an automatic snapshot, you must also specify `SnapshotType` .

`--snapshot-type` (string)

The type of DB snapshots to be returned. You can specify one of the following values:

- `automated` â All DB snapshots that have been automatically taken by Amazon RDS for my Amazon Web Services account.
- `manual` â All DB snapshots that have been taken by my Amazon Web Services account.
- `shared` â All manual DB snapshots that have been shared to my Amazon Web Services account.
- `public` â All DB snapshots that have been marked as public.
- `awsbackup` â All DB snapshots managed by the Amazon Web Services Backup service.

`--filters` (list)

A filter that specifies one or more tenant databases to describe.

Supported filters:

- `tenant-db-name` - Tenant database names. The results list only includes information about the tenant databases that match these tenant DB names.
- `tenant-database-resource-id` - Tenant database resource identifiers. The results list only includes information about the tenant databases contained within the DB snapshots.
- `dbi-resource-id` - DB instance resource identifiers. The results list only includes information about snapshots containing tenant databases contained within the DB instances identified by these resource identifiers.
- `db-instance-id` - Accepts DB instance identifiers and DB instance Amazon Resource Names (ARNs).
- `db-snapshot-id` - Accepts DB snapshot identifiers.
- `snapshot-type` - Accepts types of DB snapshots.

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

`--dbi-resource-id` (string)

A specific DB resource identifier to describe.

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

## Output

Marker -> (string)

An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords` .

DBSnapshotTenantDatabases -> (list)

A list of DB snapshot tenant databases.

(structure)

Contains the details of a tenant database in a snapshot of a DB instance.

DBSnapshotIdentifier -> (string)

The identifier for the snapshot of the DB instance.

DBInstanceIdentifier -> (string)

The ID for the DB instance that contains the tenant databases.

DbiResourceId -> (string)

The resource identifier of the source CDB instance. This identifier canât be changed and is unique to an Amazon Web Services Region.

EngineName -> (string)

The name of the database engine.

SnapshotType -> (string)

The type of DB snapshot.

TenantDatabaseCreateTime -> (timestamp)

The time the DB snapshot was taken, specified in Coordinated Universal Time (UTC). If you copy the snapshot, the creation time changes.

TenantDBName -> (string)

The name of the tenant database.

MasterUsername -> (string)

The master username of the tenant database.

TenantDatabaseResourceId -> (string)

The resource ID of the tenant database.

CharacterSetName -> (string)

The name of the character set of a tenant database.

DBSnapshotTenantDatabaseARN -> (string)

The Amazon Resource Name (ARN) for the snapshot tenant database.

NcharCharacterSetName -> (string)

The `NCHAR` character set name of the tenant database.

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