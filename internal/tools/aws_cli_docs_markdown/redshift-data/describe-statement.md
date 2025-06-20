# describe-statementÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/describe-statement.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/describe-statement.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/index.html#cli-aws-redshift-data) ]

# describe-statement

## Description

Describes the details about a specific instance when a query was run by the Amazon Redshift Data API. The information includes when the query started, when it finished, the query status, the number of rows returned, and the SQL statement.

For more information about the Amazon Redshift Data API and CLI usage examples, see [Using the Amazon Redshift Data API](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html) in the *Amazon Redshift Management Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-data-2019-12-20/DescribeStatement)

## Synopsis

```
describe-statement
--id <value>
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

`--id` (string)

The identifier of the SQL statement to describe. This value is a universally unique identifier (UUID) generated by Amazon Redshift Data API. A suffix indicates the number of the SQL statement. For example, `d9b6c0c9-0747-4bf4-b142-e8883122f766:2` has a suffix of `:2` that indicates the second SQL statement of a batch query. This identifier is returned by `BatchExecuteStatment` , `ExecuteStatement` , and `ListStatements` .

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

ClusterIdentifier -> (string)

The cluster identifier.

CreatedAt -> (timestamp)

The date and time (UTC) when the SQL statement was submitted to run.

Database -> (string)

The name of the database.

DbUser -> (string)

The database user name.

Duration -> (long)

The amount of time in nanoseconds that the statement ran.

Error -> (string)

The error message from the cluster if the SQL statement encountered an error while running.

HasResultSet -> (boolean)

A value that indicates whether the statement has a result set. The result set can be empty. The value is true for an empty result set. The value is true if any substatement returns a result set.

Id -> (string)

The identifier of the SQL statement described. This value is a universally unique identifier (UUID) generated by Amazon Redshift Data API.

QueryParameters -> (list)

The parameters for the SQL statement.

(structure)

A parameter used in a SQL statement.

name -> (string)

The name of the parameter.

value -> (string)

The value of the parameter. Amazon Redshift implicitly converts to the proper data type. For more information, see [Data types](https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html) in the *Amazon Redshift Database Developer Guide* .

QueryString -> (string)

The SQL statement text.

RedshiftPid -> (long)

The process identifier from Amazon Redshift.

RedshiftQueryId -> (long)

The identifier of the query generated by Amazon Redshift. These identifiers are also available in the `query` column of the `STL_QUERY` system view.

ResultFormat -> (string)

The data format of the result of the SQL statement.

ResultRows -> (long)

Either the number of rows returned from the SQL statement or the number of rows affected. If result size is greater than zero, the result rows can be the number of rows affected by SQL statements such as INSERT, UPDATE, DELETE, COPY, and others. A `-1` indicates the value is null.

ResultSize -> (long)

The size in bytes of the returned results. A `-1` indicates the value is null.

SecretArn -> (string)

The name or Amazon Resource Name (ARN) of the secret that enables access to the database.

SessionId -> (string)

The session identifier of the query.

Status -> (string)

The status of the SQL statement being described. Status values are defined as follows:

- ABORTED - The query run was stopped by the user.
- ALL - A status value that includes all query statuses. This value can be used to filter results.
- FAILED - The query run failed.
- FINISHED - The query has finished running.
- PICKED - The query has been chosen to be run.
- STARTED - The query run has started.
- SUBMITTED - The query was submitted, but not yet processed.

SubStatements -> (list)

The SQL statements from a multiple statement run.

(structure)

Information about an SQL statement.

CreatedAt -> (timestamp)

The date and time (UTC) the statement was created.

Duration -> (long)

The amount of time in nanoseconds that the statement ran.

Error -> (string)

The error message from the cluster if the SQL statement encountered an error while running.

HasResultSet -> (boolean)

A value that indicates whether the statement has a result set. The result set can be empty. The value is true for an empty result set.

Id -> (string)

The identifier of the SQL statement. This value is a universally unique identifier (UUID) generated by Amazon Redshift Data API. A suffix indicates the number of the SQL statement. For example, `d9b6c0c9-0747-4bf4-b142-e8883122f766:2` has a suffix of `:2` that indicates the second SQL statement of a batch query.

QueryString -> (string)

The SQL statement text.

RedshiftQueryId -> (long)

The SQL statement identifier. This value is a universally unique identifier (UUID) generated by Amazon Redshift Data API.

ResultRows -> (long)

Either the number of rows returned from the SQL statement or the number of rows affected. If result size is greater than zero, the result rows can be the number of rows affected by SQL statements such as INSERT, UPDATE, DELETE, COPY, and others. A `-1` indicates the value is null.

ResultSize -> (long)

The size in bytes of the returned results. A `-1` indicates the value is null.

Status -> (string)

The status of the SQL statement. An example is the that the SQL statement finished.

UpdatedAt -> (timestamp)

The date and time (UTC) that the statement metadata was last updated.

UpdatedAt -> (timestamp)

The date and time (UTC) that the metadata for the SQL statement was last updated. An example is the time the status last changed.

WorkgroupName -> (string)

The serverless workgroup name or Amazon Resource Name (ARN).