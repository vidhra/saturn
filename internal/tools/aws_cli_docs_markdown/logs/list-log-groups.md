# list-log-groupsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/list-log-groups.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/list-log-groups.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [logs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/index.html#cli-aws-logs) ]

# list-log-groups

## Description

Returns a list of log groups in the Region in your account. If you are performing this action in a monitoring account, you can choose to also return log groups from source accounts that are linked to the monitoring account. For more information about using cross-account observability to set up monitoring accounts and source accounts, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) .

You can optionally filter the list by log group class and by using regular expressions in your request to match strings in the log group names.

This operation is paginated. By default, your first use of this operation returns 50 results, and includes a token to use in a subsequent operation to return more results.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/ListLogGroups)

## Synopsis

```
list-log-groups
[--log-group-name-pattern <value>]
[--log-group-class <value>]
[--include-linked-accounts | --no-include-linked-accounts]
[--account-identifiers <value>]
[--next-token <value>]
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

`--log-group-name-pattern` (string)

Use this parameter to limit the returned log groups to only those with names that match the pattern that you specify. This parameter is a regular expression that can match prefixes and substrings, and supports wildcard matching and matching multiple patterns, as in the following examples.

- Use `^` to match log group names by prefix.
- For a substring match, specify the string to match. All matches are case sensitive
- To match multiple patterns, separate them with a `|` as in the example `^/aws/lambda|discovery`

You can specify as many as five different regular expression patterns in this field, each of which must be between 3 and 24 characters. You can include the `^` symbol as many as five times, and include the `|` symbol as many as four times.

`--log-group-class` (string)

Use this parameter to limit the results to only those log groups in the specified log group class. If you omit this parameter, log groups of all classes can be returned.

Possible values:

- `STANDARD`
- `INFREQUENT_ACCESS`
- `DELIVERY`

`--include-linked-accounts` | `--no-include-linked-accounts` (boolean)

If you are using a monitoring account, set this to `true` to have the operation return log groups in the accounts listed in `accountIdentifiers` .

If this parameter is set to `true` and `accountIdentifiers` contains a null value, the operation returns all log groups in the monitoring account and all log groups in all source accounts that are linked to the monitoring account.

The default for this parameter is `false` .

`--account-identifiers` (list)

When `includeLinkedAccounts` is set to `true` , use this parameter to specify the list of accounts to search. You can specify as many as 20 account IDs in the array.

(string)

Syntax:

```
"string" "string" ...
```

`--next-token` (string)

The token for the next set of items to return. The token expires after 24 hours.

`--limit` (integer)

The maximum number of log groups to return. If you omit this parameter, the default is up to 50 log groups.

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

logGroups -> (list)

An array of structures, where each structure contains the information about one log group.

(structure)

This structure contains information about one log group in your account.

logGroupName -> (string)

The name of the log group.

logGroupArn -> (string)

The Amazon Resource Name (ARN) of the log group.

logGroupClass -> (string)

The log group class for this log group. For details about the features supported by each log group class, see [Log classes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html)

nextToken -> (string)

The token for the next set of items to return. The token expires after 24 hours.