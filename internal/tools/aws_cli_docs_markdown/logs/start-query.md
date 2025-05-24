# start-queryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/start-query.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/start-query.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [logs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/index.html#cli-aws-logs) ]

# start-query

## Description

Starts a query of one or more log groups using CloudWatch Logs Insights. You specify the log groups and time range to query and the query string to use.

For more information, see [CloudWatch Logs Insights Query Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html) .

After you run a query using `StartQuery` , the query results are stored by CloudWatch Logs. You can use [GetQueryResults](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetQueryResults.html) to retrieve the results of a query, using the `queryId` that `StartQuery` returns.

### Note

To specify the log groups to query, a `StartQuery` operation must include one of the following:

- Either exactly one of the following parameters: `logGroupName` , `logGroupNames` , or `logGroupIdentifiers`
- Or the `queryString` must include a `SOURCE` command to select log groups for the query. The `SOURCE` command can select log groups based on log group name prefix, account ID, and log class.  For more information about the `SOURCE` command, see [SOURCE](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Source.html) .

If you have associated a KMS key with the query results in this account, then [StartQuery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html) uses that key to encrypt the results when it stores them. If no key is associated with query results, the query results are encrypted with the default CloudWatch Logs encryption method.

Queries time out after 60 minutes of runtime. If your queries are timing out, reduce the time range being searched or partition your query into a number of queries.

If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account to start a query in a linked source account. For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) . For a cross-account `StartQuery` operation, the query definition must be defined in the monitoring account.

You can have up to 30 concurrent CloudWatch Logs insights queries, including queries that have been added to dashboards.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/StartQuery)

## Synopsis

```
start-query
[--query-language <value>]
[--log-group-name <value>]
[--log-group-names <value>]
[--log-group-identifiers <value>]
--start-time <value>
--end-time <value>
--query-string <value>
[--limit <value>]
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

`--query-language` (string)

Specify the query language to use for this query. The options are Logs Insights QL, OpenSearch PPL, and OpenSearch SQL. For more information about the query languages that CloudWatch Logs supports, see [Supported query languages](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html) .

Possible values:

- `CWLI`
- `SQL`
- `PPL`

`--log-group-name` (string)

The log group on which to perform the query.

### Note

A `StartQuery` operation must include exactly one of the following parameters: `logGroupName` , `logGroupNames` , or `logGroupIdentifiers` . The exception is queries using the OpenSearch Service SQL query language, where you specify the log group names inside the `querystring` instead of here.

`--log-group-names` (list)

The list of log groups to be queried. You can include up to 50 log groups.

### Note

A `StartQuery` operation must include exactly one of the following parameters: `logGroupName` , `logGroupNames` , or `logGroupIdentifiers` . The exception is queries using the OpenSearch Service SQL query language, where you specify the log group names inside the `querystring` instead of here.

(string)

Syntax:

```
"string" "string" ...
```

`--log-group-identifiers` (list)

The list of log groups to query. You can include up to 50 log groups.

You can specify them by the log group name or ARN. If a log group that youâre querying is in a source account and youâre using a monitoring account, you must specify the ARN of the log group here. The query definition must also be defined in the monitoring account.

If you specify an ARN, use the format arn:aws:logs:*region* :*account-id* :log-group:*log_group_name* Donât include an * at the end.

A `StartQuery` operation must include exactly one of the following parameters: `logGroupName` , `logGroupNames` , or `logGroupIdentifiers` . The exception is queries using the OpenSearch Service SQL query language, where you specify the log group names inside the `querystring` instead of here.

(string)

Syntax:

```
"string" "string" ...
```

`--start-time` (long)

The beginning of the time range to query. The range is inclusive, so the specified start time is included in the query. Specified as epoch time, the number of seconds since `January 1, 1970, 00:00:00 UTC` .

`--end-time` (long)

The end of the time range to query. The range is inclusive, so the specified end time is included in the query. Specified as epoch time, the number of seconds since `January 1, 1970, 00:00:00 UTC` .

`--query-string` (string)

The query string to use. For more information, see [CloudWatch Logs Insights Query Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html) .

`--limit` (integer)

The maximum number of log events to return in the query. If the query string uses the `fields` command, only the specified fields and their values are returned. The default is 10,000.

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

queryId -> (string)

The unique ID of the query.