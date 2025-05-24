# list-statementsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/list-statements.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/list-statements.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/index.html#cli-aws-redshift-data) ]

# list-statements

## Description

List of SQL statements. By default, only finished statements are shown. A token is returned to page through the statement list.

When you use identity-enhanced role sessions to list statements, you must provide either the `cluster-identifier` or `workgroup-name` parameter. This ensures that the IdC user can only access the Amazon Redshift IdC applications they are assigned. For more information, see [Trusted identity propagation overview](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html) .

For more information about the Amazon Redshift Data API and CLI usage examples, see [Using the Amazon Redshift Data API](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html) in the *Amazon Redshift Management Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-data-2019-12-20/ListStatements)

`list-statements` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Statements`

## Synopsis

```
list-statements
[--cluster-identifier <value>]
[--database <value>]
[--role-level | --no-role-level]
[--statement-name <value>]
[--status <value>]
[--workgroup-name <value>]
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

`--cluster-identifier` (string)

The cluster identifier. Only statements that ran on this cluster are returned. When providing `ClusterIdentifier` , then `WorkgroupName` canât be specified.

`--database` (string)

The name of the database when listing statements run against a `ClusterIdentifier` or `WorkgroupName` .

`--role-level` | `--no-role-level` (boolean)

A value that filters which statements to return in the response. If true, all statements run by the callerâs IAM role are returned. If false, only statements run by the callerâs IAM role in the current IAM session are returned. The default is true.

`--statement-name` (string)

The name of the SQL statement specified as input to `BatchExecuteStatement` or `ExecuteStatement` to identify the query. You can list multiple statements by providing a prefix that matches the beginning of the statement name. For example, to list myStatement1, myStatement2, myStatement3, and so on, then provide the a value of `myStatement` . Data API does a case-sensitive match of SQL statement names to the prefix value you provide.

`--status` (string)

The status of the SQL statement to list. Status values are defined as follows:

- ABORTED - The query run was stopped by the user.
- ALL - A status value that includes all query statuses. This value can be used to filter results.
- FAILED - The query run failed.
- FINISHED - The query has finished running.
- PICKED - The query has been chosen to be run.
- STARTED - The query run has started.
- SUBMITTED - The query was submitted, but not yet processed.

Possible values:

- `SUBMITTED`
- `PICKED`
- `STARTED`
- `FINISHED`
- `ABORTED`
- `FAILED`
- `ALL`

`--workgroup-name` (string)

The serverless workgroup name or Amazon Resource Name (ARN). Only statements that ran on this workgroup are returned. When providing `WorkgroupName` , then `ClusterIdentifier` canât be specified.

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

NextToken -> (string)

A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request.

Statements -> (list)

The SQL statements.

(structure)

The SQL statement to run.

CreatedAt -> (timestamp)

The date and time (UTC) the statement was created.

Id -> (string)

The SQL statement identifier. This value is a universally unique identifier (UUID) generated by Amazon Redshift Data API.

IsBatchStatement -> (boolean)

A value that indicates whether the statement is a batch query request.

QueryParameters -> (list)

The parameters used in a SQL statement.

(structure)

A parameter used in a SQL statement.

name -> (string)

The name of the parameter.

value -> (string)

The value of the parameter. Amazon Redshift implicitly converts to the proper data type. For more information, see [Data types](https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html) in the *Amazon Redshift Database Developer Guide* .

QueryString -> (string)

The SQL statement.

QueryStrings -> (list)

One or more SQL statements. Each query string in the array corresponds to one of the queries in a batch query request.

(string)

ResultFormat -> (string)

The data format of the result of the SQL statement.

SecretArn -> (string)

The name or Amazon Resource Name (ARN) of the secret that enables access to the database.

SessionId -> (string)

The session identifier of the query.

StatementName -> (string)

The name of the SQL statement.

Status -> (string)

The status of the SQL statement. An example is the that the SQL statement finished.

UpdatedAt -> (timestamp)

The date and time (UTC) that the statement metadata was last updated.