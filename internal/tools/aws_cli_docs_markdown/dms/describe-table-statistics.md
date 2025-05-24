# describe-table-statisticsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-table-statistics.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-table-statistics.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/index.html#cli-aws-dms) ]

# describe-table-statistics

## Description

Returns table statistics on the database migration task, including table name, rows inserted, rows updated, and rows deleted.

Note that the âlast updatedâ column the DMS console only indicates the time that DMS last updated the table statistics record for a table. It does not indicate the time of the last update to the table.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeTableStatistics)

`describe-table-statistics` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `TableStatistics`

## Synopsis

```
describe-table-statistics
--replication-task-arn <value>
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

`--replication-task-arn` (string)

The Amazon Resource Name (ARN) of the replication task.

`--filters` (list)

Filters applied to table statistics.

Valid filter names: schema-name | table-name | table-state

A combination of filters creates an AND condition where each record matches all specified filters.

(structure)

Identifies the name and value of a filter object. This filter is used to limit the number and type of DMS objects that are returned for a particular `Describe*` call or similar operation. Filters are used as an optional parameter for certain API operations.

Name -> (string)

The name of the filter as specified for a `Describe*` or similar operation.

Values -> (list)

The filter value, which can specify one or more values used to narrow the returned results.

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

## Output

ReplicationTaskArn -> (string)

The Amazon Resource Name (ARN) of the replication task.

TableStatistics -> (list)

The table statistics.

(structure)

Provides a collection of table statistics in response to a request by the `DescribeTableStatistics` operation.

SchemaName -> (string)

The schema name.

TableName -> (string)

The name of the table.

Inserts -> (long)

The number of insert actions performed on a table.

Deletes -> (long)

The number of delete actions performed on a table.

Updates -> (long)

The number of update actions performed on a table.

Ddls -> (long)

The data definition language (DDL) used to build and modify the structure of your tables.

AppliedInserts -> (long)

The number of insert actions applied on a target table.

AppliedDeletes -> (long)

The number of delete actions applied on a target table.

AppliedUpdates -> (long)

The number of update actions applied on a target table.

AppliedDdls -> (long)

The number of data definition language (DDL) statements used to build and modify the structure of your tables applied on the target.

FullLoadRows -> (long)

The number of rows added during the full load operation.

FullLoadCondtnlChkFailedRows -> (long)

The number of rows that failed conditional checks during the full load operation (valid only for migrations where DynamoDB is the target).

FullLoadErrorRows -> (long)

The number of rows that failed to load during the full load operation (valid only for migrations where DynamoDB is the target).

FullLoadStartTime -> (timestamp)

The time when the full load operation started.

FullLoadEndTime -> (timestamp)

The time when the full load operation completed.

FullLoadReloaded -> (boolean)

A value that indicates if the table was reloaded (`true` ) or loaded as part of a new full load operation (`false` ).

LastUpdateTime -> (timestamp)

The last time a table was updated.

TableState -> (string)

The state of the tables described.

Valid states: Table does not exist | Before load | Full load | Table completed | Table cancelled | Table error | Table is being reloaded

ValidationPendingRecords -> (long)

The number of records that have yet to be validated.

ValidationFailedRecords -> (long)

The number of records that failed validation.

ValidationSuspendedRecords -> (long)

The number of records that couldnât be validated.

ValidationState -> (string)

The validation state of the table.

This parameter can have the following values:

- Not enabled â Validation isnât enabled for the table in the migration task.
- Pending records â Some records in the table are waiting for validation.
- Mismatched records â Some records in the table donât match between the source and target.
- Suspended records â Some records in the table couldnât be validated.
- No primary key âThe table couldnât be validated because it has no primary key.
- Table error â The table wasnât validated because itâs in an error state and some data wasnât migrated.
- Validated â All rows in the table are validated. If the table is updated, the status can change from Validated.
- Error â The table couldnât be validated because of an unexpected error.
- Pending validation â The table is waiting validation.
- Preparing table â Preparing the table enabled in the migration task for validation.
- Pending revalidation â All rows in the table are pending validation after the table was updated.

ValidationStateDetails -> (string)

Additional details about the state of validation.

ResyncState -> (string)

Records the current state of table resynchronization in the migration task.

This parameter can have the following values:

- Not enabled â Resync is not enabled for the table in the migration task.
- Pending â The tables are waiting for resync.
- In progress â Resync in progress for some records in the table.
- No primary key â The table could not be resynced because it has no primary key.
- Last resync at: `date/time` â Resync session is finished at time. Time provided in UTC format.

ResyncRowsAttempted -> (long)

Records the total number of mismatched data rows where the system attempted to apply fixes in the target database.

ResyncRowsSucceeded -> (long)

Records the total number of mismatched data rows where fixes were successfully applied in the target database.

ResyncRowsFailed -> (long)

Records the total number of mismatched data rows where fix attempts failed in the target database.

ResyncProgress -> (double)

Calculates the percentage of failed validations that were successfully resynced to the system.

Marker -> (string)

An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords` .